---
title: 多年来，不断发展的 npm 包活动瞄准 Roblox 开发人员
url: https://www.anquanke.com/post/id/299756
source: 安全客-有思想的安全新媒体
date: 2024-09-05
fetch_date: 2025-10-06T18:20:00.562883
---

# 多年来，不断发展的 npm 包活动瞄准 Roblox 开发人员

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

# 多年来，不断发展的 npm 包活动瞄准 Roblox 开发人员

阅读量**119929**

发布时间 : 2024-09-04 14:50:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/evolving-npm-package-campaign-roblox-devs>

译文仅供参考，具体内容表达以及含义原文为准。

攻击者在他们的武器库中添加了激进的社会工程手段，以及一种需要开发人员保持警惕的新型 Windows 操纵持久性机制。

![Roblox 徽标和显示在某人手中的移动设备屏幕上的各种游戏角色]( "Roblox logo and various gaming characters displayed on a mobile device screen held in someone's hand")

SOPA 图片有限公司通过 Alamy Stock Photo

至少一年来，攻击者一直在使用模仿流行的“noblox.js”库的恶意 Node Package Manager （npm） 包，以恶意软件为目标 Roblox 游戏开发人员，这些恶意软件会窃取 Discord 令牌和系统数据，甚至部署额外的有效负载。

该活动由 Checkmarx 的研究人员概述，至少自 2023 年 8 月以来一直活跃，它利用各种策略，包括品牌劫持、组合抢注和劫持，以使包裹看起来合法。一旦在目标系统上站稳脚跟，恶意软件就会收集各种类型的敏感数据，这些数据使用 Discord webhook 以包的形式发送到攻击者的命令和控制服务器 （C2）。

Roblox 是一个流行的游戏和游戏创建平台，拥有超过 7000 万日活跃用户的用户群，因此是威胁行为者的诱人目标。ReversingLabs 的研究人员此前披露了针对 Roblox 并交付 Luna Grabber 恶意软件的 npm 包活动，其他公司也对此进行了报道。

Checkmarx 安全研究员 Yehuda Gelb 在一篇文章中写道，Checkmarx 分析揭示了它如何随着使用各种社会工程策略来增加欺骗以及新的恶意活动而演变，包括将 QuasarRAT 添加到其二级有效载荷列表中在 Medium 平台上。它从用户“aspdasdksa2”拥有的活动 GitHub 存储库中提供辅助恶意软件，他写道，该存储库“可能用于通过其他包分发恶意软件”。

该活动提供的其他恶意软件添加了一种新颖的持久性机制，可以操纵 Windows 注册表。Gelb 指出，这确保了每次用户打开 Windows 设置应用程序时都执行，并且“是恶意软件有效性的核心”。

更重要的是，攻击者似乎高度关注其恶意活动的任何缓解措施——考虑到活动的持续时间和新型恶意包的持续流动，这一点很明显。“尽管多次删除了多个包，但在发布时，新的恶意包仍继续出现在 npm 注册表中，”Gelb 写道。

## 游戏开发者欺骗的社会工程

该活动以精心设计的社会工程为特色，表明攻击者了解他们的受众，并旨在使包看起来对 Roblox 开发人员来说尽可能真实和有用。

Gelb 写道，一种拼写错误技术结合了这种策略的子集——品牌劫持和组合抢注——在程序包的命名中创造了“他们的程序包要么是合法的’noblox.js’库的扩展，要么与合法的”库密切相关的错觉”。其中包括 noblox.js-async、noblox.js-thread 和 noblox.js-api 等文件名。

攻击者还使用“星劫”，这是威胁行为者用来夸大程序包统计信息的一种策略，因此开发人员认为程序包的下载量超过实际量，因此值得信赖。Gelb 说，在这种情况下，攻击者将恶意包链接到正版“noblox.js”包的 GitHub 存储库 URL。

该活动中采用的进一步策略试图通过模仿合法的“noblox.js”文件的结构来掩盖程序包本身中的恶意软件，但随后会在 postinstall.js 文件中引入恶意代码。“他们严重混淆了这些代码，甚至包含了无意义的汉字，以阻止轻松分析，”Gelb 指出。

## 禁用 Windows Defender for Persistence

随着活动的发展，攻击者继续加大赌注，使防御者更难检测和缓解其提供的恶意软件。Gelb 写道，一种这样的新策略通过针对 Malwarebytes 和 Windows Defender 等各种服务来“积极破坏系统的安全措施”。它首先针对前者，并试图在它正在运行时阻止它，“然后对 Windows Defender 进行更全面的攻击，”他写道。

“该脚本会识别所有磁盘驱动器并将它们添加到 Windows Defender 的排除列表中，”他解释说。“此操作实际上使 Windows Defender 对系统上的任何文件视而不见。”

Gelb 指出，总体而言，它禁用第三方防病毒软件和操纵内置 Windows 安全功能创造了一个恶意软件可以自由运行的环境，从而显着增加了其造成损害和持久性的可能性。

## 活动要求开发人员保持警惕

通过开发人员开发软件（或在本例中为游戏）所依赖的开源代码资产来瞄准开发人员，是 威胁行为者用来扩大攻击面的一种不断发展的策略。通过在开发过程中对代码进行中毒，他们可以通过软件供应链将恶意软件传播给众多用户，而无需单独针对特定系统。

事实上，Gelb 观察到，通过持续受损的 NPM 包对 Roblox 开发人员的持续攻击“清楚地提醒了开发者社区面临的持续威胁”，并要求他们在使用开源代码包时要格外小心。

他说，该活动和其他类似活动再次强调了“在纳入项目之前彻底审查一揽子计划至关重要”。“开发人员必须保持警惕，验证包的真实性，尤其是那些类似于流行库的包，以保护自己和用户免受这种复杂的供应链攻击。”

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/evolving-npm-package-campaign-roblox-devs)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299756](/post/id/299756)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/evolving-npm-package-campaign-roblox-devs)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/evolving-npm-package-campaign-roblox-devs>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [游戏开发者欺骗的社会工程](#h2-0)
* [禁用 Windows Defender for Persistence](#h2-1)
* [活动要求开发人员保持警惕](#h2-2)

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