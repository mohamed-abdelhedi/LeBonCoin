"""
Proxy Rotator
Automatically rotates through multiple proxies until one works
"""

import random
from typing import List, Optional
from src.utils.proxy_config import ProxyConfig
import logging

class ProxyRotator:
    """Manage and rotate through multiple proxies"""
    
    def __init__(self, proxy_file: str = "config/proxies.txt"):
        """
        Initialize proxy rotator
        
        Args:
            proxy_file: Path to file with proxy list (one per line)
        """
        self.proxy_file = proxy_file
        self.proxies = []
        self.current_index = 0
        self.failed_proxies = set()
        self.logger = logging.getLogger(__name__)
        
        self.load_proxies()
    
    def load_proxies(self):
        """Load proxies from file"""
        try:
            with open(self.proxy_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Validate proxy format
                try:
                    proxy_config = ProxyConfig(line)
                    if proxy_config.proxy_dict:
                        self.proxies.append(line)
                        self.logger.debug(f"✅ Loaded proxy: {line[:30]}...")
                except ValueError as e:
                    self.logger.warning(f"⚠️  Invalid proxy skipped: {line} - {e}")
                    continue
            
            if self.proxies:
                self.logger.info(f"📡 Loaded {len(self.proxies)} valid proxies")
            else:
                self.logger.warning("⚠️  No valid proxies found in file")
                
        except FileNotFoundError:
            self.logger.error(f"❌ Proxy file not found: {self.proxy_file}")
            self.proxies = []
        except Exception as e:
            self.logger.error(f"❌ Error loading proxies: {e}")
            self.proxies = []
    
    def get_next_proxy(self) -> Optional[str]:
        """
        Get next available proxy
        
        Returns:
            str: Proxy string or None if no proxies available
        """
        if not self.proxies:
            return None
        
        # Filter out failed proxies
        available = [p for p in self.proxies if p not in self.failed_proxies]
        
        if not available:
            self.logger.warning("⚠️  All proxies failed! Resetting failed list...")
            self.failed_proxies.clear()
            available = self.proxies.copy()
        
        # Get next proxy (round-robin)
        proxy = available[self.current_index % len(available)]
        self.current_index += 1
        
        self.logger.info(f"🔄 Using proxy: {proxy[:30]}...")
        return proxy
    
    def get_random_proxy(self) -> Optional[str]:
        """
        Get random available proxy
        
        Returns:
            str: Random proxy string or None
        """
        if not self.proxies:
            return None
        
        # Filter out failed proxies
        available = [p for p in self.proxies if p not in self.failed_proxies]
        
        if not available:
            self.logger.warning("⚠️  All proxies failed! Resetting...")
            self.failed_proxies.clear()
            available = self.proxies.copy()
        
        proxy = random.choice(available)
        self.logger.info(f"🎲 Random proxy: {proxy[:30]}...")
        return proxy
    
    def mark_failed(self, proxy: str):
        """
        Mark proxy as failed
        
        Args:
            proxy: Proxy string that failed
        """
        self.failed_proxies.add(proxy)
        self.logger.warning(f"❌ Proxy marked as failed: {proxy[:30]}...")
        
        remaining = len(self.proxies) - len(self.failed_proxies)
        self.logger.info(f"📊 Remaining proxies: {remaining}/{len(self.proxies)}")
    
    def mark_success(self, proxy: str):
        """
        Mark proxy as successful (remove from failed list)
        
        Args:
            proxy: Proxy string that succeeded
        """
        if proxy in self.failed_proxies:
            self.failed_proxies.remove(proxy)
            self.logger.info(f"✅ Proxy restored: {proxy[:30]}...")
    
    def get_stats(self) -> dict:
        """Get proxy statistics"""
        return {
            'total': len(self.proxies),
            'failed': len(self.failed_proxies),
            'available': len(self.proxies) - len(self.failed_proxies),
            'success_rate': (len(self.proxies) - len(self.failed_proxies)) / len(self.proxies) * 100 if self.proxies else 0
        }
    
    def reset_failed(self):
        """Reset all failed proxies (give them another chance)"""
        self.failed_proxies.clear()
        self.logger.info("🔄 All proxies reset and available again")
    
    def has_proxies(self) -> bool:
        """Check if any proxies are available"""
        return len(self.proxies) > 0


def test_proxy_rotator():
    """Test proxy rotator"""
    print("\n" + "="*80)
    print("🧪 PROXY ROTATOR TEST")
    print("="*80 + "\n")
    
    rotator = ProxyRotator("config/proxies.txt")
    
    if not rotator.has_proxies():
        print("❌ No proxies loaded!")
        print("   Add proxies to config/proxies.txt")
        return
    
    print(f"✅ Loaded {len(rotator.proxies)} proxies\n")
    
    # Test getting proxies
    print("🔄 Testing rotation (next proxy):")
    for i in range(min(5, len(rotator.proxies))):
        proxy = rotator.get_next_proxy()
        print(f"  {i+1}. {proxy}")
    print()
    
    # Test random selection
    print("🎲 Testing random selection:")
    for i in range(3):
        proxy = rotator.get_random_proxy()
        print(f"  {i+1}. {proxy}")
    print()
    
    # Test failure handling
    print("❌ Testing failure handling:")
    proxy = rotator.get_next_proxy()
    print(f"  Current proxy: {proxy}")
    rotator.mark_failed(proxy)
    print(f"  Marked as failed")
    
    stats = rotator.get_stats()
    print(f"\n📊 Statistics:")
    print(f"   Total: {stats['total']}")
    print(f"   Available: {stats['available']}")
    print(f"   Failed: {stats['failed']}")
    print(f"   Success rate: {stats['success_rate']:.1f}%")
    print()


if __name__ == "__main__":
    test_proxy_rotator()
