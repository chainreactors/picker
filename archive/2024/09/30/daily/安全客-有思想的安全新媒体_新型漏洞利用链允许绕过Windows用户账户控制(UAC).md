---
title: 新型漏洞利用链允许绕过Windows用户账户控制(UAC)
url: https://www.anquanke.com/post/id/300536
source: 安全客-有思想的安全新媒体
date: 2024-09-30
fetch_date: 2025-10-06T18:20:06.564540
---

# 新型漏洞利用链允许绕过Windows用户账户控制(UAC)

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

# 新型漏洞利用链允许绕过Windows用户账户控制(UAC)

阅读量**149807**

发布时间 : 2024-09-29 15:48:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/vulnerabilities-threats/exploit-chain-windows-uac-bypass>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员已将他们正在跟踪的弱点标记为 CVE-2024-6769，并将其称为 Windows 中的组合用户访问控制 （UAC） 绕过/权限提升漏洞。他们警告说，它可能允许经过身份验证的攻击者获得完整的系统权限。

这是根据 Fortra 的说法，Fortra 在通用漏洞评分系统 （CVSS） 量表上为该问题分配了 6.7 分（满分 10 分）的中等严重性评分。它的概念验证漏洞表明“您有能力关闭系统，”Fortra 安全研发副总监 Tyler Reguly 强调说。“驱动器上的某些位置可以写入和删除以前无法写入和删除的文件。”这包括 C：\Windows，因此攻击者可以获得 SYSTEM 拥有的文件的所有权。

就其本身而言，Microsoft 承认了这项研究，但表示它不认为这是一个实际的漏洞，因为它属于其可接受性的概念，即拥有“不健壮”的安全边界。

## 了解 Windows 中的完整性级别

要了解 Fortra 的发现，我们必须回到 Windows Vista，当时 Microsoft 引入了强制完整性控制 （MIC） 模型。简而言之，MIC 为每个用户、进程和资源分配了一个访问级别，称为完整性级别。所有人都享有低完整性级别，经过身份验证的用户为中等，管理员为高完整性级别，而系统则只为最敏感和最强大的用户提供。

除了这些完整性级别之外，还有 UAC，这是一种安全机制，默认情况下，它在中等级别运行大多数进程和应用程序，并且需要显式权限才能执行任何需要更高权限的操作。通常，管理员级别的用户只需右键单击命令提示符并选择“以管理员身份运行”即可升级。

通过结合两种漏洞利用技术，Fortra 研究人员在他们的概念验证中展示了已经授权的用户如何通过该系统，跳过对中等完整性级别施加的安全边界以获得完整的管理权限，所有这些都不会触发 UAC。

## 使用 CVE-2024-6769 跨越用户边界

要利用 CVE-2024-6769，攻击者首先必须在目标系统中立足。这需要普通用户的中等完整性级别权限，并且触发攻击的帐户必须属于系统的管理组（如果不是因为 UAC 挡路，该帐户类型可以升级到管理员权限）。

攻击的第一步涉及将目标系统的根驱动器（例如“C：”）重新映射到其控制下的位置。这也将移动 “system32” 文件夹，许多服务都依赖该文件夹来加载关键系统文件。

其中一种服务是 CTF Loader ctfmon.exe，它在没有管理员权限的情况下以高完整性级别运行。如果攻击者在 copycat system32 文件夹中放置了一个特制的山寨 DLL，ctfmon.exe将加载它并以该高完整性级别执行攻击者的代码。

接下来，如果攻击者希望获得完全管理权限，他们可以毒害激活上下文缓存，Windows 使用该缓存加载特定版本的库。为此，他们在缓存中创建一个条目，指向攻击者生成的文件夹中的合法系统 DLL 的恶意版本。通过向客户端/服务器运行时子系统 （CSRSS） 服务器发送特制消息，伪造文件由具有管理员权限的进程加载，从而授予攻击者对系统的完全控制权。

## Microsoft：不是漏洞

尽管存在权限提升的可能性，但 Microsoft 拒绝将此问题视为漏洞。在 Fortra 报告后，该公司通过指出 Microsoft Windows 安全服务标准的“非边界”部分作为回应，该部分概述了“某些 Windows 组件和配置明确不旨在提供强大的安全边界”。在相关的“Administrator to Kernel”部分下，它写道：

> 管理进程和用户被视为 Windows 可信计算基础 （TCB） 的一部分，因此与内核边界没有严格隔离。管理员可以控制设备的安全性，并可以禁用安全功能、卸载安全更新以及执行其他使内核隔离无效的操作。

从本质上讲，Reguly 解释说，“他们将 admin 到 system 的边界视为不存在的边界，因为 admin 在主机上是受信任的。换句话说，如果管理员用户最终可以执行相同的系统级操作，但需要 UAC 批准，则 Microsoft 不会将 CVE-2024-6769 视为漏洞。

在给 Dark Reading 的一份声明中，Microsoft 发言人强调，“该方法需要 Administrator 组的成员资格，因此所谓的技术只是利用不会跨越安全边界的预期权限或特权。

Reguly 和 Fortra 不同意 Microsoft 的观点。“当 UAC 推出时，我认为我们都相信 UAC 是一项出色的新安全功能，而 Microsoft 有修复安全功能旁路的历史，”他说。“因此，如果他们说这是一个可以跨越的信任边界，那么他们实际上是在对我说 UAC 不是一项安全功能。这是某种有用的机制，但实际上与安全无关。我认为这是一个非常强烈的哲学差异。

## Windows 商店仍应提防 UAC 绕过风险

撇开哲学上的差异不谈，Reguly 强调，企业需要意识到允许低完整性管理员升级其权限以获得完全系统控制的风险。

在 CVE-2024-6769 漏洞利用结束时，攻击者将拥有完全控制权来操纵或删除关键系统文件、上传恶意软件、建立持久性、禁用安全功能、访问潜在的敏感数据等。

“值得庆幸的是，只有管理员会受到此影响，这意味着您的大多数标准用户都不会受到影响，”Fortra 在给记者的常见问题解答中指出。“对于管理员来说，确保您没有运行来源无法验证的二进制文件非常重要。然而，对于这些管理员来说，警惕是目前最好的防御措施。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/vulnerabilities-threats/exploit-chain-windows-uac-bypass)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300536](/post/id/300536)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/vulnerabilities-threats/exploit-chain-windows-uac-bypass)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/exploit-chain-windows-uac-bypass>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25

### 热门推荐

文章目录

* [了解 Windows 中的完整性级别](#h2-0)
* [使用 CVE-2024-6769 跨越用户边界](#h2-1)
* [Microsoft：不是漏洞](#h2-2)
* [Windows 商店仍应提防 UAC 绕过风险](#h2-3)

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