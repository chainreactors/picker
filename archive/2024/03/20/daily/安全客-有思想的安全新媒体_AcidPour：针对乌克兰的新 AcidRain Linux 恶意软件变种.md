---
title: AcidPour：针对乌克兰的新 AcidRain Linux 恶意软件变种
url: https://www.anquanke.com/post/id/294082
source: 安全客-有思想的安全新媒体
date: 2024-03-20
fetch_date: 2025-10-04T12:09:34.249188
---

# AcidPour：针对乌克兰的新 AcidRain Linux 恶意软件变种

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

# AcidPour：针对乌克兰的新 AcidRain Linux 恶意软件变种

阅读量**79805**

发布时间 : 2024-03-19 10:27:56

**x**

##### 译文声明

本文是翻译文章，文章来源：https://twitter.com/TomHegel

译文仅供参考，具体内容表达以及含义原文为准。

SentinelLabs 研究人员发现了“AcidPour”，这是针对乌克兰 Linux 系统的 AcidRain Linux 恶意软件的变种。这种新菌株在其前身的基础上进行了扩展，并对用户构成了风险。

最初的 AcidRain 恶意软件于 2022 年 3 月出现，特别是在“Viasat 黑客攻击”期间使用，该黑客攻击在俄罗斯入侵乌克兰开始时中断了 KA-SAT Surfbeam2 调制解调器。

SentinelLabs 的首席威胁研究员TomHegel发现了专为 Linux x86 设备编译的新变体。虽然 AcidPour 与 AcidRain 在某些字符串中具有相似之处，但它在代码库中存在显着差异，代码库是针对 x86 架构而不是 MIPS 编译的。

研究员发现了专为 Linux x86 设备编译的新变体，虽然 AcidPour 与 AcidRain 在某些字符串中具有相似之处，但它在代码库中存在显着差异，代码库是针对 x86 架构而不是 MIPS 编译的。

值得注意的是，适用于 x86 设备的流行 Linux 发行版包括 Ubuntu、Mint、Fedora 和 Debian。另一方面，MIPS（无互锁流水线阶段的微处理器）是一种指令集架构（ISA），它本质上定义了处理器理解并用于执行指令的语言。与 x86 类似，它是一组关于处理器如何运行的规则和规范。

AcidRain 作为通用擦除器运行，针对嵌入式 Linux 发行版上的常见目录和设备路径。然而，AcidPour 引入了新元素，引用未排序块映像 (UBI) 和与逻辑卷管理器 (LVM) 相关的虚拟块设备，这表明目标可能会超出以前的迭代范围。

尽管有相似之处，但还是存在显着差异，包括 LVM 等设备的独特擦除逻辑，这表明威胁行为者可能会制定一种策略。好消息是，SentinelLabs 已经提高了乌克兰利益相关者对 AcidPour 的认识，尽管该行动的具体目标和范围仍不清楚。

这一发现进一步表明，恶意软件威胁的演变速度有多快，攻击者会调整策略来利用各种系统中的漏洞。从毫无戒心的用户或企业组织的角度来看，两者都必须密切关注 AcidRain 和 AcidPour 等网络安全威胁。

本文翻译自https://twitter.com/TomHegel 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294082](/post/id/294082)

安全KER - 有思想的安全新媒体

本文转载自: https://twitter.com/TomHegel

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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