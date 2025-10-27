---
title: Ebury 僵尸网络危害了 400,000 多台 Linux 服务器
url: https://www.anquanke.com/post/id/296592
source: 安全客-有思想的安全新媒体
date: 2024-05-18
fetch_date: 2025-10-06T16:48:21.998897
---

# Ebury 僵尸网络危害了 400,000 多台 Linux 服务器

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

# Ebury 僵尸网络危害了 400,000 多台 Linux 服务器

阅读量**110045**

发布时间 : 2024-05-17 11:51:06

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.helpnetsecurity.com/2024/05/16/ebury-botnet/>

译文仅供参考，具体内容表达以及含义原文为准。

ESET 研究人员发布了对最先进的服务器端恶意软件活动之一的深入调查。它仍在不断增长，并且在其至少 15 年的运营过程中发现了数十万台服务器遭到入侵。

多年来，Ebury 组织和僵尸网络一直参与垃圾邮件的传播、网络流量重定向和凭据窃取。近年来，他们的犯罪行为已转向信用卡和加密货币盗窃。

此外，Ebury 已被部署为后门，可危害近 400,000 台 Linux、FreeBSD 和 OpenBSD 服务器；截至 2023 年底，仍有超过 100,000 台设备受到威胁。在许多情况下，Ebury 运营商可以获得对 ISP 和知名托管提供商的大型服务器的完全访问权限。

Ebury 至少从 2009 年开始活跃，是一个 OpenSSH 后门和凭证窃取者。它用于部署其他恶意软件以通过僵尸网络（例如用于 Web 流量重定向的模块）、垃圾邮件代理流量、执行中间对手攻击 (AitM) 以及支持恶意基础设施的主机来获利。在 AitM 攻击中，ESET 在 2022 年 2 月至 2023 年 5 月期间观察到 34 个国家/地区超过 75 个网络的 200 多个目标。

其运营商使用 Ebury 僵尸网络窃取加密货币钱包、凭证和信用卡详细信息。 ESET 发现了该团伙为了经济利益而编写和部署的新恶意软件系列，其中包括 Apache 模块和用于重定向 Web 流量的内核模块。 Ebury 运营商还利用管理员软件中的零日漏洞批量破坏服务器。

系统遭到破坏后，一些细节就会被泄露。使用在该系统上获得的已知密码和密钥，可以重复使用凭据来尝试登录相关系统。每个 Ebury 的主要版本都引入了重要的更改、新功能和混淆技术。

“我们记录了托管提供商的基础设施受到 Ebury 损害的案例。在这些情况下，我们看到 Ebury 被部署在这些提供商租用的服务器上，而没有向承租人发出警告。这导致 Ebury 攻击者能够同时危害数千台服务器，” ESET 研究人员Marc-Etienne M. Léveillé说道，他对 Ebury 进行了十多年的调查。埃伯里没有地理边界；世界上几乎所有国家都有受到 Ebury 攻击的服务器。每当托管提供商受到损害时，都会导致同一数据中心内的大量服务器受到损害。

与此同时，没有哪个垂直行业比其他垂直行业更有针对性。受害者包括大学、小型和大型企业、互联网服务提供商、加密货币交易商、Tor 出口节点、共享托管提供商和专用服务器提供商等。

2019 年底，一家大型且受欢迎的美国域名注册商和网络托管提供商的基础设施遭到破坏。总共约有 2,500 台物理服务器和 60,000 台虚拟服务器受到攻击者的攻击。这些服务器中的很大一部分（如果不是全部）由多个用户共享，以托管超过 150 万个帐户的网站。在另一起事件中，该托管提供商总共有 70,000 台服务器在 2023 年遭到 Ebury 的攻击。托管 Linux 内核源代码的 Kernel.org 也曾是 Ebury 的受害者。

“Ebury 对 Linux 安全社区构成了严重的威胁和挑战。没有简单的修复方法可以使 Ebury 失效，但可以应用一些缓解措施来最大程度地减少其传播和影响。需要认识到的一件事是，这种情况不仅仅发生在不太关心安全的组织或个人身上。许多非常精通技术的个人和大型组织都在受害者名单中。”Léveillé 总结道。

本文翻译自 [原文链接](https://www.helpnetsecurity.com/2024/05/16/ebury-botnet/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296592](/post/id/296592)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/05/16/ebury-botnet/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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