---
title: 内存安全代码的采用使Android更安全
url: https://www.anquanke.com/post/id/300493
source: 安全客-有思想的安全新媒体
date: 2024-09-28
fetch_date: 2025-10-06T18:22:36.402379
---

# 内存安全代码的采用使Android更安全

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

# 内存安全代码的采用使Android更安全

阅读量**133373**

发布时间 : 2024-09-27 14:27:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/application-security/memory-safe-code-adoption-android-safer>

译文仅供参考，具体内容表达以及含义原文为准。

在过去五年中，Android 中与内存相关的漏洞数量急剧下降，这要归功于 Google 使用安全设计方法，该方法强调对大多数新代码使用 Rust 等内存安全语言。

缓冲区溢出和释放后使用错误等内存安全问题现在仅占所有 Android 漏洞的 24%，而 2019 年这一比例为 76%。今年到目前为止的数据表明，2024 年全年共有 36 个与 Android 内存相关的漏洞，大约是去年的一半，与 2019 年的 223 个缺陷相去甚远。

## Safety-by Design 方法获得回报

在 9 月 25 日的一篇博文中，来自 Google Android 和安全团队的研究人员将这一进展归功于安全编码，这是该公司的一种安全设计方法，优先考虑将 Rust 等内存安全语言用于新代码开发。“根据我们所学到的知识，很明显，我们不需要丢弃或重写所有现有的内存不安全代码，”研究人员写道。“相反，Android 专注于使互操作性安全便捷，作为我们内存安全之旅的主要功能。”

内存安全漏洞传统上占所有应用程序软件漏洞的 60% 以上，并将继续占 60% 以上。与其他缺陷相比，它们也异常严重。例如，在 2022 年，与内存相关的错误仅占所有已识别的 Android 漏洞的 36%，但占操作系统中最严重缺陷的 86%，占已确认利用的 Android 漏洞的 78%。

这在很大程度上与 C 和 C++ 等广泛使用的编程语言允许软件开发人员直接操作内存有关，从而为错误潜入敞开大门。相比之下，Rust、Go 和 C# 等内存安全语言具有自动内存管理和针对常见内存相关错误的内置安全检查功能。包括美国网络安全和基础设施安全局 （CISA） 甚至白宫在内的许多安全利益相关者都对与使用内存不安全语言相关的安全风险增加以及解决这些问题所涉及的大量成本表示担忧。虽然向内存安全语言的转变势头正在缓慢增强，但许多人预计将现有代码库完全迁移到内存安全代码需要数年甚至数十年的时间。

## 渐进的过渡

Google 解决这个问题的方法是使用内存安全的语言（如 Rust）来实现新的 Android 功能，同时除了修复错误外，保留现有代码基本保持不变。两位 Google 研究人员表示，结果是，在过去几年中，涉及内存不安全语言的新开发活动逐渐放缓，而内存安全开发活动却有所增加。

Google 从 Android 12 中对 Rust 的支持开始过渡，并在 Android 开源项目中逐渐增加对编程语言的使用。Android 13 标志着操作系统中的大部分新代码首次采用内存安全语言。当时，谷歌强调，其目标不是将所有 C 和 C++ 代码转换为 Rust，而是随着时间的推移逐渐过渡到新的编程语言。

在今年早些时候的一篇博文中，Google 安全工程团队的成员指出，他们认为“将 C++ 演变成具有严格内存安全保证的语言没有现实的道路”。但是，Google 不会一下子就放弃它，而是将继续投资于提高 C 和 C++ 内存安全性的工具，以支持公司用这些语言编写的现有代码库。

值得注意的是，Google 发现与内存相关的错误占所有 Android 漏洞的百分比有所下降，这不仅是因为该公司越来越多地使用像 Rust 这样的内存安全语言，还因为旧的漏洞会随着时间的推移而衰减。研究人员发现，与全新的代码相比，五年前的 Android 代码中给定数量的代码中的漏洞数量（通常称为漏洞密度）较低。

研究人员说：“问题主要在于新代码，因此需要从根本上改变我们开发代码的方式。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/application-security/memory-safe-code-adoption-android-safer)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300493](/post/id/300493)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/application-security/memory-safe-code-adoption-android-safer)

如若转载,请注明出处： <https://www.darkreading.com/application-security/memory-safe-code-adoption-android-safer>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [Safety-by Design 方法获得回报](#h2-0)
* [渐进的过渡](#h2-1)

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