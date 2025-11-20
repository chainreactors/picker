---
title: Fortinet发布警告：其FortiWeb产品中的新零日漏洞正遭攻击利用
url: https://www.anquanke.com/post/id/313275
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:32.960268
---

# Fortinet发布警告：其FortiWeb产品中的新零日漏洞正遭攻击利用

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

# Fortinet发布警告：其FortiWeb产品中的新零日漏洞正遭攻击利用

阅读量**14063**

发布时间 : 2025-11-19 17:35:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-fortiweb-zero-day-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

今日，Fortinet 发布安全更新，修复了 FortiWeb 中一个 **新的零日漏洞**，该漏洞已被威胁行为者在攻击中 **积极利用**。

该漏洞编号为 **CVE-2025-58034**，是 Web 应用防火墙中的安全缺陷，由趋势科技（Trend Micro）趋势研究团队的 Jason McFadyen 报告。

**已认证的威胁行为者** 可通过利用此 **操作系统命令注入漏洞** 实现代码执行，攻击复杂度低且无需用户交互。

“FortiWeb 中存在一个操作系统命令注入（CWE-78）漏洞，允许已认证攻击者通过精心构造的 HTTP 请求或 CLI 命令在底层系统上执行未授权代码，” Fortinet 表示。

这家美国网络安全公司在周二的安全公告中指出：“Fortinet 已观察到该漏洞在野外被利用。”

趋势科技告诉 BleepingComputer，他们已在野外观察到利用该漏洞的攻击，目前检测次数约为 **2000 次**。

为阻止传入攻击，管理员应将 FortiWeb 设备升级至今日发布的最新可用软件版本。

![]()

### 近期 FortiWeb 零日漏洞回顾

上周，Fortinet 还确认已于 **10 月 28 日静默修复了另一个被大规模利用的 FortiWeb 零日漏洞（CVE-2025-64446）**，距离威胁情报公司 Defused 首次报告在野利用已过去三周。

据 Defused 称，攻击者利用 HTTP POST 请求在暴露于互联网的设备上创建新的 **管理员级账户**。

周五，美国网络安全与基础设施安全局（CISA）也将 CVE-2025-64446 加入其 **在野利用漏洞目录**，并命令美国联邦机构在 **11 月 21 日前** 加固系统。

BleepingComputer 已就这些漏洞向 Fortinet 提出问题，但尚未收到回复。

### Fortinet 漏洞的历史利用

今年 8 月，Fortinet 曾修复 FortiSIEM 安全监控解决方案中的另一个命令注入漏洞（**CVE-2025-25256**），当时已有公开利用代码。而就在一天前，网络安全公司 GreyNoise 报告称针对 Fortinet SSL VPN 的暴力攻击激增。

Fortinet 漏洞 **常被用作零日漏洞** 用于网络间谍活动和勒索软件攻击。例如，Fortinet 在 2 月披露，中国黑客组织“ Volt Typhoon”利用两个 FortiOS SSL VPN 漏洞（**CVE-2022-42475** 和 **CVE-2023-27997**），通过自定义的 Coathanger 远程访问木马（RAT）恶意软件，对荷兰国防部军事网络植入后门。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-fortiweb-zero-day-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313275](/post/id/313275)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-fortiweb-zero-day-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-fortiweb-zero-day-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10
* ##### [macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词](/post/id/313255)

  2025-11-19 17:39:45
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员](/post/id/313249)

  2025-11-19 17:37:58

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