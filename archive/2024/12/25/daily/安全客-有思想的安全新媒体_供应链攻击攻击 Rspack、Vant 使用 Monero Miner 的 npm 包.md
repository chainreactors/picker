---
title: 供应链攻击攻击 Rspack、Vant 使用 Monero Miner 的 npm 包
url: https://www.anquanke.com/post/id/302951
source: 安全客-有思想的安全新媒体
date: 2024-12-25
fetch_date: 2025-10-06T19:34:22.452831
---

# 供应链攻击攻击 Rspack、Vant 使用 Monero Miner 的 npm 包

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

# 供应链攻击攻击 Rspack、Vant 使用 Monero Miner 的 npm 包

阅读量**65388**

发布时间 : 2024-12-24 10:21:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/supply-chain-attack-rspack-vant-npm-monero-miner/>

译文仅供参考，具体内容表达以及含义原文为准。

**摘要要点**

* **受损的 npm 软件包：** 2024 年 12 月 20 日，攻击者使用劫持的 npm 令牌入侵了流行的 npm 软件包 @rspack/core、@rspack/cli 和 “vant”，并在其更新中注入了恶意代码。
* **部署了 Monero 矿工：** 隐藏在混淆脚本中的恶意代码部署了 XMRig Monero 加密货币矿机，连接到外部服务器并为攻击者挖矿。
* **自动检测：** Sonatype 的恶意软件检测系统迅速识别并阻止了恶意版本，通过 Nexus Repository Firewall 保护了用户。
* **发布补丁：** Rspack 和 Vant 通过发布干净的更新（Rspack v1.1.8 和 Vant v4.9.15）和实施增强的安全措施来解决漏洞问题。
* **开源风险凸显：** Sonatype 报告称，98.5% 的开源恶意软件以 npmjs.com 为目标，强调了定期更新、打补丁和适当的安全解决方案的必要性。

软件供应链管理平台 Sonatype 与 Hackread.com 分享的最新研究报告显示，2024 年 12 月 20 日，流行的 npm 软件包 @rspack/core 和 @rspack/cli 因攻击者访问了被泄露的 npm 令牌而遭到入侵。

根据 Sonatype 的博文，这些攻击者随后发布了这些软件包的恶意版本（1.1.7）。Sonatype 的自动恶意软件检测系统迅速捕获了这些恶意版本，并为使用 Nexus Repository Firewall 的用户拦截了它们。

除这些软件包外，Sonatype 的深度二进制分析技术还发现了另一个被入侵的 npm 软件包 “vant”。vant “的几个较新版本显示出了被入侵的迹象，随后被阻止。研究人员怀疑，同一天发生的这两起攻击都是一个共同的威胁行为体所为。

**通过被破坏的 npm 令牌进行劫持**

Sonatype 的自动恶意软件检测系统在 @rspack/core 和 @rspack/cli 的恶意版本（1.1.7）发布到 npmjs.com 注册表后不久就发现了它们。Rspack 是一个用 Rust 编写的 JavaScript 捆绑程序，其 npm 软件包被广泛使用。@rspack/core 每周的下载量接近 394,000 次，@rspack/cli 每周的下载量超过 145,000 次。

进一步探测发现，这些软件包的恶意版本在 dist/utils/config.js 文件中包含大量混淆代码。这些代码没有明显的用途，在以前的版本中也不存在。

**代码运行 Monero 加密矿机**

被混淆的代码在目标系统上部署了已知的 Monero 矿工 “XMRig”。该矿机为攻击者挖掘加密货币。代码还试图连接到 hxxps://80.78.2872/tokens 地址。代码中出现的 Monero 地址可能会收集挖出的 XMR。 不过，在编写本报告时，与该地址相关的活动并不多。

**Vant 软件包也受到攻击**

Sonatype 研究人员 Jeff Thornhill 和 Adam Reynolds 在调查中发现了多个 “vant ”软件包的受损版本。值得注意的是，Vant 是一种流行的轻量级 Vue UI 库，适用于移动网络应用程序，在 npmjs.com 上每周大约有 46,000 次下载。vant “的受损版本包括 2.13.3、2.13.4、2.13.5、3.6.13、3.6.14、3.6.15、4.9.11、4.9.12、4.9.13 和 4.9.14。

![Supply Chain Attack Hits Rspack, Vant npm Packages with Monero Miner]()
通过 Sonatype

**补丁可用**

Rspack 和 Vant 都迅速解决了漏洞问题并发布了补丁。Rspack 发布了不含恶意代码的 1.1.8 版本。Vant 发布了 4.9.15 版更新，也解决了安全问题。

两家公司都就此次漏洞发表了声明。Rspack Project 对此次事件造成的风险表示歉意，承诺 “将实施更严格的令牌管理协议，并加强我们的安全审查流程”。相反，Vant 确认他们 “已采取措施进行修复，并重新发布了最新版本”。

Sonatype 的《2024 年开源恶意软件报告》显示，98.5% 的开源恶意软件发布在 npmjs.com 注册表上，使其成为攻击者的热门目标。为了保证安全，请及时更新软件，打上 Rspack 和 Vant 的补丁，并使用可靠的安全解决方案来检测开源软件包中的恶意软件。

本文翻译自hackread [原文链接](https://hackread.com/supply-chain-attack-rspack-vant-npm-monero-miner/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302951](/post/id/302951)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/supply-chain-attack-rspack-vant-npm-monero-miner/)

如若转载,请注明出处： <https://hackread.com/supply-chain-attack-rspack-vant-npm-monero-miner/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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