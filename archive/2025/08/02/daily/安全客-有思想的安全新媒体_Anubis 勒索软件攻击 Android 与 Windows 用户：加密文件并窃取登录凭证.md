---
title: Anubis 勒索软件攻击 Android 与 Windows 用户：加密文件并窃取登录凭证
url: https://www.anquanke.com/post/id/310816
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:18:06.423392
---

# Anubis 勒索软件攻击 Android 与 Windows 用户：加密文件并窃取登录凭证

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

# Anubis 勒索软件攻击 Android 与 Windows 用户：加密文件并窃取登录凭证

阅读量**76695**

发布时间 : 2025-08-01 17:04:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/anubis-ransomware-attacking-android-and-windows-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种新型且极具威胁性的勒索软件正在地下黑客圈快速传播，具备双平台攻击能力，能够**同时针对 Android 和 Windows 系统实施文件加密与凭证窃取攻击**。

Anubis 勒索软件首次被发现是在 **2024 年 11 月**，它代表了恶意软件设计的一次危险升级：结合传统勒索软件的破坏性加密能力与银行木马的凭证窃取技巧，形成了一个高度复杂的跨平台威胁。这一恶意软件的出现，正值全球勒索软件攻击激增之际。

根据最新威胁情报数据显示，全球在泄密站点上被公开披露的勒索软件受害者数量同比增长了近 **25%**，而勒索软件组织运营的泄密站数量也增加了 **53%**。Anubis 的活跃攻击行为，是这一统计数据显著上升的推动因素之一，特别是它频繁攻击医疗、建筑和专业服务等关键基础设施和高价值目标。

安全研究公司 Bitsight 将 Anubis 列为**特别危险的威胁**，原因在于其高度成熟的双平台攻击策略和破坏性功能。研究还发现，该勒索组织在暗网上采用了独特的**“勒索即服务（RaaS）”模式**，允许不同附属攻击者灵活参与并按比例分成。

与其他勒索软件家族不同，Anubis 融入了**“永久数据删除”机制**，一些受害者即便支付赎金，仍报告数据彻底丢失，无法恢复。

## 攻击流程：从鱼叉式钓鱼到多重数据窃取

Anubis 攻击的起点通常是精心伪造的**钓鱼邮件**，通过看似可信的邮件渠道向用户投递恶意载荷。

在 Android 设备上，Anubis 主要作为**银行木马**运作，通过伪装成正规应用界面的浮层钓鱼页面来窃取用户登录凭据。同时，它还会在后台执行**屏幕录制与按键记录（Keylogging）**操作，以获取更多认证信息。

更具传播性的特点在于：它会**利用受害者的联系人列表**批量发送短信，将自身扩散至更多设备，实现快速蔓延。

## 高级执行能力与持久化机制

Anubis 拥有极为复杂的执行技术，攻击者可通过配置命令行参数来灵活控制攻击场景，包括：

* `/KEY=`：加密密钥配置；
* `/elevated`：提升权限；
* `/PATH=`：加密目标路径；
* `/PFAD=`：自定义目录路径；
* `/WIPEMODE`：数据擦除模式。

在 Windows 系统上，Anubis 使用**椭圆曲线集成加密方案（ECIES）**对文件进行加密，这种加密算法具备极高的安全性，使得非授权解密几乎不可能实现。

此外，它还会**删除系统的“卷影副本”以阻断数据恢复路径**，关闭关键系统服务，并通过访问令牌操控等技术进行权限提升。通过这一整套多层攻击机制，Anubis 能够在设备上造成最大破坏，并使得常规的恢复手段失效，从而迫使受害者陷入**“支付赎金或永久数据丢失”**的两难境地。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/anubis-ransomware-attacking-android-and-windows-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310816](/post/id/310816)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/anubis-ransomware-attacking-android-and-windows-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/anubis-ransomware-attacking-android-and-windows-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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

* [攻击流程：从鱼叉式钓鱼到多重数据窃取](#h2-0)
* [高级执行能力与持久化机制](#h2-1)

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