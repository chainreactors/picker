---
title: ToddyCat 利用 ESET 命令行扫描器漏洞部署恶意工具 TCESB，实施多阶段隐秘攻击
url: https://www.anquanke.com/post/id/306261
source: 安全客-有思想的安全新媒体
date: 2025-04-09
fetch_date: 2025-10-06T22:03:47.301407
---

# ToddyCat 利用 ESET 命令行扫描器漏洞部署恶意工具 TCESB，实施多阶段隐秘攻击

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

# ToddyCat 利用 ESET 命令行扫描器漏洞部署恶意工具 TCESB，实施多阶段隐秘攻击

阅读量**49765**

发布时间 : 2025-04-08 10:13:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/toddycat-attackers-exploited-eset-command-line-scanner-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

臭名昭著的 APT 组织 ToddyCat 使用复杂的攻击策略，通过利用 ESET 命令行扫描程序中的弱点，在目标系统中秘密部署恶意代码。

该漏洞现已被编号为 CVE-2024-11859，攻击者借助此漏洞，在受信任的安全解决方案环境内执行恶意负载，从而绕过安全监控工具。

2024 年初，调查人员在多个受感染设备的临时目录中发现了名为 “version.dll” 的可疑文件。

进一步分析表明，这些文件是一款名为 TCESB 的复杂工具的组成部分，专门用于绕过防护机制和监控工具。

此前，ToddyCat 的攻击手段中并未出现过这款工具。它利用了 ESET 命令行扫描器（ecls）在加载动态链接库（DLL）文件时存在的不安全漏洞。

ESET 将该漏洞登记为 CVE-2024-11859，并于 2025 年 1 月 21 日发布了补丁，同时在 4 月 4 日发布了安全公告。

### ****攻击链的技术分析****

卡巴斯基报告称，攻击者运用了一种名为 DLL 代理（在 MITRE ATT&CK 框架中分类为 T1574）的技术来执行其恶意代码。

TCESB 工具旨在导出合法 version.dll 文件的所有功能，但在后台运行恶意作时将调用重定向到原始 DLL。

该漏洞利用了 ESET 命令行扫描程序的不安全加载机制，该机制在查找系统目录之前在当前目录中搜索 version.dll 文件。

此漏洞允许加载恶意 DLL 而不是合法 DLL。

分析显示，TCESB 基于开源工具 EDRSandBlast 进行了修改，以扩展其功能。

该恶意软件能够修改 Windows 内核结构，从而禁用诸如进程创建等关键系统事件的通知程序。

### ****增强隐身能力****

为增强其隐身能力，TCESB 采用了自带易受攻击驱动程序（BYOVD）技术（T1211），特别是使用存在 CVE-2021-36276 漏洞的 Dell DBUtilDrv2.sys 驱动程序。这使得攻击者能够在内核层面执行特权操作。

### ****有效负载执行机制****

该工具实施了一套复杂的有效负载执行系统，每两秒检查一次当前目录中是否存在名为 “kesp” 或 “ecore” 的特定文件。

一旦检测到这些文件，就会使用 AES-128 加密算法对其进行解密，解密密钥存储在有效负载文件的前 32 字节中。

这种多阶段的攻击方式体现了 ToddyCat 成熟的运营安全策略。他们构建了一个系统，只有在确认初始渗透成功后，才会部署有效负载。

安全专家建议对涉及已知漏洞驱动程序的安装事件进行系统监控。

像 loldrivers 项目这样的资源有助于识别此类驱动程序。此外，各组织应监控 Windows 内核调试符号加载事件，特别是在那些预计不会进行内核调试的设备上。

这一事件凸显了高级威胁行为者不断演变的攻击策略，他们持续寻找新方法来利用受信任的软件，甚至是安全解决方案本身，以持续且隐蔽地访问目标系统。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/toddycat-attackers-exploited-eset-command-line-scanner-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306261](/post/id/306261)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/toddycat-attackers-exploited-eset-command-line-scanner-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/toddycat-attackers-exploited-eset-command-line-scanner-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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