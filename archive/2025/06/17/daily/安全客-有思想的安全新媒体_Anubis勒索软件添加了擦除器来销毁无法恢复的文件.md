---
title: Anubis勒索软件添加了擦除器来销毁无法恢复的文件
url: https://www.anquanke.com/post/id/308507
source: 安全客-有思想的安全新媒体
date: 2025-06-17
fetch_date: 2025-10-06T22:47:49.632496
---

# Anubis勒索软件添加了擦除器来销毁无法恢复的文件

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

# Anubis勒索软件添加了擦除器来销毁无法恢复的文件

阅读量**48143**

发布时间 : 2025-06-16 16:18:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/anubis-ransomware-adds-wiper-to-destroy-files-beyond-recovery/>

译文仅供参考，具体内容表达以及含义原文为准。

![Anubis 勒索软件]()

Anubis 勒索软件即服务 （RaaS）作在其文件加密恶意软件中添加了一个擦除器模块，该模块会销毁目标文件，即使支付了赎金也无法恢复。

Anubis（不要与带有勒索软件模块的同名 Android 恶意软件混淆）是一种相对较新的 RaaS，于 2024 年 12 月首次观察到，但在今年年初变得更加活跃。

2 月 23 日，运营商在 RAMP 论坛上宣布了一项联盟计划。

KELA 当时的一份报告解释说，Anubis 向勒索软件附属公司提供了其收益的 80% 份额。数据勒索附属公司获得 60% 的佣金，初始访问经纪人获得 50% 的佣金。

目前，Anubis 在暗网上的勒索页面只列出了 8 名受害者，这表明一旦对技术方面的信心得到加强，它可能会增加攻击量。

在这方面，昨天发布的一份 Trend Micro 报告包含证据表明 Anubis 的运营商正在积极努力添加新功能，其中一个不寻常的功能是文件擦除功能。

研究人员在他们剖析的最新 Anubis 样本中发现了雨刷，并认为引入该功能是为了增加受害者更快地付款的压力，而不是拖延谈判或完全无视谈判。

“Anubis 与其他 RaaS 的进一步区别在于它使用文件擦除功能，旨在破坏恢复工作，即使在加密后也是如此，”Trend Micro 解释说。

“这种破坏性倾向增加了受害者的压力，并增加了本已具有破坏性的攻击的风险。”

使用命令行参数“/WIPEMODE”激活破坏性行为，该参数需要发出基于密钥的身份验证。

![Anubis 的擦除模式]()

**Anubis的擦除模式**
*来源：Trend Micro*

激活后，擦除器会擦除所有文件内容，将其大小减小到 0 KB，同时保持文件名和结构不变。

受害者仍将看到预期目录中的所有文件，但其内容将被不可逆地销毁，从而无法恢复。

![加密前（上）和加密后（下）的文件]()

**加密前的文件（上）和加密后的文件（下）**
*来源：Trend Micro*

Trend Micro 的分析显示，Anubis 在启动时支持多个命令，包括用于权限提升、目录排除和目标路径加密的命令。

默认情况下，重要的 system 和 program 目录被排除在外，以避免导致系统完全不可用。

勒索软件会删除卷影副本并终止可能干扰加密过程的进程和服务。

加密系统使用 ECIES（椭圆曲线集成加密方案），研究人员注意到与 EvilByte 和 Prince 勒索软件的实现相似之处。

加密文件附加了“.anubis”扩展名，在受影响的目录上放置了 HTML 赎金记录，并且恶意软件还尝试更改桌面壁纸（失败）。

![Thne Anubis 赎金票据]()

**Anubis 赎金票据**
*来源：Trend Micro*

Trend Micro 观察到，Anubis 攻击从带有恶意链接或附件的网络钓鱼电子邮件开始。

此处提供了与 Anubis 攻击相关的入侵指标 （IoC） 的完整列表。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/anubis-ransomware-adds-wiper-to-destroy-files-beyond-recovery/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308507](/post/id/308507)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/anubis-ransomware-adds-wiper-to-destroy-files-beyond-recovery/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/anubis-ransomware-adds-wiper-to-destroy-files-beyond-recovery/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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