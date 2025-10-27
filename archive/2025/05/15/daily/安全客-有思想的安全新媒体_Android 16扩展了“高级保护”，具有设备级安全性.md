---
title: Android 16扩展了“高级保护”，具有设备级安全性
url: https://www.anquanke.com/post/id/307379
source: 安全客-有思想的安全新媒体
date: 2025-05-15
fetch_date: 2025-10-06T22:23:19.373531
---

# Android 16扩展了“高级保护”，具有设备级安全性

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

# Android 16扩展了“高级保护”，具有设备级安全性

阅读量**86412**

发布时间 : 2025-05-14 15:40:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/android-16-expands-advanced-protection-with-device-level-security/>

译文仅供参考，具体内容表达以及含义原文为准。

![Android 16 通过设备级安全性增强了“高级保护”]()

Google 宣布对 Android 16 中的高级保护功能进行改进，以加强对复杂间谍软件攻击的防御。

Android 平台一直是间谍软件活动和利用数字取证平台进行复杂攻击的目标，这些平台通常依靠零日漏洞来感染设备，用户交互最少或根本没有用户交互。

Google 已经为高风险个人（例如记者、民选官员、公众人物）提供了“高级保护计划”，但其目前的重点是保护 Google 帐户。

在 Android 16 中，该公司将安全强化扩展到移动设备本身，超越了某些应用程序级别的设置。

这个设备级安全层捆绑了 Android 最强大的系统级安全功能，并防止恶意或意外地禁用高级保护伞中的单个安全功能。

Google 在 Android 上的高级保护类似于 Apple 的锁定模式，并将在今天作为 Google 的“The Android Show： I/O Edition”的一部分展示的最新版本的移动作系统上提供。

## 高级保护计划的运作方式

高级保护功能是一种易于激活的设备级设置，它将 Android 最强大的安全功能整合到一个系统中。

![高级保护设置]()

**高级保护设置**
*来源：Google*

具体来说，它激活验证启动和运行时完整性检查、强沙盒、USB 端口锁定、应用程序隔离、空闲 72 小时时自动重启设备，以及具有增强应用程序扫描的 Google Play 保护。

它还消除了关闭或削弱核心安全设置的能力，并在 Google 应用程序（Chrome、消息、电话）以及选择加入集成的第三方应用程序中强制执行安全设置。

最后，它引入了新的保护措施，例如入侵日志记录和阻止自动重新连接到不安全的网络。

入侵日志记录是一种新系统，它将设备事件记录在保护隐私、防篡改、云存储的日志中，这对于调查泄露非常有用。数据将仅可由用户访问，并受端到端加密保护。

自动重新连接阻止涉及不需要密码或使用 WEP 保护的弱 Wi-Fi 网络，从而降低被动监控或捕获门户攻击的风险。

下表列出了通过 Advanced Protection 控制的所有安全功能。需要注意的是，其中一些的可用性取决于制造商和设备类型，并将在今年晚些时候推出。

![高级保护中包含的所有功能概述]()

**高级保护**
中包含的所有功能概述 *来源：Google*

## Android 16 的更多安全功能

除了高级保护之外，Android 16 还将通过一组新功能带来多项数据安全和隐私增强功能，以保护用户免受电话诈骗者和恶意软件应用程序的侵害。

其中之一是“通话中诈骗保护”，它将阻止来自未知号码的通话期间的危险作，例如旁加载 APK、授予辅助功能权限或禁用 Play Protect。

![通话中诈骗保护的实际应用]()

**通话中诈骗保护行动**
*来源：Google*

Google 今天强调的另一个功能是 Messages 应用程序中的 Key Verifier 机制。此改进旨在通过使用与联系人关联的公共加密密钥验证另一方的身份来打击基于 tex 的欺诈和冒充。

公钥加密在 Google Messages 中的作用是提供端到端加密消息传递。

“通过验证 Google 通讯录应用程序中的联系人密钥（通过二维码扫描或数字比对），您可以获得额外的保证，即另一端的人是真实的，并且您与他们之间的对话是私密的，”谷歌说。

密钥验证程序功能还可以防止 SIM 卡交换攻击，攻击者冒充受害者联系人中的某人。

![Key Verifier 的 QR 码提示]()

**Key Verifier 的二维码提示**
*来源：Google*

Android 16 还通过集成人工智能来识别与各种主题相关的诈骗，其中包括收费公路、账单费用、加密、金融冒充、礼品卡和奖品以及技术支持，从而改进了消息和电话应用程序的诈骗检测。

谷歌还通过将 Find My Device 变成 Find Hub 来改进防盗保护功能，该功能还可以涵盖丢失的物品，并与蓝牙标签和多家航空公司的合作一起使用。

该公司宣布，今年晚些时候，Find Hub 将集成卫星连接，即使在没有蜂窝信号的地方，也能与朋友和家人建立联系。

谷歌今天宣布的 Android 16 新功能可在此处获得。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/android-16-expands-advanced-protection-with-device-level-security/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307379](/post/id/307379)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/android-16-expands-advanced-protection-with-device-level-security/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/android-16-expands-advanced-protection-with-device-level-security/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [高级保护计划的运作方式](#h2-0)
* [Android 16 的更多安全功能](#h2-1)

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