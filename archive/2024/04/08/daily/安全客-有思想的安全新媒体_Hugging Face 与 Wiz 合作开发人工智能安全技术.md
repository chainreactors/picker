---
title: Hugging Face 与 Wiz 合作开发人工智能安全技术
url: https://www.anquanke.com/post/id/295306
source: 安全客-有思想的安全新媒体
date: 2024-04-08
fetch_date: 2025-10-04T12:14:56.242950
---

# Hugging Face 与 Wiz 合作开发人工智能安全技术

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

# Hugging Face 与 Wiz 合作开发人工智能安全技术

阅读量**61981**

发布时间 : 2024-04-07 10:18:56

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/hugging-face-partners-with-wiz/>

译文仅供参考，具体内容表达以及含义原文为准。

***网络安全公司 Wiz 与 Hugging Face 合作，修补人工智能云提供商架构中的漏洞，这些漏洞可能导致其客户数据面临风险。***

Wiz 表示，它已经发现了 Hugging Face AI 基础设施的关键缺陷，这些缺陷可能会损害提供商并使其客户数据面临风险。它警告说，其他人工智能即服务或人工智能云提供商也可能面临类似的风险。

“我们相信这些发现并不是 Hugging Face 独有的，并且代表了许多人工智能即服务公司将面临的租户分离挑战，考虑到它们运行客户代码和处理大量数据的模型，同时增长速度比任何其他公司都快。维兹在博客文章中说道。

Wiz 研究人员与 Hugging Face 合作，将恶意 AI 模型上传到该平台，并利用它在提供商的内部环境中获得立足点。

该模型被精心设计为充当具有隐藏后门功能的普通模型，通过使用 Hugging Face Inference API 与模型进行交互。后门 AI 模型是在 Hugging Face AI 基础设施上执行和激活的。

根据 Wiz 的说法，其研究人员随后使用后门生成了一个与内部环境相反的 shell。他们逃离了Linux容器，并在Hugging Face内部AI基础设施中获得了高权限。

Wiz表示：“恶意模型对人工智能系统构成了重大风险，特别是对于人工智能即服务提供商而言，因为潜在的攻击者可能会利用这些模型来执行跨租户攻击。”

该公司表示，此类攻击的潜在影响可能是“毁灭性的”，因为攻击者可能能够访问存储在云中的数百万个私有人工智能模型和应用程序。

Hugging Face 在另一篇博客文章中表示，与该漏洞相关的所有问题均已解决。它呼吁该领域的其他人“负责任地披露”安全漏洞和错误。

“人工智能行业正在迅速变化，新的攻击媒介/漏洞一直在被发现，”它说。

本文翻译自 [原文链接](https://cybernews.com/security/hugging-face-partners-with-wiz/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295306](/post/id/295306)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/hugging-face-partners-with-wiz/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [人工智能](/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [浅析新型网络犯罪DeepSeek AI实战应用](/post/id/305102)

  2025-03-18 10:38:20
* ##### [360SRC x Hacking Group丨「奇御」AI安全技术沙龙议题征集！](/post/id/302279)

  2024-11-28 17:43:31
* ##### [从误用到滥用： 人工智能风险与攻击](/post/id/300992)

  2024-10-17 11:00:07
* ##### [一种用于网络钓鱼攻击的生成式人工智能恶意软件](/post/id/300410)

  2024-09-25 14:16:34
* ##### [苹果加入美国政府对人工智能安全的自愿承诺](/post/id/298565)

  2024-07-31 11:23:56
* ##### [Vanta筹集1.5亿美元，加速其AI产品创新](/post/id/298358)

  2024-07-25 15:02:41

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