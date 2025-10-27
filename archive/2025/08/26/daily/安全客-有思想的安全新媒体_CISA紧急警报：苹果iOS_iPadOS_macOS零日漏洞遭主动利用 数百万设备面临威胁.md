---
title: CISA紧急警报：苹果iOS/iPadOS/macOS零日漏洞遭主动利用 数百万设备面临威胁
url: https://www.anquanke.com/post/id/311464
source: 安全客-有思想的安全新媒体
date: 2025-08-26
fetch_date: 2025-10-07T00:18:01.253273
---

# CISA紧急警报：苹果iOS/iPadOS/macOS零日漏洞遭主动利用 数百万设备面临威胁

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

# CISA紧急警报：苹果iOS/iPadOS/macOS零日漏洞遭主动利用 数百万设备面临威胁

阅读量**74600**

发布时间 : 2025-08-25 17:50:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Florence Nightingale，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apple-ios-ipados-and-macos-0-day-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）就影响苹果iOS、iPadOS和macOS操作系统的**关键零日漏洞**发布紧急警告，确认威胁分子正在积极利用该漏洞。该漏洞被追踪为**CVE-2025-43300**，已被列入CISA已知被利用漏洞（KEV）目录，标志着机构和个人用户需立即采取行动保护系统。

**核心警报**

1. 苹果设备中的CVE-2025-43300漏洞允许通过**恶意图像实现代码执行**
2. 威胁分子正积极针对**iOS、iPadOS和macOS系统**发起攻击
3. 必须立即安装苹果安全更新：**联邦机构修复截止日为2025年9月11日**

### **越界写入漏洞分析**

新披露的漏洞属于苹果Image I/O框架中的**越界写入缺陷**（CWE-787）。此类漏洞允许攻击者向分配内存缓冲区的预期边界之外写入数据，可能导致**任意代码执行**、系统崩溃或权限提升。

Image I/O框架负责处理苹果生态系统中的图像读写，因其广泛支持JPEG、PNG和HEIF等多种图像格式，使得该漏洞影响尤为严重。安全研究人员指出，通过**特制恶意图像文件**可触发该漏洞，使攻击者能够以受影响应用的权限执行任意代码。

该漏洞影响**多个苹果操作系统版本**，形成了覆盖企业和消费环境中iPhone、iPad和Mac电脑的广泛攻击面。

CISA于2025年8月21日将CVE-2025-43300纳入KEV目录，为所有联邦民事行政机构设定了**2025年9月11日的强制修复期限**。根据《具有约束力的操作指令22-01》（BOD 22-01），这些机构必须应用供应商提供的缓解措施，若补丁不可用则需停止使用受影响产品。

CISA的快速响应凸显了针对该漏洞的**利用尝试的严重性**。尽管尚未确定该漏洞是否被用于勒索软件活动，但CISA指南强调应将其视为需要网络安全防御团队立即处理的高优先级安全问题。

![]()

### **紧急修复要求**

苹果公司已发布安全更新，针对受影响平台修复该漏洞，并通过多份支持公告提供详细缓解指南。

鉴于该漏洞的零日威胁性质及已证实的野外利用情况，各组织应优先将这些补丁纳入其漏洞管理框架实施。

该漏洞被列入KEV目录（已知被利用漏洞清单），为网络安全专业人员制定基于风险的修复策略提供了关键依据。

网络防御人员应利用CISA（网络安全与基础设施安全局）权威漏洞情报提升威胁检测能力，确保全面覆盖针对苹果广泛部署的操作系统的已知攻击向量。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apple-ios-ipados-and-macos-0-day-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311464](/post/id/311464)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apple-ios-ipados-and-macos-0-day-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apple-ios-ipados-and-macos-0-day-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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