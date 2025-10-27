---
title: 在全球酒店和办公室使用的 RFID 卡中发现了硬件后门
url: https://www.anquanke.com/post/id/299445
source: 安全客-有思想的安全新媒体
date: 2024-08-24
fetch_date: 2025-10-06T18:01:13.258648
---

# 在全球酒店和办公室使用的 RFID 卡中发现了硬件后门

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

# 在全球酒店和办公室使用的 RFID 卡中发现了硬件后门

阅读量**66957**

发布时间 : 2024-08-23 11:17:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/hardware-backdoor-discovered-in-rfid.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员在特定型号的MIFARE Classic非接触式卡中发现了一个硬件后门，该后门可能允许使用未知密钥进行身份验证，并打开酒店房间和办公室门。

这些攻击已经针对FM11RF08S进行了演示，这是上海复旦微电子于 2020 年发布的 MIFARE Classic 的新变体。

Quarkslab研究员Philippe Teuwen说：“FM11RF08S后门使任何了解它的实体都可以破坏这些卡上的所有用户定义的密钥，即使完全多样化，只需访问卡几分钟。

密钥不仅在现有的FM11RF08S卡中是通用的，而且调查发现，“处于供应链攻击地位的实体可以立即执行攻击”。

雪上加霜的是，在上一代产品中发现了一个类似的后门，FM11RF08，它受到另一个密钥的保护。在可追溯到 2007 年 11 月的卡片中已经观察到后门。

该攻击的优化版本可以通过对随机数生成机制进行部分逆向工程，将破解密钥的过程加快五到六倍。

“后门 […]允许瞬间克隆用于打开世界各地办公室门和酒店房间的RFID智能卡，“该公司在一份声明中说。

“尽管后门只需要在物理上接近受影响的卡几分钟即可进行攻击，但有能力进行供应链攻击的攻击者可以立即大规模执行此类攻击。”

敦促消费者检查他们是否易感，特别是考虑到这些卡在美国、欧洲和印度的酒店中广泛使用。

Teuwen指出，后门及其密钥“允许我们发起新的攻击来转储和克隆这些卡，即使它们的所有密钥都适当多样化。

这不是酒店使用的锁定系统中第一次发现安全问题。今年 3 月初，Dormacaba 的 Saflok 电子 RFID 锁被发现存在严重缺陷，威胁行为者可能会利用这些缺陷来伪造钥匙卡和解锁门。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/hardware-backdoor-discovered-in-rfid.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299445](/post/id/299445)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/hardware-backdoor-discovered-in-rfid.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/hardware-backdoor-discovered-in-rfid.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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