---
title: 美国当局发布 RansomHub 勒索软件警报
url: https://www.anquanke.com/post/id/299726
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:53.733124
---

# 美国当局发布 RansomHub 勒索软件警报

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

# 美国当局发布 RansomHub 勒索软件警报

阅读量**92012**

发布时间 : 2024-09-03 14:23:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 斯蒂芬·普里查德，文章来源：infosecurity-magazine

原文地址：<https://www.infosecurity-magazine.com/news/us-authorities-ransomhub/>

译文仅供参考，具体内容表达以及含义原文为准。

美国当局发布了一份联合网络安全公告，涵盖一个多产的勒索软件组织 RansomHub。

据信，该组织通过双重勒索技术“加密和泄露”了至少 210 名受害者的数据。

该组织的受害者涵盖公共和私营部门的组织，包括医疗保健、IT、政府、紧急服务、食品和农业以及水和废水。该集团还瞄准了制造业、运输和通信领域的“关键”基础设施。

该咨询说明详细介绍了策略、技术和程序 （TTP）、入侵指标 （IOC），以及组织可以采取的自我保护步骤。

### **RansomHub 的策略、技术和程序**

据美国国家网络防御机构 CISA 称，RansomHub “通过加密系统和泄露数据来勒索受害者”，使用双重勒索。但是，由于 RansomHub 采用联盟模式，因此数据泄露的确切方法将取决于闯入受害者网络的联盟。

这些机构表示，RansomHub 附属公司通常通过网络钓鱼、密码喷洒（针对因密码泄露而受损的帐户）和利用已知漏洞来“破坏面向互联网的系统和用户端点”。

一旦进入网络，该组织的附属公司将加密数据并删除勒索软件记录，但通常不包括赎金要求或付款详细信息。相反，受害者会获得一个客户端 ID 和指示，让他们通过 Tor 浏览器通过 .onion URL 联系该组织。研究人员表示，受害者通常有 3-90 天的时间付款，否则他们的数据将发布在 RansomHub Tor 数据泄露网站上。

为了加密数据，该小组使用椭圆曲线加密算法 Curve 25519 并使用间歇性加密。勒索软件以数据为目标，通常不会加密可执行文件。

在公告中，CISA 将 IP 地址（许多与 QakBot 相关联）和电子邮件地址列为潜在的 IOC。

### **如何应对 RansomHub 攻击**

如果受害者认为他们已成为 RansomHub 附属公司的目标，这些机构建议将任何可能受影响的主机下线，重新映像它们并颁发新的帐户凭证。他们还应该监控他们的系统是否有可疑行为。

CISA 及其合作伙伴还建议组织维护多个分段数据备份，并遵循 NIST 密码策略指南。CISO 还应确保组织通过测试和练习来验证其安全控制措施。

*阅读有关 CISA 勒索软件计划的更多信息：通过 CISA 勒索软件计划保护超过 850 台易受攻击的设备*

#StopRansomware 联合网络安全咨询说明由 FBI、CISA、多州信息共享和分析中心 （MS-ISAC） 和卫生与公众服务部 （HHS） 发布。

本文翻译自infosecurity-magazine [原文链接](https://www.infosecurity-magazine.com/news/us-authorities-ransomhub/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299726](/post/id/299726)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity-magazine](https://www.infosecurity-magazine.com/news/us-authorities-ransomhub/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/us-authorities-ransomhub/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**1赞

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