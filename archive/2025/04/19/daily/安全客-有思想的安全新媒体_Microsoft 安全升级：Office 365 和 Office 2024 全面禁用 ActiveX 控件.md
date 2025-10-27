---
title: Microsoft 安全升级：Office 365 和 Office 2024 全面禁用 ActiveX 控件
url: https://www.anquanke.com/post/id/306699
source: 安全客-有思想的安全新媒体
date: 2025-04-19
fetch_date: 2025-10-06T22:05:12.931360
---

# Microsoft 安全升级：Office 365 和 Office 2024 全面禁用 ActiveX 控件

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

# Microsoft 安全升级：Office 365 和 Office 2024 全面禁用 ActiveX 控件

阅读量**96085**

发布时间 : 2025-04-18 16:53:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/microsoft-to-disable-activex-controls-in-office-365-and-2024/>

译文仅供参考，具体内容表达以及含义原文为准。

![Windows kernel Rust ActiveX, Microsoft 365]()

根据 Microsoft 发布的一项产品公告，该公司计划从本月底开始，在运行 Windows 10 和 11 系统的 Microsoft 365 以及 Microsoft Office 2024 中逐步禁用所有 ActiveX 控件。默认情况下，这些控件将被阻止使用，除非用户手动配置系统以允许它们运行。

ActiveX 于 1996 年首次推出，是一个软件框架，它使开发人员能够在 Microsoft 办公软件应用程序中嵌入交互式对象，从而实现诸如执行嵌入代码等高级功能。

然而，正是这种功能也使得 ActiveX 成为网络犯罪分子和网络钓鱼活动青睐的攻击载体。恶意行为者利用 ActiveX 将有害代码嵌入文档中，诱骗用户触发远程后门程序或下载其他形式的恶意软件。

为了增强安全性，Microsoft 现在将在不发出任何警告提示的情况下，阻止所有办公软件组件中 ActiveX 控件的执行。（此前，这些控件默认是禁用的，但会伴有一个通知横幅。）这一变化旨在防止用户在不知情的情况下激活有害内容。

尽管如此，Microsoft 也承认，一些企业和高级用户仍然依赖 ActiveX 控件。对于这种情况，用户可以手动重新启用 ActiveX 功能，但这样做可能会带来安全风险，信息技术管理员应该仔细权衡利弊。

在办公软件中重新启用 ActiveX 控件的步骤如下：

1.选择 “文件”，然后选择 “选项”。

2.选择 “信任中心”，然后点击 “信任中心设置” 按钮。

3.选择 “ActiveX 设置”，然后确保勾选 “在启用所有控件之前提示我（限制最少）”。

4.点击 “确定”，然后再次点击 “确定” 以保存设置并返回到文档。

完成上述步骤后，所有办公软件组件中的 ActiveX 控件将被重新启用。如果某些应用程序（如 Excel）仍然无法运行 ActiveX 控件，则可能需要为每个特定程序单独配置信任设置。

此前，Microsoft 也默认在办公软件中禁用了 VBA 宏。与 ActiveX 一样，宏可以扩展Office 的功能，但也带来了安全隐患。希望启用宏的用户也必须通过 “信任中心” 设置手动进行操作。

本文翻译自securityonline [原文链接](https://securityonline.info/microsoft-to-disable-activex-controls-in-office-365-and-2024/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306699](/post/id/306699)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/microsoft-to-disable-activex-controls-in-office-365-and-2024/)

如若转载,请注明出处： <https://securityonline.info/microsoft-to-disable-activex-controls-in-office-365-and-2024/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**7赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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