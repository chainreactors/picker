---
title: Mac executable creation issue
url: https://buaq.net/go-258102.html
source: unSafe.sh - 不安全
date: 2024-08-26
fetch_date: 2025-10-06T18:00:43.649917
---

# Mac executable creation issue

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

Mac executable creation issue

Hello peeps, I'm trying to create binary from x86 code [.S extension] on Apple Mac
*2024-8-25 23:33:10
Author: [www.reddit.com(查看原文)](/jump-258102.htm)
阅读量:12
收藏*

---

Hello peeps,

I'm trying to create binary from x86 code [.S extension] on Apple Mac [2.3 GHz Dual-Core Intel Core i5 processor]. Im getting .o file without any errors. But I couldn't generate binary file from object file.

command used and error received:

$ clang -o example example.o ld: Undefined symbols: \_main, referenced from: <initial-undefines> clang: error: linker command failed with exit code 1 (use -v to see invocation)

Piece of code I used to create .o file:

.intel\_syntax noprefix

\_main: xor rax, rax

Any suggestions please.. PS: I have tried using ld as well, it gives me same error.

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/1f0z2yi/mac\_executable\_creation\_issue/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)