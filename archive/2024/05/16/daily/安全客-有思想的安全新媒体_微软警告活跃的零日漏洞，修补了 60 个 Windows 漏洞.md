---
title: 微软警告活跃的零日漏洞，修补了 60 个 Windows 漏洞
url: https://www.anquanke.com/post/id/296518
source: 安全客-有思想的安全新媒体
date: 2024-05-16
fetch_date: 2025-10-06T17:13:48.865336
---

# 微软警告活跃的零日漏洞，修补了 60 个 Windows 漏洞

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

# 微软警告活跃的零日漏洞，修补了 60 个 Windows 漏洞

阅读量**78326**

发布时间 : 2024-05-15 12:03:19

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securityweek.com/microsoft-patches-60-windows-vulns-warns-of-active-zero-day-exploitation/>

译文仅供参考，具体内容表达以及含义原文为准。

微软周二推出了最新的安全更新，解决了各种软件产品中的大约 60 个漏洞，并呼吁紧急关注多个外部威胁追踪团队报告的一个被积极利用的零日漏洞。

标记为CVE-2024-30051的零日漏洞被记录为 Windows 桌面窗口管理器 (DWM) 核心库中基于堆的缓冲区溢出，该漏洞已在需要提升系统权限的恶意软件攻击中被利用。

该漏洞的 CVSS 严重性评分为 7.8/10，并且被 Redmond 评为“重要”。

微软称赞卡巴斯基、DBAPPSecurity 和谷歌威胁分析小组的安全研究人员发现并报告了该问题，表明该问题可能已经被用于定向攻击之外。

按照惯例，微软没有分享利用 IOC 来帮助防御者寻找入侵迹象的详细信息。

微软还将CVE-2024-30040标记为已被利用的类别，警告攻击者正在绕过 Microsoft 365 和 Office 中的安全功能。该漏洞的 CVSS 评分为 8.8，如果用户欺骗加载恶意文件，攻击者就可以执行任意代码。

“此漏洞绕过了 Microsoft 365 和 Microsoft Office 中的 OLE 缓解措施，这些缓解措施可保护用户免受易受攻击的 COM/OLE 控件的侵害。成功利用此漏洞的未经身份验证的攻击者可以通过说服用户打开恶意文档来获得代码执行权限，此时攻击者可以在用户的​​上下文中执行任意代码。”微软表示。

该公司还敦促 Windows 管理员关注CVE-2024-30044，这是 Microsoft Sharepoint 中的一个严重程度的远程代码执行漏洞。
雷德蒙德的安全响应中心警告说：“具有站点所有者权限的经过身份验证的攻击者可以利用该漏洞注入任意代码并在 SharePoint Server 上下文中执行此代码。”

“具有站点所有者或更高权限的经过身份验证的攻击者可以将特制文件上传到目标 Sharepoint Server，并制作专门的 API 请求来触发文件参数的反序列化。这将使攻击者能够在 Sharepoint Server 的上下文中执行远程代码。”微软补充道。

本文翻译自 [原文链接](https://www.securityweek.com/microsoft-patches-60-windows-vulns-warns-of-active-zero-day-exploitation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296518](/post/id/296518)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securityweek.com/microsoft-patches-60-windows-vulns-warns-of-active-zero-day-exploitation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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