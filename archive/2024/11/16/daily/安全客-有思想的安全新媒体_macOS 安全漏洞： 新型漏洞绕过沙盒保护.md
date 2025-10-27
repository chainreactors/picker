---
title: macOS 安全漏洞： 新型漏洞绕过沙盒保护
url: https://www.anquanke.com/post/id/301890
source: 安全客-有思想的安全新媒体
date: 2024-11-16
fetch_date: 2025-10-06T19:12:15.793742
---

# macOS 安全漏洞： 新型漏洞绕过沙盒保护

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

# macOS 安全漏洞： 新型漏洞绕过沙盒保护

阅读量**69511**

发布时间 : 2024-11-15 11:01:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/macos-security-compromised-novel-exploit-bypasses-sandbox-protections/>

译文仅供参考，具体内容表达以及含义原文为准。

![macOS security]()

macOS 中新发现的一个漏洞可能允许攻击者绕过关键安全机制，在未经授权的情况下访问敏感文件。独立安全研究人员 Mickey Jin 在 POC2024 会议上公布了这一发现。

Jin 的研究重点是利用 macOS 进程间通信（IPC）机制的弱点，特别是 XPC 服务。这些服务专为不同进程之间的通信而设计，已被发现存在漏洞，可被用来规避操作系统的沙盒保护。

**利用 XPC 服务突破安全屏障**

macOS 采用沙箱技术限制应用程序对系统资源和用户数据的访问，从而提高了系统的整体安全性。然而，Jin 的研究表明，某些 XPC 服务（尤其是驻留在系统框架内的服务）可以被操纵来逃避这些沙箱限制。研究人员发现了多个沙箱逃逸漏洞： CVE-2023-27944、CVE-2023-32414、CVE-2023-32404、CVE-2023-41077、CVE-2023-42961、CVE-2024-27864、CVE-2023-42977 等。

通过利用这些漏洞，恶意行为者可以获得更高的权限，有效绕过预期的安全限制。Jin 强调的一个显著例子是 “ShoveService”，利用该漏洞只需编写极少代码即可实现系统级命令执行。

**苹果的缓解措施和正在进行的研究**

苹果公司已对这些发现做出回应，发布了多个已发现漏洞的补丁。不过，Jin 的研究仍在进行中，因为一些漏洞，特别是与客户端权限验证不充分的 XPC 服务相关的漏洞，仍在调查之中。

在最近的 MacOS 版本（如 Ventura 和 Sonoma）中，苹果推出了几项安全增强措施，以减轻这些威胁：

* **强制 XPC 客户端授权：** 这可以确保只有经过授权的进程才能访问敏感的 XPC 服务。
* **限制访问易受攻击的服务：** 这限制了应用程序与可能被利用的服务之间的交互。
* **增强保护机制：** 这些保护措施可防止未经授权的命令被执行，从而加强系统安全性。

**增强安全性的建议**

强烈建议用户将 macOS 系统更新到最新版本，以便从最新的安全补丁中获益。此外，在下载和安装应用程序时，尤其是从不受信任的来源下载和安装应用程序时，务必要小心谨慎，这样才能最大限度地降低受威胁的风险。

本文翻译自securityonline [原文链接](https://securityonline.info/macos-security-compromised-novel-exploit-bypasses-sandbox-protections/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301890](/post/id/301890)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/macos-security-compromised-novel-exploit-bypasses-sandbox-protections/)

如若转载,请注明出处： <https://securityonline.info/macos-security-compromised-novel-exploit-bypasses-sandbox-protections/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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