---
title: BeyondTrust 利用 Postgresql 零日SQL注入漏洞进行攻击
url: https://www.anquanke.com/post/id/304326
source: 安全客-有思想的安全新媒体
date: 2025-02-15
fetch_date: 2025-10-06T20:33:03.232109
---

# BeyondTrust 利用 Postgresql 零日SQL注入漏洞进行攻击

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

# BeyondTrust 利用 Postgresql 零日SQL注入漏洞进行攻击

阅读量**95299**

发布时间 : 2025-02-14 15:38:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/postgresql-vulnerability-exploited.html>

译文仅供参考，具体内容表达以及含义原文为准。

根据 Rapid7 的调查结果，2024 年 12 月利用 BeyondTrust 特权远程访问（PRA）和远程支持（RS）产品中的零日漏洞的威胁行为者，很可能还利用了 PostgreSQL 中此前未知的 SQL 注入漏洞。

这个被追踪为 CVE-2025-1094（通用漏洞评分系统（CVSS）评分为 8.1）的漏洞，影响了 PostgreSQL 交互式工具 psql。

安全研究员斯蒂芬・富尔（Stephen Fewer）表示：“能够通过 CVE-2025-1094 实现 SQL 注入的攻击者，随后可以利用该交互式工具运行元命令的能力来实现任意代码执行（ACE）。”

这家网络安全公司进一步指出，他们是在对 CVE-2024-12356 进行调查时发现了这一情况，CVE-2024-12356 是 BeyondTrust 软件中最近已修复的一个安全漏洞，该漏洞允许未经身份验证的远程代码执行。

具体来说，该公司发现 “要成功利用 CVE-2024-12356 漏洞，必须包含对 CVE-2025-1094 漏洞的利用，才能实现远程代码执行”。

在一次协调披露中，PostgreSQL 的维护者发布了一个更新，以修复以下版本中的问题：

1.PostgreSQL 17（在 17.3 版本中修复）

2.PostgreSQL 16（在 16.7 版本中修复）

3.PostgreSQL 15（在 15.11 版本中修复）

4.PostgreSQL 14（在 14.16 版本中修复）

5.PostgreSQL 13（在 13.19 版本中修复）

该漏洞源于 PostgreSQL 处理无效 UTF-8 字符的方式，从而为攻击者利用快捷命令 “!” 进行 SQL 注入打开了方便之门，该命令可用于执行 shell 命令。

富尔说：“攻击者可以利用 CVE-2025-1094 来执行这个元命令，从而控制所执行的操作系统 shell 命令。或者，能够通过 CVE-2025-1094 实现 SQL 注入的攻击者，可以执行由攻击者任意控制的 SQL 语句。”

与此同时，美国网络安全与基础设施安全局（CISA）将一个影响 SimpleHelp 远程支持软件的安全漏洞（CVE-2024-57727，CVSS 评分为 7.5）列入了已知被利用漏洞（KEV）目录，要求联邦机构在 2025 年 3 月 6 日前应用修复程序。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/postgresql-vulnerability-exploited.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304326](/post/id/304326)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/postgresql-vulnerability-exploited.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/postgresql-vulnerability-exploited.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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