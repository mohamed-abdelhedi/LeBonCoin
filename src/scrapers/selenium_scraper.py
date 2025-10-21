"""
Selenium-based Web Scraper
Uses browser automation to bypass anti-bot protection
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
from .base_scraper import BaseScraper

class SeleniumScraper(BaseScraper):
    """Selenium-based scraper for Leboncoin"""
    
    def __init__(self, headless=True, min_delay=2.0, max_delay=4.0):
        """
        Initialize Selenium scraper
        
        Args:
            headless (bool): Run browser in headless mode
            min_delay (float): Minimum delay between requests
            max_delay (float): Maximum delay between requests
        """
        super().__init__(min_delay, max_delay)
        self.headless = headless
        self.driver = None
        self.base_url = "https://www.leboncoin.fr"
        self._init_driver()
    
    def _init_driver(self):
        """Initialize Chrome WebDriver"""
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless")
            
            # Make it look like a real browser
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Realistic user agent
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.logger.info("Chrome WebDriver initialized")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise
    
    def search(self, query=None, location=None, category_id=None, limit=20):
        """
        Search for ads
        
        Args:
            query (str): Search query
            location (str): Location filter
            category_id (int): Category ID
            limit (int): Maximum results
            
        Returns:
            list: List of ad dictionaries
        """
        try:
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
            self.driver.get(url)
            
            # Wait and handle cookie consent
            time.sleep(random.uniform(2, 4))
            self._handle_cookie_consent()
            
            # Wait for page load
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except TimeoutException:
                self.logger.error("Page load timeout")
                return []
            
            # Scroll to load content
            self._scroll_page()
            
            # Extract ads
            ads = self._extract_ads(limit)
            self.logger.info(f"Extracted {len(ads)} ads")
            
            return ads
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return []
    
    def _handle_cookie_consent(self):
        """Handle cookie consent popup"""
        try:
            consent_selectors = [
                "button[id*='accept']",
                "button[id*='consent']",
                "button.didomi-button",
                "#didomi-notice-agree-button"
            ]
            
            for selector in consent_selectors:
                try:
                    button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if button.is_displayed():
                        button.click()
                        self.logger.info("Cookie consent accepted")
                        time.sleep(1)
                        return
                except NoSuchElementException:
                    continue
        except Exception as e:
            self.logger.debug(f"Cookie handling: {e}")
    
    def _scroll_page(self):
        """Scroll page to trigger lazy loading"""
        try:
            for i in range(3):
                self.driver.execute_script(f"window.scrollTo(0, {(i + 1) * 500});")
                time.sleep(0.5)
        except Exception as e:
            self.logger.debug(f"Scrolling error: {e}")
    
    def _extract_ads(self, limit=20):
        """Extract ads from current page"""
        ads = []
        
        try:
            # Try multiple selectors
            ad_selectors = [
                "article",
                "div[data-qa-id='aditem_container']",
                "a[data-test-id='ad']"
            ]
            
            ad_elements = []
            for selector in ad_selectors:
                try:
                    ad_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if ad_elements:
                        self.logger.info(f"Found {len(ad_elements)} elements with: {selector}")
                        break
                except:
                    continue
            
            if not ad_elements:
                self.logger.warning("No ad elements found")
                return []
            
            # Parse each ad
            for element in ad_elements[:limit]:
                try:
                    ad_data = self._parse_ad(element)
                    if ad_data:
                        ads.append(ad_data)
                except Exception as e:
                    self.logger.debug(f"Failed to parse ad: {e}")
                    continue
            
        except Exception as e:
            self.logger.error(f"Failed to extract ads: {e}")
        
        return ads
    
    def _parse_ad(self, element):
        """Parse individual ad element"""
        try:
            ad_data = {'scraped_at': datetime.now().isoformat()}
            
            # Extract title
            title_selectors = [
                "p[data-qa-id='aditem_title']",
                "div[data-qa-id='aditem_title']",
                "[data-test-id='ad-title']",
                "h2", "h3", "h4"
            ]
            
            for selector in title_selectors:
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    title = elem.text.strip()
                    if title:
                        ad_data['title'] = title
                        break
                except:
                    continue
            
            # Fallback: get first text line
            if 'title' not in ad_data:
                try:
                    all_text = element.text.strip().split('\n')
                    if all_text and all_text[0]:
                        ad_data['title'] = all_text[0][:200]
                except:
                    pass
            
            # Extract price
            price_selectors = [
                "span[data-qa-id='aditem_price']",
                "p[data-qa-id='aditem_price']",
                "[class*='price']"
            ]
            
            for selector in price_selectors:
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    price_text = elem.text.strip()
                    if price_text and ('€' in price_text or price_text.replace(' ', '').isdigit()):
                        ad_data['price'] = self.extract_price(price_text)
                        if ad_data['price']:
                            break
                except:
                    continue
            
            # Extract URL
            try:
                links = element.find_elements(By.TAG_NAME, "a")
                for link in links:
                    url = link.get_attribute('href')
                    if url and 'leboncoin.fr' in url and ('/ad/' in url or '.htm' in url):
                        ad_data['url'] = url
                        ad_data['list_id'] = self.extract_ad_id(url)
                        break
            except:
                pass
            
            # Extract location
            location_selectors = [
                "p[data-qa-id='aditem_location']",
                "[class*='location']"
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
            
            # Only return if we have title and URL
            if ad_data.get('title') and ad_data.get('url'):
                return ad_data
            
            return None
            
        except Exception as e:
            self.logger.debug(f"Error parsing ad: {e}")
            return None
    
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            self.logger.info("Browser closed")
    
    def __del__(self):
        """Destructor"""
        self.close()
