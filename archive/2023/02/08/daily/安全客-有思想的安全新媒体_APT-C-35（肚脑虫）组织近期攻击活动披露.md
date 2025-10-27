---
title: APT-C-35（肚脑虫）组织近期攻击活动披露
url: https://www.anquanke.com/post/id/286124
source: 安全客-有思想的安全新媒体
date: 2023-02-08
fetch_date: 2025-10-04T05:55:26.402297
---

# APT-C-35（肚脑虫）组织近期攻击活动披露

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

# APT-C-35（肚脑虫）组织近期攻击活动披露

阅读量**194747**

发布时间 : 2023-02-07 14:30:14

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

APT-C-35（肚脑虫），也称Donot，是一个来自于南亚的境外APT组织，其主要针对巴基斯坦及周边国家地区的政府机构进行网络间谍活动，以窃取敏感信息为主。该组织的攻击活动最早可追溯到2016年，近年来该组织活动频繁，不断被数个国内外安全团队持续追踪和披露。

近期，360高级威胁研究院在日常威胁狩猎中多次发现APT-C-35（肚脑虫）组织的攻击活动。在本轮攻击行动中，该组织依然采用宏文档作为恶意载体，从自身释放恶意载荷并执行，通过层层下载的方式加载远控模块，从而实现窃密行动，并且整个过程的恶意代码均带有数字签名信息。

APT-C-35（肚脑虫）组织使用PPT或者XLS文档作为攻击载体，当受害者打开恶意文档时，会立即释放一个压缩包文件和批处理文件，并创建3个定时任务。其中Tls\_SSL计划任务每隔4分钟执行批处理文件，批处理文件主要作用是将释放的压缩包进行解压操作，得到恶意可执行文件comd.exe，并删除Tls\_SSL计划任务。My\_Drive计划任务是定时执行comd.exe，comd.exe负责继续下载下一阶段载荷，同时下载一个批处理脚本作为Pls\_SSL计划任务的启动项从而启动下载的载荷，载荷的主要功能为下载远控模块mnps.exe，从而实现恶意活动。[[阅读原文]](https://mp.weixin.qq.com/s/rslBGQgTL_jZD73AJqI05Q)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286124](/post/id/286124)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [APT](/tag/APT)
* [APT-C-35](/tag/APT-C-35)
* [肚脑虫](/tag/%E8%82%9A%E8%84%91%E8%99%AB)

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

* ##### [猎影计划：从密流中捕获 Cobalt Strike 的隐秘身影](/post/id/310538)

  2025-07-24 12:50:35
* ##### [APT-C-55（Kimsuky）组织在RandomQuery活动中投递开源RAT的攻击活动分析](/post/id/297233)

  2024-06-13 10:15:14
* ##### [Andariel APT 使用 DoraRAT 和 Nestdoor 恶意软件监视韩国企业](/post/id/297004)

  2024-06-03 10:52:13
* ##### [Turla APT 组织涉嫌利用 MSBuild 微小后门进行隐秘攻击](/post/id/296639)

  2024-05-21 10:31:48
* ##### [发现针对印度大学的 SideCopy APT 活动](/post/id/296541)

  2024-05-16 11:47:09
* ##### [俄罗斯黑客 APT28 对波兰政府发动恶意软件攻击](/post/id/296335)

  2024-05-09 11:10:37
* ##### [透明部落：针对印度国防部门的难以捉摸的威胁](/post/id/295858)

  2024-04-22 11:09:46

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