---
title: SAP AI 核心漏洞导致客户数据面临网络攻击
url: https://www.anquanke.com/post/id/298107
source: 安全客-有思想的安全新媒体
date: 2024-07-20
fetch_date: 2025-10-06T17:42:28.196736
---

# SAP AI 核心漏洞导致客户数据面临网络攻击

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

# SAP AI 核心漏洞导致客户数据面临网络攻击

阅读量**87733**

发布时间 : 2024-07-19 11:39:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了SAP AI Core基于云的平台的安全缺陷，该平台用于创建和部署预测性人工智能（AI）工作流，这些工作流可用于获取访问令牌和客户数据。

这五个漏洞被云安全公司Wiz统称为**SAPwned**。

“我们发现的漏洞可能允许攻击者访问客户的数据并污染内部工件 – 传播到相关服务和其他客户的环境，”安全研究员Hillai Ben-Sasson在与The Hacker News分享的一份报告中说。

在 2024 年 1 月 25 日负责任地披露后，SAP 于 2024 年 5 月 15 日解决了这些弱点。

简而言之，这些漏洞使得未经授权访问客户的私有工件和对云环境（如亚马逊网络服务（AWS），Microsoft Azure和SAP HANA Cloud）的凭据成为可能。

它们还可用于修改 SAP 内部容器注册表上的 Docker 映像、Google 容器注册表上的 SAP Docker 映像以及 SAP 内部 Artifactory 服务器上托管的工件，从而导致对 SAP AI Core 服务的供应链攻击。

此外，通过利用 Helm 包管理器服务器同时暴露于读取和写入操作的事实，可以将访问权限武器化，以获得 SAP AI Core 的 Kubernetes 集群上的集群管理员权限。

“使用这个访问级别，攻击者可以直接访问其他客户的 Pod 并窃取敏感数据，例如模型、数据集和代码，”Ben-Sasson 解释说。“这种访问还允许攻击者干扰客户的 Pod，污染 AI 数据并操纵模型的推理。”

Wiz表示，之所以出现这些问题，是因为该平台使得在没有足够隔离和沙盒机制的情况下运行恶意AI模型和训练程序变得可行。

Ben-Sasson告诉The Hacker News：“Hugging Face、Replicate和SAP AI Core等AI服务提供商最近出现的安全漏洞凸显了其租户隔离和分段实施中的重大漏洞。 ”这些平台允许用户在共享环境中运行不受信任的AI模型和训练程序，从而增加了恶意用户访问其他用户数据的风险。

“与在租户隔离实践方面拥有丰富经验并使用虚拟机等强大隔离技术的资深云提供商不同，这些较新的服务通常缺乏这方面的知识，并且依赖于容器化，而容器化提供的安全性较弱。这凸显了提高对租户隔离重要性的认识的必要性，并推动人工智能服务行业加强其环境。

因此，威胁行为者可以在 SAP AI Core 上创建常规 AI 应用程序，绕过网络限制，并通过利用 AWS Elastic File System （EFS） 共享中的错误配置来探测 Kubernetes Pod 的内部网络以获取 AWS 令牌并访问客户代码和训练数据集。

“人们应该意识到，人工智能模型本质上是代码。在你自己的基础设施上运行人工智能模型时，你可能会面临潜在的供应链攻击，“Ben-Sasson说。

“仅运行来自受信任来源的受信任模型，并在外部模型和敏感基础设施之间适当分离。在使用 AI 服务提供商时，验证其租户隔离架构并确保他们应用最佳实践非常重要。

Netskope 透露，企业越来越多地使用生成式 AI 促使组织使用阻止控制、数据丢失防护 （DLP） 工具、实时指导和其他机制来降低风险。

该公司表示：“受监管的数据（组织有法律义务保护的数据）占与生成式人工智能（genAI）应用程序共享的敏感数据的三分之一以上，这给企业带来了代价高昂的数据泄露的潜在风险。

他们还关注一个名为 NullBulge 的新网络犯罪威胁组织的出现，该组织自 2024 年 4 月以来将目光投向了以 AI 和游戏为重点的实体，旨在窃取敏感数据并在地下论坛上出售受损的 OpenAI API 密钥，同时声称自己是“保护世界各地的艺术家”免受人工智能侵害的黑客行动主义团队。

SentinelOne安全研究员Jim Walter说：“NullBulge通过将GitHub和Hugging Face上公开可用的存储库中的代码武器化，导致受害者导入恶意库，或通过游戏和建模软件使用的mod包来攻击软件供应链。

“该小组使用AsyncRAT和XWorm等工具，然后交付使用泄露的LockBit Black构建器构建的LockBit有效载荷。像 NullBulge 这样的组织代表了低门槛勒索软件的持续威胁，以及信息窃取者感染的常青效应。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298107](/post/id/298107)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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