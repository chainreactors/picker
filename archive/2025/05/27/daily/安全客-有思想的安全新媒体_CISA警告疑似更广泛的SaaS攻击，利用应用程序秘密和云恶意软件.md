---
title: CISA警告疑似更广泛的SaaS攻击，利用应用程序秘密和云恶意软件
url: https://www.anquanke.com/post/id/307740
source: 安全客-有思想的安全新媒体
date: 2025-05-27
fetch_date: 2025-10-06T22:23:30.757146
---

# CISA警告疑似更广泛的SaaS攻击，利用应用程序秘密和云恶意软件

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

# CISA警告疑似更广泛的SaaS攻击，利用应用程序秘密和云恶意软件

阅读量**38749**

发布时间 : 2025-05-26 13:02:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/05/cisa-warns-of-suspected-broader-saas.html>

译文仅供参考，具体内容表达以及含义原文为准。

国网络安全和基础设施安全局(CISA)周四透露,Commvault正在监控针对其Microsoft Azure云环境中托管的应用程序的网络威胁活动。

“威胁行为者可能已经访问了Commvault(金属)Microsoft 365(M365)备份软件即服务(SaaS)解决方案的客户机密,该解决方案托管在Azure中[,”该机构表示。](https://www.cisa.gov/news-events/alerts/2025/05/22/advisory-update-cyber-threat-activity-targeting-commvaults-saas-cloud-application-metallic)

“这为威胁行为者提供了对Commvault客户M365环境的未经授权的访问,这些环境具有Commvault存储的应用程序秘密。

CISA进一步指出,该活动可能是针对各种软件即服务(SaaS)提供商的云基础设施的更广泛活动的一部分,具有默认配置和更高的权限。

几周前,Commvault透露,微软在2025年2月通知该公司,其Azure环境中的民族国家威胁行为者未经授权的活动。

该事件导致发现威胁行为者一直在利用零日漏洞[(](https://thehackernews.com/2025/04/cisa-adds-actively-exploited-broadcom.html)CVE-2025-3928),这是Commvault Web服务器中未指明的漏洞,使远程身份验证的攻击者能够创建和执行Webshell。

“基于行业专家,这个威胁行为者使用复杂的技术来尝试访问客户M365环境,”Commvault在一份公告中说。“这个威胁行为者可能已经访问了某些Commvault客户用来验证其M365环境的应用程序凭据的子集。

Commvault表示已采取多项补救措施,包括为M365轮换应用程序凭据,但强调没有未经授权访问客户备份数据。

为了减轻此类威胁,CISA建议用户和管理员遵循以下准则:

* 监控 Entra 审计日志,以获取由 Commvault 应用程序/服务委托人发起的未经授权修改或添加对服务委托人的凭据
* 审查 Microsoft 日志(Entra 审核、Entra 登录、统一审计日志)并进行内部威胁搜索
* 对于单个租户应用程序,请实施有条件访问策略,该策略将应用程序服务主体的身份验证限制为 Commvault 允许列出的 IP 地址范围内的已批准 IP 地址。
* 在行政同意的情况下,查看Entra的申请注册和服务负责人名单,以获得比业务需求更高的特权
* 限制对可信网络和管理系统的 Commvault 管理接口的访问
* 通过部署 Web 应用程序防火墙和删除对 Commvault 应用程序的外部访问来检测和阻止路径遍历尝试和可疑文件上传

CISA在2025年4月下旬将添加到其已知的易用漏洞目录[CVE-2025-3928](https://thehackernews.com/2025/04/cisa-adds-actively-exploited-broadcom.html)中,并表示将继续与合作伙伴组织合作调查恶意活动。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/05/cisa-warns-of-suspected-broader-saas.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307740](/post/id/307740)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/05/cisa-warns-of-suspected-broader-saas.html)

如若转载,请注明出处： <https://thehackernews.com/2025/05/cisa-warns-of-suspected-broader-saas.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

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