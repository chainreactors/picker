---
title: Void Manticore：伊朗威胁行为者利用数据擦除器瞄准以色列及其他地区
url: https://www.anquanke.com/post/id/296636
source: 安全客-有思想的安全新媒体
date: 2024-05-22
fetch_date: 2025-10-06T16:48:59.689715
---

# Void Manticore：伊朗威胁行为者利用数据擦除器瞄准以色列及其他地区

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

# Void Manticore：伊朗威胁行为者利用数据擦除器瞄准以色列及其他地区

阅读量**132631**

发布时间 : 2024-05-21 10:25:03

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/void-manticore-iranian-threat-actor/>

译文仅供参考，具体内容表达以及含义原文为准。

隶属于情报和安全部 (MOIS) 的伊朗威胁行为者正在使用破坏性数据擦除攻击并结合影响行动来针对以色列和阿尔巴尼亚。

该威胁行为者被追踪为 Void Manticore（又名 Storm-842），以多个在线角色进行操作，其中主要别名包括针对阿尔巴尼亚袭击的“Homeland Justice”和针对以色列袭击的“Karma”。

自 2023 年 10 月以来，Check Point Research一直在监控Void Manticore 针对以色列组织的活动，这些活动使用擦除器和勒索软件进行破坏性攻击。该组织采用五种不同的方法进行破坏性操作，包括针对 Windows 和 Linux 操作系统的自定义擦除器，以及手动删除文件和共享驱动器。

Void Manticore 在以色列的活动以使用一种名为“BiBi”的定制擦拭器为标志，该擦拭器以以色列总理本杰明·内塔尼亚胡的名字命名。该组织还使用名为“Karma”的角色来泄露被盗信息，将自己描绘成反犹太复国主义的犹太组织。这个角色在 2023 年底以色列与哈马斯冲突期间变得引人注目。

Void Manticore 威胁行为者采用相对简单和直接的技术，通常使用基本的公开工具。他们的操作通常涉及使用远程桌面协议（RDP）的横向移动和手动部署雨刷器。他们的著名工具之一是“Karma Shell”，这是一种伪装成错误页面的自制 Web shell。该恶意 shell 能够执行目录列表、进程创建、文件上传和服务管理。

**虚空蝎狮的破坏性擦拭能力**
虚空蝎狮在攻击中使用了各种定制的擦拭器：

1. Cl Wiper：首先用于针对阿尔巴尼亚的攻击，该擦除器使用 ElRawDisk 驱动程序与文件和分区交互，通过使用预定义缓冲区覆盖物理驱动器来有效擦除数据。
2. 分区擦除器：这些擦除器会删除分区信息，破坏分区表并导致磁盘上的所有数据丢失，从而导致系统在重启时崩溃。
3. BiBi Wiper：在最近针对以色列的攻击中部署了该擦除器，该擦除器存在于 Linux 和 Windows 变体中。它会损坏文件并使用特定扩展名重命名它们，从而导致大量数据丢失。

除了自动擦除器之外，Void Manticore 还使用 Windows 资源管理器、SysInternals SDelete 和 Windows Format 实用程序等工具进行手动数据破坏，从而进一步增强对目标系统的影响。

**心理战以及与伤疤蝎狮的合作**
虚空蝎狮的策略还包括心理战，旨在通过公开泄露敏感信息来挫伤和扰乱目标目标。这种双重方法放大了网络攻击的影响，使他们成为可怕的威胁。

值得注意的是，Void Manticore 和另一个伊朗威胁组织 Scarred Manticore（又名 Storm-861）之间存在显着的重叠和合作。

分析表明，这两个群体之间存在系统性的受害者交接。例如，Scarred Manticore 可能会建立初始访问并窃取数据，然后 Void Manticore 执行破坏性数据擦除攻击。此次合作使 Void Manticore 威胁行为者能够利用 Scarred Manticore 的高级功能并获得对高价值目标的访问权限。

“就一名受害者而言，我们发现在目标网络上驻留一年多后，Scarred Manticore 正在与受感染的计算机进行交互，同时新的 Web shell 被投放到磁盘上。在部署 shell 后，一组不同的 IP 开始访问网络，这表明另一个参与者 – Void Manticore 参与其中，”研究人员表示。

“新部署的 Web shell 和后续工具明显不如 Scarred Manticore 的工具库复杂。然而，他们导致了 BiBi 擦拭器的部署，这与 Karma 的活动有关。”

Void Manticore 代表着重大的网络威胁，特别是在涉及伊朗的地缘政治紧张局势的背景下。伊朗总统易卜拉欣·莱西在该国偏远地区的一次直升机坠毁事故中丧生。周一早些时候，救援人员在阿塞拜疆边境附近的西北部山区搜寻后，发现了莱西的尸体。

自 2021 年当选以来，莱西收紧了道德法规，镇压反政府抗议活动，并抵制国际社会对德黑兰核计划的监督。以色列在加沙的战争加剧了与黎巴嫩真主党和也门胡塞武装等伊朗支持组织的冲突。上个月，伊朗和以色列发生了直接袭击。目前尚不清楚莱西的死亡是否也与以色列的行动有关。

与此同时，最近的事态升级意味着虚空蝎狮与疤痕蝎狮的协调行动，结合了技术破坏和心理操纵的双重手段，将他们定位为高度危险的参与者。他们的活动不仅针对基础设施，还旨在影响公众认知和政治稳定，凸显了现代网络战的多面性。

本文翻译自 [原文链接](https://thecyberexpress.com/void-manticore-iranian-threat-actor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296636](/post/id/296636)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/void-manticore-iranian-threat-actor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络战](/tag/%E7%BD%91%E7%BB%9C%E6%88%98)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [与白俄罗斯政府有关的威胁行为者“UNC1151”瞄准乌克兰国防部](/post/id/297067)

  2024-06-05 10:31:51
* ##### [俄罗斯黑客在波兰国家媒体上发布虚假新闻](/post/id/297025)

  2024-06-03 11:26:40
* ##### [巴塞罗那 TRAM 遭受 DDoS 攻击：NoName 组织和俄罗斯网络军声称对此负责](/post/id/296967)

  2024-05-31 10:48:15
* ##### [《纽约时报》：俄罗斯有办法破坏乌克兰的 Starlink](/post/id/296907)

  2024-05-29 11:09:26
* ##### [外媒：俄罗斯黑客使用合法远程监控软件监视乌克兰及其盟友](/post/id/296835)

  2024-05-28 10:16:44
* ##### [R00TK1T 组织在与匿名埃及发生冲突后加强了对埃及公司的网络攻击](/post/id/296507)

  2024-05-15 11:48:56
* ##### [澳大利亚在支持乌克兰的过程中面临前所未有的网络威胁](/post/id/296470)

  2024-05-14 11:00:58

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