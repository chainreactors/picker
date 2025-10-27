---
title: BlackByte 使用勒索软件瞄准 ESXi 错误以访问虚拟资产
url: https://www.anquanke.com/post/id/299608
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:20.319279
---

# BlackByte 使用勒索软件瞄准 ESXi 错误以访问虚拟资产

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

# BlackByte 使用勒索软件瞄准 ESXi 错误以访问虚拟资产

阅读量**95421**

发布时间 : 2024-08-29 15:56:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/blackbyte-targets-esxi-bug-with-ransomeware-to-access-virtual-assets>

译文仅供参考，具体内容表达以及含义原文为准。

使用臭名昭著的 BlackByte 勒索软件菌株的威胁行为者加入了快速增长的网络犯罪分子的行列，他们以 VMware ESXi 中最近的身份验证绕过漏洞为目标，以破坏企业网络的核心基础设施。

该漏洞被跟踪为 CVE-2024-37085，如果 ESXi 主机使用 AD 进行用户管理，则允许对 Active Directory （AD） 具有足够访问权限的攻击者获得对该主机的完全访问权限。

## 热门目标

Microsoft 和其他安全供应商之前发现了勒索软件组织，例如 Black Basta（又名 Storm-0506）、Manatee Tempest、Scattered Spider（又名 Octo Tempest）和 Storm-1175，它们利用 CVE-2024-37085 来部署 Akira 和 Black Basta 等勒索软件菌株。在这些攻击中，攻击者使用其 AD 权限创建或重命名一个名为“ESX Admins”的组，然后使用该组以完全特权用户身份访问 ESXi 虚拟机监控程序。

BlackByte 对该漏洞的使用代表了该威胁组织扫描和利用面向公众的漏洞（如 Microsoft Exchange 中的 ProxyShell 漏洞）以获得初步立足点的惯常做法的转变。Cisco Talos 的研究人员观察到 BlackByte 威胁行为者在最近的攻击中以 CVE-2024-37085 为目标，他们将这种策略描述为他们最近为领先于防御者而进行的几项更改之一。其他更改包括使用 BlackByteNT，这是一种用 C/C++ 编写的新 BlackByte 加密器，在受感染的系统上删除多达四个易受攻击的驱动程序，而以前是三个，并使用受害者组织的 AD 凭据进行自我传播。

Talos 的调查表明，专业、科学和技术服务领域的组织最容易受到攻击，这些攻击涉及使用合法但易受攻击的驱动程序来绕过安全机制，研究人员将这种技术称为自带易受攻击的驱动程序 （BYOVD）。

“BlackByte 在编程语言方面从 C# 发展到 Go，然后在其最新版本的加密程序 BlackByteNT 中发展到 C/C++，这代表了提高恶意软件对检测和分析的弹性的刻意努力，”Talos 研究人员 James Nutland、Craig Jackson 和 Terryn Valikodath 在本周的一篇博客文章中写道。“BlackByte 加密器的自我传播特性给防御者带来了额外的挑战。使用 BYOVD 技术加剧了这些挑战，因为它可能会限制遏制和根除工作期间安全控制的有效性。

## 不断变化

Keeper Security 首席执行官兼联合创始人 Darren Guccione 表示，BackByte 转向 ESXi 中的 CVE-2024-37085 等漏洞，这表明攻击者如何不断发展其策略、技术和程序以领先于防御者。“BlackByte 和类似的威胁行为者利用 ESXi 中的漏洞表明，他们集中精力破坏企业网络的核心基础设施，”Guccione 说。“鉴于 ESXi 服务器通常托管多个虚拟机，一次成功的攻击就可能导致广泛的破坏，使其成为勒索软件组织的主要目标。”

Sygnia 在今年早些时候调查了针对 VMWare ESXi 和其他虚拟化环境的大量勒索软件攻击，称这些攻击在大多数情况下以特定模式展开。攻击链从攻击者通过网络钓鱼攻击、漏洞利用或恶意文件下载获得对目标环境的初始访问权限开始。一旦进入网络，攻击者往往会使用策略（例如更改连接域的 VMware 实例的域组成员资格）或通过 RDP 劫持来获取 ESXi 主机或 vCenter 的凭据。然后，他们验证其凭据，并使用它们在 ESXi 主机上执行勒索软件、破坏备份系统或更改密码，然后泄露数据。

## 企业压力增加

研究人员表示，对 ESXi 环境的攻击增加了组织及其安全团队维护多功能安全计划的压力。“这包括强大的漏洞管理、威胁情报共享以及事件响应政策和程序等做法，以跟上不断发展的对手 TTP，”思科 Talos 研究人员说。“在这种情况下，漏洞管理和威胁情报共享将有助于识别对手在攻击（如 ESXi 漏洞）期间可能采取的鲜为人知或新颖的途径。”

灾难恢复公司 Fenix24 的联合创始人 Heath Renfrow 表示，对于 CVE-2024-37085，组织面临着额外的挑战，因为人们认为在实施缓解措施方面存在困难。“这些缓解措施包括断开 ESXi 与 AD 的连接，删除 AD 中以前使用的任何管理 ESXi 的组，以及将 ESXi 修补到 8.0 U3，从而修复漏洞，”Renfrow 说。“VMware 是全球使用最广泛的虚拟解决方案，其攻击范围广泛且易于利用。这使得威胁行为者可以轻松获得皇冠上的明珠并迅速造成重大损害。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/blackbyte-targets-esxi-bug-with-ransomeware-to-access-virtual-assets)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299608](/post/id/299608)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cyberattacks-data-breaches/blackbyte-targets-esxi-bug-with-ransomeware-to-access-virtual-assets)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/blackbyte-targets-esxi-bug-with-ransomeware-to-access-virtual-assets>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
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

* [热门目标](#h2-0)
* [不断变化](#h2-1)
* [企业压力增加](#h2-2)

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