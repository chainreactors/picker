---
title: 新型勒索软件“SpiderX”问世，成为臭名昭著的暗黑破坏神的继任者
url: https://www.anquanke.com/post/id/296982
source: 安全客-有思想的安全新媒体
date: 2024-06-01
fetch_date: 2025-10-06T16:55:21.055939
---

# 新型勒索软件“SpiderX”问世，成为臭名昭著的暗黑破坏神的继任者

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

# 新型勒索软件“SpiderX”问世，成为臭名昭著的暗黑破坏神的继任者

阅读量**171322**

发布时间 : 2024-05-31 12:15:14

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/spiderx-new-ransomware/>

译文仅供参考，具体内容表达以及含义原文为准。

一个名为“phant0m”的威胁行为者正在臭名昭著的暗网论坛 OnniForums 上推广一种新的勒索软件即服务 (RaaS)。这种名为“SpiderX”的新勒索软件专为 Windows 系统设计，拥有一套先进的功能，使其成为之前臭名昭著的 Diablo 勒索软件的强大继任者。

Phant0m 在一篇题为“SpiderX 勒索软件简介”的详细帖子中介绍了 SpiderX，声称经过数月的开发，这款新的勒索软件已经准备好取代 Diablo。

这篇帖子重点介绍了 SpiderX 的勒索软件增强功能以​​及相对于其前身的改进。Phant0m 称 SpiderX 集成了 Diablo 的所有功能，并增加了一些旨在使其更有效、更难检测和删除的附加功能。

经过几个月的努力，| 宣布发布我的全新 Spiderx勒索软件。它将是我的 Diablo 的继任者，它确实很好地完成了它的使命，但现在终于是时候将它升级到一个全新的水平了，”威胁行为者的帖子中写道。

### **SpiderX 勒索软件的主要功能和能力**

SpiderX 是用C++编写的，phant0m 声称这种选择比 C# 和 Python 等其他语言执行速度更快。这种语言选择，加上勒索软件的小负载大小（500-600 KB，包括嵌入的自定义壁纸），确保快速高效地部署。

**ChaCha20-256加密算法：**
SpiderX 的一大突出特点是采用了 ChaCha20-256 加密算法。该算法以速度快著称，它使 SpiderX 能够以比常用的 AES-256 更快的速度加密文件，从而缩短勒索软件使受害者的文件无法访问所需的时间。

**离线功能：**
与 Diablo 一样，SpiderX 不需要互联网连接即可执行其主要功能。一旦启动，它可以加密受害者计算机上的文件并连接外部设备（例如 USB 驱动器），而无需与远程服务器通信。这使得 SpiderX 在其初始攻击阶段特别隐蔽且难以被发现。

**全面定位：**
SpiderX 的攻击范围不仅限于 Windows 驱动器上的主用户文件夹。它针对连接到系统的所有外部分区和驱动器，确保全面加密。这包括攻击后可能连接的 USB 驱动器和其他外部存储设备，这些设备也将被加密，从而放大攻击的影响。

**内置信息窃取程序：**
SpiderX 的一个新功能是其内置的信息窃取程序。一旦勒索软件被执行，该组件就会从目标系统中窃取数据，将其压缩为 zip 文件，然后将其上传到文件传输和云存储平台 MegaNz。这些被盗数据可能包含敏感信息，攻击者可以利用或出售这些信息。该过程旨在不留痕迹，掩盖其踪迹以避免被发现。

**持久且静默运行：**
SpiderX 的设计完全持久，可在后台静默运行，继续加密系统中添加的任何新文件。这种持久性确保即使受害者在初始攻击后尝试正常使用系统，勒索软件仍保持活跃。

![蜘蛛X]()
来源：暗网
**面向网络犯罪分子销售**
Phant0m 以 150 美元的价格向其他网络犯罪分子推销 SpiderX，接受以匿名性著称的比特币和门罗币付款。实惠的价格和强大的功能使 SpiderX 成为恶意行为者以最小努力进行勒索软件攻击的诱人工具。

**影响和威胁评估**
SpiderX 在暗网上的出现标志着勒索软件服务功能显著增强。其先进的功能（如 ChaCha20-256 加密算法和内置信息窃取程序）加上离线操作能力使其成为一种高效且危险的工具。勒索软件的持久性及其对联网设备的全面攻击进一步增加了其潜在影响。

随着勒索软件的不断演变，像 SpiderX 这样的工具对网络安全的威胁越来越大。最令人担忧的是，由于其成本低、效率高，SpiderX 可能会被广泛使用。

SpiderX 勒索软件的功能和易部署性凸显了警惕性和高级安全措施的必要性，以防范日益复杂的网络威胁。建议组织和个人加强网络安全措施，包括定期备份数据、更新软件和系统，以及采用增强的安全协议来降低此类攻击的风险。

本文翻译自 [原文链接](https://thecyberexpress.com/spiderx-new-ransomware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296982](/post/id/296982)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/spiderx-new-ransomware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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