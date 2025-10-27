---
title: 在Play商店中流行的相机和浏览器应用程序中发现Necro安卓恶意软件
url: https://www.anquanke.com/post/id/300403
source: 安全客-有思想的安全新媒体
date: 2024-09-26
fetch_date: 2025-10-06T18:23:38.580360
---

# 在Play商店中流行的相机和浏览器应用程序中发现Necro安卓恶意软件

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

# 在Play商店中流行的相机和浏览器应用程序中发现Necro安卓恶意软件

阅读量**93515**

发布时间 : 2024-09-25 14:17:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/necro-android-malware-found-in-popular.html>

译文仅供参考，具体内容表达以及含义原文为准。

与 Spotify、WhatsApp 和 Minecraft 相关的合法 Android 应用程序的更改版本已被用于提供名为 Necro 的已知恶意软件加载程序的新版本。

卡巴斯基表示，在 Google Play 商店中也发现了一些恶意应用程序。它们已累计下载了 1100 万次。他们包括 –

* Wuta Camera – Nice Shot Always （com.benqu.wuta） – 10+ 百万下载量
* Max Browser-Private & Security （com.max.browser） – 1+ 百万下载量

在撰写本文时，Max Browser 不再可从 Play 商店下载。另一方面，Wuta Camera 已更新（版本 6.3.7.138）以删除恶意软件。该应用程序的最新版本 6.3.8.148 于 2024 年 9 月 8 日发布。

目前尚不清楚这两款应用程序最初是如何被恶意软件入侵的，尽管据信用于集成广告功能的流氓软件开发工具包 （SDK） 是罪魁祸首。

Necro（不要与同名僵尸网络混淆）于 2019 年首次由俄罗斯网络安全公司发现，当时它隐藏在名为 CamScanner 的流行文档扫描应用程序中。

CamScanner 后来将问题归咎于名为 AdHub 的第三方提供的广告 SDK，它表示该 SDK 包含一个恶意模块，用于从远程服务器检索下一阶段的恶意软件，本质上充当将各种恶意软件加载到受害者设备上的加载程序。

新版本的恶意软件也不例外，尽管它包含混淆技术来逃避检测，特别是利用隐写术来隐藏有效载荷。

“除其他外，下载的有效载荷可以在不可见的窗口中显示广告并与之交互，下载和执行任意 DEX 文件，安装它下载的应用程序，”卡巴斯基研究员 Dmitry Kalinin 说。

它还可以 “在不可见的 WebView 窗口中打开任意链接并在其中执行任何 JavaScript 代码，在受害者的设备中运行隧道，并可能订阅付费服务。

Necro 的主要交付工具之一是托管在非官方网站和应用商店中的流行应用程序和游戏的修改版本。下载后，应用程序会初始化一个名为 Coral SDK 的模块，该模块反过来会向远程服务器发送 HTTP POST 请求。

服务器随后以一个链接作为响应，该链接指向托管在 adoss.spinsok 上的据称的 PNG 图像文件[.]com，然后 SDK 继续从中提取主要有效负载 – Base64 编码的 Java 存档 （JAR） 文件。

Necro 的恶意功能是通过从命令和控制 （C2） 服务器下载的一组附加模块（又名插件）实现的，使其能够在受感染的 Android 设备上执行各种操作 –

* NProxy – 创建穿过受害者设备的隧道
* island – 生成一个伪随机数，用作侵入性广告显示之间的时间间隔（以毫秒为单位）
* web – 定期联系 C2 服务器，并在加载特定链接时以提升的权限执行任意代码
* Cube SDK – 一个帮助程序模块，用于加载其他插件以在后台处理广告
* 点按 – 从 C2 服务器下载任意 JavaScript 代码和 WebView 界面，这些代码和界面负责秘密加载和查看广告
* Happy SDK/Jar SDK – 一个结合了 NProxy 和 web 模块的模块，有一些细微的差异

Happy SDK 的发现增加了该活动背后的威胁行为者也在试验非模块化版本的可能性。

“这表明 Necro 具有很强的适应性，可以下载自己的不同迭代，也许是为了引入新功能，”Kalinin 说。

卡巴斯基收集的遥测数据显示，它在 2024 年 8 月 26 日至 9 月 15 日期间在全球范围内阻止了超过 10000 次 Necro 攻击，其中俄罗斯、巴西、越南、厄瓜多尔、墨西哥、台湾、西班牙、马来西亚、意大利和土耳其的攻击数量最多。

“这个新版本是一个多阶段加载程序，它使用隐写术来隐藏第二阶段有效载荷，这是一种非常罕见的移动恶意软件技术，以及用于逃避检测的混淆，”Kalinin 说。

“模块化架构为木马的创建者提供了广泛的选择，可以根据受感染的应用程序进行大规模和有针对性的加载程序更新或新的恶意模块。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/necro-android-malware-found-in-popular.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300403](/post/id/300403)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/necro-android-malware-found-in-popular.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/necro-android-malware-found-in-popular.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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