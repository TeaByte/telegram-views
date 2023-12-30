import aiohttp, asyncio
from re import search
from aiohttp_socks import ProxyConnector
from argparse import ArgumentParser
from re import compile
from os import system, name
from threading import Thread
from time import sleep


user_agent = "Opera/9.54 (X11; Linux i686; en-US) Presto/2.10.331 Version/12.00",
    "Opera/9.18 (Windows 95; sl-SI) Presto/2.11.255 Version/12.00",
    "Mozilla/5.0 (Windows NT 4.0) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/88.0.4172.40 Safari/531.2 Edg/88.01016.83",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.35.1 (KHTML, like Gecko) Version/5.0 Safari/533.35.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1 rv:3.0) Gecko/20191206 Firefox/35.0",
    "Opera/8.57 (X11; Linux i686; nl-NL) Presto/2.12.346 Version/10.00",
    "Opera/9.71 (X11; Linux x86_64; nl-NL) Presto/2.9.197 Version/12.00",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.22.2 (KHTML, like Gecko) Version/4.0.5 Safari/532.22.2",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 98; Trident/5.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_1 like Mac OS X; nl-NL) AppleWebKit/535.5.7 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6535.5.7",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Trident/3.0)",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_0) AppleWebKit/5330 (KHTML, like Gecko) Chrome/37.0.856.0 Mobile Safari/5330",
    "Mozilla/5.0 (Windows NT 5.01) AppleWebKit/5360 (KHTML, like Gecko) Chrome/40.0.866.0 Mobile Safari/5360",
    "Mozilla/5.0 (iPad; CPU OS 8_2_2 like Mac OS X; en-US) AppleWebKit/535.20.2 (KHTML, like Gecko) Version/4.0.5 Mobile/8B114 Safari/6535.20.2",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/3.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/537.1 (KHTML, like Gecko) Version/15.0 EdgiOS/96.01024.82 Mobile/15E148 Safari/537.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.46.2 (KHTML, like Gecko) Version/4.0.4 Safari/532.46.2",
    "Mozilla/5.0 (Windows NT 4.0) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/79.0.4541.56 Safari/534.0 Edg/79.01054.6",
    "Opera/8.54 (X11; Linux x86_64; sl-SI) Presto/2.11.231 Version/11.00",
    "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X; en-US) AppleWebKit/533.34.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B112 Safari/6533.34.4",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5361 (KHTML, like Gecko) Chrome/40.0.851.0 Mobile Safari/5361",
    "Mozilla/5.0 (X11; Linux x86_64; rv:6.0) Gecko/20210504 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5362 (KHTML, like Gecko) Chrome/38.0.876.0 Mobile Safari/5362",
    "Mozilla/5.0 (Windows NT 5.0; nl-NL; rv:1.9.1.20) Gecko/20101011 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_7) AppleWebKit/531.1 (KHTML, like Gecko) Chrome/85.0.4762.26 Safari/531.1 Edg/85.01032.20",
    "Mozilla/5.0 (Windows 95) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/97.0.4681.33 Safari/531.0 Edg/97.01015.49",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/83.0.4832.56 Safari/536.1 Edg/83.01071.13",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5331 (KHTML, like Gecko) Chrome/39.0.859.0 Mobile Safari/5331",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_2 rv:4.0) Gecko/20120913 Firefox/36.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_1 like Mac OS X; nl-NL) AppleWebKit/535.40.5 (KHTML, like Gecko) Version/4.0.5 Mobile/8B112 Safari/6535.40.5",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows CE; Trident/5.1)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_9) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/98.0.4828.29 Safari/533.1 Edg/98.01114.85",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.1)",
    "Mozilla/5.0 (Windows NT 4.0; sl-SI; rv:1.9.1.20) Gecko/20221010 Firefox/37.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5352 (KHTML, like Gecko) Chrome/37.0.803.0 Mobile Safari/5352",
    "Opera/8.60 (X11; Linux i686; sl-SI) Presto/2.9.344 Version/12.00",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/99.0.4839.72 Safari/531.2 Edg/99.01138.48",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; Trident/3.1)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5321 (KHTML, like Gecko) Chrome/36.0.889.0 Mobile Safari/5321",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows 95; Trident/3.1)",
    "Mozilla/5.0 (Windows NT 4.0; sl-SI; rv:1.9.0.20) Gecko/20181223 Firefox/36.0",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows 98; Win 9x 4.90; Trident/4.1)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/88.0.4265.35 Safari/535.1 Edg/88.01121.22",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20110330 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_6) AppleWebKit/5320 (KHTML, like Gecko) Chrome/37.0.883.0 Mobile Safari/5320",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Trident/5.1)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5330 (KHTML, like Gecko) Chrome/36.0.859.0 Mobile Safari/5330",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/3.1)",
    "Mozilla/5.0 (Windows NT 6.1; nl-NL; rv:1.9.0.20) Gecko/20110227 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_3 rv:3.0) Gecko/20210401 Firefox/37.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/531.17.6 (KHTML, like Gecko) Version/5.1 Safari/531.17.6",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) Version/15.0 EdgiOS/93.01055.15 Mobile/15E148 Safari/531.2",
    "Mozilla/5.0 (Windows CE; nl-NL; rv:1.9.1.20) Gecko/20181127 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 4.0; sl-SI; rv:1.9.2.20) Gecko/20190704 Firefox/35.0",
    "Opera/9.10 (Windows 98; sl-SI) Presto/2.10.241 Version/11.00",
    "Mozilla/5.0 (iPad; CPU OS 8_0_1 like Mac OS X; en-US) AppleWebKit/533.20.5 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6533.20.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4 rv:4.0; en-US) AppleWebKit/534.35.4 (KHTML, like Gecko) Version/4.0.5 Safari/534.35.4",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/94.0.4043.59 Safari/531.0 EdgA/94.01056.43",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) Version/15.0 EdgiOS/82.01091.39 Mobile/15E148 Safari/531.2",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows 98; Trident/3.0)",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 5.01; Trident/3.1)",
    "Opera/8.72 (Windows NT 5.01; nl-NL) Presto/2.9.218 Version/11.00",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows CE; Trident/4.0)",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Windows 95; nl-NL; rv:1.9.2.20) Gecko/20120419 Firefox/36.0",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.0 (KHTML, like Gecko) Chrome/80.0.4107.47 Safari/537.0 EdgA/80.01047.9",
    "Mozilla/5.0 (Windows 98) AppleWebKit/5361 (KHTML, like Gecko) Chrome/39.0.829.0 Mobile Safari/5361",
    "Opera/9.46 (X11; Linux x86_64; en-US) Presto/2.8.303 Version/11.00",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/5352 (KHTML, like Gecko) Chrome/40.0.847.0 Mobile Safari/5352",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 95; Trident/4.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/532.1 (KHTML, like Gecko) Version/15.0 EdgiOS/80.01088.11 Mobile/15E148 Safari/532.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/533.0 (KHTML, like Gecko) Version/15.0 EdgiOS/93.01078.66 Mobile/15E148 Safari/533.0",
    "Opera/8.93 (Windows 95; en-US) Presto/2.9.230 Version/10.00",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_9 rv:5.0; nl-NL) AppleWebKit/532.46.6 (KHTML, like Gecko) Version/5.0.3 Safari/532.46.6",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/5.1)",
    "Opera/8.63 (Windows NT 6.0; nl-NL) Presto/2.12.339 Version/10.00",
    "Opera/9.76 (Windows NT 6.0; en-US) Presto/2.8.202 Version/10.00",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/3.0)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/87.0.4309.19 Safari/533.2 Edg/87.01136.68",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/532.1 (KHTML, like Gecko) Version/15.0 EdgiOS/98.01094.32 Mobile/15E148 Safari/532.1",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows 98; Trident/4.0)",
    "Mozilla/5.0 (Windows NT 6.0; nl-NL; rv:1.9.0.20) Gecko/20200922 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_4 rv:3.0) Gecko/20220824 Firefox/35.0",
    "Opera/8.85 (X11; Linux i686; nl-NL) Presto/2.10.211 Version/11.00",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_6) AppleWebKit/5332 (KHTML, like Gecko) Chrome/36.0.884.0 Mobile Safari/5332",
    "Mozilla/5.0 (Windows NT 5.01; nl-NL; rv:1.9.0.20) Gecko/20161021 Firefox/35.0",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/94.0.4666.56 Safari/532.1 EdgA/94.01127.67",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/3.0)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7 rv:4.0) Gecko/20130529 Firefox/37.0",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.25.3 (KHTML, like Gecko) Version/4.1 Safari/533.25.3",
    "Opera/8.36 (Windows NT 5.2; en-US) Presto/2.8.190 Version/11.00",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0) AppleWebKit/5351 (KHTML, like Gecko) Chrome/38.0.834.0 Mobile Safari/5351",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows 95; Trident/4.1)",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_1) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/92.0.4763.61 Safari/536.0 Edg/92.01145.16",
    "Mozilla/5.0 (X11; Linux x86_64; rv:6.0) Gecko/20200606 Firefox/36.0",
    "Opera/8.43 (X11; Linux i686; sl-SI) Presto/2.8.246 Version/11.00",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/531.0 (KHTML, like Gecko) Version/15.0 EdgiOS/82.01047.48 Mobile/15E148 Safari/531.0",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 4.0; Trident/3.1)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows CE; Trident/5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0 rv:2.0) Gecko/20140423 Firefox/35.0",
    "Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X; en-US) AppleWebKit/535.35.4 (KHTML, like Gecko) Version/4.0.5 Mobile/8B114 Safari/6535.35.4",
    "Mozilla/5.0 (Windows CE; en-US; rv:1.9.0.20) Gecko/20220629 Firefox/35.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 4.0; Trident/5.1)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_2) AppleWebKit/5311 (KHTML, like Gecko) Chrome/37.0.875.0 Mobile Safari/5311",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 98; Win 9x 4.90; Trident/4.0)",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.2; Trident/5.1)",
    "Mozilla/5.0 (Windows NT 6.1; sl-SI; rv:1.9.1.20) Gecko/20140731 Firefox/36.0",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0; Trident/3.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X; sl-SI) AppleWebKit/533.34.2 (KHTML, like Gecko) Version/4.0.5 Mobile/8B113 Safari/6533.34.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_1 like Mac OS X; nl-NL) AppleWebKit/534.14.6 (KHTML, like Gecko) Version/3.0.5 Mobile/8B115 Safari/6534.14.6",
    "Mozilla/5.0 (X11; Linux i686; rv:7.0) Gecko/20130531 Firefox/37.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_2) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/92.0.4833.95 Safari/532.0 Edg/92.01073.9",
    "Mozilla/5.0 (Windows NT 5.2; en-US; rv:1.9.1.20) Gecko/20180409 Firefox/35.0",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows 98; Trident/4.1)",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/80.0.4743.87 Safari/534.1 EdgA/80.01088.5",
    "Opera/8.89 (X11; Linux i686; nl-NL) Presto/2.10.197 Version/12.00",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_0) AppleWebKit/5321 (KHTML, like Gecko) Chrome/38.0.835.0 Mobile Safari/5321",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7) AppleWebKit/5312 (KHTML, like Gecko) Chrome/37.0.822.0 Mobile Safari/5312",
    "Mozilla/5.0 (Windows NT 5.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/96.0.4770.57 Safari/535.1 Edg/96.01096.54",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8 rv:2.0) Gecko/20220714 Firefox/35.0",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 6.1; Trident/5.1)",
    "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X; sl-SI) AppleWebKit/532.2.6 (KHTML, like Gecko) Version/4.0.5 Mobile/8B118 Safari/6532.2.6",
    "Mozilla/5.0 (Windows CE) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/93.0.4101.28 Safari/536.2 Edg/93.01141.7",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 5.1; Trident/3.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_9) AppleWebKit/5332 (KHTML, like Gecko) Chrome/38.0.842.0 Mobile Safari/5332",
    "Mozilla/5.0 (Windows; U; Windows CE) AppleWebKit/535.15.3 (KHTML, like Gecko) Version/5.0 Safari/535.15.3",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_1 rv:4.0) Gecko/20210504 Firefox/36.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.14.7 (KHTML, like Gecko) Version/4.0 Safari/533.14.7",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5340 (KHTML, like Gecko) Chrome/40.0.862.0 Mobile Safari/5340",
    "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20190428 Firefox/37.0",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows CE; Trident/4.1)",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5341 (KHTML, like Gecko) Chrome/40.0.865.0 Mobile Safari/5341",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5320 (KHTML, like Gecko) Chrome/36.0.828.0 Mobile Safari/5320",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/537.2 (KHTML, like Gecko) Version/15.0 EdgiOS/91.01102.96 Mobile/15E148 Safari/537.2",
    "Opera/8.40 (Windows 95; en-US) Presto/2.12.223 Version/11.00",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3 rv:3.0) Gecko/20100705 Firefox/35.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/531.19.4 (KHTML, like Gecko) Version/5.0.4 Safari/531.19.4",
    "Opera/8.62 (Windows 95; nl-NL) Presto/2.9.169 Version/10.00",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5330 (KHTML, like Gecko) Chrome/39.0.839.0 Mobile Safari/5330",
    "Mozilla/5.0 (Windows 98; Win 9x 4.90) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/93.0.4245.65 Safari/534.2 Edg/93.01024.73",
    "Mozilla/5.0 (Windows NT 5.01; en-US; rv:1.9.1.20) Gecko/20160119 Firefox/35.0",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows 95; Trident/5.0)",
    "Opera/9.36 (X11; Linux x86_64; sl-SI) Presto/2.12.324 Version/12.00",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/535.2 (KHTML, like Gecko) Version/15.0 EdgiOS/98.01043.90 Mobile/15E148 Safari/535.2",
    "Mozilla/5.0 (Windows 95; en-US; rv:1.9.2.20) Gecko/20231021 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/5341 (KHTML, like Gecko) Chrome/37.0.875.0 Mobile Safari/5341",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_5) AppleWebKit/5320 (KHTML, like Gecko) Chrome/39.0.880.0 Mobile Safari/5320",
    "Mozilla/5.0 (Windows NT 4.0; sl-SI; rv:1.9.1.20) Gecko/20150214 Firefox/36.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X; nl-NL) AppleWebKit/532.42.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6532.42.3",
    "Mozilla/5.0 (Windows 98) AppleWebKit/5312 (KHTML, like Gecko) Chrome/39.0.804.0 Mobile Safari/5312",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/5310 (KHTML, like Gecko) Chrome/39.0.848.0 Mobile Safari/5310",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows 98; Win 9x 4.90; Trident/3.0)",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 95; Trident/5.0)",
    "Opera/9.55 (Windows 95; en-US) Presto/2.10.181 Version/12.00",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20210923 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_0 rv:6.0) Gecko/20200423 Firefox/37.0",
    "Opera/8.41 (X11; Linux x86_64; en-US) Presto/2.12.279 Version/10.00",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/3.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X; nl-NL) AppleWebKit/535.46.1 (KHTML, like Gecko) Version/3.0.5 Mobile/8B119 Safari/6535.46.1",
    "Mozilla/5.0 (iPad; CPU OS 8_0_1 like Mac OS X; nl-NL) AppleWebKit/533.31.3 (KHTML, like Gecko) Version/3.0.5 Mobile/8B114 Safari/6533.31.3",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows 98; Win 9x 4.90; Trident/5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/5321 (KHTML, like Gecko) Chrome/40.0.871.0 Mobile Safari/5321",
    "Mozilla/5.0 (Windows NT 6.2; sl-SI; rv:1.9.1.20) Gecko/20220201 Firefox/37.0",
    "Mozilla/5.0 (Windows NT 6.0; sl-SI; rv:1.9.1.20) Gecko/20121227 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 5.0; nl-NL; rv:1.9.2.20) Gecko/20190221 Firefox/35.0",
    "Mozilla/5.0 (Windows 98) AppleWebKit/5312 (KHTML, like Gecko) Chrome/36.0.857.0 Mobile Safari/5312",
    "Opera/9.67 (X11; Linux x86_64; nl-NL) Presto/2.9.331 Version/10.00",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows 98; Trident/3.1)",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 5.01; Trident/4.0)",
    "Opera/8.26 (Windows NT 6.1; en-US) Presto/2.8.282 Version/11.00",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5312 (KHTML, like Gecko) Chrome/36.0.869.0 Mobile Safari/5312",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.37.6 (KHTML, like Gecko) Version/5.0.3 Safari/533.37.6",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_4 rv:6.0; nl-NL) AppleWebKit/531.43.5 (KHTML, like Gecko) Version/4.0 Safari/531.43.5",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/5360 (KHTML, like Gecko) Chrome/38.0.831.0 Mobile Safari/5360",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/81.0.4612.42 Safari/537.1 EdgA/81.01125.71",
    "Opera/9.44 (Windows NT 6.2; en-US) Presto/2.8.274 Version/10.00",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_7 rv:6.0) Gecko/20170604 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_0 rv:2.0) Gecko/20131009 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_3 rv:3.0) Gecko/20200812 Firefox/37.0",
    "Opera/8.51 (X11; Linux x86_64; nl-NL) Presto/2.8.225 Version/10.00",
    "Mozilla/5.0 (Windows 98; Win 9x 4.90; sl-SI; rv:1.9.2.20) Gecko/20161107 Firefox/35.0",
    "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X; nl-NL) AppleWebKit/532.42.5 (KHTML, like Gecko) Version/4.0.5 Mobile/8B114 Safari/6532.42.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:7.0) Gecko/20180106 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_4) AppleWebKit/5352 (KHTML, like Gecko) Chrome/36.0.854.0 Mobile Safari/5352",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/86.0.4239.15 Safari/536.0 Edg/86.01042.96",
    "Mozilla/5.0 (Windows 95) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/91.0.4751.29 Safari/537.1 Edg/91.01084.8",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/537.0 (KHTML, like Gecko) Version/15.0 EdgiOS/92.01122.0 Mobile/15E148 Safari/537.0",
    "Opera/8.94 (X11; Linux i686; en-US) Presto/2.12.242 Version/11.00",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5311 (KHTML, like Gecko) Chrome/37.0.839.0 Mobile Safari/5311",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1 rv:4.0) Gecko/20140911 Firefox/35.0",
    "Mozilla/5.0 (Windows NT 4.0; en-US; rv:1.9.2.20) Gecko/20151229 Firefox/37.0",
    "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X; en-US) AppleWebKit/535.27.3 (KHTML, like Gecko) Version/3.0.5 Mobile/8B115 Safari/6535.27.3",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/5360 (KHTML, like Gecko) Chrome/38.0.832.0 Mobile Safari/5360",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:5.0; en-US) AppleWebKit/531.7.1 (KHTML, like Gecko) Version/5.0.4 Safari/531.7.1",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5311 (KHTML, like Gecko) Chrome/36.0.819.0 Mobile Safari/5311",
    "Opera/9.68 (X11; Linux i686; sl-SI) Presto/2.10.331 Version/11.00",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 98; Trident/3.1)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_4 rv:5.0; en-US) AppleWebKit/531.4.6 (KHTML, like Gecko) Version/5.0.5 Safari/531.4.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.49.7 (KHTML, like Gecko) Version/4.0.1 Safari/533.49.7",
    "Mozilla/5.0 (Windows NT 5.01) AppleWebKit/5361 (KHTML, like Gecko) Chrome/36.0.835.0 Mobile Safari/5361",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_4 rv:2.0; nl-NL) AppleWebKit/532.23.1 (KHTML, like Gecko) Version/4.0 Safari/532.23.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/93.0.4573.64 Safari/532.1 EdgA/93.01113.57",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5341 (KHTML, like Gecko) Chrome/38.0.825.0 Mobile Safari/5341",
    "Opera/9.49 (X11; Linux i686; nl-NL) Presto/2.11.281 Version/11.00",
    "Mozilla/5.0 (Windows NT 6.2; en-US; rv:1.9.0.20) Gecko/20160509 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_2 rv:6.0) Gecko/20110122 Firefox/35.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_7 rv:4.0; nl-NL) AppleWebKit/531.49.4 (KHTML, like Gecko) Version/4.0 Safari/531.49.4",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows 95; Trident/4.1)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/93.0.4385.36 Safari/535.2 EdgA/93.01007.66",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_9) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/95.0.4790.14 Safari/531.0 Edg/95.01130.7",
    "Opera/9.25 (Windows NT 6.1; en-US) Presto/2.8.208 Version/10.00",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/536.1 (KHTML, like Gecko) Version/15.0 EdgiOS/80.01140.36 Mobile/15E148 Safari/536.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/98.0.4136.77 Safari/535.2 Edg/98.01105.66",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5322 (KHTML, like Gecko) Chrome/36.0.826.0 Mobile Safari/5322",
    "Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X; sl-SI) AppleWebKit/532.43.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B119 Safari/6532.43.4",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Trident/3.0)",
    "Mozilla/5.0 (Windows 95) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/96.0.4746.35 Safari/534.2 Edg/96.01007.52",
    "Opera/8.61 (X11; Linux x86_64; en-US) Presto/2.8.175 Version/10.00",
    "Opera/8.77 (X11; Linux i686; nl-NL) Presto/2.12.314 Version/10.00",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/82.0.4354.77 Safari/533.1 Edg/82.01069.50",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5332 (KHTML, like Gecko) Chrome/40.0.875.0 Mobile Safari/5332",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_3) AppleWebKit/5310 (KHTML, like Gecko) Chrome/40.0.801.0 Mobile Safari/5310",
    "Mozilla/5.0 (Windows NT 5.0; nl-NL; rv:1.9.1.20) Gecko/20110722 Firefox/36.0",
    "Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.10.6 (KHTML, like Gecko) Version/4.1 Safari/531.10.6",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/89.0.4267.34 Safari/536.0 EdgA/89.01114.16",
    "Mozilla/5.0 (X11; Linux x86_64; rv:6.0) Gecko/20200610 Firefox/37.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Trident/5.0)",
    "Mozilla/5.0 (Windows; U; Windows 98; Win 9x 4.90) AppleWebKit/531.30.7 (KHTML, like Gecko) Version/5.0 Safari/531.30.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.28.3 (KHTML, like Gecko) Version/4.1 Safari/534.28.3",
    "Mozilla/5.0 (Windows 98) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/85.0.4180.75 Safari/534.1 Edg/85.01056.98",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/537.2 (KHTML, like Gecko) Version/15.0 EdgiOS/84.01098.34 Mobile/15E148 Safari/537.2",
    "Mozilla/5.0 (X11; Linux i686; rv:7.0) Gecko/20100317 Firefox/37.0",
    "Opera/8.45 (X11; Linux x86_64; sl-SI) Presto/2.12.244 Version/12.00",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_4 rv:2.0; en-US) AppleWebKit/531.25.3 (KHTML, like Gecko) Version/4.0.5 Safari/531.25.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_3) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/81.0.4218.55 Safari/535.2 Edg/81.01071.33",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows CE; Trident/5.1)",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_5) AppleWebKit/5360 (KHTML, like Gecko) Chrome/37.0.824.0 Mobile Safari/5360",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_3 rv:5.0) Gecko/20170730 Firefox/37.0",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 5.2; Trident/3.0)",
    "Mozilla/5.0 (compatible; MSIE 5.0; Windows 98; Win 9x 4.90; Trident/3.1)",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_0) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/86.0.4020.50 Safari/533.1 Edg/86.01127.98",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/5311 (KHTML, like Gecko) Chrome/38.0.816.0 Mobile Safari/5311",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X; nl-NL) AppleWebKit/534.36.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B113 Safari/6534.36.4",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/531.0 (KHTML, like Gecko) Version/15.0 EdgiOS/93.01012.37 Mobile/15E148 Safari/531.0",
    "Mozilla/5.0 (Windows 98) AppleWebKit/5360 (KHTML, like Gecko) Chrome/38.0.834.0 Mobile Safari/5360",
    "Mozilla/5.0 (X11; Linux i686; rv:7.0) Gecko/20231208 Firefox/37.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_8) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/99.0.4678.71 Safari/531.2 Edg/99.01017.37",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2; Trident/3.0)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3) AppleWebKit/5332 (KHTML, like Gecko) Chrome/39.0.848.0 Mobile Safari/5332",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5352 (KHTML, like Gecko) Chrome/37.0.813.0 Mobile Safari/5352",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7 rv:6.0; en-US) AppleWebKit/531.49.2 (KHTML, like Gecko) Version/4.1 Safari/531.49.2",
    "Opera/9.77 (Windows NT 5.01; en-US) Presto/2.8.244 Version/11.00",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.20.4 (KHTML, like Gecko) Version/4.0.1 Safari/532.20.4",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/90.0.4528.98 Safari/533.0 EdgA/90.01122.48",
    "Opera/9.55 (X11; Linux x86_64; nl-NL) Presto/2.8.256 Version/12.00",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_5 rv:4.0; sl-SI) AppleWebKit/535.23.3 (KHTML, like Gecko) Version/4.1 Safari/535.23.3",
    "Mozilla/5.0 (Windows 95; sl-SI; rv:1.9.2.20) Gecko/20180304 Firefox/35.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2_1 like Mac OS X; nl-NL) AppleWebKit/535.2.6 (KHTML, like Gecko) Version/3.0.5 Mobile/8B119 Safari/6535.2.6",
    "Mozilla/5.0 (Windows; U; Windows CE) AppleWebKit/532.29.4 (KHTML, like Gecko) Version/4.0 Safari/532.29.4",
    "Opera/9.74 (Windows CE; en-US) Presto/2.11.160 Version/12.00",
    "Opera/9.85 (X11; Linux x86_64; en-US) Presto/2.11.246 Version/10.00",
    "Opera/8.40 (Windows NT 5.0; nl-NL) Presto/2.8.284 Version/12.00",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 5.01; Trident/5.0)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5342 (KHTML, like Gecko) Chrome/36.0.867.0 Mobile Safari/5342",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows 98; Win 9x 4.90; Trident/4.0)",
    "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20140411 Firefox/37.0",
    "Opera/9.42 (X11; Linux i686; en-US) Presto/2.8.169 Version/12.00",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_2) AppleWebKit/5332 (KHTML, like Gecko) Chrome/39.0.838.0 Mobile Safari/5332",
    "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X; nl-NL) AppleWebKit/532.17.2 (KHTML, like Gecko) Version/3.0.5 Mobile/8B118 Safari/6532.17.2",
    "Opera/9.84 (X11; Linux i686; en-US) Presto/2.11.332 Version/10.00",
    "Opera/9.28 (X11; Linux x86_64; sl-SI) Presto/2.9.339 Version/11.00",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.2; Trident/4.1)",
    "Opera/8.62 (X11; Linux i686; nl-NL) Presto/2.8.247 Version/12.00",
    "Mozilla/5.0 (X11; Linux x86_64; rv:7.0) Gecko/20170422 Firefox/35.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_1 like Mac OS X; en-US) AppleWebKit/534.36.1 (KHTML, like Gecko) Version/3.0.5 Mobile/8B118 Safari/6534.36.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.47.4 (KHTML, like Gecko) Version/5.0 Safari/533.47.4",
    "Opera/9.88 (X11; Linux x86_64; en-US) Presto/2.10.351 Version/12.00",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_1) AppleWebKit/5331 (KHTML, like Gecko) Chrome/39.0.801.0 Mobile Safari/5331",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_1 rv:6.0; sl-SI) AppleWebKit/535.34.3 (KHTML, like Gecko) Version/5.0 Safari/535.34.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_6) AppleWebKit/5311 (KHTML, like Gecko) Chrome/40.0.833.0 Mobile Safari/5311",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 4.0; Trident/3.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X; nl-NL) AppleWebKit/531.24.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B113 Safari/6531.24.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_9 rv:3.0) Gecko/20200409 Firefox/35.0",
    "Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/533.41.5 (KHTML, like Gecko) Version/4.0 Safari/533.41.5",
    "Mozilla/5.0 (Windows NT 5.2; nl-NL; rv:1.9.1.20) Gecko/20190303 Firefox/36.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) Version/15.0 EdgiOS/85.01013.29 Mobile/15E148 Safari/535.0",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Trident/5.1)",
    "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100102 Firefox/36.0",
    "Opera/9.77 (Windows 98; Win 9x 4.90; sl-SI) Presto/2.10.342 Version/11.00",
    "Mozilla/5.0 (Windows CE) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/96.0.4117.82 Safari/534.1 Edg/96.01052.26",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/88.0.4249.67 Safari/537.1 EdgA/88.01059.86",
    "Opera/8.46 (Windows NT 6.1; en-US) Presto/2.9.351 Version/12.00",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows 98; Trident/3.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/532.0 (KHTML, like Gecko) Version/15.0 EdgiOS/81.01087.38 Mobile/15E148 Safari/532.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8 rv:6.0; sl-SI) AppleWebKit/532.21.2 (KHTML, like Gecko) Version/5.0.4 Safari/532.21.2",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20120202 Firefox/37.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/85.0.4045.66 Safari/534.2 EdgA/85.01046.44"
