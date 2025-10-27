---
title: SAP 修复 NetWeaver 应用服务器中的关键漏洞
url: https://www.anquanke.com/post/id/303549
source: 安全客-有思想的安全新媒体
date: 2025-01-17
fetch_date: 2025-10-06T20:07:08.159910
---

# SAP 修复 NetWeaver 应用服务器中的关键漏洞

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

# SAP 修复 NetWeaver 应用服务器中的关键漏洞

阅读量**67351**

发布时间 : 2025-01-16 10:00:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-netweaver-application-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

![SAP fixes critical vulnerabilities in NetWeaver application servers]()

SAP 修复了两个影响 NetWeaver Web 应用服务器的关键漏洞，这些漏洞可被利用来升级权限和访问受限信息。

作为一月份安全补丁日的一部分，供应商还发布了其他产品的更新，以修补另外 12 个被评为中度和高度严重的问题。

SAP 公司在安全公告中写道：“SAP 强烈建议客户访问支持门户网站，优先应用补丁程序，以保护他们的 SAP 系统。”

SAP 本月解决的四个最严重的安全问题概述如下：

* CVE-2025-0070，严重程度，9.9 分）： SAP NetWeaver Application Server for ABAP 和 ABAP Platform 中不正确的身份验证允许通过身份验证的攻击者利用不正确的身份验证检查，导致权限升级并严重影响保密性、完整性和可用性。
* CVE-2025-0066，严重程度，9.9 分：由于访问控制薄弱，SAP NetWeaver AS for ABAP 和 ABAP Platform（Internet Communication Framework）中存在信息披露漏洞，攻击者可访问受限信息，严重影响保密性、完整性和可用性。
* CVE-2025-0063，高度严重性，8.8 分： SAP NetWeaver AS ABAP 和 ABAP 平台中的 SQL 注入漏洞源于某些 RFC 功能模块缺乏授权检查。这允许拥有基本权限的攻击者入侵 Informix 数据库，导致完全丧失机密性、完整性和可用性。
* CVE-2025-0061，高度严重性，8.7 分： SAP BusinessObjects Business Intelligence Platform 中存在多个漏洞，由于存在信息披露问题，未经身份验证的攻击者可通过网络执行会话劫持。这使攻击者能够访问和修改所有应用程序数据。

**影响和建议**

SAP 产品服务于制造、金融、零售、医疗保健和政府等行业的大型企业，在管理业务运营和客户关系方面发挥着重要作用。

SAP NetWeaver 是运行 ABAP 应用程序并通过 Internet Communication Framework 实现安全通信的核心平台。企业的 IT 管理员、开发人员和顾问通常使用它来管理财务、人力资源和供应链方面的 ERP 系统。

SAP BusinessObjects 是一个报表、分析和数据可视化平台，供分析师、决策者和 IT 团队使用，以获得洞察力并支持战略决策。

过去，黑客曾以 SAP 产品为攻击目标，因为这些产品没有针对已知漏洞进行更新，或者配置不当，导致网络暴露在漏洞之下。

这家德国供应商强烈建议客户应用最新的补丁程序，以保护其 SAP 环境。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-netweaver-application-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303549](/post/id/303549)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-netweaver-application-servers/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-netweaver-application-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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