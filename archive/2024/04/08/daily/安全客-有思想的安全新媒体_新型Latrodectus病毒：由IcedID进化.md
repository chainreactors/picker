---
title: 新型Latrodectus病毒：由IcedID进化
url: https://www.anquanke.com/post/id/295339
source: 安全客-有思想的安全新媒体
date: 2024-04-08
fetch_date: 2025-10-04T12:14:47.290281
---

# 新型Latrodectus病毒：由IcedID进化

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 新型Latrodectus病毒：由IcedID进化

阅读量**123084**

发布时间 : 2024-04-07 11:29:26

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/547279.php>

译文仅供参考，具体内容表达以及含义原文为准。

Proofpoint和Team Cymru 专家发现了 一种新病毒，名为 Latrodectus，被认为是著名的IcedID下载器的演变，自 2023 年 11 月以来，该病毒一直在网络钓鱼电子邮件中活跃使用。

IcedID 于 2017 年首次被发现，被归类为模块化银行木马，旨在从受感染的计算机中窃取财务信息。随着时间的推移，它变得更加复杂，获得了逃避检测和执行命令的能力。

IcedID 最近已发展成 为用于传播其他类型恶意软件（包括勒索软件）的下载器。 2024 年 2 月，IcedID 运动的一位领导人 在美国联邦法院认罪 ；他每项指控都将面临最高 20 年的监禁。

根据 Proofpoint 和 Team Cymru 的研究，IcedID 和 Latrodectus 之间存在一定的联系，包括基础设施和操作方面的相似之处，表明后者是由 IcedID 的开发人员创建的。

[![]()](https://www.securitylab.ru/upload/medialibrary/0a6/zl9lbay756n9xpbx11nqukmx1c77wfer.png)

*IcedID 和 Latrodectus 基础设施重叠*

Latrodectus 是一个能够从C2服务器接收额外恶意负载的下载程序。该病毒还执行各种检查来逃避检测，包括根据 Windows 版本要求运行进程的数量以及检查有效的 MAC 地址。

其中，Latrodectus 支持以下命令：

* 获取桌面上的文件名；
* 获取正在运行的进程列表；
* 发送有关系统的附加信息；
* 运行可执行文件；
* 执行DLL；
* 终止正在运行的进程。

攻击者通过填写反馈表并向目标组织报告版权侵权行为来发起攻击。在消息中，黑客还留下了一个链接，将受害者引导至 Google Firebase 页面，从该页面下载恶意 J​​avaScript 文件。然后，该文件使用 Windows Installer 启动包含恶意 Latrodectus 库的 MSI 文件。

[![]()](https://www.securitylab.ru/upload/medialibrary/cf4/swj72y90w65d2hinn9xgecpcq8nxxuvj.png)

*版权侵权诱饵消息*

该病毒的基础设施分为两层，这使其能够灵活地管理活动及其持续时间。新的 C2 服务器在攻击前的周末尤其活跃。

根据他们的研究，鉴于 Latrodectus 先进的规避能力和恶意负载，Proofpoint 对 Latrodectus 未来在网络犯罪活动中的使用表示担忧。据信，Latrodectus 在之前使用过 IcedID 的网络犯罪分子中传播的可能性仍然很高。

本文翻译自 [原文链接](https://www.securitylab.ru/news/547279.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295339](/post/id/295339)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/547279.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)