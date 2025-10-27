---
title: 微软揭露了四个导致潜在 RCE 和 LPE 的 OpenVPN 漏洞
url: https://www.anquanke.com/post/id/299037
source: 安全客-有思想的安全新媒体
date: 2024-08-13
fetch_date: 2025-10-06T18:00:28.568125
---

# 微软揭露了四个导致潜在 RCE 和 LPE 的 OpenVPN 漏洞

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

# 微软揭露了四个导致潜在 RCE 和 LPE 的 OpenVPN 漏洞

阅读量**44398**

发布时间 : 2024-08-12 14:21:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft周四披露了开源OpenVPN软件中的四个中等严重性安全漏洞，这些漏洞可以链接以实现远程代码执行（RCE）和本地权限提升（LPE）。

“这种攻击链可能使攻击者能够完全控制目标端点，可能导致数据泄露、系统破坏和未经授权访问敏感信息，”Microsoft威胁情报社区的弗拉基米尔·托卡列夫说。

也就是说，Black Hat USA 2024 提出的漏洞利用需要用户身份验证和对 OpenVPN 内部工作原理的深入理解。这些漏洞会影响版本 2.6.10 和 2.5.10 之前的所有 OpenVPN 版本。

漏洞列表如下 –

* CVE-2024-27459 – 导致 Windows 中出现拒绝服务 （DoS） 和 LPE 的堆栈溢出漏洞
* CVE-2024-24974 – 未经授权访问 Windows 中的“\\openvpn\\service”命名管道，允许攻击者远程与其交互并在其上启动操作
* CVE-2024-27903 – 插件机制中存在一个漏洞，导致 Windows 中的 RCE，以及 Android、iOS、macOS 和 BSD 中的 LPE 和数据操作
* CVE-2024-1305 – 导致 Windows 中 DoS 的内存溢出漏洞

四个漏洞中的前三个漏洞源于名为 openvpnserv 的组件，而最后一个漏洞位于 Windows 终端接入点 （TAP） 驱动程序中。

一旦攻击者获得对用户 OpenVPN 凭据的访问权限，所有漏洞都可以被利用，而这些凭据又可以通过各种方法获得，包括在暗网上购买被盗的凭据、使用窃取恶意软件或嗅探网络流量以捕获 NTLMv2 哈希值，然后使用 HashCat 或 John the Ripper 等破解工具来解码它们。

然后，攻击者可以以不同的组合（CVE-2024-24974 和 CVE-2024-27903 或 CVE-2024-27459 和 CVE-2024-27903）分别实现 RCE 和 LPE。

“攻击者可以利用四个发现的漏洞中的至少三个来创建漏洞利用，以促进RCE和LPE，然后可以将它们链接在一起以创建一个强大的攻击链，”Tokarev说，并补充说他们可以在实现LPE后利用自带易受攻击的驱动程序（BYOVD）等方法。

“例如，通过这些技术，攻击者可以禁用关键进程（如Microsoft Defender）的保护进程轻（PPL），或者绕过并干预系统中的其他关键进程。这些行动使攻击者能够绕过安全产品并操纵系统的核心功能，从而进一步巩固他们的控制并避免被发现。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299037](/post/id/299037)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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