---
title: 针对 Android 和 iPhone 用户的新网络钓鱼方法
url: https://www.anquanke.com/post/id/299341
source: 安全客-有思想的安全新媒体
date: 2024-08-22
fetch_date: 2025-10-06T18:01:20.594980
---

# 针对 Android 和 iPhone 用户的新网络钓鱼方法

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

# 针对 Android 和 iPhone 用户的新网络钓鱼方法

阅读量**36700**

发布时间 : 2024-08-21 14:16:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Help Net Security，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/08/20/android-iphone-phishing-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

ESET研究人员发现了一种针对Android和iPhone用户的罕见网络钓鱼活动。他们分析了一个在野外观察到的案例，该案例针对一家著名的捷克银行的客户。

![Android iPhone phishing]( "Flow")

PWA 网络钓鱼流 （来源：ESET）

这种技术值得注意，因为它从第三方网站安装网络钓鱼应用程序，而用户不必允许安装第三方应用程序。在 Android 上，这可能会导致静默安装一种特殊类型的 APK，该 APK 甚至似乎是从 Google Play 商店安装的。该威胁也针对 iOS 用户。

针对 iOS 的网络钓鱼网站指示受害者将渐进式 Web 应用程序 （PWA） 添加到他们的主屏幕，而在 Android 上，PWA 是在确认浏览器中的自定义弹出窗口后安装的。在这一点上，这些网络钓鱼应用程序与它们在两种操作系统上模仿的真实银行应用程序基本上没有区别。

PWA 本质上是捆绑到感觉像独立应用程序中的网站，通过使用本机系统提示来增强这种感觉。PWA 与网站一样，是跨平台的，这解释了这些 PWA 网络钓鱼活动如何针对 iOS 和 Android 用户。在捷克，ESET分析师在ESET Brand Intelligence Service上观察到了这种新技术，该服务监控针对客户品牌的威胁。

“对于iPhone用户来说，这样的行动可能会打破任何关于安全性的’围墙花园’假设，”ESET研究员Jakub Osmani说，他分析了这一威胁。

### ESET 发现使用电话、短信和恶意广告的网络钓鱼诈骗

ESET分析师发现了一系列针对移动用户的网络钓鱼活动，这些活动使用了三种不同的URL传递机制。这些机制包括自动语音通话、短信和社交媒体恶意广告。语音呼叫传递是通过自动呼叫完成的，该呼叫会警告用户有关过时的银行应用程序，并要求用户在数字键盘上选择一个选项。

按下正确的按钮后，将通过短信发送网络钓鱼 URL，正如推文中所报道的那样。最初的短信传递是通过不分青红皂白地向捷克电话号码发送消息来执行的。发送的消息包括一个网络钓鱼链接和文本，以社会工程受害者访问该链接。该恶意活动是通过 Instagram 和 Facebook 等 Meta 平台上的注册广告传播的。这些广告包含号召性用语，例如为“在下面下载更新”的用户提供有限的优惠。

打开第一阶段提供的 URL 后，Android 受害者会看到两个不同的活动，要么是模仿目标银行应用程序的官方 Google Play 商店页面的高质量网络钓鱼页面，要么是该应用程序的山寨网站。从这里，受害者被要求安装银行应用程序的“新版本”。

### WebAPK 绕过安全警告

网络钓鱼活动和方法之所以成为可能，是因为采用了渐进式 Web 应用程序的技术。简而言之，PWA 是使用传统 Web 应用程序技术构建的应用程序，可以在多个平台和设备上运行。

WebAPK 可以被视为渐进式 Web 应用程序的升级版本，因为 Chrome 浏览器从 PWA 生成原生 Android 应用程序：换句话说，是一个 APK。这些 WebAPK 看起来像常规的原生应用程序。此外，安装 WebAPK 不会产生任何“从不受信任的来源安装”警告。如果不允许从第三方来源安装，则甚至会安装该应用程序。

一个小组使用Telegram机器人通过官方Telegram API将所有输入的信息记录到Telegram群聊中，而另一个小组则使用带有管理面板的传统命令与控制（C&C）服务器。Osmani总结说：“基于这些活动使用了两种不同的C&C基础设施这一事实，我们已经确定有两个独立的团体正在针对几家银行进行PWA / WebAPK网络钓鱼活动。大多数已知案例都发生在捷克，只有两个网络钓鱼应用程序出现在该国以外的地方（特别是在匈牙利和格鲁吉亚）。

ESET研究发现的有关此事的所有敏感信息均已立即发送给受影响的银行进行处理。ESET还协助关闭了多个网络钓鱼域和C&C服务器。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/08/20/android-iphone-phishing-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299341](/post/id/299341)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/08/20/android-iphone-phishing-campaign/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/08/20/android-iphone-phishing-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

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