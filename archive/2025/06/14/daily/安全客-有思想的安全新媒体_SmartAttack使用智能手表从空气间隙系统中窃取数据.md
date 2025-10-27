---
title: SmartAttack使用智能手表从空气间隙系统中窃取数据
url: https://www.anquanke.com/post/id/308445
source: 安全客-有思想的安全新媒体
date: 2025-06-14
fetch_date: 2025-10-06T22:50:24.711826
---

# SmartAttack使用智能手表从空气间隙系统中窃取数据

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

# SmartAttack使用智能手表从空气间隙系统中窃取数据

阅读量**66502**

发布时间 : 2025-06-13 15:29:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/smartattack-uses-smartwatches-to-steal-data-from-air-gapped-systems/>

译文仅供参考，具体内容表达以及含义原文为准。

![气隙]()

一种被称为“SmartAttack”的新攻击使用智能手表作为隐蔽的超声波信号接收器，从物理隔离（气隙）系统中窃取数据。

气隙系统通常部署在政府设施、武器平台和核电站等关键任务环境中，与外部网络物理隔离，以防止恶意软件感染和数据盗窃。

尽管存在这种孤立性，但他们仍然容易受到内部威胁的入侵，例如使用 USB 驱动器的流氓员工或国家支持的供应链攻击。

一旦渗透，恶意软件就可以秘密运行，使用隐蔽技术来调节硬件组件的物理特性，将敏感数据传输到附近的接收器，而不会干扰系统的正常运行。

SmartAttack 由以色列大学研究人员设计，该研究人员由 [Mordechai Guri 领导，Mordechai Guri](https://arxiv.org/html/2506.08866v1) 是隐蔽攻击通道领域的专家，他之前曾提出过使用 [LCD 屏幕噪声](https://www.bleepingcomputer.com/news/security/new-pixhell-acoustic-attack-leaks-secrets-from-lcd-screen-noise/)、[RAM 调制](https://www.bleepingcomputer.com/news/security/new-rambo-attack-steals-data-using-ram-in-air-gapped-computers/)、[网卡 LED](https://www.bleepingcomputer.com/news/security/etherled-air-gapped-systems-leak-data-via-network-card-leds/)、[USB 驱动器射频信号](https://www.bleepingcomputer.com/news/security/new-software-bridges-an-air-gap-using-an-unmodified-usb/)、[SATA 电缆](https://www.bleepingcomputer.com/news/security/air-gapped-systems-leak-data-via-sata-cable-wifi-antennas/)和[电源](https://www.bleepingcomputer.com/news/security/air-gapped-pcs-vulnerable-to-data-theft-via-power-supply-radiation/)泄露数据的方法。

虽然在许多情况下，对气隙环境的攻击是理论上的，并且极难实现，但它们仍然提供了有趣且新颖的数据泄露方法。

## SmartAttack 的工作原理

SmartAttack 要求恶意软件以某种方式感染气隙计算机，以收集敏感信息，例如击键、加密密钥和凭据。然后，它可以使用计算机的内置扬声器向环境发射超声波信号。

通过使用二进制频移键控 （B-FSK），可以调制音频信号频率以表示二进制数据，即 1 和 0。18.5 kHz 的频率表示“0”，而 19.5 kHz 的频率表示“1”。

![隐蔽的通道和键盘打字的干扰]()

**隐蔽的通道和键盘打字**
的干扰*来源：arxiv.org*

这个范围内的频率是人类听不见的，但仍然可以被附近人佩戴的智能手表麦克风捕捉到。

智能手表中的声音监控应用程序应用信号处理技术来检测频移并解调编码信号，同时还可以应用完整性测试。

数据的最终泄露可以通过 Wi-Fi、蓝牙或蜂窝连接进行。

智能手表可以由流氓员工故意配备此工具，也可以由外人在佩戴者不知情的情况下感染它。

## 性能和限制

研究人员指出，与智能手机相比，智能手表使用小型、低 SNR 的麦克风，因此信号解调非常具有挑战性，尤其是在较高频率和较低信号强度的情况下。

甚至发现手腕方向在攻击的可行性中也起着至关重要的作用，当手表与计算机扬声器有“视线”时效果最佳。

根据发射器（扬声器类型），最大传输范围在 6 到 9 米（20 – 30 英尺）之间。

![发射器类型性能]()

**发射器类型性能**
*来源：arxiv.org*

数据传输速率范围为每秒 5 位 （bps） 至 50 bps，随着速率和距离的增加，可靠性会降低。

![性能测量]()

**性能测量（信噪比、误码率）**
*来源：arxiv.org*

研究人员表示，对抗 SmartAttack 的最佳方法是禁止在安全环境中使用智能手表。

另一种措施是从气隙机器上移除内置扬声器。这将消除所有声学隐蔽通道的攻击面，而不仅仅是 SmartAttack。

如果这些都不可行，那么通过宽带噪声发射、基于软件的防火墙和音频间隙进行超声波干扰仍然可以证明是有效的。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/smartattack-uses-smartwatches-to-steal-data-from-air-gapped-systems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308445](/post/id/308445)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/smartattack-uses-smartwatches-to-steal-data-from-air-gapped-systems/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/smartattack-uses-smartwatches-to-steal-data-from-air-gapped-systems/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [SmartAttack 的工作原理](#h2-0)
* [性能和限制](#h2-1)

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