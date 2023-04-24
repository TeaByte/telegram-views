from threading import Thread, active_count
from time import sleep as swait
from auto_proxy import Proxy
from telegram import Api
from utilitys import *


print(LOGO)
channel, post = input_loader()
http, socks4, socks5 = config_loader()

auto_proxies, telegram_api = (
    Proxy(
        http_sources=http, 
        socks4_sources=socks4, 
        socks5_sources=socks5
    ), 
    Api(
        channel=channel, 
        post=post
    )
)

def view_updater():
    while True:
        try: Api.views(telegram_api);swait(2)
        except Exception as e: logger(e)


def cli():
    _display = display()
    while True:
        try:
            system('cls' if name == 'nt' else 'clear')
            _display();swait(2)
        except Exception as e: logger(e)


Thread(target=view_updater).start()
Thread(target=cli).start()

def start():
    threads = []
    auto_proxies.init()
    for proxy_type, proxy in auto_proxies.proxies:
        while active_count() > THREADS: swait(0.05)
        thread = Thread(
            target=telegram_api.send_view, 
            args=(proxy, proxy_type)
        )
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
        start()

start()