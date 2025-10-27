---
title: [译] Socket listen 多地址需求与 SK_LOOKUP BPF 的诞生（LPC, 2019）
url: https://buaq.net/go-139523.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:31.809439
---

# [译] Socket listen 多地址需求与 SK_LOOKUP BPF 的诞生（LPC, 2019）

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

![](https://8aqnet.cdn.bcebos.com/118d4bcefe0a8f900bb17d3d357f6a07.jpg)

[译] Socket listen 多地址需求与 SK\_LOOKUP BPF 的诞生（LPC, 2019）

Published at 2022-12-11 | Last Update 2022-12-11 译者序本文组合翻译 Cloudflare 的几篇分享，介绍了他
*2022-12-11 08:0:0
Author: [arthurchiao.github.io(查看原文)](/jump-139523.htm)
阅读量:93
收藏*

---

Published at 2022-12-11 | Last Update 2022-12-11

### 译者序

本文组合翻译 Cloudflare 的几篇分享，介绍了他们面临的独特网络需求、解决方案的演进，
以及终极解决方案 `SK_LOOKUP` BPF 的诞生：

1. [Programming socket lookup with BPF](https://linuxplumbersconf.org/event/4/contributions/487/), LPC, 2019
2. [It’s crowded in here](https://blog.cloudflare.com/its-crowded-in-here/), Cloudflare blog, 2019
3. [Steering connections to sockets with BPF socket lookup hook](https://github.com/jsitnicki/ebpf-summit-2020)，eBPF Summit，2020

**由于译者水平有限，本文不免存在遗漏或错误之处。如有疑问，请查阅原文。**

以下是译文。

---

文章来源: https://arthurchiao.github.io/blog/birth-of-sk-lookup-bpf-zh/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)