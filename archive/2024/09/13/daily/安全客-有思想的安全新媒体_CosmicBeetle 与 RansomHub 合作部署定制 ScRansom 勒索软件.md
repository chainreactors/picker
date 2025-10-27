---
title: CosmicBeetle 与 RansomHub 合作部署定制 ScRansom 勒索软件
url: https://www.anquanke.com/post/id/300016
source: 安全客-有思想的安全新媒体
date: 2024-09-13
fetch_date: 2025-10-06T18:20:02.616226
---

# CosmicBeetle 与 RansomHub 合作部署定制 ScRansom 勒索软件

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

# CosmicBeetle 与 RansomHub 合作部署定制 ScRansom 勒索软件

阅读量**101511**

发布时间 : 2024-09-12 14:55:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html>

译文仅供参考，具体内容表达以及含义原文为准。

被称为 CosmicBeetle 的威胁行为者在针对欧洲、亚洲、非洲和南美洲的中小型企业 （SMB） 的攻击中首次推出了一种名为 ScRansom 的新自定义勒索软件菌株，同时也可能是 RansomHub 的附属公司。

“CosmicBeetle 用 ScRansom 取代了之前部署的勒索软件 Scarab，该勒索软件正在不断改进，”ESET 研究员 Jakub Souček 在今天发布的一项新分析中说。“虽然不是一流的，但威胁行为者能够破坏有趣的目标。”

ScRansom 攻击的目标涵盖制造业、制药、法律、教育、医疗保健、技术、酒店、休闲、金融服务和地区政府部门。

CosmicBeetle 以名为 Spacecolon 的恶意工具集而闻名，该工具集之前被确定用于向全球受害者组织传递 Scarab 勒索软件。

该对手也被称为 NONAME，早在 2023 年 11 月就曾尝试使用泄露的 LockBit 构建器，试图在其赎金记录和泄漏站点中冒充臭名昭著的勒索软件团伙。

目前尚不清楚谁是攻击的幕后黑手或他们来自哪里，尽管早期的假设暗示他们可能来自土耳其，因为另一个名为 ScHackTool 的工具中存在自定义加密方案。但是，ESET 怀疑该归因不再成立。

“ScHackTool 的加密方案用于合法的 Disk Monitor Gadget，”Souček 指出。“这个算法很可能是由 VOVSOFT [该工具背后的土耳其软件公司] [从 Stack Overflow 线程] 改编而来的，几年后，CosmicBeetle 偶然发现了它并将其用于 ScHackTool。”

已观察到攻击链利用暴力攻击和已知的安全漏洞（CVE-2017-0144、CVE-2020-1472、CVE-2021-42278、CVE-2021-42287、CVE-2022-42475 和 CVE-2023-27532）渗透目标环境。

入侵还涉及使用 Reaper、Darkside 和 RealBlindingEDR 等各种工具来终止与安全相关的进程，以在部署基于 Delphi 的 ScRansom 勒索软件之前避开检测，该勒索软件支持部分加密以加快进程和“擦除”模式，通过用常量值覆盖文件来使文件无法恢复。

与 RansomHub 的联系源于这样一个事实，即斯洛伐克网络安全公司在一周内发现 ScRansom 和 RansomHub 有效载荷部署在同一台机器上。

“可能是由于从头开始编写自定义勒索软件带来的障碍，CosmicBeetle 试图窃取 LockBit 的声誉，可能是为了掩盖底层勒索软件中的问题，从而增加受害者付款的机会，”Souček 说。

## Cicada3301 发布更新版本

自 2024 年 7 月以来，已观察到与 Cicada3301 勒索软件（又名 Repellent Scorpius）相关的威胁行为者使用更新版本的加密器。

“威胁作者添加了一个新的命令行参数 –no-note，”Palo Alto Networks Unit 42 在与 The Hacker News 分享的一份报告中说。“当调用此参数时，加密器不会将赎金记录写入系统。”

另一个重要的修改是二进制文件中没有硬编码的用户名或密码，尽管它仍然保留了使用这些凭据（如果存在）执行 PsExec 的能力，这是 Morphisec 最近强调的一种技术。

有趣的是，这家网络安全供应商表示，它观察到有迹象表明，该组织拥有从该组织以 Cicada3301 品牌运营之前的旧入侵事件中获得的数据。

这增加了威胁行为者可能在不同的勒索软件品牌下运作，或从其他勒索软件组织购买数据的可能性。话虽如此，Unit 42 指出，它发现与 2022 年 3 月部署 BlackCat 勒索软件的附属公司进行的另一次攻击有一些重叠。

## BURNTCIGAR 成为 EDR 雨刷器

这些发现还遵循了多个勒索软件团伙使用的内核模式签名 Windows 驱动程序的演变，以关闭端点检测和响应 （EDR） 软件，该软件允许它充当擦除器来删除与这些解决方案相关的关键组件，而不是终止它们。

有问题的恶意软件是 POORTRY，它通过名为 STONESTOP 的加载程序提供，以编排自带易受攻击的驱动程序 （BYOVD） 攻击，从而有效地绕过驱动程序签名强制保护措施。Trend Micro 于 2023 年 5 月首次注意到它能够“强制删除”磁盘上的文件。

POORTRY 早在 2021 年就被检测到，也被称为 BURNTCIGAR，多年来已被多个勒索软件团伙使用，包括 CUBA、BlackCat、Medusa、LockBit 和 RansomHub。

“Stonestop 可执行文件和 Poortry 驱动程序都经过了大量打包和混淆处理，”Sophos 在最近的一份报告中说。“这个加载程序被一个名为 ASMGuard 的闭源打包程序混淆了，可在 GitHub 上找到。”

POORTRY “专注于通过一系列不同的技术禁用 EDR 产品，例如删除或修改内核通知例程。EDR 杀手旨在通过从磁盘上擦除关键文件来终止与安全相关的进程并使 EDR 代理变得无用。

流氓驱动程序利用该公司所描述的“几乎无限供应的被盗或不当使用的代码签名证书”来绕过 Microsoft 的驱动程序签名验证保护。

RansomHub 使用 POORTRY 的改进版本值得注意，因为今年还观察到勒索软件团队使用另一种名为 EDRKillShifter 的 EDR 杀手工具。

这还不是全部。还检测到勒索软件团伙利用卡巴斯基提供的名为 TDSSKiller 的合法工具解除目标系统上的 EDR 服务，这表明威胁行为者正在其攻击中加入多个具有类似功能的程序。

“重要的是要认识到，威胁行为者一直在尝试不同的方法来禁用 EDR 产品——至少自 2022 年以来我们一直在观察这一趋势，”Sophos 告诉 The Hacker News。“这种实验可能涉及各种策略，例如利用易受攻击的驱动程序或使用无意泄露或通过非法手段获得的证书。”

“虽然这些活动似乎显着增加，但更准确地说，这是一个持续过程的一部分，而不是突然增加。”

“RansomHub 等组织使用不同的 EDR 杀手工具，例如 EDRKillShifter，可能反映了这种正在进行的实验。也可能涉及不同的附属公司，这可以解释使用各种方法的原因，尽管没有具体信息，我们不想在这一点上进行太多推测。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300016](/post/id/300016)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Cicada3301 发布更新版本](#h2-0)
* [BURNTCIGAR 成为 EDR 雨刷器](#h2-1)

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