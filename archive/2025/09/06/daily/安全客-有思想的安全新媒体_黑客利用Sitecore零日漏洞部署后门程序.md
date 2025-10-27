---
title: 黑客利用Sitecore零日漏洞部署后门程序
url: https://www.anquanke.com/post/id/311903
source: 安全客-有思想的安全新媒体
date: 2025-09-06
fetch_date: 2025-10-02T19:43:00.860104
---

# 黑客利用Sitecore零日漏洞部署后门程序

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

# 黑客利用Sitecore零日漏洞部署后门程序

阅读量**428388**

发布时间 : 2025-09-05 18:27:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-exploited-sitecore-zero-day-flaw-to-deploy-backdoors/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

威胁行为者一直在利用旧版 Sitecore 部署中的零日漏洞来部署 **WeepSteel** 侦察恶意软件。

该漏洞编号为 **CVE-2025-53690**，是一种 **ViewState** 反序列化漏洞，由 2017 年前的 Sitecore 指南中包含的示例 **ASP.NET** 机器密钥导致。

一些客户在生产环境中重复使用了此密钥，使得知晓该密钥的攻击者能够构造有效的恶意“**\_VIEWSTATE**”负载，诱骗服务器对其进行反序列化并执行，从而实现 **远程代码执行（RCE）**。

![]()

该漏洞并非 **ASP.NET** 本身的缺陷，而是由于重复使用公开文档中从未打算用于生产环境的密钥而造成的配置错误漏洞。

## 漏洞利用活动

发现野外恶意活动的 **Mandiant** 研究人员报告称，威胁行为者一直在多阶段攻击中利用该漏洞。

攻击者以“**/sitecore/blocked.aspx** ”端点为目标，该端点包含一个未经验证的 **ViewState** 字段，并通过利用 **CVE-2025-53690**，以 **IIS NETWORK SERVICE** 账户权限实现远程代码执行。

他们投放的恶意负载是 **WeepSteel**，这是一种侦察型后门，用于收集系统、进程、磁盘和网络信息，并将其数据窃取行为伪装成标准的 **ViewState** 响应。

![]()

Mandiant 观察到攻击者在已入侵环境中执行了侦察命令，包括 **whoami**、**hostname**、**tasklist**、**ipconfig /all** 和 **netstat -ano**。

在攻击的下一阶段，黑客部署了 **Earthworm（一种网络隧道和反向 SOCKS 代理）**、**Dwagent（远程访问工具）** 以及用于创建被盗数据档案的 **7-Zip**。

随后，他们通过创建本地管理员账户（**‘asp$’**、**‘sawadmin’**）、转储缓存的（**SAM 和 SYSTEM 配置单元**）凭据，以及尝试通过 **GoTokenTheft** 进行令牌模拟来提升权限。

攻击者通过禁用这些账户的密码过期策略、授予其 **RDP 访问权限**，并将 **Dwagent 注册为 SYSTEM 服务**，以确保持久化控制。

![]()

## 缓解 CVE-2025-53690

**CVE-2025-53690** 影响 **Sitecore Experience Manager (XM)**、**Experience Platform (XP)**、**Experience Commerce (XC)** 和 **Managed Cloud**（最高版本 9.0），当使用 2017 年前文档中包含的示例 **ASP.NET 机器密钥** 部署时会受影响。

**XM Cloud**、**Content Hub**、**CDP**、**Personalize**、**OrderCloud**、**Storefront**、**Send**、**Discover**、**Search** 和 **Commerce Server** 不受影响。

Sitecore 与 Mandiant 的报告协同发布了安全公告，警告使用静态机器密钥的多实例部署也面临风险。

对潜在受影响管理员的建议操作是：立即将 **web.config** 中所有静态 值替换为新的唯一密钥，并确保 **web.config** 内的 元素已加密。

一般而言，建议将定期轮换静态机器密钥作为持续的安全措施。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-exploited-sitecore-zero-day-flaw-to-deploy-backdoors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311903](/post/id/311903)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-exploited-sitecore-zero-day-flaw-to-deploy-backdoors/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-exploited-sitecore-zero-day-flaw-to-deploy-backdoors/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [漏洞利用活动](#h2-0)
* [缓解 CVE-2025-53690](#h2-1)

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