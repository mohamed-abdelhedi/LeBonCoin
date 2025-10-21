"""
ScraperAPI Integration
Use ScraperAPI to handle proxies, CAPTCHA, and blocking automatically
Sign up: https://www.scraperapi.com/
"""

import requests
from typing import Optional, Dict
import logging
from bs4 import BeautifulSoup

class ScraperAPIClient:
    """Client for ScraperAPI service"""
    
    def __init__(self, api_key: str):
        """
        Initialize ScraperAPI client
        
        Args:
            api_key: Your ScraperAPI key from dashboard
        """
        self.api_key = api_key
        self.base_url = "http://api.scraperapi.com"
        self.logger = logging.getLogger(__name__)
        
        if not api_key or api_key == "YOUR_API_KEY_HERE":
            self.logger.warning("⚠️  No valid ScraperAPI key configured!")
    
    def scrape_url(self, url: str, render_js: bool = False, country_code: str = None) -> Optional[str]:
        """
        Scrape URL using ScraperAPI
        
        Args:
            url: URL to scrape
            render_js: Enable JavaScript rendering (costs more credits)
            country_code: Country code for geotargeting (e.g., 'fr', 'us')
            
        Returns:
            str: HTML content or None if failed
        """
        try:
            params = {
                'api_key': self.api_key,
                'url': url,
            }
            
            if render_js:
                params['render'] = 'true'
            
            if country_code:
                params['country_code'] = country_code
            
            self.logger.info(f"📡 ScraperAPI request: {url[:50]}...")
            
            response = requests.get(self.base_url, params=params, timeout=60)
            response.raise_for_status()
            
            self.logger.info(f"✅ ScraperAPI success!")
            return response.text
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"❌ ScraperAPI error: {e}")
            return None
    
    def get_search_results(self, query: str, country_code: str = 'fr') -> Optional[str]:
        """
        Get Leboncoin search results using ScraperAPI
        
        Args:
            query: Search query
            country_code: Country code (default: 'fr' for France)
            
        Returns:
            str: HTML content or None
        """
        url = f"https://www.leboncoin.fr/recherche?text={query}"
        return self.scrape_url(url, render_js=True, country_code=country_code)
    
    def parse_search_results(self, html: str) -> list:
        """
        Parse search results HTML
        
        Args:
            html: HTML content from ScraperAPI
            
        Returns:
            list: List of ad dictionaries
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            ads = []
            
            # Find ad cards (adjust selectors as needed)
            ad_elements = soup.find_all('a', href=lambda x: x and '/ad/' in x)
            
            for elem in ad_elements[:20]:  # Limit to 20
                try:
                    url = elem.get('href')
                    if url and '/ad/' in url:
                        # Basic extraction
                        ad_data = {
                            'url': url if url.startswith('http') else f"https://www.leboncoin.fr{url}",
                            'title': elem.get_text(strip=True)[:200] if elem.get_text() else None
                        }
                        
                        if ad_data['title']:
                            ads.append(ad_data)
                            
                except Exception as e:
                    continue
            
            self.logger.info(f"📊 Parsed {len(ads)} ads from HTML")
            return ads
            
        except Exception as e:
            self.logger.error(f"❌ Parse error: {e}")
            return []
    
    def get_account_info(self) -> Optional[Dict]:
        """
        Get ScraperAPI account information
        
        Returns:
            dict: Account info or None
        """
        try:
            url = "https://api.scraperapi.com/account"
            params = {'api_key': self.api_key}
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            self.logger.info("✅ Account info retrieved")
            return data
            
        except Exception as e:
            self.logger.error(f"❌ Account info error: {e}")
            return None


def test_scraperapi():
    """Test ScraperAPI integration"""
    print("\n" + "="*80)
    print("🔧 SCRAPERAPI SETUP TEST")
    print("="*80 + "\n")
    
    # Load API key
    try:
        with open('config/scraperapi_key.txt', 'r') as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        print("❌ API key file not found!")
        print("\n📝 Setup instructions:")
        print("   1. Sign up at https://www.scraperapi.com/")
        print("   2. Get your API key from dashboard")
        print("   3. Create file: config/scraperapi_key.txt")
        print("   4. Paste your API key in the file")
        print("   5. Run this test again")
        return
    
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("❌ Invalid API key!")
        print("   Replace 'YOUR_API_KEY_HERE' with your real key")
        return
    
    # Test API
    client = ScraperAPIClient(api_key)
    
    print("🔍 Testing account info...")
    info = client.get_account_info()
    
    if info:
        print(f"✅ Account validated!")
        print(f"\n📊 Account details:")
        print(f"   Request limit: {info.get('requestLimit', 'N/A')}")
        print(f"   Requests used: {info.get('requestCount', 'N/A')}")
        remaining = info.get('requestLimit', 0) - info.get('requestCount', 0)
        print(f"   Remaining: {remaining}")
        print()
        
        # Test scraping
        test_search = input("Test scraping? (y/n): ").strip().lower()
        if test_search == 'y':
            query = input("Search query (e.g., 'laptop'): ").strip() or "laptop"
            
            print(f"\n🔍 Scraping Leboncoin for: {query}")
            print("   (This will use 1 API credit)")
            
            html = client.get_search_results(query)
            
            if html:
                print("✅ HTML received!")
                ads = client.parse_search_results(html)
                print(f"📊 Found {len(ads)} ads")
                
                if ads:
                    print("\n📦 Sample results:")
                    for i, ad in enumerate(ads[:5], 1):
                        print(f"  {i}. {ad.get('title', 'N/A')[:60]}")
                        print(f"     🔗 {ad.get('url', 'N/A')[:70]}...")
            else:
                print("❌ Scraping failed")
    else:
        print("❌ Could not validate account")
        print("   Check your API key")


if __name__ == "__main__":
    test_scraperapi()
