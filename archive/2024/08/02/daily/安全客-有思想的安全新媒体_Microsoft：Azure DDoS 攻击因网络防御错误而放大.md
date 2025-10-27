---
title: Microsoft：Azure DDoS 攻击因网络防御错误而放大
url: https://www.anquanke.com/post/id/298668
source: 安全客-有思想的安全新媒体
date: 2024-08-02
fetch_date: 2025-10-06T18:01:00.877119
---

# Microsoft：Azure DDoS 攻击因网络防御错误而放大

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

# Microsoft：Azure DDoS 攻击因网络防御错误而放大

阅读量**132057**

发布时间 : 2024-08-01 14:22:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/microsoft-azure-ddos-attack-amplified-cyber-defense-error>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft昨天将实施错误归咎于放大了分布式拒绝服务（DDoS）攻击的影响，该攻击最终导致该公司的Azure云服务中断了近八个小时。

该攻击影响了多个 Azure 产品/服务，包括 Azure App Services、Azure IoT Central、Application Insights、Log Search Alerts 和 Azure Policy。中断从美国东部时间上午 7 点 45 分左右开始，一直持续到美国东部时间下午 3 点 43 分，还影响了主要的 Azure 门户以及 Microsoft 365 和 Microsoft Purview 数据保护服务的一个子集。

## DDoS 网络防御错误正在调查中

在昨天的事件摘要中，Microsoft 将 DDoS 攻击描述为导致“意外的使用激增，导致 Azure Front Door （AFD） 和 Azure 内容分发网络 （CDN） 组件的性能低于可接受的阈值。峰值导致间歇性服务错误、超时和突然增加延迟。

在某些方面更令人担忧的是，“虽然最初的触发事件是DDoS攻击，它激活了我们的DDoS保护机制，但初步调查表明，我们防御措施实施中的错误放大了攻击的影响，而不是减轻了它。

Microsoft 尚未具体确定加剧 DDoS 攻击的错误。但根据其对 7 月 30 日事件的描述，该公司为支持 DDoS 缓解工作而进行的初始网络配置更改可能会导致一些意想不到的“副作用”。该公司实施了一种更新的方法，首先在亚太地区和欧洲推出，然后在验证该方法有效后在美洲部署。

“我们的团队将完成一次内部回顾，以更详细地了解这一事件，”Microsoft表示。“我们将在大约 72 小时内发布初步事故后审查 （PIR），以分享有关发生的事情以及我们如何应对的更多详细信息。”

## DDoS 缓解中的无意错误

Tenable 的研究工程师 Rody Quinlan 表示，组织可以通过多种方式破坏 DDoS 缓解工作。

他说：“组织可能会通过各种实施错误无意中放大网络攻击，例如配置错误的速率限制、低效的负载均衡、防火墙配置错误、过于激进的安全规则、资源扩展不足、不正确的流量过滤以及对单点故障的依赖。“这些错误可能导致合法流量受阻、服务器超载、防火墙瓶颈以及关键服务脱机。”

虽然Microsoft的初步回应可能导致了本周的Azure服务问题，但这一事件再次提醒人们，对于希望破坏和降低目标在线形象的对手来说，DDoS攻击仍然有效。

Cloudflare今年早些时候的一份报告发现，网络层DDoS攻击同比增长了117%。造成这种情况的部分原因是针对黑色星期五及其前后的零售、运输和公共关系网站的 DDoS 攻击的具体增加以及一般的假日购物季。然而，许多攻击也是由希望发出特定信息或传达特定政治立场的团体发起的。例如，Cloudflare表示，它观察到针对台湾、以色列和巴勒斯坦地区的DDoS攻击大幅增加，这些地区的地缘政治紧张局势以及对环境科学网站的攻击。

## DDoS攻击采用“粉碎抢夺”策略

“DDoS 的趋势通常是周期性的，但目前我们看到攻击的规模越来越大，持续时间越来越短，”DDoS 安全供应商 Nexusguard 的主管 Donny Chong 说。“我们的最新数据显示，去年攻击规模平均增加了183%，平均规模为0.80Gbps，”他说。与此同时，在 2022 年至 2023 年期间，DDoS 攻击的平均持续时间降至略高于 101 分钟。Chong 说，目前，81% 的 DDoS 攻击持续时间不到 90 分钟。

“攻击持续时间减少的部分原因是攻击者在对业务造成干扰时变得越来越高效，”可能是因为他们正在使用人工智能 （AI） 来自动化某些攻击。但是，较短的攻击持续时间也可能是由于缓解技术造成的，Chong说。“[攻击者]发现越来越难以维持长时间的中断。因此，现在更多的是’砸抢’，而不是长期的围困，“他说。

Quinlan 表示，缓解 DDoS 中断的关键是拥有实时流量分析功能、可扩展的云基础设施、冗余系统和智能负载均衡以防止过载。Quinlan 说：“适当的速率限制、节流和 WAF（Web 应用程序防火墙）过滤恶意流量，以及定期的软件和硬件漏洞修复对于保护系统至关重要。“有效的事件响应计划以及与互联网服务提供商和安全提供商的合作可以增强检测和缓解能力。”

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/microsoft-azure-ddos-attack-amplified-cyber-defense-error)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298668](/post/id/298668)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/microsoft-azure-ddos-attack-amplified-cyber-defense-error)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/microsoft-azure-ddos-attack-amplified-cyber-defense-error>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [DDOS](/tag/DDOS)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [DDoS 网络防御错误正在调查中](#h2-0)
* [DDoS 缓解中的无意错误](#h2-1)
* [DDoS攻击采用“粉碎抢夺”策略](#h2-2)

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