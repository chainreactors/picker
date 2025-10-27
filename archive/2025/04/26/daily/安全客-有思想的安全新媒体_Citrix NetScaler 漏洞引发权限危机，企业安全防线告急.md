---
title: Citrix NetScaler 漏洞引发权限危机，企业安全防线告急
url: https://www.anquanke.com/post/id/306870
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:04.904891
---

# Citrix NetScaler 漏洞引发权限危机，企业安全防线告急

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

# Citrix NetScaler 漏洞引发权限危机，企业安全防线告急

阅读量**76479**

发布时间 : 2025-04-25 10:21:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/citrix-netscaler-console-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

Citrix NetScaler Console存在一个严重漏洞，尽管该漏洞最初仅被归类为 “敏感信息泄露” 问题，但实际上它允许未经身份验证的用户获得完全的管理员访问权限。

概念验证（PoC）的利用代码已被发布，攻击者能够通过利用内部应用程序编程接口（API）的漏洞来创建管理员账户。

Citrix 最初于 2024 年 7 月 10 日披露了 CVE-2024-6235 漏洞。该漏洞的通用漏洞评分系统第 4 版（CVSSv4）评分为 9.4 分，表明其严重程度极高。

虽然最初该漏洞仅被简单描述为 “NetScaler Console 中的敏感信息泄露”，但来自 Rapid7 公司的安全研究员 chutton-r7 揭示称，其影响要严重得多。它使得未经身份验证的攻击者能够获得对受影响系统的完全管理员访问权限。

Rapid7 的分析证实：“该漏洞允许未经身份验证的攻击者从内部 API 获取管理员级别的会话 ID，并利用这个会话 ID 在系统上创建其他管理员用户。”

这实际上将该问题从信息泄露转变为了系统被完全攻破。

根据 Shodan 搜索引擎的搜索结果，大约有 318 个 NetScaler Console 实例仍暴露在互联网上，可能存在被利用的风险。

****严重的 NetScaler 管理员权限接管漏洞****

该漏洞存在于一个内部 API 端点，该端点会不当泄露管理员会话令牌。

通过向 /internal/v2/config/mps\_secret/ADM\_SESSIONID 发送带有特定请求头的简单 GET 请求，攻击者无需身份验证即可获取有效的会话令牌。

一旦攻击者获取了会话 ID，他们需要从 NetScaler 管理面板的 HTML 中检索一个名为 rand\_key 的额外参数。在拥有这两个参数后，攻击者就可以创建一个具有系统完全访问权限的新超级管理员账户。

PoC 脚本可实现这整个过程的自动化，包括从内部 API 检索会话 ID、获取所需的 rand\_key 参数，以及创建一个新的管理员用户。

|  |  |
| --- | --- |
| ****风险因素**** | ****详情**** |
| 受影响产品 | NetScaler Console 14.1 版本，14.1-25.53 版本之前的所有版本 |
| 影响 | 通过未经身份验证的会话劫持获取完全管理员访问权限 |
| 利用前提条件 | 攻击者必须能够访问 NetScaler Console的 IP 地址（无需身份验证） |
| CVSS 3.1 评分 | 9.4 分（严重） |

****受影响的系统及已发布的补丁****

该漏洞影响 NetScaler Console 14.1 版本中 14.1-25.53 版本之前的所有版本。

据报道，早期版本分支（13.1.x 和 12.1.x）不受影响。Citrix于 2024 年 7 月发布了补丁，修复了这个漏洞以及 NetScaler 产品中的其他安全问题。

安全专家建议立即将系统更新到 14.1-25.53 版本或更高版本，并建议不要将 NetScaler Console 实例暴露在公共互联网上。

企业机构应该实施强大的补丁管理策略，并通过网络分段和特权访问工作站来限制对管理界面的访问。

截至 2025 年 4 月 24 日，研究人员仍在持续监测该漏洞在实际环境中的被利用情况，对于仍在运行存在漏洞的 NetScaler Console 实例的企业机构来说，这个漏洞仍是一个重大隐患。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/citrix-netscaler-console-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306870](/post/id/306870)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/citrix-netscaler-console-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/citrix-netscaler-console-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**10赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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