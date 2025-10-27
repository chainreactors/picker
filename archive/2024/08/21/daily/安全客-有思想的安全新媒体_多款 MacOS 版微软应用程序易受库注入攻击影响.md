---
title: 多款 MacOS 版微软应用程序易受库注入攻击影响
url: https://www.anquanke.com/post/id/299296
source: 安全客-有思想的安全新媒体
date: 2024-08-21
fetch_date: 2025-10-06T18:00:36.827254
---

# 多款 MacOS 版微软应用程序易受库注入攻击影响

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

# 多款 MacOS 版微软应用程序易受库注入攻击影响

阅读量**56829**

发布时间 : 2024-08-20 11:44:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/remote-workforce/multiple-microsoft-apps-for-macos-vuln-to-malicious-library-injection-attacks>

译文仅供参考，具体内容表达以及含义原文为准。

广泛使用的 Microsoft macOS 应用程序容易受到库注入攻击，这些攻击让攻击者使用应用程序的权利来绕过 macOS 严格的基于权限的安全模型和控制。

攻击者可以滥用易受攻击的应用程序来执行各种恶意操作，例如从用户帐户秘密发送电子邮件或录制音频和视频剪辑，而无需用户知情且无需任何用户交互。

思科 Talos 的研究人员最近在 研究 Apple 的透明度、同意和控制 （TCC） 框架的可利用性时发现了这些问题，该框架用于管理和执行 macOS 系统上用户数据和各种系统服务的隐私设置。TCC 的核心功能之一是控制应用程序对敏感用户数据以及摄像头、麦克风、联系人、日历和位置服务等系统功能的访问。

## 易受攻击的应用程序

思科 Talos 研究人员发现，适用于 macOS 的八个主要 Microsoft 应用程序（Outlook、Teams、PowerPoint、OneNote、Excel、Word 和其他两个与 Teams 相关的组件）允许攻击者将恶意库注入应用程序的运行进程中。“该库可以使用已经授予该过程的所有权限，有效地代表应用程序本身运行，”思科Talos在本周的一份报告中表示。

Cisco Talos 发现的问题与 Microsoft 决定禁用应用程序中的库验证功能有关，以便允许加载第三方插件。“权限规定应用程序是否可以访问麦克风、摄像头、文件夹、屏幕录制、用户输入等资源。因此，如果攻击者要访问这些信息，他们可能会泄露敏感信息，或者在最坏的情况下，升级特权，“研究人员说。

Cisco Talos 已针对 8 个适用于 macOS 的 Microsoft 应用中的已禁用库验证问题发布了 8 个单独的 CVE。

Microsoft没有立即回应Dark Reading的置评请求。但是，根据思科Talos的说法，Microsoft已将该问题描述为低严重性威胁，并表示不会为他们发布任何修复程序。即便如此，Microsoft在收到问题通知后似乎已经更新了受影响的Teams和OneNote应用程序，思科Talos说。但这家安全供应商表示，Microsoft的四款macOS应用程序——Excel、Outlook、PowerPoint和Word仍然容易受到攻击。

## 苹果的TCC遭到破坏

Sectigo 产品高级副总裁 Jason Soroko 表示，Microsoft 决定将问题归类为低严重性并选择不发布修复程序，这具有潜在风险。Soroko说：“如果攻击者利用这些漏洞未经授权访问摄像头或麦克风等敏感设备功能，这种方法忽略了危害。“通过淡化威胁，Microsoft有可能低估攻击者的聪明才智，他们甚至可以以创造性和破坏性的方式将’低严重性’的漏洞武器化。

思科 Talos 本身将 Microsoft 应用程序描述为破坏了 Apple TCC 框架的安全和隐私保护。与大多数其他默认情况下依赖于所谓的自由访问控制的操作系统不同，TCC 更进一步，要求应用程序在寻求访问某些内容和服务（例如联系人、日历、照片以及访问麦克风和摄像头）时获得明确的用户权限。TCC还支持一项功能，该功能专门防止代码和库注入到应用程序的运行进程中。

思科Talos表示，通过禁用库验证，Microsoft基本上为攻击者提供了一个机会，可以绕过保护措施进行终结运行，并将任意库潜入应用程序的运行进程中。

索罗科说，利用这个问题的难易程度各不相同。“虽然库注入攻击需要技术技能，但这些漏洞存在于 Teams 和 Outlook 等广泛使用的应用程序中这一事实增加了风险状况。具有足够知识的攻击者可以利用这些漏洞，尤其是在安全实践宽松的环境中。

他建议组织审查并收紧应用程序权限，并实施对异常活动的监控。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/remote-workforce/multiple-microsoft-apps-for-macos-vuln-to-malicious-library-injection-attacks)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299296](/post/id/299296)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/remote-workforce/multiple-microsoft-apps-for-macos-vuln-to-malicious-library-injection-attacks)

如若转载,请注明出处： <https://www.darkreading.com/remote-workforce/multiple-microsoft-apps-for-macos-vuln-to-malicious-library-injection-attacks>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [易受攻击的应用程序](#h2-0)
* [苹果的TCC遭到破坏](#h2-1)

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