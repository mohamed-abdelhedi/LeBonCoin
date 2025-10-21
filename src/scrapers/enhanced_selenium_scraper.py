"""
Enhanced Selenium Scraper with detailed ad information
Extracts: title, price, description, location, and other details
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
from datetime import datetime
import re
from .base_scraper import BaseScraper

class EnhancedSeleniumScraper(BaseScraper):
    """Enhanced Selenium-based scraper with detailed extraction"""
    
    def __init__(self, headless=True, min_delay=2.0, max_delay=4.0, fetch_details=True):
        """
        Initialize Enhanced Selenium scraper
        
        Args:
            headless (bool): Run browser in headless mode
            min_delay (float): Minimum delay between requests
            max_delay (float): Maximum delay between requests
            fetch_details (bool): Visit each ad page for full details
        """
        super().__init__(min_delay, max_delay)
        self.headless = headless
        self.fetch_details = fetch_details
        self.driver = None
        self.base_url = "https://www.leboncoin.fr"
        self._init_driver()
    
    def _init_driver(self):
        """Initialize Chrome WebDriver"""
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless=new")
            
            # Make it look like a real browser
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
            
            self.logger.info("Chrome WebDriver initialized (Enhanced)")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise
    
    def search(self, query=None, location=None, category_id=None, limit=20, max_pages=None):
        """
        Search for ads with detailed extraction (supports pagination)
        
        Args:
            query (str): Search query
            location (str): Location filter
            category_id (int): Category ID
            limit (int): Maximum results per page (default 20)
            max_pages (int): Maximum pages to scrape (None = auto-calculate from limit)
            
        Returns:
            list: List of ad dictionaries with full details
        """
        try:
            # Calculate pages needed
            if max_pages is None:
                # Each page typically has ~35 ads, so calculate pages needed
                ads_per_page = 35
                max_pages = max(1, (limit + ads_per_page - 1) // ads_per_page)
            
            all_ads = []
            ads_collected = 0
            
            for page_num in range(1, max_pages + 1):
                if ads_collected >= limit:
                    break
                
                # Build URL with page parameter
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
                
                self.logger.info(f"Searching page {page_num}/{max_pages}: {url}")
                self.driver.get(url)
            
                # Wait and handle cookie consent (only on first page)
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
                
                # Scroll to load more content
                self._scroll_page(scrolls=5)
                
                # Extract ad URLs from current page
                remaining = limit - ads_collected
                page_urls = self._extract_ad_urls(remaining)
                self.logger.info(f"Page {page_num}: Found {len(page_urls)} ad URLs")
                
                if not page_urls:
                    self.logger.info(f"No more ads on page {page_num}, stopping")
                    break
                
                # Extract details from each ad
                for i, ad_url in enumerate(page_urls, 1):
                    if ads_collected >= limit:
                        break
                    
                    self.logger.info(f"[Page {page_num}] Extracting ad {i}/{len(page_urls)}: {ad_url}")
                    
                    if self.fetch_details:
                        ad_data = self._extract_ad_details(ad_url)
                    else:
                        ad_data = {'url': ad_url, 'list_id': self.extract_ad_id(ad_url)}
                    
                    if ad_data:
                        all_ads.append(ad_data)
                        ads_collected += 1
                    
                    # Rate limiting
                    if i < len(page_urls) and ads_collected < limit:
                        self.rate_limit()
                
                self.logger.info(f"Page {page_num} complete. Total ads: {ads_collected}/{limit}")
                
                # Small delay before next page
                if page_num < max_pages and ads_collected < limit:
                    time.sleep(random.uniform(2, 3))
            
            self.logger.info(f"Successfully extracted {len(all_ads)} complete ads from {page_num} page(s)")
            return all_ads
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return []
    
    def _handle_cookie_consent(self):
        """Handle cookie consent popup"""
        try:
            consent_selectors = [
                "button[id*='didomi-notice-agree-button']",
                "button[id*='accept']",
                "button[id*='consent']",
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
        except Exception as e:
            self.logger.debug(f"Cookie handling: {e}")
    
    def _scroll_page(self, scrolls=5):
        """Scroll page to trigger lazy loading"""
        try:
            for i in range(scrolls):
                # Scroll down
                self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {(i+1)/scrolls});")
                time.sleep(random.uniform(0.5, 1.0))
        except Exception as e:
            self.logger.debug(f"Scrolling error: {e}")
    
    def _extract_ad_urls(self, limit=20):
        """Extract ad URLs from listing page"""
        ad_urls = []
        
        try:
            # Wait for ads to load
            time.sleep(2)
            
            # Find all links
            links = self.driver.find_elements(By.TAG_NAME, "a")
            self.logger.info(f"Found {len(links)} total links on page")
            
            for link in links:
                try:
                    url = link.get_attribute('href')
                    if url and '/ad/' in url and 'leboncoin.fr' in url:
                        # Clean URL
                        base_url = url.split('?')[0]
                        if base_url not in ad_urls:
                            ad_urls.append(base_url)
                            
                            if len(ad_urls) >= limit:
                                break
                except:
                    continue
            
            self.logger.info(f"Extracted {len(ad_urls)} unique ad URLs")
            
        except Exception as e:
            self.logger.error(f"Failed to extract ad URLs: {e}")
        
        return ad_urls[:limit]
    
    def _extract_ad_details(self, url):
        """Visit ad page and extract full details"""
        try:
            self.driver.get(url)
            time.sleep(random.uniform(2, 3))
            
            ad_data = {
                'url': url,
                'list_id': self.extract_ad_id(url),
                'scraped_at': datetime.now().isoformat()
            }
            
            # Extract title
            title_selectors = [
                "h1[data-qa-id='adview_title']",
                "h1",
                "div[data-qa-id='adview_title']"
            ]
            for selector in title_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    title = elem.text.strip()
                    if title:
                        ad_data['title'] = title
                        break
                except:
                    continue
            
            # Extract price
            price_selectors = [
                "div[data-qa-id='adview_price']",  # Container div
                "div[data-qa-id='adview_price'] p",  # p tag inside
                "p.text-headline-1",  # Direct p tag with class
                "span[data-qa-id='adview_price']",
                "div[data-test-id='price']"
            ]
            for selector in price_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    price_text = elem.text.strip()
                    if price_text and '€' in price_text:
                        price = self.extract_price(price_text)
                        if price:
                            ad_data['price'] = price
                            self.logger.debug(f"Price extracted: {price} from selector: {selector}")
                            break
                except Exception as e:
                    self.logger.debug(f"Selector {selector} failed: {e}")
                    continue
            
            # Extract description
            desc_selectors = [
                "div[data-qa-id='adview_description_container']",
                "div[data-qa-id='adview_description']",
                "div[class*='description']",
                "span[data-qa-id='adview_description_container']"
            ]
            for selector in desc_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    desc = elem.text.strip()
                    if desc and len(desc) > 10:
                        ad_data['description'] = desc
                        break
                except:
                    continue
            
            # Extract location
            location_selectors = [
                "div[data-qa-id='adview_location_informations']",
                "span[data-qa-id='adview_location']",
                "div[class*='location']"
            ]
            for selector in location_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    location = elem.text.strip()
                    if location:
                        ad_data['location'] = location
                        break
                except:
                    continue
            
            # Extract category
            try:
                breadcrumb = self.driver.find_elements(By.CSS_SELECTOR, "nav a, nav span")
                if breadcrumb and len(breadcrumb) > 1:
                    ad_data['category'] = breadcrumb[1].text.strip()
            except:
                pass
            
            # Extract seller name
            seller_selectors = [
                "div[data-qa-id='adview_seller_name']",
                "a[data-qa-id='adview_seller_name']"
            ]
            for selector in seller_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    seller = elem.text.strip()
                    if seller:
                        ad_data['seller_name'] = seller
                        break
                except:
                    continue
            
            # Extract date
            date_selectors = [
                "div[data-qa-id='adview_date']",
                "span[data-qa-id='adview_date']"
            ]
            for selector in date_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    date_text = elem.text.strip()
                    if date_text:
                        ad_data['date_posted'] = date_text
                        break
                except:
                    continue
            
            # Validation
            if not ad_data.get('title'):
                self.logger.warning(f"No title found for {url}")
                return None
            
            price_display = f"{ad_data.get('price')} €" if ad_data.get('price') else "No price"
            self.logger.info(f"✅ Extracted: {ad_data.get('title')[:50]} - {price_display}")
            return ad_data
            
        except Exception as e:
            self.logger.error(f"Failed to extract ad details from {url}: {e}")
            return None
    
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
