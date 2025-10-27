---
title: 研究人员发现了与网络犯罪集团 FIN7 有关的新基础设施
url: https://www.anquanke.com/post/id/299294
source: 安全客-有思想的安全新媒体
date: 2024-08-21
fetch_date: 2025-10-06T18:00:35.780982
---

# 研究人员发现了与网络犯罪集团 FIN7 有关的新基础设施

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

# 研究人员发现了与网络犯罪集团 FIN7 有关的新基础设施

阅读量**68181**

发布时间 : 2024-08-20 11:46:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167258/cyber-crime/experts-found-infrastructure-fin7.html>

译文仅供参考，具体内容表达以及含义原文为准。

## Cymru、Silent Push 和 Stark Industries Solutions 团队的研究人员发现了与网络犯罪组织 FIN7 相关的新基础设施。

Cymru团队的研究人员确定了两个可能与网络犯罪组织FIN7有关的集群。该团队与 Silent Push 和 Stark Industries Solutions 的网络安全专家合作，他们分享了他们的发现。

FIN7 是一个俄罗斯犯罪集团（又名 Carbanak），自 2015 年年中以来一直活跃，它专注于美国的餐馆、赌博和酒店业，以收集用于攻击或在网络犯罪市场出售的金融信息。

这些集群分别显示了从分配给 Post Ltd（俄罗斯）和 Smart Ape（爱沙尼亚）的 IP 地址入站到 FIN7 基础设施的通信。研究人员确定了 25 个 Stark 分配的 IP 地址，用于托管与 FIN7 组执行的操作相关的域。

专家们向斯塔克的安全团队报告了他们的发现，安全团队立即暂停了这些地址。Stark 的初步反馈表明，受感染的主机可能是从他们的一个经销商那里获得的。Stark Industries Solutions 是一个白标品牌，通过各种经销商销售服务。确定的 9 个 IP 地址被用作进一步调查的起点，使团队能够追踪和破坏其他 FIN7 基础设施和活动。

第一个集群涉及分配给Post Ltd的四个IP地址，Post Ltd是一家在俄罗斯北高加索地区运营的宽带提供商。

*“在过去的 30 天里，我们观察到这些 IP 地址与至少 15 个 Stark 分配的主机进行通信，我们将其与 Silent Push 研究中引用的 TTP 相关联。这些主机包括 **86.104.72.16**，它位于 Silent Push 的原始指标列表中。*

![FIN7 cluster 1]()

第二个集群由分配给爱沙尼亚云托管提供商 SmartApe 的三个 IP 地址组成。

*“在过去的 30 天里，我们观察到这些 IP 地址与至少 16 个 Stark 分配的主机进行通信，我们将其与 Silent Push 研究中引用的 TTP 相关联。同样，这些主机包括 **86.104.72.16**。*

专家们还注意到，在Post Ltd集群中发现的12个宿主在SmartApe集群中也被观察到。

![FIN7 cluster 2]()

“除了在上述两个集群中确定的 19 个主机外，Stark 安全团队的见解还发现了另外 6 个主机，我们评估它们与同一活动有关，”报告总结道。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167258/cyber-crime/experts-found-infrastructure-fin7.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299294](/post/id/299294)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167258/cyber-crime/experts-found-infrastructure-fin7.html)

如若转载,请注明出处： <https://securityaffairs.com/167258/cyber-crime/experts-found-infrastructure-fin7.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [Cymru、Silent Push 和 Stark Industries Solutions 团队的研究人员发现了与网络犯罪组织 FIN7 相关的新基础设施。](#h2-0)

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