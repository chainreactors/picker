---
title: 新的Gafgyt僵尸网络变种针对弱SSH密码进行GPU加密货币挖矿
url: https://www.anquanke.com/post/id/299211
source: 安全客-有思想的安全新媒体
date: 2024-08-17
fetch_date: 2025-10-06T18:02:16.476373
---

# 新的Gafgyt僵尸网络变种针对弱SSH密码进行GPU加密货币挖矿

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

# 新的Gafgyt僵尸网络变种针对弱SSH密码进行GPU加密货币挖矿

阅读量**43546**

发布时间 : 2024-08-16 14:40:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了 **Gafgyt** 僵尸网络的一种新变体，该僵尸网络针对具有弱 SSH 密码的机器，最终使用其 GPU 计算能力在受感染的实例上挖掘加密货币。

这表明“物联网僵尸网络的目标是在云原生环境中运行的更强大的服务器，”Aqua Security研究员Assaf Morag在周三的分析中表示。

自 2014 年以来，已知 Gafgyt（又名 BASHLITE、Lizkebab 和 Torlus）在野外活跃，有利用弱或默认凭据来控制路由器、摄像头和数字视频录像机 （DVR） 等设备的历史。它还能够利用 Dasan、华为、Realtek、SonicWall 和 Zyxel 设备中的已知安全漏洞。

受感染的设备被围困在一个僵尸网络中，该僵尸网络能够针对感兴趣的目标发起分布式拒绝服务 （DDoS） 攻击。有证据表明，Gafgyt 和 Necro 由一个名为 Keksec 的威胁组织运营，该组织也被追踪为 Kek Security 和 FreakOut。

像 Gafgyt 这样的物联网僵尸网络不断发展以添加新功能，2021 年检测到的变体使用 TOR 网络来掩盖恶意活动，并从泄露的 Mirai 源代码中借用一些模块。值得注意的是，Gafgyt 的源代码在 2015 年初就在网上泄露，进一步推动了新版本和改编版本的出现。

![Gafgyt Botnet Variant]( "Gafgyt Botnet Variant")

最新的攻击链涉及使用弱密码暴力破解 SSH 服务器，以部署下一阶段的有效载荷，以促进使用“systemd-net”的加密货币挖掘攻击，但在终止已经在受感染主机上运行的竞争恶意软件之前。

它还执行一个蠕虫模块，一个名为 ld-musl-x86 的基于 Go 的 SSH 扫描器，该模块负责扫描互联网上以查找安全性较差的服务器，并将恶意软件传播到其他系统，从而有效地扩大了僵尸网络的规模。这包括 SSH、Telnet 以及与游戏服务器和云环境（如 AWS、Azure 和 Hadoop）相关的凭据。

“正在使用的加密矿工是XMRig，一个门罗币加密货币矿工，”莫拉格说。“然而，在这种情况下，威胁行为者正在寻求使用 –opencl 和 –cuda 标志运行加密矿工，这些标志利用了 GPU 和 Nvidia GPU 的计算能力。”

“这一点，再加上威胁行为者的主要影响是加密挖矿而不是DDoS攻击这一事实，支持了我们的说法，即这种变体与以前的变体不同。它旨在针对具有强大 CPU 和 GPU 功能的云原生环境。

通过查询 Shodan 收集的数据显示，有超过 3000 万台可公开访问的 SSH 服务器，因此用户必须采取措施保护实例免受暴力攻击和可能的利用。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299211](/post/id/299211)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

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