---
title: 新型安卓恶意软件 NGate 窃取 NFC 数据克隆非接触式支付卡
url: https://www.anquanke.com/post/id/299508
source: 安全客-有思想的安全新媒体
date: 2024-08-28
fetch_date: 2025-10-06T18:03:45.157191
---

# 新型安卓恶意软件 NGate 窃取 NFC 数据克隆非接触式支付卡

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

# 新型安卓恶意软件 NGate 窃取 NFC 数据克隆非接触式支付卡

阅读量**56387**

发布时间 : 2024-08-27 11:05:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-android-malware-ngate-steals-nfc.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了新的 Android 恶意软件，该恶意软件可以将受害者的非接触式支付数据从实体信用卡和借记卡中继到攻击者控制的设备，目的是进行欺诈操作。

这家斯洛伐克网络安全公司正在以 NGate 的身份跟踪这种新型恶意软件，并表示它观察到针对捷克三家银行的犯罪软件活动。

研究人员 Lukáš Štefanko 和 Jakub Osmani 在一项分析中表示，该恶意软件“具有独特的能力，可以通过安装在受害者 Android 设备上的恶意应用程序将数据从受害者的支付卡中继到攻击者的 root Android 手机”。

该活动是自 2023 年 11 月以来发现使用恶意渐进式 Web 应用程序 （PWA） 和 WebAPK 针对捷克金融机构的更广泛活动的一部分。NGate 的首次使用记录是在 2024 年 3 月。

攻击的最终目标是使用 NGate 从受害者的物理支付卡中克隆近场通信 （NFC） 数据，并将信息传输到攻击者设备，然后该设备模拟原始卡从 ATM 取款。

NGate 源于一个名为 NFCGate 的合法工具，该工具最初由达姆施塔特工业大学安全移动网络实验室的学生于 2015 年开发，用于安全研究目的。

据信，这些攻击链涉及社会工程和 SMS 网络钓鱼的结合，通过将用户引导至冒充合法银行网站或 Google Play 商店中可用的官方移动银行应用程序的短期域来诱骗用户安装 NGate。

迄今为止，在 2023 年 11 月至 2024 年 3 月期间，已确定了多达 6 个不同的 NGate 应用程序，当时这些活动可能是在捷克当局逮捕了一名 22 岁的男子后停止的，他涉嫌从 ATM 机上窃取资金。

NGate 除了滥用 NFCGate 的功能来捕获 NFC 流量并将其传递给另一台设备外，还提示用户输入敏感的财务信息，包括银行客户 ID、出生日期和银行卡的 PIN 码。网络钓鱼页面显示在 WebView 中。

“它还要求他们打开智能手机上的 NFC 功能，”研究人员说。“然后，受害者被指示将他们的支付卡放在智能手机的背面，直到恶意应用程序识别出该卡。”

这些攻击进一步采用了一种阴险的方法，受害者在通过 SMS 消息发送的链接安装 PWA 或 WebAPK 应用程序后，他们的凭据被网络钓鱼，随后接到威胁行为者的电话，威胁行为者假装是银行员工，并通知他们他们的银行账户因安装该应用程序而被盗用。

随后，他们被指示更改他们的 PIN 码并使用不同的移动应用程序（即 NGate）验证他们的银行卡，该应用程序的安装链接也通过短信发送。没有证据表明这些应用程序是通过 Google Play 商店分发的。

“NGate 使用两个不同的服务器来促进其操作，”研究人员解释说。“第一个是网络钓鱼网站，旨在引诱受害者提供敏感信息并能够发起 NFC 中继攻击。第二个是 NFCGate 中继服务器，其任务是将 NFC 流量从受害者的设备重定向到攻击者的设备。

在披露这一消息的同时，Zscaler ThreatLabz 详细介绍了一种名为 Copybara 的已知 Android 银行木马的新变体，该木马通过语音网络钓鱼（电话钓鱼）攻击传播并引诱他们输入他们的银行账户凭据。

“Copybara 的这种新变体自 2023 年 11 月以来一直活跃，并利用 MQTT 协议与其命令和控制 （C2） 服务器建立通信，”Ruchna Nigam 说。

“该恶意软件滥用 Android 设备原生的辅助功能服务功能，对受感染的设备进行精细控制。在后台，该恶意软件还继续下载网络钓鱼页面，这些页面使用其徽标和应用程序名称模仿流行的加密货币交易所和金融机构。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-android-malware-ngate-steals-nfc.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299508](/post/id/299508)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-android-malware-ngate-steals-nfc.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-android-malware-ngate-steals-nfc.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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