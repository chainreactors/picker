---
title: 新型窃密木马Lampion采用ClickFix攻击手法，可静默窃取用户登录凭据
url: https://www.anquanke.com/post/id/312981
source: 安全客-有思想的安全新媒体
date: 2025-10-31
fetch_date: 2025-11-01T03:08:48.727771
---

# 新型窃密木马Lampion采用ClickFix攻击手法，可静默窃取用户登录凭据

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

# 新型窃密木马Lampion采用ClickFix攻击手法，可静默窃取用户登录凭据

阅读量**14783**

发布时间 : 2025-10-31 17:39:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-lampion-stealer-uses-clickfix-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员发现一场利用**Lampion银行木马**的复杂攻击活动。该恶意软件自2019年起活跃，目前**重新聚焦于葡萄牙金融机构**。

幕后威胁 actor 团伙显著改进了攻击战术，引入**新型社会工程技术**，使传统检测手段愈发难以识别。

此最新攻击变种的独特之处在于整合了**ClickFix诱饵**——一种欺骗用户在执行恶意载荷前“修复技术问题”的欺诈手段。

### **感染链：从钓鱼邮件到ClickFix诱饵**

感染始于精心构造的**仿冒银行转账通知的钓鱼邮件**。

威胁 actor 使用**被盗邮箱账户**分发邮件，使其具备普通检查难以识破的真实性。

邮件包含**ZIP文件附件**而非直接链接——这一战术转变于2024年9月中旬实施，体现了团伙为绕过安全控制的**适应性策略**。

Bitsight分析师将攻击活动的演变划分为三个阶段，其中最显著的变化发生在2024年12月中旬，当时**ClickFix社会工程学**被引入攻击链。

![]()

研究人员记录到，该恶意软件的日活跃感染量达数十次，目前有**数百台受感染系统**处于攻击者控制之下。

这种规模反映了攻击活动的有效性和团伙的**运营成熟度**。感染链呈现**多阶段架构**，旨在每一步规避检测。

受害者下载伪装标签的附件后，会看到看似合法的**Windows错误通知**（包含熟悉的UI元素）。

此ClickFix诱饵诱导用户点击链接以“修复问题”，实则启动恶意软件交付流程——在用户产生虚假安全感的同时，感染过程在后台悄然展开。

支持该攻击活动的技术基础设施展现了**极高的运营安全专业性**。

![]()

感染链通过**混淆的Visual Basic脚本**推进，每阶段进一步隐藏恶意意图，最终加载包含窃取功能的DLL载荷。

值得注意的是，2025年6月左右，第一阶段新增了**持久化机制**，使恶意软件能够在系统重启后存活并维持跨会话访问。

威胁 actor 利用**跨多个云服务商的地理分布式基础设施**，有效隔离其操作。

基础设施内置的IP黑名单功能阻止安全研究人员追踪完整感染链，同时允许攻击者**精细化控制向特定受害者分发特定载荷**。

Bitsight研究人员指出，每个感染阶段存在数百个独特样本，表明其采用**自动化生成技术**。这意味着团伙具备足够技术能力在攻击周期中高效扩展操作，同时维持全程运营安全。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-lampion-stealer-uses-clickfix-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312981](/post/id/312981)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-lampion-stealer-uses-clickfix-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-lampion-stealer-uses-clickfix-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **641**

* 粉丝
* **6**

### TA的文章

* ##### [Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中](/post/id/312947)

  2025-10-31 17:44:46
* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道](/post/id/312953)

  2025-10-31 17:43:54
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27

### 相关文章

* ##### [Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中](/post/id/312947)

  2025-10-31 17:44:46
* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道](/post/id/312953)

  2025-10-31 17:43:54
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27
* ##### [OpenAI官方证实：GPT-5处理心理与情感困扰的能力已获显著优化](/post/id/312964)

  2025-10-31 17:42:05
* ##### [Chromium内核浏览器Blink渲染引擎中存在高危漏洞，可致攻击者在数秒内引发浏览器崩溃](/post/id/312968)

  2025-10-31 17:40:59

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