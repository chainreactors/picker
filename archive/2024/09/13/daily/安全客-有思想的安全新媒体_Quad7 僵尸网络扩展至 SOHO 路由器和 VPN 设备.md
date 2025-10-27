---
title: Quad7 僵尸网络扩展至 SOHO 路由器和 VPN 设备
url: https://www.anquanke.com/post/id/300037
source: 安全客-有思想的安全新媒体
date: 2024-09-13
fetch_date: 2025-10-06T18:20:09.224920
---

# Quad7 僵尸网络扩展至 SOHO 路由器和 VPN 设备

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

# Quad7 僵尸网络扩展至 SOHO 路由器和 VPN 设备

阅读量**72297**

发布时间 : 2024-09-12 14:50:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html>

译文仅供参考，具体内容表达以及含义原文为准。

神秘的 Quad7 僵尸网络的运营商正在积极发展，通过利用已知和未知的安全漏洞组合来破坏多个品牌的 SOHO 路由器和 VPN 设备。

根据法国网络安全公司 Sekoia 的一份新报告，目标包括来自 TP-LINK、Zyxel、Asus、Axentra、D-Link 和 NETGEAR 的设备。

研究人员 Felix Aimé、Pierre-Antoine D. 和 Charles M. 说：“Quad7 僵尸网络运营商似乎正在发展他们的工具集，引入新的后门并探索新的协议，目的是增强隐身性并规避其操作中继盒 （ORB） 的跟踪能力。

Quad7，也称为 7777，于 2023 年 10 月由独立研究员 Gi7w0rm 首次公开记录，突显了该活动集群将 TP-Link 路由器和大华数字录像机 （DVR） 诱捕到僵尸网络中的模式。

该僵尸网络因在受感染设备上打开 TCP 端口 7777 而得名，据观察，该僵尸网络会暴力破解 Microsoft 3665 和 Azure 实例。

“僵尸网络似乎还感染了 MVPower、Zyxel NAS 和 GitLab 等其他系统，尽管数量非常少，”VulnCheck 的 Jacob Baines 在今年 1 月早些时候指出。“僵尸网络不只是在端口 7777 上启动服务。它还会在端口 11228 上启动 SOCKS5 服务器。

Sekoia 和 Cymru 团队在过去几个月的后续分析发现，该僵尸网络不仅破坏了保加利亚、俄罗斯、美国和乌克兰的 TP-Link 路由器，而且还扩展到了打开了 TCP 端口 63256 和 63260 的华硕路由器。

最新调查结果显示，该僵尸网络由三个额外的集群组成 –

* xlogin（又名 7777 僵尸网络）- 由受感染的 TP-Link 路由器组成的僵尸网络，这些路由器同时打开了 TCP 端口 7777 和 11288
* alogin（又名 63256 僵尸网络）- 由受感染的华硕路由器组成的僵尸网络，这些路由器同时打开了 TCP 端口 63256 和 63260
* rlogin – 由受感染的 Ruckus Wireless 设备组成的僵尸网络，这些设备打开了 TCP 端口 63210
* axlogin – 能够以 Axentra NAS 设备为目标的僵尸网络（尚未在野外检测到）
* zylogin – 由打开了 TCP 端口 3256 的受感染 Zyxel VPN 设备组成的僵尸网络

Sekoia 告诉 The Hacker News，感染人数最多的国家是保加利亚（1,093 人）、美国（733 人）和乌克兰（697 人）。

作为战术演变的进一步迹象，威胁行为者现在利用一个名为 UPDTAE 的新后门，该后门建立了基于 HTTP 的反向 shell，以在受感染设备上建立远程控制并执行从命令和控制 （C2） 服务器发送的命令。

目前尚不清楚该僵尸网络的确切目的或幕后黑手，但该公司表示，该活动很可能是中国政府支持的威胁行为者所为。

“关于 7777 [僵尸网络]，我们只看到了针对 Microsoft 365 帐户的暴力破解尝试，”Aimé 告诉该出版物。“对于其他僵尸网络，我们仍然不知道它们是如何使用的。”

“然而，在与其他研究人员交流和新发现之后，我们几乎可以肯定，运营商更有可能是 CN 国家资助的，而不是简单的网络犯罪分子进行 [商业电子邮件泄露]。”

“我们看到威胁行为者试图通过在受感染的边缘设备上使用新的恶意软件来变得更加隐蔽。此举背后的主要目的是防止跟踪附属僵尸网络。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300037](/post/id/300037)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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