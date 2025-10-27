---
title: GitHub 上的假冒 LDAPNightmware 利用程序传播信息窃取型恶意软件
url: https://www.anquanke.com/post/id/303447
source: 安全客-有思想的安全新媒体
date: 2025-01-14
fetch_date: 2025-10-06T20:04:37.580927
---

# GitHub 上的假冒 LDAPNightmware 利用程序传播信息窃取型恶意软件

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

# GitHub 上的假冒 LDAPNightmware 利用程序传播信息窃取型恶意软件

阅读量**67234**

发布时间 : 2025-01-13 11:22:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/fake-ldapnightmware-exploit-on-github-spreads-infostealer-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Hacker]()

GitHub 上的一个针对 CVE-2024-49113（又名 “LDAPNightmare”）的欺骗性概念验证（PoC）漏洞利用程序会让用户感染信息窃取恶意软件，从而将敏感数据外泄到外部 FTP 服务器。

这种策略并不新奇，因为在 GitHub 上已经有多个恶意工具伪装成 PoC 漏洞利用的记录案例。

然而，趋势科技发现的这一案例突出表明，威胁行为者仍在使用这种策略诱骗毫无戒心的用户感染恶意软件。

![Malicious repository on GitHub]()

**GitHub 上的恶意软件库**
来源：Trend Micro 趋势科技

**欺骗性利用**

趋势科技报告称，恶意 GitHub 仓库包含一个似乎是从 SafeBreach Labs 于 2025 年 1 月 1 日发布的 CVE-2024-49113 合法 PoC 中分叉出来的项目。

该漏洞是影响 Windows 轻量级目录访问协议（LDAP）的两个漏洞之一，微软在 2024 年 12 月的 “星期二补丁 ”中对其进行了修复，另一个漏洞是严重的远程代码执行（RCE）问题，被追踪为 CVE-2024-49112。

SafeBreach最初发布的关于PoC的博文错误地提到了CVE-2024-49112，而他们的PoC是针对CVE-2024-49113的，后者是一个严重性较低的拒绝服务漏洞。

这个错误即使后来得到了纠正，也引起了更多人对 LDAPNightmare 及其潜在攻击的兴趣和讨论，这可能正是威胁行为者试图利用的。

从恶意软件库下载 PoC 的用户会得到一个包含 UPX 的可执行文件 “poc.exe”，执行后会在受害者的 %Temp% 文件夹中投放一个 PowerShell 脚本。

该脚本会在被入侵系统上创建一个计划任务，执行一个从 Pastebin 获取第三个脚本的编码脚本。

这个最终有效载荷会收集计算机信息、进程列表、目录列表、IP 地址和网络适配器信息以及已安装的更新，并使用硬编码凭据将它们以 ZIP 压缩包的形式上传到外部 FTP 服务器。

![Stealing data from the infected system]()

从受感染系统中窃取数据
来源：趋势科技

该攻击的危害指标列表可在此处找到。

GitHub 用户为研究或测试而获取公开漏洞时需要谨慎，最好只信任声誉良好的网络安全公司和研究人员。

威胁行为者过去曾试图假冒知名安全研究人员，因此验证资源库的真实性也至关重要。

如果可能，在系统上执行代码之前先审查代码，将二进制文件上传到 VirusTotal，并跳过任何看起来被混淆的代码。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/fake-ldapnightmware-exploit-on-github-spreads-infostealer-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303447](/post/id/303447)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/fake-ldapnightmware-exploit-on-github-spreads-infostealer-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/fake-ldapnightmware-exploit-on-github-spreads-infostealer-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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