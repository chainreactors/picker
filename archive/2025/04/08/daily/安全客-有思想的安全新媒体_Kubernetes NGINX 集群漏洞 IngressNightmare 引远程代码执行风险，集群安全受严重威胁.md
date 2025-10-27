---
title: Kubernetes NGINX 集群漏洞 IngressNightmare 引远程代码执行风险，集群安全受严重威胁
url: https://www.anquanke.com/post/id/306227
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:47.667219
---

# Kubernetes NGINX 集群漏洞 IngressNightmare 引远程代码执行风险，集群安全受严重威胁

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

# Kubernetes NGINX 集群漏洞 IngressNightmare 引远程代码执行风险，集群安全受严重威胁

阅读量**55235**

发布时间 : 2025-04-07 09:54:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/ingressnightmare/>

译文仅供参考，具体内容表达以及含义原文为准。

最近发现的一组被称为 IngressNightmare 的漏洞，存在于 Ingress NGINX Controller 中，使得集群面临未经身份验证的远程代码执行（RCE）风险。Kubernetes 在容器编排领域占据主导地位，但其重要性也使其成为了被攻击利用的目标。

在 Kubernetes 中，Ingress 充当着一个复杂的流量管理系统，允许外部访问内部服务。它由两个核心组件组成：

****1.********Ingress 资源****：这些资源基于主机名、路径或其他标准来定义路由规则，通常在 YAML 配置文件中指定。

****2.********Ingress Controller****：这些控制器实现路由规则，通常使用反向代理或负载均衡器。

基于流行的 NGINX Web 服务器构建的 Ingress NGINX Controller，是部署最为广泛的选项之一，在 GitHub 上获得了超过 18000 个星标。

这些漏洞可能会让攻击者破坏整个 Kubernetes 环境。在 Kubernetes 中，Ingress 通过 Ingress 资源（即通过主机名或路径定义路由规则的 YAML 文件）和 Ingress Controller（如 NGINX 变体，它通过反向代理实施这些规则）来管理外部到内部服务的流量。

例如，一个 YAML 文件可能会将 example.com/ 定向到前端服务，将 example.com/api 定向到后端服务。尽管这个系统功能多样，但一旦被利用，就会存在漏洞。

****IngressNightmare 四个关键漏洞****

IngressNightmare 包含了 Ingress NGINX Controller 的准入 Webhook（用于验证 Ingress 对象）中的四个漏洞。这些漏洞影响 v1.11.0 之前的版本、v1.11.0 至 v1.11.4 版本以及 v1.12.0 版本，v1.11.5 和 v1.12.1 版本中已提供补丁。这些漏洞分别是：

****1.********CVE-2025-1097（身份验证 TLS 匹配 CN 注释注入）****：此漏洞允许攻击者通过 auth-tls-match-cn 注释注入恶意配置，绕过身份验证检查。它可以操纵 TLS 验证，有可能暴露敏感数据或为进一步的攻击创造条件（通用漏洞评分系统（CVSS）评分为 8.8）。

****2.********CVE-2025-1098（镜像 UID 注入）****：通过利用与镜像相关的注释（mirror-target 或 mirror-host）或 UID 操纵，攻击者可以注入任意配置。这可能会重定向流量或执行未经授权的操作，损害集群的完整性（CVSS 评分为 8.8）。

****3.********CVE-2025-24514（身份验证 URL 注释注入）****：这个漏洞针对 auth-url 注释，允许攻击者注入控制器会处理的恶意 URL。这可能导致未经授权的访问，或成为更广泛攻击的入口点（CVSS 评分为 8.8）。

****4.********CVE-2025-1974（NGINX 配置代码执行）****：这是最严重的漏洞，通过利用 NGINX 配置验证，使得未经身份验证的远程代码得以执行。攻击者注入在 nginx -t 测试期间执行的代码，从而获得对集群机密的访问权限并实现完全控制（CVSS 评分为 9.8）。

成功利用这些漏洞可能会暴露所有机密信息、实现横向移动，甚至导致集群被接管。

****攻击是如何进行的？****

IngressNightmare 攻击通过多个阶段利用这些漏洞。首先是发现阶段，攻击者使用诸如 Shodan 之类的工具扫描暴露的控制器。

然后，他们精心构造一个恶意的 Ingress 对象，将有害的 NGINX 指令嵌入到诸如 auth-url 或 auth-tls-match-cn 之类的注释中。

这个对象作为未经身份验证的准入审查请求发送到 Webhook，利用了 Webhook 缺乏身份验证的缺陷。

根据报告，控制器生成一个包含注入代码的 NGINX 配置，并且在使用 nginx -t 进行验证期间，诸如加载恶意库之类的恶意指令会被执行，从而实现远程代码执行。凭借控制器的权限，攻击者可以访问机密信息、进行横向移动，并有可能控制整个集群。

****缓解策略****

使用以下命令检查存在漏洞的 Pod：

kubectl get pods –all-namespaces –selector app.kubernetes.io/name=ingress-nginx

通过 kubectl describe pod 命令验证版本。如果存在风险，使用以下命令升级到 v1.11.5 或 v1.12.1 版本：

helm upgrade ingress-nginx ingress-nginx/ingress-nginx –version <patched-version>

如果无法立即打补丁，可以使用网络策略限制 Webhook 的访问，或者通过设置 controller.admissionWebhooks.enabled=false（Helm）或删除 ValidatingWebhookConfiguration 来禁用它。

Ingress 还存在一些操作方面的问题：SSL 错误需要对机密信息和 DNS 进行验证；路由问题需要检查日志和端点；性能瓶颈可以通过扩展副本数量以及调整代理设置（如 proxy-buffer-size: “8k”）来解决。

IngressNightmare 揭示了 Kubernetes 容易受到复杂攻击的现状。鉴于已有补丁和缓解措施可用，各组织必须优先确保其集群的安全。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/ingressnightmare/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306227](/post/id/306227)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/ingressnightmare/)

如若转载,请注明出处： <https://cybersecuritynews.com/ingressnightmare/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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