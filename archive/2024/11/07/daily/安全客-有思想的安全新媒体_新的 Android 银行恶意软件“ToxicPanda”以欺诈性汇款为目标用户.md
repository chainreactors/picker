---
title: 新的 Android 银行恶意软件“ToxicPanda”以欺诈性汇款为目标用户
url: https://www.anquanke.com/post/id/301587
source: 安全客-有思想的安全新媒体
date: 2024-11-07
fetch_date: 2025-10-06T19:12:14.339114
---

# 新的 Android 银行恶意软件“ToxicPanda”以欺诈性汇款为目标用户

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

# 新的 Android 银行恶意软件“ToxicPanda”以欺诈性汇款为目标用户

阅读量**86153**

发布时间 : 2024-11-06 11:06:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html>

译文仅供参考，具体内容表达以及含义原文为准。

超过1500台安卓设备感染了一种名为ToxicPanda的新型安卓银行恶意软件，该恶意软件允许威胁者进行欺诈性银行交易。

ToxicPanda的主要目标是利用一种名为 “设备上欺诈（ODF）”的著名技术，通过账户接管（ATO）从受攻击设备上发起转账，”Cleafy研究人员Michele Roviello、Alessandro Strino和Federico Valentini在周一的一份分析报告中说。

“它的目的是绕过银行用于执行用户身份验证和认证的反制措施，并结合银行用于识别可疑转账的行为检测技术。”

ToxicPanda被认为是一个说中文的威胁行为者所为，该恶意软件与另一个被称为TgToxic的安卓恶意软件有基本相似之处，后者可以从加密钱包中窃取凭证和资金。趋势科技于 2023 年初记录了 TgToxic。

据报告，大多数入侵事件发生在意大利（56.8%），其次是葡萄牙（18.7%）、香港（4.6%）、西班牙（3.9%）和秘鲁（3.4%），这是中国威胁行为者针对欧洲和拉丁美洲零售银行用户策划欺诈计划的罕见案例。

该银行木马似乎还处于初级阶段。分析显示，它是其祖先的精简版，删除了自动传输系统 (ATS)、Easyclick 和混淆例程，同时还引入了 33 个新命令来获取各种数据。

此外，多达 61 条命令被发现与 TgToxic 和 ToxicPanda 相同，这表明新恶意软件家族的幕后黑手是同一个威胁行为体或与其关系密切的附属机构。

研究人员说：“虽然它与 TgToxic 系列有一些僵尸命令相似之处，但代码与其原始源代码有很大差异。”研究人员说：“TgToxic 所特有的许多功能都明显不存在，而且有些命令看起来就像占位符，没有真正实现。”

该恶意软件伪装成谷歌浏览器、Visa 和 99 Speedmart 等流行应用程序，并通过模仿应用程序商店列表页面的伪造页面进行传播。目前尚不清楚这些链接是如何传播的，是否涉及恶意广告或钓鱼技术。

一旦通过侧载安装，ToxicPanda 就会滥用安卓的可访问性服务来获取更高的权限，操纵用户输入，并从其他应用程序中获取数据。它还可以拦截通过短信发送或使用验证器应用程序生成的一次性密码（OTP），从而使威胁行为者能够绕过双因素身份验证（2FA）保护，完成欺诈性交易。

该恶意软件的核心功能除了获取信息外，还允许攻击者远程控制被入侵的设备，并执行所谓的ODF，从而在受害者不知情的情况下发起未经授权的转账。

Cleafy说，它能够访问ToxicPanda的命令与控制（C2）面板，这是一个用中文显示的图形界面，允许操作员查看受害设备的列表，包括型号信息和位置，并将它们从引擎盖上移除。此外，该面板还可作为请求实时远程访问任何设备以进行 ODF 的渠道。

研究人员说：“ToxicPanda 需要展示更先进、更独特的能力，这将使其分析变得更加复杂。然而，日志信息、死代码和调试文件等人工制品表明，该恶意软件可能处于早期开发阶段，或者正在进行大量代码重构–特别是考虑到它与 TGToxic 的相似性。”

佐治亚理工学院、德国国际大学和庆熙大学的一组研究人员详细介绍了一种名为DVa（Detector of Victim-specific Accessibility的缩写）的后台恶意软件分析服务，以标记利用安卓设备辅助功能的恶意软件。

他们说：“DVa使用动态执行跟踪，进一步利用滥用向量引导的符号执行策略来识别滥用例程并将其归属于受害者。“最后，DVa检测了[可访问性]授权的持久机制，以了解恶意软件是如何阻碍合法查询或删除尝试的。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301587](/post/id/301587)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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