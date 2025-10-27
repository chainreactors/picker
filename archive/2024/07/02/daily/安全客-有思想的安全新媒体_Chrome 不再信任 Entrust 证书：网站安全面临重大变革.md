---
title: Chrome 不再信任 Entrust 证书：网站安全面临重大变革
url: https://www.anquanke.com/post/id/297595
source: 安全客-有思想的安全新媒体
date: 2024-07-02
fetch_date: 2025-10-06T17:40:38.477215
---

# Chrome 不再信任 Entrust 证书：网站安全面临重大变革

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

# Chrome 不再信任 Entrust 证书：网站安全面临重大变革

阅读量**129434**

发布时间 : 2024-07-01 12:22:36

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/chrome-to-distrust-entrust-certificates/>

译文仅供参考，具体内容表达以及含义原文为准。

谷歌的 Chrome 浏览器将采取一项重大安全举措，从 2024 年底开始不再信任著名证书颁发机构 (CA) Entrust 颁发的证书。这一决定将对众多网站的运营造成阻碍，其中包括美国银行、ESPN 和 IRS.GOV 等主要组织的网站。

数字证书 (SSL/TLS) 在确保用户和网站之间的安全连接方面发挥着至关重要的作用。这些由受信任的 CA 颁发的证书充当安全印章（更像是网站的蓝色勾号），可帮助用户判断网站的合法性。它还可以确保加密通信以防止数据泄露。

然而，由于过去六年来“合规性不达标、未兑现改进承诺以及缺乏切实可衡量的进展”，Chrome 已将Entrust 从其受信任的 CA 名单中移除。Entrust 在维护安全标准方面屡屡出现缺陷，这导致 Google 对其作为可靠 CA 的能力失去了信心。

“我们认为 Chrome 不再有理由继续信任 Entrust。” – Google Chrome

这一举措还延伸至 AffirmTrust，一家被 Entrust 收购的知名度较低的供应商。虽然这些证书与 Let’s Encrypt（49.7%）相比只占很小一部分（0.1%），但考虑到美国银行、BookMyShow、ESPN 等组织，甚至互联网流量很大的政府网站（如 IRS.gov）也获得了 Entrust 的认证，其影响仍然很大。

![Entrust、美国银行、美国国税局]()
Chrome 证书查看器上显示的美国银行和 IRS.gov 证书
这对用户和网站所有者意味着什么
从 2024 年 11 月 1 日开始，Chrome用户遇到带有不受信任的 Entrust 证书的网站时，将会看到整页警告，指出该网站“不安全”。

![委托]()
Chrome 对拥有 Entrust 或 AffirmTrust 证书的网站显示警告的示例（来源：Google）
此警告仅适用于 2024 年 10 月 31 日之后颁发的证书，为拥有现有 Entrust 证书的网站提供宽限期。但是，由于证书有有效期，网站所有者必须在证书到期前转换到其他 CA。考虑到其市场份额，Let’s Encrypt 是一个免费且值得信赖的选择，强烈推荐。

这一转变对于维护安全的网络环境至关重要。当 CA 未能满足预期时，它会危及整个互联网生态系统。Chrome 的决定优先考虑用户保护，消除了对可能被盗用的证书的信任。

使用受影响的 Entrust 证书的网站所有者应迅速采取行动，切换到其他 CA。Chrome 证书查看器可用于识别 Entrust 颁发的证书。虽然这看起来不方便，但有必要确保用户继续访问而不会收到安全警告。

**仅适用于内部网络的潜在解决方法**
管理内部网络的大型组织有一定的回旋余地。Chrome 允许企业通过在本地网络上将受影响的证书安装为受信任的证书来绕过这些更改。这确保使用这些证书的内部网站正常运行。

**Entrust 争议：深入剖析**
Mozilla 的 Bug Tracker (Bug 1890685 ) 上的讨论揭示了更多背景信息。它揭示了一个关键问题——Entrust 未能撤销 2024 年 3 月 18 日至 21 日期间颁发的一组特定的扩展验证 (EV) TLS 证书。这违反了他们自己的认证实践声明 (CPS)。

Entrust 选择不撤销证书，理由是可能让客户感到困惑，并否认存在任何安全风险。然而，这一决定引发了众怒。批评者强调，适当的撤销程序对于维护 CA 系统的信任至关重要。Entrust 将客户便利置于安全性之上，这引发了人们对其严格遵守安全最佳实践的承诺的担忧。

Mike Shaver 在 Google Groups 上发表的一篇详细帖子进一步阐明了这一情况。Shaver 对 Entrust 是否能够遵守 WebPKI 和 Mozilla 根存储计划 (MRSP) 的要求表示怀疑。尽管 Entrust 试图解决这些问题，但其对证书撤销、运营问责制和透明度的处理仍然受到质疑。

Shaver 指出，Entrust 倾向于优先考虑客户便利性，而不是严格遵守安全标准。他还批评 Entrust 缺乏有关组织变革的详细信息，以及未能满足 Mozilla 的事件响应要求。在 Entrust 展示出实质性的改进和透明度之前，继续信任其证书将对整个 Web PKI 和互联网用户的安全构成重大风险。

但这并不是结束。事实上，这只是冰山一角。Shaver 在论坛上的评论是对 3 月至 5 月期间与 Entrust 相关的一系列合规事件的回应。Ben Wilson 在专门的wiki 页面中总结了这些最近的事件。

***“简而言之，这些事件的起因是对电动汽车指南的误解导致证书错误发放，随后在事件处理中出现了许多错误，包括故意继续错误发放证书，” 威尔逊说。***

他补充说，考虑到严格的规范和根存储要求，这是 Entrust 的一个非常严重的缺陷。

然而，Chrome 决定不信任 Entrust 证书发出了一个强烈的信息——优先考虑用户安全需要要求 CA 负责维护最高安全标准。

本文翻译自 [原文链接](https://thecyberexpress.com/chrome-to-distrust-entrust-certificates/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297595](/post/id/297595)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/chrome-to-distrust-entrust-certificates/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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