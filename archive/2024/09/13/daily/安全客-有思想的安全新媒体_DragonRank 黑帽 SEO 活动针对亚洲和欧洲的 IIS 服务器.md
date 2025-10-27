---
title: DragonRank 黑帽 SEO 活动针对亚洲和欧洲的 IIS 服务器
url: https://www.anquanke.com/post/id/300034
source: 安全客-有思想的安全新媒体
date: 2024-09-13
fetch_date: 2025-10-06T18:20:08.419102
---

# DragonRank 黑帽 SEO 活动针对亚洲和欧洲的 IIS 服务器

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

# DragonRank 黑帽 SEO 活动针对亚洲和欧洲的 IIS 服务器

阅读量**62024**

发布时间 : 2024-09-12 14:50:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/dragonrank-black-hat-seo-campaign.html>

译文仅供参考，具体内容表达以及含义原文为准。

一个 “简体中文演员 ”已经与一个针对亚洲和欧洲多个国家的新活动相关联，该活动的最终目标是执行搜索引擎优化 （SEO） 排名操纵。

黑帽 SEO 集群被 Cisco Talos 代号为 **DragonRank**，受害者足迹分散在泰国、印度、韩国、比利时、荷兰和中国。

“DragonRank 利用目标的 Web 应用程序服务来部署 Web shell，并利用它来收集系统信息并启动 PlugX 和 BadIIS 等恶意软件，运行各种凭据收集实用程序，”安全研究员 Joey Chen 说。

这些攻击导致 35 台 Internet 信息服务 （IIS） 服务器遭到入侵，最终目标是部署 BadIIS 恶意软件，ESET 于 2021 年 8 月首次记录了该恶意软件。

它专门设计用于通过将受感染的 IIS 服务器变成其客户（即其他威胁行为者）与其受害者之间恶意通信的中继点来促进代理软件和 SEO 欺诈。

最重要的是，它可以修改提供给搜索引擎的内容，以操纵搜索引擎算法并提高攻击者感兴趣的其他网站的排名。

“调查最令人惊讶的方面之一是 IIS 恶意软件的多功能性，以及 [检测] SEO 欺诈犯罪计划，其中恶意软件被滥用于操纵搜索引擎算法并帮助提升第三方网站的声誉，”安全研究员 Zuzana Hromcova 当时告诉 The Hacker News。

Talos 强调的最新一组攻击涵盖了广泛的垂直行业，包括珠宝、媒体、研究服务、医疗保健、视频和电视制作、制造、运输、宗教和精神组织、IT 服务、国际事务、农业、体育和风水。

攻击链首先利用 phpMyAdmin 和 WordPress 等 Web 应用程序中的已知安全漏洞来放置开源 ASPXspy Web shell，然后充当将补充工具引入目标环境的渠道。

该活动的主要目标是破坏托管企业网站的 IIS 服务器，滥用它们来植入 BadIIS 恶意软件，并通过利用与色情和性相关的关键字有效地将它们重新用作诈骗操作的启动板。

该恶意软件的另一个重要方面是，当它将连接中继到命令和控制 （C2） 服务器时，它能够在其 User-Agent 字符串中伪装成 Google 搜索引擎爬虫，从而允许它绕过某些网站安全措施。

“威胁行为者通过更改或利用搜索引擎算法来提高网站在搜索结果中的排名，从而进行 SEO 操纵，”Chen 解释说。“他们进行这些攻击是为了将流量吸引到恶意网站，提高欺诈内容的知名度，或通过人为夸大或缩小排名来扰乱竞争对手。”

DragonRank 与其他黑帽 SEO 网络犯罪团伙区别开来的一个重要之处在于，它试图使用 PlugX（中国威胁行为者广泛共享的后门）和各种凭据收集程序（如 Mimikatz、PrintNotifyPotato、BadPotato 和 GodPotato）来破坏目标网络中的其他服务器并保持对它们的控制。

尽管攻击中使用的 PlugX 恶意软件依赖于 DLL 旁加载技术，但负责启动加密有效负载的加载程序 DLL 使用 Windows 结构化异常处理 （SEH） 机制，以试图确保合法文件（即易受 DLL 旁加载影响的二进制文件）可以加载 PlugX，而不会触发任何警报。

Talos 出土的证据表明，威胁行为者以“tttseo”和 QQ 即时消息应用程序在 Telegram 上保持存在，以促进与付费客户的非法商业交易。

“这些对手还提供看似优质的客户服务，量身定制促销计划以最好地满足客户的需求，”Chen 补充道。

“客户可以提交他们希望推广的关键字和网站，DragonRank 会制定适合这些规范的策略。该集团还专门针对特定国家和语言进行促销活动，确保提供定制和全面的在线营销方法。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/dragonrank-black-hat-seo-campaign.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300034](/post/id/300034)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/dragonrank-black-hat-seo-campaign.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/dragonrank-black-hat-seo-campaign.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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