---
title: 立即修补：Kubernetes RCE 漏洞允许完全接管 Windows 节点
url: https://www.anquanke.com/post/id/293971
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:38.944526
---

# 立即修补：Kubernetes RCE 漏洞允许完全接管 Windows 节点

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

# 立即修补：Kubernetes RCE 漏洞允许完全接管 Windows 节点

阅读量**106038**

发布时间 : 2024-03-14 19:02:38

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/cloud-security/patch-now-kubernetes-flaw-allows-for-full-takeover-of-windows-nodes>

译文仅供参考，具体内容表达以及含义原文为准。

广泛使用的 Kubernetes 容器管理系统中的一个安全漏洞允许攻击者在 Windows 端点上以系统权限远程执行代码，从而可能导致完全接管Kubernetes 集群内的所有 Windows 节点。

Akamai 安全研究员 Tomer Peled 发现了该漏洞，该漏洞的编号为 CVE-2023-5528，CVSS 评分为 7.2。他在3 月 13 日发布的博客文章中解释说，漏洞利用在于操纵 Kubernetes 卷，该功能旨在支持集群上 pod 之间的数据共享，或将数据持久存储在 pod 的生命周期之外。

根据该缺陷的 GitHub 列表，作为攻击媒介，攻击者需要在 Windows 节点上创建 Pod 和持久卷，这将使他们能够升级到这些节点上的管理员权限。

Peled 告诉 Dark Reading：“利用此漏洞非常容易，因为攻击者只需要修改一个参数并应用 3 个 YAML 文件即可通过 Windows 端点获得 RCE。” 他在帖子中写道，Kubernetes 框架“基本上所有事情都使用 YAML 文件”。

Kubernetes 集群仅在使用 Windows 树内存储插件时才会受到影响；然而，佩莱德在帖子中指出，“开发人员可以使用许多不同的卷类型”，从而创建不同的攻击场景。

运行本地部署和 Azure Kubernetes 服务的 1.28.4 版本之前的 Kubernetes 默认安装容易受到攻击。Kubernetes 团队已收到有关该缺陷的警报，并且有一个补丁可用于修复，强烈推荐使用该补丁。

Peled 写道：“由于问题出在源代码中，因此这种威胁将仍然活跃，并且对它的利用可能会增加——这就是为什么我们强烈建议修补你的集群，即使它没有任何 Windows 节点。”

**追随缺陷**

Peled 在调查另一个漏洞后发现了该缺陷，该漏洞具有相同的根本原因：不安全的函数调用和 Kubernetes 中缺乏用户输入清理。该缺陷是CVE-2023-3676，这是一个命令注入漏洞，可以通过将恶意 YAML 文件应用到集群来利用。该漏洞的发现导致了另外两个漏洞的发现，这两个漏洞也是由于 YAML 文件中的 subPath 参数缺乏清理而导致的，这会创建带有卷的 pod，并为恶意代码注入提供了机会。

Peled 解释说：“在研究的最后，我们注意到代码中的一个潜在位置看起来可能会导致另一个命令注入漏洞”，该漏洞最终成为 CVE-2023-5528。

“经过多次尝试，我们成功实现了类似的结果：作为 kubelet 服务（系统权限）执行命令，”他写道。

**漏洞利用和修补**

研究人员执行的概念验证主要针对本地卷，这是 Kubernetes 中的卷类型之一。在创建包含本地卷的 pod 时，kubelet 服务最终将通过命令行调用“exec.command”到达一个函数，从而在节点上的卷位置和 pod 内的位置之间创建符号链接。

与许多终端一样，Windows 的命令提示符 (cmd) 允许依次执行两个或多个命令，以及在同一命令行中执行多个命令。“我们可以控制 cmd 执行中的参数之一，这意味着我们可以使用命令注入，”Peled 解释道。

在本地卷上实现此目的有一些先决条件，包括需要指定或创建持久卷等。然而，一旦创建了该卷，“用户就可以使用 permanentVolumeClaim 请求存储空间，”他写道。“这是可以注射的地方。”

针对该缺陷创建的补丁通过删除 cmd 调用并将其替换为将执行相同操作来创建符号链接的本机 GO 函数来消除注入的机会。“现在，GO ‘os’ 库将只执行符号链接操作，正如最初的预期，”他解释道。

**您的系统容易受到攻击吗？**

Kubernetes已成为使用最广泛的容器开源系统之一；然而，由于其被利用和访问组织数据的巨大潜力，它也已成为威胁行为者的主要目标。此外，Kubernetes 配置本身通常会创建一个易受攻击的安装，为威胁行为者提供了广泛的攻击面。

“Kubernetes 是一个非常复杂且强大的工具，”Peled 说。“一方面，它的稳健性允许用户根据组织的需求定制体验，但另一方面，从开发人员或用户的角度来看，它很难确保其各个方面的安全。”

事实上，CVE-2023-5528 及其相关缺陷的发现凸显了部署 Kubernetes 的企业“验证 Kubernetes 配置 YAML 的重要性，因为 Kubernetes 本身及其 sidecar 项目的多个代码区域缺乏输入清理，”Peled 写道。

他告诉 Dark Reading，遵循基于角色的访问控制 (RBAC) 等最佳实践并确保集群是最新的也“应该可以缓解大部分已知威胁”。

运行 Kubernetes 的企业环境仅当系统版本早于 1.28.4 并且系统运行 Windows 节点时才容易被利用。如果是这种情况，Akamai 提供了一个命令供管理员运行以确定是否应该对系统进行修补。如果是这样，应优先考虑修补。

“如果你的 Kubernetes 集群没有任何 Windows 节点，你不必急于修补这个特定的漏洞，”Peled 指出。“但无论如何，当你有时间的时候修补它很重要。”

如果无法立即修补，Akamai 还提供开放策略代理 (OPA) 规则来帮助检测和阻止此类行为。OPA 是一个开源代理，允许用户接收进出节点的流量数据，并对接收到的数据采取基于策略的操作。

本文翻译自 [原文链接](https://www.darkreading.com/cloud-security/patch-now-kubernetes-flaw-allows-for-full-takeover-of-windows-nodes)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293971](/post/id/293971)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/patch-now-kubernetes-flaw-allows-for-full-takeover-of-windows-nodes>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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