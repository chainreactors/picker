---
title: 3500 万台设备易受攻击：Matrix DDoS 活动凸显了日益增长的 IoT 威胁
url: https://www.anquanke.com/post/id/302249
source: 安全客-有思想的安全新媒体
date: 2024-11-29
fetch_date: 2025-10-06T19:14:47.142044
---

# 3500 万台设备易受攻击：Matrix DDoS 活动凸显了日益增长的 IoT 威胁

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

# 3500 万台设备易受攻击：Matrix DDoS 活动凸显了日益增长的 IoT 威胁

阅读量**53725**

发布时间 : 2024-11-28 14:13:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/35-million-devices-vulnerable-matrix-ddos-campaign-highlights-growing-iot-threat/>

译文仅供参考，具体内容表达以及含义原文为准。

![Matrix DDoS Campaign]()

Aqua Nautilus 研究人员发现了一个以 Matrix 为名的威胁行为者领导的大规模分布式拒绝服务 (DDoS) 活动。通过蜜罐活动发现的这一行动展示了 DDoS 僵尸网络策略令人担忧的演变，Matrix 利用可访问的工具和普遍存在的漏洞发动了大规模网络攻击。

Matrix 充分体现了即使只有极少技术专长的个人也能利用公开工具部署破坏性 DDoS 操作。正如 Aqua Nautilus 所强调的，“该活动展示了可获取的工具和基本技术知识如何使个人能够对众多漏洞实施广泛、多层面的攻击。”该活动主要针对物联网设备、路由器、电信设备和企业系统的漏洞，创建了一个能够对全球造成重大破坏的僵尸网络。

Matrix 采用了多种初始访问技术，包括：

1. **路由器漏洞：** 利用 CVE-2017-18368（命令注入）和 CVE-2021-20090 （Arcadyan 固件）等漏洞。
2. **物联网和 DVR 漏洞利用：** 利用 Hi3520 平台等设备的弱点。
3. **企业目标：** 利用 Apache Hadoop 的 YARN 和 HugeGraph 服务器中的漏洞渗透企业系统。
4. **凭证滥用：** 使用常见的默认凭据（如 admin:admin）进行暴力攻击。

然后将这些设备同化到僵尸网络中，显著扩大 DDoS 攻击的规模和威力。

Matrix 的运作得益于其复杂的工具库，尽管这些工具库被大量借用：

* **Mirai 变种：** 针对物联网设备实施大规模 DDoS 攻击。
* **PyBot 和 DiscordGo：** 基于 Python 的框架，用于僵尸网络管理和协调。
* **基于 Telegram 的销售：** 一个名为 Kraken Autobuy 的 Telegram 僵尸程序促进自动 DDoS 服务销售，提供针对第 4 层（传输层）和第 7 层（应用层）的攻击计划。

Aqua Nautilus 的研究人员注意到，尽管活动范围很广，但所使用的工具基本上都是开源的。研究人员说：“真正的技能在于有效整合和操作这些工具的能力，”他们强调了脚本小子利用强大资源所造成的日益严重的威胁。

![]()
其中一种 DDoS 工具的 ASCI 图像 | 图片： Aqua Nautilus

该活动主要集中在中国和日本等物联网丰富的地区，尽管其影响遍及全球。有趣的是，尽管疑似来自俄罗斯，但该活动并不以俄罗斯或乌克兰资产为目标，这表明金融动机大于政治议程。僵尸网络的潜在范围惊人；一项分析显示，有近 3500 万台联网设备可能成为攻击目标，如果只有一小部分被利用，僵尸网络的规模估计可达 170 万台设备。

这些攻击的后果不仅仅是直接的 DDoS 受害者。Aqua Nautilus 指出：”如果受影响的服务器是云供应商基础设施的一部分，它们可能会被服务提供商停用，从而导致受害者的业务中断。

Matrix DDoS 活动代表了网络威胁领域令人担忧的变化。通过利用基本漏洞和公开工具，Matrix 展示了大规模网络攻击的可及性在不断提高。随着威胁行为者不断创新并扩大其影响范围，企业和个人必须保持警惕，采取积极措施保护自己的系统不受损害。

本文翻译自securityonline [原文链接](https://securityonline.info/35-million-devices-vulnerable-matrix-ddos-campaign-highlights-growing-iot-threat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302249](/post/id/302249)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/35-million-devices-vulnerable-matrix-ddos-campaign-highlights-growing-iot-threat/)

如若转载,请注明出处： <https://securityonline.info/35-million-devices-vulnerable-matrix-ddos-campaign-highlights-growing-iot-threat/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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