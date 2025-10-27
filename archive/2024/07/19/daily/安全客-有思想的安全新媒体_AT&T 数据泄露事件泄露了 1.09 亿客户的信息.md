---
title: AT&T 数据泄露事件泄露了 1.09 亿客户的信息
url: https://www.anquanke.com/post/id/298034
source: 安全客-有思想的安全新媒体
date: 2024-07-19
fetch_date: 2025-10-06T17:40:51.346499
---

# AT&T 数据泄露事件泄露了 1.09 亿客户的信息

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

# AT&T 数据泄露事件泄露了 1.09 亿客户的信息

阅读量**72688**

发布时间 : 2024-07-18 15:14:30

**x**

##### 译文声明

本文是翻译文章，文章来源：Heimdal

原文地址：<https://heimdalsecurity.com/blog/att-data-breach-109-million-customers/>

译文仅供参考，具体内容表达以及含义原文为准。

黑客在AT&T数据泄露事件中获得了大约1.09亿人的电话和短信记录。

2024 年 4 月，托管在 Snowflake 帐户中的 AT&T 在线数据库遭到破坏。

## AT&T数据泄露影响了哪些信息？

该事件影响了该公司几乎所有在 2022 年 5 月 1 日至 10 月 31 日以及 2023 年 1 月 2 日进行通信的移动客户。

尽管电话和短信记录遭到破坏，但根据AT&T的说法，黑客无法访问电话或消息的内容。

> 下载的数据不包括任何通话或短信的内容。它没有电话或短信的时间戳。它也没有任何详细信息，例如社会安全号码、出生日期或其他个人身份信息。

来源 – AT&T 声明

![]()

###

来源 – 美国证券交易委员会表格

### 被盗数据包括：

* AT&T有线用户的电话号码
* AT&T或MVNO无线号码联系的电话号码
* 号码参与的电话或短信数量
* 某一天或某月的通话时长

此外，根据AT&T的声明

> 对于记录的子集，还包括与交互关联的一个或多个蜂窝基站 ID 号。

来源 – AT&T 声明

尽管数据不会将姓名和其他个人身份信息与电话号码相关联，但黑客可以使用其他被盗数据库进行匹配。因此，他们可以详细说明通信模式并找出谁与谁建立联系。

此外，他们可以将这种情报用于社会工程、在线冒充和网络钓鱼攻击。

该公司表示，他们将仅通过电子邮件或美国邮件联系所有以前或当前受影响的客户。

## 如何保护敏感数据

AT&T数据泄露的根源在于第三方运营商Snowflake的泄露事件。因此，AT&T似乎在保护数据方面做得不多。但是，在与第三方合作时，公司应强制执行一些标准安全措施：

### **签署安全协议**

确保您的协作者遵循您使用的相同安全策略。明确要求第三方采取数据保护措施。保留对运营商是否采用安全最佳实践进行审核的权利。阅读本《第三方风险管理指南》以获取灵感。

### **加密敏感数据**

使用端到端加密来保护传输中的敏感数据。如果黑客通过DNS隧道或利用VPN漏洞获取您的数据，他们将无法读取和使用它们。此外，加密静态敏感数据。

### **定期审核**

根据您与第三方运营商签署的安全协议，定期进行审核。这将使您了解是否存在可能影响您的数据的安全问题。

本文翻译自Heimdal [原文链接](https://heimdalsecurity.com/blog/att-data-breach-109-million-customers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298034](/post/id/298034)

安全KER - 有思想的安全新媒体

本文转载自: [Heimdal](https://heimdalsecurity.com/blog/att-data-breach-109-million-customers/)

如若转载,请注明出处： <https://heimdalsecurity.com/blog/att-data-breach-109-million-customers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [AT&T数据泄露影响了哪些信息？](#h2-0)
  + [被盗数据包括：](#h3-2)
* [如何保护敏感数据](#h2-3)
  + [签署安全协议](#h3-4)
  + [加密敏感数据](#h3-5)
  + [定期审核](#h3-6)

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