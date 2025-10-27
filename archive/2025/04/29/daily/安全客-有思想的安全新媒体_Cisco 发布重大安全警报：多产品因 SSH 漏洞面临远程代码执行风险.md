---
title: Cisco 发布重大安全警报：多产品因 SSH 漏洞面临远程代码执行风险
url: https://www.anquanke.com/post/id/306932
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:26.992342
---

# Cisco 发布重大安全警报：多产品因 SSH 漏洞面临远程代码执行风险

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

# Cisco 发布重大安全警报：多产品因 SSH 漏洞面临远程代码执行风险

阅读量**89242**

发布时间 : 2025-04-28 09:35:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cisco-confirms-multiple-products-impacted/>

译文仅供参考，具体内容表达以及含义原文为准。

Cisco Systems 发布了一份重要的安全公告，确认其产品组合中的多款产品受到了 Erlang/OTP SSH 服务器（CVE-2025-32433）中的远程代码执行（RCE）漏洞的影响。

这一漏洞的最高 CVSSv3.1 评分为 10.0，它使得未经身份验证的攻击者能够通过在身份验证过程中利用对 SSH 消息的不当处理，在易受攻击的系统上执行任意代码。

该漏洞影响了从网络编排工具到企业路由平台等关键基础设施组件，并且概念验证性的攻击代码已经在安全社区中流传。

****Erlang SSH 服务器远程代码执行漏洞****

该漏洞存在于 Erlang/OTP 对 SSH 协议（RFC 4252）的实现中，具体是在成功身份验证之前对通道请求消息的处理过程中。

攻击者可以通过发送特制的 SSH 数据包来利用这一漏洞，这些数据包能够绕过身份验证检查，从而直接访问 Erlang 运行时系统。

这使得攻击者能够使用 SSH 服务账户（通常是根用户或管理员级用户）的权限来执行操作系统命令。

Cisco 的公告强调，利用这一漏洞无需进行身份验证（CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H），这使得面向互联网的系统特别容易受到攻击。

Erlang/OTP 平台的并发模型加剧了这种风险，因为单个被攻陷的 SSH 连接可能会在集群环境中的分布式节点上生成恶意进程。

****受影响的**** ****Cisco**** ****产品****

|  |  |
| --- | --- |
| ****风险因素**** | ****详情**** |
| 受影响产品 | 网络服务编排器、超云核心、智能节点管理器、催化剂中心、智能物理层、ConfD 和 ConfD 基础版 |
| 影响 | 远程代码执行（RCE） |
| 利用漏洞前提条件 | – 运行易受攻击的 Erlang/OTP 版本  – 启用并可访问 SSH 守护进程  – 无需身份验证或用户交互 |
| CVSS 3.1 评分 | 10.0（严重） |

Cisco 已确定有 18 个产品系列正在接受积极调查，已确认受影响的产品包括：

1.网络服务编排器（NSO）：对服务提供商的编排至关重要（CSCwo83796）

2.超云核心 – 订阅者微服务基础设施：5G 核心网络组件（CSCwo83747）

3.智能节点管理器 – 基于服务器或虚拟机的集中式应用程序

4.广域应用服务（WAAS）：加速和优化基础设施（正在调查中）

5.催化剂中心（前身为 DNA 中心）：企业网络管理枢纽（正在调查中）

值得注意的是，ConfD 和 ConfD 基础版网络自动化工具（CSCwo83759）存在漏洞，但由于配置防护措施，可避免受到远程代码执行的攻击。

已确认不受影响的产品包括 Cisco IOS XE 软件、安全防火墙管理中心和身份服务引擎。

Cisco 计划从 2025 年 5 月开始为 NSO 和 ConfD 等高优先级产品分阶段提供修复方案，不过大多数解决方案仍在开发中。

由于缺乏可行的解决方法，各机构不得不实施严格的网络控制措施，包括：

1.将管理接口与不可信网络进行隔离

2.实施防火墙规则，将 SSH 访问限制在可信的 IP 范围内

3.监控异常的身份验证模式

由于 Erlang/OTP 是关键基础设施组件的基础，这一漏洞给电信网络、云平台和企业 IT 环境带来了系统性风险。安全团队应：

1.对所有使用 Erlang/OTP 25.0 至 26.1 版本的系统进行审计

2.优先为面向互联网的 SSH 服务打补丁

3.实施运行时保护机制，以检测攻击模式

Cisco 的产品安全事件响应团队（PSIRT）确认正在积极监控该漏洞在现实中的被利用情况，不过截至 2025 年 4 月 24 日，尚未观察到恶意攻击活动。

这一事件是今年企业系统中出现的第三起与 SSH 相关的严重漏洞事件，突显了在分布式系统中进行协议级安全审计的必要性。

在各机构等待供应商提供补丁期间，重点转向了遏制策略和威胁搜寻行动，以识别潜在的攻击前活动。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cisco-confirms-multiple-products-impacted/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306932](/post/id/306932)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cisco-confirms-multiple-products-impacted/)

如若转载,请注明出处： <https://cybersecuritynews.com/cisco-confirms-multiple-products-impacted/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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