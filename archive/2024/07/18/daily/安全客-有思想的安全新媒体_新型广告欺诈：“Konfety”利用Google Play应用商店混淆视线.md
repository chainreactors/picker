---
title: 新型广告欺诈：“Konfety”利用Google Play应用商店混淆视线
url: https://www.anquanke.com/post/id/298009
source: 安全客-有思想的安全新媒体
date: 2024-07-18
fetch_date: 2025-10-06T17:38:32.984514
---

# 新型广告欺诈：“Konfety”利用Google Play应用商店混淆视线

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

# 新型广告欺诈：“Konfety”利用Google Play应用商店混淆视线

阅读量**69326**

发布时间 : 2024-07-17 14:17:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html>

译文仅供参考，具体内容表达以及含义原文为准。

有关“大规模广告欺诈行动”的细节已经浮出水面，该行动利用 Google Play 商店中的数百个应用程序来执行一系列邪恶活动。

该活动的代号为**Konfety**（俄语中糖果的意思），因为它滥用了与俄罗斯广告网络CaramelAds相关的移动广告软件开发工具包（SDK）。

“Konfety代表了一种新形式的欺诈和混淆，其中威胁行为者在主要市场上操作’诱饵双胞胎’应用程序的’邪恶双胞胎’版本，”HUMAN的Satori威胁情报团队在与The Hacker News分享的一份技术报告中说。

虽然这些诱饵应用程序的数量超过 250 个，是无害的，并通过 Google Play 商店分发，但它们各自的“邪恶双胞胎”通过恶意广告活动传播，旨在促进广告欺诈、监控网络搜索、安装浏览器扩展程序以及将 APK 文件代码旁加载到用户的设备上。

该活动最不寻常的方面是，邪恶的双胞胎伪装成诱饵双胞胎，欺骗后者的应用程序 ID 和广告发布商 ID 来呈现广告。诱饵和邪恶的双胞胎应用程序都在同一基础架构上运行，允许威胁参与者根据需要呈指数级扩展其操作。

话虽如此，诱饵应用程序不仅表现正常，而且大多数甚至不呈现广告。它们还包含 GDPR 同意通知。

“这种’诱饵/邪恶双胞胎’混淆机制是威胁行为者将欺诈性流量表示为合法的一种新方法，”HUMAN研究人员说。“在巅峰时期，与 Konfety 相关的程序化处理量达到每天 100 亿个请求。”

换句话说，Konfety 利用 SDK 的广告渲染功能来实施广告欺诈，使区分恶意流量和合法流量更具挑战性。

据说 Konfety 邪恶的双胞胎应用程序是通过推广 APK 模组和其他软件（如 Letasoft Sound Booster）的恶意广告活动传播的，诱杀 URL 托管在攻击者控制的域、受感染的 WordPress 网站和其他允许内容上传的平台，包括 Docker Hub、Facebook、Google Sites 和 OpenSea。

[![]()](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ZnK1du4eDdAprFQWWWac8Fw8arGOfHM4tNm9Cm8LU6ly_eYiwdniCAQ-slx6is6QBtKTIZHiF0lm6-iNBREPVUMNhKrBINRmnFwgzRaXhJdE3qpz0SCyGUgSIgHbD1qIMPhMllcqun5WEusuO5d9bdnUP5kx5WOl_MilJ2GHjg7dPWaVhnFC-a-6nl4q/s728-rw-e365/apps.png)

最终点击这些 URL 的用户将被重定向到一个域，该域诱骗他们下载恶意的邪恶孪生应用程序，该应用程序反过来充当第一阶段的滴管，该阶段从 APK 文件的资产中解密，用于设置命令和控制 （C2） 通信。

初始阶段程序进一步尝试在设备的主屏幕上隐藏应用程序的图标，并运行第二阶段 DEX 有效负载，当用户在其主屏幕上或使用其他应用程序时，通过提供断章取义的全屏视频广告来执行欺诈。

“Konfety行动的关键在于邪恶的双胞胎应用程序，”研究人员说。“这些应用程序通过从诱饵孪生应用程序复制其应用程序 ID/包名称和发布者 ID 来模仿其相应的诱饵孪生应用程序。”

“从邪恶孪生应用程序派生的网络流量在功能上与从诱饵孪生应用程序派生的网络流量相同;Evil Twins 提供的广告展示在请求中使用了诱饵 Twins 的软件包名称。

该恶意软件的其他功能包括将 CaramelAds SDK 武器化以使用默认 Web 浏览器访问网站，通过发送通知提示用户点击虚假链接来引诱用户，或旁加载其他广告 SDK 的修改版本。

这还不是全部。我们敦促安装 Evil Twins 应用程序的用户在设备主屏幕上添加一个搜索工具栏小部件，该小部件通过将数据发送到名为 vptrackme[.] 的域来暗中监控他们的搜索。com 和 youaresearching[.]com。

研究人员总结说：“威胁行为者明白，在商店中托管恶意应用程序不是一种稳定的技术，并且正在寻找创造性和聪明的方法来逃避检测并实施可持续的长期欺诈。“建立中介 SDK 公司并传播 SDK 以滥用高质量出版商的行为者是一种日益增长的技术。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298009](/post/id/298009)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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