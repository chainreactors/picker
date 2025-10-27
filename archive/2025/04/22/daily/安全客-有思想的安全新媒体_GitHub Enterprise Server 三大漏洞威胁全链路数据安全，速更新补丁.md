---
title: GitHub Enterprise Server 三大漏洞威胁全链路数据安全，速更新补丁
url: https://www.anquanke.com/post/id/306716
source: 安全客-有思想的安全新媒体
date: 2025-04-22
fetch_date: 2025-10-06T22:03:48.610491
---

# GitHub Enterprise Server 三大漏洞威胁全链路数据安全，速更新补丁

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

# GitHub Enterprise Server 三大漏洞威胁全链路数据安全，速更新补丁

阅读量**46870**

发布时间 : 2025-04-21 10:54:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/github-enterprise-server-vulnerabilities-expose-risk-of-code-execution-and-data-leaks/>

译文仅供参考，具体内容表达以及含义原文为准。

![GitHub Enterprise, CVE-2025-3509]()

GitHub 已发布安全更新，以修复 GitHub Enterprise Server 中的多个漏洞，其中包括一个严重的高危漏洞，攻击者可能利用该漏洞执行任意代码。使用 GitHub Enterprise Server 的组织被敦促迅速应用这些补丁，以保护其系统安全。

****高危代码执行漏洞****

GitHub Enterprise Server 的预接收钩子（pre-receive hook）功能中存在一个漏洞（CVE-2025-3509）。这一漏洞可能使恶意攻击者得以执行任意代码，进而可能导致权限提升和系统被完全攻破。攻击者可以通过绑定到动态分配的、暂时可用的端口来利用该漏洞，比如在热补丁升级期间。

需要注意的是，这个漏洞只有在特定的操作条件下才能被利用，比如在热补丁更新过程中。此外，利用该漏洞需要具备站点管理员权限，或者是拥有修改包含预接收钩子的存储库权限的用户。

****信息泄露漏洞****

一个中等严重程度的漏洞（CVE-2025-3124）可能会让攻击者查看已登录用户无权查看的私有存储库名称。该问题出现在 GitHub 高级安全概览中，原因是在使用 “仅已存档（only archived:）” 进行筛选时，缺少权限检查。

****跨站脚本漏洞****

另一个严重的高危漏洞（CVE-2025-3246）涉及到 GitHub 的 Markdown 渲染中对输入的处理不当。攻击者可以利用这一漏洞在数学公式块（\(..\)）中嵌入恶意的 HTML/CSS 代码，从而导致跨站脚本攻击（XSS）。成功利用该漏洞需要访问目标 GitHub Enterprise Server 实例，并且需要特权用户与恶意元素进行交互。GitHub 已经通过禁止数学公式块过早地被美元符号转义，并改进了数学公式渲染内容，以确保未被包裹的内容得到正确转义，从而缓解了这一问题。

**受影响的版本和缓解措施**

以下版本的 GitHub Enterprise Server 受到影响：

1.受影响版本范围：3.13.0 至 3.13.13；3.13.14 及以上版本不受影响

2.受影响版本范围：3.14.0 至 3.14.10；3.14.11 及以上版本不受影响

3.受影响版本范围：3.15.0 至 3.15.5；3.15.6 及以上版本不受影响

4.受影响版本范围：3.16.0 至 3.16.1；3.16.2 及以上版本不受影响

GitHub 已发布了修复这些漏洞的补丁版本。对于管理员来说，将其 GitHub Enterprise Server 实例升级到最新的不受影响的版本至关重要，以确保其系统和数据的安全。

本文翻译自securityonline [原文链接](https://securityonline.info/github-enterprise-server-vulnerabilities-expose-risk-of-code-execution-and-data-leaks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306716](/post/id/306716)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/github-enterprise-server-vulnerabilities-expose-risk-of-code-execution-and-data-leaks/)

如若转载,请注明出处： <https://securityonline.info/github-enterprise-server-vulnerabilities-expose-risk-of-code-execution-and-data-leaks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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