---
title: Tutorial: Hacking Electron Games - Part 2: Coding an Internal Overlay with HTML/CSS/JS for Persistent Cheats (Game: Vampire Survivors)
url: https://buaq.net/go-146463.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:10.144729
---

# Tutorial: Hacking Electron Games - Part 2: Coding an Internal Overlay with HTML/CSS/JS for Persistent Cheats (Game: Vampire Survivors)

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

Tutorial: Hacking Electron Games - Part 2: Coding an Internal Overlay with HTML/CSS/JS for Persistent Cheats (Game: Vampire Survivors)

TL;DR: In part 1, we enabled remote debugging and reverse engineered our way to player data via Chro
*2023-1-22 02:40:36
Author: [www.reddit.com(查看原文)](/jump-146463.htm)
阅读量:29
收藏*

---

**TL;DR**: In [part 1](https://www.youtube.com/watch?v=6u0V1svtj3A), we enabled remote debugging and reverse engineered our way to player data via Chrome DevTools. Now, I'll demonstrate how to create persistent cheats in Vampire Survivors via an internal overlay coded in HTML, CSS, and JavaScript. This is a great primer for anyone not familiar with web languages. The lessons learned in this series are directly applicable to aspects of reversing and modifying JS code, whether in an Electron app or via a web browser! I hope you learn something new and useful. =)

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/10hy6se/tutorial\_hacking\_electron\_games\_part\_2\_coding\_an/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)