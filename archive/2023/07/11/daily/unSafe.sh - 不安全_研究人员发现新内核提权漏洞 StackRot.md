---
title: 研究人员发现新内核提权漏洞 StackRot
url: https://buaq.net/go-171659.html
source: unSafe.sh - 不安全
date: 2023-07-11
fetch_date: 2025-10-04T11:51:25.280865
---

# 研究人员发现新内核提权漏洞 StackRot

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

研究人员发现新内核提权漏洞 StackRot

北大安全研究员 Ruihan Li 发现了一个被成为 StackRot 的内核漏洞，负责管理虚拟内存区的 maple tree 可在没有正确获得 MM 写锁的情况下进行节点替换操作，导致释
*2023-7-10 18:58:58
Author: [www.solidot.org(查看原文)](/jump-171659.htm)
阅读量:24
收藏*

---

北大安全研究员 Ruihan Li 发现了一个被成为 StackRot 的内核漏洞，负责管理虚拟内存区的 maple tree 可在没有正确获得 MM 写锁的情况下进行节点替换操作，导致释放后使用问题。非特权本地用户可利用该漏洞提权。漏洞影响 Linux v6.1-6.4，没有证据表明该漏洞正被利用。Li 表示，StackRot 位于内核内存子系统中，影响所有内核配置，触发需要的功能非常少，但利用富有挑战性。该漏洞是在 6 月 15 日披露的，7 月 1 日释出的稳定版内核 v6.1.37、6.3.11 和 6.4.1 修复了漏洞，POC 以及其它技术细节预计将在本月底公开。

https://www.openwall.com/lists/oss-security/2023/07/05/1

文章来源: https://www.solidot.org/story?sid=75471
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)