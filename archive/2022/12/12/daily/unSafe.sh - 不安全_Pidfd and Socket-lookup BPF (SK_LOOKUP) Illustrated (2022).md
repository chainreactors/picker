---
title: Pidfd and Socket-lookup BPF (SK_LOOKUP) Illustrated (2022)
url: https://buaq.net/go-139522.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:31.052505
---

# Pidfd and Socket-lookup BPF (SK_LOOKUP) Illustrated (2022)

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

![](https://8aqnet.cdn.bcebos.com/ab05fd7da77e2a79219bba5cd53bc1bb.jpg)

Pidfd and Socket-lookup BPF (SK\_LOOKUP) Illustrated (2022)

Published at 2022-12-11 | Last Update 2022-12-11 TL; DRMost unix programming tex
*2022-12-11 08:0:0
Author: [arthurchiao.github.io(查看原文)](/jump-139522.htm)
阅读量:72
收藏*

---

Published at 2022-12-11 | Last Update 2022-12-11

### TL; DR

Most unix programming text books as well as practices hold the following statements to be true:

1. **One socket** could be opened by **one and only one process** (application);
2. **One socket** could listen/serve on **one and only one port**;

   Recall the `bind` system call
   `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)` where
   `addr` is determined by `IP+Port` (and socket address family).

However, with some advanced techniques like **`pidfd_getfd()`**
system call in Linux kernel `5.4+` and **`SK_LOOKUP`** BPF in
kernel `5.6+`, we could easily break the above limitations, supporting scenarios like below:

```
       +-----------+  +-----------+  +----------+                              +------------------+
       | Process 1 |  | Process 2 |  | Process 3|                              |   Process(app)   |
       |           |  |           |  |          |                              |                  |
       |  SockFD1  |  |  SockFD2  |  |  SockFD3 |                              |     SockFD       |
       +-----------+  +-----------+  +----------+                              +------------------+
                \         |         /                                                   |
                +--------------------+                                         +------------------+
                |       Socket       |                                         |     Socket       |
                +--------------------+                                         +------------------+
                          |                                                    /        |         \
                +--------------------+                                 +--------+  +---------+  +----------+
                |       [email protected]       |                                 |  [email protected] |  | [email protected]  |  | [email protected]  |
                +--------------------+                                 +--------+  +---------+  +----------+
                          |                                                     \       |         /
                +--------------------+                                          +------------------+
                |      ServerIP      |                                          |    ServerIP      |
                +--------------------+                                          +------------------+
                          /\                                                            /\
                          ||                                                            ||
                       requests                                                      requests

                       Scenario 1:                                                  Scenario 2:
  Multiple processes serve requests over the same socket.         Single socket listens/serves on multiple ports.
  E.g. Three HTTP servers share the same [email protected]:80         E.g. one socket servers on [email protected]
  socket.                                                         {:6, :66, :666} simultaneously.
```

This post explains the underlying working mechanism of the `SK_LOOKUP` BPF,
and provides example codes based on [cilium/ebpf](https://github.com/cilium/ebpf)
library, which has minimal dependencies and doesn’t require header files to be installed.

Demo codes in this post: [github.com/arthurchiao/pidfd-and-sk-lookup-bpf-illustrated](https://github.com/arthurchiao/pidfd-and-sk-lookup-bpf-illustrated).

---

文章来源: https://arthurchiao.github.io/blog/pidfd-and-socket-lookup-bpf-illustrated/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)