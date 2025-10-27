---
title: 新的网络威胁使用FrigidStealer恶意软件瞄准MacOS
url: https://www.anquanke.com/post/id/304723
source: 安全客-有思想的安全新媒体
date: 2025-02-26
fetch_date: 2025-10-06T20:32:40.123557
---

# 新的网络威胁使用FrigidStealer恶意软件瞄准MacOS

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

# 新的网络威胁使用FrigidStealer恶意软件瞄准MacOS

阅读量**84647**

发布时间 : 2025-02-25 10:29:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Melania Watson，文章来源：securitybrief

原文地址：<https://securitybrief.asia/story/new-cyber-threats-target-macos-with-frigidstealer-malware>

译文仅供参考，具体内容表达以及含义原文为准。

![Story image]()

Proofpoint已识别出两个新的网络犯罪威胁行为者 ——TA2726 和 TA2727，他们参与了Web注入攻击活动，同时还发现了针对MacOS用户的新型恶意软件。

恶意网站注入的形势特点是，多个威胁行为者采用恶意软件传播方法，这些方法通常涉及三个要素：提供给网站访问者的恶意 JavaScript 脚本、一个决定传播何种负载的流量分发服务，以及由该脚本下载的最终负载。

尽管威胁行为者 TA569 曾发起过一些引人注目的Web注入攻击活动，但新的行为者已经出现，这使得分析师追踪此类攻击的工作变得更加复杂。

从 2023 年开始，Proofpoint观察到多个威胁行为者采用了类似的Web注入和流量重定向技术。这些模仿者使用相似方法的出现，加剧了区分他们的难度。Proofpoint发布这份报告，旨在厘清其中涉及的威胁行为者。

TA2726 和 TA2727 已被确定为新的流量贩卖者和恶意软件分发者，他们专门在以受攻击网站为特征的网络攻击链中活动。

这些攻击活动与基于电子邮件的威胁不同，后者与合法但已遭入侵的网站相关联。

已发现 TA2727 与一种名为 FrigidStealer的新型信息窃取恶意软件的传播有关，该恶意软件针对苹果电脑，同时 TA2727 还涉及传播现有的针对 Windows 和Android 系统的恶意软件。

Proofpoint也在重新评估过去被认为是 TA569 实施的活动，并高度确信 TA2726 充当着 TA569 和 TA2727 的流量分发服务角色。

据悉，TA2726 运营着一个流量分发服务（TDS），为多个行为者传播恶意软件提供便利，并且可能在网络犯罪论坛上兜售流量，不过这一点尚未得到高度确信的证实。TA2726 至少从 2022 年 9 月起就开始活跃，它不开展电子邮件攻击活动，任何电子邮件活动都是网站共享带来的附带影响。

该行为者主要针对北美地区，将流量重定向到 TA569，而将其他地区的流量导向 TA2727，以传播包括Lumma Stealer、DeerStealer、FrigidStealer或 Marcher等各种恶意软件。

TA2726 所使用的基础设施，比如使用 Keitaro 系统以及特定的域名和 IP 地址模式，能够清晰地识别出其活动。

追溯分析表明，先前以SocGholish之名报告的流量分发服务活动可以追溯到 TA2726。

TA2727 是一个受经济利益驱动的组织，它与其他以盈利为目的的行为者合作，据信会在在线论坛上购买流量来传播恶意软件。

这个行为者于 2025 年 1 月首次被认定，当时的一场攻击活动最初被认为与 TA569 有关。

在这场攻击活动中，电子邮件中的网址将用户引导至已被注入恶意 JavaScript 的受攻击网站。攻击者使用了基于位置的重定向技术来提供特定的负载。在北美地区，用户遇到的是 SocGholish  注入，而在法国和英国，发现了一种独特的虚假更新负载链。

在欧洲的这场攻击活动中，攻击者针对使用Microsoft Edge或Google Chrome 的 Windows 设备，将其重定向到虚假的更新网站，通过一个被植入木马的 IFILOader 安装  Lumma Stealer 恶意软件。

这场攻击活动的一个独特分支使用 Marcher 木马攻击安卓设备，Marcher 自 2013 年起就是已知的威胁。

在 2025 年 1 月底的进一步分析中，重点关注到MacOS用户正成为新型恶意软件 FrigidStealer 的攻击目标。

用户访问受攻击的网站时，会被重定向到虚假的更新页面，如果与之交互，就会安装该恶意软件。Proofpoint的研究人员已提供了技术细节，阐明了此次攻击是如何绕过MacOS的安全功能来安装FrigidStealer 的。

Web注入威胁具有动态变化和不断演变的特点，这就要求安全团队保持警惕。

最佳实践包括制定网络检测规则、对用户进行培训，以及使用浏览器隔离工具。

鼓励各组织实施全面的防御措施和用户培训计划，以有效降低这些威胁带来的风险。

本文翻译自securitybrief [原文链接](https://securitybrief.asia/story/new-cyber-threats-target-macos-with-frigidstealer-malware)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304723](/post/id/304723)

安全KER - 有思想的安全新媒体

本文转载自: [securitybrief](https://securitybrief.asia/story/new-cyber-threats-target-macos-with-frigidstealer-malware)

如若转载,请注明出处： <https://securitybrief.asia/story/new-cyber-threats-target-macos-with-frigidstealer-malware>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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