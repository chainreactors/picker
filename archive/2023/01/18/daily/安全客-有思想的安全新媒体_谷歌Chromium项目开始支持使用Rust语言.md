---
title: 谷歌Chromium项目开始支持使用Rust语言
url: https://www.anquanke.com/post/id/285516
source: 安全客-有思想的安全新媒体
date: 2023-01-18
fetch_date: 2025-10-04T04:06:22.576417
---

# 谷歌Chromium项目开始支持使用Rust语言

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

# 谷歌Chromium项目开始支持使用Rust语言

阅读量**146959**

发布时间 : 2023-01-17 10:00:05

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第442期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1.银保监会发布《银行保险监管统计管理办法》

[![]()](https://p1.ssl.qhimg.com/t01651419548ef05760.png)

中国银保监会近日发布《银行保险监管统计管理办法》，自2023年2月1日起正式施行。《办法》明确要求银行保险机构应将本单位监管统计工作纳入数据治理范畴，明确提出了监管统计数据分析应用相关要求，引导银行保险机构充分运用数据分析手段，安全、合规开展数据分析和挖掘应用。

银保监会有关部门负责人介绍，《办法》在修订过程中充分征求并吸取了行业意见，应有利于推动和加强银行保险机构监管统计管理，规范监管统计行为，提升监管统计数据质量，强化监管统计数据安全保护，促进监管统计工作持续高质量发展。

监管统计是银行业保险业监管的重要基础性工作。《办法》的主要内容包括监管统计管理机构、监管统计调查管理、银行保险机构监管统计管理、银行保险机构监管统计管理等。其中，关于监管统计调查管理，《办法》规定了监管统计调查原则、监管统计调查分类、派出机构临时统计调查、监管统计资料管理、监管统计资料公布等监管要求。[[阅读原文]](https://baijiahao.baidu.com/s?id=1754711128616084908&wfr=spider&for=pc)

## 2.谷歌Chromium项目开始支持使用Rust语言

[![]()](https://p4.ssl.qhimg.com/t0157a4313b499ba1da.png)

Google 安全博客宣布，Chromium 项目开始支持使用 Rust 语言。Rust 是一种高性能、内存安全语言，而软件项目发现的大部分漏洞都属于内存安全 bug。

据悉，目前的支持只是第一阶段，在C++代码中使用Rust写的第三方库（编译成.so）。估计明年Chromium的二进制发行文件中会包含rust写的库。

而更广泛地在Chromium中使用Rust则还需要时间去评估。[[阅读原文]](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html)

## 3.法国数据保护监管机构对Tiktok罚款540万美元

[![]()](https://p3.ssl.qhimg.com/t0131e8f11e29ddbcd0.png)

因违反cookie同意规则，法国数据保护监管机构对短视频平台 TikTok 处以500 万欧元（约540万美元）罚款。

法国数据保护监管机构声称，用户无法拒绝 cookie，就像他们接受 cookie 一样容易，字节跳动旗下的公司也未能充分告知不同 cookie 的目的。受限委员会认为，让拒绝机制更复杂实际上相当于阻止用户拒绝 cookie，并鼓励他们更喜欢“全部接受”按钮的便利性。

2022年12月，法国 CNIL对 APPLE 处以800 万欧元的罚款，原因是在其终端上存放和/或写入用于广告目的的标识符之前未征得 iPhone 法国用户（iOS 14.6版本）的同意。[[阅读原文]](https://securityaffairs.com/140786/digital-id/cnil-fined-tiktok.html?_ga=2.107486341.68580306.1673779871-556034239.1631001578&_gl=1*18ez4no*_ga*NTU2MDM0MjM5LjE2MzEwMDE1Nzg.*_ga_P62M3QN974*MTY3Mzc3OTg3MS43Ni4wLjE2NzM3Nzk4NzEuMC4wLjA.*_ga_8ZWTX5HC4Z*MTY3Mzc3OTg3MS44LjAuMTY3Mzc3OTg3MS4wLjAuMA..)

## 4.受污染的VPN被用来传播EyeSpy监控软件

[![]()](https://p2.ssl.qhimg.com/t01593e1116d02d34cb.png)

该项恶意软件活动被发现始于2022年5约，受感染的 VPN 安装程序被用来提供一种名为EyeSpy的监控软件。

它使用“SecondEye 的组件——一个合法的监控应用程序——通过木马化安装程序来监视 20Speed VPN 的用户，这是一种基于伊朗的 VPN 服务，”Bitdefender在一份分析中说。

这家罗马尼亚网络安全公司补充说，据称大部分感染起源于伊朗，在德国和美国检测到的病例较少。

根据通过互联网档案馆捕获的快照，SecondEye声称是一种商业监控软件，可以用作“家长控制系统或在线看门狗”。截至2021年11月，它的售价在99 美元到200美元之间。[[阅读原文]](https://thehackernews.com/2023/01/beware-tainted-vpns-being-used-to.html)

## 5.Cacti服务器因未能修补大多数关键漏洞而受到攻击

[![]()](https://p2.ssl.qhimg.com/t01ae263e045245c9a5.png)

大多数暴露在互联网上的 Cacti 服务器尚未针对最近修补的严重安全漏洞进行修补，该漏洞已在野外被积极利用。

据悉，该结论是根据攻击面管理平台 Censys 得出，该平台发现在总共6427台服务器中只有26台运行 Cacti 的补丁版本（1.2.23和1.3.0）。

该问题与CVE-2022-46169（CVSS 分数：9.8）有关，它结合了身份验证绕过和命令注入，使未经身份验证的用户能够在受影响版本的基于 Web 的开源监控解决方案上执行任意代码。[[阅读原文]](https://thehackernews.com/2023/01/cacti-servers-under-attack-as-majority.html)

## 6.数以百计的SugarCRM服务器被感染恶意程序

[![]()](https://p3.ssl.qhimg.com/t01ed779461ffae941c.png)

过去两周，黑客利用SugarCRM系统的一个高危漏洞传播恶意程序控制服务器。

漏洞是在2022年12月爆出的，当时没有补丁属于0day，公开漏洞的人还发布了漏洞利用代码，称它是一个身份验证绕过加远程代码执行漏洞，这意味着攻击者不需要身份凭证就可以在存在漏洞的服务器上远程运行恶意代码。SugarCRM官方在1月5日发布公告证实了该漏洞。提供网络监测服务的 Censys安全研究人员周三报告，在其监测到的3059台SugarCRM服务器中有354台SugarCRM感染了恶意程序植入了后门。[[阅读原文]](https://www.solidot.org/story?sid=73882)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285516](/post/id/285516)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [1.银保监会发布《银行保险监管统计管理办法》](#h2-1)
* [2.谷歌Chromium项目开始支持使用Rust语言](#h2-2)
* [3.法国数据保护监管机构对Tiktok罚款540万美元](#h2-3)
* [4.受污染的VPN被用来传播EyeSpy监控软件](#h2-4)
* [5.Cacti服务器因未能修补大多数关键漏洞而受到攻击](#h2-5)
* [6.数以百计的SugarCRM服务器被感染恶意程序](#h2-6)

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