---
title: 新型 PIXHELL 攻击利用屏幕噪音从气隙计算机中窃取数据
url: https://www.anquanke.com/post/id/299974
source: 安全客-有思想的安全新媒体
date: 2024-09-12
fetch_date: 2025-10-06T18:22:44.468077
---

# 新型 PIXHELL 攻击利用屏幕噪音从气隙计算机中窃取数据

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

# 新型 PIXHELL 攻击利用屏幕噪音从气隙计算机中窃取数据

阅读量**84261**

发布时间 : 2024-09-11 14:33:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为 **PIXHELL** 的新型侧信道攻击可能被滥用，通过突破“音频间隙”并利用屏幕上像素产生的噪声泄露敏感信息，从而针对气隙计算机。

以色列内盖夫本古里安大学（Ben Gurion University of the Negev）软件和信息系统工程系进攻性网络研究实验室（Offensive Cyber Research Lab）的负责人莫迪凯·古里（Mordechai Guri）博士在新发表的论文中说：“气隙和音频隙计算机中的恶意软件会生成精心制作的像素模式，这些像素模式会产生0 – 22 kHz频率范围内的噪声。

“恶意代码利用线圈和电容器产生的声音来控制从屏幕发出的频率。声学信号可以编码和传输敏感信息。

该攻击值得注意的是，它不需要在受感染的计算机上安装任何专用的音频硬件、扬声器或内部扬声器，而是依靠 LCD 屏幕来产生声音信号。

气隙隔离是一项重要的安全措施，旨在通过物理和逻辑隔离任务关键型环境与外部网络（即互联网）隔离，保护关键任务环境免受潜在的安全威胁。这通常是通过断开网络电缆、禁用无线接口和禁用 USB 连接来实现的。

也就是说，可以通过流氓 Insider 或破坏硬件或软件供应链来规避此类防御。另一种情况可能涉及毫无戒心的员工插入受感染的 USB 驱动器，以部署能够触发秘密数据泄露通道的恶意软件。

“网络钓鱼、恶意内部人员或其他社会工程技术可能被用来诱骗有权访问气隙系统的个人采取危及安全性的操作，例如点击恶意链接或下载受感染的文件，”Guri 博士说。

“攻击者还可能通过针对软件应用程序依赖项或第三方库来使用软件供应链攻击。通过破坏这些依赖项，它们可能会引入漏洞或恶意代码，而这些漏洞或恶意代码在开发和测试过程中可能会被忽视。

与最近演示的 RAMBO 攻击一样，PIXHELL 利用部署在受感染主机上的恶意软件创建一个声学通道，用于从音频间隙系统中泄露信息。

这是由于 LCD 屏幕的内部组件和电源中包含电感器和电容器，导致它们以可听见的频率振动，当电流通过线圈时会产生高音调的噪音，这种现象称为线圈啸叫。

具体来说，功耗的变化会在电容器中引起机械振动或压电效应，从而产生可闻噪声。影响消费模式的一个关键方面是被照亮的像素数量及其在屏幕上的分布，因为白色像素比深色像素需要更多的显示功率。

“此外，当交流电 （AC） 通过屏蔽电容器时，它们会以特定频率振动，”Guri 博士说。“声源是由 LCD 屏幕的内部电气部分产生的。其特性受实际位图、图案和投影在屏幕上的像素强度的影响。

“通过仔细控制屏幕上显示的像素图案，我们的技术可以从 LCD 屏幕产生特定频率的某些声波。”

因此，攻击者可以利用该技术以声音信号的形式泄露数据，然后将其调制并传输到附近的 Windows 或 Android 设备，这些设备随后可以解调数据包并提取信息。

话虽如此，值得注意的是，发出的声学信号的功率和质量取决于特定的屏幕结构、内部电源以及线圈和电容器的位置等因素。

另一个需要强调的重要一点是，默认情况下，PIXHELL 攻击对查看 LCD 屏幕的用户可见，因为它涉及显示由交替的黑白行组成的位图模式。

“为了保持隐蔽性，攻击者可能会使用一种在用户不在时进行传输的策略，”古里博士说。“例如，在下班时间对秘密频道进行所谓的’夜间攻击’，从而降低被揭露和暴露的风险。”

然而，通过在传输之前将像素颜色降低到非常低的值，即使用 （1,1,1）、（3,3,3）、（7,7,7） 和 （15,15,15） 的 RGB 级别，可以在工作时间内将攻击转变为隐蔽攻击，从而给用户留下屏幕为黑色的印象。

但这样做的副作用是“显着”降低声音制作水平。这种方法也不是万无一失的，因为如果用户“仔细”看屏幕，他们仍然可以辨认出异常模式。

这不是第一次在实验性设置中克服 audio-gap 限制。Guri 博士之前进行的研究采用了计算机风扇 （Fansmitter）、硬盘驱动器 （Diskfiltration）、CD/DVD 驱动器 （CD-LEAK）、电源装置 （POWER-SUPPLaY） 和喷墨打印机 （Inkfiltration） 产生的声音。

作为对策，建议使用声学干扰器来中和传输，监控音频频谱中是否有异常或不常见的信号，限制授权人员的物理访问，禁止使用智能手机，并使用外部摄像头来检测异常的调制屏幕模式。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299974](/post/id/299974)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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