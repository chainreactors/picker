---
title: Zerobot恶意软件利用Apache漏洞传播
url: https://www.anquanke.com/post/id/284621
source: 安全客-有思想的安全新媒体
date: 2022-12-24
fetch_date: 2025-10-04T02:24:14.014529
---

# Zerobot恶意软件利用Apache漏洞传播

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

# Zerobot恶意软件利用Apache漏洞传播

阅读量**247695**

发布时间 : 2022-12-23 10:30:33

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近日，Microsoft Defender for IoT研究团队观察到Zerobot僵尸网络已升级，通过影响互联网暴露和未修补Apache服务器的安全漏洞来感染新设备。同时，这个最新版本增加了新的分布式拒绝服务（DDoS）功能。同时，微软研究人员还发现了新的证据表明Zerobot通过破坏具有已知漏洞的设备来传播，例如Tenda GPON AC1200路由器中的命令注入漏洞CVE-2022-30023。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284621](/post/id/284621)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [僵尸网络](/tag/%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9C)

**+1**0赞

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

* ##### [FritzFrog 僵尸网络利用 Log4Shell、PwnKit 漏洞进行横向移动和权限升级](/post/id/293068)

  2024-02-02 11:34:58
* ##### [网络安全研究人员发现了一种针对路由器和物联网设备的 P2PInfect 僵尸网络的新变种](/post/id/291644)

  2023-12-05 11:44:36
* ##### [ShellBot僵尸网​​络使用十六进制IP地址绕过检测](/post/id/290743)

  2023-10-13 10:49:57
* ##### [HinataBot僵尸网络可发起3.3 Tbps大规模DDoS攻击](/post/id/287615)

  2023-03-20 11:30:19
* ##### [新版Prometei僵尸网络感染全球超过1万个系统](/post/id/287374)

  2023-03-14 11:00:17
* ##### [MyloBot僵尸网络蔓延全球，日均感染5万+设备](/post/id/286657)

  2023-02-23 11:30:28
* ##### [微软发现MCCrash新型僵尸网络](/post/id/284434)

  2022-12-19 14:00:51

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