---
title: 苹果集中发布更新修复入侵卡巴斯基的三角测量漏洞 用户应尽快升级
url: https://buaq.net/go-170242.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:42.198002
---

# 苹果集中发布更新修复入侵卡巴斯基的三角测量漏洞 用户应尽快升级

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

![](https://8aqnet.cdn.bcebos.com/f75b87abfc4e78f8a147cdf2eb1ddfe3.jpg)

苹果集中发布更新修复入侵卡巴斯基的三角测量漏洞 用户应尽快升级

6 月初安全公司卡巴斯基发布分析报告揭露名为三角测量 (IOSTriangulation)的攻击事件，在这起攻击事件中黑客集团利用 iMessage 零点击漏洞 (0click) 渗透
*2023-6-25 20:18:50
Author: [www.landiannews.com(查看原文)](/jump-170242.htm)
阅读量:37
收藏*

---

[6 月初安全公司卡巴斯基发布分析报告揭露名为三角测量 (IOSTriangulation)的攻击事件](https://www.landiannews.com/archives/98951.html)，在这起攻击事件中黑客集团利用 iMessage 零点击漏洞 (0click) 渗透到卡巴斯基员工的 iPhone 中，试图窃取机密信息。

分析发现黑客至少在 2019 年就已经成功渗透了卡巴斯基员工的 iPhone，到 2022 年夏季卡巴斯基发现了异常，随后开始追踪。

追踪显示发起这次攻击的黑客集团大概率背后有国家力量支持，因为 iOS 平台的零点击漏洞实在太难得了，在黑市里高峰期甚至能卖到 400 万美元。卡巴斯基认为自己不是黑客集团的主要目标，毕竟黑客不差钱，大概率是有其他目的的。

[![苹果集中发布更新修复入侵卡巴斯基的三角测量漏洞 用户应尽快升级](https://img.lancdn.com/landian/2023/05/98951.png)](https://img.lancdn.com/landian/2023/05/98951.png)

卡巴斯基在 2 月份向苹果通报了漏洞，苹果也修复了其中一个漏洞，但没有给卡巴斯基回复。

本周苹果发布 iOS 16.5.1 版、iPadOS 16.5.1 版、iOS 15.7.7 版、iPadOS 15.7.7 版、macOS Ventura 13.4.1 版、macOS Monterey 12.6.7 版、macOS Big Sur 11.7.8 版、watchOS 9.5.2 版、watchOS 8.8.1 版、Safari 16.5.1 版对卡巴斯基以及安全研究人员发现的漏洞进行了集中修复。

有一个漏洞是匿名研究人员提交的，漏洞编号为 CVE-2023-32439，是 WebKit 中的漏洞，苹果称这枚漏洞可能也已经遭到了积极利用，也就是属于零日漏洞范畴。

**以下是漏洞编号及说明：**

CVE-2023-32434：内核中的整数溢出漏洞，应用程序能够使用内核权限执行任意代码，黑客在 iOS 15.7 之前的版本开始就积极利用了该漏洞，漏洞由卡巴斯基报告。

CVE-2023-32435：WebKit 中的内存损坏漏洞，处理 Web 内容时可能导致任意代码执行，黑客在 iOS 15.7 之前的版本开始就积极利用了该漏洞，漏洞由卡巴斯基报告。

CVE-2023-32439：处理恶意制作的 Web 内容时可能导致任意代码执行，苹果获悉有报告称此问题已被积极利用，漏洞由匿名研究人员报告。关联的 WebKit Bugzilla ID：256567

**以下是版本支持说明：**

iOS/iPadOS 16.5.1 版：支持 iPhone 8 及后续机型、iPad Pro 所有机型、第 3 代 iPad Air 及后续机型、第 5 代 iPad 及后续机型、第 5 代 iPad Mini 及后续机型

iOS/iPadOS 15.7.7 版：支持 iPhone 6s 系列、iPhone 7 系列、第 1 代 iPhone SE、第 2 代 iPad Air、第 4 代 iPad Mini、第 7 代 iPod Touch

watchOS 9.5.2 版：支持 Apple Watch S4 及后续机型

watchOS 8.8.1 版：支持 Apple Watch S3~S7、SE

Safari 16.5.1 版：支持运行 macOS Monterey 的 Mac

对于上面没有提到的机型例如 iPhone 5s 等则没有更新，使用受支持设备的用户请转到设置、通用里检查更新获取最新版本。

附苹果安全公告页面：<https://support.apple.com/en-us/HT201222>

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99232.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99232.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)