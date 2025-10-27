---
title: 安装量为 4B 的 Android 应用为代码执行攻击敞开了大门
url: https://www.anquanke.com/post/id/296200
source: 安全客-有思想的安全新媒体
date: 2024-05-07
fetch_date: 2025-10-06T17:17:04.647287
---

# 安装量为 4B 的 Android 应用为代码执行攻击敞开了大门

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

# 安装量为 4B 的 Android 应用为代码执行攻击敞开了大门

阅读量**74211**

发布时间 : 2024-05-06 11:34:45

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/xiaomi-file-manager-wps-office-android-apps-vulnerable/>

译文仅供参考，具体内容表达以及含义原文为准。

***如果您的Android设备有小米文件管理器或WPS Office，请立即更新。多个总安装量超过 40 亿的 Android 应用程序被发现存在漏洞，允许攻击者运行任意代码或窃取凭据。***

微软发现多个流行的 Android 应用程序容易受到攻击，从而诱骗这些应用程序覆盖自己的关键文件。恶意软件可以通过创建文件名来利用此漏洞（称为“脏流攻击”），然后易受攻击的应用程序会在未经验证的情况下盲目接受这些文件名。

“此漏洞模式的影响包括任意代码执行和令牌盗窃，具体取决于应用程序的实现，”微软表示。

“任意代码执行可以使威胁行为者完全控制应用程序的行为。同时，令牌盗窃可以为威胁行为者提供对用户帐户和敏感数据的访问权限。”

小米的文件管理器（在 Google Play 商店中安装量超过 10 亿）和 WPS Office（在 Google Play 商店中的安装量超过 5 亿）都容易受到攻击。披露后，截至 2024 年 2 月，开发人员已发布解决这些漏洞的更新。

然而，微软还发现了其他多个容易受到“脏流”影响的未公开应用程序，这些应用程序的安装次数超过了 25 亿次。至少还有另外两款应用的安装量超过 5 亿。该公司还预计“该漏洞模式可能会在其他应用程序中发现”。

## 攻击将如何进行？

Android 操作系统通过为每个应用程序分配自己的专用数据和内存空间来强制应用程序隔离。对于文件共享，Android 提供了一个组件作为接口，用于管理数据并将数据公开给设备上的其他应用程序。

微软研究人员观察到，多个应用程序不会验证所提供的文件内容，甚至在其内部数据目录中缓存接收到的文件时使用其他应用程序提供的文件名。

“实施不当可能会引入漏洞，从而绕过应用程序主目录中的读/写限制，”微软解释道。

以小米的文件管理器为例，该实现允许攻击者通过用恶意库覆盖本机库来执行任意代码。此外，攻击者还可以连接到本地网络上的远程 FTP 或 SMB 共享。

![]()

谷歌为开发者发布了如何清理应用程序的指南。

“如果攻击者可以覆盖应用程序的文件，这可能会导致恶意代码执行（通过覆盖应用程序的代码），或者允许以其他方式修改应用程序的行为（例如，通过覆盖应用程序的共享首选项或其他配置文件）”，Google警告。

微软通过分享对该漏洞的研究，希望其他开发者能够检查他们的应用程序是否存在类似的普遍问题并发布修复程序。

本文翻译自 [原文链接](https://cybernews.com/security/xiaomi-file-manager-wps-office-android-apps-vulnerable/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296200](/post/id/296200)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/xiaomi-file-manager-wps-office-android-apps-vulnerable/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [攻击将如何进行？](#h2-0)

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