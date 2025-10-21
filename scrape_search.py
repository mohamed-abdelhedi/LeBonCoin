"""
Main Scraper - Search Page Only (Fast)
Extracts data from search results without visiting individual product pages
Uses: Proxy rotation with ScraperAPI fallback
"""
import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scrapers.fast_search_scraper import FastSearchScraper
from src.database.db_handler import DatabaseHandler
from src.utils.proxy_rotator import ProxyRotator
from src.utils.scraperapi_client import ScraperAPIClient


class SearchPageScraper:
    """Search page scraper with proxy rotation and ScraperAPI fallback"""
    
    def __init__(self):
        self.use_proxies = False
        self.use_scraperapi = False
        self.proxy_rotator = None
        self.scraperapi_client = None
        
    def setup(self):
        """Setup proxy and ScraperAPI"""
        print("\n" + "="*60)
        print("🔧 SETUP")
        print("="*60 + "\n")
        
        # Ask about proxies
        use_proxy = input("Use proxy rotation? (y/n): ").strip().lower()
        if use_proxy == 'y':
            try:
                self.proxy_rotator = ProxyRotator("config/proxies.txt")
                stats = self.proxy_rotator.get_stats()
                print(f"✅ Loaded {stats['total']} proxies")
                self.use_proxies = True
            except Exception as e:
                print(f"❌ Proxy loading failed: {e}")
        
        # Ask about ScraperAPI
        use_api = input("Use ScraperAPI as fallback? (y/n): ").strip().lower()
        if use_api == 'y':
            try:
                with open('config/scraperapi_key.txt', 'r') as f:
                    api_key = f.read().strip()
                self.scraperapi_client = ScraperAPIClient(api_key=api_key)
                account = self.scraperapi_client.get_account_info()
                if account:
                    remaining = account.get('requestLimit', 0) - account.get('requestCount', 0)
                    print(f"✅ ScraperAPI ready - {remaining} credits remaining")
                self.use_scraperapi = True
            except Exception as e:
                print(f"❌ ScraperAPI setup failed: {e}")
        
        print()
        
    def scrape(self, query, limit=20):
        """
        Scrape search results
        
        Args:
            query: Search query
            limit: Maximum number of ads
            
        Returns:
            list: Scraped ads
        """
        print("="*60)
        print("🚀 SEARCH PAGE SCRAPER")
        print("="*60)
        print(f"📝 Query: {query}")
        print(f"📊 Limit: {limit} ads")
        print(f"🔄 Method: Search page only (fast)")
        print("="*60 + "\n")
        
        ads = []
        
        # Method 1: Direct scraping (no proxy)
        if not self.use_proxies:
            print("🔄 Method 1: Direct connection...\n")
            try:
                scraper = FastSearchScraper(headless=True)
                ads = scraper.search(query=query, limit=limit)
                
                if ads and len(ads) > 0:
                    print(f"\n✅ Success! Found {len(ads)} ads\n")
                    return ads
                else:
                    print(f"\n❌ No results from direct connection\n")
            except Exception as e:
                print(f"\n❌ Direct connection failed: {str(e)[:100]}\n")
        
        # Method 2: Try proxies
        if self.use_proxies and self.proxy_rotator:
            print("🔄 Method 2: Proxy rotation...\n")
            print("🔍 Headless mode: DISABLED (so you can see what's happening)\n")
            stats = self.proxy_rotator.get_stats()
            max_attempts = min(5, stats['available'])
            
            for attempt in range(1, max_attempts + 1):
                proxy = self.proxy_rotator.get_next_proxy()
                print(f"  Attempt {attempt}/{max_attempts}: {proxy[:30]}...")
                
                try:
                    # Disable headless to see browser activity
                    scraper = FastSearchScraper(headless=False, proxy=proxy)
                    ads = scraper.search(query=query, limit=limit)
                    
                    if ads and len(ads) > 0:
                        self.proxy_rotator.mark_success(proxy)
                        print(f"\n✅ Success with proxy! Found {len(ads)} ads\n")
                        return ads
                    else:
                        self.proxy_rotator.mark_failed(proxy)
                        print(f"  ❌ No results")
                        
                except Exception as e:
                    self.proxy_rotator.mark_failed(proxy)
                    print(f"  ❌ Failed: {str(e)[:50]}")
            
            print(f"\n❌ All proxies failed\n")
        
        # Method 3: ScraperAPI fallback
        if self.use_scraperapi and self.scraperapi_client:
            print("🔄 Method 3: ScraperAPI fallback...\n")
            try:
                html = self.scraperapi_client.get_search_results(query, country_code='fr')
                if html:
                    ads = self.scraperapi_client.parse_search_results(html)
                    if ads and len(ads) > 0:
                        ads = ads[:limit]
                        print(f"✅ ScraperAPI success! Found {len(ads)} ads\n")
                        return ads
            except Exception as e:
                print(f"❌ ScraperAPI failed: {e}\n")
        
        print("❌ All methods failed\n")
        return []
    
    def save_results(self, ads, query):
        """Save results to database and Excel"""
        if not ads:
            print("⚠️  No ads to save\n")
            return
        
        print("="*60)
        print("💾 SAVING RESULTS")
        print("="*60 + "\n")
        
        try:
            import pandas as pd
            import os
            
            # Ensure exports directory exists
            os.makedirs('exports', exist_ok=True)
            
            # Save to database
            db = DatabaseHandler()
            result = db.save_ads(ads)
            if isinstance(result, tuple):
                new, updated = result
                print(f"✅ Database: {new} new, {updated} updated")
            else:
                print(f"✅ Database: {result} ads saved")
            
            # Export ONLY current scrape to Excel
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            query_clean = query.replace(' ', '-').lower()
            filename = f"exports/leboncoin-{query_clean}-{len(ads)}ads-{timestamp}.xlsx"
            
            # Create DataFrame from current ads only
            df = pd.DataFrame(ads)
            
            # Reorder columns for better readability
            columns_order = ['title', 'price', 'location', 'url', 'list_id']
            existing_cols = [col for col in columns_order if col in df.columns]
            other_cols = [col for col in df.columns if col not in columns_order]
            df = df[existing_cols + other_cols]
            
            # Export to Excel
            df.to_excel(filename, index=False, engine='openpyxl')
            print(f"✅ Excel: {filename}")
            
            print()
            
        except Exception as e:
            print(f"❌ Save failed: {e}\n")
    
    def show_results(self, ads):
        """Display results"""
        if not ads:
            return
        
        print("="*60)
        print("📊 RESULTS")
        print("="*60 + "\n")
        
        # Statistics
        total = len(ads)
        with_price = sum(1 for ad in ads if ad.get('price'))
        with_location = sum(1 for ad in ads if ad.get('location'))
        
        print(f"Total ads: {total}")
        print(f"With prices: {with_price}/{total} ({with_price/total*100:.1f}%)")
        print(f"With locations: {with_location}/{total} ({with_location/total*100:.1f}%)")
        
        # Price stats
        prices = [ad.get('price') for ad in ads if ad.get('price')]
        if prices:
            print(f"\nPrice range:")
            print(f"  Min: {min(prices)}€")
            print(f"  Max: {max(prices)}€")
            print(f"  Avg: {sum(prices)/len(prices):.2f}€")
        
        # Sample ads
        print(f"\n{'='*60}")
        print("📱 SAMPLE ADS (First 5)")
        print("="*60 + "\n")
        
        for i, ad in enumerate(ads[:5], 1):
            print(f"{i}. {ad.get('title', 'No title')}")
            print(f"   💰 {ad.get('price', 'N/A')}€")
            print(f"   📍 {ad.get('location', 'N/A')}")
            print(f"   🔗 {ad.get('url', 'N/A')[:60]}...")
            print()


def main():
    """Main function"""
    print("\n" + "="*60)
    print("🔍 LEBONCOIN SEARCH PAGE SCRAPER")
    print("="*60)
    print("📄 Extracts data from search results only")
    print("⚡ Fast - no individual page visits")
    print("🔄 Proxy rotation + ScraperAPI fallback")
    print("="*60 + "\n")
    
    # Get inputs
    query = input("Search query (e.g., 'iphone', 'audi'): ").strip()
    if not query:
        print("❌ Query required!")
        return
    
    try:
        limit = int(input("Number of ads (default: 20): ").strip() or "20")
    except ValueError:
        limit = 20
    
    # Initialize scraper
    scraper = SearchPageScraper()
    scraper.setup()
    
    # Scrape
    ads = scraper.scrape(query, limit)
    
    # Show results
    scraper.show_results(ads)
    
    # Save
    if ads:
        save = input("💾 Save to database? (y/n): ").strip().lower()
        if save == 'y':
            scraper.save_results(ads, query)
    
    print("="*60)
    print("✅ DONE!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
