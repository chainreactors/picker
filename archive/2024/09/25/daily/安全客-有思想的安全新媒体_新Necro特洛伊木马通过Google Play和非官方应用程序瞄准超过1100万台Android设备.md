---
title: 新Necro特洛伊木马通过Google Play和非官方应用程序瞄准超过1100万台Android设备
url: https://www.anquanke.com/post/id/300361
source: 安全客-有思想的安全新媒体
date: 2024-09-25
fetch_date: 2025-10-06T18:25:36.546450
---

# 新Necro特洛伊木马通过Google Play和非官方应用程序瞄准超过1100万台Android设备

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

# 新Necro特洛伊木马通过Google Play和非官方应用程序瞄准超过1100万台Android设备

阅读量**65539**

发布时间 : 2024-09-24 14:23:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Do son ，文章来源：securityonline

原文地址：<https://securityonline.info/new-necro-trojan-targets-over-11-million-android-devices-through-google-play-and-unofficial-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Android 用户关注的开发中，卡巴斯基实验室发现了 Necro 木马的新版本，这是一种能够感染数百万台设备的多阶段恶意软件加载程序。已发现这种最新变体潜伏在 Google Play 上提供的流行应用程序的修改版本和官方应用程序中，包括广泛使用的应用程序，例如 Wuta Camera 和 Max Browser。据估计，受感染的 Android 设备总数超过 1100 万台。

Necro 木马最初于 2019 年在 CamScanner 应用程序中发现，现已重新出现，利用 Google Play 等合法平台和非官方来源。这一次，它不仅损害了小众修改，还损害了 Spotify、WhatsApp mods、Minecraft 等知名应用程序。令人不安的是，这些受感染的版本已经通过非官方网站甚至官方应用商店进入用户设备，加剧了风险。

![]()

包含 Spotify 模组的网站 |图片来源： Kaspersky Labs

卡巴斯基的报告表明，该木马的创建者混合使用了混淆和隐写技术来逃避检测。隐写术是移动恶意软件中的一种罕见方法，用于将有效载荷隐藏在图像文件中，使标准安全系统难以检测和阻止。

![]()

Google Play 中的 Wuta Camera 应用 |图片来源： Kaspersky Labs

感染始于安装恶意加载程序，通常嵌入在 Spotify Plus 等修改后的应用程序中，该应用程序错误地声称提供额外的功能。安装后，加载程序将与远程命令和控制 （C2） 服务器建立通信。此服务器提供加密响应，其中包括伪装在 PNG 图像文件的 ARGB 通道中的隐藏有效负载。然后，加载程序提取有效负载并执行它，让攻击者控制受感染的设备。

Necro 的功能不仅仅是展示广告。它还可以：

* 下载并执行任意代码（DEX 文件）。
* 安装其他恶意应用程序。
* 打开隐藏的 Web 窗口以运行 JavaScript，这可能会在用户不知情的情况下为用户订阅付费服务。
* 通过受害者的设备创建隧道，允许攻击者进一步访问敏感数据。

根据卡巴斯基的遥测数据，Necro 在俄罗斯、巴西和越南特别活跃，但其全球影响力正在扩大。在 2024 年 8 月下旬至 9 月中旬期间，这家安全公司在全球范围内阻止了超过 10,000 次 Necro 攻击。然而，鉴于该木马能够渗透到官方和非官方应用程序分发渠道，这个数字可能只代表总感染量的一小部分。

如果您下载了任何受感染的应用程序，立即采取行动至关重要。Kaspersky 建议采取以下步骤来保护您的设备：

1. **更新或删除受感染的应用程序**：确保您的应用程序（尤其是来自 Google Play 的应用程序）是最新的。Wuta Camera 和 Max Browser 的受感染版本已从商店中删除，并提供了没有恶意代码的更新版本。
2. **坚持使用官方来源**：避免从非官方网站下载应用程序，因为这些网站通常包含恶意软件。
3. **使用可靠的安全解决方案**：安装值得信赖的移动安全解决方案，可以在像 Necro 这样的威胁感染您的设备之前检测和阻止它们。

本文翻译自securityonline [原文链接](https://securityonline.info/new-necro-trojan-targets-over-11-million-android-devices-through-google-play-and-unofficial-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300361](/post/id/300361)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-necro-trojan-targets-over-11-million-android-devices-through-google-play-and-unofficial-apps/)

如若转载,请注明出处： <https://securityonline.info/new-necro-trojan-targets-over-11-million-android-devices-through-google-play-and-unofficial-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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