from configparser import ConfigParser
from time import sleep as swait
from re import search


error_file = open('errors.txt', 'a+', encoding='utf-8')
logger = lambda error: error_file.write(f'{error}\n')


def auto_loader():
    try: 
        cfg = ConfigParser(interpolation=None)
        cfg.read("config.ini", encoding="utf-8")
        return (
            cfg["HTTP"].get("Sources").splitlines(), 
            cfg["SOCKS4"].get("Sources").splitlines(), 
            cfg["SOCKS5"].get("Sources").splitlines()
        )
    except KeyError: 
        print(' [ Error ] config.ini not found!')
        swait(3);quit()


def input_loader():
    url_input = search(r'(https?:\/\/t\.me\/)?([^/]+)/(\d+)', input(' [ INPUT ] Enter Post URL: '))
    if url_input: 
        _, channel, post = url_input.groups()
        return channel, post
    else: 
        print(' [ ERROR ] Channel Or Post Not Found!')
        swait(3);quit()
