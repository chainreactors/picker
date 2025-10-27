---
title: Adobe 紧急发布安全更新，修复十二款产品多项漏洞
url: https://www.anquanke.com/post/id/306342
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:04.851553
---

# Adobe 紧急发布安全更新，修复十二款产品多项漏洞

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

# Adobe 紧急发布安全更新，修复十二款产品多项漏洞

阅读量**75101**

发布时间 : 2025-04-10 10:32:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/adobe-security-update-multiple-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

Adobe 已发布了一套全面的安全更新，用于修复旗下十二款产品中存在的多个漏洞。

这些补丁均于 2025 年 4 月 8 日发布，旨在解决严重、重要及中等程度的安全缺陷，这些缺陷可能会使用户面临各种网络威胁，包括任意代码执行、权限提升以及应用程序拒绝服务攻击。

****已修复的重大漏洞****

****1.Adobe ColdFusion（APSB25-15）****

ColdFusion 的更新修复了多个漏洞，包括不当的输入验证（CVE-2025-24446）、不可信数据的反序列化（CVE-2025-24447）以及不当的访问控制（CVE-2025-30281）。

其他漏洞，如操作系统命令注入（CVE-2025-30286）和跨站脚本攻击（CVE-2025-30292）也得到了解决。

这些漏洞可能会导致任意代码执行、权限提升或敏感信息泄露。

****2.Adobe After Effects（APSB25-23）****

After Effects 的更新修复了诸如内存泄漏和应用程序拒绝服务等严重漏洞。

如果被成功利用，可能会在已登录用户的环境中执行任意代码。受影响的版本包括 24.6.4 及更早版本，以及 Windows 和 macOS 系统上的 25.1 版本。

****3.Adobe Media Encoder（APSB25-24）****

Media Encoder 的更新修复了两个严重漏洞：越界写入（CVE-2025-27194）和基于堆的缓冲区溢出（CVE-2025-27195）。

这些漏洞可能会导致任意代码执行，通用漏洞评分系统（CVSS）评分为 7.8。

****4.Adobe Bridge（APSB25-25）****

Bridge 的安全补丁修复了一个基于堆的缓冲区溢出漏洞（CVE-2025-27193），该漏洞可能会导致任意代码执行。

此漏洞影响 Windows 和 macOS 平台上的 14.1.5 及更早版本，以及 15.0.2 版本。

****5.Adobe Commerce（APSB25-26）****

Adobe Commerce 和 Magento 开源版收到了安全更新，以修复可能导致安全功能绕过、权限提升和应用程序拒绝服务的漏洞。

受影响的版本包括所有平台上的 Adobe Commerce 2.4.8-beta2 及更早版本、Adobe Commerce B2B 1.5.1 及更早版本，以及 Magento 开源版 2.4.8-beta2 及更早版本。

****6.Adobe Experience Manager Forms（APSB25-27）****

AEM Forms 的更新修复了路径遍历（CVE-2024-38819）和区分大小写匹配异常漏洞（CVE-2024-38820）。

这些漏洞源于对第三方组件的依赖，可能会导致未经授权的访问或数据泄露。

****7.Adobe Premiere Pro（APSB25-28）****

Premiere Pro 的更新修复了一个严重的基于堆的缓冲区溢出漏洞（CVE-2025-27196），该漏洞可能会导致受影响的 24.6.4 及更早版本，以及 Windows 和 macOS 系统上的 25.1 版本中执行任意代码。

****8.Adobe Photoshop（APSB25-30）****

Photoshop 的补丁修复了一个基于堆的缓冲区溢出漏洞（CVE-2025-27198），被评定为严重级别，CVSS 评分为 7.8。

如果该漏洞被成功利用，可能会导致任意代码执行。

****9.Adobe Animate（APSB25-31）****

Adobe Animate 的更新修复了严重漏洞，如基于堆的缓冲区溢出（CVE-2025-27199）和释放后使用（CVE-2025-27200），这两个漏洞的 CVSS 评分均为 7.8，可能会导致任意代码执行。

此外，还修复了两个内存泄漏漏洞（CVE-2025-27201 和 CVE-2025-27202），评定为重要级别，CVSS 评分为 5.5。这些漏洞影响 Windows 和 macOS 平台上的 Adobe Animate 2023（23.0.10 及更早版本）和 2024（24.0.7 及更早版本）。

****10.Adobe Experience Manager Screens（APSB25-32）****

Adobe Experience Manager（AEM）Screens 的更新修复了一个与反射型跨站脚本攻击（XSS）相关的重要漏洞（CVE-2025-27205）。

此漏洞的 CVSS 评分为 5.4，如果被成功利用，可能会导致任意代码执行。它影响所有平台上直至 AEM 6.5 Screens FP11.3 的 AEM Screens 版本。

****11.Adobe FrameMaker（APSB25-33）****

FrameMaker 的更新修复了几个严重漏洞，包括越界写入（CVE-2025-30304）、基于堆的缓冲区溢出（CVE-2025-30295）和基于栈的缓冲区溢出（CVE-2025-30298）。

这些问题可能会让攻击者执行任意代码或导致应用程序崩溃。

****12.Adobe XMP Toolkit SDK（APSB25-34）****

XMP Toolkit SDK 的更新修复了多个越界读取漏洞（例如，CVE-2025-30305 至 CVE-2025-30309）。

利用这些漏洞可能会导致信息泄露或应用程序不稳定。

安全专家建议所有受影响的 Adobe 产品用户立即更新其安装的软件。

对于大多数产品，可以通过 Creative Cloud 桌面应用程序的更新机制进行更新，或者在各个应用程序中进入 “帮助” 菜单并选择 “更新”。

对于托管环境，IT 管理员可以使用 Creative Cloud Packager 创建部署包。

Adobe 已确认，目前尚未发现这些漏洞在现实中被利用的情况。然而，及时打补丁对于维护 Adobe 创意和企业产品生态系统的安全完整性仍然至关重要。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/adobe-security-update-multiple-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306342](/post/id/306342)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/adobe-security-update-multiple-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/adobe-security-update-multiple-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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