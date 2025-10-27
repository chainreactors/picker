---
title: Vice Society 转向使用Inc勒索软件攻击医疗行业
url: https://www.anquanke.com/post/id/300233
source: 安全客-有思想的安全新媒体
date: 2024-09-21
fetch_date: 2025-10-06T18:24:53.475286
---

# Vice Society 转向使用Inc勒索软件攻击医疗行业

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

# Vice Society 转向使用Inc勒索软件攻击医疗行业

阅读量**128811**

发布时间 : 2024-09-20 14:34:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/vice-society-inc-ransomware-healthcare-attack>

译文仅供参考，具体内容表达以及含义原文为准。

Inc勒索软件正在兴起，其中一个知名的威胁行为者最近使用它来针对美国的医疗保健组织。

Vice Society（微软追踪其为Vanilla Tempest）自2022年7月以来一直活跃。在这段时间里，这个讲俄语的团伙利用了各种家族的勒索软件来辅助其双重勒索攻击，包括BlackCat、Hello Kitty、Quantum Locker、Rhysida、Zeppelin——包括他们自己的变种——以及以其自身命名的程序。

在X平台上的一系列帖子中，微软威胁情报中心(MSTIC)指出了该团伙最新的武器：Inc勒索软件。

MSTIC的高级威胁情报总监Jeremy Dallman表示：“Vanilla Tempest是我们跟踪的最活跃的勒索软件操作者之一。虽然我们已经看到他们针对医疗保健行业有一段时间了，但这里值得注意的变化是他们在利用更大的勒索软件即服务生态系统时使用了Inc勒索软件载荷。”

## Vice Society 进军医疗保健领域

Vice Society涉足多个行业，包括IT和制造业，但它最为人所知的是针对教育和医疗保健部门的活动。

在这方面，它与更广泛的威胁形势是一致的。根据Check Point Research的数据，医疗保健是勒索软件攻击者最常瞄准的行业。显然，其他类型的网络犯罪分子也喜欢这个行业，全球医疗保健机构平均每周遭受2,018次攻击，比去年增加了32%。

Check Point美洲区CISO Cindi Carter警告说，这是合乎逻辑的。除了受制于过时的传统技术和官僚体制之外，“医疗保健组织捕获、创建和分享的数据对于网络犯罪分子来说具有很高的价值。”她说，“你的医疗记录是你除了指纹之外最具标识性的数字信息。”

在最近利用医疗保健领域固有弱点的活动中，Vice Society获得了之前已被Gootloader后门加载器感染的受害者的初始访问权限。然后它部署了工具，包括Supper后门、AnyDesk的远程监控和管理(RMM)解决方案以及MEGA的数据同步工具，后两者都是合法的商业产品。该团体使用远程桌面协议(RDP)在网络中横向移动，并滥用Windows管理规范(WMI)提供程序主机来投放Inc勒索软件。

## Inc 勒索软件的崛起

自去年夏天开始活跃以来，Inc勒索软件即服务(RaaS)运营因其对特别大型组织的入侵而获得了大量头条新闻——其中包括施乐公司和苏格兰国家医疗服务系统(NHS)等。GuidePoint Security的威胁情报顾问Jason Baker表示，它的运作模式符合其野心的范围。

“特别是Inc联盟成员之所以脱颖而出的原因在于，他们在谈判过程中有一种非常结构化的工作方式。没有即兴发挥。没有随口说出的话。刺激和威胁保持在相对最低的程度，”他从第一手经验中回忆道。

“这就像是有人抢劫银行和有人在小巷里抢劫的区别。你可以看出有人对[攻击]进行了思考并且知道自己在做什么，”他说。

正如Dark Reading上个月报道的那样，Inc的恶意软件泄露了关于其数据加密性质和成功的信息。尽管这可能会给防御者在补救和潜在的与联盟成员的谈判中带来优势，Baker警告说现实更为复杂，尤其是在医疗保健方面。

他指出：“如果一个组织知道它可以恢复，并且不需要解密器，那么这会大大减少他们觉得需要支付赎金的感觉。但问题在于现代的双重勒索，尤其是当涉及到敏感的个人健康信息(PHI)或敏感的知识产权时。双重勒索方法之所以能够长期存在是有原因的：它确实在某种程度上克服了即使能够恢复的能力。”

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/vice-society-inc-ransomware-healthcare-attack)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300233](/post/id/300233)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/vice-society-inc-ransomware-healthcare-attack)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/vice-society-inc-ransomware-healthcare-attack>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Vice Society 进军医疗保健领域](#h2-0)
* [Inc 勒索软件的崛起](#h2-1)

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