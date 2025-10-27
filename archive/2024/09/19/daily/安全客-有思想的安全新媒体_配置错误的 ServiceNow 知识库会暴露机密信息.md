---
title: 配置错误的 ServiceNow 知识库会暴露机密信息
url: https://www.anquanke.com/post/id/300139
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:11.479262
---

# 配置错误的 ServiceNow 知识库会暴露机密信息

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

# 配置错误的 ServiceNow 知识库会暴露机密信息

阅读量**83123**

发布时间 : 2024-09-18 15:01:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 菲奥娜·杰克逊，文章来源：TechRepublic

原文地址：<https://www.techrepublic.com/article/servicenow-knowledge-bases-security-issue/>

译文仅供参考，具体内容表达以及含义原文为准。

AppOmni 研究人员发现了 1000 多个配置错误的知识库实例，其中的文章可能会通过 Public Widget 受到损害。

ServiceNow 是一个用于管理 IT 服务和流程的基于云的平台，其用户可能会在不知不觉中暴露机密信息，包括姓名、电话号码、内部系统详细信息和活动凭据。知识库（ServiceNow 中的自助服务平台，用户可以在其中创建、存储和共享文章和指南等信息）配置错误可能会导致未经授权的个人访问系统。许多组织将知识库用作敏感内部信息的存储库，例如如何重置公司密码、如何应对网络攻击、与 HR 流程相关的数据等。根据 SaaS 安全平台提供商 AppOmni 的一篇新博客，大约 60% 的风险暴露涉及默认设置为允许公共访问的旧版本知识库。其他应用程序具有“用户标准”（定义用户访问知识库或参与知识库的特定条件的规则），这些规则无意中向未经身份验证的用户授予访问权限。

85% 的财富 500 强企业都在使用 ServiceNow，目前有超过 1000 个实例设置错误。许多拥有多个 ServiceNow 实例的组织被发现始终错误地配置了知识库访问控制，这表明这些设置要么是跨实例克隆的，要么存在对它们工作方式的根本误解。

AppOmni SaaS 安全研究主管 Aaron Costello 表示：“这凸显了企业迫切需要定期检查和更新其安全配置，以防止未经授权的访问并保护其数据资产。

“了解这些问题以及如何缓解这些问题对于在企业 SaaS 环境中保持强大的安全性至关重要。”

这不是 ServiceNow 第一次被发现由于用户配置错误而暴露敏感数据。2020 年，另一位研究人员报告了类似的发现，即知识库文章可以通过现在安全的 UI 页面公开访问。

ServiceNow 首席信息安全官 Ben De Bont 表示：“ServiceNow 致力于促进与安全社区的合作。我们致力于保护客户的数据，而安全研究人员是我们不断努力提高产品安全性的重要合作伙伴。

## 什么是知识库配置错误？

AppOmni 发现，企业在三种情况下将其 ServiceNow 知识库置于泄露风险中：

1. 如果使用旧版本的 ServiceNow，其中知识库的默认设置允许在未设置用户条件时进行公共访问。
2. 如果将“Any User”和“Any user for kb”用户标准用作允许列表。这两者都向未经身份验证的用户授予访问权限，而管理员可能没有意识到这一点。
3. 如果管理员未配置拒绝列表，则允许外部用户绕过访问控制。

## 攻击者如何获得对知识库的访问权限

根据 Costello 的概念验证，攻击者可以通过公共小部件访问配置错误的知识库，例如“知识库文章页面”小部件，它显示特定知识库文章中的内容。

攻击者可以使用名为 Burp Suite 的工具自动请求通过小部件查找和访问文章。使用知识库文章页面 Widget 可以更轻松地实现这一点，该 Widget 对文章 ID 使用可预测的格式“KBXXXXXXX”，其中 X 表示正整数。

Burp Suite 的 Intruder 功能可以快速迭代这些整数并识别可能无意中暴露的文章。然后，它可以返回正文文本，其中可能同时包含多个不安全文章的敏感数据。

## 如何保护知识库免受未经授权的访问

### 对知识库访问控制运行定期诊断

ServiceNow 的用户条件诊断工具允许管理员确定哪些用户（经过身份验证和未经身份验证）能够访问知识库和单个文章。

导航到 /get\_public\_knowledge\_bases.do 以识别公共知识库，并导航到 /km\_diagnostics.do 上的完整诊断工具以识别公共和非公共用户对单个文章的访问级别。

### 默认情况下，使用业务规则拒绝对知识库的未经身份验证的访问

确保为知识库激活“sys\_id 6c8ec5147711111016f35c207b5a9969”业务规则（将来宾用户添加到“无法读取且无法贡献”用户条件）。

本文翻译自TechRepublic [原文链接](https://www.techrepublic.com/article/servicenow-knowledge-bases-security-issue/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300139](/post/id/300139)

安全KER - 有思想的安全新媒体

本文转载自: [TechRepublic](https://www.techrepublic.com/article/servicenow-knowledge-bases-security-issue/)

如若转载,请注明出处： <https://www.techrepublic.com/article/servicenow-knowledge-bases-security-issue/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [什么是知识库配置错误？](#h2-0)
* [攻击者如何获得对知识库的访问权限](#h2-1)
* [如何保护知识库免受未经授权的访问](#h2-2)
  + [对知识库访问控制运行定期诊断](#h3-3)
  + [默认情况下，使用业务规则拒绝对知识库的未经身份验证的访问](#h3-4)

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