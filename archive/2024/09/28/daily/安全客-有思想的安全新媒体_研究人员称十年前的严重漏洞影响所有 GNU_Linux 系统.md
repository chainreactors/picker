---
title: 研究人员称十年前的严重漏洞影响所有 GNU/Linux 系统
url: https://www.anquanke.com/post/id/300491
source: 安全客-有思想的安全新媒体
date: 2024-09-28
fetch_date: 2025-10-06T18:22:35.604584
---

# 研究人员称十年前的严重漏洞影响所有 GNU/Linux 系统

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

# 研究人员称十年前的严重漏洞影响所有 GNU/Linux 系统

阅读量**116658**

发布时间 : 2024-09-27 14:28:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 迪巴·艾哈迈德，文章来源：hackread

原文地址：<https://hackread.com/old-vulnerability-9-9-impacts-all-gnu-linux-systems/>

译文仅供参考，具体内容表达以及含义原文为准。

一位研究人员声称发现了一个十年前的漏洞，评级为 9.9，该漏洞影响了所有 GNU/Linux 系统，使攻击者能够控制易受攻击的设备。该漏洞正在调查中，预计将于下周全面披露。

网络安全研究员和 Linux 开发人员 Simone Margaritelli 发现了一个关键的 Linux 漏洞，该漏洞可能允许攻击者完全控制易受攻击的系统。此 Linux 漏洞会影响 GNU/Linux 系统，特别是针对 Linux 远程代码执行。如果得到证实，它可能是历史上最严重的漏洞之一。

## 十年前的缺陷：

据报道，该漏洞已经存在了十多年，影响了所有 GNU/Linux 系统。虽然具体细节仍处于保密状态，但 Canonical 和 Red Hat 等主要 Linux 分销商确认的严重性评分为 9.9 分（满分 10 分），这表明如果被利用，可能会造成巨大的损害。

## 争议：

尽管问题严重，但尚未分配通用漏洞和披露 （CVE） 标识符，开发人员仍在争论漏洞的某些方面是否构成安全风险。这种分歧导致延迟解决问题，并导致安全研究人员感到沮丧。

Margaritelli 公开表达了他对披露处理方式的失望。他声称已经提供了概念验证漏洞，但开发人员更专注于讨论漏洞的影响，而不是努力寻找解决方案。

因此，他决定不进行负责任的披露，而是完全披露缺陷。虽然他的决定可能会加速修复竞赛，但如果不采取迅速的对策，也会使数百万个 Linux 系统面临恶意攻击。

供您参考，Simone Margaritelli，又名 evilsocket，是一位著名的网络安全专家，他为世界各地的专业人士和研究人员创造了许多工具。他最显着的贡献之一是 Bettercap，这是一个专为中间人 （MITM） 黑客攻击和网络渗透测试而设计的开源工具。

该漏洞可能会影响已知暴露的服务（如 OpenSSH）和可能的过滤服务（如 Net Filter），尽管没有迹象表明哪些服务可能会受到影响，这些只是假设。

根据最新更新，该漏洞最初将于 9 月 30 日披露到 Openwall 安全邮件列表，然后在 10 月 6 日完全公开披露。建议 Linux 用户在补丁可用时立即了解官方更新和补丁系统。

> \* 未经身份验证的 RCE 与 3 周前披露的所有 GNU/Linux 系统（以及其他系统）的对比。
> \* 在 2 周内完成完全披露（与开发人员达成协议）。
> \* 仍然没有分配 CVE（至少应该有 3 个，可能是 4 个，最好是 6 个）。
> \* 仍然没有有效的修复。
> \* Canonical、RedHat 和…pic.twitter.com/N2d1rm2VeR
>
> — 西蒙娜·玛格丽特利 （@evilsocket） September 23， 2024

软件安全平台 Sonatype 的首席技术官兼开源安全基金会管理委员会成员 Brian Fox 发现，此漏洞与 **Log4j/Log4Shell** 漏洞 （CVE-2021-44228） 之间存在相似之处。Fox 正在与 Sonatype 的研究团队和开源安全社区密切合作，以了解问题的严重性和可能的缓解方法。

“虽然我们还没有技术细节，但 9.9 CVSS 的漏洞表明利用的复杂性较低，并且有迹象表明系统核心存在缺陷。考虑到这是 Linux，这个漏洞的范围很广，成功利用可能是毁灭性的——从 wifi 路由器到保持灯亮的网格，一切都在 Linux 上运行，“Brain 解释说。

“他进一步补充道：”这种低复杂性和高使用率的组合让人想起 Log4Shell，尽管这里的使用规模要大得多。我理解逐步取消披露的逻辑，因为这个漏洞需要时间来发现和修复，但是，我们也应该预料到威胁行为者会仔细检查提交历史并寻找可以利用的线索。

“在我们等待更多细节公布的同时，企业安全团队必须搜索他们的环境和 SBOM，以了解他们可能容易受到攻击的地方并准备好修补。取消你的假期，因为在 10 月 6 日，这可能是一场与攻击者的赛跑，“Brian 强调说。

本文翻译自hackread [原文链接](https://hackread.com/old-vulnerability-9-9-impacts-all-gnu-linux-systems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300491](/post/id/300491)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/old-vulnerability-9-9-impacts-all-gnu-linux-systems/)

如若转载,请注明出处： <https://hackread.com/old-vulnerability-9-9-impacts-all-gnu-linux-systems/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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

* [十年前的缺陷：](#h2-0)
* [争议：](#h2-1)

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