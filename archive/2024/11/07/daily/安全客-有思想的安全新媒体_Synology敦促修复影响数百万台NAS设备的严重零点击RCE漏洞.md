---
title: Synology敦促修复影响数百万台NAS设备的严重零点击RCE漏洞
url: https://www.anquanke.com/post/id/301600
source: 安全客-有思想的安全新媒体
date: 2024-11-07
fetch_date: 2025-10-06T19:12:11.000377
---

# Synology敦促修复影响数百万台NAS设备的严重零点击RCE漏洞

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

# Synology敦促修复影响数百万台NAS设备的严重零点击RCE漏洞

阅读量**105462**

发布时间 : 2024-11-06 14:24:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html>

译文仅供参考，具体内容表达以及含义原文为准。

NAS设备制造商群晖（Synology）已经解决了影响DiskStation和BeePhotos的一个可能导致远程代码执行的关键安全漏洞。

这个零日漏洞被追踪为CVE-2024-10443，并被Midnight Blue称为RISK:STATION，由安全研究员Rick de Jager在Pwn2Own Ireland 2024黑客大赛上展示。

RISK:STATION是一个 “未经验证的零点击漏洞，允许攻击者在流行的群晖DiskStation和BeeStation NAS设备上执行root级代码，影响数百万台设备。

该漏洞的零点击性质意味着它不需要任何用户交互来触发利用，从而允许攻击者访问设备以窃取敏感数据并植入额外的恶意软件。

该漏洞影响以下版本

* BeePhotos for BeeStation OS 1.0（升级至 1.0.2-10026 或更高版本）
* 適用於 BeeStation OS 1.1 的 BeePhotos (升級至 1.1.0-10053 或以上版本)
* Synology Photos 1.6 for DSM 7.2 (升級至 1.6.2-0720 或以上)
* Synology Photos 1.7 for DSM 7.2 (升級至 1.7.0-0795 或以上版本)

为了让用户有足够的时间应用补丁，有关该漏洞的其他技术细节目前暂未公布。Midnight Blue表示，目前有100万到200万台Synology设备同时受到影响并暴露在互联网上。

**QNAP 修补了 3 个关键漏洞**

QNAP解决了影响QuRouter、SMB服务和HBS 3混合备份同步的三个关键漏洞，所有这些漏洞都在Pwn2Own中被利用。

* CVE-2024-50389 – 已在 QuRouter 2.4.5.032 及更新版本中修复
* CVE-2024-50387 – 已於 SMB Service 4.15.002 及 SMB Service h4.15.002 及更新版本中修復
* CVE-2024-50388 – 已在 HBS 3 Hybrid Backup Sync 25.1.1.673 及更新版本中修復

虽然没有证据表明上述任何漏洞已在野外被利用，但鉴于 NAS 设备过去一直是勒索软件攻击的高价值目标，建议用户尽快应用这些补丁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301600](/post/id/301600)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/synology-urges-patch-for-critical-zero.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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