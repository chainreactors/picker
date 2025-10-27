---
title: 超过46，000个Grafana实例暴露于帐户接管错误
url: https://www.anquanke.com/post/id/308501
source: 安全客-有思想的安全新媒体
date: 2025-06-17
fetch_date: 2025-10-06T22:47:52.060011
---

# 超过46，000个Grafana实例暴露于帐户接管错误

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

# 超过46，000个Grafana实例暴露于帐户接管错误

阅读量**54188**

发布时间 : 2025-06-16 16:14:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/over-46-000-grafana-instances-exposed-to-account-takeover-bug/>

译文仅供参考，具体内容表达以及含义原文为准。

![超过 46,000 个 Grafana 实例暴露于账户接管错误中]()

超过 46000 个面向 Internet 的 Grafana 实例仍未修补，并面临客户端开放重定向漏洞，该漏洞允许执行恶意插件和帐户接管。

该漏洞被跟踪为 CVE-2025-4123，并影响用于监控和可视化基础设施和应用程序指标的开源平台的多个版本。

该漏洞由漏洞赏金猎人 Alvaro Balada 发现，并在 5 月 21 日发布的 Grafana Labs 安全更新中得到解决。

然而，据应用安全公司 OX Security 的研究人员称，截至撰写本文时，通过公共互联网可访问的所有 Grafana 实例中，超过三分之一尚未修补，他们将该错误称为“Grafana Ghost”。

分析师告诉 BleepingComputer，他们的工作重点是展示将 Balada 的发现武器化的能力。

在确定了易受攻击的版本后，他们通过将数据与平台在整个生态系统中的分布相关联来评估风险。

他们发现 128,864 个实例在网上暴露，其中 46,506 个仍在运行仍可被利用的易受攻击版本。这相当于大约 36% 的百分比。

![截至 6 月 13 日易受攻击的 Grafana 终端节点]()

**易受攻击的 Grafana 端点**
*来源：BleepingComputer*

OX Security 对 CVE-2025-4123 的深入分析发现，通过一系列结合客户端路径遍历和开放重定向机制的利用步骤，攻击者可以引诱受害者点击 URL，从而导致从威胁行为者控制的站点加载恶意 Grafana 插件。

研究人员表示，这些恶意链接可用于在用户的浏览器中执行任意 JavaScript。

![开发过程]()

**漏洞利用过程**
*来源：OX Security*

该漏洞不需要提升的权限，即使启用了匿名访问，也可以运行。

该漏洞允许攻击者劫持用户会话、更改帐户凭据，并在安装了 Grafana Image Renderer 插件的情况下执行服务器端请求伪造 （SSRF） 以读取内部资源。

虽然 Grafana 中的默认内容安全策略 （CSP） 提供了一些保护，但由于客户端实施的限制，它无法防止漏洞利用。

OX Security 的漏洞利用表明，CVE-2025-4123 可以在客户端被利用，并且可以通过 Grafana 原生的 JavaScript 路由逻辑来绕过现代浏览器规范化机制。

这允许攻击者利用 URL 处理不一致来提供恶意插件，这些插件反过来会修改用户电子邮件地址，从而使通过密码重置的帐户劫持变得微不足道。

尽管 CVE-2025-4123 有多项利用要求，例如用户交互、受害者点击链接时的活动用户会话以及启用插件功能（默认启用），但大量暴露的实例和无需身份验证会造成重大攻击面。

为了降低漏洞利用的风险，建议 Grafana 管理员升级到版本 10.4.18+security-01、11.2.9+security-01、11.3.6+security-01、11.4.4+security-01、11.5.4+security-01、11.6.1+security-01 和 12.0.0+security-01。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/over-46-000-grafana-instances-exposed-to-account-takeover-bug/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308501](/post/id/308501)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/over-46-000-grafana-instances-exposed-to-account-takeover-bug/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/over-46-000-grafana-instances-exposed-to-account-takeover-bug/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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