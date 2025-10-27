---
title: NTLM中继攻击死灰复燃，域环境安全面临严峻挑战
url: https://www.anquanke.com/post/id/309488
source: 安全客-有思想的安全新媒体
date: 2025-07-08
fetch_date: 2025-10-06T23:18:11.762958
---

# NTLM中继攻击死灰复燃，域环境安全面临严峻挑战

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

# NTLM中继攻击死灰复燃，域环境安全面临严峻挑战

阅读量**40620**

发布时间 : 2025-07-07 15:48:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elad Shamir，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/07/04/ntlm-relay-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

NTLM中继攻击是攻击者入侵域内主机的最简单途径之一。尽管许多安全从业者认为NTLM中继问题已被解决，事实并非如此——实际上，这种攻击可能正变得更加频繁。根据笔者所在公司的咨询部门观察，NTLM中继攻击在近几年内已成为最常见的攻击手段之一。

**由于大多数环境仍然存在漏洞，NTLM为横向移动和权限提升奠定了基础。这类攻击起源于“已认证用户”，且往往能够触及域环境的“Tier Zero”高权限层级，导致极大安全暴露和严重影响。**

以下是对该攻击的基本原理、常见目标及防御措施的介绍。

### 基本原理

NTLM是一种源自1990年代的遗留认证协议。如今，Active Directory环境中更倾向于使用Kerberos作为认证协议，但当Kerberos不可用时，NTLM仍被广泛使用。许多软件硬编码调用NTLM认证包，而非使用封装了Kerberos和NTLM的Negotiate包，导致NTLM仍频繁被使用。

NTLM认证流程涉及三个消息：Negotiate（协商）、Challenge（质询）和Authenticate（认证）。客户端向服务器发送请求启动认证，服务器返回随机质询，客户端回复包含加密凭据的响应。该机制确保每次认证尝试均唯一，防止重放攻击——即攻击者截获并重放有效认证消息以冒充客户端。

### NTLM中继攻击问题

NTLM的主要安全漏洞在于其易受中继攻击。攻击者可简单地在客户端和服务器间转发NTLM消息，直到服务器为客户端建立会话，令攻击者能够执行客户端具备的任何操作。中继攻击无需破解密码或依赖弱密码，因而成为极易实施的攻击手段。

有人可能质疑，此攻击是否依赖受害者在特定时刻主动认证？其实并非如此。中继攻击可与认证强制攻击（如Printer Bug或PetitPotam漏洞）结合，强迫受害者立即发起认证请求。所有“已认证用户”都可执行这类强制认证，因此任何人都能发起中继攻击。

### 攻击目标及后续步骤

NTLM中继攻击常见的三类目标如下，针对每类的后续动作与防护措施各不相同：

1. **SMB服务器**：成功中继攻击可建立与SMB服务器的会话。攻击者下一步取决于受害者权限，如访问C$或ADMIN$共享，远程注册表导出LSA机密（含计算机账户密码），或通过服务控制管理器横向移动。常见场景包括强制SCCM站点服务器认证并中继至SCCM数据库服务器，实现整个层级的接管。大多数Windows主机，尤其是服务器，都易受此攻击。微软正在努力缓解，从Windows Server 2008开始的域控制器以及Windows Server 2025和Windows 11开始的所有Windows主机默认启用SMB签名防护中继攻击，但旧版本默认关闭，且多数组织未做修改。
2. **LDAP或LDAPS**：相比SMB，LDAP中继更复杂但更有价值。当前多数域控制器通过LDAP通道仍易受中继攻击。LDAP服务器支持LDAP签名和通道绑定防护中继，但默认未强制执行，且多数组织未更改设置。需注意这些为域控制器级别设置，不同域控制器配置可能不同。好消息是，Windows Server 2025中域控制器默认启用LDAP SASL绑定的加密（封装）功能，逐步降低LDAP中继攻击风险。
3. **ADCS Web注册（ESC8）**：中继至ADCS比SMB复杂得多，因证书滥用条件苛刻，但中继逻辑仍相对简单。中继ADCS Web注册能让攻击者为受害者获取证书，进而冒充其身份。该漏洞由安全专家Will Schroeder和Lee Chagolla-Christensen发现并发布在Certified Pre-Owned白皮书中。如果证书颁发机构易受中继攻击，所有可注册相关证书的计算机均面临风险。默认的“Machine”证书模板即满足攻击条件，暴露全域内计算机。

###

NTLM中继攻击流程虽复杂，涉及多个环节，但只要攻击者熟悉手法，攻击速度快且实施简单。作为红队成员，我可以说这是攻击AD环境时的核心利器。如果环境中存在允许这些攻击的条件，安全风险极高。

微软正着手多个缓解措施，包括未来默认禁用NTLM，但这至少还需数年。近期最有效的防御措施是确保所有服务器强制启用签名和通道绑定。考虑到部分服务器可能不支持这些功能，建议针对具体服务器有选择地执行。建议持续评估环境中NTLM中继风险，优先保护高暴露目标。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/07/04/ntlm-relay-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309488](/post/id/309488)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/07/04/ntlm-relay-attacks/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/07/04/ntlm-relay-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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