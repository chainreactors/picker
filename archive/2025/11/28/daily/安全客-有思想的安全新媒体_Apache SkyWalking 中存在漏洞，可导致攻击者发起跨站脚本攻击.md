---
title: Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击
url: https://www.anquanke.com/post/id/313482
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:18.977410
---

# Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击

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

# Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击

阅读量**23784**

发布时间 : 2025-11-28 18:07:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/apache-skywalking-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Apache SkyWalking（一款流行的应用性能监控工具）近期被发现存在一个漏洞，攻击者可利用该漏洞执行恶意脚本并发起 **跨站脚本（XSS）攻击**。

该漏洞编号为 **CVE-2025-54057**，影响所有版本的 SkyWalking，直至 10.2.0 版本。

![]()

### 漏洞概述

该漏洞属于“**存储型 XSS（跨站脚本）**”问题。这意味着攻击者可将恶意代码注入网页，当其他用户查看该网页时，代码会在其浏览器中执行。

这可能导致多种安全问题，包括窃取登录凭据和个人数据等敏感信息。

该漏洞的成因是网页中 **未正确过滤与脚本相关的 HTML 标签**，使得攻击者能够注入并存储恶意脚本。

此安全缺陷的严重性级别被评为“**重要**”。一旦被利用，攻击者可能 **未授权访问用户账户、冒充用户或篡改网站**。对于使用 Apache SkyWalking 监控其应用程序的组织而言，数据被盗的可能性是一个重大隐患。成功的攻击可能会危及整个应用程序及其数据。

Apache SkyWalking **10.2.0 及之前的所有版本** 均受此漏洞影响。SkyWalking 开发团队已在 10.3.0 版本中发布补丁。

强烈建议所有 Apache SkyWalking 用户 **立即升级到最新版本**，以保护其系统免受潜在攻击。升级到新版本是缓解此漏洞风险的唯一方法。

该漏洞由安全研究员 Vinh Nguyễn Quang 发现并报告。Apache 软件基金会接到通知后，开发并发布了修复程序。

此漏洞的披露凸显了开源社区在识别和解决安全问题方面的重要性。

本文翻译自gbhackers [原文链接](https://gbhackers.com/apache-skywalking-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313482](/post/id/313482)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/apache-skywalking-flaw/)

如若转载,请注明出处： <https://gbhackers.com/apache-skywalking-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **750**

* 粉丝
* **6**

### TA的文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22

### 相关文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22
* ##### [逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下](/post/id/313462)

  2025-11-28 18:02:37
* ##### [纳闽再保险启用绿色数据中心，实现效能提升与运营成本优化](/post/id/313459)

  2025-11-28 18:00:45
* ##### [遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态](/post/id/313453)

  2025-11-28 18:00:14

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