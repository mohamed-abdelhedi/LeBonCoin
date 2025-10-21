"""
Leboncoin JSON Scraper using Scrapling Library
Advanced stealth scraping with JSON output
"""

import sys
import re
import json
from datetime import datetime
from scrapling.fetchers import StealthyFetcher, StealthySession
from scrapling.parser import Selector
import os
import time


class JSONLeboncoinScraper:
    """Leboncoin scraper with JSON export using Scrapling's StealthyFetcher"""
    
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
        print("📋 LEBONCOIN JSON SCRAPER")
        print("="*60)
        print(f"📝 Query: {query}")
        print(f"📊 Limit: {limit} ads")
        print(f"🔄 Method: StealthyFetcher (Advanced anti-detection)")
        print(f"💾 Output: JSON format")
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
            
            # Price - extract from HTML string directly
            price_elem = card.css_first('p[data-test-id="price"]')
            if price_elem:
                # Get the full HTML of the price element
                price_html = str(price_elem)
                # Extract text between <span> tags - try multiple patterns
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
            
            # Add metadata
            ad['scraped_at'] = datetime.now().isoformat()
            
            return ad
            
        except Exception as e:
            return None
    
    def save_to_json(self, ads, query, output_format='pretty'):
        """
        Save results to JSON file
        
        Args:
            ads (list): List of ad dictionaries
            query (str): Search query
            output_format (str): 'pretty' for readable, 'compact' for minified
            
        Returns:
            str: Path to saved JSON file
        """
        if not ads:
            print("⚠️  No ads to save\n")
            return None
        
        print("="*60)
        print("💾 SAVING TO JSON")
        print("="*60 + "\n")
        
        # Create exports folder if needed
        os.makedirs('exports', exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"exports/leboncoin-{query}-{len(ads)}ads-{timestamp}.json"
        
        # Prepare data structure
        output_data = {
            "metadata": {
                "query": query,
                "total_ads": len(ads),
                "scraped_at": datetime.now().isoformat(),
                "scraper": "Scrapling JSON Scraper v1.0",
                "method": "StealthyFetcher"
            },
            "ads": ads
        }
        
        # Calculate statistics
        prices = [ad['price'] for ad in ads if 'price' in ad and ad['price']]
        if prices:
            output_data["statistics"] = {
                "total_with_price": len(prices),
                "min_price": min(prices),
                "max_price": max(prices),
                "avg_price": round(sum(prices) / len(prices), 2),
                "median_price": sorted(prices)[len(prices)//2]
            }
        
        # Save to file
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                if output_format == 'pretty':
                    json.dump(output_data, f, ensure_ascii=False, indent=2)
                else:
                    json.dump(output_data, f, ensure_ascii=False)
            
            file_size = os.path.getsize(filename)
            print(f"✅ JSON file saved: {filename}")
            print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            print(f"📋 Format: {output_format.capitalize()}")
            print(f"🔢 Total ads: {len(ads)}")
            
            if prices:
                print(f"\n💰 Price Statistics:")
                print(f"  • Range: €{min(prices):,} - €{max(prices):,}")
                print(f"  • Average: €{output_data['statistics']['avg_price']:,.2f}")
                print(f"  • Median: €{output_data['statistics']['median_price']:,}")
            
            print()
            return filename
            
        except Exception as e:
            print(f"❌ Error saving JSON: {e}\n")
            return None
    
    def display_preview(self, ads, limit=5):
        """Display a preview of scraped ads"""
        if not ads:
            print("⚠️  No ads to display\n")
            return
        
        print("="*60)
        print(f"📋 PREVIEW (showing {min(limit, len(ads))} of {len(ads)} ads)")
        print("="*60 + "\n")
        
        for i, ad in enumerate(ads[:limit], 1):
            print(f"{i}. {ad.get('title', 'N/A')}")
            if 'price' in ad:
                print(f"   💰 €{ad['price']:,}")
            if 'location' in ad:
                print(f"   📍 {ad['location']}")
            if 'url' in ad:
                print(f"   🔗 {ad['url']}")
            print()


def main():
    """Main function"""
    print("="*60)
    print("📋 LEBONCOIN JSON SCRAPER")
    print("="*60)
    print("📄 Advanced stealth scraping with JSON output")
    print("⚡ Uses Scrapling's StealthyFetcher")
    print("🔒 Modified Firefox with fingerprint spoofing")
    print("="*60 + "\n")
    
    # Get user input
    query = input("Search query (e.g., 'iphone', 'audi'): ").strip()
    if not query:
        print("❌ Query cannot be empty")
        return
    
    limit_input = input("Number of ads (default: 20): ").strip()
    limit = int(limit_input) if limit_input.isdigit() else 20
    
    # Initialize scraper
    scraper = JSONLeboncoinScraper()
    scraper.setup()
    
    # Scrape
    start_time = time.time()
    ads = scraper.scrape(query, limit)
    elapsed = time.time() - start_time
    
    # Display preview
    if ads:
        scraper.display_preview(ads, limit=5)
        
        # Ask about JSON format
        print("JSON Output Format:")
        print("1. Pretty (readable, formatted with indentation)")
        print("2. Compact (minified, smaller file size)")
        format_choice = input("\nChoose format (1/2, default: 1): ").strip()
        output_format = 'compact' if format_choice == '2' else 'pretty'
        
        # Save to JSON
        json_file = scraper.save_to_json(ads, query, output_format)
        
        if json_file:
            print("="*60)
            print("✅ DONE!")
            print("="*60)
            print(f"⏱️  Time: {elapsed:.1f} seconds")
            print(f"📊 Scraped: {len(ads)} ads")
            print(f"💾 Saved: {json_file}")
            print("="*60 + "\n")
    else:
        print("="*60)
        print("⚠️  NO RESULTS")
        print("="*60)
        print(f"⏱️  Time: {elapsed:.1f} seconds")
        print("📊 Scraped: 0 ads")
        print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user\n")
    except Exception as e:
        print(f"\n\n❌ Error: {e}\n")
