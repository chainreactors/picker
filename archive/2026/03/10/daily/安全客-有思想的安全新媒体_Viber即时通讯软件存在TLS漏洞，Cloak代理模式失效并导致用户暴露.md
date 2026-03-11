---
title: Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露
url: https://www.anquanke.com/post/id/315068
source: 安全客-有思想的安全新媒体
date: 2026-03-10
fetch_date: 2026-03-11T04:03:18.623011
---

# Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露

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

# Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露

阅读量**21563**

发布时间 : 2026-03-10 14:01:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Alex Lekander，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/viber-messenger-tls-flaw-breaks-cloak-proxy-mode-and-exposes-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

乐天 Viber 在代理混淆功能的实现中存在一处安全漏洞，该漏洞会导致**本应被隐藏的网络流量可被网络监控系统轻易识别**。

此缺陷会削弱应用绕过网络审查的能力，**可能导致在受限网络中 Viber 通信被直接封锁**。

该漏洞编号为 **CVE-2025-13476**，安全评级为**高危**，由 CERT 协调中心（CERT/CC）发布公告披露。公告显示，该问题影响：

* Android 版 Viber **25.7.2.0g**
* Windows 版 Viber **25.6.0.0 至 25.8.1.0**

  且仅在启用 **Cloak 代理模式**时生效。

  该漏洞由独立安全研究员 Oleksii Gaienko 上报。

该漏洞源于 Viber 在启用 Cloak 代理时**TLS 握手过程存在缺陷**。

Cloak 模式的设计目标是将代理或 VPN 流量伪装成普通浏览器 HTTPS 连接，从而隐藏代理行为。但 CERT/CC 发现，其实际实现会生成**固定且高度可预测的 TLS ClientHello 指纹**，扩展字段种类极少。

这导致其流量特征明显异于正常浏览器行为，**极易被识别**。

由于这一固定不变的指纹特征，网络运营商、政府机构及企业安全设备普遍使用的**深度包检测（DPI）系统**，可稳定识别出正在使用 Viber Cloak 代理模式的连接。

一旦被识别，相关流量可被精准封锁或限流，**使该功能绕过网络限制的设计目标完全失效**。

乐天 Viber 是由日本跨国科技与电商企业乐天集团旗下的主流即时通讯与 VoIP 平台，为全球数亿用户提供加密消息、音视频通话及群组通信服务。

在部分网络政策严格的地区，用户依赖 **Cloak 模式** 等代理配置来维持通讯服务的可用性。

CERT/CC 警告称，受影响用户会误以为流量已被隐藏，而实际并非如此，**应用本身不会提示混淆机制已失效**。

在对通讯软件存在严格过滤的环境中，该漏洞可让网络管理员或审查机构**快速检测并封锁 Viber 通信**，可能导致试图绕过限制的用户无法正常使用服务。

CERT/CC 建议用户将应用升级至已修复 TLS 握手实现的版本，具体要求如下：

* Windows：升级至 **Viber 27.3.0.0 或更高版本**
* Android：升级至 **Viber 27.2.0.0g 或更高版本**

同时建议 Windows 用户**开启自动更新**，确保后续能及时防御新的安全问题。

在完成系统更新前，**处于高审查环境下的用户应假定**：Cloak 代理流量可被网络监控工具识别并封锁，相关绕过行为可能暴露。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/viber-messenger-tls-flaw-breaks-cloak-proxy-mode-and-exposes-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315068](/post/id/315068)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/viber-messenger-tls-flaw-breaks-cloak-proxy-mode-and-exposes-users/)

如若转载,请注明出处： <https://cyberinsider.com/viber-messenger-tls-flaw-breaks-cloak-proxy-mode-and-exposes-users/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1070**

* 粉丝
* **6**

### TA的文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18

### 相关文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18
* ##### [黑客可利用间接提示注入攻击 借助外部内容操控AI智能体](/post/id/315071)

  2026-03-10 14:01:03
* ##### [海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单](/post/id/315077)

  2026-03-10 14:00:36

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