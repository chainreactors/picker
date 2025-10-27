---
title: Hugging Face 披露 Spaces 平台遭未经授权访问
url: https://www.anquanke.com/post/id/297032
source: 安全客-有思想的安全新媒体
date: 2024-06-05
fetch_date: 2025-10-06T16:55:59.247013
---

# Hugging Face 披露 Spaces 平台遭未经授权访问

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

# Hugging Face 披露 Spaces 平台遭未经授权访问

阅读量**87283**

发布时间 : 2024-06-04 11:30:03

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/hugging-face-discloses-unauthorized-access/>

译文仅供参考，具体内容表达以及含义原文为准。

该公司在一篇博客文章中透露，黑客入侵了人工智能公司 Hugging Face 的平台并窃取了其用户机密。

谷歌和亚马逊资助的 Hugging Face检测到其 Spaces 平台遭到未经授权的访问，该平台是一种用于展示 AI/机器学习 (ML) 应用程序和协作模型开发的托管服务。简而言之，该平台允许用户创建、托管和共享 AI 和 ML 应用程序，以及发现其他人制作的AI应用程序。

**Hugging Face Hack 利用代币**
Hugging Face 怀疑 Spaces 的部分机密信息可能已被未经授权访问。为了应对这一安全事件，该公司撤销了这些机密信息中的多个 HF 令牌，并通过电子邮件通知了受影响的用户。

Hugging Face 表示：“我们建议您刷新任何密钥或令牌，并考虑将您的 HF 令牌切换为新的默认细粒度访问令牌。”

该公司尚未透露受该事件影响的用户数量，该事件仍在调查中。

Hugging Face 表示，过去几天它已经做出了“重大”改进以加强 Spaces 的安全性，包括提供更好的可追溯性和审计功能的组织令牌、实施密钥管理服务，以及扩展其系统识别泄露令牌和使其无效的能力。

它还正在与外部网络安全专家一起调查此次违规行为，并将该事件报告给执法和数据保护机构。

**针对人工智能即服务提供商的威胁日益增加**
像 Hugging Face 这样的人工智能即服务 (AIaaS) 提供商面临的风险正在迅速增加，因为该领域的爆炸式增长使它们成为试图利用这些平台进行恶意目的的攻击者的有利可图的目标。

4 月初，云安全公司Wiz详细介绍了 Hugging Face 中的两个安全问题，这些问题可能允许攻击者获得跨租户访问权限，并通过接管持续集成和持续部署 (CI/CD) 管道来毒害 AI/ML 模型。

Wiz在一份详细介绍该威胁的报告中表示：“如果恶意行为者入侵 Hugging Face 平台，他们就有可能获取私人 AI 模型、数据集和关键应用程序的访问权限，从而造成大范围破坏和潜在的供应链风险。”

Wiz 研究人员发现的一个安全问题与 Hugging Face Spaces 平台有关。Wiz 发现攻击者可以在应用程序构建时执行任意代码，从而使他们能够从自己的机器上仔细检查网络连接。检查发现存在与共享容器注册表的连接，该注册表中存放着属于其他客户的图像，研究人员可以操纵这些图像。

HiddenLayer先前的研究 发现了 Hugging Face Safetensors 转换服务存在缺陷，这可能使攻击者能够劫持用户提交的 AI 模型并发动供应链攻击。

Hugging Face 还在 12 月证实已修复Lasso Security报告的严重 API 缺陷。

Hugging Face 表示正在积极解决这些安全问题，并继续调查近期的未经授权的访问，以确保其平台和用户的安全和完整性。

本文翻译自 [原文链接](https://thecyberexpress.com/hugging-face-discloses-unauthorized-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297032](/post/id/297032)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/hugging-face-discloses-unauthorized-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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