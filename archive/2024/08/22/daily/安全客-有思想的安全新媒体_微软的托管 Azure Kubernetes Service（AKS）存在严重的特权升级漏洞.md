---
title: 微软的托管 Azure Kubernetes Service（AKS）存在严重的特权升级漏洞
url: https://www.anquanke.com/post/id/299350
source: 安全客-有思想的安全新媒体
date: 2024-08-22
fetch_date: 2025-10-06T18:01:23.273982
---

# 微软的托管 Azure Kubernetes Service（AKS）存在严重的特权升级漏洞

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

# 微软的托管 Azure Kubernetes Service（AKS）存在严重的特权升级漏洞

阅读量**64223**

发布时间 : 2024-08-21 14:10:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/application-security/azure-kubernetes-bug-lays-open-cluster-secrets>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft 解决了其托管的 Azure Kubernetes 服务 （AKS） 中的一个严重权限提升漏洞，该漏洞允许攻击者访问群集使用的各种服务的凭据。

Mandiant在本周的一份报告中表示，攻击者可能利用此问题在受影响的AKS集群中访问敏感信息，窃取数据并执行其他恶意操作。该公司已经发现并向Microsoft报告了该漏洞。

## 无需特权

该漏洞影响了使用 Azure CNI 和 Azure 网络策略网络配置设置的 AKS 群集。Mandiant 表示，在受影响的 AKS 集群的任何 pod 中具有命令执行权限的攻击者可能利用该漏洞下载节点的配置详细信息，包括在 Kubernetes 节点初始设置期间使用的 TLS 引导令牌。这些令牌将允许攻击者执行 TLS 引导攻击并生成合法的 kubelet 证书，这将赋予他们在集群中提升的权限并未经授权访问其所有内容。

值得注意的是，攻击者可以在不需要任何特殊权限的情况下利用该漏洞，Mandiant说。“这次攻击不需要 pod 在 hostNetwork 设置为 true 的情况下运行，也不需要 pod 以 root 身份运行，”Mandiant 研究人员 Nick McClendon、Daniel McNamara 和 Jacob Paullus 在本周的一篇博客文章中写道。

## 未记录的 WireServer 组件

Mandiant 在 Microsoft 修复该漏洞之前发现该漏洞源于在 AKS pod 上具有命令执行权限的攻击者访问名为 WireServer 的未记录的 Azure 组件的能力。Mandiant 研究人员发现，通过遵循 CyberCX 于 2023 年 5 月发布的攻击技术，他们可以从 WireServer 恢复集群的 TLS 引导令牌。“获得对WireServer和HostGAPlugin端点的访问权限，攻击者可以检索和解密提供给许多扩展的设置，包括’自定义脚本扩展‘，这是一种用于为虚拟机提供初始配置的服务，”Mandiant研究人员写道。

他们将这个问题描述为当组织部署 Kubernetes 集群而不考虑在 pod 中拥有代码执行权限的攻击者如何能够利用该访问权限时会发生什么。攻击者可以通过多种方式接管 Pod，包括利用 Pod 中运行的应用程序中的漏洞、在持续集成过程中或通过被入侵的开发人员帐户。

## 过度访问

如果没有细粒度的网络策略、对不安全工作负载的限制以及对内部服务的身份验证要求，有权访问 Kubernetes 集群中 Pod 的攻击者可以访问 Kubernetes 集群上的其他 Pod 和服务。这包括包含配置详细信息、实例元数据以及集群内以及其他云服务的服务的凭据的服务器。

Mandiant说：“采用一种流程来创建限制性NetworkPolicies，只允许访问所需的服务，可以防止整个攻击类别。“当根本无法访问该服务时，可以防止通过未记录的服务进行权限提升。”

Critical Start网络威胁研究高级经理Callie Guenther表示，尽管Microsoft已经修补了这个问题，但安全团队必须立即审核他们的AKS配置。如果他们使用 Azure CNI 进行网络配置，使用 Azure 进行网络策略，则尤其如此，Guenther 在一封电子邮件评论中说。Guenther 指出：“他们还应该轮换所有 Kubernetes 密钥，执行严格的 pod 安全策略，并实施强大的日志记录和监控以检测任何可疑活动。“虽然这个漏洞很严重，需要立即采取行动，但它是第二阶段的攻击，这意味着它需要事先访问pod。因此，应该在组织威胁形势的更广泛背景下相应地确定其优先级。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/application-security/azure-kubernetes-bug-lays-open-cluster-secrets)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299350](/post/id/299350)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/application-security/azure-kubernetes-bug-lays-open-cluster-secrets)

如若转载,请注明出处： <https://www.darkreading.com/application-security/azure-kubernetes-bug-lays-open-cluster-secrets>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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

* [无需特权](#h2-0)
* [未记录的 WireServer 组件](#h2-1)
* [过度访问](#h2-2)

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