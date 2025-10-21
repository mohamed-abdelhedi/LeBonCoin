"""
Enhanced Scraper with Stealth Mode & Proxy Support
Anti-blocking features for Leboncoin scraping
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from datetime import datetime
import re
from .base_scraper import BaseScraper

class StealthScraper(BaseScraper):
    """Enhanced Selenium scraper with anti-blocking features"""
    
    def __init__(self, headless=True, min_delay=5.0, max_delay=12.0, fetch_details=True, 
                 proxy=None, stealth_mode=True):
        """
        Initialize Stealth Selenium scraper
        
        Args:
            headless (bool): Run browser in headless mode
            min_delay (float): Minimum delay between requests (5-12 recommended)
            max_delay (float): Maximum delay between requests
            fetch_details (bool): Visit each ad page for full details
            proxy (str): Proxy URL (e.g., "http://user:pass@proxy:port")
            stealth_mode (bool): Enable extra anti-detection features
        """
        super().__init__(min_delay, max_delay)
        self.headless = headless
        self.fetch_details = fetch_details
        self.proxy = proxy
        self.stealth_mode = stealth_mode
        self.driver = None
        self.base_url = "https://www.leboncoin.fr"
        self._init_driver()
    
    def _init_driver(self):
        """Initialize Chrome WebDriver with stealth features"""
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless=new")
            
            # Proxy configuration (supports multiple formats)
            if self.proxy:
                # Import proxy config helper
                from src.utils.proxy_config import ProxyConfig
                
                try:
                    proxy_config = ProxyConfig(self.proxy)
                    chrome_arg = proxy_config.get_chrome_argument()
                    
                    if chrome_arg:
                        chrome_options.add_argument(chrome_arg)
                        self.logger.info(f"🌐 Proxy configured: {chrome_arg}")
                        
                        # If proxy has authentication, handle it
                        if proxy_config.has_auth():
                            username, password = proxy_config.get_credentials()
                            self.logger.info(f"🔐 Proxy authentication: {username}:***")
                    else:
                        self.logger.warning("⚠️  Could not configure proxy")
                        
                except ValueError as e:
                    self.logger.error(f"❌ Invalid proxy format: {e}")
                    raise
            
            # Anti-detection arguments
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            # Remove automation indicators
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Randomize user agent
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            ]
            selected_ua = random.choice(user_agents)
            chrome_options.add_argument(f"user-agent={selected_ua}")
            self.logger.info(f"User agent: {selected_ua[:50]}...")
            
            # Additional headers to appear more human
            chrome_options.add_argument("--lang=en-US,en;q=0.9,fr;q=0.8")
            chrome_options.add_argument("--accept-language=en-US,en;q=0.9,fr;q=0.8")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            
            # Execute stealth JavaScript
            if self.stealth_mode:
                self._apply_stealth_scripts()
            
            self.logger.info("Stealth Chrome WebDriver initialized")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise
    
    def _apply_stealth_scripts(self):
        """Apply JavaScript to hide automation"""
        # Hide webdriver property
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # Override permissions
        self.driver.execute_script("Object.defineProperty(navigator, 'permissions', {get: () => ({query: () => Promise.resolve({state: 'denied'})})})")
        
        # Override plugins
        self.driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
        
        # Override languages
        self.driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en', 'fr']})")
        
        self.logger.info("Stealth scripts applied")
    
    def _human_delay(self, min_delay=None, max_delay=None):
        """Add human-like delay with variation"""
        min_d = min_delay if min_delay else self.min_delay
        max_d = max_delay if max_delay else self.max_delay
        
        # Random delay with occasional longer pauses (simulating reading/thinking)
        if random.random() < 0.1:  # 10% chance of longer pause
            delay = random.uniform(max_d * 1.5, max_d * 2)
            self.logger.debug(f"Long pause: {delay:.1f}s (simulating reading)")
        else:
            delay = random.uniform(min_d, max_d)
        
        time.sleep(delay)
    
    def _human_scroll(self):
        """Scroll like a human - not all at once"""
        try:
            # Random number of scroll actions
            num_scrolls = random.randint(3, 7)
            
            for i in range(num_scrolls):
                # Scroll by random amount
                scroll_amount = random.randint(300, 800)
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                
                # Random small delay between scrolls
                time.sleep(random.uniform(0.3, 1.2))
            
            # Sometimes scroll back up a bit
            if random.random() < 0.3:
                self.driver.execute_script(f"window.scrollBy(0, {-random.randint(200, 400)});")
                time.sleep(random.uniform(0.5, 1.0))
                
        except Exception as e:
            self.logger.debug(f"Scrolling error: {e}")
    
    def _random_mouse_movement(self):
        """Simulate random mouse movements"""
        try:
            if not self.headless and self.stealth_mode:
                actions = ActionChains(self.driver)
                
                # Random movements
                for _ in range(random.randint(2, 4)):
                    x_offset = random.randint(-100, 100)
                    y_offset = random.randint(-100, 100)
                    actions.move_by_offset(x_offset, y_offset)
                
                actions.perform()
        except Exception as e:
            self.logger.debug(f"Mouse movement error: {e}")
    
    def search(self, query=None, location=None, category_id=None, limit=20, max_pages=None):
        """
        Search with stealth features
        
        Args:
            query (str): Search query
            location (str): Location filter
            category_id (int): Category ID
            limit (int): Maximum results
            max_pages (int): Maximum pages to scrape
            
        Returns:
            list: List of ad dictionaries
        """
        try:
            # Calculate pages needed
            if max_pages is None:
                ads_per_page = 35
                max_pages = max(1, (limit + ads_per_page - 1) // ads_per_page)
            
            # Limit pages for safety
            if max_pages > 5:
                self.logger.warning(f"Limiting to 5 pages for safety (requested {max_pages})")
                max_pages = 5
            
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
                
                self.logger.info(f"🔍 Page {page_num}/{max_pages}: {url}")
                self.driver.get(url)
                
                # Human-like waiting
                self._human_delay(3, 6)
                
                # Handle cookies (only first page)
                if page_num == 1:
                    self._handle_cookie_consent()
                
                # Human-like scrolling
                self._human_scroll()
                
                # Random mouse movement (if not headless)
                if not self.headless:
                    self._random_mouse_movement()
                
                # Extract URLs
                remaining = limit - ads_collected
                page_urls = self._extract_ad_urls(remaining)
                
                if not page_urls:
                    self.logger.info(f"No more ads on page {page_num}")
                    break
                
                self.logger.info(f"📄 Page {page_num}: Found {len(page_urls)} URLs")
                
                # Extract each ad with human-like timing
                for i, ad_url in enumerate(page_urls, 1):
                    if ads_collected >= limit:
                        break
                    
                    self.logger.info(f"[{ads_collected + 1}/{limit}] Extracting: {ad_url[:60]}...")
                    
                    if self.fetch_details:
                        ad_data = self._extract_ad_details(ad_url)
                    else:
                        ad_data = {'url': ad_url, 'list_id': self.extract_ad_id(ad_url)}
                    
                    if ad_data:
                        all_ads.append(ad_data)
                        ads_collected += 1
                    
                    # Human-like delay between ads
                    if i < len(page_urls) and ads_collected < limit:
                        self._human_delay()
                
                # Longer pause between pages
                if page_num < max_pages and ads_collected < limit:
                    pause = random.uniform(5, 10)
                    self.logger.info(f"⏸️  Pausing {pause:.1f}s before next page...")
                    time.sleep(pause)
            
            self.logger.info(f"✅ Extracted {len(all_ads)} ads from {page_num} page(s)")
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
                    # Small delay before clicking (human-like)
                    time.sleep(random.uniform(0.5, 1.5))
                    button.click()
                    self.logger.info("✅ Cookie consent accepted")
                    time.sleep(1)
                    return
                except:
                    continue
        except Exception as e:
            self.logger.debug(f"Cookie handling: {e}")
    
    def _extract_ad_urls(self, limit=20):
        """Extract ad URLs from listing page"""
        ad_urls = []
        
        try:
            time.sleep(2)
            links = self.driver.find_elements(By.TAG_NAME, "a")
            
            for link in links:
                try:
                    url = link.get_attribute('href')
                    if url and '/ad/' in url and 'leboncoin.fr' in url:
                        base_url = url.split('?')[0]
                        if base_url not in ad_urls:
                            ad_urls.append(base_url)
                            if len(ad_urls) >= limit:
                                break
                except:
                    continue
            
        except Exception as e:
            self.logger.error(f"Failed to extract URLs: {e}")
        
        return ad_urls[:limit]
    
    def _extract_ad_details(self, url):
        """Extract full ad details"""
        try:
            self.driver.get(url)
            self._human_delay(2, 4)
            
            ad_data = {
                'url': url,
                'list_id': self.extract_ad_id(url),
                'scraped_at': datetime.now().isoformat()
            }
            
            # Extract all fields (same as enhanced scraper)
            # Title
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
            
            # Price
            price_selectors = [
                "div[data-qa-id='adview_price']",
                "div[data-qa-id='adview_price'] p",
                "p.text-headline-1"
            ]
            for selector in price_selectors:
                try:
                    elem = self.driver.find_element(By.CSS_SELECTOR, selector)
                    price_text = elem.text.strip()
                    if price_text and '€' in price_text:
                        price = self.extract_price(price_text)
                        if price:
                            ad_data['price'] = price
                            break
                except:
                    continue
            
            # Description
            desc_selectors = [
                "div[data-qa-id='adview_description_container']",
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
            
            # Location
            location_selectors = [
                "div[data-qa-id='adview_location_informations']",
                "span[data-qa-id='adview_location']"
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
            
            if ad_data.get('title'):
                price_display = f"{ad_data.get('price')} €" if ad_data.get('price') else "No price"
                self.logger.info(f"✅ {ad_data.get('title')[:40]} - {price_display}")
                return ad_data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to extract {url}: {e}")
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
