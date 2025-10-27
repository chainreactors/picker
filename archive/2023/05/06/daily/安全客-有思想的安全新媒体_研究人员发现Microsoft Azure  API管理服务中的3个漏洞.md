---
title: 研究人员发现Microsoft Azure  API管理服务中的3个漏洞
url: https://www.anquanke.com/post/id/288526
source: 安全客-有思想的安全新媒体
date: 2023-05-06
fetch_date: 2025-10-04T11:36:42.767959
---

# 研究人员发现Microsoft Azure  API管理服务中的3个漏洞

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

# 研究人员发现Microsoft Azure API管理服务中的3个漏洞

阅读量**335720**

|评论**1**

发布时间 : 2023-05-05 11:59:52

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft Azure API管理服务中披露了三个新的安全漏洞，恶意行为者可能会滥用这些漏洞来访问敏感信息或后端服务。

据以色列云安全公司 Ermetic称，这包括两个服务器端请求伪造(SSRF)漏洞和一个API管理开发人员门户中的无限制文件上传功能实例：

通过滥用SSRF漏洞，攻击者可以从服务的CORS代理和托管代理本身发送请求，访问内部Azure资产，拒绝服务并绕过Web应用程序防火墙；通过文件上传路径遍历，攻击者可以将恶意文件上传到Azure托管的内部工作负载。

在Ermetic发现的两个SSRF漏洞中，其中一个是绕过 Microsoft为解决Orca今年早些时候报告的类似漏洞而实施的修复程序。

另一个漏洞存在于API管理代理功能中。利用SSRF缺陷可能会导致机密性和完整性丧失，从而使威胁行为者能够读取内部Azure资源并执行未经授权的代码。在开发人员门户中发现的路径遍历缺陷源于缺乏对上传文件的文件类型和路径的验证。

经过身份验证的用户可以利用此漏洞将恶意文件上传到开发人员门户服务器，甚至可能在底层系统上执行任意代码。经过负责任的披露，这三个漏洞都已被微软修复。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288526](/post/id/288526)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**25赞

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

* ##### [再添数字政府新名片！深圳“深治慧”平台入选2025数博会创新案例](/post/id/311777)

  2025-09-02 15:37:49
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/310525)

  2025-07-24 10:24:57
* ##### [ISC.AI 2025国际人工智能发展高峰论坛：凝聚全球共识，点亮AI未来](/post/id/310510)

  2025-07-24 09:47:17
* ##### [ISC.AI大咖来了——国家网络安全守卫者 周鸿祎](/post/id/310504)

  2025-07-24 09:43:28
* ##### [攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）](/post/id/310339)

  2025-07-21 17:41:39
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/309947)

  2025-07-11 16:10:36
* ##### [报名开启！ISC.AI训练营助力AI与数字安全人才培养](/post/id/309827)

  2025-07-10 17:42:56

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