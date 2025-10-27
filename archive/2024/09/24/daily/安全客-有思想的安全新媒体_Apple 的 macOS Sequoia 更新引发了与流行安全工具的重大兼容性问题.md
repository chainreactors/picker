---
title: Apple 的 macOS Sequoia 更新引发了与流行安全工具的重大兼容性问题
url: https://www.anquanke.com/post/id/300316
source: 安全客-有思想的安全新媒体
date: 2024-09-24
fetch_date: 2025-10-06T18:22:42.541935
---

# Apple 的 macOS Sequoia 更新引发了与流行安全工具的重大兼容性问题

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

# Apple 的 macOS Sequoia 更新引发了与流行安全工具的重大兼容性问题

阅读量**104921**

发布时间 : 2024-09-23 15:46:51

**x**

##### 译文声明

本文是翻译文章，文章来源：hackread

原文地址：<https://hackread.com/apples-macos-sequoia-update-breaks-security-tools/>

译文仅供参考，具体内容表达以及含义原文为准。

Apple 的 macOS Sequoia 更新导致与流行的安全工具存在重大兼容性问题。据报道，随着供应商争先恐后地寻找解决方案，用户正面临中断和挫败感。了解受影响的软件、可能的解决方法以及有关此持续问题的最新更新。

据报道，Apple 最新的 macOS 更新 macOS Sequoia（版本 15）导致 CrowdStrike、SentinelOne、ESET 和 Microsoft 等主要提供商的安全工具出现问题。该更新似乎与几种流行的安全工具不兼容，导致它们无法操作。该问题影响 macOS 用户和企业，让使用以 macOS 为中心的安全工具的人感到沮丧。

供您参考，Apple 周一正式推出了其专注于 AI 的 macOS Sequoia。这是一款新的操作系统，在 WWDC 2024 上首次亮相，提供 Apple Intelligence 等独家功能，使用 Apple 芯片在应用程序之间创建语言、图像和操作，利用用户的个人上下文。

然而，该更新引发了对某些与安全相关的产品和应用程序的担忧，因为社交媒体、Reddit 和专注于 Mac 的 Slack 频道上的一些安全研究人员和用户报告了安装 Sequoia 后这些安全工具的问题。

在 Mastodon 上，安全研究员 Will Dormann 报告了 macOS Sequoia 中与防火墙相关的 DNS 问题，并指出阻止 macOS Sequoia 防火墙内的传入连接也会阻止对 DNS 请求的回复，从而导致问题。

Dormann 还指出了一个影响 macOS Sequoia 上 Chrome 和基于 Chromium 的浏览器的相关问题，即在 macOS 防火墙中阻止 Google Chrome 的传入连接会导致大量下载停滞。

与此同时，Apple 尚未解决有关 Sequoia 与 ESET Endpoint Security 和 CrodStrike Falcon 等安全软件兼容性的担忧，并且与 Sequoia 的兼容性问题的全部范围仍不清楚。

大多数公司建议用户在问题解决之前不要更新操作系统，因为他们无法支持 macOS Sequoia。CrowdStrike 证实了这个问题，并宣布推迟支持红杉资本。

该公司正在等待 Apple 在更新其软件之前发布修复程序。同样，ESET 承认更新后存在网络连接问题，但后来澄清说他们的产品与 Sequoia 兼容。

虽然 SentinelOne 最初建议用户不要升级到 Sequoia，但他们后来澄清说可以获得全面支持。但是，一些用户仍然报告了防火墙和 DNS 配置等其他功能的问题。

安全研究员 Wacław Jacek 在他的博客上分享了一种可能的解决方法，包括使用命令行工具来调整特定应用程序的防火墙设置。根据 Jacek 的说法，要修改防火墙设置，请使用 CLI 工具 /usr/libexec/ApplicationFirewall/socketfilterfw。

这将允许您的浏览器再次访问互联网，但其他软件可能仍无法运行。要禁用整个防火墙，请打开终端应用程序，找到 Web 浏览器的路径，运行 ls -l，然后使用 /usr/libexec/ApplicationFirewall/socketfilterfw 将浏览器添加到防火墙。

在情况得到解决之前，请在考虑红杉更新时谨慎行事，尤其是在您严重依赖第三方安全软件的情况下。

### **专家评论**

Qualys 威胁研究部门安全研究经理 Mayuresh Dani 先生与 Hackread.com 分享了他对这种情况的担忧，他说：“随着新操作系统的发布，所有安全供应商都必须测试和验证他们的版本。安全供应商在这种情况下一直积极主动，并且已经发出了措施，以防他们的系统面临最新 Mac 更新的问题，这是一件好事。

Mayuresh 强调说：“从外观上看，网络堆栈（或者更确切地说是 macOS Sequoia 防火墙）已经发生了变化，因为使用它来提供安全性的安全工具无法做到这一点。不仅是安全工具，VPN 也很难获得 DNS 解析。

他还向负责保护 Mac 的安全团队提出了以下建议：

1. 避免更新到 macOS Sequoia，除非他们的安全供应商已正式认证其使用。
2. 在内部认证之前，关闭对主要操作系统版本的自动更新。
3. 在组织范围的部署之前，通过使用认证软件安装操作系统的 Dev 和 Beta 版本，对新的操作系统版本进行内部认证。

尽管如此，在生产环境中部署主要更新之前进行全面测试的重要性不应被忽视。它还强调了组织需要制定适当的备份计划和替代安全措施。开发不完全依赖单个工具或供应商的多层安全方法可以增强整体稳定性。

本文翻译自hackread [原文链接](https://hackread.com/apples-macos-sequoia-update-breaks-security-tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300316](/post/id/300316)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/apples-macos-sequoia-update-breaks-security-tools/)

如若转载,请注明出处： <https://hackread.com/apples-macos-sequoia-update-breaks-security-tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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