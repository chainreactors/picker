---
title: Postman Workspaces 泄露 30000 个 API 密钥和敏感令牌
url: https://www.anquanke.com/post/id/302988
source: 安全客-有思想的安全新媒体
date: 2024-12-26
fetch_date: 2025-10-06T19:36:16.110119
---

# Postman Workspaces 泄露 30000 个 API 密钥和敏感令牌

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

# Postman Workspaces 泄露 30000 个 API 密钥和敏感令牌

阅读量**73583**

|评论**1**

发布时间 : 2024-12-25 10:45:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/postman-workspaces-leak-api-keys-sensitive-tokens/>

译文仅供参考，具体内容表达以及含义原文为准。

**摘要**

* **30,000 个公共工作区被暴露：** CloudSEK 发现 Postman 工作区存在大量数据泄露。
* **存在风险的敏感数据：**泄漏的数据包括 API 密钥、令牌和管理员凭证。
* **受影响的主要平台：** 受影响的服务包括 GitHub、Slack 和 Salesforce。
* **主要原因：** 错误配置访问、明文存储和公开共享集合。
* **缓解步骤：** 使用环境变量、轮换令牌并采用秘密管理工具。

2024 年 12 月 23 日，CloudSEK 的 TRIAD 团队从滥用 Postman Workspaces（一种流行的基于云的 API 开发和测试平台）中发现了关键安全漏洞和风险。

在长达一年的调查中，研究人员发现超过30,000个可公开访问的工作区泄露了有关第三方API的敏感信息，包括访问令牌、刷新令牌和第三方API密钥，给企业和个人带来了严重风险。

![Postman Workspaces Leak 30000 API Keys and Sensitive Tokens]()
通过 CloudSec

根据该公司与 Hackread.com 共享的报告，泄露的数据涉及各行各业的组织，从小型企业到大型企业，影响到 GitHub、Slack 和 Salesforce 等主要平台。受影响的关键行业包括医疗保健、运动服装和金融服务，使企业面临众多威胁和安全风险。

研究人员指出，导致这些数据泄漏的常见做法包括无意中共享 Postman 集合、错误配置访问控制、与可公开访问的存储库同步，以及未加密的明文存储敏感数据。

这些漏洞可能导致严重后果。泄露的数据包括管理员凭据、支付处理 API 密钥和对内部系统的访问权限，会给受影响的组织造成财务和声誉损失。

Postman 中的敏感数据泄露会给个人开发者和整个组织带来严重后果。据报道，api.github.com、slack.com 和 hooks.slack.com 等顶级 API 服务暴露的秘密最多。Salesforce.com、login.microsoftonline.com 和 graph.facebook.com 等知名服务也被曝光。

![Postman Workspaces Leak 30000 API Keys and Sensitive Tokens]()
泄漏的 ZenDesk 凭证和泄漏的 Razorpay API 密钥（Via CloudSec）

泄漏的 API 密钥或访问令牌可让攻击者直接访问关键系统和数据，从而可能导致数据泄露、未经授权的系统访问以及网络钓鱼和社交工程攻击的增加。

Postman 经常存储 API 密钥、机密和 PII 等敏感信息，用于与 API 进行身份验证和通信。为确保数据安全，企业应明智地使用环境变量、限制权限、避免使用长期令牌、使用外部机密管理，并在共享任何集合或环境之前进行仔细检查。

CloudSEK 负责任地向受影响的组织报告了大多数已发现的事件，帮助降低了风险。为防止此类风险，CloudSEK 建议企业采取更可靠的安全措施，例如使用环境变量避免硬编码敏感数据、限制权限、频繁轮换令牌、利用秘密管理工具，以及在共享之前仔细检查集合。

此外，在这些发现披露后，Postman 还实施了一项秘密保护策略，以防止敏感数据在公共工作空间中暴露。如果发现秘密，该政策会提醒用户，提供解决方案，并帮助用户过渡到私人或团队工作空间。

从本月开始，我们将从公共 API 网络中移除已知暴露机密的公共工作空间。该公司指出：“随着我们推出这一政策变更，包含秘密的公共工作空间的所有者将收到通知，并有机会在该工作空间从网络中移除之前删除其暴露的秘密。”

本文翻译自hackread [原文链接](https://hackread.com/postman-workspaces-leak-api-keys-sensitive-tokens/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302988](/post/id/302988)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/postman-workspaces-leak-api-keys-sensitive-tokens/)

如若转载,请注明出处： <https://hackread.com/postman-workspaces-leak-api-keys-sensitive-tokens/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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