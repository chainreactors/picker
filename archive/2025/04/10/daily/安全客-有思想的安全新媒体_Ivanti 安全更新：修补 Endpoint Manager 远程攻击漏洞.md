---
title: Ivanti 安全更新：修补 Endpoint Manager 远程攻击漏洞
url: https://www.anquanke.com/post/id/306306
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:03.720543
---

# Ivanti 安全更新：修补 Endpoint Manager 远程攻击漏洞

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

# Ivanti 安全更新：修补 Endpoint Manager 远程攻击漏洞

阅读量**51440**

发布时间 : 2025-04-09 10:46:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：TheHackersNews

原文地址：<https://cybersecuritynews.com/ivanti-security-updates-april/>

译文仅供参考，具体内容表达以及含义原文为准。

领先的企业软件解决方案提供商 Ivanti 已为其 Endpoint Manager（EPM）产品发布了关键的安全更新，以修复多个可能会让攻击者获得未经授权的访问权限、提升权限或破坏系统的漏洞。

这些更新于 2025 年 4 月 8 日今天发布，针对的是 Ivanti Endpoint Manager EPM 2024 和 EPM 2022 SU6 版本，补丁分别可在 2024 SU1 和 2022 SU7 版本中获取。

这些更新修复了一系列中等到高严重程度的漏洞，其中包括一些可能会被远程利用的漏洞。

### ****漏洞概述****

安全公告详细列出了六个常见漏洞和暴露（CVE），在通用漏洞评分系统（CVSS）的评分标准下，严重程度得分范围从 4.8（中等）到 8.2（高）。其中最值得关注的漏洞包括：

1.CVE-2025-22466（CVSS 评分 8.2，高）：这是一个反射型跨站脚本（XSS）漏洞，允许远程的未经身份验证的攻击者通过用户交互获取管理员权限。这个漏洞有可能让攻击者对受影响的系统获得重要控制权。

2.CVE-2025-22458（CVSS 评分 7.8，高）：一个动态链接库（DLL）劫持漏洞，使具有本地访问权限的已身份验证攻击者能够将权限提升到系统（SYSTEM）级别，对系统完整性构成严重威胁。

3.CVE-2025-22461（CVSS 评分 7.2，高）：一个 SQL 注入漏洞，允许具有管理员权限的远程已身份验证攻击者执行任意代码，有可能导致整个系统被攻陷。

其他漏洞包括不可信的指针解引用（CVE-2025-22464）、额外的反射型 XSS 问题（CVE-2025-22465）以及不当的证书验证（CVE-2025-22459），这些漏洞可能使攻击者能够拦截有限的客户端-服务器流量。

这些漏洞影响 Ivanti Endpoint Manager EPM 2022 SU6 及更早版本，以及 EPM 2024 版本。Ivanti已在最新版本中修复了这些问题：

1.EPM 2022 SU7

2.EPM 2024 SU1

补丁可通过 Ivanti 许可门户（ILS）下载，该公司敦促客户立即进行更新以降低风险。

### ****目前尚无已知的漏洞利用情况****

Ivanti 表示，截至披露日期，尚未发现这些漏洞被积极利用的情况。这些问题是通过该公司的负责任披露计划发现的，公司感谢 Eviden SEC 咨询漏洞实验室发现 CVE-2025-22458 的安全研究人员 Paul Serban，和 Trend Micro 发现 CVE-2025-22461的 Kevin Salapatek，所做出的贡献。

Ivanti 指出：“目前，没有已知的公开漏洞利用情况可以用来提供入侵指标列表。” 然而，这些漏洞的潜在严重性凸显了应用更新的紧迫性。

这些漏洞带来了一系列风险，从拒绝服务攻击到整个系统被接管，具体取决于攻击者的访问级别和利用方法。虽然有些漏洞需要用户交互或本地访问权限，但其他一些漏洞，如高严重性的 XSS 和 SQL 注入漏洞，可以被远程利用，这使得在未打补丁的环境中它们特别危险。

Ivanti 建议客户：

1.立即更新到 EPM 2022 SU7 或 EPM 2024 SU1 版本。

2.尽管尚未发现已知的漏洞利用情况，但仍需监控系统是否存在异常活动。

3.如果需要支持，请联系 Ivanti Success Portal。

在其安全公告中，Ivanti 强调了其对产品安全的重视以及与更广泛的安全社区的合作。该公司表示：“我们认识到安全研究人员、道德黑客和更广泛的安全社区在识别和报告漏洞方面发挥的重要作用。” 并引导用户查看其漏洞披露政策以获取更多详细信息。

随着网络威胁每天都在演变，这份安全公告对于依赖 Ivanti Endpoint Manager 的组织来说是一个重要的提醒，即要优先进行补丁管理。虽然尚未有漏洞被利用的报告，但远程访问和权限提升的潜在风险使得这些更新对于维护安全的企业环境来说是必不可少的。

如需了解更多信息或下载补丁，请访问 Ivanti 许可门户。随着安全社区继续监控这些漏洞，请随时关注最新动态。

本文翻译自TheHackersNews [原文链接](https://cybersecuritynews.com/ivanti-security-updates-april/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306306](/post/id/306306)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://cybersecuritynews.com/ivanti-security-updates-april/)

如若转载,请注明出处： <https://cybersecuritynews.com/ivanti-security-updates-april/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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