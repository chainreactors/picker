---
title: 如何将 Microsoft Copilot 武器化以供网络攻击者使用
url: https://www.anquanke.com/post/id/298970
source: 安全客-有思想的安全新媒体
date: 2024-08-10
fetch_date: 2025-10-06T17:59:18.168989
---

# 如何将 Microsoft Copilot 武器化以供网络攻击者使用

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

# 如何将 Microsoft Copilot 武器化以供网络攻击者使用

阅读量**39143**

发布时间 : 2024-08-09 14:49:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jeffrey Schwartz，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/application-security/how-to-weaponize-microsoft-copilot-for-cyberattackers>

译文仅供参考，具体内容表达以及含义原文为准。

企业正在快速实施 Microsoft 的基于 Copilot AI 的聊天机器人，希望改变员工收集数据和组织时间和工作的方式。但与此同时，Copilot 也是威胁行为者的理想工具。

安全研究员迈克尔·巴古里（Michael Bargury）是Microsoft Azure安全首席技术官办公室的前高级安全架构师，现在是Zenity的联合创始人兼首席技术官，他表示，攻击者可以使用Copilot搜索数据，在不生成日志的情况下将其泄露，并对受害者进行社交工程到网络钓鱼网站，即使他们不打开电子邮件或点击链接。

今天在拉斯维加斯举行的Black Hat USA上，Bargury展示了Copilot如何像其他聊天机器人一样，容易受到提示注入的影响，使黑客能够逃避其安全控制。

这次简报会名为“靠 Microsoft Copilot 为生”，是 Bargury 多天来的第二次黑帽演讲。在周三的第一次演讲中，Bargury 演示了开发人员如何在不知不觉中构建能够泄露数据或绕过策略和数据丢失预防控制的 Copilot 聊天机器人，这些机器人使用 Microsoft 的机器人创建和管理工具 Copilot Studio。

## Copilot的红队黑客工具

周四的后续会议重点关注与实际聊天机器人相关的各种风险，Bargury 在 GitHub 上发布了 Microsoft 365 的攻击性安全工具集。新的 LOLCopilot 模块是 powerpwn 的一部分，专为 Microsoft Copilot、Copilot Studio 和 Power Platform 设计。

Bargury 将其描述为一个红队黑客工具，展示如何通过提示注入来改变机器人的行为，或者用 Microsoft 的话来说就是“副驾驶”。有两种类型：直接提示注入或越狱，是指攻击者操纵 LLM 提示符以更改其输出。通过间接提示注入，攻击者会修改模型访问的数据源。

使用该工具，Bargury 可以向副驾驶添加直接提示注入，越狱它并修改模型中的参数或指令。例如，他可以在电子邮件中嵌入一个HTML标签，以将正确的银行帐号替换为攻击者的帐号，而无需更改任何参考信息或更改模型，例如使用白色文本或非常小的字体。

“我能够操纵 Copilot 代表您所做的一切，包括它为您提供的回应、它可以代表您执行的每一项操作，以及我如何亲自完全控制对话，”Bargury 告诉 Dark Reading。

此外，该工具可以在不被发现的情况下完成所有这些操作。“这里没有迹象表明这来自不同的来源，”巴古里说。“这仍然指向这个受害者实际创建的有效信息，所以这个线程看起来值得信赖。你看不到任何立即注射的迹象。

## RCE = 远程“副驾驶”执行攻击

Bargury 将 Copilot 提示注入描述为等同于远程代码执行 （RCE） 攻击。虽然副驾驶不运行代码，但他们确实遵循指令、执行操作并根据这些操作创建组合。

“我可以从外面进入你的谈话，并完全控制副驾驶代表你做的所有行动及其输入，”他说。“因此，我是说这相当于LLM应用程序世界中的远程代码执行。

在会议期间，Bargury 演示了他所描述的远程副驾驶执行 （RCE），其中攻击者：

