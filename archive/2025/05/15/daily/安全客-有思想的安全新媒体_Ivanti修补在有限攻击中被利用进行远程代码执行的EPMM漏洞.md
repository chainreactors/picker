---
title: Ivanti修补在有限攻击中被利用进行远程代码执行的EPMM漏洞
url: https://www.anquanke.com/post/id/307365
source: 安全客-有思想的安全新媒体
date: 2025-05-15
fetch_date: 2025-10-06T22:23:25.148465
---

# Ivanti修补在有限攻击中被利用进行远程代码执行的EPMM漏洞

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

# Ivanti修补在有限攻击中被利用进行远程代码执行的EPMM漏洞

阅读量**62672**

发布时间 : 2025-05-14 15:23:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/05/ivanti-patches-epmm-vulnerabilities.html>

译文仅供参考，具体内容表达以及含义原文为准。

Ivanti 发布了安全更新，以解决 Endpoint Manager Mobile （EPMM） 软件中的两个安全漏洞，这两个漏洞在攻击中被链接起来，以获得远程代码执行。

有问题的漏洞如下 –

* **CVE-2025-4427**（CVSS 评分：5.3）- Ivanti Endpoint Manager Mobile 中的身份验证绕过，允许攻击者在没有适当凭据的情况下访问受保护的资源
* **CVE-2025-4428**（CVSS 评分：7.2）- Ivanti Endpoint Manager Mobile 中存在远程代码执行漏洞，允许攻击者在目标系统上执行任意代码

这些缺陷会影响产品的以下版本 –

* 11.12.0.4 及更早版本（已在 11.12.0.5 中修复）
* 12.3.0.1 及更早版本（已在 12.3.0.2 中修复）
* 12.4.0.1 及更早版本（在 12.4.0.2 中已修复）
* 12.5.0.0 及更早版本（已在 12.5.0.1 中修复）

Ivanti 感谢 CERT-EU 报告这些问题，并表示“在披露时，它知道被利用的客户数量非常有限”，并且这些漏洞“与集成到 EPMM 中的两个开源库有关”。

然而，该公司没有透露受影响的图书馆的名称。目前还不知道依赖这两个库的其他软件应用程序可能会受到影响。此外，该公司表示仍在调查这些案件，并且没有与恶意活动相关的可靠入侵指标。

Ivanti 指出：“如果客户已经使用内置的 Portal ACL 功能或外部 Web 应用程序防火墙过滤了对 API 的访问，那么客户的风险就会大大降低。

“此问题仅影响本地 EPMM 产品。Ivanti Neurons for MDM、Ivanti 基于云的统一端点管理解决方案、Ivanti Sentry 或任何其他 Ivanti 产品中都没有它。

另外，Ivanti 还发布了补丁，以遏制 Neurons for ITSM 本地版本中的身份验证绕过漏洞（CVE-2025-22462，CVSS 评分：9.8），该漏洞可能允许未经身份验证的远程攻击者获得对系统的管理访问权限。没有证据表明该安全缺陷已在野外被利用。

近年来，随着 Ivanti 设备中的零日攻击成为威胁行为者的避雷针，用户必须迅速行动起来，将其实例更新到最新版本，以实现最佳保护。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/05/ivanti-patches-epmm-vulnerabilities.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307365](/post/id/307365)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/05/ivanti-patches-epmm-vulnerabilities.html)

如若转载,请注明出处： <https://thehackernews.com/2025/05/ivanti-patches-epmm-vulnerabilities.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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