---
title: Diicot 威胁组织利用高级恶意软件攻击 Linux
url: https://www.anquanke.com/post/id/302932
source: 安全客-有思想的安全新媒体
date: 2024-12-24
fetch_date: 2025-10-06T19:36:39.770459
---

# Diicot 威胁组织利用高级恶意软件攻击 Linux

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

# Diicot 威胁组织利用高级恶意软件攻击 Linux

阅读量**102895**

|评论**1**

发布时间 : 2024-12-23 11:29:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/diicot-threat-group-targets-linux-with-advanced-malware-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

Wiz Threat Research 揭示了一个由讲罗马尼亚语的威胁组织 Diicot（又称 Mexals）策划的新恶意软件活动。该活动以 Linux 环境为目标，采用了先进的恶意软件技术，标志着其能力显著升级。该组织一直利用 Linux 系统进行加密劫持，使用 XMRig 等工具和复杂的自传播机制。

据 Wiz Research 称，与早期迭代版本相比，更新后的恶意软件显示出惊人的复杂程度，凸显了攻击者适应和完善其战术的能力。报告指出：“我们分析的恶意软件包括一些显著的改进，反映了更高的复杂程度。”主要的进步包括引入了新的指挥控制（C2）基础设施，从基于 Discord 的 C2 过渡到 HTTP，以及采用 Zephyr 协议和 Monero 挖矿。

![Diicot threat group]()
Diicot 图表 | 来源：Wiz Research Wiz Research

该恶意软件还改进了混淆技术。例如，修改后的 UPX 标头现在包括损坏的校验和，使标准解包工具失效。这些变化表明，该恶意软件正在努力绕过现代安全措施，阻挠自动检测。

该活动的一个突出特点是它能够根据环境调整自己的行为。在云环境中，恶意软件会优先向其他主机传播，而在传统环境中，它会部署加密有效载荷。报告解释说，“云检测逻辑”“基于远程机器的 Linux 发行版和版本”，显示了该组织对目标的细致关注。

调查中发现的有效载荷包括：

* **Brute-Spreader**： 在网络中传播并保持持久性的主要有效载荷。
* **反向外壳 (client.go)**： 允许攻击者完全远程控制被入侵的机器。
* **SSH 标记扫描器**： 识别弱 SSH 凭据以获得初始访问权限。

该活动对运行 OpenSSH 的 Linux 系统构成重大风险。薄弱的凭证和错误配置的安全设置很容易成为这种高级恶意软件的入口点。Wiz 研究人员强调：“如果你的系统依赖 SSH 且没有适当的安全保护，它们很容易成为攻击目标。”

加密劫持仍然是 Diicot 行动的核心动机。攻击者从 Monero 挖矿中赚取了超过 16,000 美元，还从 Zephyr 协议中赚取了更多难以追踪的收入。除了经济损失，企业还面临数据外渗、系统受损和潜在运营中断的风险。

随着 Diicot 集团的不断发展，防御策略也必须与时俱进。Wiz Research 建议加强 SSH 配置，强制执行强密码，并部署能够识别混淆有效载荷的高级检测机制。

本文翻译自securityonline [原文链接](https://securityonline.info/diicot-threat-group-targets-linux-with-advanced-malware-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302932](/post/id/302932)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/diicot-threat-group-targets-linux-with-advanced-malware-campaign/)

如若转载,请注明出处： <https://securityonline.info/diicot-threat-group-targets-linux-with-advanced-malware-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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