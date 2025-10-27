---
title: Using Rust and Ptrace to invoke Syscalls in external processes
url: https://buaq.net/go-135342.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:06.340427
---

# Using Rust and Ptrace to invoke Syscalls in external processes

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

Using Rust and Ptrace to invoke Syscalls in external processes

Not specifically reverse engineering, but definitely relevant and I think this subreddit might have
*2022-11-12 22:53:1
Author: [www.reddit.com(查看原文)](/jump-135342.htm)
阅读量:33
收藏*

---

Not specifically reverse engineering, but definitely relevant and I think this subreddit might have some members who might enjoy reading

Also: this is gonna be part 1 of a three part series where the second two articles will get us to injecting shared object libraries, and implement plt/got hooking by inspecting the application's loaded elf linkmaps

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/yt95yi/using\_rust\_and\_ptrace\_to\_invoke\_syscalls\_in/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)