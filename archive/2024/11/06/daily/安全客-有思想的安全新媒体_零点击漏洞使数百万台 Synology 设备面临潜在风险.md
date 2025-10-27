---
title: 零点击漏洞使数百万台 Synology 设备面临潜在风险
url: https://www.anquanke.com/post/id/301548
source: 安全客-有思想的安全新媒体
date: 2024-11-06
fetch_date: 2025-10-06T19:16:57.419698
---

# 零点击漏洞使数百万台 Synology 设备面临潜在风险

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

# 零点击漏洞使数百万台 Synology 设备面临潜在风险

阅读量**71561**

发布时间 : 2024-11-05 10:10:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 DEF-X

原文地址：[https://medium.com/@defxcyber/zero-click-flaw-exposes-potentially-millions-of-synology-devices-to-risk-c18e91fb688c](https://medium.com/%40defxcyber/zero-click-flaw-exposes-potentially-millions-of-synology-devices-to-risk-c18e91fb688c)

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络附加存储设备（NAS）制造商群晖科技（Synology）迅速解决了在最近的 Pwn2Own 黑客活动中发现的两个关键零日漏洞。这两个漏洞被命名为RISK:STATION，代号为CVE-2024-10443，由Midnight Blue安全研究员Rick de Jager在Synology Photos和BeeStation的BeePhotos软件中发现。

这些零点击漏洞在一台Synology BeeStation BST150-4T上进行了演示，允许远程攻击者通过root权限在易受攻击的、暴露在互联网上的NAS系统上执行代码。演示结束后，Synology 立即收到通知，并在 48 小时内发布了补丁程序以降低风险。午夜蓝 “强调，由于犯罪滥用的可能性很高，而且有数百万台设备可能受到影响，因此用户迫切需要应用这些更新。为了加强这种紧迫性，我们还发布了媒体公告，鼓励用户立即采取行动。

群暉科技提供下列更新以保障系統安全：

– BeePhotos for BeeStation OS 1.1： 更新至 1.1.0-10053 或更新版本
– BeePhotos for BeeStation OS 1.0：更新至版本 1.0.2 或更新版本： 更新至版本 1.0.2-10026 或更新版本
– Synology Photos 1.7 for DSM 7.2： 更新至版本 1.7.0-0795 或更新版本
– Synology Photos 1.6 for DSM 7.2：更新至版本 1.6.2 或更高版本： 更新至 1.6.2-0720 或更新版本

另一家著名的 NAS 供应商 QNAP 也在一周内发布了针对 Pwn2Own 上被利用的漏洞的补丁，特别是在其 SMB 服务和混合备份同步解决方案中。Synology 和 QNAP 都加快了修补程序的速度，尽管趋势科技的零日计划通常会给供应商分配 90 天的时间来进行全面披露。这种紧迫性反映了一个事实，即 NAS 设备通常被个人和组织用来存储敏感信息，而且经常暴露在互联网上供远程访问，因此成为网络犯罪分子的目标。攻击者经常利用弱密码和未修补的漏洞窃取或加密数据，然后向所有者勒索赎金。

在2024年爱尔兰Pwn2Own大会上展示了Synology零时差的Midnight Blue安全研究人员告诉网络安全记者Kim Zetter，他们在美国和欧洲警察部门以及韩国、意大利和加拿大的关键基础设施承包商的网络中发现了暴露的Synology NAS设备。

自2016年以来，eCh0raix (QNAPCrypt)等勒索软件就一直以这些系统为目标。近年来，攻击者越来越多地使用其他勒索软件类型（如 DeadBolt 和 Checkmate）以及各种漏洞来锁定暴露在互联网上的 NAS 设备并勒索赎金。

本文翻译自 [原文链接](https://medium.com/%40defxcyber/zero-click-flaw-exposes-potentially-millions-of-synology-devices-to-risk-c18e91fb688c)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301548](/post/id/301548)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： [https://medium.com/@defxcyber/zero-click-flaw-exposes-potentially-millions-of-synology-devices-to-risk-c18e91fb688c](https://medium.com/%40defxcyber/zero-click-flaw-exposes-potentially-millions-of-synology-devices-to-risk-c18e91fb688c)

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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