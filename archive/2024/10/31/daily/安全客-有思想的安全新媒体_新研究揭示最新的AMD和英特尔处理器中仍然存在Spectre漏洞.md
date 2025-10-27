---
title: 新研究揭示最新的AMD和英特尔处理器中仍然存在Spectre漏洞
url: https://www.anquanke.com/post/id/301411
source: 安全客-有思想的安全新媒体
date: 2024-10-31
fetch_date: 2025-10-06T18:51:23.981514
---

# 新研究揭示最新的AMD和英特尔处理器中仍然存在Spectre漏洞

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

# 新研究揭示最新的AMD和英特尔处理器中仍然存在Spectre漏洞

阅读量**52700**

发布时间 : 2024-10-30 16:01:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/new-research-reveals-spectre.html>

译文仅供参考，具体内容表达以及含义原文为准。

在影响现代CPU处理器的Spectre安全漏洞曝光六年后多，新的研究发现最新的AMD和英特尔处理器仍然容易受到推测执行攻击。

这项由苏黎世联邦理工学院（ETH Zürich）的研究员Johannes Wikner和Kaveh Razavi披露的攻击，旨在破坏x86芯片上的间接分支预测器屏障（IBPB），这是对抗推测执行攻击的关键缓解措施。

推测执行是指现代CPU通过预测程序将采取的分支提前，按非顺序执行某些指令的性能优化功能，从而在推测使用的值正确时加快任务处理。
如果结果出现误预测，这些被称为瞬态的指令将被声明无效并取消，然后处理器才能用正确的值恢复执行。

虽然瞬态指令的执行结果不会提交到架构程序状态，但它仍然可能通过强制误预测将某些敏感数据加载到处理器缓存中，从而使恶意对手得以访问原本无法访问的数据。

英特尔将IBPB描述为一种“间接分支控制机制，它建立一个屏障，防止在屏障之前执行的软件控制同一逻辑处理器上在屏障之后执行的间接分支的预测目标。”

它被用作帮助对抗分支目标注入（BTI），即Spectre v2（CVE-2017-5715），一种跨域瞬态执行攻击（TEA），利用处理器使用的间接分支预测器导致披露小工具被推测执行。

披露小工具指的是攻击者能够访问受害者秘密的能力，这些秘密在架构上原本是不可见的，并通过隐蔽通道将其窃取。

苏黎世联邦理工学院的最新发现表明，英特尔微架构（如Golden Cove和Raptor Cove）中的微码错误可能被用来绕过IBPB。这种攻击被描述为第一个实用的“跨进程Spectre泄露”的端到端攻击。

研究人员表示，这个微码缺陷“保留了分支预测，即使IBPB应该已经使其无效，它们仍然可能被使用。”这种屏障后的推测允许攻击者绕过进程上下文和虚拟机施加的安全边界。

研究发现，由于Linux内核应用IBPB的方式，AMD的IBPB版本也可以被类似地绕过，导致一个代号为Post-Barrier Inception（即PB-Inception）的攻击，使未授权的对手能够泄露AMD Zen 1(+)和Zen 2处理器上的特权内存。
英特尔已经发布了微码补丁来解决这个问题（CVE-2023-38575，CVSS分数：5.5）。AMD方面，根据2022年11月发布的公告，正在跟踪这个漏洞，编号为CVE-2022-23824。

研究人员说：“英特尔用户应确保他们的intel-microcode是最新的。AMD用户应确保安装内核更新。”

这次披露发生在苏黎世联邦理工学院研究人员详细介绍了新的RowHammer攻击技术几个月后，这些技术被代号命名为ZenHammer和SpyHammer，后者使用RowHammer以高精度推断DRAM温度。

研究指出，“RowHammer对温度变化非常敏感，即使变化非常小（例如，±1°C）。随着温度的升高，RowHammer诱导的位错误率持续增加（或减少），一些容易受到RowHammer影响的DRAM单元只在特定温度下出现位错误。”

通过利用RowHammer与温度之间的相关性，攻击者可以识别计算机系统的使用情况并测量环境温度。这种攻击还可以通过使用温度测量来确定个人在家的习惯以及他们进出房间的时间，从而侵犯隐私。

研究人员指出，“SpyHammer是一种简单有效的攻击，可以在不需要对受害者系统进行修改或事先了解的情况下，监视关键系统的温度。”

“在采用一个明确且完全安全的RowHammer防御机制之前，SpyHammer可能对系统的安全和隐私构成潜在威胁，这是一个巨大的挑战，因为RowHammer漏洞随着技术缩放而持续恶化。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/new-research-reveals-spectre.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301411](/post/id/301411)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/new-research-reveals-spectre.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/new-research-reveals-spectre.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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