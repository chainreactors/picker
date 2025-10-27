---
title: 华硕Armoury Crate漏洞让攻击者获得Windows管理员特权
url: https://www.anquanke.com/post/id/308565
source: 安全客-有思想的安全新媒体
date: 2025-06-19
fetch_date: 2025-10-06T22:47:56.862161
---

# 华硕Armoury Crate漏洞让攻击者获得Windows管理员特权

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

# 华硕Armoury Crate漏洞让攻击者获得Windows管理员特权

阅读量**100272**

发布时间 : 2025-06-18 15:15:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/asus-armoury-crate-bug-lets-attackers-get-windows-admin-privileges/>

译文仅供参考，具体内容表达以及含义原文为准。

![华硕]()

ASUS Armoury Crate 软件中存在一个高严重性漏洞，可让威胁行为者在 Windows 机器上将其权限提升到 SYSTEM 级别。

该安全问题被跟踪为 CVE-2025-3464，严重性评分为 8.8 分（满分 10 分）。

攻击者可利用此漏洞绕过授权，并影响 Armoury Crate 系统管理软件的AsIO3.sys。

Armoury Crate 奥创游戏智控中心是华硕 Windows 的官方系统控制软件，提供集中化界面来控制 RGB 灯效 （Aura Sync）、调整风扇曲线、管理性能配置文件和华硕外围设备，以及下载驱动程序和固件更新。

为了执行所有这些功能并提供低级系统监控，软件套件使用内核驱动程序来访问和控制硬件功能。

Cisco Talos 的研究员 Marcin “Icewall” Noga 向这家科技公司报告了 CVE-2025-3464。

根据 Talos 的公告，问题在于驱动程序根据硬编码的 SHA-256 哈希AsusCertService.exe和 PID 允许列表来验证调用者，而不是使用适当的作系统级访问控制。

利用该漏洞涉及创建从良性测试应用程序到虚假可执行文件的硬链接。攻击者启动应用程序，暂停它，然后交换硬链接以指向AsusCertService.exe。

当驱动程序检查文件的 SHA-256 哈希时，它会读取现在链接的受信任二进制文件，从而允许测试应用程序绕过授权并获得对驱动程序的访问权限。

这授予攻击者低级系统权限，使他们能够直接访问物理内存、I/O 端口和特定于模型的寄存器 （MSR），从而为作系统完全泄露开辟道路。

请务必注意，攻击者必须已经在系统上（恶意软件感染、网络钓鱼、被盗用的非特权帐户）才能利用 CVE-2025-3464。

但是，该软件在世界各地的计算机上的广泛部署可能代表着一个足够大的攻击面，以至于利用变得具有吸引力。

思科 Talos 验证 CVE-2025-3464 会影响 Armoury Crate 版本 5.9.13.0，但华硕的公告指出，该漏洞会影响 5.9.9.0 到 6.1.18.0 之间的所有版本。

为了缓解安全问题，建议通过打开 Armoury Crate 应用程序并转到“设置”>“更新中心”>“检查更新”>“更新”来应用最新更新。

Cisco 在 2 月份向 ASUS 报告了该漏洞，但到目前为止尚未观察到野外利用。但是，“华硕强烈建议用户将他们的 Armoury Crate 安装更新到最新版本。

导致本地权限提升的 Windows 内核驱动程序错误在黑客中很受欢迎，包括勒索软件行为者、恶意软件作和对政府机构的威胁。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/asus-armoury-crate-bug-lets-attackers-get-windows-admin-privileges/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308565](/post/id/308565)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/asus-armoury-crate-bug-lets-attackers-get-windows-admin-privileges/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/asus-armoury-crate-bug-lets-attackers-get-windows-admin-privileges/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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