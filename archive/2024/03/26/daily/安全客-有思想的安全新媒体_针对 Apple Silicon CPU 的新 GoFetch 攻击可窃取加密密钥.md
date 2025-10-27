---
title: 针对 Apple Silicon CPU 的新 GoFetch 攻击可窃取加密密钥
url: https://www.anquanke.com/post/id/294288
source: 安全客-有思想的安全新媒体
date: 2024-03-26
fetch_date: 2025-10-04T12:11:20.922629
---

# 针对 Apple Silicon CPU 的新 GoFetch 攻击可窃取加密密钥

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

# 针对 Apple Silicon CPU 的新 GoFetch 攻击可窃取加密密钥

阅读量**85854**

发布时间 : 2024-03-25 10:26:20

**x**

##### 译文声明

本文是翻译文章，文章来源：https://gofetch.fail/files/gofetch.pdf

译文仅供参考，具体内容表达以及含义原文为准。

美国几所大学的研究团队披露了一种新的旁道攻击方法的细节，该方法可用于从苹果 CPU 驱动的系统中提取秘密加密密钥。

这种被称为GoFetch 的攻击方法被描述为一种微架构旁道攻击，允许从恒定时间加密实现中提取秘密密钥。这些类型的攻击需要对目标系统进行本地访问。

该攻击针对名为数据内存相关预取器 (DMP) 的硬件优化，它尝试预取程序内存内容中的地址以提高性能。

研究人员找到了一种使用特制加密操作输入的方法，使他们能够通过监控 DMP 的行为来推断密钥，一次猜测一些密钥。

他们成功地演示了针对多种加密实现的端到端密钥提取攻击，包括 OpenSSL Diffie-Hellman Key Exchange、Go RSA 以及后量子 CRYSTALS-Kyber 和 CRYSTALS-Dilithium。

GoFetch 建立在先前披露的名为Augury的攻击方法之上，该方法于 2022 年提出。

研究人员已经成功地针对 Apple M1 处理器驱动的系统进行了 GoFetch 攻击，并且他们发现了证据表明该攻击也可以针对 M2 和 M3 处理器。他们还测试了使用 DMP 的英特尔处理器，但发现它对于此类攻击“更稳健”。

调查结果已于 2023 年 12 月报告给 Apple。OpenSSL、Go Crypto 和 CRYSTALS 开发人员也已收到通知。

专家表示，苹果正在调查这个问题，但全面解决这个问题似乎并不容易。研究人员提出了几种对策，但它们涉及不易实施的硬件更改或可能对性能产生重大影响的缓解措施。

研究人员发表了一篇论文，详细介绍了他们的工作，并且很快还将发布概念验证 (PoC) 代码。还提供了一段视频来展示密钥提取漏洞的实际应用。

本文翻译自https://gofetch.fail/files/gofetch.pdf 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294288](/post/id/294288)

安全KER - 有思想的安全新媒体

本文转载自: https://gofetch.fail/files/gofetch.pdf

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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