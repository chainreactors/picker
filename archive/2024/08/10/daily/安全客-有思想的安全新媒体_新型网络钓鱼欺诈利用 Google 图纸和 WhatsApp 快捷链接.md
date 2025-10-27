---
title: 新型网络钓鱼欺诈利用 Google 图纸和 WhatsApp 快捷链接
url: https://www.anquanke.com/post/id/298978
source: 安全客-有思想的安全新媒体
date: 2024-08-10
fetch_date: 2025-10-06T17:59:19.820254
---

# 新型网络钓鱼欺诈利用 Google 图纸和 WhatsApp 快捷链接

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

# 新型网络钓鱼欺诈利用 Google 图纸和 WhatsApp 快捷链接

阅读量**36442**

发布时间 : 2024-08-09 14:47:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-phishing-scam-uses-google-drawings.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种新颖的网络钓鱼活动，该活动利用 Google 绘图和通过 WhatsApp 生成的缩短链接来逃避检测并诱骗用户点击旨在窃取敏感信息的虚假链接。

“攻击者选择了一组计算领域最知名的网站来制造威胁，包括谷歌和WhatsApp来托管攻击元素，以及一个看起来像亚马逊的网站来收集受害者的信息，”Menlo安全研究员Ashwin Vamshi说。“这次攻击是’依赖受信任的站点 （LoTS）’威胁的一个很好的例子。”

攻击的起点是一封网络钓鱼电子邮件，该电子邮件将收件人定向到一个图形，该图形似乎是亚马逊帐户验证链接。就其本身而言，该图形托管在 Google 绘图上，显然是为了逃避检测。

滥用合法服务对攻击者有明显的好处，因为它们不仅是一种低成本的解决方案，而且更重要的是，它们提供了一种在网络内部的秘密通信方式，因为它们不太可能被安全产品或防火墙阻止。

“在攻击开始时，Google绘图吸引人的另一件事是，它允许用户（在这种情况下是攻击者）在他们的图形中包含链接，”Vamshi说。“这些链接很容易被用户忽视，特别是如果他们对他们的亚马逊账户面临潜在威胁感到紧迫感。”

最终点击验证链接的用户将被带到一个类似于亚马逊的登录页面，该页面使用两种不同的URL缩短器连续制作URL–WhatsApp（“l.wl[.]co“），其次是 qrco[.]de — 作为混淆和欺骗安全 URL 扫描器的附加层。

虚假页面旨在收集凭据、个人信息和信用卡详细信息，然后将受害者重定向到原始的网络钓鱼亚马逊登录页面。作为额外的步骤，一旦验证了凭据，网页将无法从同一 IP 地址访问。

研究人员在Microsoft 365的反网络钓鱼机制中发现了一个漏洞，该漏洞可能被滥用以增加用户打开网络钓鱼电子邮件的风险。

该方法需要使用 CSS 技巧来隐藏“首次接触安全提示”，当用户收到来自未知地址的电子邮件时，它会提醒用户。Microsoft已经承认了这个问题，但尚未发布修复程序。

奥地利网络安全机构Certitude表示：“首次接触安全提示被附加在HTML电子邮件的正文之前，这意味着可以通过使用CSS样式标签来改变其显示方式。“我们可以更进一步，欺骗 Microsoft Outlook 添加到加密和/或签名的电子邮件中的图标。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-phishing-scam-uses-google-drawings.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298978](/post/id/298978)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-phishing-scam-uses-google-drawings.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-phishing-scam-uses-google-drawings.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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