---
title: 安全研究员披露Facebook、Instagram双因素身份验证漏洞
url: https://www.anquanke.com/post/id/285963
source: 安全客-有思想的安全新媒体
date: 2023-02-04
fetch_date: 2025-10-04T05:39:18.065043
---

# 安全研究员披露Facebook、Instagram双因素身份验证漏洞

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

# 安全研究员披露Facebook、Instagram双因素身份验证漏洞

阅读量**309632**

发布时间 : 2023-02-03 10:30:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一名来自尼泊尔的安全研究员Gtm Mänôz，披露了一个影响Instagram和Facebook的双因素身份验证漏洞。在向Meta报告此漏洞后，其将一笔27200美元的赏金收入了囊中。

双因素身份验证(2FA)是目前常见的一种保护用户账户安全的手段。它是一种需要提供两个身份验证因素以确认身份的身份验证过程，用户需要用两种方式（用户所知道的和用户所拥有的，例如密码和手机收到的验证码）证明自己的身份才能获得账户访问授权。

据悉，该漏洞存在于Facebook母公司Meta用于确认手机号码和电子邮件地址的组件中。Gtm Mänôz注意到，该组件未对验证码做时间和失败次数校验，这使得攻击者在获知受害者的手机号码后，能够暴力破解验证码。[[阅读原文]](http://www.hackdig.com/02/hack-897826.htm)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285963](/post/id/285963)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全漏洞](/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)
* [双因素认证](/tag/%E5%8F%8C%E5%9B%A0%E7%B4%A0%E8%AE%A4%E8%AF%81)
* [meta](/tag/meta)

**+1**1赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃](/post/id/308349)

  2025-06-11 16:08:49
* ##### [“欧洲版CVE”上线，EUVD释放漏洞治理新信号](/post/id/307472)

  2025-05-16 18:04:21
* ##### [CVE-2025-24977:OpenCTI平台中的关键RCE缺陷将基础设施暴露为根级攻击](/post/id/307143)

  2025-05-07 16:32:13
* ##### [僵尸网络通过CVE-2024-6047和CVE-2024-11120开发旧GeoVision物联网设备](/post/id/307139)

  2025-05-07 16:27:26
* ##### [CVE-2025-47241:浏览器使用中的关键白名单绕过暴露了内部服务](/post/id/307134)

  2025-05-07 16:17:59
* ##### [CISA将Microsoft .NET和Apache OFBiz错误标记为在攻击中被利用](/post/id/303897)

  2025-02-06 15:03:21

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