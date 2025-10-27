---
title: 三星 MagicINFO 9 服务器曝出 18 个严重漏洞（CVSS 最高达 9.8），恐致系统完全失控
url: https://www.anquanke.com/post/id/310590
source: 安全客-有思想的安全新媒体
date: 2025-07-26
fetch_date: 2025-10-06T23:16:53.012243
---

# 三星 MagicINFO 9 服务器曝出 18 个严重漏洞（CVSS 最高达 9.8），恐致系统完全失控

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

# 三星 MagicINFO 9 服务器曝出 18 个严重漏洞（CVSS 最高达 9.8），恐致系统完全失控

阅读量**71593**

发布时间 : 2025-07-25 16:50:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/18-serious-flaws-cvss-up-to-9-8-expose-samsung-magicinfo-9-servers-to-full-compromise/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员近日披露，三星广泛部署的数字标牌管理平台 **MagicINFO 9 Server** 存在**多达 18 个严重安全漏洞**，其中部分漏洞的 CVSS 评分高达 **9.8**。这些漏洞允许攻击者执行远程代码注入、上传 Web shell、绕过身份验证等高危攻击，可能导致服务器被完全接管。

所有漏洞均影响 MagicINFO 9 Server 21.1080.0 之前版本，安全专家强烈建议用户尽快升级补丁。

MagicINFO 是三星推出的数字标牌集中管理平台，广泛应用于零售、交通枢纽等场景，用于创建、调度、分发和监控屏幕内容。正因其部署范围广泛，这些漏洞的潜在风险尤为严重。

以下是本次披露漏洞的关键类别及代表性 CVE 编号和影响：

### **1. 远程代码执行（RCE）——通过文件上传**

多数漏洞与**服务端对文件类型检查不严**有关，攻击者可上传 .jsp、.exe 等可执行恶意文件，注入并远程执行任意代码。

涉及 CVE：

**• CVE-2025-54439**

**• CVE-2025-54444**

**• CVE-2025-54440**

**• CVE-2025-54441**

**• CVE-2025-54442**

**• CVE-2025-54448**

**• CVE-2025-54449**

CVSS 评分： 8.8–9.8（高危至严重）

### **2. 路径穿越 + Web Shell 上传**

3 个路径穿越漏洞可使攻击者将 Web Shell 上传至服务器执行目录，**实现远程访问控制**。

涉及 CVE：

**• CVE-2025-54438**

**• CVE-2025-54443**

**• CVE-2025-54446**

问题类型： **路径限制不当，允许跳出预期目录。**

### **3. 身份验证绕过 + 硬编码凭据**

两项漏洞涉及硬编码的账户凭据，可**直接绕过认证系统**：

涉及 CVE：

**• CVE-2025-54454（CVSS 9.1）**

**• CVE-2025-54455（CVSS 9.1）**

此外，**CVE-2025-54452（CVSS 7.3）** 也存在**身份验证机制缺陷**，可能被用于冒充合法用户。

### **4. XML 外部实体注入（XXE）和 SSRF**

**• CVE-2025-54445（CVSS 8.2）**

该漏洞**允许服务端请求伪造（SSRF）**，可能暴露内网服务或访问敏感文件。

### **5. 其他漏洞**

**CVE-2025-54450、CVE-2025-54453、CVE-2025-54451**

涉及**代码生成、路径处理**等多种问题，进一步扩大攻击面。

### **组合攻击路径示例：**

攻击者可先通过 CVE-2025-54454 **使用硬编码账号绕过认证**，再利用 CVE-2025-54438 执行路径穿越**上传 Web Shell**，最后结合 CVE-2025-54444 **实现远程代码执行**，取得高权限控制权。

对于将 MagicINFO 服务器暴露在公网，或连接至内网中含有敏感数据的组织而言，这一系列漏洞可能带来严重安全后果。

三星官方已发布安全更新，建议用户立即升级至 MagicINFO 9 Server v21.1080.0 或更高版本。

本文翻译自securityonline [原文链接](https://securityonline.info/18-serious-flaws-cvss-up-to-9-8-expose-samsung-magicinfo-9-servers-to-full-compromise/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310590](/post/id/310590)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/18-serious-flaws-cvss-up-to-9-8-expose-samsung-magicinfo-9-servers-to-full-compromise/)

如若转载,请注明出处： <https://securityonline.info/18-serious-flaws-cvss-up-to-9-8-expose-samsung-magicinfo-9-servers-to-full-compromise/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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