REGEX = compile(
    r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
    + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
    + r")(?:\D|$)"
)


class Telegram:
    def __init__(self, channel: str, post: int) -> None:
        # Async Tasks
        self.tasks = 225 
        
        self.channel = channel
        self.post = post
        
        self.cookie_error = 0
        self.sucsess_sent = 0
        self.failled_sent = 0
        self.token_error  = 0
        self.proxy_error  = 0


    async def request(self, proxy: str, proxy_type: str):
        if proxy_type == 'socks4': connector = ProxyConnector.from_url(f'socks4://{proxy}')
        elif proxy_type == 'socks5': connector = ProxyConnector.from_url(f'socks5://{proxy}')
        elif proxy_type == 'https': connector = ProxyConnector.from_url(f'https://{proxy}')
        else: connector = ProxyConnector.from_url(f'http://{proxy}')
        
        jar = aiohttp.CookieJar(unsafe=True)
        async with aiohttp.ClientSession(cookie_jar=jar, connector=connector) as session:
            try:
                async with session.get(
                    f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme', 
                    headers={
                        'referer': f'https://t.me/{self.channel}/{self.post}',
                        'user-agent': user_agent
                    }, timeout=aiohttp.ClientTimeout(total=5)
                ) as embed_response:
                    if jar.filter_cookies(embed_response.url).get('stel_ssid'):
                        views_token = search('data-view="([^"]+)"', await embed_response.text())
                        if views_token:
                            views_response = await session.post(
                                'https://t.me/v/?views=' + views_token.group(1), 
                                headers={
                                    'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                                    'user-agent': user_agent, 'x-requested-with': 'XMLHttpRequest'
                                }, timeout=aiohttp.ClientTimeout(total=5)
                            )
                            if (
                                await views_response.text() == "true" 
                                and views_response.status == 200
                            ): self.sucsess_sent += 1
                            else: self.failled_sent += 1
                        else: self.token_error += 1
                    else: self.cookie_error += 1
            except: self.proxy_error += 1
            finally: jar.clear()


    def run_proxies_tasks(self, lines: list, proxy_type):
        async def inner(proxies: list):
            await asyncio.wait(
                [asyncio.create_task(self.request(proxy, proxy_type)) 
                for proxy in proxies])
        chunks = [lines[i:i+self.tasks] for i in range(0, len(lines), self.tasks)]
        for chunk in chunks: asyncio.run(inner(chunk))
    
    
    def run_auto_tasks(self):
        while True:
            async def inner(proxies: tuple):
                await asyncio.wait(
                    [asyncio.create_task(self.request(proxy, proxy_type)) 
                    for proxy_type, proxy in proxies])
            auto = Auto()
            chunks = [auto.proxies[i:i+self.tasks] for i in range(0, len(auto.proxies), self.tasks)]
            for chunk in chunks: asyncio.run(inner(chunk))


    async def run_rotated_task(self, proxy, proxy_type):
        while True: 
            await asyncio.wait(
                [asyncio.create_task(self.request(proxy, proxy_type)) 
                for _ in range(self.tasks)])


    def cli(self):
        logo = '''
        ~ Telegram Auto Views V4 ~
          ~ github.com/TeaByte ~
               ~ @TeaByte ~
        '''
        while not self.sucsess_sent:
            print(logo)
            print('\n\n        [ Waiting... ]\r')
            sleep(0.3);system('cls' if name=='nt' else 'clear')

        while True:
            print(logo)
            print(f'''
        DATA: 
        @{self.channel}/{self.post}
        Sent: {self.sucsess_sent}
        Fail: {self.failled_sent}

        ERRORS:
        Proxy Error:  {self.proxy_error}
        Token Error:  {self.token_error}
        Cookie Error: {self.cookie_error}
            ''')
            sleep(0.3);system('cls' if name=='nt' else 'clear')


