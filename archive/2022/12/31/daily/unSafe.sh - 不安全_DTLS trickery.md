---
title: DTLS trickery
url: https://buaq.net/go-143461.html
source: unSafe.sh - 不安全
date: 2022-12-31
fetch_date: 2025-10-04T02:47:01.945006
---

# DTLS trickery

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

DTLS trickery

Probably the last post in 2022.I fixed SOCKS5 handling in psc and crash so that it is now possible
*2022-12-30 18:37:0
Author: [c-skills.blogspot.com(查看原文)](/jump-143461.htm)
阅读量:23
收藏*

---

Probably the last post in 2022.

I fixed *SOCKS5* handling in [psc](https://github.com/stealth/psc) and [crash](https://github.com/stealth/crash) so that it is now possible to use it with *curl* and IPv6. Also added **DTLS** (read: **TLS** over **UDP**) support for *crash* in order to make it possible to use anti censorship *SOCKS* proxies in countries that block outgoing **TCP** connections such as in Iran (see previous post).

When I read about *LibreSSL* having **QUIC** support, I tried to use this, but their bold announcement was a spoiler. They only "support" the **QUIC** handshake to obtain keying materials by means of **TLS** integration. I wouldn't really call this "QUIC support", although I love *LibreSSL* much more than *OpenSSL* (due to their permanent API changes). As **DTLS** has only reliability for its handshake, I had to add my own TCP-style data flow mechanisms to handle packet loss and re-orders. *OpenSSL* also wants to add **QUIC** support, so lets see in a couple of years how far this goes (hopefully with full proto and API support and not just the handshake) to finally have a usable **QUIC** lib.

*Crash* also switched from **TLS** v1.2 to v1.3 being mandatory, i.e. it is not proto compatible to the 2.x versions anymore. As soon as **DTLS** v1.3 will be widely deployed, it will also switch to **DTLS** v1.3. Due to all these new features and compat things the crash-3 versions are dubbed experimental (although working stable).

Wish you a nice rest of 2022 and a Guten Rutsch for 2023!

文章来源: https://c-skills.blogspot.com/2022/12/dtls-trickery.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)