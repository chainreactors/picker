---
title: 紧急关注：Windows Active Directory 域漏洞致攻击者权限提升危机
url: https://www.anquanke.com/post/id/306338
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:06.278149
---

# 紧急关注：Windows Active Directory 域漏洞致攻击者权限提升危机

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

# 紧急关注：Windows Active Directory 域漏洞致攻击者权限提升危机

阅读量**67540**

发布时间 : 2025-04-10 10:17:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/windows-active-directory-domain-vulnerability-let-attackers-escalate-privileges/>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft 披露了 Active Directory Domain Services 中存在的一个重大安全漏洞，该漏洞可能使攻击者将其权限提升至系统级别，从而有可能完全控制受影响的系统。

这个被追踪编号为 CVE-2025-29810 的漏洞，已作为 Microsoft 2025 年 4 月 “补丁星期二” 安全更新周期的一部分被修复。

安全研究人员将该漏洞归类为 “重要” 级别，其通用漏洞评分系统（CVSS）评分为 7.5，不过Microsoft  指出，目前在现实中利用该漏洞进行攻击的可能性似乎不大。

**Windows Active Directory 域漏洞**

该漏洞源于 Windows Active Directory 域服务中不当的访问控制机制，具体属于常见弱点枚举（CWE）中的 CWE-284 弱点分类。

根据 Microsoft 的安全公告，攻击者要成功利用该漏洞，需先在网络上拥有低级别的权限，然后才能尝试利用此漏洞。

攻击途径基于网络，但攻击复杂度较高，这意味着潜在攻击者在实施攻击前，需要收集特定于目标环境的信息，并对目标网络做好准备工作。

该漏洞的 CVSS 向量字符串为 “CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C”，表明这是一种网络攻击途径，攻击复杂度高，利用漏洞所需权限低，且无需用户交互。

该漏洞对保密性、完整性和可用性这三个安全方面均有影响，且在每个方面的评级均为 “高”。

以下是该漏洞的概要信息：

|  |  |
| --- | --- |
| ****风险因素**** | ****详情**** |
| 受影响产品 | Windows 活动目录域服务 |
| 影响 | 权限提升 |
| 利用漏洞的前提条件 | – 基于网络的攻击  – 高攻击复杂度  – 所需权限低  – 无需用户交互 |
| CVSS 评分 | 7.5（重要） |

**利用潜力**

安全分析师指出，尽管该漏洞很严重，但由于利用它存在一定复杂性，Microsoft 将其可利用性归类为 “可能性较低”。

成功利用这一漏洞的攻击者可以将其权限提升至系统（SYSTEM）级别，基本上能够完全控制被入侵的系统。

该漏洞似乎涉及对 Active Directory 内部身份验证机制的操纵，不过 Microsoft  并未公布具体的技术细节，以免为潜在攻击者提供可乘之机。

Microsoft 已在其 4 月的安全更新周期中为大多数受影响的系统发布了补丁。然而，根据安全公告，适用于基于 x64 系统的 Windows 10 和 32 位系统的 Windows 10 的更新暂未立即推出，将 “尽快” 发布。

Digital Fortress Institute 的网络安全研究员 Jane Marshall 博士表示：“对于部署了Active Directory 的企业环境而言，这个漏洞存在重大风险。”

“尽管利用该漏洞的复杂度较高，但考虑到潜在影响巨大，各组织应优先进行补丁更新。”

****对系统管理员的建议****

安全专家建议系统管理员立即采取以下措施：

1.尽快为域控制器和成员服务器应用可用补丁。

2.监控网络流量，留意可疑的身份验证尝试。

3.在整个域环境中实施最小权限原则。

4.关注 Microsoft  即将为目前尚未有补丁的 Windows 10 系统发布的更新。

该漏洞是由安全研究员 Matthieu Buffet 发现并通过协调漏洞披露机制报告给 Microsoft 的。

Microsoft 已确认，在补丁发布之前，没有证据表明该漏洞已被公开披露或在攻击中被利用。

这一事件凸显了在企业目录服务中建立恰当访问控制机制的持续重要性，以及及时进行安全补丁更新的关键意义，尤其是对于像 Active Directory 域服务这样的核心基础架构组件而言。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/windows-active-directory-domain-vulnerability-let-attackers-escalate-privileges/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306338](/post/id/306338)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/windows-active-directory-domain-vulnerability-let-attackers-escalate-privileges/)

如若转载,请注明出处： <https://cybersecuritynews.com/windows-active-directory-domain-vulnerability-let-attackers-escalate-privileges/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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