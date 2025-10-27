---
title: WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序
url: https://buaq.net/go-174834.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:47.521288
---

# WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序

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

WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序

WinRAR 修复了一个高危漏洞 CVE-2023-40477，该漏洞允许远程攻击者通过引诱受害者打开一个特制的 RAR 压缩文件去执行任意代码。该漏洞需要欺骗用户因此危险等级评分略低为
*2023-8-19 19:24:48
Author: [www.solidot.org(查看原文)](/jump-174834.htm)
阅读量:39
收藏*

---

WinRAR 修复了一个高危漏洞 CVE-2023-40477，该漏洞允许远程攻击者通过引诱受害者打开一个特制的 RAR 压缩文件去执行任意代码。该漏洞需要欺骗用户因此危险等级评分略低为 7.8/10。该漏洞是 Zero Day Initiative 的 研究员 goodbyeselene 发现的，2023 年 6 月 8 日报告给开发商 RARLAB，漏洞存在于恢复卷处理过程中，是未能正确验证用户提供的数据导致的。RARLAB 在 8 月 2 日释出 WinRAR v6.23 修复了该漏洞。WinRAR 用户需要尽可能快的升级。WinRAR v6.23 还修复了另一个会导致错误文件初始化的漏洞。

https://www.zerodayinitiative.com/advisories/ZDI-23-1152/

文章来源: https://www.solidot.org/story?sid=75841
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)