---
title: GitGuardian 工具可以帮助公司发现开发者在GitHub上泄露的信息
url: https://www.anquanke.com/post/id/298304
source: 安全客-有思想的安全新媒体
date: 2024-07-26
fetch_date: 2025-10-06T17:40:18.993463
---

# GitGuardian 工具可以帮助公司发现开发者在GitHub上泄露的信息

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

# GitGuardian 工具可以帮助公司发现开发者在GitHub上泄露的信息

阅读量**90274**

发布时间 : 2024-07-25 15:07:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Industry News，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/07/24/gitguardian-github-tool/>

译文仅供参考，具体内容表达以及含义原文为准。

GitGuardian 发布了一个工具，帮助公司发现他们的开发人员在公共 GitHub 上泄露了多少秘密，包括与公司相关的和个人的秘密。

![]()

即使您的组织不参与开源，您的开发人员或分包商也可能无意中泄露其个人 GitHub 仓库上的敏感信息。想想公司机密或源代码——一个重大的风险警报！

输入您的域名并获得有价值的指标，例如在 GitHub 上公开泄露的秘密数量和有效秘密的数量。

### 审计中包含的数据

**已扫描的提交**：GitHub 上的所有活动都链接到提交电子邮件。GitGuardian 可以将此类提交电子邮件绑定到 GitHub 帐户，从而监控该帐户的活动。

**您边界内的活跃开发人员**：在其 GitHub 个人资料中提及您的公司名称的开发人员，或在 GitHub 上公开推送代码时使用其公司电子邮件地址的开发人员。

**在 GitHub 上公开泄露的机密**：机密是授予系统或数据访问权限的数字身份验证凭据。这些通常是 API 密钥或用户名和密码。

**在 GitHub 上公开可用的有效机密**：仍可能被恶意人员利用的机密。

**按类别划分的机密细分**：每个类别的机密泄露百分比（例如。私钥、版本控制平台、云提供商、消息系统、数据存储等）。

**在提交中直接提及您的公司**：在提交的代码中提及您的公司域的提交。

**涉及至少一个秘密泄露的开发人员**：您外围的开发人员至少泄露了一个秘密。

**敏感文件中包含的机密**：在本身敏感的文件（如配置文件）中发布的机密。

**公共事件**：当私有仓库公开时，将发生公共事件。此类事件是敏感的，因为它泄露了存储库的整个历史记录，可以在其中找到敏感数据。

**从 GitHub 中删除的秘密**：在 GitHub 上无法再找到，但已被泄露并可以在 GitHub 档案中找到的秘密。

GitGuardian 的秘密检测引擎自 2017 年以来一直在生产环境中运行，分析来自 GitHub 的数十亿次提交。算法和检测器不断针对 40 亿次提交的数据集进行训练。最新的 2024 年机密状态蔓延显示，2023 年在 GitHub 上暴露了 1280 万个新机密事件。GitGuardian 可以通过首先识别在 GitHub 上活跃的开发人员来告诉您有多少泄漏与您的公司有关。

即使您的组织不参与开源，您的开发人员或分包商也可能无意中泄露其个人 GitHub 仓库上的敏感信息。这包括公司机密或源代码，构成重大风险。

审核生成的分数范围从 A 到 E。此分数考虑了检测到的硬编码密钥的数量、泄密者的数量（至少泄露了一个密钥的开发人员）以及过去三年中您范围内的开发人员数量。公司按其开发人员数量进行分组，以便进行公平的比较。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/07/24/gitguardian-github-tool/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298304](/post/id/298304)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/07/24/gitguardian-github-tool/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/07/24/gitguardian-github-tool/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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