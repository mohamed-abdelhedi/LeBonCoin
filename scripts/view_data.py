"""
VIEW DATA
Simple script to view scraped data
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.database import DatabaseHandler

def main():
    """View data from database"""
    
    print("=" * 70)
    print("DATA VIEWER")
    print("=" * 70)
    print()
    
    try:
        db = DatabaseHandler()
        
        # Get statistics
        stats = db.get_statistics()
        
        print("STATISTICS:")
        print(f"  Total ads: {stats['total_ads']}")
        print(f"  Categories: {stats['categories']}")
        print(f"  Ads with prices: {stats['ads_with_prices']}")
        
        if stats['ads_with_prices'] > 0:
            print(f"\nPRICE STATISTICS:")
            print(f"  Minimum: {stats['price_min']:,.2f} EUR")
            print(f"  Maximum: {stats['price_max']:,.2f} EUR")
            print(f"  Average: {stats['price_avg']:,.2f} EUR")
            print(f"  Total value: {stats['price_total']:,.2f} EUR")
        
        # Get recent ads
        print("\n" + "=" * 70)
        print("RECENT ADS (Last 10)")
        print("=" * 70)
        print()
        
        ads = db.get_ads(limit=10)
        
        for i, ad in enumerate(ads, 1):
            # ad structure: (ad_id, list_id, title, description, price, ...)
            print(f"[{i}] {ad[2]}")  # title
            if ad[4]:  # price
                print(f"    Price: {ad[4]:,.2f} EUR")
            if ad[14]:  # url
                print(f"    URL: {ad[14][:60]}...")
            print()
        
        # Options
        print("=" * 70)
        print("\nOptions:")
        print("1. Export to CSV")
        print("2. View by category")
        print("3. Exit")
        
        choice = input("\nChoose (1-3): ").strip()
        
        if choice == '1':
            filename = db.export_to_csv()
            print(f"\nExported to: {filename}")
            print(f"Open with: start {filename}")
        
        elif choice == '2':
            category = input("Enter category name: ").strip()
            ads = db.get_ads(category=category, limit=20)
            print(f"\nFound {len(ads)} ads in category '{category}'")
            for i, ad in enumerate(ads[:10], 1):
                print(f"{i}. {ad[2]}")  # title
        
        print("\nDone!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