class Auto:
    def __init__(self):
        self.proxies = []
        try: 
            with open(f'auto/http.txt', 'r') as file:
                self.http_sources = file.read().splitlines()
                
            with open(f'auto/socks4.txt', 'r') as file:
                self.socks4_sources = file.read().splitlines()
                
            with open(f'auto/http.txt', 'r') as file:
                self.socks5_sources = file.read().splitlines()
                
        except FileNotFoundError: 
            print(' [ Error ] auto file not found!')
            exit()
        
        print(' [ WAIT ] Scraping proxies... ')
        asyncio.run(self.init())


    async def scrap(self, source_url, proxy_type):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    source_url, 
                    headers={'user-agent': user_agent}, 
                    timeout=aiohttp.ClientTimeout(total=15)
                ) as response:
                    html = await response.text()
                    if tuple(REGEX.finditer(html)):
                        for proxy in tuple(REGEX.finditer(html)):
                            self.proxies.append( (proxy_type, proxy.group(1)) )
        except Exception as e:
            with open('error.txt', 'a', encoding='utf-8', errors='ignore') as f:
                f.write(f'{source_url} -> {e}\n')


    async def init(self):
        tasks = []
        self.proxies.clear()
        for sources in (
            (self.http_sources, 'http'), 
            (self.socks4_sources, 'socks4'), 
            (self.socks5_sources, 'socks5') 
        ):
            srcs, proxy_type = sources
            for source_url in srcs: 
                task = asyncio.create_task(
                    self.scrap(source_url, proxy_type)
                )
                tasks.append(task)
        await asyncio.wait(tasks)


parser = ArgumentParser()
parser.add_argument('-c', '--channel', dest='channel', help='Channel user', type=str, required=True)
parser.add_argument('-pt', '--post', dest='post', help='Post number', type=int, required=True)
parser.add_argument('-t', '--type', dest='type', help='Proxy type', type=str, required=False)
parser.add_argument('-m', '--mode', dest='mode', help='Proxy mode', type=str, required=True)
parser.add_argument('-p', '--proxy', dest='proxy', help='Proxy file path or user:password@host:port', type=str, required=False)
args = parser.parse_args()

api = Telegram(args.channel, args.post)
Thread(target=api.cli).start()

if args.mode[0] == "l":
    with open(args.proxy, 'r') as file:
        lines = file.read().splitlines()
    api.run_proxies_tasks(lines, args.type)

elif args.mode[0] == "r":  
    asyncio.run(api.run_rotated_task(args.proxy, args.type))
    
else: api.run_auto_tasks()
