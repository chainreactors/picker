---
title: 新恶意软件技术可利用 Windows UI 框架规避 EDR 工具
url: https://www.anquanke.com/post/id/302691
source: 安全客-有思想的安全新媒体
date: 2024-12-14
fetch_date: 2025-10-06T19:37:36.120571
---

# 新恶意软件技术可利用 Windows UI 框架规避 EDR 工具

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

# 新恶意软件技术可利用 Windows UI 框架规避 EDR 工具

阅读量**107848**

发布时间 : 2024-12-13 10:15:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/new-malware-technique-could-exploit.html>

译文仅供参考，具体内容表达以及含义原文为准。

一种新设计的技术利用名为 “用户界面自动化”（UI Automation，UIA）的 Windows 可访问性框架来执行各种恶意活动，而不会引起端点检测和响应（EDR）解决方案的注意。

“要利用这种技术，必须说服用户运行一个使用 UI Automation 的程序，”Akamai 安全研究员 Tomer Peled 在与 The Hacker News 分享的一份报告中说。“这可能会导致隐蔽命令的执行，从而获取敏感数据、将浏览器重定向到钓鱼网站等。”

更糟糕的是，本地攻击者可以利用这一安全盲点执行命令，并从/向 Slack 和 WhatsApp 等消息应用程序读/写消息。除此之外，它还有可能被武器化，通过网络操纵用户界面元素。

作为微软 .NET Framework 的一部分，UI Automation 最早出现在 Windows XP 中，旨在提供对各种用户界面（UI）元素的编程访问，帮助用户使用辅助技术产品（如屏幕阅读器）进行操作。它还可用于自动测试场景。

“微软在一份支持文档中指出：”辅助技术应用程序通常需要访问受保护的系统用户界面元素，或访问可能以更高权限级别运行的其他进程。“因此，辅助技术应用程序必须得到系统的信任，并且必须以特殊权限运行。”

“要访问更高的 IL 进程，辅助技术应用程序必须在应用程序的清单中设置 UIAccess 标志，并由具有管理员权限的用户启动。”

通过使用组件对象模型（COM）作为进程间通信（IPC）机制，实现了用户界面与其他应用程序中元素的交互。这使得创建 UIA 对象成为可能，通过设置事件处理程序，当检测到某些用户界面变化时就会触发该事件处理程序，从而实现与焦点应用程序的交互。

Akamai的研究发现，这种方法也可能为滥用开辟一条途径，使恶意行为者能够读/写信息、窃取在网站上输入的数据（如支付信息），并在浏览器中当前显示的网页刷新或更改时执行命令，将受害者重定向到恶意网站。

佩莱德指出：“除了当前屏幕上显示的、我们可以与之交互的用户界面元素外，还有更多元素被提前加载并置于缓存中。我们还可以与这些元素进行交互，比如阅读屏幕上未显示的信息，甚至可以设置文本框并发送信息，而屏幕上却不会反映出来。”

尽管如此，值得注意的是，这些恶意场景都是 UI Automation 的预期功能，就像 Android 的辅助服务 API 已成为恶意软件从被入侵设备中提取信息的主要方式一样。

“这又回到了应用程序的预期目的： 这些权限级别必须存在才能使用，”Peled 补充说。“这就是 UIA 能够绕过 Defender 的原因–该应用程序没有发现任何异常。如果某些东西被视为功能而不是错误，那么机器的逻辑就会遵循这一功能。”

**从 COM 到 DCOM：横向移动攻击向量**

Deep Instinct 在披露这一信息的同时，还揭露了允许软件组件通过网络通信的分布式 COM (DCOM) 远程协议，该协议可被用于远程编写自定义有效载荷，以创建嵌入式后门。

安全研究人员 Eliran Nissan 说，这种攻击 “允许在目标计算机上编写自定义 DLL，将其加载到服务中，并使用任意参数执行其功能。这种类似后门的攻击滥用了 IMsiServer COM 接口。”

尽管如此，这家以色列网络安全公司指出，这种攻击会留下明显的破坏迹象（IoCs），可以被检测和阻止。此外，它还要求攻击者和受害者的机器处于同一域中。

日产说：“到目前为止，由于基于 IDispatch 的 COM 对象具有可编写脚本的特性，因此 DCOM 横向移动攻击只针对这些对象进行研究。新的’DCOM Upload & Execute’方法远程将自定义有效载荷写入受害者的[Global Assembly Cache]，从服务上下文中执行这些有效载荷，并与它们通信，有效地发挥了嵌入式后门的作用。”

“这里介绍的研究证明，许多意想不到的 DCOM 对象都可能被利用来进行横向移动，因此应调整适当的防御措施。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/new-malware-technique-could-exploit.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302691](/post/id/302691)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/new-malware-technique-could-exploit.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/new-malware-technique-could-exploit.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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