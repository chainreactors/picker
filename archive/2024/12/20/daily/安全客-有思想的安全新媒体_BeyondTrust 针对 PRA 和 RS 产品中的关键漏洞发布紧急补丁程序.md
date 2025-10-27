---
title: BeyondTrust 针对 PRA 和 RS 产品中的关键漏洞发布紧急补丁程序
url: https://www.anquanke.com/post/id/302846
source: 安全客-有思想的安全新媒体
date: 2024-12-20
fetch_date: 2025-10-06T19:35:54.079821
---

# BeyondTrust 针对 PRA 和 RS 产品中的关键漏洞发布紧急补丁程序

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

# BeyondTrust 针对 PRA 和 RS 产品中的关键漏洞发布紧急补丁程序

阅读量**82351**

|评论**1**

发布时间 : 2024-12-19 10:55:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/beyondtrust-issues-urgent-patch-for.html>

译文仅供参考，具体内容表达以及含义原文为准。

BeyondTrust 披露了特权远程访问（PRA）和远程支持（RS）产品中的一个关键安全漏洞，该漏洞可能导致执行任意命令。

特权远程访问可控制、管理和审计特权账户和凭证，为内部、外部和第三方用户访问内部部署和云资源提供零信任。远程支持允许服务台人员安全地连接到远程系统和移动设备。

该漏洞被追踪为 CVE-2024-12356（CVSS 得分：9.8），被描述为一个命令注入实例。

该公司在一份公告中说：“在特权远程访问（PRA）和远程支持（RS）产品中发现了一个关键漏洞，未经身份验证的攻击者可以注入以网站用户身份运行的命令。”

攻击者可以通过发送恶意客户端请求来利用该漏洞，从而在网站用户的上下文中执行任意操作系统。

该问题影响以下版本-

* 特权远程访问（24.3.1 及更早版本）- 已在 PRA 补丁 BT24-10-ONPREM1 或 BT24-10-ONPREM2 中修复
* 远程支持（24.3.1 及更早版本）- 已在 RS 修补程序 BT24-10-ONPREM1 或 BT24-10-ONPREM2 中修复

截至 2024 年 12 月 16 日，该漏洞的补丁已应用于云实例。如果没有订阅自动更新，建议使用内部部署版本软件的用户应用最新的修补程序。

BeyondTrust 表示：“如果客户使用的版本早于 22.1，则需要升级才能应用此补丁。”

该公司表示，这一缺陷是在 2024 年 12 月 2 日发生 “安全事故 ”后启动的持续取证调查中发现的，涉及 “数量有限的远程支持 SaaS 客户”。

BeyondTrust 说：“对远程支持 SaaS 问题进行的根本原因分析发现，远程支持 SaaS 的一个 API 密钥已被泄露。”BeyondTrust 补充说，它 “立即撤销了 API 密钥，通知了已知的受影响客户，并在当天暂停了这些实例，同时为这些客户提供了替代的远程支持 SaaS 实例。”

BeyondTrust 还表示，该公司仍在与一家未具名的 “网络安全和取证公司 ”合作，以确定此次漏洞的原因和影响。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/beyondtrust-issues-urgent-patch-for.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302846](/post/id/302846)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/beyondtrust-issues-urgent-patch-for.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/beyondtrust-issues-urgent-patch-for.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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