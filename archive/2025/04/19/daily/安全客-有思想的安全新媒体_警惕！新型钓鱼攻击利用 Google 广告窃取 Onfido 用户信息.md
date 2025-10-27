---
title: 警惕！新型钓鱼攻击利用 Google 广告窃取 Onfido 用户信息
url: https://www.anquanke.com/post/id/306692
source: 安全客-有思想的安全新媒体
date: 2025-04-19
fetch_date: 2025-10-06T22:05:14.097133
---

# 警惕！新型钓鱼攻击利用 Google 广告窃取 Onfido 用户信息

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

# 警惕！新型钓鱼攻击利用 Google 广告窃取 Onfido 用户信息

阅读量**90896**

发布时间 : 2025-04-18 15:03:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/onfido-users-targeted-in-google-ad-malvertising-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![malver]()

一场新的网络钓鱼活动出现了，它并非通过收件箱来骗取信任，而是借助 Google 广告。Push 的安全研究人员发现了一场恶意广告活动，其目标瞄准了 Onfido 的用户。Onfido 是一个在金融科技、人力资源以及受监管行业中广泛使用的数字身份验证平台。

攻击者使用了一条具有欺骗性的 Google 搜索广告，引诱受害者点击一个虚假的 Onfido 登录页面，该页面所在的域看起来十分正规：dashboard [.] onfido [.] us [.] com。

![]()

一旦用户点击，这个恶意链接会导向一个克隆的 Onfido 页面，其看起来足够可信，足以骗过受害者。不过，Push 基于浏览器的检测系统立即标记了这个网址。这个虚假的登录页面是通过 Evilginx（一种中间人网络钓鱼框架）来提供服务的，该框架会代理合法页面，以窃取会话令牌和用户凭证。

有趣的是，这个网络钓鱼页面被配置为仅在通过 Google 广告推荐访问时才会正常显示。直接访问同一个域名会将用户重定向到合法 Onfido 域名的 404 页面 —— 这是一种逃避检测的策略，目的是躲避安全爬虫的检查。

Onfido 并不像 Microsoft 或 Google 那样是典型的网络钓鱼目标。但这恰恰是关键所在。

随着围绕主要平台的网络钓鱼防御措施日益加强，攻击者正将注意力转移到那些监控较少的软件即服务（SaaS）工具上，这些工具往往缺乏诸如密钥支持或强大身份验证策略等功能。

这次攻击是恶意广告的一个典型案例 —— 利用付费搜索结果来推送恶意链接。Google 广告并不像电子邮件网关那样依赖相同的信誉和域名历史检查，这为攻击者提供了一个全新的渠道来发起网络钓鱼尝试。

所使用的虚假域名是 us [.] com—— 这并非一个合法的美国政府顶级域名，而是一个域名转售服务，它允许子域名冒充受信任的品牌。这种域名便宜且易于注册，普通用户很难将其与真正的.us 域名区分开来。

尽管 Evilginx 最初是作为红队工具被开发出来的，但如今它在现实中的网络钓鱼活动中被越来越多地使用。它的优势在于其灵活性 —— 几乎可以代理任何登录页面，且无需大量定制的 JavaScript 代码，这降低了它被安全工具检测到的可能性。

即便你的电子邮件没有问题，你的搜索栏也可能是最薄弱的环节。正如 Push 所说：“像恶意广告这种绕过电子邮件的网络钓鱼攻击非常有吸引力”，因为它们完全避开了防御措施。

本文翻译自securityonline [原文链接](https://securityonline.info/onfido-users-targeted-in-google-ad-malvertising-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306692](/post/id/306692)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/onfido-users-targeted-in-google-ad-malvertising-campaign/)

如若转载,请注明出处： <https://securityonline.info/onfido-users-targeted-in-google-ad-malvertising-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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