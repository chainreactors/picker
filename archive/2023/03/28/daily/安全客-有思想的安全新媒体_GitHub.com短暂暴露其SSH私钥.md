---
title: GitHub.com短暂暴露其SSH私钥
url: https://www.anquanke.com/post/id/287806
source: 安全客-有思想的安全新媒体
date: 2023-03-28
fetch_date: 2025-10-04T10:47:58.025161
---

# GitHub.com短暂暴露其SSH私钥

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

# GitHub.com短暂暴露其SSH私钥

阅读量**182872**

发布时间 : 2023-03-27 10:30:02

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

最大的源代码托管平台 GitHub 宣布更换其 SSH 密钥。原因是本周早些时候，它发现 GitHub.com 的 RSA SSH 私钥在一个公开的库内短暂暴露。它立即采取了行动并展开了调查。问题并不是任何 GitHub 系统被入侵或客户信息泄露的结果，它认为问题是疏忽大意，认为没有证据表明曝光的密钥遭到了滥用，出于谨慎考虑它更换了密钥。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287806](/post/id/287806)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Github](/tag/Github)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

### 相关文章

* ##### [GitHub大数据：10%程序员至少泄露一条机密信息](/post/id/287446)

  2023-03-15 11:00:13
* ##### [黑客窃取GitHub代码签名证书](/post/id/285840)

  2023-01-31 16:40:57
* ##### [攻击者通过破解软件传播Raccoon和Vidar恶意软件](/post/id/285614)

  2023-01-18 11:30:34
* ##### [GitHub宣布对所有公共仓库进行免费秘密扫描](/post/id/284474)

  2022-12-20 11:30:34
* ##### [黑客窃取130个GitHub存储库后，Dropbox披露漏洞](/post/id/282585)

  2022-11-03 10:45:43
* ##### [数千个GitHub存储库使用恶意软件提供虚假PoC漏洞利用](/post/id/282066)

  2022-10-24 11:00:03
* ##### [黑客利用虚假CircleCI 通知窃取GitHub帐户](/post/id/280685)

  2022-09-23 14:15:10

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