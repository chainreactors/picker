---
title: 恶意程序滥用微软IIS功能在Windows上执行恶意代码
url: https://www.anquanke.com/post/id/286520
source: 安全客-有思想的安全新媒体
date: 2023-02-21
fetch_date: 2025-10-04T07:35:26.982250
---

# 恶意程序滥用微软IIS功能在Windows上执行恶意代码

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

# 恶意程序滥用微软IIS功能在Windows上执行恶意代码

阅读量**168047**

发布时间 : 2023-02-20 11:00:27

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。

微软 IIS（Internet Information Services）是广泛使用的 Web 服务器，它的一项功能叫 Failed Request Event Buffering（FREB），旨在帮助管理员诊断错误，FREB 能从缓存中将部分错误相关的请求写入磁盘。黑客找到了滥用该功能的方法，攻击者首先需要入侵运行 IIS 的 Windows 系统，启用 FREB，通过将恶意代码注入 IIS 进程内存劫持执行，它随后就能拦截所有 HTTP 请求，寻找特殊格式的请求，这种特殊的请求能以隐蔽的方式执行远程代码，系统上没有可疑文件或进程在运行。研究人员将这种恶意程序命名为 Frebniis。[阅读原文]

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286520](/post/id/286520)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意程序](/tag/%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F)
* [微软 IIS](/tag/%E5%BE%AE%E8%BD%AF%20IIS)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* ##### [Android贷款应用骗取1200 万用户数据](/post/id/291713)

  2023-12-07 12:08:16
* ##### [安全错觉：黑客已学会模仿iOS中的锁定模式](/post/id/291727)

  2023-12-07 12:01:58
* ##### [恶意PyPI软件包使用Cloudflare隧道潜入防火墙](/post/id/285352)

  2023-01-10 14:00:23
* ##### [安装量达1500万，诈骗软件专门针对发展中国家](/post/id/284013)

  2022-12-05 11:00:46
* ##### [Google Play商店4款恶意应用总下载量超百万次](/post/id/282607)

  2022-11-03 15:00:02
* ##### [新恶意程序跨平台感染 Windows、Linux 和 FreeBSD](/post/id/282049)

  2022-10-24 10:15:41
* ##### [360CERT网络安全四月月报发布](/post/id/241060)

  2021-05-14 12:00:11

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