---
title: 微软将Raspberry Robin蠕虫与Clop勒索软件攻击关联
url: https://www.anquanke.com/post/id/282249
source: 安全客-有思想的安全新媒体
date: 2022-10-29
fetch_date: 2025-10-03T21:11:33.820567
---

# 微软将Raspberry Robin蠕虫与Clop勒索软件攻击关联

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

# 微软将Raspberry Robin蠕虫与Clop勒索软件攻击关联

阅读量**372098**

发布时间 : 2022-10-28 10:15:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软表示，一个被追踪为DEV-0950的威胁组织使用 Clop 勒索软件来加密先前感染了Raspberry Robin 蠕虫的受害者网络。

据悉，DEV-0950 恶意活动与追踪为FIN11和TA505的网络犯罪组织重叠，这些组织以在目标系统上部署Clop勒索软件而闻名。除了勒索软件，Raspberry Robin蠕虫还被用于将其他第二阶段的有效载荷投放到受感染的设备上，具体包括 IcedID、Bumblebee 和 Truebot。

安全分析师称，Raspberry Robin蠕虫通过恶意 .LNK 文件的BadUSB 设备传播到其他设备。连接BadUSB 设备并单击链接后，蠕虫将使用cmd.exe生成一个msiexec进程，以启动存储在受感染驱动器上的第二个恶意文件。在受感染的 Windows 设备上，它与其命令和控制服务器 (C2) 进行通信。在使用几个合法的 Windows 实用程序（fodhelper、msiexec 和 odbcconf）绕过受感染系统上的用户帐户控制 (UAC) 后，它还提供和执行额外的有效负载。[[阅读原文]](https://www.bleepingcomputer.com/news/security/microsoft-links-raspberry-robin-worm-to-clop-ransomware-attacks/)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282249](/post/id/282249)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索病毒](/tag/%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92)
* [蠕虫](/tag/%E8%A0%95%E8%99%AB)
* [TA505](/tag/TA505)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* ##### [地狱猎犬在行动：至少20个俄罗斯组织成为网络攻击的受害者](/post/id/291583)

  2023-12-01 11:00:24
* ##### [麒麟勒索病毒声称攻击汽车巨头延锋](/post/id/291533)

  2023-11-29 11:34:08
* ##### [LockBit 勒索团伙攻击加拿大政府承包商](/post/id/291424)

  2023-11-21 15:24:31
* ##### [FBI ：“分散蜘蛛”勒索组织的策略](/post/id/291401)

  2023-11-17 10:49:33
* ##### [加利福尼亚州长滩市在网络攻击后关闭 IT 系统](/post/id/291399)

  2023-11-17 10:44:55
* ##### [美杜莎勒索软件威胁泄露数据后，丰田证实存在违规行为](/post/id/291394)

  2023-11-17 10:35:15
* ##### [核能、石油和天然气是 2024 年勒索软件组织的主要目标](/post/id/291368)

  2023-11-14 16:30:29

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