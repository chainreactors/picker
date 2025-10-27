---
title: Dropbox 报告其 Sign 产品的敏感身份验证数据遭到泄露
url: https://www.anquanke.com/post/id/296189
source: 安全客-有思想的安全新媒体
date: 2024-05-07
fetch_date: 2025-10-06T17:17:07.989735
---

# Dropbox 报告其 Sign 产品的敏感身份验证数据遭到泄露

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

# Dropbox 报告其 Sign 产品的敏感身份验证数据遭到泄露

阅读量**74313**

发布时间 : 2024-05-06 11:11:37

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/dropbox-data-breach-of-sensitive-data/>

译文仅供参考，具体内容表达以及含义原文为准。

云存储和文件共享公司 Dropbox 披露了一个安全漏洞，导致未经授权访问敏感信息，包括密码和其他身份验证信息。

Dropbox 在向美国证券交易委员会提交的 8-K 文件中透露，此次违规行为针对的是其生产环境，特别是影响了 Dropbox Sign（以前称为 HelloSign），这是一个用于数字签名文档的平台。

> *“攻击者破坏了 Sign 后端的一个服务帐户，该帐户是一种用于执行应用程序和运行自动化服务的非人类帐户。因此，该帐户有权在 Sign 的生产环境中执行各种操作。然后，威胁参与者使用对生产环境的访问权限来访问我们的客户数据库。*

访问的信息涉及所有 Dropbox Sign 用户，包括帐户设置、姓名和电子邮件。对于某些用户来说，电话号码、哈希密码等其他数据以及 API 密钥、OAuth 令牌和多因素身份验证等身份验证信息也受到了损害。

> “从技术角度来看，Dropbox Sign 的基础设施在很大程度上与其他 Dropbox 服务是分开的。也就是说，我们彻底调查了这一风险，并认为该事件与 Dropbox Sign 基础设施无关，不会影响任何其他 Dropbox 产品。”

在法证调查人员参与并通知执法​​部门的同时，监管机构也是基于个人信息访问的推定而被告知的。

Dropbox 已采取措施减轻违规影响，包括轮换 OAuth 令牌以及为具有 Dropbox Sign API 访问权限的客户生成新的 API 密钥。 Dropbox表示，在 API 密钥轮换之前，某些功能将继续受到限制。

用户通知正在进行中，Dropbox 正在联系受影响的用户并提供必要行动的指导。该[公司](https://thecyberexpress.com/how-to-start-a-cyber-security-company/)预计所有通知将在下周内完成。

尽管 Dropbox 预计不会对其运营或财务状况产生重大影响，但它承认潜在的[风险](https://thecyberexpress.com/what-are-risks-in-cybersecurity/ "风险")，包括诉讼、客户行为的变化和监管审查的加强。

继2022 年针对其开发人员的网络钓鱼活动导致公司 GitHub 帐户和敏感信息遭到未经授权的访问之后，此次 Dropbox 数据泄露事件标志着这家文件共享巨头面临的另一项安全挑战。

本文翻译自 [原文链接](https://thecyberexpress.com/dropbox-data-breach-of-sensitive-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296189](/post/id/296189)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/dropbox-data-breach-of-sensitive-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [德克萨斯州交通部 (TxDOT) 数据泄露事件暴露了 30 万份车祸报告](/post/id/308355)

  2025-06-11 16:33:57
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [美国电话电报公司（AT&T）再次遭遇大规模身份数据泄露事件](/post/id/308193)

  2025-06-06 15:22:45
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光](/post/id/304864)

  2025-02-28 15:37:26

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