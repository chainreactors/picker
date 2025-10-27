---
title: GE 超声设备漏洞百出，容易遭受勒索软件和数据盗窃
url: https://www.anquanke.com/post/id/296586
source: 安全客-有思想的安全新媒体
date: 2024-05-18
fetch_date: 2025-10-06T16:48:24.871383
---

# GE 超声设备漏洞百出，容易遭受勒索软件和数据盗窃

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

# GE 超声设备漏洞百出，容易遭受勒索软件和数据盗窃

阅读量**113734**

发布时间 : 2024-05-17 11:41:54

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/vulnerabilities-threats/ge-ultrasound-gear-riddled-with-bugs-open-to-ransomware-data-theft>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员在 GE HealthCare 的 Vivid Ultrasound 系列产品以及两个相关软件程序中发现了 11 个安全漏洞。

问题多种多样，包括敏感数据缺少加密、使用硬编码凭据等等。 CVSS 3.1 评分系统的严重程度从 5.7 到 9.6 不等。

正如 Nozomi Networks在其报告中所解释的那样，这些错误可能会导致具有完全权限的远程代码执行 (RCE) 以及此类权限可能带来的任何数量的攻击场景。然而，最严重的情况还需要物理访问相关设备，从而大大降低医疗机构的潜在风险。

然而，“即使在谈论确实需要物理访问才能被利用的漏洞时，我们也认为攻击的可能性也远不能忽略不计，”Nozomi Networks 的高级安全研究员 Andrea Palanca 警告说。 “事实上，超声波机用于外部人员经常访问的医院和诊所，而我们的研究表明，只需一分钟的物理访问就足以执行攻击。因此，我们认为不仅是恶意的内部人员，但外人也可能有机会完成攻击。”

**坏消息**
在研究过程中，Nozomi 的研究人员分析了 GE 的三款产品：Vivid T9 超声系统，主要用于心脏成像；其预装的 Common Service Desktop Web 应用程序，用于各种管理目的；以及 EchoPAC 临床软件包，医生用它来查看和分析超声图像。

在某些方面，GE 的超声波设备旨在防止用户造成安全问题。例如，公共服务桌面Web应用仅暴露在设备的localhost接口上，防止远程篡改。这很重要，因为管理员使用该软件来执行更改密码和收集日志等操作。

然而，其他安全设计元素却没有那么有效。

Vivid T9 本质上是一台运行 GE 定制版本 Windows 10 的完整 PC。为了将其重点用于医疗保健环境，大部分设备逻辑由其上运行的应用程序和脚本处理。例如，它的图形用户界面 (GUI) 限制用户访问底层操作系统功能，但有一些例外。

然而，由于系统中的一个老错误——CVE-2020-6977，一个 CVSS 8.4 级的 kiosk 突破漏洞——研究人员能够绕过 GUI 进入 PC 并获得管理权限。然后，利用 Common Service Desktop 中严重性为 8.4 的命令注入问题 CVE-2024-1628，他们能够执行任意代码，投放导致机器冻结的勒索软件。

事实证明，只要启用了该程序的“共享”功能，利用 EchoPAC 就更加简单。通过连接到医生的工作站，攻击者可以滥用硬编码凭据（CVE-2024-27107、关键 9.6 CVSS）来访问其实时数据库服务器实例。在那里，他们可以读取、编辑和窃取患者数据。

**好消息**
问题在于，与物联网 (IoT) 连接的医疗设备不同，利用 T9 和通用服务桌面需要恶意内部人员能够物理访问设备的嵌入式键盘和触控板。（而 EchoPAC 更容易入侵，只需要在局域网中立足，不需要任何其他凭证。）

这对于医疗机构来说是个好消息，但有一点需要注意。攻击者可以通过将恶意驱动器插入 T9 暴露的 USB 端口来避免所有必要的点击和键入。在实验中，Nozomi 展示了特制驱动器如何在一分钟内破坏 T9。

帕兰卡说：“考虑到利用这些漏洞可能造成的重大影响，并且我们已经实际证明了这一点，我们希望我们的研究结果能够激励越来越多的供应商尽早采取更强有力的安全措施。”

GE HealthCare 的产品安全门户提供所有 11 个漏洞的补丁和缓解措施。

本文翻译自 [原文链接](https://www.darkreading.com/vulnerabilities-threats/ge-ultrasound-gear-riddled-with-bugs-open-to-ransomware-data-theft)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296586](/post/id/296586)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/ge-ultrasound-gear-riddled-with-bugs-open-to-ransomware-data-theft>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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