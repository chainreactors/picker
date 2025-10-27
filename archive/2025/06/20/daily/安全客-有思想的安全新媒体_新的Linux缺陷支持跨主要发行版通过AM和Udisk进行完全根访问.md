---
title: 新的Linux缺陷支持跨主要发行版通过AM和Udisk进行完全根访问
url: https://www.anquanke.com/post/id/308613
source: 安全客-有思想的安全新媒体
date: 2025-06-20
fetch_date: 2025-10-06T22:51:27.637650
---

# 新的Linux缺陷支持跨主要发行版通过AM和Udisk进行完全根访问

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

# 新的Linux缺陷支持跨主要发行版通过AM和Udisk进行完全根访问

阅读量**129040**

发布时间 : 2025-06-19 15:43:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html>

译文仅供参考，具体内容表达以及含义原文为准。

[![]()](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXov8Cx_igQW4qij-AsFmuK3PvE_68RZF_35cguvWlQV8pWKAVOOf1DIWk6ZpL8eriWkF1Pdwlkx7GmolL2yQeknbGs1F7QwEdF6Bu3dvIl6t7CatxuL7USxwGjM166GTEcOq-XK3g_bteqdnY27DijtddyJhVZ3M8PVBoXN5cqb7_h9UVwKBs0h1O3omK/s728-rw-e365/Linux-LPE.jpg)![]()
网络安全研究人员发现了两个本地权限提升 （LPE） 漏洞，这些漏洞可能被用来在运行主要 Linux 发行版的机器上获得 root 权限。

Qualys 发现的漏洞如下 –

* **CVE-2025-6018** – SUSE 15 的可插拔身份验证模块 （PAM） 中的 LPE 从非特权变为 allow\_active)
* **CVE-2025-6019** – LPE 通过 udisks 守护程序从 allow\_active 到 libblockdev 中的 root

“这些现代的’本地到根’漏洞利用缩小了普通登录用户和完整系统接管之间的差距，”Qualys 威胁研究部门 （TRU） 高级经理 Saeed Abbasi 说。

“通过链接合法服务，例如 udisks 循环挂载和 PAM/环境怪癖，拥有任何活动 GUI 或 SSH 会话的攻击者可以跨越 polkit 的 allow\_active 信任区，并在几秒钟内成为 root。”

这家网络安全公司表示，CVE-2025-6018 存在于 openSUSE Leap 15 和 SUSE Linux Enterprise 15 的 PAM 配置中，使非特权本地攻击者能够提升为“allow\_active”用户并调用 Polkit作，否则这些作是为实际存在的用户保留的。

另一方面，CVE-2025-6019 会影响 libblockdev，并且可通过大多数 Linux 发行版默认包含的 udisks 守护程序进行利用。它实质上允许“allow\_active”用户通过与 CVE-2025-6018 链接来获得完全的 root 权限。

“虽然它名义上需要’allow\_active’权限，但 udisks 默认在几乎所有 Linux 发行版上都提供，因此几乎任何系统都容易受到攻击，”Abbasi 补充道。“获得’allow\_active’的技术，包括这里披露的 PAM 问题，进一步消除了这一障碍。”

一旦获得 root 权限，攻击者就可以全权访问系统，允许他们将其用作跳板，进行更广泛的入侵后作，例如更改安全控制和植入后门以进行秘密访问。

Qualys 表示，它已经开发了概念验证 （PoC） 漏洞利用，以确认各种作系统（包括 Ubuntu、Debian、Fedora 和 openSUSE Leap 15）上存在这些漏洞。

为了降低这些缺陷带来的风险，必须应用 Linux 发行版供应商提供的补丁。作为临时解决方法，用户可以修改“org.freedesktop.udisks2.modify-device”的 Polkit 规则，以要求管理员身份验证（“auth\_admin”）。

## Linux PAM 中披露的缺陷

此次披露是在 Linux PAM 的维护者解决了一个高严重性路径遍历漏洞（**CVE-2025-6020，CVSS** 评分：7.8）之际，该漏洞也可能允许本地用户升级到 root 权限。此问题已在版本 1.7.1 中修复。

Linux PAM 维护者 Dmitry V. Levin 说：“在 linux-pam <= 1.7.0 中pam\_namespace的模块可能会在没有适当保护的情况下访问用户控制的路径，这允许本地用户通过多个符号链接攻击和竞争条件将其权限提升到 root。

如果 Linux 系统使用 pam\_namespace 设置多实例化目录，而多实例化目录或实例目录的路径由用户控制，则容易受到攻击。作为 CVE-2025-6020 的解决方法，用户可以禁用 pam\_namespace 或确保它不在用户控制的路径上运行。

ANSSI 的 Olivier Bal-Petre 于 2025 年 1 月 29 日向维护者报告了该漏洞，他表示，如果用户不使用其发行版提供的脚本，则还应更新他们的 namespace.init 脚本，以确保两条路径中的任何一条都可以安全地以 root 身份进行作。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308613](/post/id/308613)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html)

如若转载,请注明出处： <https://thehackernews.com/2025/06/new-linux-flaws-enable-full-root-access.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Linux PAM 中披露的缺陷](#h2-0)

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