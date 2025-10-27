---
title: Ring 0级固件威胁：新型UEFI rootkit恶意软件BlackLotus曝光
url: https://www.anquanke.com/post/id/282003
source: 安全客-有思想的安全新媒体
date: 2022-10-22
fetch_date: 2025-10-03T20:34:57.952075
---

# Ring 0级固件威胁：新型UEFI rootkit恶意软件BlackLotus曝光

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

# Ring 0级固件威胁：新型UEFI rootkit恶意软件BlackLotus曝光

阅读量**181532**

发布时间 : 2022-10-21 08:17:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 cnbeta，文章来源：cnbeta.com

原文地址：<https://www.cnbeta.com/articles/tech/1329141.htm>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

最近引发广泛讨论的“BlackLotus”，属于一款相当全能的固件级 rootkit 恶意软件。特点是能够躲过各种删除操作，以及绕过先进的 Windows 防护措施。此前这类高级攻击能力，仅被拥有深厚背景的机构所拥有，比如情报威胁组织。然而据报道，一款更新、更强大的 UEFT rootkit，正被人挂到暗网论坛上叫卖。

卖家宣称 BlackLotus 是一款固件级 rootkit 恶意软件，能够绕过 [Windows](https://microsoft.pvxt.net/x9Vg1) 防护措施、并在 x86 架构的最底层运行恶意代码。

率先曝光此事的安全研究人员指出，单个 rootkit 的许可证费用高达 5000 美元，而后续代码重建则只需 200 美元。

不过考虑到卖家罗列出来的功能，即使需要耗费重资，世界各地的网络犯罪分子和黑帽黑客也会趋之若鹜。

Scott Scheferman 总结道：

> BlackLotus 采用了汇编与 C 语言编写，体量仅 80KB（约 81920 字节）。
>
> 通过在内核级别（ring 0）提供‘代理防护’（agent protection），该 rootkit 能够在 UEFI 固件中长期驻留。
>
> 此外 BlackLotus 具有反虚拟机、反调试和代码混淆功能，以阻碍研究人员对其展开分析尝试，且附带功能齐备的安装指南 / 常见问题解答。

与同类 rootkit 一样，BlackLotus 能够在 Windows 启动前的第一阶段被加载，因而能够绕过 Windows / x86 平台上的诸多安全防护措施。

> 除了无视 Secure Boot、UAC、BitLocker、HVCI 和 Windows Defender，该恶意软件还提供了加载未签名驱动程序的能力。
>
> 其它高级功能包括功能齐备的文件传输模式、以及易攻破的签名引导加载程序 —— 除非影响当今仍在使用的数百个引导加载程序，否则很难将它斩草除根。

Scott Scheferman 还强调了 BlackLotus 可能对基于固件的现代安全防护机制构成威胁。

而且新 UEFI rootkit 在易用性、扩展性、可访问性、持久性、规避和破坏潜力方面，都实现了相当大的跨越。

此前人们一度认为这类威胁相当罕见，但过去几天不断被打脸的攻击报告，已经指向了截然不同的未来趋势。

最后，安全社区将对 BlackLotus 恶意软件的实际样本展开更加细致、深入的分析，以确定传闻的真实性、还是说它只是某人精心编造的一个骗局。

本文翻译自cnbeta.com [原文链接](https://www.cnbeta.com/articles/tech/1329141.htm)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282003](/post/id/282003)

安全KER - 有思想的安全新媒体

本文转载自: [cnbeta.com](https://www.cnbeta.com/articles/tech/1329141.htm)

如若转载,请注明出处： <https://www.cnbeta.com/articles/tech/1329141.htm>

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