"""
Database Handler
Manages SQLite database operations
"""

import sqlite3
import logging
from datetime import datetime
import hashlib

class DatabaseHandler:
    """Handle all database operations"""
    
    def __init__(self, db_path="data/leboncoin.db"):
        """
        Initialize database handler
        
        Args:
            db_path (str): Path to SQLite database
        """
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        self.initialize()
    
    def initialize(self):
        """Initialize database with schema"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Read schema file
            with open('config/schema.sql', 'r', encoding='utf-8') as f:
                schema = f.read()
            
            # Execute schema
            for statement in schema.split(';'):
                if statement.strip() and 'CREATE TABLE' in statement:
                    cursor.execute(statement)
            
            # Insert default categories
            self._insert_default_categories(cursor)
            
            conn.commit()
            conn.close()
            
            self.logger.info(f"Database initialized: {self.db_path}")
            
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
            raise
    
    def _insert_default_categories(self, cursor):
        """Insert default categories"""
        categories = [
            (1, "Véhicules", None),
            (2, "Voitures", 1),
            (3, "Motos", 1),
            (8, "Immobilier", None),
            (9, "Ventes immobilières", 8),
            (10, "Locations", 8),
            (14, "Multimédia", None),
            (15, "Informatique", 14)
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO categories (category_id, category_name, parent_category_id) VALUES (?, ?, ?)",
            categories
        )
    
    def save_ads(self, ads, session_id=None):
        """
        Save ads to database
        
        Args:
            ads (list): List of ad dictionaries
            session_id (str): Scraping session ID
            
        Returns:
            tuple: (inserted_count, updated_count)
        """
        if not session_id:
            session_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        inserted = 0
        updated = 0
        
        for ad in ads:
            try:
                # Check if exists
                cursor.execute("SELECT ad_id FROM ads WHERE list_id = ?", (ad.get('list_id'),))
                existing = cursor.fetchone()
                
                if existing:
                    # Update
                    cursor.execute("""
                        UPDATE ads SET 
                            title = ?, description = ?, price = ?, url = ?, 
                            category_name = ?, updated_at = ?
                        WHERE list_id = ?
                    """, (
                        ad.get('title'),
                        ad.get('description', ''),
                        ad.get('price'),
                        ad.get('url'),
                        ad.get('category', 'Unknown'),
                        datetime.now().isoformat(),
                        ad.get('list_id')
                    ))
                    updated += 1
                else:
                    # Insert
                    cursor.execute("""
                        INSERT INTO ads (
                            list_id, title, description, price, url,
                            category_name, ad_type, status, created_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        ad.get('list_id'),
                        ad.get('title'),
                        ad.get('description', ''),
                        ad.get('price'),
                        ad.get('url'),
                        ad.get('category', 'Unknown'),
                        'offer',
                        'active',
                        datetime.now().isoformat()
                    ))
                    inserted += 1
                    
            except Exception as e:
                self.logger.warning(f"Failed to save ad: {e}")
                continue
        
        # Log scraping session
        cursor.execute("""
            INSERT INTO scraping_logs (
                scraping_session_id, ads_found, ads_inserted, ads_updated, scraping_date
            ) VALUES (?, ?, ?, ?, ?)
        """, (session_id, len(ads), inserted, updated, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        
        self.logger.info(f"Database updated: {inserted} inserted, {updated} updated")
        
        return (inserted, updated)
    
    def get_ads(self, limit=None, category=None):
        """
        Get ads from database
        
        Args:
            limit (int): Maximum results
            category (str): Filter by category
            
        Returns:
            list: List of ad tuples
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT * FROM ads"
        params = []
        
        if category:
            query += " WHERE category_name = ?"
            params.append(category)
        
        query += " ORDER BY created_at DESC"
        
        if limit:
            query += " LIMIT ?"
            params.append(limit)
        
        cursor.execute(query, params)
        ads = cursor.fetchall()
        
        conn.close()
        return ads
    
    def get_statistics(self):
        """
        Get database statistics
        
        Returns:
            dict: Statistics dictionary
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Total ads
        cursor.execute("SELECT COUNT(*) FROM ads")
        stats['total_ads'] = cursor.fetchone()[0]
        
        # Categories
        cursor.execute("SELECT COUNT(DISTINCT category_name) FROM ads")
        stats['categories'] = cursor.fetchone()[0]
        
        # Ads with prices
        cursor.execute("SELECT COUNT(*) FROM ads WHERE price IS NOT NULL")
        stats['ads_with_prices'] = cursor.fetchone()[0]
        
        # Price statistics
        cursor.execute("""
            SELECT MIN(price), MAX(price), AVG(price), SUM(price)
            FROM ads WHERE price IS NOT NULL
        """)
        min_p, max_p, avg_p, total = cursor.fetchone()
        
        stats['price_min'] = min_p or 0
        stats['price_max'] = max_p or 0
        stats['price_avg'] = avg_p or 0
        stats['price_total'] = total or 0
        
        conn.close()
        return stats
    
    def export_to_csv(self, filename=None, query_name=None, mode='new'):
        """
        Export ads to CSV with custom naming
        
        Args:
            filename (str): Custom filename (auto-generated if None)
            query_name (str): Search query name for filename
            mode (str): 'new' = create new file (default), 'append' = append to existing
            
        Returns:
            str: Filename
        """
        import pandas as pd
        import os
        import re
        
        # Ensure exports directory exists
        os.makedirs('exports', exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        
        query = """
            SELECT 
                a.list_id, a.title, a.description, a.price,
                a.category_name, a.url, a.created_at, a.updated_at
            FROM ads a
            ORDER BY a.created_at DESC
        """
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        if not filename:
            # Generate filename: website-product-count-timestamp.csv
            website = "leboncoin"
            
            # Clean query name for filename (remove special chars)
            if query_name:
                product = re.sub(r'[^\w\s-]', '', query_name)
                product = re.sub(r'[\s]+', '_', product)
                product = product[:30]  # Limit length
            else:
                product = "search"
            
            count = len(df)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            filename = f"exports/{website}-{product}-{count}ads-{timestamp}.csv"
        
        # Write mode: 'w' = overwrite (new), 'a' = append
        write_mode = 'w'  # ALWAYS CREATE NEW FILE
        write_header = True
        
        df.to_csv(filename, index=False, encoding='utf-8', mode=write_mode, header=write_header)
        
        action = "created"
        self.logger.info(f"Data {action}: {filename} ({len(df)} rows)")
        return filename
