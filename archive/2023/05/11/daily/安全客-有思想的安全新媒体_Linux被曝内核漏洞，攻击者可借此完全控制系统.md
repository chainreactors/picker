---
title: Linux被曝内核漏洞，攻击者可借此完全控制系统
url: https://www.anquanke.com/post/id/288671
source: 安全客-有思想的安全新媒体
date: 2023-05-11
fetch_date: 2025-10-04T11:36:46.766247
---

# Linux被曝内核漏洞，攻击者可借此完全控制系统

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

# Linux被曝内核漏洞，攻击者可借此完全控制系统

阅读量**241058**

发布时间 : 2023-05-10 12:06:46

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

9日，Linux系统Netfilter框架被曝存在一个内核漏洞CVE-2023-32233。利用该漏洞，在本地访问Linux设备的攻击者，可在内核内存中执行任意读写，非特权本地用户可将特权提升到root级别，从而实现对系统进行完全控制。

Netfilter是一个内置于Linux内核中的数据包过滤和网络地址转换(NAT)框架，通过前端实用程序（例如 IPtables和UFW）进行管理。

安全专家称，该漏洞会影响多个Linux内核版本，包括当前的稳定版本v6.3.1。

工程师 Pablo Neira Ayuso提交了Linux内核 源代码提交来解决该问题，引入了两个函数来管理Netfilter nf\_tables子系统中匿名集的生命周期。

研究人员私下与Linux内核团队分享了他们的漏洞利用，以帮助他们开发修复程序，并提供了详细描述所采用的漏洞利用技术和PoC的源代码。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288671](/post/id/288671)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168535)

[安全客](/member.html?memberId=168535)

这个人太懒了，签名都懒得写一个

* 文章
* **122**

* 粉丝
* **0**

### TA的文章

* ##### [注册机内藏勒索软件！收款竟用支付宝？](/post/id/292743)

  2024-01-19 11:10:00
* ##### [全球首发！《2023年度统信UOS安全威胁防御报告》来了](/post/id/292263)

  2023-12-29 11:27:27
* ##### [数字安全“奥斯卡”落幕，ISC 2023创新百强重磅出炉](/post/id/292240)

  2023-12-29 10:24:44
* ##### [一个安全运营工程师的自白](/post/id/291372)

  2023-11-15 10:40:17
* ##### [打造实战型安全人才新高地，360发布ISC安全课SaaS化教培平台](/post/id/291209)

  2023-11-03 17:22:35

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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