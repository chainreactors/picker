---
title: api.telegram超时阻断解决方法
url: https://buaq.net/go-173231.html
source: unSafe.sh - 不安全
date: 2023-07-31
fetch_date: 2025-10-04T11:51:32.655363
---

# api.telegram超时阻断解决方法

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

api.telegram超时阻断解决方法

错误：HTTPSConnectionPool(host='api.telegram.org', port=443): Read timed out. (
*2023-7-30 18:2:0
Author: [blog.upx8.com(查看原文)](/jump-173231.htm)
阅读量:16
收藏*

---

错误：HTTPSConnectionPool(host='api.telegram.org', port=443): Read timed out. (read timeout=25)

解决方法：

安装`sudo apt install tor`

```
sudo apt install privoxy torsocks

nano /etc/privoxy/config
```

`pip install pysocks`

`forward-socks5t / 127.0.0.1:9050 .`

```
sudo systemctl enable privoxy.service
sudo systemctl start privoxy.service
```

`/etc/tor/torsocks.conf`

```
TorAddress 127.0.0.1
TorPort 9050
```

```
from telebot import apihelper

apihelper.proxy = {'https': 'socks5h://127.0.0.1:9050',
#    'http':'http://127.0.0.1:8118',
#    'https':'https://127.0.0.1:8118'
}
bot = telebot.TeleBot(TOKEN) # be sure telebot.TeleBot calls after apihelper.proxy
```

文章来源: https://blog.upx8.com/3727
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)