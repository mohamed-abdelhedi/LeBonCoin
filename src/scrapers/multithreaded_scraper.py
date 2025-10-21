"""
Multi-Threaded Enhanced Selenium Scraper
Uses ThreadPoolExecutor for parallel ad extraction
Optimized for i7-10750H (6 cores, 12 threads, 16GB RAM)
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
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from .base_scraper import BaseScraper

class MultiThreadedScraper(BaseScraper):
    """Multi-threaded Selenium scraper for faster extraction"""
    
    def __init__(self, headless=True, min_delay=3.0, max_delay=6.0, num_threads=4):
        """
        Initialize Multi-threaded Selenium scraper
        
        Args:
            headless (bool): Run browser in headless mode
            min_delay (float): Minimum delay between requests (increased for safety)
            max_delay (float): Maximum delay between requests (increased for safety)
            num_threads (int): Number of parallel threads (4-6 recommended for your CPU)
        """
        super().__init__(min_delay, max_delay)
        self.headless = headless
        self.num_threads = num_threads
        self.base_url = "https://www.leboncoin.fr"
        self.thread_local = threading.local()
        
        # Thread-safe logging
        self._lock = threading.Lock()
        
        self.logger.info(f"Multi-threaded scraper initialized with {num_threads} threads")
    
    def _get_driver(self):
        """Get or create a driver for the current thread"""
        if not hasattr(self.thread_local, 'driver') or self.thread_local.driver is None:
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
            
            # Rotate user agents slightly
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            ]
            chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
            
            self.thread_local.driver = webdriver.Chrome(options=chrome_options)
            self.thread_local.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            with self._lock:
                self.logger.info(f"Chrome WebDriver initialized for thread {threading.current_thread().name}")
        
        return self.thread_local.driver
    
    def search(self, query=None, location=None, category_id=None, limit=20):
        """
        Search for ads using multi-threading
        
        Args:
            query (str): Search query
            location (str): Location filter
            category_id (int): Category ID
            limit (int): Maximum results
            
        Returns:
            list: List of ad dictionaries with full details
        """
        try:
            # Use main driver for listing page
            driver = self._get_driver()
            
            # Build URL
            params = []
            if query:
                params.append(f"text={query}")
            if category_id:
                params.append(f"category={category_id}")
            if location:
                params.append(f"locations={location}")
            
            url = f"{self.base_url}/recherche"
            if params:
                url += "?" + "&".join(params)
            
            self.logger.info(f"Searching: {url}")
            driver.get(url)
            
            # Wait and handle cookie consent
            time.sleep(random.uniform(3, 5))
            self._handle_cookie_consent(driver)
            
            # Wait for page load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except TimeoutException:
                self.logger.error("Page load timeout")
                return []
            
            # Scroll to load more content
            self._scroll_page(driver, scrolls=5)
            
            # Extract ad URLs from listing page
            ad_urls = self._extract_ad_urls(driver, limit)
            self.logger.info(f"Found {len(ad_urls)} ad URLs")
            
            if not ad_urls:
                return []
            
            # Extract details from each ad using thread pool
            self.logger.info(f"Starting parallel extraction with {self.num_threads} threads...")
            ads = self._parallel_extract(ad_urls)
            
            self.logger.info(f"Successfully extracted {len(ads)} complete ads")
            return ads
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return []
    
    def _parallel_extract(self, ad_urls):
        """Extract ad details in parallel using thread pool"""
        ads = []
        
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(self._extract_ad_details_threaded, url, i+1, len(ad_urls)): url 
                for i, url in enumerate(ad_urls)
            }
            
            # Collect results as they complete
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    ad_data = future.result()
                    if ad_data:
                        ads.append(ad_data)
                except Exception as e:
                    with self._lock:
                        self.logger.error(f"Failed to extract {url}: {e}")
        
        return ads
    
    def _extract_ad_details_threaded(self, url, index, total):
        """Thread-safe ad extraction"""
        try:
            driver = self._get_driver()
            
            # Random delay to avoid detection
            delay = random.uniform(self.min_delay, self.max_delay)
            time.sleep(delay)
            
            with self._lock:
                self.logger.info(f"[{index}/{total}] Extracting: {url}")
            
            driver.get(url)
            time.sleep(random.uniform(2, 4))
            
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
                    elem = driver.find_element(By.CSS_SELECTOR, selector)
                    title = elem.text.strip()
                    if title:
                        ad_data['title'] = title
                        break
                except:
                    continue
            
            # Extract price (FIXED SELECTORS)
            price_selectors = [
                "div[data-qa-id='adview_price']",
                "div[data-qa-id='adview_price'] p",
                "p.text-headline-1",
                "span[data-qa-id='adview_price']"
            ]
            for selector in price_selectors:
                try:
                    elem = driver.find_element(By.CSS_SELECTOR, selector)
                    price_text = elem.text.strip()
                    if price_text and '€' in price_text:
                        price = self.extract_price(price_text)
                        if price:
                            ad_data['price'] = price
                            break
                except:
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
                    elem = driver.find_element(By.CSS_SELECTOR, selector)
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
                    elem = driver.find_element(By.CSS_SELECTOR, selector)
                    location = elem.text.strip()
                    if location:
                        ad_data['location'] = location
                        break
                except:
                    continue
            
            # Extract category
            try:
                breadcrumb = driver.find_elements(By.CSS_SELECTOR, "nav a, nav span")
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
                    elem = driver.find_element(By.CSS_SELECTOR, selector)
                    seller = elem.text.strip()
                    if seller:
                        ad_data['seller_name'] = seller
                        break
                except:
                    continue
            
            # Validation
            if not ad_data.get('title'):
                with self._lock:
                    self.logger.warning(f"No title found for {url}")
                return None
            
            price_display = f"{ad_data.get('price')} €" if ad_data.get('price') else "No price"
            with self._lock:
                self.logger.info(f"✅ [{index}/{total}] {ad_data.get('title')[:40]} - {price_display}")
            
            return ad_data
            
        except Exception as e:
            with self._lock:
                self.logger.error(f"Failed to extract ad details from {url}: {e}")
            return None
    
    def _handle_cookie_consent(self, driver):
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
                    button = WebDriverWait(driver, 3).until(
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
    
    def _scroll_page(self, driver, scrolls=5):
        """Scroll page to trigger lazy loading"""
        try:
            for i in range(scrolls):
                driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {(i+1)/scrolls});")
                time.sleep(random.uniform(0.5, 1.0))
        except Exception as e:
            self.logger.debug(f"Scrolling error: {e}")
    
    def _extract_ad_urls(self, driver, limit=20):
        """Extract ad URLs from listing page"""
        ad_urls = []
        
        try:
            time.sleep(2)
            
            links = driver.find_elements(By.TAG_NAME, "a")
            self.logger.info(f"Found {len(links)} total links on page")
            
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
            
            self.logger.info(f"Extracted {len(ad_urls)} unique ad URLs")
            
        except Exception as e:
            self.logger.error(f"Failed to extract ad URLs: {e}")
        
        return ad_urls[:limit]
    
    def close(self):
        """Close all browser instances"""
        if hasattr(self.thread_local, 'driver') and self.thread_local.driver:
            try:
                self.thread_local.driver.quit()
                self.logger.info("Browser closed")
            except:
                pass
    
    def __del__(self):
        """Destructor"""
        self.close()
