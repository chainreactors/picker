---
title: 英特尔探索仅 64 位的 x86S 架构
url: https://buaq.net/go-164989.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:48.767469
---

# 英特尔探索仅 64 位的 x86S 架构

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

英特尔探索仅 64 位的 x86S 架构

自 Windows 7 时代以来，大部分 PC 用户运行的 Windows 操作系统都是 64 位，搭载的内存超过了 4GB，64 位应用和游戏都逐渐成为了主流。对芯片巨人而言，是时候简化
*2023-5-21 22:58:46
Author: [www.solidot.org(查看原文)](/jump-164989.htm)
阅读量:22
收藏*

---

自 Windows 7 时代以来，大部分 PC 用户运行的 Windows 操作系统都是 64 位，搭载的内存超过了 4GB，64 位应用和游戏都逐渐成为了主流。对芯片巨人而言，是时候简化 x86 指令集架构了。英特尔发表了一份白皮书，探索了仅 64 位的 x86S 架构，主要包括：用 64 位的简化分段模型分段支持 32 位应用；移除 ring 1 和 2，以及过时的分段功能如门；移除 16 位寻址支持；移除对 ring 3 I/O 端口访问的支持；移除字符串端口 I/O；限制本地中断控制器（APIC）使用 X2APIC，移除 8259 支持；移除未使用操作系统模式位。64 位的 x86S 芯片仍然支持 32 位应用，但不再支持 32 位操作系统。

https://cdrdv2.intel.com/v1/dl/getContent/776648

文章来源: https://www.solidot.org/story?sid=75012
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)