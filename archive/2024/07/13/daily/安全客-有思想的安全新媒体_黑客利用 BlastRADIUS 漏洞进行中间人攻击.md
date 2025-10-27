---
title: 黑客利用 BlastRADIUS 漏洞进行中间人攻击
url: https://www.anquanke.com/post/id/297824
source: 安全客-有思想的安全新媒体
date: 2024-07-13
fetch_date: 2025-10-06T17:39:36.953977
---

# 黑客利用 BlastRADIUS 漏洞进行中间人攻击

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

# 黑客利用 BlastRADIUS 漏洞进行中间人攻击

阅读量**143011**

发布时间 : 2024-07-12 09:57:47

**x**

##### 译文声明

本文是翻译文章，文章来源：Heimdal

原文地址：<https://heimdalsecurity.com/blog/blastradius-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员警告称，RADIUS网络认证协议中的一个缺陷，名为BlastRADIUS，可以帮助黑客执行中间人（Man-in-the-middle，简称MitM）攻击。

RADIUS是Remote Authentication Dial-In User Service（远程认证拨入用户服务）的缩写，这是一种用于验证用户和设备的客户端/服务器协议。各种网络设备，如交换机、路由器、接入点和其他路由基础设施都依赖于它。

RADIUS在应用层运行，可以使用传输控制协议（TCP）或用户数据报协议（UDP）。

## 有关 BlastRADIUS 缺陷的更多信息

Blast-RADIUS 使用协议漏洞 CVE-2024-3596 和 MD5 哈希算法。因此，它们使攻击者能够访问 RADIUS 流量。此外，黑客将能够：

* 操作服务器响应
* 添加任意协议属性
* 获得 RADIUS 设备的管理员权限

![radius attack diagram]()

来源 – Blast-RADIUS 研究团队

他们如何在不需要暴力破解或窃取凭据的情况下以管理员身份进行身份验证？

研究人员解释说，一旦他们访问使用RADIUS的网络，攻击者就可以对RADIUS服务器做出响应，以将响应更改为任何有效响应。有 4 种可能的类型或响应：

* Access-Accept（接受访问）
* Access-Reject（拒绝访问）
* Access-Challenge（访问挑战）
* Protocol-Error（协议错误）

但在此案例中，响应类型并不重要。

这种能力允许攻击者将拒绝访问（Reject）响应更改为接受访问（Accept），反之亦然。

如果攻击者截获了一个通常在多因素认证（MFA）中使用的访问挑战（Access-Challenge）响应，他们可以将其更改为接受访问（Access-Accept）响应，这将允许他们绕过多因素认证（MFA）。

研究人员还表示，

> 由于 RADIUS 协议的灵活性、代理性质，代理 RADIUS 服务器链中的任何服务器都可能成为攻击成功的目标。

来源 – 卡内基梅隆大学，漏洞说明 VU#456537

## 针对BlastRADIUS攻击的预防措施

安全专家发现 RADIUS 漏洞的利用可能性令人担忧。他们说，在这种情况下，MD5 哈希算法不被认为是可靠的。

> 最近发布的“Blast RADIUS”漏洞表明，RADIUS需要更新。RADIUS 不再可以依赖 MD5 来确保安全性。在更广泛的 Internet 上以明文形式发送设备或位置信息不再被接受。

来源 – IETF

目前，研究人员敦促网络管理员执行以下预防措施：

* 升级到 RADIUS over TLS （RADSEC）
* 开始使用“多跳”RADIUS 部署
* 使用受限访问管理 VLAN 或 TLS/IPsec 隧道将 RADIUS 流量与 Internet 访问隔离开来

本文翻译自Heimdal [原文链接](https://heimdalsecurity.com/blog/blastradius-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297824](/post/id/297824)

安全KER - 有思想的安全新媒体

本文转载自: [Heimdal](https://heimdalsecurity.com/blog/blastradius-flaw/)

如若转载,请注明出处： <https://heimdalsecurity.com/blog/blastradius-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [中间人攻击](/tag/%E4%B8%AD%E9%97%B4%E4%BA%BA%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [热点 | 利用AI造谣幼儿园大火被抓，大模型内容安全谁来守护？](/post/id/308685)

  2025-06-20 16:47:19
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

### 热门推荐

文章目录

* [有关 BlastRADIUS 缺陷的更多信息](#h2-0)
* [针对BlastRADIUS攻击的预防措施](#h2-1)

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