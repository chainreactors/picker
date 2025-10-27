---
title: Meta开源其内部源码管理系统Sapling
url: https://www.anquanke.com/post/id/283434
source: 安全客-有思想的安全新媒体
date: 2022-11-19
fetch_date: 2025-10-03T23:11:42.460910
---

# Meta开源其内部源码管理系统Sapling

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

# Meta开源其内部源码管理系统Sapling

阅读量**502747**

发布时间 : 2022-11-18 10:30:17

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Git 是广泛使用的源码管理系统，但它在处理规模庞大的源代码库时速度比较慢。

微软几年前发布了一个解决方案叫 GVFS（Git 虚拟文件系统）。现在另一家巨型公司 Meta/Facebook 宣布了它的内部解决方案 Sapling。Meta 称，Sapling 项目始于 10 年前，旨在解决现有源代码管理系统难以处理庞大代码库的难题，一开始是作为 Mercurial 的扩展，后来快速成长为有着自己的存储格式、线程协议、算法和行为的独立系统。Meta 目前只开源了兼容 Git 的 Sapling 系统客户端，未来将会开源其它部分。[[阅读原文]](https://www.solidot.org/story?sid=73397)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283434](/post/id/283434)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [开源](/tag/%E5%BC%80%E6%BA%90)
* [meta](/tag/meta)
* [Sapling](/tag/Sapling)

**+1**28赞

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

* ##### [BlackHat USA 2024 | vArmor云原生容器沙箱](/post/id/299446)

  2024-08-23 11:17:43
* ##### [正式开源！字节安全团队自研云原生容器沙箱 vArmor](/post/id/290482)

  2023-08-22 17:08:29
* ##### [Meta探索构建去中心化微博服务挑战Twitter](/post/id/287384)

  2023-03-14 14:00:37
* ##### [恶意Npm包使用误植域名技术下载恶意软件](/post/id/286363)

  2023-02-14 13:00:37
* ##### [安全研究员披露Facebook、Instagram双因素身份验证漏洞](/post/id/285963)

  2023-02-03 10:30:43
* ##### [欧盟对Meta开出4.11亿美元罚单](/post/id/285140)

  2023-01-06 11:30:56
* ##### [Meta因分类广告被欧盟指控违反反垄断法](/post/id/284492)

  2022-12-21 10:15:06

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