---
title: Cicada3301 勒索软件声称攻击了法国标致汽车经销商
url: https://www.anquanke.com/post/id/302764
source: 安全客-有思想的安全新媒体
date: 2024-12-18
fetch_date: 2025-10-06T19:33:13.017170
---

# Cicada3301 勒索软件声称攻击了法国标致汽车经销商

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

# Cicada3301 勒索软件声称攻击了法国标致汽车经销商

阅读量**60521**

|评论**1**

发布时间 : 2024-12-17 11:28:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/cicada3301-ransomware-french-peugeot-dealership/>

译文仅供参考，具体内容表达以及含义原文为准。

**摘要**

* Cicada3301 勒索软件组织声称已入侵标致特许经营公司，窃取了 35GB 的敏感数据。
* 该组织采用 “勒索软件即服务”（RaaS）模式，收取 20% 的佣金。
* 该勒索软件于 2024 年 6 月首次被发现，主要针对 Windows 和 Linux/ESXi 系统。
* Cicada3301 与 BlackCat 有相似之处，使用 ChaCha20 加密和类似的策略。
* 泄露的数据包括发票、护照副本和内部通信。

Cicada3301 是一个勒索软件组织，它声称对针对 Concession Peugeot（concessions.peugeot.fr）的数据泄露事件负责，Concession Peugeot 是法国一家著名的汽车经销商，与标致品牌有关联。该组织声称已经窃取了 35GB 的敏感数据，这标志着其侵略性网络活动的继续。

![]()
cicada3301勒索软件暗网泄露网站截图（截图：Hackread.com）

该组织于上周末（2024 年 12 月 15 日，周日）在其官方暗网泄漏网站上宣布了这一所谓的漏洞。值得注意的是，Cicada3301 这个名字在 2010 年代初曾与密码谜题联系在一起，后来被以 “勒索软件即服务”（RaaS）模式运作的勒索软件组织所采用。

这种模式使关联公司能够通过租用勒索软件基础设施并与运营商分成来实施攻击。Check Point 在 2024 年 9 月的报告中还提到了 Cicada3301，该组织在一个俄语地下论坛上发布了一则广告，提供勒索软件即服务（ransomware-as-a-service）。该组织要求从成功的攻击中收取 20% 的佣金，甚至还为合作伙伴之间的纠纷提供谈判机制。

网络安全公司 Truesec 于 2024 年 6 月首次发现了 Cicada3301 勒索软件组织。该勒索软件使用 Rust 语言编写，可同时针对 Windows 和 Linux/ESXi 系统，展示了其跨平台能力。

Cicada3301 与 ALPHV/BlackCat 勒索软件有明显的相似之处，包括使用 ChaCha20 加密、关闭虚拟机的相同命令以及为加密提供图形输出的 -ui 命令。两组勒索软件还共享类似的文件命名模式和用于解密赎金票据的关键参数。这些重叠表明它们之间有共同的联系，或者采用了成熟的技术来最大限度地提高效率和影响。

对标致特许经营店的攻击符合 Cicada3301 的战略，即针对高价值组织实施攻击，以最大限度地扩大影响。35GB 的数据被盗尤其令人担忧，因为 Hackread.com 查看的泄露文件截图显示了官方和内部通信、发票、护照副本甚至食谱。

![]()
cicada3301勒索软件暗网泄露网站截图（截图：Hackread.com）

**编者注**

事实上，标致特许经营公司在官方子域名 concessions.peugeot.fr 下运营，这与标致这个大品牌有更紧密的联系。像标致这样的大公司通常会让其授权经销商使用子域名，以保持一致的在线形象，使客户更容易信任他们的服务。

然而，这种设置意味着对经销商的攻击很容易看起来像对主公司的攻击。虽然这次漏洞只针对经销商，但使用标致的域名可能会导致混乱，并引发对整个品牌安全性的质疑。

本文翻译自hackread [原文链接](https://hackread.com/cicada3301-ransomware-french-peugeot-dealership/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302764](/post/id/302764)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/cicada3301-ransomware-french-peugeot-dealership/)

如若转载,请注明出处： <https://hackread.com/cicada3301-ransomware-french-peugeot-dealership/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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