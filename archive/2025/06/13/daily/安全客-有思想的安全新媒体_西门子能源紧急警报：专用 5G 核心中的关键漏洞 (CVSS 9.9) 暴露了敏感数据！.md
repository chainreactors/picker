---
title: 西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！
url: https://www.anquanke.com/post/id/308380
source: 安全客-有思想的安全新媒体
date: 2025-06-13
fetch_date: 2025-10-06T22:51:13.226701
---

# 西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！

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

# 西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！

阅读量**1131913**

发布时间 : 2025-06-12 14:24:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/urgent-siemens-energy-alert-critical-flaw-cvss-9-9-in-private-5g-core-exposes-sensitive-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![西门子能源,关键漏洞 CVE-2025-40585]()

西门子已就其能源服务平台(以前称为托管应用程序和服务)发布了关键安全公告,警告利用Elspec G5数字故障记录器(G5DFR)的系统中涉及默认凭据的严重漏洞。该漏洞被跟踪为CVE-2025-40585,其CVSS v3.1基本得分为9.9,突显了其破坏关键基础设施的潜力。

*西门子表示:“使用Elspec G5 Digital Fault Recorder的解决方案包含具有管理权限的默认凭据。具有远程访问的客户端配置可以允许攻击者远程控制G5DFR组件并从设备中篡改输出。*

核心问题源于受影响系统中存在硬编码的默认用户名和密码。如果保持不变,这些凭据可能会被未经身份验证的远程攻击者利用来控制G5DFR组件,从而能够操纵故障监控数据或触发电网中的错误读数等输出。

*“使用G5DFR的受影响解决方案包含默认凭据。这可能允许攻击者控制G5DFR组件并篡改设备的输出*,“该咨询警告说。

该漏洞已归类为CWE-276:不正确的默认权限,当在工业控制系统(ICS)和操作技术(OT)设备中发现时,这是一个常见但极具影响力的弱点。

受影响的产品包括:

* ①西门子能源服务与Elspec G5DFR
* ②当前部署的所有版本

在咨询时没有软件补丁可用。相反,西门子提供了一条直接的缓解路线:

*使用 G5DFR Web 界面更改默认用户名、密码和权限级别。联系客户支持以获取进一步帮助* 。 ”

除了证书变更外,西门子还敦促所有运营商(特别是传输系统运营商(TSO)和配电系统运营商(DSO))采用弹性、多层保护策略。这包括针对网络引起的故障验证网格设计并保护网络边界。

西门子还强调确保更广泛的OT环境的重要性:

*“西门子强烈建议通过适当的机制(例如防火墙、分段、VPN)来保护网络访问……并根据我们的运营指南配置环境。*

本文翻译自securityonline [原文链接](https://securityonline.info/urgent-siemens-energy-alert-critical-flaw-cvss-9-9-in-private-5g-core-exposes-sensitive-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308380](/post/id/308380)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/urgent-siemens-energy-alert-critical-flaw-cvss-9-9-in-private-5g-core-exposes-sensitive-data/)

如若转载,请注明出处： <https://securityonline.info/urgent-siemens-energy-alert-critical-flaw-cvss-9-9-in-private-5g-core-exposes-sensitive-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**5赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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