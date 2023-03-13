import requests
from os import system, name
from threading import active_count
from time import sleep as swait
from utilitys import logger
from re import search


TIME_OUT = 15
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'


class Api():
    def __init__(self, channel, post) -> None:
        self.url = 'https://t.me/'
        self.real_views = 0
        self.channel, self.post = channel, post
        self.proxy_errors, self.token_errors = 0, 0


    def views(self):
        while True:
            try:
                telegram_request = requests.get(
                    f'{self.url}{self.channel}/{self.post}', 
                    params={'embed': '1', 'mode': 'tme'},
                    headers={'referer': f'{self.url}{self.channel}/{self.post}', 'user-agent': USER_AGENT})
                self.real_views = search('<span class="tgme_widget_message_views">([^<]+)', telegram_request.text).group(1)
                swait(2)
            except Exception as e: logger(e)


    def send_view(self, proxy, proxy_type):
        try:
            session = requests.session()
            response = session.get(
                f'{self.url}{self.channel}/{self.post}', 
                params={'embed': '1', 'mode': 'tme'},
                headers={'referer': f'{self.url}{self.channel}/{self.post}', 'user-agent': USER_AGENT},
                proxies={'http': f'{proxy_type}://{proxy}', 'https': f'{proxy_type}://{proxy}'},
                timeout=TIME_OUT)
            cookies_dict = session.cookies.get_dict()
            session.get('https://t.me/v/', 
                params={'views': str(search('data-view="([^"]+)', response.text).group(1))}, 
                cookies={'stel_dt': '-240', 'stel_web_auth': 'https%3A%2F%2Fweb.telegram.org%2Fz%2F',
                    'stel_ssid': cookies_dict.get('stel_ssid', None), 'stel_on': cookies_dict.get('stel_on', None)},
                headers={'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                    'user-agent': USER_AGENT, 'x-requested-with': 'XMLHttpRequest'},
                proxies={'http': f'{proxy_type}://{proxy}', 'https': f'{proxy_type}://{proxy}'},
                timeout=TIME_OUT)
            
        except AttributeError: self.token_errors += 1
        except requests.exceptions.RequestException: self.proxy_errors += 1
        except Exception as e: logger(e)
    
    
    def tui(self, logo, THREADS):
        print(' [ OUTPUT ] Stated.. Wait few seconds to run threads');swait(7)
        while int(active_count()) < THREADS-100: swait(0.05)
        system('cls' if name == 'nt' else 'clear')
        while True:
            print(logo)
            print(f'''
    [ Data ]:       {self.channel.capitalize()}/{self.post}
    [ Live Views ]: {self.real_views}
    
    [ Token Errors ]:      {self.token_errors}
    [ Connection Errors ]: {self.proxy_errors}
    
    [ Threads ]: {active_count()}
            ''')
            swait(2)
            system('cls' if name == 'nt' else 'clear')


