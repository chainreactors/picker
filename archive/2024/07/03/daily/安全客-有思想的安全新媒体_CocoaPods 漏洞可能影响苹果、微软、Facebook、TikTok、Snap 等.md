---
title: CocoaPods 漏洞可能影响苹果、微软、Facebook、TikTok、Snap 等
url: https://www.anquanke.com/post/id/297621
source: 安全客-有思想的安全新媒体
date: 2024-07-03
fetch_date: 2025-10-06T17:39:30.566807
---

# CocoaPods 漏洞可能影响苹果、微软、Facebook、TikTok、Snap 等

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

# CocoaPods 漏洞可能影响苹果、微软、Facebook、TikTok、Snap 等

阅读量**116597**

发布时间 : 2024-07-02 11:49:29

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/cocoapods-vulnerabilities-apple-facebook/>

译文仅供参考，具体内容表达以及含义原文为准。

今天报告的 CocoaPods 漏洞可能允许恶意行为者接管数千个无人认领的 pod，并将恶意代码插入许多最流行的iOS和 MacOS 应用程序中，从而可能影响“几乎所有 Apple 设备”。

EVA 信息安全研究人员发现，开源 CocoaPods 依赖管理器中的三个漏洞存在于 Meta（Facebook、Whatsapp）、苹果（Safari、AppleTV、Xcode）和微软（Teams）提供的应用程序中；以及TikTok、Snapchat、亚马逊、LinkedIn、Netflix、Okta、雅虎、Zynga 等中。

这些漏洞已被修补，但研究人员仍然发现 685 个 Pod“与孤立 Pod 有明确的依赖关系；毫无疑问，专有代码库中还有数百或数千个这样的 Pod”。

这一普遍问题进一步证明了软件供应链的脆弱性。研究人员写道，他们经常发现，他们审查的客户端代码中有 70-80%“是由开源库、软件包或框架组成的”。

**CocoaPods 漏洞**
新发现的漏洞（其中一个漏洞 (CVE-2024-38366) 获得了 10 分（满分 10 分））实际上源于 2014 年 5 月 CocoaPods 迁移到新的“Trunk”服务器时，当时留下了 1,866 个所有者从未回收的孤立 pod。

另外两个 CocoaPods 漏洞（CVE-2024-38368 和 CVE-2024-38367）也源于此次迁移。

对于 CVE-2024-38368，研究人员表示，在分析“Trunk”服务器的源代码时，他们注意到所有孤立 Pod 都与默认的 CocoaPods 所有者相关联，并且为该默认所有者创建的电子邮件为unclaimed-pods@cocoapods.org 。他们还注意到，用于声明 Pod 的公共 API 端点仍然可用，并且该 API“允许任何人声明孤立 Pod，而无需任何所有权验证过程”。

Reef Spektor 和 Eran Vaknin 写道：“通过向公开可用的 API 发出简单的 curl 请求，并提供未认领的目标 pod 名称，潜在的攻击者就大有可为，他们可以将部分或全部这些孤立 pod 占为己有。”

一旦接管了 Pod，攻击者就能够操纵源代码或将恶意内容插入 Pod，这“将继续感染许多下游依赖项，并可能进入目前正在使用的大量 Apple 设备。”

2014 年初，CocoaPods 的“Trunk”源代码发生了变化，用于实现注册电子邮件的 MX 记录验证。这些变化创建了一条新的攻击路径，通过分析注册流程可以识别出该路径，从而导致 CVE-2024-38366 漏洞。这些变化使用第三方 Ruby gem 包 rfc-822 为用户提供的电子邮件地址创建了新的验证流程，该流程可以通过几种方式进行攻击，可能导致“转储 pod 所有者的会话令牌、毒害客户端流量甚至完全关闭服务器”的攻击。

在 CVE-2024-38367 中，研究人员发现他们可以欺骗 XFH 标头，通过破坏电子邮件安全边界来设计零点击帐户接管。

研究人员表示：“通过这种方法，我们成功接管了一些最受欢迎的 CocoaPods 软件包的所有者账户。我们可能会利用这些账户对供应链进行极具破坏性的攻击，从而影响整个 Apple 生态系统。”

**DevOps 团队：开始工作**
虽然这些漏洞已被修补，但开发人员和 DevOps 团队的工作才刚刚开始。

EVA 研究人员表示，近年来使用过 CocoaPods 的开发人员和 DevOps 团队（尤其是在 2023 年 10 月之前）“应该验证其应用程序代码中使用的开源依赖项的完整性”。

“我们发现的漏洞可用于控制依赖管理器本身以及任何已发布的包。”

下游依赖关系可能意味着过去几年中数以千计的应用程序和数百万台设备被暴露，应该密切关注依赖于未分配所有者的孤立 CocoaPod 包的软件。

开发人员和组织应检查其应用程序中使用的依赖项列表和包管理器，验证第三方库的校验和，执行定期扫描以检测恶意代码或可疑更改，保持软件更新，并限制使用孤立或未维护的包。

研究人员写道：“依赖项管理器是软件供应链安全中经常被忽视的一个方面。安全领导者应该探索加强对这些工具使用的治理和监督的方法。”

本文翻译自 [原文链接](https://thecyberexpress.com/cocoapods-vulnerabilities-apple-facebook/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297621](/post/id/297621)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/cocoapods-vulnerabilities-apple-facebook/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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