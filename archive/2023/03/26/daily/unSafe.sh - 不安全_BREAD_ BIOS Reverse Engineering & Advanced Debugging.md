---
title: BREAD: BIOS Reverse Engineering & Advanced Debugging
url: https://buaq.net/go-155256.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:16.785897
---

# BREAD: BIOS Reverse Engineering & Advanced Debugging

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

BREAD: BIOS Reverse Engineering & Advanced Debugging

Hi,Some time ago, I was involved in a legacy BIOS reverse engineering project, and I noticed that mo
*2023-3-25 22:28:8
Author: [www.reddit.com(查看原文)](/jump-155256.htm)
阅读量:31
收藏*

---

Hi,

Some time ago, I was involved in a legacy BIOS reverse engineering project, and I noticed that most of the analysis being made was static in nature. Essentially, we were reading the ROM binary using various tools and trying to make sense of it in our heads. However, this approach had some limitations since we didn't have access to the contents of registers, memory, etc. at any given point in the code. This made the whole process more complicated than it needed to be.

That's when I decided to develop my own debugger. I created BREAD, a compact injectable debugger that takes up only ~1.5kB of space. With BREAD, you can easily add it to the BIOS ROM and start debugging from there. Additionally, since it was designed for real mode, it can be used to debug bootable code or even DOS programs. It operates on real hardware and communicates via serial port with the GDB that you're already familiar with.

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/121nfp2/bread\_bios\_reverse\_engineering\_advanced\_debugging/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)