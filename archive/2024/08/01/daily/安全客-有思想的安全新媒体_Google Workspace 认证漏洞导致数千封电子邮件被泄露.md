---
title: Google Workspace 认证漏洞导致数千封电子邮件被泄露
url: https://www.anquanke.com/post/id/298610
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:04.473148
---

# Google Workspace 认证漏洞导致数千封电子邮件被泄露

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

# Google Workspace 认证漏洞导致数千封电子邮件被泄露

阅读量**88406**

发布时间 : 2024-07-31 11:22:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Fiona Jackson，文章来源：TechRepublic

原文地址：<https://www.techrepublic.com/article/google-workspace-vulnerability-accounts-compromised/>

译文仅供参考，具体内容表达以及含义原文为准。

数以千计的电子邮件地址在黑客使用它们创建 Google Workspace 帐户并绕过验证过程后遭到入侵。

根据谷歌的说法，“特别构建的请求”可以在不验证电子邮件的情况下开设Workspace帐户。这意味着不良行为者只需要他们想要的目标的电子邮件地址来冒充他们。

虽然没有一个虚假帐户用于滥用 Google 服务，例如 Gmail 或 Docs，但它们用于通过“使用 Google 登录”功能访问第三方服务。

一位在 Google Cloud 社区论坛上分享体验的受影响用户收到 Google 通知，称有人在未经验证的情况下使用他们的电子邮件创建了 Workspace 帐户，然后使用它登录 Dropbox。

谷歌发言人告诉TechRepublic：“在6月下旬，我们迅速解决了一个账户滥用问题，影响了一小部分电子邮件账户。我们正在进行彻底的分析，但到目前为止，还没有发现谷歌生态系统中存在更多滥用行为的证据。

验证漏洞仅限于“电子邮件已验证”工作区帐户，因此它不会影响其他用户类型，例如“域已验证”帐户。

Google Workspace滥用和安全保护主管Anu Yamunan告诉Krebs on Security，恶意活动始于6月下旬，并检测到“几千个”未经验证的Workspace帐户。然而，该报道和 Hacker News 的评论者声称，攻击实际上始于 6 月初

在发送给受影响电子邮件的消息中，谷歌表示，它在发现漏洞后72小时内修复了该漏洞，此后添加了“额外的检测”过程，以确保它不会被重复。

## 不良行为者如何利用 Google Workspace 帐号

注册 Google Workspace 帐户的个人可以访问有限数量的服务，例如 Docs，作为免费试用。此试用将在 14 天后结束，除非他们验证其电子邮件地址，该电子邮件地址提供完整的 Workspace 访问权限。

但是，该漏洞允许不良行为者在未经验证的情况下访问全套服务，包括 Gmail 和依赖域的服务。

“这里的策略是由不良行为者创建一个专门构建的请求，以在注册过程中规避电子邮件验证，”Yamunan告诉Krebs on Security。“这里的载体是，他们会使用一个电子邮件地址来尝试登录，并使用一个完全不同的电子邮件地址来验证令牌。

“一旦他们通过了电子邮件验证，在某些情况下，我们看到他们使用 Google 单点登录访问第三方服务。”

Google 部署的修复程序可防止恶意用户重复使用为一个电子邮件地址生成的令牌来验证另一个地址。

受影响的用户批评了谷歌提供的试用期，称那些试图使用带有自定义域的电子邮件地址开设Workspace帐户的人在验证其域所有权之前不应有任何访问权限。

这并不是Google Workspace在过去一年中第一次遭受安全事件的影响。

去年 12 月，网络安全研究人员发现了 DeleFriend 漏洞，该漏洞可能让攻击者使用权限提升来获得超级管理员访问权限。然而，一位匿名的谷歌代表告诉The Hacker News，这并不代表“我们产品中的潜在安全问题”。

11 月，Bitdefender 的一份报告披露了 Workspace 中与 Windows 版 Google Credential Provider 相关的几个弱点，这些弱点可能导致勒索软件攻击、数据泄露和密码盗窃。谷歌再次对这些发现提出异议，并告诉研究人员，它没有计划解决这些问题，因为它们超出了特定的威胁模型。

本文翻译自TechRepublic [原文链接](https://www.techrepublic.com/article/google-workspace-vulnerability-accounts-compromised/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298610](/post/id/298610)

安全KER - 有思想的安全新媒体

本文转载自: [TechRepublic](https://www.techrepublic.com/article/google-workspace-vulnerability-accounts-compromised/)

如若转载,请注明出处： <https://www.techrepublic.com/article/google-workspace-vulnerability-accounts-compromised/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [不良行为者如何利用 Google Workspace 帐号](#h2-0)

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