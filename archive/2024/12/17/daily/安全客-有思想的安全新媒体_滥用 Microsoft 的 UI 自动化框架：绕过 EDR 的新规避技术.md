---
title: 滥用 Microsoft 的 UI 自动化框架：绕过 EDR 的新规避技术
url: https://www.anquanke.com/post/id/302736
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:46.488896
---

# 滥用 Microsoft 的 UI 自动化框架：绕过 EDR 的新规避技术

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

# 滥用 Microsoft 的 UI 自动化框架：绕过 EDR 的新规避技术

阅读量**55099**

发布时间 : 2024-12-16 11:01:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/abusing-microsofts-ui-automation-framework-the-new-evasion-technique-bypassing-edr/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Akamai安全研究员Tomer Peled公布了一种利用微软传统UI自动化框架的新型攻击技术。研究结果揭示了攻击者如何利用该框架绕过现代端点检测和响应（EDR）系统，从而引发重大网络安全问题。

微软的UI自动化框架是在Windows XP时代推出的，旨在帮助残疾用户，提供更高的权限来操作用户界面（UI）元素。根据 Peled 的说法，“UI 自动化需要权限才能操作屏幕上存在的几乎所有 UI 元素”。这种功能虽然有利于无障碍操作，但却为攻击者提供了一条隐秘操作的途径。

Peled 的研究强调了攻击者如何滥用 UI Automation 来达到以下目的：

* 渗出敏感数据，如信用卡详细信息。
* 将浏览器重定向到钓鱼网站。
* 操纵 Slack 和 WhatsApp 等聊天应用程序读写信息。

这种技术最令人担忧的一点是它无法被检测工具发现。Peled 指出：“我们针对这种技术测试过的所有 EDR 技术都无法发现任何恶意活动。”这使它成为威胁行为者的一个有吸引力的选择，尤其是因为它适用于从 XP 开始的所有 Windows 操作系统。

这种攻击利用组件对象模型（COM）来操纵跨应用程序的用户界面元素。通过设置事件处理程序，攻击者可以监控用户界面元素并与之交互，包括从活动窗口读取敏感数据或模拟用户输入以执行命令。

Peled 的报告概述了概念验证（PoC）攻击，以展示威胁的严重性。在一个例子中，攻击者设置了处理程序，以获取在线商家网站上输入的信用卡详细信息。在另一个场景中，浏览器被重定向到使用 UI Automation 的钓鱼网站，从而使攻击者能够部署漏洞或窃取凭证。

![Microsoft UI Automation]()
从 Slack 读取消息 | 来源：Akamai Akamai

即使是消息应用程序也不能幸免。报告详细介绍了攻击者如何利用 Windows UI Automation “读取对话并渗出数据，或设置文本框并发送信息，而不会在屏幕上反映出来”。

UI Automation 框架的传统性质给检测和防范带来了巨大挑战。为了减轻这些威胁，Peled 建议监控加载 UIAutomationCore.dll 的异常进程，并跟踪 UI Automation 打开的命名管道。然而，该框架的固有设计限制了全面检测。

虽然微软已经实施了一些限制措施，如限制 UI Automation 与高权限应用程序的交互，但 Peled 的发现强调了技术熟练的攻击者利用这一攻击载体的潜力。报告总结道：“这项分析是一个不幸的例子，说明了为善的技术是如何被恶意劫持的。”

本文翻译自securityonline [原文链接](https://securityonline.info/abusing-microsofts-ui-automation-framework-the-new-evasion-technique-bypassing-edr/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302736](/post/id/302736)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/abusing-microsofts-ui-automation-framework-the-new-evasion-technique-bypassing-edr/)

如若转载,请注明出处： <https://securityonline.info/abusing-microsofts-ui-automation-framework-the-new-evasion-technique-bypassing-edr/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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