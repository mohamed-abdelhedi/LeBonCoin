"""
Leboncoin Scraper using Scrapling Library
Advanced stealth scraping with anti-detection
"""

import sys
import re
from datetime import datetime
from scrapling.fetchers import StealthyFetcher, StealthySession
from scrapling.parser import Selector
from src.database.db_handler import DatabaseHandler
import pandas as pd
import os
import time


class ScraplingLeboncoinScraper:
    """Leboncoin scraper using Scrapling's StealthyFetcher"""
    
    def __init__(self):
        """Initialize scraper"""
        self.base_url = "https://www.leboncoin.fr"
        self.use_session = False
        self.session = None
        
    def setup(self):
        """Interactive setup"""
        print("="*60)
        print("🔧 SETUP")
        print("="*60 + "\n")
        
        # Ask about session mode
        use_session = input("Use session mode (keeps browser open)? (y/n): ").strip().lower()
        self.use_session = use_session == 'y'
        
        if self.use_session:
            print("✅ Session mode: Browser stays open for multiple requests")
        else:
            print("✅ One-shot mode: Browser opens/closes per request")
        
        print()
    
    def scrape(self, query, limit=20):
        """
        Scrape leboncoin using Scrapling
        
        Args:
            query (str): Search query
            limit (int): Max number of ads
            
        Returns:
            list: Scraped ads
        """
        print("="*60)
        print("🕷️  SCRAPLING STEALTH SCRAPER")
        print("="*60)
        print(f"📝 Query: {query}")
        print(f"📊 Limit: {limit} ads")
        print(f"🔄 Method: StealthyFetcher (Advanced anti-detection)")
        print("="*60 + "\n")
        
        all_ads = []
        
        try:
            # Calculate pages needed
            ads_per_page = 35
            max_pages = max(1, (limit + ads_per_page - 1) // ads_per_page)
            
            print(f"📄 Will scan up to {max_pages} page(s)\n")
            
            if self.use_session:
                # Use session mode (keeps browser open)
                with StealthySession(headless=False) as session:
                    for page_num in range(1, max_pages + 1):
                        if len(all_ads) >= limit:
                            break
                        
                        ads = self._scrape_page(session, query, page_num, limit - len(all_ads))
                        all_ads.extend(ads)
                        
                        if not ads or len(ads) == 0:
                            print(f"  No more ads on page {page_num}, stopping\n")
                            break
                        
                        print(f"  ✅ Page {page_num}: Found {len(ads)} ads (Total: {len(all_ads)})\n")
                        
                        if page_num < max_pages and len(all_ads) < limit:
                            time.sleep(2)  # Delay between pages
            else:
                # Use one-shot mode (opens/closes browser per request)
                for page_num in range(1, max_pages + 1):
                    if len(all_ads) >= limit:
                        break
                    
                    ads = self._scrape_page_oneshot(query, page_num, limit - len(all_ads))
                    all_ads.extend(ads)
                    
                    if not ads or len(ads) == 0:
                        print(f"  No more ads on page {page_num}, stopping\n")
                        break
                    
                    print(f"  ✅ Page {page_num}: Found {len(ads)} ads (Total: {len(all_ads)})\n")
                    
                    if page_num < max_pages and len(all_ads) < limit:
                        time.sleep(2)
            
            print(f"\n🎉 Success! Scraped {len(all_ads)} ads\n")
            return all_ads[:limit]
            
        except KeyboardInterrupt:
            print("\n⚠️  Interrupted by user\n")
            return all_ads
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
            return all_ads
    
    def _scrape_page_oneshot(self, query, page_num, max_ads):
        """Scrape single page using one-shot mode"""
        url = self._build_url(query, page_num)
        print(f"  🔄 Fetching page {page_num}...")
        
        try:
            # One-shot request (opens and closes browser)
            page = StealthyFetcher.fetch(
                url,
                headless=False,
                network_idle=True,
                google_search=False
            )
            
            return self._extract_ads(page, max_ads)
            
        except Exception as e:
            print(f"  ❌ Page {page_num} failed: {str(e)[:80]}")
            return []
    
    def _scrape_page(self, session, query, page_num, max_ads):
        """Scrape single page using session"""
        url = self._build_url(query, page_num)
        print(f"  🔄 Fetching page {page_num}...")
        
        try:
            page = session.fetch(
                url,
                network_idle=True,
                google_search=False
            )
            
            return self._extract_ads(page, max_ads)
            
        except Exception as e:
            print(f"  ❌ Page {page_num} failed: {str(e)[:80]}")
            return []
    
    def _build_url(self, query, page_num):
        """Build search URL"""
        params = [f"text={query}"]
        if page_num > 1:
            params.append(f"page={page_num}")
        return f"{self.base_url}/recherche?" + "&".join(params)
    
    def _extract_ads(self, page, max_ads):
        """Extract ads from page using Scrapling selectors"""
        ads = []
        
        try:
            # Select the ARTICLE tags with data-qa-id="aditem_container"
            ad_cards = page.css('article[data-qa-id="aditem_container"]')
            
            if not ad_cards:
                # Fallback: try data-test-id
                ad_cards = page.css('article[data-test-id="ad"]')
            
            for card in ad_cards[:max_ads]:
                try:
                    ad = self._parse_ad_card(card)
                    if ad and ad.get('url'):
                        ads.append(ad)
                except Exception as e:
                    continue
            
            return ads
            
        except Exception as e:
            return []
    
    def _parse_ad_card(self, card):
        """Parse individual ad card (article element)"""
        ad = {}
        
        try:
            # Find the <a> tag inside the article to get the URL
            link = card.css_first('a[href*="/ad/"]')
            if not link:
                return None
            
            # URL - Get href from the link element
            url = link.attrib.get('href', '') if hasattr(link, 'attrib') else ''
            if not url:
                # Try XPath method
                url_list = link.xpath('./@href').getall()
                url = url_list[0] if url_list else ''
            
            if not url:
                return None
            
            if url and not url.startswith('http'):
                url = self.base_url + url
            ad['url'] = url
            
            # Extract list_id from URL
            if '/ad/' in url:
                list_id = url.split('/ad/')[-1].split('/')[0].split('?')[0]
                ad['list_id'] = list_id
            else:
                return None
            
            # Title - correct selector
            title_elem = card.css_first('p[data-test-id="adcard-title"]')
            if title_elem and hasattr(title_elem, 'text'):
                ad['title'] = title_elem.text.strip()
            
            # Price - extract from HTML string directly (Scrapling's .text seems unreliable for nested elements)
            price_elem = card.css_first('p[data-test-id="price"]')
            if price_elem:
                # Get the full HTML of the price element
                price_html = str(price_elem)
                # Extract text between <span> tags - try multiple patterns
                # Pattern 1: <span class="">38 900€</span>
                price_match = re.search(r'<span[^>]*>([\d\s\xa0\u202f]+)€?</span>', price_html)
                if not price_match:
                    # Pattern 2: Any text with digits in span
                    price_match = re.search(r'<span[^>]*>([^<]*\d[^<]*)€?</span>', price_html)
                if not price_match:
                    # Pattern 3: Just find any digits with spaces
                    price_match = re.search(r'([\d\s\xa0\u202f]+)\s*€', price_html)
                
                if price_match:
                    price_text = price_match.group(1).strip()
                    try:
                        # Remove all spaces, non-breaking spaces, and narrow no-break spaces (\u202f)
                        price_str = price_text.replace(' ', '').replace('\xa0', '').replace('\u202f', '')
                        price = int(price_str)
                        ad['price'] = price
                    except:
                        pass
            
            # Location - get all text-caption paragraphs and find the one with location
            caption_elems = card.css('p.text-caption.text-neutral')
            if caption_elems and len(caption_elems) > 0:
                for elem in caption_elems:
                    if hasattr(elem, 'text'):
                        text = elem.text.strip()
                        # Location usually has a postal code (5 digits)
                        if re.search(r'\d{5}', text):
                            ad['location'] = text
                            break
                
                # Category is usually the first caption
                if len(caption_elems) > 0 and hasattr(caption_elems[0], 'text'):
                    ad['category_name'] = caption_elems[0].text.strip()
            
            return ad
            
        except Exception as e:
            return None
    
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
            filename = f"exports/leboncoin-scrapling-{query_clean}-{len(ads)}ads-{timestamp}.xlsx"
            
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
        """Display results statistics"""
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
            print(f"{i}. {ad.get('title', 'N/A')}")
            print(f"   💰 {ad.get('price', 'N/A')}€")
            print(f"   📍 {ad.get('location', 'N/A')}")
            print(f"   🔗 {ad.get('url', 'N/A')[:80]}...")
            print()


def main():
    """Main function"""
    print("\n" + "="*60)
    print("🕷️  LEBONCOIN SCRAPLING SCRAPER")
    print("="*60)
    print("📄 Advanced stealth scraping with anti-detection")
    print("⚡ Uses Scrapling's StealthyFetcher")
    print("🔒 Modified Firefox with fingerprint spoofing")
    print("="*60 + "\n")
    
    # Get user input
    query = input("Search query (e.g., 'iphone', 'audi'): ").strip()
    if not query:
        print("❌ Query is required")
        return
    
    limit_input = input("Number of ads (default: 20): ").strip()
    limit = int(limit_input) if limit_input else 20
    
    # Initialize scraper
    scraper = ScraplingLeboncoinScraper()
    scraper.setup()
    
    # Start scraping
    start_time = time.time()
    ads = scraper.scrape(query=query, limit=limit)
    elapsed = time.time() - start_time
    
    # Show results
    scraper.show_results(ads)
    
    # Save option
    if ads:
        save = input("\n💾 Save to database? (y/n): ").strip().lower()
        if save == 'y':
            scraper.save_results(ads, query)
    
    # Summary
    print("="*60)
    print("✅ DONE!")
    print("="*60)
    print(f"⏱️  Time: {elapsed:.1f} seconds")
    print(f"📊 Scraped: {len(ads)} ads")
    if ads:
        print(f"⚡ Speed: {len(ads)/elapsed:.2f} ads/second")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)
