---
title: XRPL 官方 NPM 包遭恶意篡改，私钥窃取威胁波及数十万加密货币应用
url: https://www.anquanke.com/post/id/306856
source: 安全客-有思想的安全新媒体
date: 2025-04-25
fetch_date: 2025-10-06T22:04:25.760370
---

# XRPL 官方 NPM 包遭恶意篡改，私钥窃取威胁波及数十万加密货币应用

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

# XRPL 官方 NPM 包遭恶意篡改，私钥窃取威胁波及数十万加密货币应用

阅读量**74014**

发布时间 : 2025-04-24 14:38:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/ripple-xprl-official-npm-package-hijacked/>

译文仅供参考，具体内容表达以及含义原文为准。

一场针对加密货币用户的重大供应链攻击事件发生了。XRP Ledger 的 JavaScript SDK 的官方 XRPL NPM 包遭到了恶意代码的篡改，这些恶意代码旨在窃取加密货币的私钥，有可能影响到成千上万的应用程序。

2025 年 4 月 21 日格林尼治标准时间 20 点 53 分，Aikido Intel 的安全监控系统检测到 xrpl 库出现了五个不同寻常的新软件包版本，该库平均每周的下载量超过 14 万次。

进一步的调查证实，这些版本包含了能够窃取加密货币私钥并获取对用户数字钱包未经授权访问权限的后门代码。

Aikido Intel 的恶意软件研究员 Charlie Eriksen 警告称：“有成千上万的应用程序和网站在使用这个软件包，这对加密货币生态系统来说可能是一场灾难性的供应链攻击。”

安全团队很快确定，一个名为 “mukulljangid” 的用户发布了这些可疑的软件包版本。据信这个账户属于一名 Ripple 的员工，其账号凭证已被泄露。

恶意版本 ——4.2.1、4.2.2、4.2.3、4.2.4 和 2.14.2—— 与该项目在 GitHub 代码库上的任何官方版本都不相符，这立即引起了警惕。

技术分析显示，该软件包中嵌入了一个可疑函数。这个函数的设计目的是将私钥信息发送到一个仅在 2025 年 1 月注册的外部域名 ——0x9c [.] xyz.checkValidityOfSeed。

当用户创建新钱包或与现有钱包进行交互时，恶意代码就会被激活，将敏感的加密信息发送给攻击者。

Eriksen 解释说：“攻击者一直在积极尝试不同的方法来插入后门，同时尽可能地隐藏自己。从手动将后门插入已构建的 JavaScript 代码中，到将其放入 TypeScript 代码中，然后再编译成已构建的版本。”

XRP Ledger Foundation 已确认，该漏洞仅影响 xrpl.js 库，而不影响 XRP 账本的代码库或 GitHub 代码库本身。

为应对这一发现，版本4.2.5 和 2.14.3迅速发布，以替换被篡改的软件包。

安全专家估计，在被检测到并移除之前，恶意软件包版本大约被下载了 450 次。

强烈敦促在 4 月 21 日至 4 月 22 日期间可能安装了任何被篡改软件包的用户检查其网络日志中是否有与可疑域名的出站连接。

这一事件凸显了针对加密货币基础设施的软件供应链攻击日益增长的威胁。过去也曾发生过类似事件，包括 2021 年 UAParser.js 被篡改事件，那次事件影响了一个每周下载量达数百万次的软件包。

建议使用 XRP 的机构和开发人员立即更新到最新的软件包版本，并假定任何由被篡改版本处理过的种子密钥或私钥都已被泄露。

金融机构和加密货币服务提供商也应该对其依赖的软件进行全面的安全审计，以确保它们没有受到此次或类似的供应链攻击的影响。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/ripple-xprl-official-npm-package-hijacked/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306856](/post/id/306856)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/ripple-xprl-official-npm-package-hijacked/)

如若转载,请注明出处： <https://cybersecuritynews.com/ripple-xprl-official-npm-package-hijacked/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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