---
title: 微软Azure API漏洞泄露VPN密钥，内置角色权限过大引发云上安全风险
url: https://www.anquanke.com/post/id/309498
source: 安全客-有思想的安全新媒体
date: 2025-07-08
fetch_date: 2025-10-06T23:18:15.030040
---

# 微软Azure API漏洞泄露VPN密钥，内置角色权限过大引发云上安全风险

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

# 微软Azure API漏洞泄露VPN密钥，内置角色权限过大引发云上安全风险

阅读量**42917**

发布时间 : 2025-07-07 15:48:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/azure-api-vulnerabilities-leak-vpn-keys-and-built-in-roles/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软Azure的基于角色的访问控制系统（RBAC）近日被曝存在**严重安全漏洞**，可能导致企业网络遭遇未授权访问。

安全研究人员指出，一系列**权限过大的内置角色**与**API实现缺陷**结合，构成了攻击者可用来入侵云基础设施与本地网络的高危攻击路径。

这些漏洞的核心问题出在**Azure RBAC权限模型的设计缺陷**。多个看似“服务范围受限”的内置角色，**实际授予了远超其描述的权限范围**，引发权限漂移（Privilege Escalation）风险。

研究发现，至少**10个Azure内置角色**包含了“`*/read`”权限，意味着相关身份可访问**多达9,618项Azure操作权限**，而这些角色原本只是用于执行受限的管理任务。

例如，“Managed Applications Reader”（托管应用读取者）、“Log Analytics Reader”（日志分析读取者）、“Monitoring Reader”（监控读取者）等角色，看似仅具备特定服务的读取权限，**实际却拥有对整个Azure订阅中所有资源的广泛读取权限**。

研究人员指出，这些**超权限角色**的安全风险远不止信息泄露：

* 攻击者可利用这些读取权限**枚举存储账户、数据库、网络配置、备份库等关键资源**，为后续攻击提供情报支持；
* 更严重的是，攻击者还能访问**部署脚本、自动化账户与Web应用配置**，其中可能包含**明文凭据与敏感环境变量**。

除了RBAC权限问题，研究人员还发现**Azure API本身的实现缺陷**也构成了严重威胁：
攻击者可通过一个特定接口，**仅凭基础读取权限即可提取VPN预共享密钥（Pre-Shared Key）**。

这一漏洞源自Azure对不同HTTP方法权限控制不一致——虽然系统通常将敏感操作限制为POST请求，但**VPN密钥提取操作却被错误实现为GET请求**，导致被绕过。

### 攻击链利用方式

最危险之处在于：**这些漏洞可组合形成完整攻击链，威胁混合云环境。**
攻击者只需获取一个看似权限受限的Azure身份，即可利用RBAC超权限进行信息侦察，并进一步**窃取VPN密钥，实现对企业私有网络的渗透接入**。

攻击链大致流程如下：

1. 攻击者获取绑定有高危RBAC角色的身份凭据；
2. 利用“\*/read”权限，**枚举VPN网关配置**，并调用存在漏洞的API接口**提取预共享密钥**；
3. 借助该密钥，攻击者可构造**伪造的站点到站点VPN连接**，直接加入企业私网，继而访问与该网关连接的**云端资源与本地系统**。

微软已确认VPN接口漏洞，并将其评级为“重要”，向研究人员发放了**7,500美元漏洞赏金**；
但对于RBAC权限过大的问题，微软仅将其标记为“低危”，**选择更新文档说明而非修复权限设计缺陷**。

这引发了业界对**云平台最小权限原则落实不力**的广泛关注。对于使用Azure混合云架构的组织而言，应**及时审计RBAC角色权限**，关注API接口权限边界，防止低权限身份成为攻击跳板。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/azure-api-vulnerabilities-leak-vpn-keys-and-built-in-roles/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309498](/post/id/309498)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/azure-api-vulnerabilities-leak-vpn-keys-and-built-in-roles/)

如若转载,请注明出处： <https://cybersecuritynews.com/azure-api-vulnerabilities-leak-vpn-keys-and-built-in-roles/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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