---
title: 在线视频下载器Dirpy 泄露用户数据，包括露骨内容
url: https://www.anquanke.com/post/id/296790
source: 安全客-有思想的安全新媒体
date: 2024-05-25
fetch_date: 2025-10-06T17:17:07.742367
---

# 在线视频下载器Dirpy 泄露用户数据，包括露骨内容

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

# 在线视频下载器Dirpy 泄露用户数据，包括露骨内容

阅读量**153288**

发布时间 : 2024-05-24 12:05:28

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/online-video-downloader-dirpy-data-leak/>

译文仅供参考，具体内容表达以及含义原文为准。

Dirpy 系统配置错误，导致用户的 IP 地址和下载内容被泄露，其中包括露骨内容。

3 月 24 日，Cyber​​news 研究团队发现了一个属于在线视频下载器 Dirpy 的开放 Kibana 实例。Dirpy 的最大用户群在日本和美国，它提供的在线视频下载服务主要用于 YouTube 和成人网站。

由于存在许多服务提供商，因此此类平台的法律地位仍处于灰色地带。虽然未经版权所有者许可从 YouTube 或其他平台下载视频通常是违法的，但出于个人非商业用途下载视频仍然是合法的。

尽管这项服务的合法性值得怀疑，但在线视频下载的需求量仍然巨大。仅 Dirpy 的平台每月就有 200 万访问者，这意味着不良的网络安全措施可能会影响大量个人。

Cyber​​news 研究团队发现，Dirpy 视频下载器未能在其 Kibana 上正确设置身份验证，导致包含 1570 万条私人数据的日志泄露。

**泄露的数据包括：**

* 用户 IP 地址
* 高级用户帐户 ID
* 包含下载内容的活动日志，包括露骨内容
* 请求内容的 URL
* 用户诊断信息

![活动日志显示用户正在下载露骨内容]()

活动日志显示用户正在下载 NSFW 内容

Kibana 是一款开源数据可视化工具，用于创建交互式仪表板。它提供强大的搜索和查询功能，支持实时数据监控并生成报告。

Kibana 的这些特性导致 Dirpy 的用户数据实时泄露，直到实例关闭。在团队与该公司联系后，实例的访问才得到保障。研究显示，Dirpy 的数据从 2024 年 3 月 18 日到 4 月 24 日都可用。

一旦 Kibana 实例暴露在互联网上且未通过身份验证保护，任何人都可以访问它，包括威胁行为者，他们可以轻松地将泄露的数据用于恶意目的。

![活动日志扩展以显示用户 IP 和诊断信息]()
活动日志扩展以显示用户 IP 和诊断信息

**露骨内容下载日志被泄露**
此次泄密事件引起了人们的极大担忧，因为它暴露了下载视频的日志，包括与下载内容相关的用户 IP 地址。下载内容中很大一部分来自成人网站，泄露了用户的敏感信息，例如他们的性取向、习惯和兴趣。

由于该服务的免费版本可供任何人使用，无需创建账户，因此此次泄露的影响有所减弱。但是，无论有没有账户，IP 地址都已暴露，构成风险。IP 可能用于识别用户，以及粗略位置，在某些情况下，还可以识别精确位置。

此次泄密事件再次提醒我们，使用在线服务时必须谨慎。互联网上的每一个行为都会留下痕迹。强烈建议使用 VPN 或安全代理服务，因为它可以消除网络地址与个人身份信息之间的联系。

![肮脏的日志]()
Dirpy 泄露的活动日志

本文翻译自 [原文链接](https://cybernews.com/security/online-video-downloader-dirpy-data-leak/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296790](/post/id/296790)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/online-video-downloader-dirpy-data-leak/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [德克萨斯州交通部 (TxDOT) 数据泄露事件暴露了 30 万份车祸报告](/post/id/308355)

  2025-06-11 16:33:57
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [美国电话电报公司（AT&T）再次遭遇大规模身份数据泄露事件](/post/id/308193)

  2025-06-06 15:22:45
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光](/post/id/304864)

  2025-02-28 15:37:26

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