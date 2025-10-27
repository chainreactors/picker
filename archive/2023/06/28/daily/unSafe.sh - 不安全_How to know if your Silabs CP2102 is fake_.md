---
title: How to know if your Silabs CP2102 is fake?
url: https://buaq.net/go-170591.html
source: unSafe.sh - 不安全
date: 2023-06-28
fetch_date: 2025-10-04T11:44:14.862468
---

# How to know if your Silabs CP2102 is fake?

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

How to know if your Silabs CP2102 is fake?

That is easy: plug the USB/Serial CP210x in your Linux machine and run:#
*2023-6-27 22:38:28
Author: [acassis.wordpress.com(查看原文)](/jump-170591.htm)
阅读量:28
收藏*

---

That is easy: plug the USB/Serial CP210x in your Linux machine and run:

```
# udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1
```

If it is original you will see a complete Unique ID:

```
# udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1
    ATTRS{serial}=="201794XXXXXXXa11b392c201cf25bb41"

# udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1
    ATTRS{serial}=="fe5e32XXXXXXXa119dec3a1dcf25bb41"
```

If it is fake probably you will see “0001” as Unique ID:

```
# udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1
    ATTRS{serial}=="0001"
```

文章来源: https://acassis.wordpress.com/2023/06/27/how-to-know-if-your-silabs-cp2102-is-fake/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)