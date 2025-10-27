---
title: [译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）
url: https://buaq.net/go-135304.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:22.035444
---

# [译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）

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

![](https://8aqnet.cdn.bcebos.com/13ff8e1a1dff4946110707538720bcc4.jpg)

[译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）

Published at 2022-11-12 | Last Update 2022-11-12 译者序本文翻译自 KubeCon+CloudNativeCon
*2022-11-12 08:0:0
Author: [arthurchiao.github.io(查看原文)](/jump-135304.htm)
阅读量:126
收藏*

---

Published at 2022-11-12 | Last Update 2022-11-12

### 译者序

本文翻译自 KubeCon+CloudNativeCon North America 2022 的一篇分享：
[100 Gbit/s Clusters with Cilium: Building Tomorrow’s Networking Data Plane](https://kccncna2022.sched.com/event/182DB)。

作者 Daniel Borkmann, Nikolay Aleksandrov, Nico Vibert 都来自 Isovalent（Cilium 母公司）。
翻译时补充了一些背景知识、代码片段和链接，以方便理解。

翻译已获得 Daniel 授权。

**由于译者水平有限，本文不免存在遗漏或错误之处。如有疑问，请查阅原文。**

以下是译文。

---

文章来源: https://arthurchiao.github.io/blog/cilium-tomorrow-networking-data-plane-zh/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)