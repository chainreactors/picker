---
title: Google Chrome 0-Day漏洞被野外利用以执行任意代码
url: https://www.anquanke.com/post/id/308045
source: 安全客-有思想的安全新媒体
date: 2025-06-04
fetch_date: 2025-10-06T22:50:44.052468
---

# Google Chrome 0-Day漏洞被野外利用以执行任意代码

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

# Google Chrome 0-Day漏洞被野外利用以执行任意代码

阅读量**94032**

发布时间 : 2025-06-03 14:45:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/chrome-0-day-vulnerability-exploited-in-the-wild/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在确认攻击者正在积极利用一个关键的零日漏洞后，Google 发布了 Chrome 的紧急安全更新。

该漏洞被跟踪为 CVE-2025-5419，允许威胁行为者通过 Chrome V8 JavaScript 引擎中的越界读写作在受害者的系统上执行任意代码。

这家科技巨头为 Windows 和 Mac 用户推出了 Chrome 137.0.7151.68/.69 版本，为 Linux 系统推出了 137.0.7151.68 版本，该更新将在未来几天和几周内在全球范围内推出。

Google 已明确表示“CVE-2025-5419 的漏洞正在广泛存在”，将其标记为需要用户立即关注的高优先级安全问题。

## Chrome 0 Day 漏洞被利用

CVE-2025-5419 由 Google 威胁分析小组的 Clement Lecigne 和 Benoît Sevens 于 2025 年 5 月 27 日发现并报告。该漏洞源于 V8 中的内存损坏问题，V8 是 Chrome 的 JavaScript 和 WebAssembly 引擎，用于处理来自网站和 Web 应用程序的代码。

越界内存访问漏洞特别危险，因为它们可能允许攻击者读取敏感数据或将恶意代码写入系统内存。

认识到威胁的严重性后，Google 于 2025 年 5 月 28 日实施了紧急缓解措施，在所有 Chrome 平台上推送配置更改，以帮助在完整补丁可用之前保护用户。

这种快速响应表明了该漏洞的严重性及其对全球 Chrome 用户构成的积极威胁。

此安全更新还解决了第二个漏洞 CVE-2025-5068，这是 Chrome 的渲染引擎 Blink 中的一个释放后使用缺陷。安全研究人员 Walkman 于 2025 年 4 月 7 日报告了这个中等严重性漏洞，并提供了 1,000 美元的赏金。

虽然没有零日漏洞那么严重，但释放后使用漏洞仍可能导致内存损坏和潜在的代码执行。

Google 一直保持其政策，即在大多数用户更新其浏览器之前限制访问详细的漏洞信息。

这种方法可以防止恶意行为者对补丁进行逆向工程以开发新的漏洞，而用户仍然使用易受攻击的版本。

该公司认为，其全面的安全测试基础设施能够在许多漏洞达到稳定版本之前检测到它们。

Google 采用高级工具（包括 AddressSanitizer、MemorySanitizer、UndefinedBehaviorSanitizer、Control Flow Integrity、libFuzzer 和 AFL）来识别开发过程中的潜在安全问题。

Chrome 用户应立即通过导航到“设置”>“关于 Chrome”来更新他们的浏览器，这将自动下载并安装最新版本。

鉴于 CVE-2025-5419 已被积极利用，强烈建议用户将此更新视为紧急更新。用户可以验证其 Chrome 版本是否与 137.0.7151.68 或更高版本匹配，以确保免受这些漏洞的影响。

组织应优先在其网络中部署此更新，以防止通过针对零日漏洞的恶意网站进行潜在入侵。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/chrome-0-day-vulnerability-exploited-in-the-wild/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308045](/post/id/308045)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/chrome-0-day-vulnerability-exploited-in-the-wild/)

如若转载,请注明出处： <https://cybersecuritynews.com/chrome-0-day-vulnerability-exploited-in-the-wild/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Chrome 0 Day 漏洞被利用](#h2-0)

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