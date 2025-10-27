---
title: Confluence 新漏洞可能导致超过 20 万个数据中心实例被暴露
url: https://www.anquanke.com/post/id/296730
source: 安全客-有思想的安全新媒体
date: 2024-05-24
fetch_date: 2025-10-06T16:48:54.364199
---

# Confluence 新漏洞可能导致超过 20 万个数据中心实例被暴露

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

# Confluence 新漏洞可能导致超过 20 万个数据中心实例被暴露

阅读量**77851**

发布时间 : 2024-05-23 11:14:23

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/atlassian-confluence-server-exposed-instances/>

译文仅供参考，具体内容表达以及含义原文为准。

数十万个可能存在漏洞的 Atlassian Confluence 数据中心和 Confluence 服务器实例暴露给攻击者，其中大部分位于美国，并且攻击者可远程在其上运行代码。

最近在两款 Atlassian 产品中发现的漏洞允许攻击者对受影响的系统进行远程代码执行 (RCE) 攻击。

该 RCE 漏洞编号为 CVE-2024-21683，影响 Confluence 数据中心和 Confluence 服务器。

据 Cyber​​news 研究团队称，由于企业利用这些服务来帮助团队协同工作和共享信息，攻击者可以利用该漏洞渗透受影响的系统并获取数据。

该漏洞的 CVSS 评分为 8.3，允许经过身份验证的攻击者执行任意代码，这对机密性、完整性和可用性都有很大影响，并且不需要用户交互。

![暴露国家]()
**有多少 Atlassian 实例被暴露？**
虽然 Atlassian针对受影响的两项服务发布了修复程序，但团队发现数十万个易受攻击的实例暴露在互联网上，诱使威胁行为者采取行动。

Cyber​​news 研究人员发现，有 224,962 个数据中心和服务器实例被暴露。攻击者可以使用相同的工具来发现受影响的服务器，并利用最近发现的漏洞进行恶意攻击。

例如，研究人员声称攻击者可以利用该漏洞首次进入网络或环境。建立初始立足点后，攻击者可以完全控制系统，包括安装恶意软件、访问敏感数据和操纵系统配置的能力。

该团队表示：“受损的系统可以用作网络内进一步攻击的枢纽点。”

暴露的实例也会危及普通用户。研究人员认为，恶意行为者可以窃取登录凭据，这将使他们能够渗透 Atlassian 帐户以及重复使用相同凭据的其他帐户。

据该团队介绍，RCE 漏洞是高级勒索软件团伙经常使用的攻击媒介，以获取进入目标系统的初始入口点。

例如，去年，知名勒索软件集团 Cl0p 利用 Progress Software 的 MOVEit Transfer 软件中现已修复的零日漏洞，允许攻击者访问和下载存储在其中的数据。数千家组织和数千万人受到影响，造成数千万美元的损失。

根据Cyber​​news 的勒索软件监控工具Ransomlooker 的数据，平均赎金需求为 530 万美元，因此尽快修复任何具有 RCE 功能的错误至关重要。

**哪些国家受影响最严重？**
深入研究有关暴露的数据中心和服务器服务的信息后发现，只有五个国家托管了一半仍然易受攻击的实例。

该团队表示，美国可能存在的易受攻击实例数量最多，为 53,195 个。另外 22,007 个易受攻击的实例被追踪到日本。

与此同时，南非、法国和德国各自拥有超过 11,000 个暴露的未修补的 Confluence 服务。

该团队建议暴露于新型 RCE 漏洞的组织立即将 Atlassian Confluence Server 或 Data Center 升级到 Atlassian 推荐的最新版本。

Atlassian是一家澳大利亚裔美国软件巨头，为开发人员和管理人员提供产品。该公司拥有 10,000 多名员工，预计 2023 年收入将超过 35 亿美元。

项目管理平台Jira和企业软件Confluence是该公司的旗舰产品。

最近的漏洞并不是 Atlassian 产品第一次遇到严重漏洞。2022 年，对手和民族国家行为者利用RCE 漏洞影响了Atlassian 的 Confluence。

本文翻译自 [原文链接](https://cybernews.com/security/atlassian-confluence-server-exposed-instances/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296730](/post/id/296730)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/atlassian-confluence-server-exposed-instances/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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