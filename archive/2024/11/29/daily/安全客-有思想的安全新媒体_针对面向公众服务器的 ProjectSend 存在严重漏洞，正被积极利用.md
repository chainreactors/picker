---
title: 针对面向公众服务器的 ProjectSend 存在严重漏洞，正被积极利用
url: https://www.anquanke.com/post/id/302270
source: 安全客-有思想的安全新媒体
date: 2024-11-29
fetch_date: 2025-10-06T19:14:42.056439
---

# 针对面向公众服务器的 ProjectSend 存在严重漏洞，正被积极利用

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

# 针对面向公众服务器的 ProjectSend 存在严重漏洞，正被积极利用

阅读量**62100**

发布时间 : 2024-11-28 15:14:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/critical-flaw-in-projectsend-under.html>

译文仅供参考，具体内容表达以及含义原文为准。

根据VulnCheck的调查结果，一个影响ProjectSend开源文件共享应用程序的关键安全漏洞很可能已被恶意利用。

该漏洞最初是在一年半前作为 2023 年 5 月推送的提交的一部分修补的，直到 2024 年 8 月发布 r1720 版本后才正式可用。截至 2024 年 11 月 26 日，该漏洞已被指定为 CVE 标识符 CVE-2024-11680（CVSS 得分：9.8）。

Synacktiv 于 2023 年 1 月向项目维护者报告了该漏洞，并将其描述为一个不当的授权检查，允许攻击者在易受影响的服务器上执行恶意代码。

该公司在 2024 年 7 月发布的一份报告中说：“在 ProjectSend r1605 版本中发现了一个不适当的授权检查，允许攻击者执行敏感操作，如启用用户注册和自动验证，或在上传文件允许扩展名的白名单中添加新条目。”

“最终，这允许在托管应用程序的服务器上执行任意 PHP 代码。”

VulnCheck 说，它观察到未知威胁行为者利用 Project Discovery 和 Rapid7 发布的漏洞利用代码，以面向公众的 ProjectSend 服务器为目标。据信，这些利用尝试始于 2024 年 9 月。

还发现这些攻击启用了用户注册功能，以获得认证后权限进行后续利用，这表明它们并不局限于扫描易受攻击的实例。

VulnCheck的Jacob Baines说：“我们很可能已经进入了‘攻击者安装网络外壳’的领域（从技术上讲，该漏洞也允许攻击者嵌入恶意JavaScript，这可能是一个有趣的、不同的攻击场景）。”

“如果攻击者上传了网络外壳，就可以在网络根目录下的 upload/files/ 中找到它。”

对大约 4000 台暴露在互联网上的 ProjectSend 服务器进行的分析表明，其中仅有 1%的服务器使用的是已打补丁的版本（r1750），其余所有实例运行的要么是未命名的版本，要么是 2022 年 10 月发布的 r1605 版本。

鉴于该漏洞似乎被广泛利用，建议用户尽快应用最新的补丁程序，以减轻主动威胁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/critical-flaw-in-projectsend-under.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302270](/post/id/302270)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/critical-flaw-in-projectsend-under.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/critical-flaw-in-projectsend-under.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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