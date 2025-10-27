---
title: 巴西广告欺诈网络“Camu”每日竞价请求数超过20亿次
url: https://www.anquanke.com/post/id/299659
source: 安全客-有思想的安全新媒体
date: 2024-08-31
fetch_date: 2025-10-06T17:59:25.244401
---

# 巴西广告欺诈网络“Camu”每日竞价请求数超过20亿次

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

# 巴西广告欺诈网络“Camu”每日竞价请求数超过20亿次

阅读量**94121**

发布时间 : 2024-08-30 14:47:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/brazilian-ad-fraud-network-camu-hits-2-billion-daily-bid-requests>

译文仅供参考，具体内容表达以及含义原文为准。

今年早些时候，一个盗版网络每天欺诈性地提供超过 20 亿个在线广告。

“Camu”（葡萄牙语中“camuflagen”的缩写）总部位于巴西，大规模贩卖广告欺诈。在今年早些时候的高峰期，它每天处理 132 个域的约 25 亿个出价请求。正如 HUMAN Security 研究人员在一份新报告中所描述的那样，这大约相当于整个佐治亚州亚特兰大市产生的广告流量。

自 2023 年 12 月发现卡姆以来，人类研究人员一直在卡姆身上盖上一条湿毯子。尽管它仍然处于活动状态，但它每天处理的出价请求只有区区 1 亿个。

该方案的工作原理要归功于一个完全简单的基于 cookie 的重定向机制，该机制向用户发送他们正在寻找的电影和电视节目，但讨厌的调查人员会诱骗网站。

## 卡姆的两张面孔

Camu 的盗版网站提供与任何其他标准盗版或色情网站类似的用户体验。当访问者到达网站并点击他们想要查看的内容时，他们会被重定向到托管该网站的第二个域（所谓的“提现网站”）。

这些广告中有许多来自完全诚实的公司，如果他们知道的话，肯定不想与非法内容联系在一起。为了让他们蒙在鼓里，Camu 采用了一种基本的机制来确保只有他们的目标受众最终会进入他们的提现网站。

“这次行动中的行为者滥用了互联网的一个非常重要的部分，其中域能够根据不同的参数进行不同的加载，”HUMAN 的欺诈运营总监 Will Herbig 解释说。“如果我在电脑上访问域，而不是在手机上访问域，它可能会以不同的方式加载页面，这没关系。然而，卡姆正在利用这一点，他们以一种很难被发现的方式滥用它。

当盗版网站的访问者被重定向到提现网站时，他们会被分配一个令牌。该令牌在他们的浏览器上安装一个 cookie，从某种意义上说，这 “允许” 他们进入带有内容和广告的提现网站。

如果任何不受欢迎的人（例如，安全研究人员或广告商的员工）通过任何其他方式到达提现域，他们将不会拥有该 cookie，因此不会被允许进入该网站。相反，他们会被重定向到一个不同的、平淡无奇但最终无害的这样或那样的网站。

为了掩盖其恶意域与为其提供服务的盗版网站之间的关系，Camu 操纵了在重定向过程中传输的信息。它不仅会 “清除 ”任何暗示引用网站的信息，还会将虚假的引用信息添加到登陆域的 URL 中，从而给人一种访问者从信誉良好的网站或搜索引擎登陆那里的感觉。

## 广告交易平台如何助长欺诈

正如 Herbig 很快指出的那样，“除了 Camu 和 Merry-Go-Round，我们正在跟踪其他 7 个规模较小但规模相似的运营，它们正在做这类事情。

在线广告购买的自动化程度一直使这项业务变得容易，中间商交换以程序化方式在合法广告商之间贩卖库存，有时不如合法买家。

“许多公司只与与他们有直接关系的公司投放广告。这并非完全万无一失，但这往往是一种更安全的方法。Herbig 解释道。然而，他补充说，“程序化生态系统是巨大的。那里有数以万计的出版商网络。他们中的许多人都信誉良好，[但是] 有一些威胁行为者正试图利用这一点。

为了解决中间商广告交易平台带来的问题，一些广告商转向中间商验证服务。不幸的是，其中一些服务已被证明充其量是无效的。

“广告欺诈年复一年地保持’有史以来最高’，无论是金额还是广告展示量的百分比，”独立广告欺诈研究员 Augustine Fou 博士感叹道。“我们有一些像这样的案例，偶尔会揭露一个微小但具有代表性的例子，即广告费流向了错误的地方，比如盗版网站。但与广告展示的其他可怕地方相比，盗版网站显得苍白无力。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/brazilian-ad-fraud-network-camu-hits-2-billion-daily-bid-requests)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299659](/post/id/299659)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/brazilian-ad-fraud-network-camu-hits-2-billion-daily-bid-requests)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/brazilian-ad-fraud-network-camu-hits-2-billion-daily-bid-requests>

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

* [卡姆的两张面孔](#h2-0)
* [广告交易平台如何助长欺诈](#h2-1)

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