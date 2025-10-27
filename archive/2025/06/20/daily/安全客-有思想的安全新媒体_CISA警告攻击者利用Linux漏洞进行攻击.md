---
title: CISA警告攻击者利用Linux漏洞进行攻击
url: https://www.anquanke.com/post/id/308641
source: 安全客-有思想的安全新媒体
date: 2025-06-20
fetch_date: 2025-10-06T22:51:18.285591
---

# CISA警告攻击者利用Linux漏洞进行攻击

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

# CISA警告攻击者利用Linux漏洞进行攻击

阅读量**104701**

发布时间 : 2025-06-19 16:06:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-warns-of-attackers-exploiting-linux-flaw-with-poc-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CISA 已警告美国联邦机构，攻击者以 Linux 内核的 OverlayFS 子系统中的一个高严重性漏洞为目标，该漏洞允许他们获得 root 权限。

此本地权限提升安全漏洞 （CVE-2023-0386） 是由 Linux 内核不当的所有权管理漏洞引起的，于 2023 年 1 月修补，并在两个月后公开披露。

从 2023 年 5 月开始，GitHub 上还分享了多个概念验证 （PoC） 漏洞利用，使漏洞利用尝试更容易实现，并将漏洞推向 Linux 管理员修补优先级列表的顶部。

根据 Datadog Security Labs 的分析，CVE-2023-0386 很容易被利用，并且会影响广泛的 Linux 发行版，包括 Debian、Red Hat、Ubuntu 和 Amazon Linux 等流行的发行版，如果它们使用的内核版本低于 6.2。

“Linux 内核包含一个不正确的所有权管理漏洞，在用户如何将支持的文件从 nosuid 挂载复制到另一个挂载中，在 Linux 内核的 OverlayFS 子系统中发现了对具有功能的 setuid 文件的执行的未经授权的访问，”CISA 解释说。“此 uid 映射错误允许本地用户提升他们在系统上的权限。”

根据 2021 年 11 月的约束性作指令 （BOD） 22-01 的规定，美国联邦机构现在必须保护其网络免受针对添加到 CISA 已知利用漏洞目录中的 CVE-2023-0386 漏洞的持续攻击。

网络安全机构已给联邦民事行政部门 （FCEB） 机构三周时间，以便在 7 月 8 日之前修补其 Linux 系统。

“这些类型的漏洞是恶意网络行为者的频繁攻击媒介，并对联邦企业构成重大风险，”CISA 在一份公告中表示，该公告将 CVE-2023-0386 标记为自修补以来首次被积极利用。

周二，Qualys 威胁研究小组 （TRU） 的安全研究人员还警告说，威胁行为者可以利用最近修补的两个本地权限提升 （LPE） 漏洞，在运行主要 Linux 发行版的系统上取得根。

Qualys TRU 开发了概念验证漏洞，并成功以 CVE-2025-6019 为目标，以获得 Debian、Ubuntu、Fedora 和 openSUSE 系统的 root 权限。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-warns-of-attackers-exploiting-linux-flaw-with-poc-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308641](/post/id/308641)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-warns-of-attackers-exploiting-linux-flaw-with-poc-exploit/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-warns-of-attackers-exploiting-linux-flaw-with-poc-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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