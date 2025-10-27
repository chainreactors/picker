---
title: Kubernetes 集群安全漏洞遭利用，算力资源面临严重危机
url: https://www.anquanke.com/post/id/306888
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:03:58.450195
---

# Kubernetes 集群安全漏洞遭利用，算力资源面临严重危机

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

# Kubernetes 集群安全漏洞遭利用，算力资源面临严重危机

阅读量**85938**

发布时间 : 2025-04-25 14:33:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-taking-advantage-of-unsecured-kubernetes-clusters/>

译文仅供参考，具体内容表达以及含义原文为准。

对于网络安全专业人士而言，出现了一个令人担忧的新情况：威胁行为者正越来越多地将目标对准未受安全保护的 Kubernetes 集群，以便在受害者组织毫不知情的情况下，利用其计算资源来部署加密货币挖矿活动。

这些攻击利用了容器化环境中的漏洞，尤其侧重于利用配置错误和薄弱的身份验证机制，这些漏洞使得攻击者能够未经授权访问 Kubernetes 基础设施。

攻击通常始于通过密码喷洒技术窃取凭据，随后会创建未经授权的资源组和容器部署。

一旦威胁行为者获得了对 Kubernetes 集群的访问权限，他们就可以部署大量专门用于加密货币挖矿活动的容器，从而有效地将一个组织的计算资源转化为攻击者的盈利资产。

在过去的一年里，出现了一个特别值得关注的案例，攻击者对教育领域的云租户发动了复杂的密码喷洒攻击。

这些攻击涉及使用一个名为 AzureChecker.exe 的命令行界面工具，该工具会连接到恶意域名，以下载包含用于密码喷洒操作的目标信息的 AES 加密数据。

Microsoft的研究人员确定，在这些攻击背后有一个被追踪代号为 Storm-1977 的威胁组织。

在分析攻击方法时，Microsoft威胁情报部门观察到，该工具接受一个名为 accounts.txt 的文件作为输入，该文件包含用户名和密码组合，然后这些组合会被用于对目标租户进行验证。

在一个有记录的事件中，研究人员目睹了一起成功的账户被攻破事件，威胁行为者利用一个来宾账户在被攻破的订阅中创建了一个资源组。

在获得初始访问权限后，攻击者接着在该资源组内创建了 200 多个容器，并专门为加密货币挖矿操作对它们进行了配置。

****通过 Kubernetes 审计检测攻击****

检测这些加密货币挖矿操作的一个关键因素是了解 Kubernetes 审计日志中出现的独特模式。

当威胁行为者部署他们的挖矿基础设施时，他们通常需要特权访问权限，这会在集群的审计跟踪记录中留下可识别的痕迹。

安全团队可以实施特定的追踪查询，以识别诸如特权 Pod 部署之类的可疑活动。

例如，以下查询可以检测到特权容器的创建，这是加密货币挖矿操作的一个常见需求：

CloudAuditEvents

where Timestamp > ago(1d)

where DataSource == “Azure Kubernetes Service”

where OperationName == “create”

where RawEventData.ObjectRef.resource == “pods”

where RawEventData.ResponseStatus.code startswith “20”

extend PodName = RawEventData.RequestObject.metadata.name

extend PodNamespace = RawEventData.ObjectRef.namespace

mv-expand Container = RawEventData.RequestObject.spec.containers

extend ContainerName = Container.name

where Container.securityContext.privileged == “true”

针对 Kubernetes 环境的攻击路径展示了威胁行为者是如何从初始访问逐步发展到部署加密货币挖矿操作的。

建议各组织实施强大的安全措施，包括适当的身份验证控制、网络流量限制，以及对容器化环境进行持续监控，以便在这些威胁建立起加密货币挖矿操作之前就识别并缓解它们。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-taking-advantage-of-unsecured-kubernetes-clusters/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306888](/post/id/306888)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-taking-advantage-of-unsecured-kubernetes-clusters/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-taking-advantage-of-unsecured-kubernetes-clusters/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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