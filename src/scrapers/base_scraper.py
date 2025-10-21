"""
Base Scraper Class
Contains common functionality for all scrapers
"""

import logging
import time
import random
from datetime import datetime

class BaseScraper:
    """Base class for all scrapers"""
    
    def __init__(self, min_delay=1.0, max_delay=3.0):
        """
        Initialize base scraper
        
        Args:
            min_delay (float): Minimum delay between requests
            max_delay (float): Maximum delay between requests
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.logger = self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/scraper.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)
    
    def rate_limit(self):
        """Apply rate limiting between requests"""
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)
    
    def extract_price(self, price_text):
        """
        Extract numeric price from text
        
        Args:
            price_text (str): Text containing price
            
        Returns:
            float: Extracted price or None
        """
        if not price_text:
            return None
        
        import re
        price_text = price_text.replace('€', '').replace(' ', '').replace('\xa0', '')
        match = re.search(r'([0-9,\.]+)', price_text)
        
        if match:
            try:
                price_str = match.group(1).replace(',', '')
                return float(price_str)
            except ValueError:
                return None
        return None
    
    def extract_ad_id(self, url):
        """
        Extract ad ID from URL
        
        Args:
            url (str): Leboncoin URL
            
        Returns:
            int: Ad ID or None
        """
        if not url:
            return None
        
        import re
        # Try pattern: /1234567.htm
        match = re.search(r'/(\d+)\.htm', url)
        if match:
            return int(match.group(1))
        
        # Try pattern: /ad/category/1234567
        match = re.search(r'/ad/[^/]+/(\d+)', url)
        if match:
            return int(match.group(1))
        
        return None
