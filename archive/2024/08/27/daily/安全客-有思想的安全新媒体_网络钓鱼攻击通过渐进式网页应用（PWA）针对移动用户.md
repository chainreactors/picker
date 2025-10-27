---
title: 网络钓鱼攻击通过渐进式网页应用（PWA）针对移动用户
url: https://www.anquanke.com/post/id/299484
source: 安全客-有思想的安全新媒体
date: 2024-08-27
fetch_date: 2025-10-06T18:00:46.775372
---

# 网络钓鱼攻击通过渐进式网页应用（PWA）针对移动用户

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

# 网络钓鱼攻击通过渐进式网页应用（PWA）针对移动用户

阅读量**40918**

发布时间 : 2024-08-26 14:26:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

译文仅供参考，具体内容表达以及含义原文为准。

## 网络犯罪分子使用渐进式 Web 应用程序 （PWA） 来冒充银行应用程序并窃取移动用户的凭据。

ESET 研究人员详细介绍了针对使用渐进式 Web 应用程序 （PWA） 的移动用户的网络钓鱼活动。威胁行为者使用的虚假应用程序与 iOS 和 Android 上的真实银行应用程序几乎没有区别。该技术于 2023 年 7 月在波兰首次披露，随后在捷克以及匈牙利和格鲁吉亚等其他国家观察到。

该活动使用渐进式 Web 应用程序来冒充银行应用程序并窃取 Android 和 iOS 用户的凭据。

渐进式 Web 应用程序 （PWA） 是使用 Web 平台技术构建的应用程序，但提供类似于特定于平台的应用程序的用户体验。

该技术允许从第三方网站安装网络钓鱼应用程序，而无需用户启用第三方应用程序安装。对于 iOS 用户来说，这破坏了 “walled garden” 方法的通常安全假设。在 Android 上，它可能导致看似来自 Google Play 商店的 APK 的静默安装，从而进一步欺骗用户。

针对 iOS 的网络钓鱼网站会指示受害者将渐进式 Web 应用程序 （PWA） 添加到他们的主屏幕，而在 Android 上，PWA 是在确认浏览器中的自定义弹出窗口后安装的。该技术于 2023 年 7 月在波兰首次披露，随后由 ESET 研究人员在捷克观察到，其他病例针对匈牙利和格鲁吉亚的银行。

*“阴险地，安装 PWA/WebAPK 应用程序并不会警告受害者安装第三方应用程序。在 Android 上，这些网络钓鱼 WebAPK 甚至似乎是从 Google Play 商店安装的。“ESET 发布的**报告**写道。“观察到的大多数应用程序都针对捷克银行的客户，但我们也观察到一个针对匈牙利银行的网络钓鱼应用程序，另一个针对格鲁吉亚银行的网络钓鱼应用程序。”*

对这些攻击中使用的 C2 服务器和后端基础设施的分析表明，两个不同的威胁行为者正在运营这些活动。

ESET 发现的网络钓鱼活动通过三种不同的 URL 交付方式针对移动用户：自动语音通话、SMS 消息和社交媒体恶意广告。自动呼叫会警告用户过时的银行应用程序，并在用户按照提示发送后通过短信发送网络钓鱼 URL。SMS 活动不分青红皂白地将网络钓鱼链接发送到捷克电话号码。社交媒体恶意广告涉及 Instagram 和 Facebook 等平台上的广告，针对特定人群发出号召性用语。点击这些 URL 后，受害者被重定向到模仿官方应用商店的网络钓鱼页面，例如 Google Play 或 Apple Store。

![progressive web applications (PWA)]()

攻击者试图诱骗受害者安装其银行应用程序的虚假“新版本”。根据活动的不同，单击安装/更新按钮会直接在受害者的手机上触发恶意应用程序的安装。

对于 Android 用户，这可以是 WebAPK，而对于 iOS 和 Android 用户，它可能是渐进式 Web 应用程序 （PWA）。安装过程不会触发有关未知应用程序的浏览器警告，从而利用 Chrome 的 WebAPK 技术。iOS 用户会看到一个弹出窗口，模拟本机提示，将网络钓鱼 PWA 添加到其主屏幕，没有任何警告。安装应用程序后，受害者被要求输入他们的银行凭证，然后将这些凭证发送到 C2 服务器。

专家注意到，这些活动使用了两个不同的 C2 基础设施，这表明两个 dinstict 组织正在针对捷克和其他银行开展 PWA/WebAPK 网络钓鱼活动。

一个组使用 Telegram 机器人通过官方 API 将输入的信息记录到 Telegram 群聊中，而另一个组则使用带有管理面板的传统 C2 服务器，该面板与 NGate Android 恶意软件活动相关联。

*“我们发现了一种新的网络钓鱼方法，将成熟的社会工程方法与 PWA 应用程序的跨平台技术相结合。还发现了针对 Android 用户的案例，特别是通过目标应用的 Google Play 商店页面的山寨页面并使用 WebAPK 技术。大多数已知案例都在捷克境内，只有两个网络钓鱼应用程序出现在该地区之外（匈牙利和格鲁吉亚）。“ESET 发布的报告总结道。“我们预计会创建和分发更多的山寨应用程序，因为安装后很难将合法应用程序与网络钓鱼应用程序区分开来。”*

本文翻译自securityaffairs 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299484](/post/id/299484)

安全KER - 有思想的安全新媒体

本文转载自: securityaffairs

如若转载,请注明出处：

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

* [网络犯罪分子使用渐进式 Web 应用程序 （PWA） 来冒充银行应用程序并窃取移动用户的凭据。](#h2-0)

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