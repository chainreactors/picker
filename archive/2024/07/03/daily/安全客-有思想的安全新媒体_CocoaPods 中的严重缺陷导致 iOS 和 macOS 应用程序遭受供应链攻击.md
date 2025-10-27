---
title: CocoaPods 中的严重缺陷导致 iOS 和 macOS 应用程序遭受供应链攻击
url: https://www.anquanke.com/post/id/297638
source: 安全客-有思想的安全新媒体
date: 2024-07-03
fetch_date: 2025-10-06T17:39:24.343713
---

# CocoaPods 中的严重缺陷导致 iOS 和 macOS 应用程序遭受供应链攻击

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

# CocoaPods 中的严重缺陷导致 iOS 和 macOS 应用程序遭受供应链攻击

阅读量**135065**

发布时间 : 2024-07-02 13:20:29

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html>

译文仅供参考，具体内容表达以及含义原文为准。

![供应链攻击]()

Swift 和 Objective-C Cocoa 项目的CocoaPods依赖管理器中发现了三个安全漏洞，可能被利用来发起软件供应链攻击，使下游客户面临严重风险。

EVA 信息安全研究人员 Reef Spektor 和 Eran Vaknin在今天发布的一份报告中表示，这些漏洞允许“任何恶意行为者声称拥有数千个无人认领的 pod，并将恶意代码插入许多最受欢迎的 iOS 和 macOS 应用程序中”。

这家以色列应用安全公司表示，截至 2023 年 10 月，这三个问题已被CocoaPods修补。为了应对这些披露，它还重置了当时的所有用户会话。

其中一个漏洞是 CVE-2024-38368（CVSS 评分：9.3），攻击者可以利用该漏洞滥用“ Claim Your Pods ”流程并控制软件包，从而有效地篡改源代码并引入恶意更改。但是，这需要所有先前的维护者都已从项目中移除。

问题的根源可以追溯到 2014 年，当时迁移到Trunk 服务器时留下了数千个所有者不明（或无人认领）的软件包，这允许攻击者使用公共 API 来认领 pod 以及 CocoaPods 源代码中提供的电子邮件地址（“unclaimed-pods@cocoapods.org”）来接管控制权。

第二个漏洞更为严重（CVE-2024-38366，CVSS 评分：10.0），它利用不安全的电子邮件验证工作流程在 Trunk 服务器上运行任意代码，然后可用于操纵或替换软件包。

该服务中还发现了电子邮件地址验证组件中的第二个问题（CVE-2024-38367，CVSS 评分：8.2），该问题可能会诱使收件人点击看似无害的验证链接，而实际上，它会将请求重新路由到攻击者控制的域以获取对开发人员会话令牌的访问权限。

更糟糕的是，通过欺骗 HTTP 标头（即修改X-Forwarded-Host标头字段）并利用配置错误的电子邮件安全工具，这可以升级为零点击帐户接管攻击。

研究人员表示：“我们发现几乎每个 pod 所有者都在 Trunk 服务器上注册了他们的组织电子邮件，这使得他们容易受到我们的零点击接管漏洞的攻击。”

这并不是 CocoaPods 第一次受到关注。2023 年 3 月，Checkmarx透露，与依赖项管理器关联的废弃子域（“cdn2.cocoapods[.]org”）可能已被攻击者通过 GitHub Pages 劫持，目的是托管他们的有效载荷。

本文翻译自 [原文链接](https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297638](/post/id/297638)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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