---
title: 如何调查 Google Workspace 中的 ChatGPT 活动
url: https://www.anquanke.com/post/id/300151
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:12.337863
---

# 如何调查 Google Workspace 中的 ChatGPT 活动

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

# 如何调查 Google Workspace 中的 ChatGPT 活动

阅读量**121003**

发布时间 : 2024-09-18 15:01:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 The Hacker News ，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html>

译文仅供参考，具体内容表达以及含义原文为准。

自 2022 年推出 ChatGPT 以来，OpenAI 不断推出产品公告和改进，超出了预期。2024 年 5 月 16 日发布了一个这样的公告，对于大多数消费者来说，这可能感觉无伤大雅。该帖子的标题**为“ChatGPT 中数据分析的改进”，**概述了用户如何直接从 Google Drive 和 Microsoft OneDrive 添加文件。值得一提的是，Google AI Studio 和 Claude Enterprise 等其他 genAI 工具最近也增加了类似的功能。非常棒，对吧？或。

当您将组织的 Google Drive 或 OneDrive 帐户连接到 ChatGPT（或其他 genAI 工具）时，您授予它广泛的权限，您不仅会授予它您的个人文件，还会授予它整个共享驱动器中的资源的广泛权限。正如您可能想象的那样，这种广泛集成的好处伴随着一系列网络安全挑战。

那么，您如何确定员工是否启用了 ChatGPT 和 Google Drive 之间的集成，以及如何监控哪些文件已被访问呢？这篇文章将介绍如何在 Google Workspace 中原生执行此操作，以及 Nudge Security 如何帮助您发现所有正在使用的 genAI 应用程序，以及它们已与哪些其他应用程序集成。

## 在 Google Workspace 中哪里可以看到 ChatGPT 活动

在 Google Workspace 中，有几种方法可以识别和调查与 ChatGPT 连接相关的活动。

在 Google Workspace 的 Admin Console 中，导航到 Reporting > Audit and investigation > Drive 日志事件。在这里，您将看到访问的 Google Drive 资源列表。

您还可以通过 Reporting→Audit and investigation→ Oauth log events 下的 API 调用来调查活动。

因此，定期检查您的 Google Workspace 管理控制台可以帮助您了解 ChatGPT 正在访问哪些资源，但在活动已经发生后看到这些活动当然不如在使用 ChatGPT 创建新集成后立即收到警报有价值。这就是 Nudge security 可以提供帮助的地方。

## 如何查看 genAI 与 Nudge Security 的所有集成

Nudge Security 可以发现您组织中任何人为任何 SaaS 应用程序创建的所有帐户，包括 ChatGPT 和快速扩展的新创建的 genAI 工具列表，而无需事先了解该工具的存在。借助内置的 AI 控制面板，客户可以跟上 AI 的采用情况并主动降低 AI 安全风险。

此外，Nudge Security 在可筛选的 OAuth 控制面板中显示整个组织的 OAuth 授权，例如授予 ChatGPT 的授权，其中包括授权类型（登录或集成）、活动和风险洞察。按类别筛选以查看与 AI 工具相关的所有授权：

单击授权以打开详细信息屏幕，您可以在其中查看风险配置文件、有关授权创建者和创建时间的详细信息、访问详细信息、授予的范围等：

然后，您可以通过 Slack 或电子邮件向授权的创建者发送“提示”以采取特定操作，例如限制授权的范围，或者您可以立即从 Nudge Security 用户界面中撤销授权。

最后，您可以设置自定义规则，以确保在组织中的用户为 ChatGPT 或任何其他 genAI 应用程序创建 OAuth 授权时收到通知。您还可以创建规则，以便在创建新的 genAI 账户时立即收到提醒，并推动新的 genAI 用户查看和确认您的 genAI 可接受使用策略。

## 平衡生产力与安全性

虽然 ChatGPT 与 Google Drive 和 Microsoft OneDrive 的集成为提高生产力提供了巨大的潜力，但它也为重大的安全风险打开了大门。组织必须在清楚地了解潜在风险的情况下进行这些集成，并实施适当的治理和安全措施来减轻这些风险。

Nudge Security 提供可见性以及上下文和自动化，以帮助企业在不影响数据安全性的情况下采用 genAI 工具。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300151](/post/id/300151)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [在 Google Workspace 中哪里可以看到 ChatGPT 活动](#h2-0)
* [如何查看 genAI 与 Nudge Security 的所有集成](#h2-1)
* [平衡生产力与安全性](#h2-2)

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