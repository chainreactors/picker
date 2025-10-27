---
title: Claroty利用RCE在西门子PLC中发现硬编码的加密密钥
url: https://www.anquanke.com/post/id/281714
source: 安全客-有思想的安全新媒体
date: 2022-10-14
fetch_date: 2025-10-03T19:48:58.531791
---

# Claroty利用RCE在西门子PLC中发现硬编码的加密密钥

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

# Claroty利用RCE在西门子PLC中发现硬编码的加密密钥

阅读量**250815**

发布时间 : 2022-10-13 11:45:09

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

位于纽约的工业网络安全公司 Claroty 的研究部门 Team82 透露，他们成功提取了嵌入西门子可编程逻辑计算机（PLC）系列 SIMATIC S7-1200/1500s 和西门子自动化工程软件平台 TIA Portal 中的严密防护、硬编码的密码密钥。

据悉，该团队针对SIMATIC S7-1200和S7-1500 PLC的CPU部署了一种新的远程代码执行 (RCE) 技术，为此他们使用了之前对 Siemens PLC 的研究中发现的漏洞 ( CVE-2020-15782 )这使他们能够绕过 PLC 上的本机内存保护并获得读/写权限。

经测试，他们不仅能够提取西门子产品线中使用的内部严密保护的私钥，还能够实施完整的协议栈，加密和解密受保护的通信和配置。[[阅读原文]](https://www.infosecurity-magazine.com/news/claroty-found-cryptographic-keys/)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/281714](/post/id/281714)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞利用](/tag/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8)
* [西门子](/tag/%E8%A5%BF%E9%97%A8%E5%AD%90)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* ##### [ingress-nightmare 漏洞利用分析与 k8s 相关组件理解](/post/id/306494)

  2025-04-14 15:24:44
* ##### [【翻译】Zoom 漏洞链：从Cookie XSS到会话接管以及摄像头劫持](/post/id/299543)

  2024-08-28 10:53:50
* ##### [ZIMBRA 零日漏洞CVE-2023-37580 被四个黑客组织利用，窃取政府电子邮件](/post/id/291404)

  2023-11-17 10:56:15
* ##### [俄罗斯Winter Vivern APT （CVE-2023-5631 ）XSS 漏洞利用过程](/post/id/291055)

  2023-10-27 11:47:08
* ##### [Citrix Bleed 漏洞（CVE-2023-4966）POC发布](/post/id/291013)

  2023-10-26 12:10:10
* ##### [安全专家发布VMware (CVE-2023-34051) POC 漏洞利用代码](/post/id/290987)

  2023-10-25 11:52:41
* ##### [CVE-2023-42793漏洞被两个朝鲜黑客组织利用，向国防、媒体、IT服务组织等机构发起攻击](/post/id/290867)

  2023-10-23 11:20:18

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