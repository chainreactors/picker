---
title: ClickFix：基于剪贴板的社会工程的威胁日益严重
url: https://www.anquanke.com/post/id/302027
source: 安全客-有思想的安全新媒体
date: 2024-11-21
fetch_date: 2025-10-06T19:13:57.192334
---

# ClickFix：基于剪贴板的社会工程的威胁日益严重

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

# ClickFix：基于剪贴板的社会工程的威胁日益严重

阅读量**56147**

发布时间 : 2024-11-20 14:40:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/clickfix-the-rising-threat-of-clipboard-based-social-engineering/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一份详细的报告中，Proofpoint 的研究人员揭示了一种被称为 ClickFix 的独特社交工程方法令人震惊的崛起，这种方法利用人类行为，通过自找麻烦的方式传播恶意软件。ClickFix最初于2024年初在访问代理TA571和一个名为ClearFake的威胁集群的活动中被发现，现在已成为网络安全领域的一个普遍威胁。

ClickFix 利用对话框中的虚假错误信息诱骗用户运行恶意 PowerShell 命令。这些信息看似真实，模仿软件错误或更新提示。例如，用户可能会看到通过复制和粘贴所提供的命令来 “修复 ”问题的说明，这些命令可以直接输入 PowerShell 或 Windows “运行 ”对话框。用户并不知道，这一简单的操作可能会释放 AsyncRAT、DarkGate 或 Lumma Stealer 等危险的恶意软件。

Proofpoint 强调指出：“ClickFix 技术被多种不同的威胁行为者使用，可以通过被入侵的网站、文档、HTML 附件、恶意 URL 等发起。”

ClickFix 的多功能性在于它能够伪装成各行业和平台的合法操作。最近的活动包括

* **虚假验证码验证：** 在针对乌克兰政府实体的活动中，ClickFix 将自己伪装成验证码检查。用户在验证其人性的幌子下被诱骗运行 PowerShell 命令。Proofpoint 将此与俄罗斯间谍行为者联系起来，指出 GitHub 上的开源 reCAPTCHA Phish 工具包在这些攻击中起到了重要作用。
* **假冒可信平台：** 10 月中旬的一次攻击活动针对 GitHub 用户发布了虚假的安全漏洞通知。恶意电子邮件将受害者引向使用 ClickFix 发送 Lumma Stealer 的伪造 GitHub 网站。
* **特定语言攻击：** 一个德语攻击活动利用伪装成流行电子商务平台 Ricardo 更新的 ClickFix 引诱瑞士组织。受害者被引向一个执行 JavaScript 的登陆页面，以下载恶意软件，很可能是 AsyncRAT 或 PureLog Stealer。

ClickFix 攻击者不断改进方法以逃避检测。2024 年 9 月，Proofpoint 观察到 ClickFix 攻击活动使用 HTML 附件，这些附件会反转网页源代码中的字符串，从而使分析师的审查复杂化。此外，以 ChatGPT 为主题的恶意广告活动体现了 ClickFix 的适应性，它利用流行趋势来引诱受害者。

![]()
乌克兰语诱饵，声称与所要求的所谓信息有关 | 图片： Proofpoint

Proofpoint 的可视性表明，ClickFix 活动已经影响了全球 300 多个组织。虽然许多操作似乎是出于经济动机，但其他操作则暗示了间谍目的，例如与针对乌克兰的 UAC-0050 相关的操作。

尽管 ClickFix 被广泛采用，但它并不总是归咎于单一的威胁行为者或组织。Proofpoint 指出：”大多数观察到的 ClickFix 活动都不是由已知的威胁行为者或组织实施的。

本文翻译自securityonline [原文链接](https://securityonline.info/clickfix-the-rising-threat-of-clipboard-based-social-engineering/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302027](/post/id/302027)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/clickfix-the-rising-threat-of-clipboard-based-social-engineering/)

如若转载,请注明出处： <https://securityonline.info/clickfix-the-rising-threat-of-clipboard-based-social-engineering/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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