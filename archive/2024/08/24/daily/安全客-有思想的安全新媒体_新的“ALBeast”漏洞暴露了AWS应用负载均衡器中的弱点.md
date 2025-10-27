---
title: 新的“ALBeast”漏洞暴露了AWS应用负载均衡器中的弱点
url: https://www.anquanke.com/post/id/299432
source: 安全客-有思想的安全新媒体
date: 2024-08-24
fetch_date: 2025-10-06T18:01:08.415624
---

# 新的“ALBeast”漏洞暴露了AWS应用负载均衡器中的弱点

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

# 新的“ALBeast”漏洞暴露了AWS应用负载均衡器中的弱点

阅读量**42334**

发布时间 : 2024-08-23 11:20:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-albeast-vulnerability-exposes.html>

译文仅供参考，具体内容表达以及含义原文为准。

多达 15,000 个使用 Amazon Web Services （AWS） 应用程序负载均衡器 （ALB） 进行身份验证的应用程序可能容易受到基于配置的问题的影响，这可能会使它们面临规避访问控制并危及应用程序的风险。

这是根据以色列网络安全公司Miggo的调查结果得出的，该公司将问题称为**ALBeast**。

“这个漏洞允许攻击者直接访问受影响的应用程序，特别是当他们暴露在互联网上时，”安全研究员Liad Eliyahu说。

ALB 是一项 Amazon 服务，旨在根据请求的性质将 HTTP 和 HTTPS 流量路由到目标应用程序。它还允许用户从他们的应用程序中“卸载身份验证功能”到 ALB 中。

“Application Load Balancer 将在用户访问云应用程序时安全地对他们进行身份验证，”亚马逊在其网站上指出。

“Application Load Balancer 与 Amazon Cognito 无缝集成，允许最终用户通过 Google、Facebook 和 Amazon 等社交身份提供商进行身份验证，并通过 Microsoft Active Directory 等企业身份提供商通过 SAML 或任何符合 OpenID Connect 标准的身份提供商 （IdP） 进行身份验证。”

该攻击的核心涉及威胁参与者创建自己的 ALB 实例，并在其帐户中配置了身份验证。

在下一步中，ALB 用于签署他们控制下的令牌，并通过伪造具有受害者身份的真实 ALB 签名令牌来修改 ALB 配置，最终使用它来访问目标应用程序，绕过身份验证和授权。

换句话说，这个想法是让AWS对令牌进行签名，就好像它实际上来自受害者系统一样，并使用它来访问应用程序，假设它要么是可公开访问的，要么是攻击者已经可以访问它。

继 2024 年 4 月负责任地披露后，亚马逊更新了身份验证功能文档，并添加了新代码来验证签名者。

“为确保安全性，您必须在根据声明进行任何授权之前验证签名，并验证 JWT 标头中的签名者字段是否包含预期的应用程序负载均衡器 ARN，”亚马逊现在在其文档中明确指出。

“此外，作为安全最佳实践，我们建议您将目标限制为仅接收来自 Application Load Balancer 的流量。您可以通过配置目标的安全组来引用负载均衡器的安全组 ID 来实现此目的。

Acronis揭示了Microsoft Exchange的错误配置如何为电子邮件欺骗攻击打开大门，使威胁行为者能够绕过DKIM、DMARC和SPF保护，并发送伪装成受信任实体的恶意电子邮件。

该公司表示：“如果你没有锁定你的Exchange Online组织，只接受来自第三方服务的邮件，或者你没有为连接器启用增强过滤，任何人都可以通过 ourcompany.protection.outlook.com 或 ourcompany.mail.protection.outlook.com 向你发送电子邮件，DMARC（SPF和DKIM）验证将被跳过。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-albeast-vulnerability-exposes.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299432](/post/id/299432)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-albeast-vulnerability-exposes.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-albeast-vulnerability-exposes.html>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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