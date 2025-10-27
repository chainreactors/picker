---
title: Microsoft 在 11 月补丁星期二中解决了关键的零日漏洞
url: https://www.anquanke.com/post/id/301773
source: 安全客-有思想的安全新媒体
date: 2024-11-14
fetch_date: 2025-10-06T19:14:44.569459
---

# Microsoft 在 11 月补丁星期二中解决了关键的零日漏洞

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

# Microsoft 在 11 月补丁星期二中解决了关键的零日漏洞

阅读量**63233**

发布时间 : 2024-11-13 10:43:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/microsoft-addresses-critical-zero-day-vulnerabilities-in-november-patch-tuesday/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-43451]()

微软 11 月 2024 日发布的 “星期二补丁 ”解决了 92 个漏洞，其中包括 4 个关键漏洞和 83 个 “重要 ”漏洞。值得注意的是，此次发布的补丁包括针对四个在野外被积极利用的零日漏洞的补丁，强调了企业和用户立即采取行动的迫切需要。值得注意的修补程序涵盖了主要微软服务中的漏洞，包括 Azure Active Directory、Windows Kerberos、.NET 和 Visual Studio、SQL Server 和 Hyper-V。该版本还为 Microsoft SharePoint Server 提供了深度防御 (DiD) 更新，加强了基本漏洞修补之外的保护。

**零日漏洞需要立即关注**

在已处理的漏洞中，有四个漏洞因被积极利用而引人注目：

* **CVE-2024-43451（NTLM 哈希值披露欺骗漏洞）：** 该漏洞使攻击者有可能泄露用户的 NTLMv2 哈希值，为未经授权的身份验证提供便利。网络安全和基础设施安全局 (CISA) 已将此漏洞添加到已知漏洞目录中，要求联邦机构在 2024 年 12 月 3 日前打上补丁。
* **CVE-2024-49040（微软 Exchange 服务器欺骗漏洞）：** 虽然细节仍然有限，但任何影响 Exchange Server（企业通信的基石）的漏洞都值得立即关注。
* **CVE-2024-49019（Active Directory 证书服务权限提升漏洞）：** 利用此漏洞可授予攻击者域管理员权限，构成严重的安全风险。
* **CVE-2024-49039（Windows 任务调度程序权限提升漏洞）：** 该漏洞允许攻击者执行特权 RPC 功能，可能导致未经授权的系统访问。CISA 已将此漏洞列入已知漏洞目录，修补期限与 CVE-2024-43451 相同。

**已解决的关键漏洞**

除零点漏洞外，微软还修补了四个关键漏洞：

* **CVE-2024-43625（Microsoft Windows VMSwitch 权限提升漏洞）：** 成功利用漏洞可授予攻击者 SYSTEM 权限。
* **CVE-2024-43639（Windows Kerberos 远程代码执行漏洞）：** 此漏洞允许未经认证的攻击者远程执行代码，破坏系统完整性。
* **CVE-2024-49056（Airlift.microsoft.com 权限提升漏洞）：** 此漏洞允许攻击者在 airlift.microsoft.com 平台上提升权限。
* **CVE-2024-43498（.NET 和 Visual Studio 远程代码执行漏洞）：** 攻击者可利用此漏洞在有漏洞的 .NET 网络应用程序或桌面应用程序上远程执行代码。

**更多补丁亮点**

十一月补丁星期二还包括对各种组件漏洞的修复，其中包括

* **Windows 内核：** 解决了多个漏洞，包括权限提升 （CVE-2024-43630） 和拒绝服务 （CVE-2024-43642） 漏洞。
* **Windows NT 操作系统内核：** 权限提升漏洞 （CVE-2024-43623） 已修补。
* **Win32k：** 权限提升漏洞 （CVE-2024-43636） 已修补。
* **Microsoft Word：** 安全功能绕过漏洞 （CVE-2024-49033） 已修复。

**建议**

强烈建议组织和个人优先修补这些漏洞，以降低潜在风险。 鉴于某些漏洞的严重性和被积极利用的情况，立即采取行动对于维护系统安全性和完整性至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/microsoft-addresses-critical-zero-day-vulnerabilities-in-november-patch-tuesday/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301773](/post/id/301773)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/microsoft-addresses-critical-zero-day-vulnerabilities-in-november-patch-tuesday/)

如若转载,请注明出处： <https://securityonline.info/microsoft-addresses-critical-zero-day-vulnerabilities-in-november-patch-tuesday/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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