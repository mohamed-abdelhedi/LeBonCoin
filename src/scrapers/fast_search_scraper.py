"""
Fast Search Page Scraper
Extracts data ONLY from search results page (no individual ad visits)
- Much faster (5-10x speed increase)
- Less API calls = safer from blocking
- Prices visible on search page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
import random
from datetime import datetime
from .base_scraper import BaseScraper

class FastSearchScraper(BaseScraper):
    """Fast scraper - extracts data from search results only"""
    
    def __init__(self, headless=True, min_delay=2.0, max_delay=4.0, proxy=None):
        """
        Initialize Fast Search scraper
        
        Args:
            headless (bool): Run browser in headless mode
            min_delay (float): Minimum delay between page loads
            max_delay (float): Maximum delay between page loads
            proxy (str): Proxy string (format: ip:port or user:pass@ip:port)
        """
        super().__init__(min_delay, max_delay)
        self.headless = headless
        self.proxy = proxy
        self.driver = None
        self.base_url = "https://www.leboncoin.fr"
        self._init_driver()
    
    def _init_driver(self):
        """Initialize Chrome WebDriver"""
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless=new")
            
            # Add proxy if provided
            if self.proxy:
                # Convert proxy format for Selenium
                # Expected: IP:PORT or http://IP:PORT
                proxy_str = self.proxy.strip()
                if not proxy_str.startswith('http://') and not proxy_str.startswith('https://'):
                    proxy_str = f'http://{proxy_str}'
                chrome_options.add_argument(f'--proxy-server={proxy_str}')
                self.logger.info(f"🔄 Using proxy: {proxy_str[:40]}...")
            
            # Anti-detection
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Realistic user agent
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.logger.info("🚀 Fast Search Scraper initialized")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise
    
    def search(self, query=None, location=None, category_id=None, limit=20, max_pages=None):
        """
        Fast search - extracts from search results only (no ad visits)
        
        Args:
            query (str): Search query
            location (str): Location filter
            category_id (int): Category ID
            limit (int): Maximum results total
            max_pages (int): Maximum pages to scrape (None = auto-calculate)
            
        Returns:
            list: List of ad dictionaries
        """
        try:
            # Calculate pages needed (35 ads per page typical)
            if max_pages is None:
                ads_per_page = 35
                max_pages = max(1, (limit + ads_per_page - 1) // ads_per_page)
            
            all_ads = []
            ads_collected = 0
            
            self.logger.info(f"⚡ Fast mode: scanning {max_pages} page(s) for {limit} ads")
            
            for page_num in range(1, max_pages + 1):
                if ads_collected >= limit:
                    break
                
                # Build URL
                params = []
                if query:
                    params.append(f"text={query}")
                if category_id:
                    params.append(f"category={category_id}")
                if location:
                    params.append(f"locations={location}")
                if page_num > 1:
                    params.append(f"page={page_num}")
                
                url = f"{self.base_url}/recherche"
                if params:
                    url += "?" + "&".join(params)
                
                self.logger.info(f"📄 Page {page_num}/{max_pages}: {url}")
                self.driver.get(url)
                
                # Handle cookie consent (first page only)
                if page_num == 1:
                    time.sleep(random.uniform(2, 4))
                    self._handle_cookie_consent()
                else:
                    time.sleep(random.uniform(1, 2))
                
                # Wait for page load
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                except TimeoutException:
                    self.logger.error(f"Page {page_num} load timeout")
                    continue
                
                # Scroll to load lazy content
                self._scroll_page(scrolls=3)
                
                # Extract ads from search page
                remaining = limit - ads_collected
                page_ads = self._extract_ads_from_search(remaining)
                
                self.logger.info(f"📊 Page {page_num}: Extracted {len(page_ads)} ads from search results")
                
                if not page_ads:
                    self.logger.info(f"No more ads on page {page_num}, stopping")
                    break
                
                # Add to collection
                all_ads.extend(page_ads)
                ads_collected = len(all_ads)
                
                self.logger.info(f"✅ Progress: {ads_collected}/{limit} ads collected")
                
                # Small delay before next page
                if page_num < max_pages and ads_collected < limit:
                    time.sleep(random.uniform(2, 3))
            
            self.logger.info(f"🎉 Success! Extracted {len(all_ads)} ads from {page_num} page(s)")
            self._print_statistics(all_ads)
            
            return all_ads[:limit]  # Ensure we don't exceed limit
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return []
    
    def _extract_ads_from_search(self, limit=35):
        """
        Extract ad data directly from search page
        
        Args:
            limit (int): Maximum ads to extract
            
        Returns:
            list: List of ad dictionaries
        """
        ads = []
        
        try:
            time.sleep(1)  # Wait for content
            
            # Find all links on page
            links = self.driver.find_elements(By.TAG_NAME, "a")
            
            # Find ad card elements (common patterns)
            ad_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='aditem_container'], .styles_adCard__2YFTi, [class*='adCard']")
            
            self.logger.info(f"Found {len(ad_elements)} potential ad cards")
            
            if not ad_elements:
                # Fallback: find links with /ad/ in href
                self.logger.info("Using fallback method: extracting from links")
                processed_urls = set()
                
                for link in links:
                    if len(ads) >= limit:
                        break
                    
                    try:
                        url = link.get_attribute('href')
                        if not url or '/ad/' not in url or 'leboncoin.fr' not in url:
                            continue
                        
                        # Clean URL
                        base_url = url.split('?')[0]
                        if base_url in processed_urls:
                            continue
                        
                        processed_urls.add(base_url)
                        
                        # Try to find parent container
                        ad_data = self._extract_ad_from_element(link, base_url)
                        if ad_data:
                            ads.append(ad_data)
                            
                    except Exception as e:
                        continue
            else:
                # Process ad cards
                for element in ad_elements[:limit]:
                    try:
                        ad_data = self._extract_ad_from_card(element)
                        if ad_data:
                            ads.append(ad_data)
                    except Exception as e:
                        self.logger.debug(f"Failed to parse ad card: {e}")
                        continue
            
            return ads
            
        except Exception as e:
            self.logger.error(f"Failed to extract ads from search: {e}")
            return []
    
    def _extract_ad_from_card(self, element):
        """
        Extract ad data from ad card element
        
        Args:
            element: Selenium WebElement (ad card)
            
        Returns:
            dict: Ad data or None
        """
        try:
            ad_data = {
                'scraped_at': datetime.now().isoformat()
            }
            
            # Extract URL (required)
            try:
                link = element.find_element(By.TAG_NAME, "a")
                url = link.get_attribute('href')
                if url and '/ad/' in url:
                    ad_data['url'] = url.split('?')[0]  # Clean URL
                    ad_data['list_id'] = self.extract_ad_id(url)
                else:
                    return None
            except:
                return None
            
            # Extract title
            title_selectors = [
                "[data-qa-id='aditem_title']",
                "p[data-qa-id='aditem_title']",
                "[class*='title']",
                "h2",
                "h3"
            ]
            for selector in title_selectors:
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    title = elem.text.strip()
                    if title and len(title) > 3:
                        ad_data['title'] = title
                        break
                except:
                    continue
            
            # Extract price (KEY FEATURE - UPDATED SELECTORS)
            price_selectors = [
                # New specific selector from user
                ".text-callout.text-on-surface.leading-sz-20\\!.flex.flex-wrap.items-center.font-bold",
                "p.text-callout.text-on-surface",
                "[class*='text-callout'][class*='font-bold']",
                # Fallback selectors
                "[data-qa-id='aditem_price']",
                "span[data-qa-id='aditem_price']",
                "p[data-qa-id='aditem_price']",
                "[class*='price']",
                "[class*='Price']"
            ]
            for selector in price_selectors:
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    price_text = elem.text.strip()
                    if price_text and '€' in price_text:
                        price = self.extract_price(price_text)
                        if price:
                            ad_data['price'] = price
                            self.logger.debug(f"  💰 Price found with selector: {selector[:50]}")
                            break
                except:
                    continue
            
            # If still no price, try finding by text content
            if not ad_data.get('price'):
                try:
                    text_content = element.text
                    if '€' in text_content:
                        import re
                        price_match = re.search(r'(\d+(?:\s?\d+)*)\s*€', text_content)
                        if price_match:
                            price = self.extract_price(price_match.group(0))
                            if price:
                                ad_data['price'] = price
                                self.logger.debug(f"  💰 Price found in text: {price} €")
                except:
                    pass
            
            # Extract location
            location_selectors = [
                "[data-qa-id='aditem_location']",
                "[class*='location']",
                "[class*='Location']"
            ]
            for selector in location_selectors:
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    location = elem.text.strip()
                    if location:
                        ad_data['location'] = location
                        break
                except:
                    continue
            
            # Extract image URL (bonus)
            try:
                img = element.find_element(By.TAG_NAME, "img")
                img_src = img.get_attribute('src')
                if img_src and 'http' in img_src:
                    ad_data['image_url'] = img_src
            except:
                pass
            
            # Validation: must have title
            if not ad_data.get('title'):
                return None
            
            # Success log
            price_str = f"{ad_data['price']} €" if ad_data.get('price') else "No price"
            self.logger.debug(f"  ✓ {ad_data['title'][:40]} - {price_str}")
            
            return ad_data
            
        except Exception as e:
            self.logger.debug(f"Failed to extract from card: {e}")
            return None
    
    def _extract_ad_from_element(self, link_element, url):
        """
        Extract ad data from link and its parent container
        
        Args:
            link_element: Selenium WebElement (link)
            url (str): Ad URL
            
        Returns:
            dict: Ad data or None
        """
        try:
            ad_data = {
                'url': url,
                'list_id': self.extract_ad_id(url),
                'scraped_at': datetime.now().isoformat()
            }
            
            # Try to get parent container
            try:
                # Go up 2-3 levels to find ad container
                parent = link_element
                for _ in range(3):
                    parent = parent.find_element(By.XPATH, "..")
                    
                    # Look for title in parent
                    if not ad_data.get('title'):
                        title_text = parent.text.strip().split('\n')[0] if parent.text else None
                        if title_text and len(title_text) > 3 and len(title_text) < 200:
                            ad_data['title'] = title_text
                    
                    # Look for price in parent
                    if not ad_data.get('price'):
                        text = parent.text
                        if '€' in text:
                            # Extract price from text using multiple patterns
                            import re
                            
                            # Try different price patterns
                            price_patterns = [
                                r'(\d+(?:\s?\d+)*)\s*€',  # Standard: "1200 €" or "1 200 €"
                                r'€\s*(\d+(?:\s?\d+)*)',  # Reverse: "€ 1200"
                                r'(\d+(?:,\d+)?)\s*€',    # With comma: "1200,50 €"
                            ]
                            
                            for pattern in price_patterns:
                                price_match = re.search(pattern, text)
                                if price_match:
                                    price = self.extract_price(price_match.group(0))
                                    if price:
                                        ad_data['price'] = price
                                        break
                            
                            if ad_data.get('price'):
                                break
                    
                    if ad_data.get('title') and ad_data.get('price'):
                        break
                        
            except:
                pass
            
            # If no title, try link text
            if not ad_data.get('title'):
                title = link_element.text.strip()
                if title and len(title) > 3:
                    ad_data['title'] = title
            
            # Validation
            if not ad_data.get('title'):
                return None
            
            return ad_data
            
        except Exception as e:
            return None
    
    def _handle_cookie_consent(self):
        """Handle cookie consent popup"""
        try:
            consent_selectors = [
                "button[id*='didomi-notice-agree-button']",
                "button[id*='accept']",
                "button.didomi-button"
            ]
            
            for selector in consent_selectors:
                try:
                    button = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    button.click()
                    self.logger.info("Cookie consent accepted")
                    time.sleep(1)
                    return
                except:
                    continue
        except:
            pass
    
    def _scroll_page(self, scrolls=3):
        """Scroll page to trigger lazy loading"""
        try:
            for i in range(scrolls):
                scroll_position = (i + 1) / scrolls
                self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {scroll_position});")
                time.sleep(random.uniform(0.3, 0.8))
        except Exception as e:
            self.logger.debug(f"Scrolling error: {e}")
    
    def _print_statistics(self, ads):
        """Print extraction statistics"""
        if not ads:
            return
        
        with_price = sum(1 for ad in ads if ad.get('price'))
        with_location = sum(1 for ad in ads if ad.get('location'))
        
        self.logger.info(f"\n{'='*60}")
        self.logger.info(f"📊 EXTRACTION STATISTICS")
        self.logger.info(f"{'='*60}")
        self.logger.info(f"  Total ads: {len(ads)}")
        self.logger.info(f"  With prices: {with_price}/{len(ads)} ({with_price/len(ads)*100:.0f}%)")
        self.logger.info(f"  With locations: {with_location}/{len(ads)} ({with_location/len(ads)*100:.0f}%)")
        self.logger.info(f"{'='*60}\n")
    
    def close(self):
        """Close the browser"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("Browser closed")
            except:
                pass
    
    def __del__(self):
        """Destructor"""
        self.close()
