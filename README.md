# Telegram Views V4 ( Asynchronous )

![Gif](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGFkOTRiMTdjMTc3OTJhZmU0MDRmZGFlNGJiMjA3NGYxOGQwM2Y2ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/jStbo9qVAJsObKKr5a/giphy.gif)


## Features
- Asynchronous ( Good for your computer )
- Support ( HTTP/S, SOCKS4, SOCKS5 ) Proxies
- Auto Proxy Scraping Mode ( You don't have to get proxies )


Arguments exmaple
```
# In this example we are sending to channel @tviews post number ( 4 )
# e.g: https://t.me/tviews/4

# Auto Scraping Mode ( Auto Proxy [ PROXYLESS ] MODE )
tviews.py --mode auto --channel tviews --post 4

# Load Proxies From File ( File List Mode )
tviews.py --type http --mode list --proxy http.txt --channel tviews --post 4

# Using Rotating Proxy ( Rotating Mode )
tviews.py -t http -m rotate -p user:password@ip:port -c tviews -pt 4
```
