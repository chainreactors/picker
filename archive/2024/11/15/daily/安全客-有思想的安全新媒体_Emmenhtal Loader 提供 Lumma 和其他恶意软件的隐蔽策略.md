---
title: Emmenhtal Loader 提供 Lumma 和其他恶意软件的隐蔽策略
url: https://www.anquanke.com/post/id/301831
source: 安全客-有思想的安全新媒体
date: 2024-11-15
fetch_date: 2025-10-06T19:13:41.542885
---

# Emmenhtal Loader 提供 Lumma 和其他恶意软件的隐蔽策略

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

# Emmenhtal Loader 提供 Lumma 和其他恶意软件的隐蔽策略

阅读量**86217**

发布时间 : 2024-11-14 15:25:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/emmenhtal-loaders-stealthy-tactics-for-delivering-lumma-and-other-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Emmenhtal Loader]()

威胁的发展日新月异，攻击者不断改进其技术以躲过防御。Emmenhtal 就是这些潜在威胁之一，它是一种恶意软件加载器，采用 LOLBAS（Living Off the Land Binaries and Scripts，离岸二进制文件和脚本）策略来隐蔽地分发恶意软件。

据 ANY.RUN 的研究人员称，Emmenhtal 利用脚本分发 Lumma、Arechclient2、Hijackloader 和 Amadey 等病毒，每个病毒都经过精心伪装，以逃避检测。

让我们深入探讨 Emmenhtal 用来保持隐蔽性的策略，并分解其执行链以了解其运作方式。我们将使用受控环境来分析这一恶意软件活动。

**Emmenhtal 加载程序概述**

Emmenhtal 载入器出现于 2024 年初。它采用 LOLBAS 技术，利用合法的 Windows 工具躲过检测系统。

它将自身嵌入修改过的系统二进制文件中，通过层层加密脚本执行有效载荷。它的感染过程经常使用 HTA（HTML 应用程序）文件和 PowerShell 脚本，这使得使用标准安全工具识别它成为一项重大挑战。

通过 ANY.RUN 脚本跟踪器等工具可以轻松检查 Emmenhtal 使用的脚本。

![]()在 ANY.RUN 沙盒中分析的恶意脚本

**艾门塔尔执行链分解**

我们可以通过检查 Emmenhtal 载入器如何在 ANY.RUN 的交互式沙盒中传输 Lumma 来查看其执行链。

![]()

艾门塔尔加载器的执行链

**初始阶段： LNK 文件**

该过程以 .LNK 文件开始，该文件通常伪装成无害的样子，用于启动 Forfiles 命令。

该文件的目的是在不提醒用户的情况下触发感染链。在 ANY.RUN 沙盒中，我们可以看到 forfiles.exe 进程出现在进程树中。

![]()进程树中出现的 Forefiles

![]()ANY.RUN 沙盒中的 Forefiles.exe

**第二阶段： 执行 PowerShell 和启动 Mshta**

随着艾门塔尔加载程序在其执行链中的推进，第二阶段开始启动 PowerShell，这在推进感染中起着至关重要的作用。PowerShell 是 LOLBAS 技术中常用的工具，因为它具有多功能性并与 Windows 集成，因此成为 Emmenhtal 幕后黑手等威胁行为者的首选。

对于分析 Emmenhtal 的网络安全专业人员来说，ANY.RUN 的沙盒提供了一个受控环境，可以实时观察每种策略。

通过查看屏幕右侧的 MITRE ATT&CK 矩阵，您可以看到 Emmenhtal 的技术与对手既定战术的映射关系，从而有助于更好地了解其方法。

![]()在 ANY.RUN 沙盒内启动 PowerShell 技术

感染链的下一步涉及 PowerShell 启动 Mshta。Mshta 被指示从远程服务器下载加密有效载荷。

![]()ANY.RUN 沙箱检测到的 Mshta.exe

下载 Mshta 之后，PowerShell 会运行一个 BASE64 编码的命令。这种混淆技术可使命令看起来像一串随机字符，从而隐藏其真实意图，不被随意检查到。解码后，该命令会显示 Emmenhtal 加载器执行过程的下一步，为启动最终有效载荷做准备。

![]()ANY.RUN 检测到的 BASE64 编码 PowerShell 命令

**由 Emmenhtal 加载器启动有效载荷**

此执行链中的最后一个 PowerShell 脚本是 Emmenhtal 加载器，它会启动一个有效载荷，通常是 Updater.exe，以及一个以生成的名称作为参数的二进制文件。这一步将 Emmenhtal 从加载器阶段过渡到实际恶意软件的交付阶段。

在我们的示例中，Emmenhtal 确实启动了 Updater.exe，如沙箱内所示。

![]()Emmenhtal 载入器交付 Lumma 恶意软件

**系统感染和 Lumma 发送**

随着 Updater.exe 的激活，Emmenhtal 载入器通过发送 Lumma 恶意软件完成了感染链。此时，Lumma 会成功感染系统，并启动其预期的恶意活动。

![]()Lumma 恶意软件触发的 Suricata 规则

**使用 ANY.RUN 安全地调查威胁**

艾门塔尔加载器是一种隐秘的恶意软件，它利用合法的 Windows 实用程序和混淆脚本逃避检测。不过，有了正确的工具，识别和阻止其活动就成为可能。

ANY.RUN 的交互式沙盒可让您在安全、受控的环境中探索 Emmenhtal 和其他复杂恶意软件的行为。

本文翻译自securityonline [原文链接](https://securityonline.info/emmenhtal-loaders-stealthy-tactics-for-delivering-lumma-and-other-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301831](/post/id/301831)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/emmenhtal-loaders-stealthy-tactics-for-delivering-lumma-and-other-malware/)

如若转载,请注明出处： <https://securityonline.info/emmenhtal-loaders-stealthy-tactics-for-delivering-lumma-and-other-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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