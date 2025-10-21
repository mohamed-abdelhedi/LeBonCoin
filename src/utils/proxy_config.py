"""
Proxy Configuration Manager
Supports multiple proxy formats:
- IP:PORT
- USERNAME:PASSWORD@IP:PORT
- http://IP:PORT
- http://USERNAME:PASSWORD@IP:PORT
"""

import re
from typing import Optional, Dict

class ProxyConfig:
    """Handle proxy configuration and formatting"""
    
    def __init__(self, proxy_string: Optional[str] = None):
        """
        Initialize proxy configuration
        
        Args:
            proxy_string: Proxy in various formats:
                - "IP:PORT" → "127.0.0.1:8080"
                - "USERNAME:PASSWORD@IP:PORT" → "user:pass@127.0.0.1:8080"
                - "http://IP:PORT"
                - "http://USERNAME:PASSWORD@IP:PORT"
        """
        self.proxy_string = proxy_string
        self.proxy_dict = None
        
        if proxy_string:
            self.proxy_dict = self.parse_proxy(proxy_string)
    
    def parse_proxy(self, proxy_string: str) -> Optional[Dict[str, str]]:
        """
        Parse proxy string into Chrome-compatible format
        
        Args:
            proxy_string: Proxy in various formats
            
        Returns:
            dict: Proxy configuration for Chrome
        """
        if not proxy_string or not proxy_string.strip():
            return None
        
        proxy = proxy_string.strip()
        
        # Pattern 1: IP:PORT (simplest)
        # Example: 127.0.0.1:8080
        pattern1 = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)$'
        match = re.match(pattern1, proxy)
        if match:
            ip, port = match.groups()
            return {
                'http': f'http://{ip}:{port}',
                'https': f'http://{ip}:{port}',
                'chrome_arg': f'--proxy-server=http://{ip}:{port}'
            }
        
        # Pattern 2: USERNAME:PASSWORD@IP:PORT
        # Example: user:pass@127.0.0.1:8080
        pattern2 = r'^([^:]+):([^@]+)@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)$'
        match = re.match(pattern2, proxy)
        if match:
            username, password, ip, port = match.groups()
            return {
                'http': f'http://{username}:{password}@{ip}:{port}',
                'https': f'http://{username}:{password}@{ip}:{port}',
                'chrome_arg': f'--proxy-server=http://{ip}:{port}',
                'username': username,
                'password': password
            }
        
        # Pattern 3: http://IP:PORT
        # Example: http://127.0.0.1:8080
        pattern3 = r'^https?://(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)$'
        match = re.match(pattern3, proxy)
        if match:
            return {
                'http': proxy,
                'https': proxy,
                'chrome_arg': f'--proxy-server={proxy}'
            }
        
        # Pattern 4: http://USERNAME:PASSWORD@IP:PORT (full format)
        # Example: http://user:pass@127.0.0.1:8080
        pattern4 = r'^https?://([^:]+):([^@]+)@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)$'
        match = re.match(pattern4, proxy)
        if match:
            username, password, ip, port = match.groups()
            return {
                'http': proxy,
                'https': proxy,
                'chrome_arg': f'--proxy-server=http://{ip}:{port}',
                'username': username,
                'password': password
            }
        
        # Pattern 5: hostname:port (for proxy services)
        # Example: proxy.example.com:8080
        pattern5 = r'^([a-zA-Z0-9.-]+):(\d+)$'
        match = re.match(pattern5, proxy)
        if match:
            host, port = match.groups()
            return {
                'http': f'http://{host}:{port}',
                'https': f'http://{host}:{port}',
                'chrome_arg': f'--proxy-server=http://{host}:{port}'
            }
        
        # Pattern 6: USERNAME:PASSWORD@hostname:port
        # Example: user:pass@proxy.example.com:8080
        pattern6 = r'^([^:]+):([^@]+)@([a-zA-Z0-9.-]+):(\d+)$'
        match = re.match(pattern6, proxy)
        if match:
            username, password, host, port = match.groups()
            return {
                'http': f'http://{username}:{password}@{host}:{port}',
                'https': f'http://{username}:{password}@{host}:{port}',
                'chrome_arg': f'--proxy-server=http://{host}:{port}',
                'username': username,
                'password': password
            }
        
        # Invalid format
        raise ValueError(
            f"Invalid proxy format: {proxy}\n"
            f"Supported formats:\n"
            f"  - IP:PORT (e.g., 127.0.0.1:8080)\n"
            f"  - USERNAME:PASSWORD@IP:PORT\n"
            f"  - http://IP:PORT\n"
            f"  - http://USERNAME:PASSWORD@IP:PORT"
        )
    
    def get_chrome_argument(self) -> Optional[str]:
        """Get Chrome proxy argument"""
        if self.proxy_dict:
            return self.proxy_dict.get('chrome_arg')
        return None
    
    def get_requests_dict(self) -> Optional[Dict[str, str]]:
        """Get proxy dict for requests library"""
        if self.proxy_dict:
            return {
                'http': self.proxy_dict['http'],
                'https': self.proxy_dict['https']
            }
        return None
    
    def has_auth(self) -> bool:
        """Check if proxy has authentication"""
        return self.proxy_dict and 'username' in self.proxy_dict
    
    def get_credentials(self) -> Optional[tuple]:
        """Get username and password if available"""
        if self.has_auth():
            return (self.proxy_dict['username'], self.proxy_dict['password'])
        return None
    
    def test_format(self) -> Dict[str, any]:
        """Test and show parsed proxy configuration"""
        if not self.proxy_dict:
            return {'valid': False, 'error': 'No proxy configured'}
        
        result = {
            'valid': True,
            'chrome_arg': self.get_chrome_argument(),
            'requests_dict': self.get_requests_dict(),
            'has_auth': self.has_auth(),
        }
        
        if self.has_auth():
            username, password = self.get_credentials()
            result['username'] = username
            result['password'] = '***' + password[-3:] if len(password) > 3 else '***'
        
        return result


def test_proxy_formats():
    """Test various proxy formats"""
    print("\n" + "="*80)
    print("🧪 PROXY FORMAT TESTER")
    print("="*80 + "\n")
    
    test_cases = [
        # Simple IP:PORT
        "127.0.0.1:8080",
        "192.168.1.100:3128",
        
        # With authentication
        "user:pass@127.0.0.1:8080",
        "myuser:mypass123@192.168.1.100:3128",
        
        # Full HTTP format
        "http://127.0.0.1:8080",
        "http://user:pass@127.0.0.1:8080",
        
        # Hostname
        "proxy.example.com:8080",
        "user:pass@proxy.example.com:8080",
        
        # Invalid formats
        "invalid",
        "127.0.0.1",
        "http://example.com",
    ]
    
    for proxy_str in test_cases:
        print(f"Testing: {proxy_str}")
        try:
            proxy = ProxyConfig(proxy_str)
            result = proxy.test_format()
            
            if result['valid']:
                print(f"  ✅ Valid!")
                print(f"     Chrome arg: {result['chrome_arg']}")
                print(f"     Has auth: {result['has_auth']}")
                if result['has_auth']:
                    print(f"     Username: {result['username']}")
                    print(f"     Password: {result['password']}")
            else:
                print(f"  ❌ Invalid: {result['error']}")
                
        except ValueError as e:
            print(f"  ❌ Error: {str(e).split(chr(10))[0]}")
        
        print()


if __name__ == "__main__":
    test_proxy_formats()
