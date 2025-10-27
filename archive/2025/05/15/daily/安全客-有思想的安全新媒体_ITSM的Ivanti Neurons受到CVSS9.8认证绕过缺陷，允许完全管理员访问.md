---
title: ITSM的Ivanti Neurons受到CVSS9.8认证绕过缺陷，允许完全管理员访问
url: https://www.anquanke.com/post/id/307370
source: 安全客-有思想的安全新媒体
date: 2025-05-15
fetch_date: 2025-10-06T22:23:22.146668
---

# ITSM的Ivanti Neurons受到CVSS9.8认证绕过缺陷，允许完全管理员访问

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

# ITSM的Ivanti Neurons受到CVSS9.8认证绕过缺陷，允许完全管理员访问

阅读量**55291**

发布时间 : 2025-05-14 15:30:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/ivanti-neurons-for-itsm-hit-by-cvss-9-8-authentication-bypass-flaw-enabling-full-admin-access/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-29847 & CVE-2024-8190 Ivanti ITSM，身份验证绕过]()

Ivanti 为其本地 Neurons for ITSM 平台发布了一个关键安全补丁，解决了一个严重漏洞 CVE-2025-22462，该漏洞可能允许未经身份验证的攻击者获得管理访问权限。该漏洞的 CVSS 基本分数为 9.8，对未实施建议的网络限制或安全配置的客户构成严重风险。

“*根据系统配置，成功利用此漏洞可能允许未经身份验证的远程攻击者获得对系统的管理访问权限*，”Ivanti 在公告中警告说。

该漏洞存在于身份验证绕过缺陷中，该缺陷会影响 Ivanti Neurons for ITSM 本地部署。此问题会影响 2025 年 5 月版本 2023.4、2024.2 和 2024.3 安全补丁之前的所有实例。

“*身份验证绕过…允许未经身份验证的远程攻击者获得对系统的管理访问权限*，“公告指出。

虽然在披露时未观察到漏洞利用，但风险级别在很大程度上取决于系统配置。Ivanti 为满足以下条件的客户引入了 6.9 分（中等）的环境评分：

* 限制 IIS 对内部网络和特定 IP 的访问
* 将解决方案放置在 DMZ 中
* 仅限高权限内部用户登录

“*遵循 Ivanti 关于保护 IIS 网站和限制访问的指南的客户…降低了对环境的风险，*“Ivanti 解释道。

以下版本受到影响：

* Ivanti Neurons for ITSM（仅限本地）：版本 2023.4、2024.2 和 2024.3（2025 年 5 月补丁之前）

可用的修补版本：

* 2023.4 2025 年 5 月安全补丁
* 2024.2 2025 年 5 月安全补丁
* 2024.3 2025 年 5 月安全补丁

修补程序下载和文档可通过 Ivanti 的许可证系统获得。

如果无法立即进行修补，Ivanti 建议：

* 使用 ACL 限制 IIS 访问以仅允许受信任的 IP
* 确保通过 DMZ 路由外部登录访问
* 遵循 Ivanti 部署和 IIS 强化文档中的安全部署指南

本文翻译自securityonline [原文链接](https://securityonline.info/ivanti-neurons-for-itsm-hit-by-cvss-9-8-authentication-bypass-flaw-enabling-full-admin-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307370](/post/id/307370)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ivanti-neurons-for-itsm-hit-by-cvss-9-8-authentication-bypass-flaw-enabling-full-admin-access/)

如若转载,请注明出处： <https://securityonline.info/ivanti-neurons-for-itsm-hit-by-cvss-9-8-authentication-bypass-flaw-enabling-full-admin-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

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