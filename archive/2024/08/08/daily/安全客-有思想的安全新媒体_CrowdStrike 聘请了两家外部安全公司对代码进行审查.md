---
title: CrowdStrike 聘请了两家外部安全公司对代码进行审查
url: https://www.anquanke.com/post/id/298887
source: 安全客-有思想的安全新媒体
date: 2024-08-08
fetch_date: 2025-10-06T17:59:25.492478
---

# CrowdStrike 聘请了两家外部安全公司对代码进行审查

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

# CrowdStrike 聘请了两家外部安全公司对代码进行审查

阅读量**71911**

发布时间 : 2024-08-07 15:41:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：theregister

原文地址：<https://www.theregister.com/2024/08/07/crowdstrike_full_incident_root_cause_analysis/>

译文仅供参考，具体内容表达以及含义原文为准。

CrowdStrike已经聘请了两家外部安全公司来审查其威胁检测套件Falcon，该套件上个月引发了全球IT中断 – 尽管它可能没有太多可发现的东西，因为CrowdStrike已经确定了导致崩溃的简单错误。

外部审查的消息出现在信息安全供应商周二发布的根本原因分析[PDF]中。

正如我们从 CrowdStrike 早些时候关于有缺陷的 Falcon 更新的事后文章中了解到的那样，该更新在全球数百万台 Windows 机器上启动循环，问题始于 2 月份。

就在那时，开发人员向 Falcon 添加了发现和阻止命名管道和其他 Windows 进程间通信 （IPC） 机制的新颖利用的能力;在野外看到此类攻击发生强烈表明一个盒子已被破坏，这是一件好事，标记并停止。

在CrowdStrike将其作为新的“模板类型”推送到客户的Falcon传感器版本7.11之前，这种新的检测功能经过了通常的开发和测试。

顾名思义，这些模板类型是：模板。它们是通用的软件例程，每个例程都会在系统上捕获不同类型的潜在不良活动。为了让 Falcon 使用它们来检测特定威胁，CrowdStrike 定义并发布了所谓的“模板实例”，这些实例自定义模板代码以识别特定形式的利用、入侵和其他不良内容。

CrowdStrike 这样解释这种架构：“模板类型代表一种传感器功能，它支持新的遥测和检测，它们的运行时行为由模板实例动态配置。

自 3 月以来，CrowdStrike 已从其云端推送到远程 Falcon 部署，这些模板实例利用 IPC 模板类型代码来检测特定威胁。这些更新作为所谓的“快速响应内容”提供，存储在编号为 291 的频道文件中。Falcon 将在可用时下载更新的 channel 291 文件，并解析其数据。

该数据中的模板实例将告诉 Falcon 如何使用相关的模板类型来检测特定威胁。实例通过将正则表达式格式的参数传递给其模板类型来实现此目的。在基于 C++ 的内容解释器的帮助下，模板类型使用这些正则表达式（是的，正则表达式）参数来对抗类型正在监视的任何资源，以确定是否成功进行了检测。

通过根本原因分析，可以更深入地了解接下来出了什么问题：

新的 IPC 模板类型定义了 21 个输入参数字段，但使用通道文件 291 的模板实例调用内容解释器的集成代码仅提供 20 个输入值进行匹配。

这种参数计数不匹配避免了多层构建验证和测试，因为在传感器发布测试过程、模板类型（使用测试模板实例）压力测试或现场成功部署IPC模板实例的前几次过程中都没有发现。

在某种程度上，这是由于在测试期间和初始IPC模板实例中对第21个输入使用了通配符匹配标准。

据我们所知，这意味着：检测恶意 IPC 使用的模板类型有 21 个可能的输入值来自定义其操作，尽管将通道文件的实例参数插入解释器以与该模板类型一起使用的代码仅提供了 20 个。对于初始实例，这不是问题，因为实例不会导致解释器使用缺少的第 21 个参数。一切似乎都很好。早期的测试和验证也忽略了这一点。

然后，正如 CrowdStrike 之前解释的那样，在 7 月 19 日那次命运多舛的频道 291 文件更新中，另外两个 IPC 模板实例自动部署到 Falcon 用户。

其中一个实例首次指示解释器使用第 21 个参数，但只向该代码提供了 20 个参数。不幸的是，这导致在 Windows 内核模式下运行的内容解释器使用未初始化的字段（缺少第 21 个参数）作为指针，这导致它接触未分配的内存并最终导致操作系统崩溃。

“尝试访问第 21 个值会产生超出输入数据数组末端的越界内存读取，并导致系统崩溃，”安全商店在其分析中总结道。

CrowdStrike 更新了其传感器内容编译器，以确保将来的模板类型从实例获取正确数量的输入，并于 7 月 27 日投入生产。

CrowdStrike 还写道，它已经向内容解释器添加了运行时边界检查，用于快速响应更新，以确保它不会再次读取其输入数组的末尾。此修复程序和另一项检查数组大小是否正确的检查正在使用传感器软件修补程序向后移植到所有 Windows 传感器版本 7.11 及更高版本。该版本将于 8 月 9 日正式发布。

此外，受到惩罚的安全供应商正在进行更多的内部测试，以确保将来不会将有缺陷的文件推送给 Falcon 客户。尽管参数不匹配，但 CrowdStrike 的验证引擎错过了这个错误，并允许将错误的频道文件泄露给用户。

此外，正如 CrowdStrike 在其早期的分析中指出的那样，每个模板实例都将以分阶段的方式部署到客户手中，而不是一次性推送给所有人。这将减少任何更多中断更新的爆炸半径。

值得注意的是，该公司被投资者起诉，因为他们一开始就没有使用这种分阶段的方法。

“展望未来，CrowdStrike专注于利用从这一事件中吸取的教训来更好地为我们的客户服务，”一位发言人宣称。“CrowdStrike 始终坚定不移地履行我们保护客户和阻止违规行为的使命。”

但还没有那么坚定，以至于它点名了它雇佣来审查其节目的合作伙伴。这些审查已经开始，重点是导致7月19日惨败的代码和流程。

“我们没有提供有关为我们工作的供应商的信息，这些信息超出了根本原因分析中提到的内容，”CrowdStrike发言人告诉*The Register*。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/08/07/crowdstrike_full_incident_root_cause_analysis/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298887](/post/id/298887)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/08/07/crowdstrike_full_incident_root_cause_analysis/)

如若转载,请注明出处： <https://www.theregister.com/2024/08/07/crowdstrike_full_incident_root_cause_analysis/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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