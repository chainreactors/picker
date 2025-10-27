---
title: 开源身份和访问管理平台 Keycloak 发布了安全更新以解决一个高严重性漏洞
url: https://www.anquanke.com/post/id/300750
source: 安全客-有思想的安全新媒体
date: 2024-10-12
fetch_date: 2025-10-06T18:51:41.168499
---

# 开源身份和访问管理平台 Keycloak 发布了安全更新以解决一个高严重性漏洞

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

# 开源身份和访问管理平台 Keycloak 发布了安全更新以解决一个高严重性漏洞

阅读量**187214**

发布时间 : 2024-10-11 10:37:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/keycloak-patches-cve-2024-3656-granting-low-privilege-users-administrative-access/>

译文仅供参考，具体内容表达以及含义原文为准。

开源身份和访问管理平台 Keycloak 发布了一个安全更新，以解决一个可能允许低权限用户未经授权访问管理功能的高严重性漏洞。

![CVE-2024-3656]()

该漏洞由安全研究员 Maurizio Agazzini 发现，被追踪为 CVE-2024-3656，CVSS 得分为 8.1。它影响到 24.0.5 之前的所有 Keycloak 版本。

该漏洞存在于 Keycloak 管理 REST API 的某些端点中。通过利用这些端点，拥有低级用户账户的恶意行为者有可能执行命令并访问通常为管理员保留的敏感信息。这可能导致一系列严重的安全漏洞，包括

数据泄露： 未经授权访问敏感的用户数据、系统配置和应用程序机密。
系统受损：修改系统设置，可能会中断服务或让攻击者进一步控制基础设施。
权限升级： 提升用户权限以完全控制 Keycloak 服务器和连接的应用程序。
Keycloak 已在 24.0.5 版本中解决了此漏洞。强烈建议所有用户立即将其部署更新到最新版本。

Ezoic
您能做些什么？

更新 Keycloak： 如果您运行的 Keycloak 版本早于 24.0.5，请尽快升级到已修补的版本。
查看 API 活动： 监控 Keycloak 日志，查看是否有可疑的 API 请求，尤其是来自低权限账户的请求。
实施最低权限： 确保用户只拥有其角色所需的必要权限。
保持信息畅通： 随时了解 Keycloak 的最新安全公告和补丁。
通过迅速采取行动，企业可以降低 CVE-2024-3656 带来的风险，并保护其关键系统和数据。

本文翻译自securityonline [原文链接](https://securityonline.info/keycloak-patches-cve-2024-3656-granting-low-privilege-users-administrative-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300750](/post/id/300750)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/keycloak-patches-cve-2024-3656-granting-low-privilege-users-administrative-access/)

如若转载,请注明出处： <https://securityonline.info/keycloak-patches-cve-2024-3656-granting-low-privilege-users-administrative-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞预警](/tag/%E6%BC%8F%E6%B4%9E%E9%A2%84%E8%AD%A6)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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