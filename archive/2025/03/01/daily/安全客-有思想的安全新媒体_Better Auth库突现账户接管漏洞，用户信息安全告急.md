---
title: Better Auth库突现账户接管漏洞，用户信息安全告急
url: https://www.anquanke.com/post/id/304859
source: 安全客-有思想的安全新媒体
date: 2025-03-01
fetch_date: 2025-10-06T21:55:49.692490
---

# Better Auth库突现账户接管漏洞，用户信息安全告急

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

# Better Auth库突现账户接管漏洞，用户信息安全告急

阅读量**177574**

|评论**1**

发布时间 : 2025-02-28 15:17:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/account-takeover-vulnerability-found-in-better-auth-library/>

译文仅供参考，具体内容表达以及含义原文为准。

![Better Auth vulnerability]()

在 Better Auth 库（一种流行的 TypeScript 身份验证框架）中发现了一个严重的安全漏洞。该漏洞可能允许攻击者绕过安全措施并可能接管用户帐户。

该漏洞存在于 trustedOrigins 保护功能中，该功能旨在限制重定向到受信任的网站。但是，已发现允许攻击者利用此功能并将用户重定向到恶意网站的旁路。

根据安全公告：“发现安全功能 trustedOrigins 的绕过。这适用于通配符或绝对 URL trustedOrigins 配置，并会使受害者网站面临开放重定向漏洞，该漏洞可用于通过将“callbackURL”参数值更改为攻击者拥有的网站来窃取受害者帐户的重置密码令牌。

此漏洞可通过开放重定向来利用，攻击者会制作恶意链接并将其发送给受害者。当受害者点击该链接时，他们会被重定向到由攻击者控制的网站，这可能允许攻击者窃取受害者的重置密码令牌并接管他们的帐户。

该漏洞是由于负责处理 trustedOrigins 的中间件中未正确验证回调 URL 而引起的。攻击者可以制作恶意负载，例如：

https://demo.better-auth.com/api/auth/reset-password/x?callbackURL=/\/example.com

这利用了 URL 解析方式的问题，允许攻击者将受害者重定向到外部域。一旦受害者点击该链接，他们的密码重置令牌就会被发送到攻击者的网站，从而实现完整的帐户泄露。

另一种利用方法涉及在库的 trustedOrigins 处理中使用弱正则表达式模式： *[^/\\]\*?\.example\.com[/\\]\*?*

攻击者可以使用如下负载：http:attacker.com?.example.com/

由于 and 是 URL 中的特殊字符，因此浏览器将“http：”解释为 URL 方案的一部分，而不是纯文本，从而导致无意中重定向到攻击者的站点。

Better Auth 项目发布了 1.1.21 版本来解决该漏洞。强烈建议 Better Auth 库的所有用户尽快更新到最新版本，以保护自己免受潜在攻击。

本文翻译自securityonline [原文链接](https://securityonline.info/account-takeover-vulnerability-found-in-better-auth-library/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304859](/post/id/304859)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/account-takeover-vulnerability-found-in-better-auth-library/)

如若转载,请注明出处： <https://securityonline.info/account-takeover-vulnerability-found-in-better-auth-library/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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