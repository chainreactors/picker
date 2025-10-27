---
title: 黑客利用恶意NuGet包攻击.NET开发人员
url: https://www.anquanke.com/post/id/287696
source: 安全客-有思想的安全新媒体
date: 2023-03-23
fetch_date: 2025-10-04T10:19:52.362868
---

# 黑客利用恶意NuGet包攻击.NET开发人员

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

# 黑客利用恶意NuGet包攻击.NET开发人员

阅读量**206307**

发布时间 : 2023-03-22 12:00:31

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

威胁攻击者通过 NuGet 存储库提供的加密货币窃取程序瞄准并感染 .NET 开发人员，并通过打字抓取模拟多个合法软件包。

根据 JFrog 安全研究人员 Natan Nehorai 和 Brian Moussalli 的说法，其中三个在一个月内被下载了超过150000次，他们发现了这个正在进行的活动。虽然大量下载可能表明大量 .NET 开发人员的系统遭到破坏，但也可以解释为攻击者试图使其恶意 NuGet 包合法化。JFrog 安全研究人员表示：“前三个软件包的下载次数令人难以置信——这可能表明攻击非常成功，感染了大量机器。  ”

“然而，这并不是攻击成功的完全可靠指标，因为攻击者可能会自动夸大下载计数（使用机器人）以使软件包看起来更合法。”威胁行为者在创建 NuGet 存储库配置文件时还使用了域名仿冒来冒充使用 NuGet .NET 程序包管理器的 Microsoft 软件开发人员的帐户。[[阅读原文]](https://www.bleepingcomputer.com/news/security/hackers-target-net-developers-with-malicious-nuget-packages/)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287696](/post/id/287696)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [.net](/tag/.net)
* [NuGet](/tag/NuGet)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

### 相关文章

* ##### [卷入.NET WEB](/post/id/273034)

  2022-05-13 14:30:29
* ##### [CVE-2020-0618 复现&分析](/post/id/236295)

  2021-04-23 16:30:14
* ##### [如何控制.NET CLR使用日志实现EDR规避](/post/id/235238)

  2021-03-29 15:30:28
* ##### [基于.NET动态编译技术实现任意代码执行](/post/id/234449)

  2021-03-12 15:30:45
* ##### [Windows .NET Core SDK权限提升漏洞分析](/post/id/215180)

  2020-08-25 15:30:33
* ##### [红队新思路：利用Windows调试框架在.NET进程内直接调用.NET方法](/post/id/213892)

  2020-08-14 15:00:40
* ##### [如何利用COMPlus\_ETWEnabled隐藏.NET行为](/post/id/207843)

  2020-06-08 10:30:05

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