---
title: Mark Wielaard: Checking usage of realloc with Valgrind
url: https://buaq.net/go-172995.html
source: unSafe.sh - 不安全
date: 2023-07-27
fetch_date: 2025-10-04T11:52:46.883115
---

# Mark Wielaard: Checking usage of realloc with Valgrind

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

Mark Wielaard: Checking usage of realloc with Valgrind

Checking usage of realloc with ValgrindPosted on July 26, 2023, 16:22.Full ar
*2023-7-26 22:22:4
Author: [gnu.wildebeest.org(查看原文)](/jump-172995.htm)
阅读量:11
收藏*

---

## Checking usage of realloc with Valgrind

Posted on July 26, 2023, 16:22.

**Full article**: [Checking usage of realloc with Valgrind](https://developers.redhat.com/articles/2023/05/31/checking-usage-realloc-valgrind)

**Summary**: realloc has a surprising number of tricky corner cases to watch out for. Valgrind Memcheck will help you find various issues like using it with bad arguments, pointers that might have become invalid, and leaks of blocks that have been resized.

Also, don’t forget to use GCC with -fanalyzer, -Wuse-after-free, and -Wfree-nonheap-object to catch some of these issues early.

Finally, there is the almost philosophical question of what it means to have a zero-sized memory block. Since different implementations of (and standards describing) realloc answer that question differently, it is best to avoid ever calling realloc with size zero.

If you do then Valgrind 3.21.0 has two options to help:

* --show-realloc-size-zero=no|yes. Warn for size zero realloc calls.
* --realloc-zero-bytes-frees=yes|no. Whether size zero returns NULL or not.

Both options were implemented by Paul Floyd.

文章来源: https://gnu.wildebeest.org/blog/mjw/2023/07/26/checking-usage-of-realloc-with-valgrind/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)