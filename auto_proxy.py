import requests
from threading import Thread
from utilitys import logger
from re import compile


REGEX = compile(r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
                + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
                + r")(?:\D|$)")


class Proxy:
    def __init__(self, http_sources, socks4_sources, socks5_sources):
        self.http_sources = http_sources
        self.socks4_sources = socks4_sources
        self.socks5_sources = socks5_sources
        self.proxies = []


    def scrap(self, sources, proxy_type):
        for source_url in [s for s in sources if s]:
            try: response = requests.get(
                source_url, timeout=15, 
                headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
            )
            except Exception as e: logger(e)
            if tuple(REGEX.finditer(response.text)):
                for proxy in tuple(REGEX.finditer(response.text)):
                    self.proxies.append( (proxy_type, proxy.group(1)) )


    def init(self):
        threads = []
        self.proxies.clear()
        for i in (
        (self.http_sources, 'http'), 
        (self.socks4_sources, 'socks4'), 
        (self.socks5_sources, 'socks5') ):
            thread = Thread(target=self.scrap, args=(*i, ))
            threads.append(thread)
            thread.start()
        for t in threads:  t.join()
        
    
