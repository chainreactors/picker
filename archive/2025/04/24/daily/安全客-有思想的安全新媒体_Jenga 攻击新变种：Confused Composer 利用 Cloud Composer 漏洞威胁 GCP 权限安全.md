---
title: Jenga 攻击新变种：Confused Composer 利用 Cloud Composer 漏洞威胁 GCP 权限安全
url: https://www.anquanke.com/post/id/306790
source: 安全客-有思想的安全新媒体
date: 2025-04-24
fetch_date: 2025-10-06T22:04:26.596796
---

# Jenga 攻击新变种：Confused Composer 利用 Cloud Composer 漏洞威胁 GCP 权限安全

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

# Jenga 攻击新变种：Confused Composer 利用 Cloud Composer 漏洞威胁 GCP 权限安全

阅读量**48961**

发布时间 : 2025-04-23 10:17:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/confusedcomposer-gcp-composer-vulnerability-allows-privilege-escalation/>

译文仅供参考，具体内容表达以及含义原文为准。

![GCP Composer Privilege Escalation]()

Tenable Research 发现了Google Cloud Platform（GCP）中一个现已修复的权限提升漏洞，该漏洞被称为 “Confused Composer”。此漏洞存在于 Cloud Composer 中，原本可能会让攻击者提升自己的权限。

核心问题在于，拥有 composer.environments.update 权限的身份可以编辑 Cloud Composer 环境，从而获取更高的权限。这种权限提升的目标是默认的 Cloud Build 服务账号。报告强调了该账号所拥有的重要权限，并指出它 “包括对 Cloud Build 本身的权限，以及对 Cloud Storage、Artifact Registry 等的权限”。

要理解这个漏洞，了解 Cloud Composer 和 Cloud Build 是什么非常重要。

Cloud Composer 是 Google Cloud Platform 中的一项托管工作流编排服务，基于 Apache Airflow，用于调度和自动化数据管道。

Cloud Build 是 Google Cloud Platform 中的一项托管持续集成与持续交付（CI/CD）服务，用于构建、测试和部署应用程序及容器。

该报告突出了这些服务之间的相互关系：“Cloud Composer 使用 Cloud Build 来构建软件包，而这恰恰是攻击者可能会滥用流程以提升权限的地方。”

Cloud Composer 允许用户安装自定义的 Python 包索引（PyPI）软件包。该漏洞源于在这个过程中 Composer 与 Cloud Build 之间的交互方式。

以下是攻击途径的概述：

1.用户指定一个自定义的 PyPI 软件包。

2.Composer 启动一个构建过程，并自动配置一个 Cloud Build 实例。

3.这个实例关联到默认的 Cloud Build 服务账号，该账号拥有广泛的权限。

拥有 composer.environments.update 权限的攻击者可以向 Composer 配置中注入恶意的 PyPI 软件包。

攻击者会将他们的恶意软件包添加到 Composer 中。Cloud Build 使用 Pip 来安装这个软件包。报告指出了一个关键细节：“事实证明，Pip 会自动运行软件包安装前和安装后的脚本。”

这使得攻击者能够在 Cloud Build 环境中执行任意代码。然后攻击者可以注入代码来访问 Cloud Build 的元数据 API。由于构建实例使用的是默认的 Cloud Build 服务账号，攻击者可以提取其令牌，并获得对一个高权限服务账号的控制权。

该报告强调了这个漏洞的严重性：“这种攻击特别危险，因为攻击者不需要直接访问 Composer 的服务账号或 Cloud Build 的服务账号，只需要具备更新 Composer 环境的能力即可。” 报告还阐明 “从默认的 Cloud Build 服务账号手中完全掌控项目是完全可行的”。

Google Cloud Platform 已经修复了这个漏洞。此前，“在执行 PyPI 模块安装的更新操作期间，Composer 使用的是 Cloud Build 服务账号”。现在，Composer 在进行这些安装时使用的是 Composer环境服务账号。

这个修复措施已经应用到新的 Composer 实例上，现有的实例计划在 2025 年 4 月前完成更新。

Google Cloud Platform 还更新了Composer 的文档，包括访问控制、安装 Python 依赖项以及访问 Airflow CLI等部分。

Tenable Research 指出，ConfusedComposer 是一类更广泛的攻击类型Jenga的一部分。这类攻击是 “混淆函数（Confused Function）” 漏洞的一个变种，并且 “利用了云服务权限方面那些有点隐蔽的云提供商配置错误，从而将权限提升到超出预期的访问级别”。

本文翻译自securityonline [原文链接](https://securityonline.info/confusedcomposer-gcp-composer-vulnerability-allows-privilege-escalation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306790](/post/id/306790)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/confusedcomposer-gcp-composer-vulnerability-allows-privilege-escalation/)

如若转载,请注明出处： <https://securityonline.info/confusedcomposer-gcp-composer-vulnerability-allows-privilege-escalation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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