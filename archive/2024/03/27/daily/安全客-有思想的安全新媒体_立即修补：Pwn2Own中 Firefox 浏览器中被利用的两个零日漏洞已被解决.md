---
title: 立即修补：Pwn2Own中 Firefox 浏览器中被利用的两个零日漏洞已被解决
url: https://www.anquanke.com/post/id/294359
source: 安全客-有思想的安全新媒体
date: 2024-03-27
fetch_date: 2025-10-04T12:07:51.529413
---

# 立即修补：Pwn2Own中 Firefox 浏览器中被利用的两个零日漏洞已被解决

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

# 立即修补：Pwn2Own中 Firefox 浏览器中被利用的两个零日漏洞已被解决

阅读量**96539**

发布时间 : 2024-03-26 11:17:32

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/firefox-zero-days-pwn2own-patch-now/>

译文仅供参考，具体内容表达以及含义原文为准。

Mozilla 解决了最近在 2024 年 Pwn2Own 温哥华黑客大赛中 Firefox 网络浏览器中被利用的两个零日漏洞。

Pwn2Own 温哥华 2024 黑客竞赛于本周举行，趋势科技的零日计划 (ZDI) 透露，参赛者因展示29 个不同的零日而获得了 1,132,500 美元。

竞赛获胜者研究员 Manfred Paul (@\_manfp) 利用了两个关键漏洞，例如 CVE-2024-29944 和 CVE-2024-29943。

Manfred Paul (@\_manfp)通过使用 OOB Write (CVE-2024-29943) 进行 RCE 和暴露的危险函数错误 (CVE-2024-29944) 完成了 Mozilla Firefox沙箱逃逸。

除了 10 点 Pwn 大师积分外，他还额外获得了 100,000 美元，使他领先领先者 25 分。

最终，Manfred Paul 被授予 Pwn Master 称号。他总共赢得了 202,500 美元和 25 点积分。

已修复安全漏洞的详细信息

CVE-2024-29943：通过范围分析绕过进行越界访问

根据 Mozilla 的说法，攻击者可能会欺骗基于范围的边界检查消除，并对 JavaScript 对象执行越界读取或写入。

Firefox < 124.0.1 容易受到此攻击。

Mozilla 在其通报中表示，“攻击者能够通过欺骗基于范围的边界检查消除来对 JavaScript 对象执行越界读取或写入”。

CVE-2024-29944：通过事件处理程序执行特权 JavaScript

为了在父进程中启用任意 JavaScript 执行，攻击者能够将事件处理程序注入特权对象中。

该漏洞仅影响桌面版 Firefox；移动版本不受影响。

Mozilla 表示，“攻击者能够将事件处理程序注入特权对象，从而允许在父进程中执行任意 JavaScript”。

补丁发布

Mozilla发布了Firefox 124.0.1 和 Firefox ESR 115.9.1 来解决这两个安全问题。

这些缺陷凸显了保持严格的安全程序并在软件更新可用后立即应用它们的重要性。

通过更新到 Firefox 124.0.1，用户可以确保他们免受这些严重漏洞和任何相关风险的影响。

本文翻译自 [原文链接](https://cybersecuritynews.com/firefox-zero-days-pwn2own-patch-now/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294359](/post/id/294359)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/firefox-zero-days-pwn2own-patch-now/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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