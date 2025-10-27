---
title: 新的Android木马“BlankBot”针对土耳其用户的财务数据
url: https://www.anquanke.com/post/id/298829
source: 安全客-有思想的安全新媒体
date: 2024-08-07
fetch_date: 2025-10-06T18:02:16.199140
---

# 新的Android木马“BlankBot”针对土耳其用户的财务数据

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

# 新的Android木马“BlankBot”针对土耳其用户的财务数据

阅读量**59364**

发布时间 : 2024-08-06 11:33:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种名为 BlankBot 的新 Android 银行木马，该木马针对土耳其用户，旨在窃取财务信息。

Intel 471在上周发表的一份分析报告中表示：“BlankBot具有一系列恶意功能，包括客户注入，键盘记录，屏幕录制，并通过WebSocket连接与控制服务器进行通信。

据说 BlankBot 于 2024 年 7 月 24 日被发现，正在积极开发中，该恶意软件滥用 Android 的辅助功能服务权限来完全控制受感染的设备。

下面列出了一些包含 BlankBot 的恶意 APK 文件的名称 –

* app-release.apk （com.abcdefg.w568b）
* app-release.apk （com.abcdef.w568b）
* 应用程序发布签名 （14）.apk （com.whatsapp.chma14）
* app.apk （com.whatsapp.chma14p）
* app.apk （com.whatsapp.w568bp）
* showcuu.apk （com.whatsapp.w568b）

与最近重新出现的 Mandrake Android 木马一样，BlankBot 实现了一个基于会话的包安装程序，以规避 Android 13 中引入的限制设置功能，以阻止侧载应用程序直接请求危险权限。

“该机器人要求受害者允许安装来自第三方来源的应用程序，然后它检索存储在应用程序资产目录中的 Android 包套件 （APK） 文件，没有加密，并继续包安装过程，”Intel 471 说。

该恶意软件具有广泛的功能，可以根据从远程服务器收到的特定命令执行屏幕录制、键盘记录和注入覆盖，以收集银行账户凭据、支付数据，甚至用于解锁设备的模式。

BlankBot 还能够拦截 SMS 消息、卸载任意应用程序以及收集联系人列表和已安装应用程序等数据。它还利用辅助功能服务 API 来阻止用户访问设备设置或启动防病毒应用程序。

“BlankBot 是一种新的 Android 银行木马，仍在开发中，在不同应用程序中观察到的多种代码变体证明了这一点，”这家网络安全公司表示。“无论如何，一旦恶意软件感染了Android设备，它就可以执行恶意操作。”

谷歌发言人告诉The Hacker News，该公司尚未在Google Play商店中找到任何包含该恶意软件的应用程序。

这家科技巨头表示：“Google Play Protect会自动保护Android用户免受此恶意软件的已知版本的侵害，该保护在具有Google Play服务的Android设备上默认处于开启状态。“Google Play Protect 会警告用户并阻止包含此恶意软件的应用，即使这些应用来自 Play 以外的来源。”

谷歌概述了它正在采取的各种措施，以打击威胁行为者使用黄貂鱼等蜂窝站点模拟器将短信直接注入Android手机，这种欺诈技术被称为SMS Blaster欺诈。

“这种注入消息的方法完全绕过了运营商网络，从而绕过了所有复杂的基于网络的反垃圾邮件和反欺诈过滤器，”谷歌说。“SMS Blasters 暴露了一个虚假的 LTE 或 5G 网络，该网络执行单一功能：将用户的连接降级到传统的 2G 协议。”

缓解措施包括用户选项，可以在调制解调器级别禁用 2G 并关闭零密码，后者是虚假基站的基本配置，以便注入 SMS 有效载荷。

今年5月初，谷歌还表示，如果它的蜂窝网络连接未加密，以及犯罪分子是否使用蜂窝站点模拟器窥探用户或向他们发送基于短信的欺诈信息，它正在加强蜂窝网络安全。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298829](/post/id/298829)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-android-trojan-blankbot-targets.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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