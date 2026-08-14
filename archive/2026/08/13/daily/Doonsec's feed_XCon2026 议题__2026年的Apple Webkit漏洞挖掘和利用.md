---
title: XCon2026 议题||2026年的Apple Webkit漏洞挖掘和利用
url: https://mp.weixin.qq.com/s/qR00vZbeHPlzw01xOZqlxg
source: Doonsec's feed
date: 2026-08-13
fetch_date: 2026-08-14T03:58:31.667639
---

# XCon2026 议题||2026年的Apple Webkit漏洞挖掘和利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fHEm7hZn9HJAeO0nmNnWcAWOuQpw82SauQJmMBYaGVgAuPRp5ACe2RXUib5zJAGAMAgyne0332CGL4DfVXK3fJeEHoD59SyMZuG3Csricoqo0/0?wx_fmt=jpeg)

# XCon2026 议题||2026年的Apple Webkit漏洞挖掘和利用

嘶吼专业版

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/mibLibLia0X2icBlYQrK2saVibv0aArAWAH8SmCTROs4zk2L7V7fyCVbEdicdEqHxn4SDelL4kfMib3AQ2bTukJTSTtfsGYDiaqrJzPaGibFTOK3UFcw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)

XCon2026||定义·未定义

每一道防线背后，都有人在试图寻找裂缝。

Apple WebKit，这个承载着数十亿iOS与macOS用户日常浏览体验的核心引擎，始终是浏览器安全研究领域备受关注、也最难啃的"硬骨头"之一。随着Apple逐年加固缓解机制，外界普遍认为WebKit漏洞利用的窗口正在急剧收窄。然而事实真的如此吗？

在即将于8月28日召开的XCon2026大会的现场，StringLabs的CTO ZZ以及高级安全研究员 JC将带来议题《2026年的Apple Webkit漏洞挖掘和利用》，通过一场深度的硬核分享，给出他们在2026年的实战答案。

01

议题简介

在当下的2026年，WebKit作为苹果生态的核心Web渲染引擎，漏洞挖掘和利用愈发艰难，其多进程模型、沙箱隔离、libpas内存分配器以及PAC等硬件级防护体系，构成了浏览器安全的重要防线。

本议题将系统分享当前对WebKit漏洞挖掘与利用的探索实践。

首先将会剖析WebKit的安全设计与架构，重点介绍libpas内存分配器的安全特性、分配机制与Scavenger回收机制，以及堆内存复用带来的潜在风险；同时分享PAC的基本原理，以及其与APRR、NX等机制协同缓解任意代码执行的作用。 随后分析2025-2026年WebKit漏洞趋势，并在此基础上分享研究过程中使用的一些漏洞利用技巧，包括原语构建、JIT与堆布局操控，以及完整攻击链的构建思路。针对缓解措施，重点探讨StructureID随机化与PAC的主流绕过策略，并分析其实际有效性与局限性。

02

议题亮点

本次演讲将围绕以下四个方面展开：

* WebKit安全架构与libpas内存分配器深度解析：系统梳理多进程模型与沙箱隔离机制，重点剖析libpas内存分配器的安全特性、分配与Scavenger回收机制，以及堆内存复用实例，揭示其在漏洞利用中的关键作用；同时讲解PAC的基本原理与APRR、NX的协同缓解机制。
* 漏洞利用原语构建与链式攻击实践：通过一些实际漏洞案例，分享利用原语构建方法、JIT与堆布局的操控技巧，以及如何将多个漏洞串联形成完整攻击链的实战经验，u涵盖StructureID绕过与OOB等漏洞能力扩展等关键环节。
* 现代缓解措施绕过策略与技术路径： 重点探讨StructureID随机化与PAC的主流绕过思路，系统呈现当前多种技术路径的实践方法，并深入分析其在实际环境中的有效性、局限性以及对防御体系演进的影响。
* 分享业界 AI Agent 在 WebKit 安全领域的进展：探讨部分 AI Agent 在 WebKit 漏洞挖掘与利用方面的进展和成果，并分析 WebKit 等 Web 引擎在 AI 冲击下的风险与展望。

03

演讲人介绍

ZZ——StringLabs CTO

主要从事移动端、浏览器和区块链的漏洞挖掘和利用的安全研究，漏洞挖掘和研究成果曾获得 Apple、Google、Huawei、Web3社区等公开致谢。也曾从事过安全产品的设计与研发。目前专注于漏洞研究和AI相结合的探索。

JC——StringLabs 高级安全研究员

高级安全研究员 主要从事编译器（web2/3）相关的漏洞安全研究。曾在宝马、HP等多家外企从事编译器相关研究和研发，也曾参与某主流编译器生态的构建。目前专注于漏洞安全研究。

**XCon2026售票通道现已全面开启**

**【体验票】****¥0元**，含：分会场+展商互动区

**【学生票】****¥398元，**XCon2026全场通——含：主会场＋分会场+展商互动区

\*特别说明：购买学生票，现场验票时，须出示有效期内学生证。如无法提供有效证件，需按普通票补齐票价

【学生票】团购专项 2张享9折、5张享7折

10张享5折

**【普通票】****¥2790元，**XCon2026全场通——含：主会场＋分会场+展商互动区

【普通票】团购专项 5张享7折、10张享5折

![图片](https://mmbiz.qpic.cn/mmbiz_png/pX30G7omHPotGkiaeRRrfOzpuCIwiaftAr1SRAl0iaELpsPlKnIwEicnic0JwWkFTibSJ7Ttve2eX6PRSKc4Z7mbtMxQ/640?wx_fmt=png&wx_lazy=1&wx_co=1&wxfrom=5&tp=wxpic#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/mibLibLia0X2icBZxXhdgjOf3JPQtmL3cJfz76zBiaM5C2VbG02MerXBzdjNmpSq2DVlJDDjImXYmaLm0eJaNOeiaY8UV90k5bUhplVkjMr7P3LP4/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=4)

微信号：XConXFocus

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过