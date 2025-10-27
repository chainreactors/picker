---
title: FiberGateway路由器遭黑客攻击：葡萄牙160万户房屋面临风险
url: https://www.anquanke.com/post/id/308048
source: 安全客-有思想的安全新媒体
date: 2025-06-04
fetch_date: 2025-10-06T22:50:42.958939
---

# FiberGateway路由器遭黑客攻击：葡萄牙160万户房屋面临风险

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

# FiberGateway路由器遭黑客攻击：葡萄牙160万户房屋面临风险

阅读量**50839**

发布时间 : 2025-06-03 14:50:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/fibergateway-router-hacked-portugals-1-6m-homes-at-risk/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究员 João Domingos 发布了影响 FiberGateway GR241AG 路由器的完整漏洞利用链的全面细分，该路由器在葡萄牙有超过 160 万个家庭使用。最初是个人 DNS 配置挫败感，导致 root 访问、通过公共 WiFi 远程执行代码，并最终导致设备完全受损。

Domingos 的旅程始于 2020 年，目标很简单：配置 Pi-hole 来过滤 DNS 流量。但是 Meo 提供的路由器锁定了 DNS 设置。他没有接受失败或购买新硬件，而是开始了一场黑客冒险之旅：以 10 欧元的价格购买一台二手GR241AG，将其拆解，并最终通过 UART 接口实现 root 访问。

在这项研究中最具电影感的时刻之一，Domingos 描述了附近硬盘驱动器的振动如何在启动过程中无意中诱导故障注入，从而将设备放入 root shell：

> “*我正在从路由器附近的 HDD 磁盘恢复文件。看来是 HDD 的震动起到了某种故障注入的作用……如果在启动期间发生这种情况，则会发生分段错误，并且启动进程将下降到根 shell。*

他使用 USB 驱动器转储了路由器的固件，并在一个库中发现了明文管理员凭据。这授予了对具有新功能（固件更新、DNS 修改和流量监控）的受限 shell 的访问权限，即使对于面向公众的 MEO WiFi 用户也是如此。

在 tcpdump 实用程序中发现参数注入漏洞后，我们取得了突破。通过巧妙地使用 -z 和 -G 标志，Domingos 构建了一个漏洞利用链，允许在没有物理访问的情况下远程执行代码 – 完全通过网络。

也许最令人担忧的是最后一步：通过 MEO WiFi 实现完全 RCE，MEO WiFi 是 Meo 默认启用的公共网络，横跨葡萄牙。

通过利用 IPv6 的邻居发现协议 （NDP），Domingos 能够识别路由器的内部 IP 地址，即使每次重启时该地址都会发生变化。然后，使用早期的 tcpdump 注入，他在路由器中启动了一个反向 shell：

“*完整的漏洞利用链将包括以下内容：连接到 MEO WiFi 网络，通过发送 ICMPv6 数据包来识别 IPv6 地址，通过 SSH 连接到路由器，然后利用 tcpdump 获得反向 shell*。”

他甚至使用 Python 脚本自动执行该过程 — 一个用于完全利用，另一个用于从私有接口转储 WPA2 密钥。

此漏洞的影响是巨大的：

* + DNS 劫持
  + 提取电话记录

* + 网络监控
  + 本地网络设备访问
  + WPA2 密钥盗窃

* 拒绝服务

所有这一切，都在任何公共 MEO WiFi 信号的范围内。

Domingos 负责任地向葡萄牙的 Centro Nacional de Cibersegurança （CNCS） 披露了调查结果，后者联系了 Meo 的 CERT 团队。在一周内，通过 MEO WiFi 的远程 RCE 得到了缓解。在接下来的几个月里，其他漏洞得到了修补，但访问权限被撤销，阻止了进一步的验证。

本文翻译自securityonline [原文链接](https://securityonline.info/fibergateway-router-hacked-portugals-1-6m-homes-at-risk/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308048](/post/id/308048)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/fibergateway-router-hacked-portugals-1-6m-homes-at-risk/)

如若转载,请注明出处： <https://securityonline.info/fibergateway-router-hacked-portugals-1-6m-homes-at-risk/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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