---
title: How a BUG reported 15 years ago still around
url: https://buaq.net/go-153031.html
source: unSafe.sh - 不安全
date: 2023-03-12
fetch_date: 2025-10-04T09:21:30.025544
---

# How a BUG reported 15 years ago still around

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

How a BUG reported 15 years ago still around

Skip to contentI downloaded a Dell OS Recovery Windows image to install
*2023-3-11 23:26:2
Author: [acassis.wordpress.com(查看原文)](/jump-153031.htm)
阅读量:39
收藏*

---

[Skip to content](#content)

I downloaded a Dell OS Recovery Windows image to install on my old Dell G3 that was with Linux since I bought it and removed Windows.

According to Dell website I could use “Startup Disk” (usb-creator) program on Ubuntu to install the Dell ISO images on my USB Thumb driver, but after selecting the .iso file nothing was displayed on screen.

Then I decided to run the “Startup Disk” program from terminal to understand what was going on:

```
# /usr/bin/python3 /usr/bin/usb-creator-gtk
```

I noticed the message: “Unable to find Joliet SVD”

```
isoinfo -J -R -l -i 7YXN5A08_Win10x64ROW_home.iso
isoinfo: Unable to find Joliet SVD
```

So, that is it, a known BUG reported 15 years ago and no solution!

Update: I also tried this solution: <https://gist.github.com/roman-yepishev/68ce1d30096c350b8c6ee5e6b08a87e9> but didn’t work, during the USB boot a prompt “\_” appears blinking in the top left corner of screen but the system doesn’t start

文章来源: https://acassis.wordpress.com/2023/03/11/how-a-bug-reported-15-years-ago-still-around/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)