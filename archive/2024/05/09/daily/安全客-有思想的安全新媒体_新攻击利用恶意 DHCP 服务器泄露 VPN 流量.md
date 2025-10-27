---
title: 新攻击利用恶意 DHCP 服务器泄露 VPN 流量
url: https://www.anquanke.com/post/id/296273
source: 安全客-有思想的安全新媒体
date: 2024-05-09
fetch_date: 2025-10-06T17:13:49.789941
---

# 新攻击利用恶意 DHCP 服务器泄露 VPN 流量

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

# 新攻击利用恶意 DHCP 服务器泄露 VPN 流量

阅读量**71087**

发布时间 : 2024-05-08 11:02:25

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.bleepingcomputer.com/news/security/new-tunnelvision-attack-leaks-vpn-traffic-using-rogue-dhcp-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为“TunnelVision”的新攻击可以将流量路由到 VPN 加密隧道之外，从而使攻击者能够窥探未加密的流量，同时保持安全 VPN 连接的外观。

攻击者设置一个恶意 DHCP 服务器来更改路由表，以便所有 VPN 流量直接发送到本地网络或恶意网关，而不会进入加密的 VPN 隧道。

报告中写道：“我们的技术是在与目标 VPN 用户相同的网络上运行 DHCP 服务器，并将我们的 DHCP 配置设置为将自身用作网关。”

在 Linux 上使用网络命名空间将网络接口和路由表与系统的其他部分隔离，防止恶意 DHCP 配置影响 VPN 流量。

配置 VPN 客户端以拒绝所有不使用 VPN 接口的入站和出站流量。

至于 VPN 提供商，我们鼓励他们增强客户端软件以实施自己的 DHCP 处理程序或集成额外的安全检查，以阻止应用有风险的 DHCP 配置。

本文翻译自 [原文链接](https://www.bleepingcomputer.com/news/security/new-tunnelvision-attack-leaks-vpn-traffic-using-rogue-dhcp-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296273](/post/id/296273)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-tunnelvision-attack-leaks-vpn-traffic-using-rogue-dhcp-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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