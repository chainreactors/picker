---
title: Oracle云代码编辑器曝RCE漏洞，允许攻击者上传恶意文件
url: https://www.anquanke.com/post/id/310236
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:39:01.065769
---

# Oracle云代码编辑器曝RCE漏洞，允许攻击者上传恶意文件

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

# Oracle云代码编辑器曝RCE漏洞，允许攻击者上传恶意文件

阅读量**86919**

发布时间 : 2025-07-18 17:36:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/oracle-cloud-code-editor-rce-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Oracle云基础设施（OCI）代码编辑器近日被披露存在一个严重的远程代码执行（RCE）漏洞，攻击者可通过用户的一次点击操作，静默劫持其 Cloud Shell 环境。

该漏洞目前已被修复，影响范围包括代码编辑器所集成的多个服务模块，如资源管理器（Resource Manager）、函数服务（Functions）和数据科学（Data Science），凸显了看似独立的云开发工具如何可能演变为攻击载体。

#### **要点概览**

1.Oracle Cloud 代码编辑器的文件上传功能缺乏跨站请求伪造（CSRF）防护，使得攻击者可通过“一键”方式上传恶意文件；

2. 该漏洞可实现远程代码执行，并可能危及多个 OCI 集成服务的安全；

3. Oracle 已通过强制要求使用 `X-CSRF-Token` 请求头来阻止跨域攻击。

### 漏洞分析

**该漏洞源于 Oracle 代码编辑器与 Cloud Shell 的深度集成：二者共享底层文件系统及用户会话上下文。这一设计缺陷使得攻击者可以在用户毫不知情的情况下，利用代码编辑器上传恶意文件至 Cloud Shell，并借助用户权限在环境中执行任意代码，从而完全控制受害者的云开发环境。**

尽管这种高度集成的设计初衷是为了为开发者提供无缝的使用体验，但实际上却无意中暴露出一个可被利用的攻击面，最终被安全研究人员发现并加以利用。

Tenable 的研究始于一个简单的问题：既然开发人员可以轻松地通过代码编辑器上传文件，那么攻击者是否也能做到？这一思路最终导致研究人员发现了代码编辑器中的一个 `/file-upload` 接口，该接口缺乏跨站请求伪造（CSRF）防护措施，这与 Cloud Shell 中已正确配置安全机制的上传接口形成鲜明对比。

![]()

此次漏洞的核心组件是 Cloud Shell 路由器（router.cloudshell.us-ashburn-1.oci.oraclecloud.com），该路由器接受包含 multipart/form-data 负载的 HTTP POST 请求。

该路由器使用了配置为 SameSite=None 属性的 CS-ProxyChallenge Cookie，未能对经过身份验证的用户发起的跨站请求提供有效防护。

利用路径非常直接。攻击者可以创建恶意的 HTML 页面，当经过身份验证的 OCI 用户访问该页面时，恶意文件会在用户不知情的情况下自动上传至其 Cloud Shell 环境。

此次攻击采用了精心构造的 HTTP 请求：

![]()

研究人员演示了攻击者如何覆盖 `.bashrc` 文件，从而建立反向 shell，获得对 Cloud Shell 的交互式访问权限，并利用受害者的凭据通过 OCI CLI 实现对 OCI 服务的横向移动。

### **防护措施**

**针对该漏洞，Oracle 采取了额外的安全措施，特别是要求所有相关请求必须携带自定义 HTTP 头 `x-csrf-token`，其值为 `csrf-value`。**

此项改动有效防止了 CSRF 攻击，因为浏览器在跨源请求时无法自动附加自定义请求头，除非存在正确的 CORS 配置。

该漏洞的影响不仅限于 Cloud Shell，还波及到 Code Editor 的集成服务。由于这些服务运行在相同的共享文件系统上，恶意负载可能会影响 Resource Manager 工作区、Functions 部署以及 Data Science 环境，形成覆盖 OCI 开发者工具包的多重攻击面。

此次事件凸显了云服务集成所带来的安全挑战，便利性功能在无意间扩大了攻击面，超出了其原本的设计范围。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/oracle-cloud-code-editor-rce-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310236](/post/id/310236)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/oracle-cloud-code-editor-rce-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/oracle-cloud-code-editor-rce-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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