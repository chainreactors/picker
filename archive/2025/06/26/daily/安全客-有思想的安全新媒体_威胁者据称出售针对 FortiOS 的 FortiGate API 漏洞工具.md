---
title: 威胁者据称出售针对 FortiOS 的 FortiGate API 漏洞工具
url: https://www.anquanke.com/post/id/308930
source: 安全客-有思想的安全新媒体
date: 2025-06-26
fetch_date: 2025-10-06T22:52:19.971952
---

# 威胁者据称出售针对 FortiOS 的 FortiGate API 漏洞工具

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

# 威胁者据称出售针对 FortiOS 的 FortiGate API 漏洞工具

阅读量**51087**

发布时间 : 2025-06-25 14:14:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/fortigate-api-exploit-tool/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

据报道，一名威胁行为者在暗网市场上出售了一款复杂的 FortiGate API 漏洞利用工具，引发了网络安全社区的极大担忧。

该工具的售价为 12,000 美元，并带有托管服务以促进交易，据称它通过利用 170 多个不安全的 API 端点来针对 Fortinet 的 FortiOS 系统，为攻击者提供了从受影响的设备中收集大量敏感信息的方法。

**涉嫌 API 漏洞利用工具索赔**

根据这些披露，该漏洞利用具有一个自动化模块，能够从运行易受攻击的 FortiOS 版本（特别是 7.2 及更低版本）的各种 FortiGate 防火墙设备中扫描和提取数据，但也确认会影响 6.x 系列的早期版本。

它利用多线程技术进行快速、批量的数据提取，使攻击者能够同时攻击多个目标，并在单个作中转储 150 多个独特的配置文件。

据称，该漏洞利用提供了对高度敏感和任务关键型配置数据的访问。据称可检索的信息类型包括防火墙策略、VPN 会话日志、用户帐户凭据、SSL 门户设置、SNMP 社区和加密密钥，以及更深奥的网络设置，包括 DNS、高可用性集群和 NTP 服务器详细信息。

值得注意的是，该工具声称可以绕过传统身份验证，只需要知道设备的 IP 地址和 API 端口，通常暴露在 443 或 10443 处，而不需要用户名或密码。

此类未经授权的访问的影响可能很严重，会暴露组织网络布局、管理员密码哈希、备份配置文件，甚至 SAML、LDAP、RADIUS 或 VPN 会话的实时身份验证令牌，从而为企业环境中的横向移动或权限提升铺平道路。

安全分析师警告说，这种漏洞的出现不仅增加了机会主义攻击的风险，而且还降低了经验不足的恶意行为者进行企业级漏洞的技术门槛。

该工具的自动化，再加上对结构化数据输出和隐蔽 HTTP 标头作的支持，将相对容易地实现大规模利用活动和有针对性的间谍活动。

目前，Fortinet 尚未确认该漏洞的真实性，但敦促运行受影响 FortiOS 版本的组织审查其安全状况，限制未经授权的 API 访问，并在可用时立即应用固件补丁。

这些披露凸显了网络犯罪市场中高级漏洞利用工具商品化所带来的风险越来越大，这让人们认识到在企业防御策略中保持警惕、稳健漏洞管理和快速部署安全更新的重要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/fortigate-api-exploit-tool/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308930](/post/id/308930)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/fortigate-api-exploit-tool/)

如若转载,请注明出处： <https://cybersecuritynews.com/fortigate-api-exploit-tool/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [政策法规](/tag/%E6%94%BF%E7%AD%96%E6%B3%95%E8%A7%84)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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