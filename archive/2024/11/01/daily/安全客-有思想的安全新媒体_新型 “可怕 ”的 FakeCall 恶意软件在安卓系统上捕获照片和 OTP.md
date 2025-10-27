---
title: 新型 “可怕 ”的 FakeCall 恶意软件在安卓系统上捕获照片和 OTP
url: https://www.anquanke.com/post/id/301444
source: 安全客-有思想的安全新媒体
date: 2024-11-01
fetch_date: 2025-10-06T19:15:11.471594
---

# 新型 “可怕 ”的 FakeCall 恶意软件在安卓系统上捕获照片和 OTP

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

# 新型 “可怕 ”的 FakeCall 恶意软件在安卓系统上捕获照片和 OTP

阅读量**88864**

发布时间 : 2024-10-31 11:14:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/scary-fakecall-malware-captures-photos-otps-android/>

译文仅供参考，具体内容表达以及含义原文为准。

**一种新的、更复杂的 FakeCall 恶意软件变种正瞄准安卓设备。了解使该恶意软件成为严重威胁的高级功能，包括屏幕捕获和远程控制功能。**

Zimperium’s zLabs 的网络安全研究人员发现了 FakeCall 恶意软件的一个 “可怕 ”的新变种。这种恶意软件会诱骗受害者拨打诈骗电话号码，导致身份被盗和经济损失。FakeCall 是一种网络钓鱼（语音钓鱼）恶意软件，一旦安装，几乎可以完全控制目标安卓手机。

最新变种展示了几项新功能，包括识别、压缩和上传图像缩略图，选择性上传特定图像，远程控制屏幕，模拟用户操作，捕获和传输实时视频，以及远程解锁设备。这些功能可以捕获敏感文件或个人照片。

FakeCall 恶意软件通常通过从受威胁网站下载的恶意应用程序或网络钓鱼电子邮件渗透到设备中。该应用程序会请求成为默认呼叫处理程序的权限。如果获得许可，恶意软件就会获得大量权限。

![New "Scary" FakeCall Malware Captures Photos and OTPs on Android]()
攻击流程（Zimperium）

根据 Zimperium 在周三发布之前与 Hackread.com 分享的博文，攻击者在攻击中使用了一种名为 “电话监听器服务 ”的服务。事实上，这项服务是恶意软件的关键组成部分，使其能够操纵设备的通话功能，从而拦截和控制所有来电和去电，并攫取敏感信息，如一次性密码（OTP）或账户验证码。

此外，恶意软件还能操纵设备显示屏，显示虚假的通话界面，诱骗受害者提供敏感信息。它还可以操纵通话记录来隐藏其恶意活动并控制通话时间。攻击者可以利用这些功能欺骗受害者泄露敏感信息或转移资金。

![New "Scary" FakeCall Malware Captures Photos and OTPs on Android]()
假电话界面截图（Zimperium）

该恶意软件还利用安卓辅助功能服务捕获屏幕内容并操纵设备显示屏，在模仿合法手机应用程序的同时创建欺骗性用户界面。攻击者可以利用这种伎俩窃取敏感信息、进行监视和远程控制设备。

它可以监控来自股票拨号器应用程序的事件，并检测来自系统权限管理器和系统用户界面的权限提示。检测到特定事件后，它可以绕过用户同意，为恶意软件授予权限。恶意软件允许远程攻击者控制受害者的设备用户界面，使他们能够模拟用户交互并精确操纵设备。

另一方面，好消息是谷歌已经对受 Scary 恶意软件仿冒影响的应用程序进行了调查。谷歌告知 Hackread.com，Google Play 上的所有应用程序都受到了保护，不会受到新变种的影响。

**“根据我们目前的检测结果，Google Play 上没有发现包含这种恶意软件的应用程序。安卓用户会自动受到 Google Play Protect 的保护，以防已知版本的恶意软件，该保护在使用 Google Play 服务的安卓设备上默认开启。Google Play Protect 可以警告用户或阻止已知存在恶意行为的应用程序，即使这些应用程序来自 Play 之外。”**

谷歌发言人

为防范此类恶意软件，请务必从 Google Play 商店等可信来源下载应用程序，谨慎对待权限请求，并使用具有设备检测功能的移动安全软件。

本文翻译自hackread [原文链接](https://hackread.com/scary-fakecall-malware-captures-photos-otps-android/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301444](/post/id/301444)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/scary-fakecall-malware-captures-photos-otps-android/)

如若转载,请注明出处： <https://hackread.com/scary-fakecall-malware-captures-photos-otps-android/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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