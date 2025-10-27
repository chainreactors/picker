---
title: 新的二维码网络钓鱼活动利用 Microsoft Sway 窃取凭据
url: https://www.anquanke.com/post/id/299603
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:19.063092
---

# 新的二维码网络钓鱼活动利用 Microsoft Sway 窃取凭据

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

# 新的二维码网络钓鱼活动利用 Microsoft Sway 窃取凭据

阅读量**159471**

发布时间 : 2024-08-29 15:57:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员正在提请注意一种新的 QR 码网络钓鱼（又名 quishing）活动，该活动利用 Microsoft Sway 基础设施托管虚假页面，再次凸显了出于恶意目的滥用合法云产品的情况。

“通过使用合法的云应用程序，攻击者为受害者提供了可信度，帮助他们信任它所提供的内容，”Netskope 威胁实验室研究员 Jan Michael Alcantara 说。

“此外，受害者在打开 Sway 页面时使用他们已经登录的 Microsoft 365 帐户，这也可以帮助说服他们了解其合法性。Sway 还可以通过链接（URL 链接或视觉链接）共享，或使用 iframe 嵌入到网站上。

这些攻击主要针对亚洲和北美的用户，其中科技、制造和金融行业是最受欢迎的行业。

Microsoft Sway 是一种基于云的工具，用于创建新闻稿、演示文稿和文档。自 365 年以来，它一直是 Microsoft 2015 系列产品的一部分。

这家网络安全公司表示，从 2024 年 7 月开始，它观察到独特的 Microsoft Sway 网络钓鱼页面的流量增加了 2024 倍，最终目标是窃取用户的 Microsoft 365 凭据。这是通过提供 Sway 上托管的虚假 QR 码来实现的，扫描后，会将用户重定向到网络钓鱼网站。

为了进一步逃避静态分析工作，已经观察到其中一些压制活动使用 Cloudflare Turnstile 作为向静态 URL 扫描器隐藏域的一种方式。

该活动还以利用中间对手 （AitM） 网络钓鱼策略（即透明网络钓鱼）来使用相似的登录页面来窃取凭据和双因素身份验证 （2FA） 代码而著称，同时尝试将受害者登录到服务中。

“使用二维码将受害者重定向到网络钓鱼网站给防御者带来了一些挑战，”Michael Alcantara 说。“由于 URL 嵌入在图像中，因此只能扫描基于文本的内容的电子邮件扫描仪可能会被绕过。”

“此外，当用户收到二维码时，他们可能会使用其他设备（例如手机）来扫描二维码。由于在移动设备（尤其是个人手机）上实施的安全措施通常不如笔记本电脑和台式机严格，因此受害者通常更容易受到滥用。

这不是网络钓鱼攻击第一次滥用 Microsoft Sway。2020 年 4 月，Group-IB 详细介绍了一项名为 PerSwaysion 的活动，该活动通过使用 Sway 作为跳板，将受害者重定向到凭据收集网站，成功地入侵了德国、英国、荷兰、香港和新加坡多家公司的至少 156 名高级官员的企业电子邮件帐户。

随着安全供应商制定对策来检测和阻止此类基于图像的威胁，压制活动变得越来越复杂。

“巧妙的是，攻击者现在已经开始使用 Unicode 文本字符而不是图像制作二维码，”SlashNext 首席技术官 J. Stephen Kowski 说。“这种我们称之为’Unicode QR 码网络钓鱼’的新技术对传统的安全措施提出了重大挑战。”

使该攻击特别危险的是，它完全绕过了旨在扫描可疑图像的检测，因为它们完全由文本字符组成。此外，Unicode QR 码可以完美地呈现在屏幕上，没有任何问题，并且在以纯文本形式查看时看起来明显不同，这进一步使检测工作复杂化。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299603](/post/id/299603)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络钓鱼](/tag/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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