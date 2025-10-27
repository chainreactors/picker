---
title: GitHub Actions易受拼写攻击，使开发者暴露于隐藏的恶意代码风险之中
url: https://www.anquanke.com/post/id/299904
source: 安全客-有思想的安全新媒体
date: 2024-09-10
fetch_date: 2025-10-06T18:23:54.313239
---

# GitHub Actions易受拼写攻击，使开发者暴露于隐藏的恶意代码风险之中

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

# GitHub Actions易受拼写攻击，使开发者暴露于隐藏的恶意代码风险之中

阅读量**58038**

发布时间 : 2024-09-09 16:02:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/github-actions-vulnerable-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

长期以来，威胁行为者一直利用拼写错误作为诱骗毫无戒心的用户访问恶意网站或下载诱杀软件和软件包的手段。

这些攻击通常涉及注册域名或软件包，其名称与合法域名或软件包略有不同（例如，goog1e.com 与 google.com 域名或软件包）。

以跨平台开源存储库为目标的攻击者依靠开发人员的打字错误，通过 PyPI、npm、Maven Central、NuGet、RubyGems 和 Crate 发起软件供应链攻击。

云安全公司 Orca 的最新调查结果显示，即使是持续集成和持续交付 （CI/CD） 平台 GitHub Actions 也无法幸免于威胁。

“如果开发人员在他们的 GitHub 操作中犯了与拼写错误者的操作相匹配的拼写错误，则应用程序可能会在开发人员甚至没有意识到的情况下运行恶意代码，”安全研究员 Ofir Yakobi 在与 The Hacker News 分享的一份报告中说。

这种攻击是可能的，因为任何人都可以通过使用临时电子邮件帐户创建 GitHub 帐户来发布 GitHub Action。鉴于操作在用户存储库的上下文中运行，因此可以利用恶意操作来篡改源代码、窃取密钥并使用它来传递恶意软件。

该技术涉及的只是让攻击者创建名称和名称与流行或广泛使用的 GitHub Actions 非常相似的组织和存储库。

如果用户在为其项目设置 GitHub 操作时无意中犯了拼写错误，并且该拼写错误的版本已经由对手创建，则用户的工作流程将运行恶意操作，而不是预期的操作。

“想象一下，一个操作会泄露敏感信息或修改代码以引入细微的错误或后门，从而可能影响所有未来的构建和部署，”Yakobi 说。

“事实上，受感染的操作甚至可以利用您的 GitHub 凭证将恶意更改推送到组织内的其他存储库，从而放大多个项目的损害。”

Orca 表示，在 GitHub 上搜索后发现，有多达 198 个文件调用了 “action/checkout” 或 “actons/checkout” 而不是 “actions/checkout” （注意缺少的 “s” 和 “i”），使所有这些项目都处于危险之中。

这种形式的拼写抢注对威胁行为者很有吸引力，因为它是一种低成本、高影响的攻击，可能会导致强大的软件供应链泄露，同时影响多个下游客户。

建议用户仔细检查操作及其名称，以确保他们引用的是正确的 GitHub 组织，坚持使用来自可信来源的操作，并定期扫描其 CI/CD 工作流以查找拼写错误问题。

“这项实验强调了攻击者利用 GitHub Actions 中的拼写错误是多么容易，以及保持警惕和最佳实践在防止此类攻击方面的重要性，”Yakobi 说。

“实际问题更令人担忧，因为这里我们只强调公共仓库中发生的情况。对私有存储库的影响仍然未知，因为相同的拼写错误可能会导致严重的安全漏洞。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/github-actions-vulnerable-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299904](/post/id/299904)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/github-actions-vulnerable-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/github-actions-vulnerable-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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