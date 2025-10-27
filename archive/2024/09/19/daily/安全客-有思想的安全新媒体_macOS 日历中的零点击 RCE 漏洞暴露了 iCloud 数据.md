---
title: macOS 日历中的零点击 RCE 漏洞暴露了 iCloud 数据
url: https://www.anquanke.com/post/id/300161
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:14.448191
---

# macOS 日历中的零点击 RCE 漏洞暴露了 iCloud 数据

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

# macOS 日历中的零点击 RCE 漏洞暴露了 iCloud 数据

阅读量**88018**

发布时间 : 2024-09-18 15:00:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/vulnerabilities-threats/zero-click-rce-bug-macos-calendar-exposes-icloud-data>

译文仅供参考，具体内容表达以及含义原文为准。

macOS 中严重性为严重性、中等和低严重性的漏洞链的零点击可能使攻击者能够破坏 macOS 的品牌安全保护，并最终损害受害者的 iCloud 数据。

故事始于 Calendar 活动附件缺乏清理。从那时起，研究人员 Mikko Kenttälä 发现，他可以在目标系统上实现远程代码执行 （RCE），并访问敏感数据 – 在他的实验中，他使用了 iCloud 照片。该过程中的任何步骤都不需要任何用户交互，Apple 的 Gatekeeper 和 Transparency， Consent， and Control （TCC） 保护措施都无法阻止它。

## macOS 中的 Zero-Click 漏洞利用链

早在 2023 年 2 月，链中最重要的第一个漏洞 CVE-2022-46723 就被授予 CVSS 评分 9.8 分（满分 10 分），为“严重”。

它不仅危险，而且很容易利用。攻击者可以简单地向受害者发送包含恶意文件的日历邀请。由于 macOS 未能正确审查文件名，攻击者可以任意命名它，从而产生各种有趣的效果。

例如，他们可以以删除特定的、预先存在的系统文件为目标来命名它。如果他们为其指定与现有文件相同的名称，然后删除用于传递该文件的日历事件，则无论出于何种原因，系统都会删除恶意文件和它模仿的原始文件。

更危险的是攻击者执行路径遍历的可能性，以这样一种方式命名他们的附件，使其能够逃离 Calendar 的沙箱（应该保存附件）到系统上的其他位置。

Kenttälä 使用这种任意文件写入能力来利用操作系统升级（在发现时，macOS Ventura 即将发布）。首先，他创建了一个文件，模拟 Siri 建议的重复日历事件，隐藏了在迁移过程中触发更多文件执行的警报。其中一个后续文件负责将旧日历数据迁移到新系统。另一个允许他从 Samba（开源服务器消息块 （SMB） 协议）挂载网络共享，而不会触发安全标志。另外两个文件触发了恶意应用程序的启动。

## 破坏 Apple 的原生安全控制

由于 macOS 的 Gatekeeper 安全功能被绕过，恶意应用程序在没有发出任何警报的情况下悄悄进入——这是 Mac 系统和不受信任的应用程序面临的障碍。它被标记为 CVE-2023-40344，早在 2024 年 1 月就被分配了中等严重性（满分 10 个 CVSS 评级）。

不过，Gatekeeper 并不是唯一在攻击中被破坏的标志性 macOS 安全功能。使用恶意应用程序启动的脚本，Kenttälä 成功地将与 iCloud 照片关联的配置文件替换为恶意配置文件。这将 Photos 重新指向一个自定义路径，在 TCC 保护之外，TCC 是 macOS 用来确保应用程序不会不当访问敏感数据和资源的协议。重新指向的 CVE-2023-40434 — CVSS 严重性评分为“低”3.3 — 为肆意盗窃照片打开了大门，这些照片可以通过“微不足道的修改”泄露到外国服务器。

“MacOS 的 Gatekeeper 和 TCC 对于确保仅安装受信任的软件和管理对敏感数据的访问至关重要，”Critical Start 网络威胁研究高级经理 Callie Guenther 解释说。“然而， macOS 日历中的零点击漏洞表明，攻击者如何通过利用沙盒进程来绕过这些保护。”不过，Guenther 指出，macOS 并不是唯一容易受到这些类型攻击的漏洞：“Windows 中存在类似的漏洞，其中 Device Guard 和 SmartScreen 可以使用权限提升或利用内核漏洞等技术绕过。

例如，她补充说，“攻击者使用 DLL 劫持或沙盒逃逸方法来击败 Windows 安全控制。这两个操作系统都依赖于强大的安全框架，但顽固的对手（尤其是 APT 组织）会想方设法绕过这些防御。

Apple 在 2022 年 10 月至 2023 年 9 月的不同时间点承认并修补了漏洞利用链中的许多漏洞。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/vulnerabilities-threats/zero-click-rce-bug-macos-calendar-exposes-icloud-data)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300161](/post/id/300161)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/vulnerabilities-threats/zero-click-rce-bug-macos-calendar-exposes-icloud-data)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/zero-click-rce-bug-macos-calendar-exposes-icloud-data>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [macOS 中的 Zero-Click 漏洞利用链](#h2-0)
* [破坏 Apple 的原生安全控制](#h2-1)

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