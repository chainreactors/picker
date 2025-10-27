---
title: TrickMo Android 木马利用辅助功能服务进行设备银行欺诈
url: https://www.anquanke.com/post/id/300107
source: 安全客-有思想的安全新媒体
date: 2024-09-15
fetch_date: 2025-10-06T18:20:10.405602
---

# TrickMo Android 木马利用辅助功能服务进行设备银行欺诈

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

# TrickMo Android 木马利用辅助功能服务进行设备银行欺诈

阅读量**99593**

发布时间 : 2024-09-14 14:58:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种名为 TrickMo 的 Android 银行木马的新变体，该木马具有逃避分析并显示虚假登录屏幕以捕获受害者银行凭证的新功能。

“这些机制包括将格式错误的 ZIP 文件与 JSONPacker 结合使用，”Cleafy 安全研究人员 Michele Roviello 和 Alessandro Strino 说。“此外，该应用程序是通过共享相同反分析机制的 dropper 应用程序安装的。”

“这些功能旨在逃避检测并阻碍网络安全专业人员分析和缓解恶意软件的努力。”

TrickMo 于 2019 年 9 月首次被 CERT-Bund 发现，它有针对 Android 设备的历史，特别是针对德国用户窃取一次性密码 （OTP） 和其他双因素身份验证 （2FA） 代码以促进金融欺诈。

这种以移动为中心的恶意软件被评估为现已解散的 TrickBot 电子犯罪团伙所为，随着时间的推移，该团伙不断改进其混淆和反分析功能，以便在雷达下飞行。

其中值得注意的是它能够记录屏幕活动、记录击键、收集照片和 SMS 消息、远程控制受感染设备进行设备欺诈 （ODF），以及滥用 Android 的辅助功能服务 API 进行 HTML 覆盖攻击以及在设备上执行点击和手势。

意大利网络安全公司发现的恶意 dropper 应用程序伪装成 Google Chrome 网络浏览器，安装后启动后，会敦促受害者通过单击“确认”按钮更新 Google Play 服务。

如果用户继续更新，则会以“Google 服务”为幌子将包含 TrickMo 有效负载的 APK 文件下载到设备，然后要求用户为新应用程序启用辅助功能服务。

“无障碍服务旨在通过提供与设备交互的替代方式来帮助残障用户，”研究人员说。“但是，当被 TrickMo 等恶意应用程序利用时，这些服务可以授予对设备的广泛控制权。”

“这种提升的权限允许 TrickMo 执行各种恶意操作，例如拦截 SMS 消息、处理通知以拦截或隐藏身份验证代码，以及执行 HTML 覆盖攻击以窃取用户凭据。此外，该恶意软件可以关闭键盘锁并自动接受权限，使其能够无缝集成到设备的操作中。

此外，滥用辅助功能服务允许恶意软件禁用关键的安全功能和系统更新，随意自动授予权限，并阻止卸载某些应用程序。![TrickMo Android 木马]( "TrickMo Android Trojan")

Cleafy 的分析还发现了命令和控制 （C2） 服务器中的错误配置，这使得访问从设备中泄露的 12 GB 敏感数据（包括凭据和图片）成为可能，而无需任何身份验证。

C2 服务器还托管覆盖攻击中使用的 HTML 文件。这些文件包含各种服务的虚假登录页面，包括 ATB Mobile 和 Alpha Bank 等银行以及 Binance 等加密货币平台。

安全漏洞不仅凸显了威胁行为者的运营安全 （OPSEC） 错误，而且还使受害者的数据面临被其他威胁行为者利用的风险。

TrickMo 的 C2 基础设施暴露的大量信息可用于身份盗窃、渗透各种在线账户、进行未经授权的资金转移，甚至进行欺诈性购买。更糟糕的是，攻击者可能会劫持帐户并通过重置密码将受害者锁定在外面。

研究人员指出：“使用个人信息和图像，攻击者可以制作令人信服的消息，诱骗受害者泄露更多信息或执行恶意操作。

“利用如此全面的个人数据会导致直接的经济和声誉损失，并给受害者带来长期后果，使恢复成为一个复杂而漫长的过程。”

此次披露之际，谷歌一直在填补旁加载的安全漏洞，让第三方开发者确定他们的应用程序是否使用 Play Integrity API 进行旁加载，如果是，则要求用户从 Google Play 下载应用程序才能继续使用它们。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300107](/post/id/300107)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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