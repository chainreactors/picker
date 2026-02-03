---
title: 签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用
url: https://www.anquanke.com/post/id/314681
source: 安全客-有思想的安全新媒体
date: 2026-02-02
fetch_date: 2026-02-03T04:08:20.136626
---

# 签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用

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

# 签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用

阅读量**21428**

发布时间 : 2026-02-02 16:11:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/signed-stolen-phantom-stealer-hijacks-java-app-via-fake-dhl-invoice/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款新型高水准恶意软件攻击活动正利用用户对正规软件的信任实施作恶，将**经数字签名的合法 Java 工具变为攻击武器**，投放一款极具破坏力的信息窃取恶意软件。威胁情报研究员马诺伊・克希尔萨加尔发现了这一多阶段攻击手段：攻击者以虚假敦豪物流（DHL）发票为诱饵，投放**幻影窃取者（Phantom Stealer）v3.5.0**—— 这是一款基于.NET 框架的模块化恶意软件，专门用于窃取各类敏感账号凭证。

此次发现揭示出攻击者绕过传统防御体系的**危险新趋势**：他们采用**DLL 侧载技术**，将恶意代码隐藏在受信任的正规应用程序中实施攻击。

该攻击以经典的社会工程学手段为开端：攻击者发送伪装成敦豪物流发票的钓鱼垃圾邮件，催促收件人打开邮件中的 ZIP 压缩附件，声称可通过该附件查看发票文档。

而这份压缩包中却暗藏陷阱：里面包含一个**经合法数字签名的 Java 工具 jdeps.exe**，攻击者将其重命名为 DHL-INVOICE.exe，同时在同目录下植入一个名为 jli.dll 的恶意文件。

当用户点击这个伪装成 “发票” 的可执行文件时，会在不知情的情况下启动这款受信任的 Java 应用。但受 Windows 系统的库文件加载机制影响，该应用会优先加载同目录下的恶意 DLL 文件，而非系统中的正版文件。

克希尔萨加尔在报告中解释道：**“攻击者通过 DLL 侧载技术实现恶意代码执行，让受信任的 Java 启动程序加载该恶意 DLL，并将程序执行权移交至 XLoader 加载器。”**

一旦伪装成 jli.dll 的 XLoader 加载器被激活，便会通过一系列复杂操作规避检测：它利用**经过混淆的状态驱动逻辑**解析自身配置信息，并解密最终的恶意载荷。

该加载器并不会直接运行恶意软件，而是采用**进程掏空技术**：先启动一个合法的微软系统进程 AddInProcess32.exe，随后掏空该进程的内存空间，将恶意代码注入其中。

报告指出：**“恶意载荷通过进程掏空技术被注入 AddInProcess32.exe 进程，实现在合法微软进程中执行恶意代码。”** 这一手段让恶意软件得以 “明处隐藏”，在安全检测工具中，其进程会显示为常规的微软后台任务，难以被识别。

这一精密攻击链的最终环节，便是**幻影窃取者 v3.5.0**的投放。该恶意软件是一款 “基于.NET 框架的模块化信息窃取工具，支持凭证盗取与多渠道数据泄露”。

与常规的垃圾邮件攻击不同，此次攻击活动依托**经数字签名的合法二进制文件**，并采用先进的代码注入技术，攻击手段实现了**质的升级**。克希尔萨加尔在报告中指出，该攻击行动展现出一套 “成熟且以隐身性为核心的恶意载荷投放链”，专门用于绕过现代终端安全防护系统。

报告还披露了攻击者为保护恶意软件配置信息所采用的加密手段：他们使用**CBC 模式的 AES-256 加密算法**，并通过 PBKDF2 算法生成加密密钥，对其命令与控制（C2）配置信息进行加密保护。这一高等级的操作安全设计意味着，即便该恶意软件被安全人员截获，若无对应的解密密钥，其内部工作机制也难以被分析破解。

本文翻译自securityonline [原文链接](https://securityonline.info/signed-stolen-phantom-stealer-hijacks-java-app-via-fake-dhl-invoice/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314681](/post/id/314681)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/signed-stolen-phantom-stealer-hijacks-java-app-via-fake-dhl-invoice/)

如若转载,请注明出处： <https://securityonline.info/signed-stolen-phantom-stealer-hijacks-java-app-via-fake-dhl-invoice/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **990**

* 粉丝
* **6**

### TA的文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用](/post/id/314681)

  2026-02-02 16:11:51

### 相关文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [Moltbook AI平台曝出高危漏洞，致邮箱地址、登录令牌及API密钥泄露](/post/id/314663)

  2026-02-02 16:11:48
* ##### [工业控制系统监控与数据采集漏洞引发拒绝服务攻击，或对工业生产运营造成中断影响](/post/id/314653)

  2026-02-02 16:11:14
* ##### [“修复”实为陷阱：ConsentFix钓鱼攻击借Azure CLI绕过多重身份验证](/post/id/314685)

  2026-02-02 16:11:09

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