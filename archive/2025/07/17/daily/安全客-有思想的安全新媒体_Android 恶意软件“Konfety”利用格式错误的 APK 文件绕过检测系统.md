---
title: Android 恶意软件“Konfety”利用格式错误的 APK 文件绕过检测系统
url: https://www.anquanke.com/post/id/310159
source: 安全客-有思想的安全新媒体
date: 2025-07-17
fetch_date: 2025-10-06T23:27:50.924516
---

# Android 恶意软件“Konfety”利用格式错误的 APK 文件绕过检测系统

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

# Android 恶意软件“Konfety”利用格式错误的 APK 文件绕过检测系统

阅读量**82045**

发布时间 : 2025-07-16 18:15:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/android-malware-konfety-uses-malformed-apks-to-evade-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为 Konfety 的 Android 恶意软件新变种近日被发现，其利用格式错误的 ZIP 结构和其他混淆手段绕过分析与检测机制。

Konfety 通常伪装成合法应用，模仿 Google Play 上常见的无害产品，但实际上并不具备所宣传的功能。

该恶意软件的功能包括：将用户重定向到恶意网站、推送不受欢迎的应用安装、伪造浏览器通知等。实际上，它使用 CaramelAds SDK 加载并展示隐藏广告，并窃取包括已安装应用、网络配置和系统信息在内的数据。

![]()

虽然 Konfety 并非传统意义上的间谍软件或远程访问木马（RAT），但它在 APK 中包含一个加密的次级 DEX 文件，在运行时解密并加载，其中包含在 AndroidManifest 文件中声明的隐藏服务。这一机制为后续动态加载更多危险模块打开了大门，使当前感染设备可能进一步被植入更具破坏性的功能。

## 规避检测的技巧

移动安全平台 Zimperium 的研究人员分析了该最新变种，发现 Konfety 使用多种方法隐藏其恶意本质与行为。

Konfety 通过复制 Google Play 上合法应用的名称和品牌，诱导受害者下载安装，这种策略被安全公司 Human 称为“恶意双胞胎”（evil twin）或“诱饵双胞胎”（decoy twin）。这些仿冒应用主要通过第三方应用商店传播。

使用者之所以偏向这些第三方市场，往往是因为他们希望获取“免费”版本的付费应用，规避 Google 追踪，或是他们的设备已经不再受支持，亦或根本无法访问 Google 服务。

此外，Konfety 利用动态代码加载技术，将其恶意逻辑隐藏在一个加密的 DEX 文件中，待运行时才解密加载，这是非常有效的混淆与规避方式。另一个鲜见的反分析策略是对 APK 文件结构本身进行操控，以干扰或阻止静态分析工具和逆向工程工具的正常解析。

具体而言：

**APK 设置了通用用途位标志（General Purpose Bit Flag）中的 bit 0**，该标志表示文件已加密，尽管实际上并未加密。如此设置会在分析时触发虚假的密码提示，从而阻碍或拖延对 APK 内容的访问。

![]()

**关键文件采用 BZIP 压缩算法（0x000C）声明**，而该压缩方式并不被 APKTool 或 JADX 等常用分析工具支持，最终导致解析失败。然而 Android 系统在运行时会忽略这种声明方式并退回到默认处理流程，从而允许该恶意应用顺利安装并运行，而不影响用户体验。

安装完成后，Konfety 会隐藏自身的图标与应用名，并根据受害者所处的地理位置调整其行为，具备地理围栏（geofencing）能力。

使用压缩结构进行混淆的手法并非首次出现。卡巴斯基在 2024 年 4 月发布的报告中就曾指出 **SoumniBot** 恶意软件使用了类似策略，包括在 AndroidManifest.xml 中声明无效的压缩方法、伪造文件大小与数据偏移信息、以及使用超长命名空间字符串干扰分析工具。

\*\*安全建议：\*\*切勿从第三方 Android 应用商店下载 APK 文件，仅信任您了解且可信的软件发布方。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/android-malware-konfety-uses-malformed-apks-to-evade-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310159](/post/id/310159)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/android-malware-konfety-uses-malformed-apks-to-evade-detection/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/android-malware-konfety-uses-malformed-apks-to-evade-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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

* [规避检测的技巧](#h2-0)

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