* 操纵副驾驶篡改受害商贩的银行信息，以窃取资金
* 在收益报告发布之前泄露数据 ，以便根据该信息进行交易
* 使 Copilot 成为恶意内部人员，将用户引导至网络钓鱼站点以获取凭据

Bargury 并不是唯一一个研究威胁行为者如何通过立即注入攻击 Copilot 和其他聊天机器人的研究人员。今年 6 月，Anthropic 详细介绍了其 AI 产品的红队测试方法。就其本身而言，Microsoft已经吹捧其在AI安全方面的红队努力已有一段时间了。

## Microsoft的AI红队战略

近几个月来，Microsoft已经解决了新浮出水面的关于提示注射的研究，这些研究有直接和间接的形式。

Microsoft Azure 的首席技术官兼技术研究员 Mark Russinovich 最近在 5 月份的年度 Microsoft Build 会议上讨论了各种 AI 和 Copilot 威胁。他强调了Microsoft新的Prompt Shields的发布，这是一个旨在检测直接和间接提示注入攻击的API。

Russinovich说：“这里的想法是，我们正在寻找迹象表明上下文中嵌入了指令，无论是直接用户上下文还是通过RAG（检索增强生成）输入的上下文，这可能会导致模型行为不端。

Prompt Shields 是 Microsoft 最近推出的一系列 Azure 工具之一，这些工具专为开发人员构建安全的 AI 应用程序而设计。其他新工具包括 Groundedness Detection，用于检测 LLM 输出中的幻觉，以及用于检测应用程序对越狱攻击和创建不当内容的敏感性的安全评估。

Russinovich 还指出了另外两个安全红队的新工具：PyRIT（用于生成式 AI 的 Python 风险识别工具包），这是一个开源框架，用于发现生成式 AI 系统中的风险。另一种是 Crescendomation，它会自动执行 Crescendo 攻击，从而产生恶意内容。此外，他还宣布了Microsoft与HiddenLayer的新合作伙伴关系，HiddenLayer的模型扫描器现在可供Azure AI使用，以扫描商业和开源模型中的漏洞，恶意软件或篡改。

## 对反“提示软件”工具的需求

Bargury表示，虽然Microsoft表示已经使用安全过滤器解决了这些攻击，但AI模型仍然容易受到它们的影响。

他具体说，需要更多的工具来扫描他和其他研究人员所说的“提示软件”，即隐藏的指令和不受信任的数据。“我不知道你今天有什么东西可以开箱即用[用于检测]，”巴古里说。

“Microsoft Defender 和 Purview 现在没有这些功能，”他补充道。“他们有一些用户行为分析，这很有帮助。如果他们发现副驾驶端点有多个对话，这可能表明他们正在尝试进行即时注射。但实际上，像这样的事情是非常外科手术的，有人有一个有效载荷，他们会把有效载荷发送给你，而[防御]不会发现它。

Bargury 说，他经常与 Microsoft 的红色团队进行沟通，并指出他们知道他在 Black Hat 上的演讲。此外，他认为Microsoft已经采取了积极的行动，以解决与人工智能相关的风险，特别是其自己的Copilot。

“他们真的很努力，”他说。“我可以告诉你，在这项研究中，我们发现了 Microsoft 在 Microsoft Copilot 内部实施的 10 种不同的安全机制。这些机制可以扫描进入 Copilot 的所有内容，从 Copilot 流出的所有内容，以及中间的许多步骤。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/application-security/how-to-weaponize-microsoft-copilot-for-cyberattackers)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298970](/post/id/298970)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/application-security/how-to-weaponize-microsoft-copilot-for-cyberattackers)

如若转载,请注明出处： <https://www.darkreading.com/application-security/how-to-weaponize-microsoft-copilot-for-cyberattackers>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Copilot的红队黑客工具](#h2-0)
* [RCE = 远程“副驾驶”执行攻击](#h2-1)
* [Microsoft的AI红队战略](#h2-2)
* [对反“提示软件”工具的需求](#h2-3)

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