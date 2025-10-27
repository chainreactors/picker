---
title: 由 Snowflake 帐户攻击后续分析：攻击源于合法凭证暴露
url: https://www.anquanke.com/post/id/297996
source: 安全客-有思想的安全新媒体
date: 2024-07-18
fetch_date: 2025-10-06T17:38:44.181186
---

# 由 Snowflake 帐户攻击后续分析：攻击源于合法凭证暴露

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

# 由 Snowflake 帐户攻击后续分析：攻击源于合法凭证暴露

阅读量**60286**

发布时间 : 2024-07-17 11:20:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Stephanie Schneider，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/snowflake-account-attacks-driven-by-exposed-legitimate-credentials>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者刚刚完成了 2024 年最大的数据泄露事件之一，他们甚至不必入侵公司的环境。他们的目标是什么？从云存储系统中窃取数据并勒索受害者以获取经济利益。

针对 Snowflake 客户的活动并不是新颖或复杂的策略、技术或程序 （TTP） 的结果。相反，该活动背后的威胁行为者购买或发现已经可用的暴露的合法凭据，并使用它们登录。对于没有多重身份验证 （MFA） 的帐户，仅此而已。正在进行的 Snowflake 活动为凭证管理提供了另一个引人注目的用例，并警告了信息窃取者和被盗凭据的危险。

2024 年 5 月下旬，一个被追踪为 UNC5537 的出于经济动机的威胁行为者开始在网络犯罪论坛上宣传出售 Ticketmaster 和 Santander 的数据，声称他们已经破坏了云数据仓库平台 Snowflake。

Snowflake 和 Mandiant 的分析发现，使用被盗的客户凭据破坏了个人客户帐户。根据 Mandiant 的说法，威胁行为者可能已经能够使用这些暴露的凭据访问大约 165 家公司的帐户。

## 关键要点

几个关键要点：

1. 受影响的帐户未配置 MFA。成功的身份验证只需要有效的用户名和密码，这使威胁参与者可以轻松访问目标帐户。
2. 分析显示，在信息窃取恶意软件输出中发现的一些凭据已经在暗网上出售多年，并且仍然有效，这意味着这些凭据没有被轮换或更新。信息窃取程序是一种恶意软件，旨在从受感染的设备中窃取敏感信息，这可能导致未经授权的访问和数据盗窃。在 Snowflake 攻击的情况下，信息窃取者通过受感染的设备捕获了 Snowflake 客户用户的登录凭据，从而允许攻击者访问存储在平台上的客户帐户和数据。此外，信息窃取者可能会泄露敏感的客户信息，包括个人数据、财务记录和商业智能。
3. 受感染的 Snowflake 实例没有网络允许列表。允许列表涉及编译受制裁实体的列表，例如 IP 地址、域和应用程序。只有此指定列表中的实体才被授予对特定资源的访问权限或可以执行特定操作的权限。此方法通过减少攻击面和限制对受信任、经过验证的实体的访问来帮助增强安全性。

鉴于该活动的高调成功以及云存储提供商通常可用的数据的深度和广度，我们可以预期类似的凭证填充工作会有所增加。现在是时候验证您的相关安全控制（例如密码策略）是否尽可能安全，以避免潜在的风险。

## 如何增强防御力

如何增强对此类攻击的防御能力？

* 启用 MFA。 MFA 是一种简单而高效的措施，可以显著改善组织的安全状况和弹性。凭据可能会通过网络钓鱼或恶意软件（如信息窃取程序）被盗。但是，MFA 不仅需要密码来访问帐户，还增加了额外的安全层，使攻击更难获得未经授权的访问。
* 管理您的凭据。 尽组织所能，监视暗网中是否有公开的凭据。这可能是通过供应商、信用监控或其他途径。如果您收到个人信息已泄露的通知，请务必尽快采取行动评估风险并确定适当的后续步骤，包括可能更改密码。
* 监控针对供应商的网络活动。 通过开源报告或其他方式建立监控，以获得可能针对关键服务提供商的网络攻击活动的早期预警。使用预先通知更改凭据，并确认与受影响公司的连接中的策略合规性。

最近的 Snowflake 帐户攻击凸显了强大的凭据管理和 MFA 在保护云存储系统方面的重要性。随着基于凭据的攻击的频率和规模可能会增加，现在是组织加强防御并确保其安全实践能够抵御不断变化的威胁的时候了。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/snowflake-account-attacks-driven-by-exposed-legitimate-credentials)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297996](/post/id/297996)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/snowflake-account-attacks-driven-by-exposed-legitimate-credentials)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/snowflake-account-attacks-driven-by-exposed-legitimate-credentials>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [关键要点](#h2-0)
* [如何增强防御力](#h2-1)

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