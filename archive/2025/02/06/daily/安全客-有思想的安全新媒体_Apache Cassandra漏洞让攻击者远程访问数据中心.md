---
title: Apache Cassandra漏洞让攻击者远程访问数据中心
url: https://www.anquanke.com/post/id/303823
source: 安全客-有思想的安全新媒体
date: 2025-02-06
fetch_date: 2025-10-06T20:34:33.310021
---

# Apache Cassandra漏洞让攻击者远程访问数据中心

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

# Apache Cassandra漏洞让攻击者远程访问数据中心

阅读量**292650**

发布时间 : 2025-02-05 15:02:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-cassandra-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

在广泛使用的分布式数据库系统 Apache Cassandra 中，发现了一个新的安全漏洞，编号为 CVE – 2025 – 24860。

该漏洞涉及授权绕过问题，当使用特定的授权器配置时，可能使用户未经授权访问数据中心或网络区域。

此外，权限受限的用户可以通过数据控制语言（DCL）语句提升自身权限。建议运维人员检查访问规则是否存在违规情况，并升级到已修复版本 4.0.16、4.1.8 或 5.0.3 以解决该问题。

### SIEM 即服务

该漏洞影响以下版本的 Apache Cassandra：

* 4.0.0 至 4.0.15
* 4.1.0 至 4.1.7
* 5.0.0 至 5.0.2

此问题源于 Cassandra 网络授权器（CassandraNetworkAuthorizer）和 Cassandra CIDR 授权器（CassandraCIDRAuthorizer）中的授权错误漏洞。这些组件旨在根据用户权限限制对特定数据中心或 IP/CIDR 组的访问。

然而，由于该漏洞，权限受限的用户有可能通过 DCL 语句更新自身权限，从而绕过这些访问控制。

此漏洞影响：

* 4.0.0 – 4.0.15 版本以及 4.1.0 – 4.1.7 版本中的 Cassandra 网络授权器
* 5.0.0 – 5.0.2 版本中的 Cassandra 网络授权器和 Cassandra CIDR 授权器

强烈敦促使用受影响授权器的运维人员检查其数据访问规则，查看是否因该漏洞导致潜在违规情况。为降低风险，用户应升级到以下已修复的 Apache Cassandra 版本：4.0.16、4.1.8、5.0.3。

这些更新修复了该漏洞并恢复了正常的授权控制。

该问题由斯特凡・米克洛索维奇（Stefan Miklosovic）报告，已由 Apache Cassandra 开发团队处理。

如需更多详细信息，可访问 Apache Cassandra 官方网站或查阅[cve.org](https://cve.org/)上的 CVE 记录。

这一发现凸显了定期进行安全审计和及时更新的重要性，以确保像 Apache Cassandra 这样的分布式数据库系统在生产环境中的完整性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-cassandra-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303823](/post/id/303823)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-cassandra-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-cassandra-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Stealth Falcon 在复杂的网络间谍活动中利用新的零日漏洞 (CVE-2025-33053)](/post/id/308352)

  2025-06-11 16:12:52

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