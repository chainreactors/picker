---
title: Discovering vulnerabilities quickly with targeted scanning — Portswigger
url: https://buaq.net/go-145507.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:56:00.512188
---

# Discovering vulnerabilities quickly with targeted scanning — Portswigger

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

Discovering vulnerabilities quickly with targeted scanning — Portswigger

This lab contains a vulnerability that enables you to read arbitrary files from the server. To solve
*2023-1-14 12:30:54
Author: [infosecwriteups.com(查看原文)](/jump-145507.htm)
阅读量:79
收藏*

---

## This lab contains a vulnerability that enables you to read arbitrary files from the server. To solve the lab, retrieve the contents of /etc/passwd within 10 minutes | Approach

## Let’s Start — You have to solve the lab in 10 Minutes

Access the Lab, Turn on the Proxy, and Turn off your Intercept in Burpsuite

Now notice the Content list of HTTP history in the Proxy tab, you can see that there is a request `/product/stock`from that the Parameter `ProductID` is an endpoint to test.

Right-click on `/product/stock`→ Do Active Scan

The scanner found an Out-of-band resource load on `/product/stock`

It is possible to induce the application to retrieve the contents of an arbitrary external URL and return those contents in its own response.

* Send the Request to the Repeater
* Add the below Payload in `ProductID` Parameter

```
<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
```

Send the Request, Now you can able to view the `/etc/passwd`

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

Thank you for Reading!!

Happy Hunting ~

```
Author: Karthikeyan Nagaraj ~ Cyberw1ng
```

文章来源: https://infosecwriteups.com/discovering-vulnerabilities-quickly-with-targeted-scanning-portswigger-b8c102f5c3ba?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)