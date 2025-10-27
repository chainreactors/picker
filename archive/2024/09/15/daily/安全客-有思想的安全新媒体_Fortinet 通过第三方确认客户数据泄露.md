---
title: Fortinet 通过第三方确认客户数据泄露
url: https://www.anquanke.com/post/id/300115
source: 安全客-有思想的安全新媒体
date: 2024-09-15
fetch_date: 2025-10-06T18:20:13.136727
---

# Fortinet 通过第三方确认客户数据泄露

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

# Fortinet 通过第三方确认客户数据泄露

阅读量**112711**

发布时间 : 2024-09-14 14:57:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/fortinet-customer-data-breach-third-party>

译文仅供参考，具体内容表达以及含义原文为准。

Fortinet 已确认属于其“少数”客户的数据遭到泄露，此前一名黑客本周使用有点色彩缤纷的绰号“Fortibitch”泄露了 440GB 的信息。

黑客声称从 Azure SharePoint 站点获取了数据，并声称他们在公司拒绝与该个人就赎金要求进行谈判后泄露了这些数据。研究人员表示，这种情况再次凸显了公司必须保护第三方云存储库中保存的数据的责任。

## 未经授权访问 SaaS 环境

Fortinet 本身尚未具体确定泄露的来源。 但在 9 月 12 日的公告中，该公司表示，有人“未经授权访问了存储在 Fortinet 基于云的第三方共享文件驱动器实例上的有限数量的文件”。

这家安全供应商是全球市值最大的安全供应商之一，它发现该问题影响了其全球 775,000 多家客户中的不到 0.3%，这将使受影响的组织数量约为 2,325 家。

Fortinet 表示，它没有看到围绕受感染数据进行恶意活动的迹象。“Fortinet 立即执行了一项保护客户的计划，并酌情直接与客户沟通并支持他们的风险缓解计划，”该安全供应商在公告中指出。“该事件不涉及任何数据加密、勒索软件部署或访问 Fortinet 的企业网络。”Fortinet 表示，预计该事件不会对其运营或财务产生任何重大影响。

在与 Dark Reading 共享的威胁情报报告中，CloudSEK 表示，它观察到一个使用 Fortibitch 手柄的威胁行为者泄露了似乎不仅包括客户数据，还包括财务和营销文件、产品信息、来自印度的人力资源数据以及一些员工数据。

“该行为者试图勒索公司，但在谈判失败后，公布了数据，”CloudSEK 说。该公司推测，如果数据有任何真实价值，黑客会先尝试出售这些数据。

Fortinet 没有确认或否认黑客是否试图与该公司就被盗数据进行接触。

该黑客在 BreachForums 上的帖子包括对 Fortinet 收购 Lacework 和 NextDLP 的上下文无关的引用。它还提到了其他一些威胁行为者，其中最有趣的是被追踪为 DC8044 的乌克兰组织。“Fortibitch 和 DC8044 之间没有直接联系，但语气表明两者之间存在历史，”CloudSEK 表示。“根据现有信息，我们可以中等置信度确定威胁行为者位于乌克兰境外。”

## 泄露 Cloud Data Exposure 风险提醒

Fortinet 泄露事件（虽然显然不是太严重）提醒人们，在没有适当护栏 的情况下使用软件即服务 （SaaS） 和其他云服务时，企业组织的数据泄露风险会增加。Metomic 最近对大约 650 万个 Google Drive 文件进行了扫描，结果显示其中超过 40% 的文件包含敏感数据，包括员工数据和包含密码的电子表格。

通常，组织将数据存储在 Google Drive 文件中，几乎没有保护。超过三分之一 （34.2%） 的扫描文件与外部电子邮件地址共享，超过 350,000 个文件已公开共享。

Metomic 的首席执行官兼创始人 Rich Vibert 表示，在云环境中保护数据时，组织会犯三个基本错误：不使用多因素身份验证 （MFA） 来控制对 SaaS 应用程序的访问;为员工提供对应用程序本身中的文件夹和敏感资产的过多访问权限;以及存储敏感数据的时间过长。

目前尚不清楚黑客是如何从 Fortinet 的 SharePoint 环境中访问数据。但 CloudSEK 的威胁情报记者 Koushik Pal 表示，一种可能的情况是，攻击者通过网络钓鱼等方式获得了对有效登录凭据的访问权限，然后登录并从 SharePoint 和类似环境中泄露了数据。Pal 指出，信息窃取程序也是一种“非常常见”的攻击媒介。

## 重新思考云安全

“通常，开发人员应该使用环境变量、保险库或加密存储来存储敏感信息，并避免在源代码中对凭据进行硬编码，”Pal 说。开发人员通常会将 API 密钥、用户名和密码等访问凭证硬编码到源代码中，并无意中将代码推送到公共或不安全的私有存储库中，从那里可以相对容易地访问它们。

“组织应强制要求访问 SharePoint 和其他关键系统时使用 MFA，以防止未经授权的访问，即使凭据被盗用，”Pal 解释说。“定期监控存储库，以发现泄露的凭据、敏感数据或错误配置，并在所有团队中实施安全最佳实践。”

Synopsys Software Integrity Group 网络安全高级经理 Akhil Mittal 表示，像 Fortinet 经历的事件表明，为什么组织将其云资产的安全完全交给云服务提供商是一个错误。“组织应该重新考虑如何将客户数据存储在共享驱动器中，确保关键信息与不太敏感的文件分开保存，”他说。

对传输中和静态的敏感数据进行加密也是一个好主意，这样即使攻击者获得了访问权限，也可以减轻损害。Mittal 认为对云资产的持续监控是保护云资产的基础。“将零信任原则应用于第三方平台还可以确保不会自动信任任何外部服务，从而降低未经授权访问的风险，”他补充道。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/fortinet-customer-data-breach-third-party)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300115](/post/id/300115)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/fortinet-customer-data-breach-third-party)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/fortinet-customer-data-breach-third-party>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [未经授权访问 SaaS 环境](#h2-0)
* [泄露 Cloud Data Exposure 风险提醒](#h2-1)
* [重新思考云安全](#h2-2)

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