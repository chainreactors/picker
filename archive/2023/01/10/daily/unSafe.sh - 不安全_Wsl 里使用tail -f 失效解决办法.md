---
title: Wsl 里使用tail -f 失效解决办法
url: https://buaq.net/go-144808.html
source: unSafe.sh - 不安全
date: 2023-01-10
fetch_date: 2025-10-04T03:22:56.178045
---

# Wsl 里使用tail -f 失效解决办法

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

Wsl 里使用tail -f 失效解决办法

tail ---disable-inotify -f ok.log加个---disable-inotify 就能解决 注意是3条“-”
*2023-1-9 19:39:12
Author: [www.yanglong.pro(查看原文)](/jump-144808.htm)
阅读量:20
收藏*

---

```
tail ---disable-inotify -f ok.log
```

加个`---disable-inotify` 就能解决 注意是3条“`-`”

文章来源: https://www.yanglong.pro/wsl-%e9%87%8c%e4%bd%bf%e7%94%a8tail-f-%e5%a4%b1%e6%95%88%e8%a7%a3%e5%86%b3%e5%8a%9e%e6%b3%95/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)