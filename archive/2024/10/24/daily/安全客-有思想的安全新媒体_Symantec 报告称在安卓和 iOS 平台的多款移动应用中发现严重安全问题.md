---
title: Symantec 报告称在安卓和 iOS 平台的多款移动应用中发现严重安全问题
url: https://www.anquanke.com/post/id/301178
source: 安全客-有思想的安全新媒体
date: 2024-10-24
fetch_date: 2025-10-06T18:46:11.241482
---

# Symantec 报告称在安卓和 iOS 平台的多款移动应用中发现严重安全问题

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

# Symantec 报告称在安卓和 iOS 平台的多款移动应用中发现严重安全问题

阅读量**56042**

发布时间 : 2024-10-23 15:23:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/hardcoded-cloud-credentials-found-in-popular-mobile-apps-a-major-security-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![23andMe Data Leak]()

Symantec最近发布的一份报告称，在安卓和 iOS 平台上广泛使用的几款移动应用程序中发现了一个严重的安全问题。这些应用程序被发现包含硬编码的云服务凭据，使用户和后端服务面临重大安全风险。

报告显示，几款流行的移动应用程序在其源代码中包含了硬编码和未加密的亚马逊网络服务（AWS）和微软 Azure 凭据。这种危险的做法意味着，获得应用程序二进制代码或源代码访问权限的攻击者可以轻松提取这些凭据，从而在未经授权的情况下访问云资源、用户数据和后端基础设施。

一个特别令人担忧的例子是 Pic Stitch： 拼贴制作应用在 Google Play 商店的下载量超过 500 万次。该应用程序的源代码包含硬编码的 AWS 凭据，这些凭据用于访问亚马逊 S3 存储桶，存在数据被盗或被篡改的重大风险。正如报告中指出的，“如果布尔标志设置为 true，应用程序就会加载生产凭证，包括生产的亚马逊 S3 存储桶名称、读写访问密钥和秘密密钥”，从而使它们容易被利用。

![Hardcoded Cloud Credentials]()
Pic Stitch 硬编码凭证代码 | 图片： Symantec

其他应用程序，如 Crumbl、Eureka： Eureka: Earn Money for Surveys》和《Videoshop – Video Editor》等应用程序也是这一漏洞的受害者。这些应用程序总共拥有数百万下载量和极高的用户评价，但却被发现对 AWS 凭据进行了硬编码，从而将敏感的云资源暴露在潜在攻击之下。例如，Crumbl 使用纯文本凭据配置 AWS 服务以及硬编码 WebSocket Secure (WSS) 端点，构成了重大安全风险。

同样，在 Android 端，Meru Cabs 和 Sulekha Business 等应用也有硬编码的 Microsoft Azure Blob Storage 凭据。Meru Cabs 应用程序的下载量超过 500 万次，它使用这些凭据来管理日志上传。这使得关键的云存储资源可能被滥用，从而使敏感数据极易受到未经授权的访问。

硬编码凭据，尤其是未加密的凭据，使应用程序极易受到攻击。报告称：”任何可以访问应用程序二进制代码或源代码的人都有可能提取这些凭据，并滥用它们来操纵或外泄数据，从而导致严重的安全漏洞。这些应用程序的广泛使用加剧了这一问题，使数百万用户面临风险。

为了解决这个问题，开发人员需要采取更好的安全措施，例如

* **使用环境变量：** 将敏感凭证存储在运行时加载的环境变量中，而不是直接嵌入到应用程序的源代码中。
* **实施机密管理：** 利用 AWS Secrets Manager 或 Azure Key Vault 等工具，安全地存储和访问云服务凭据。
* **加密敏感数据：** 如果必须存储凭证，确保使用强大的加密算法对其进行加密，并仅在需要时才解密。
* **定期代码审查和审计：** 定期审查代码是否存在安全漏洞，如硬编码凭据，以尽早降低风险。
* **自动化安全扫描：** 将安全扫描工具集成到您的 CI/CD 管道中，以便在开发过程中捕捉潜在漏洞

本文翻译自securityonline [原文链接](https://securityonline.info/hardcoded-cloud-credentials-found-in-popular-mobile-apps-a-major-security-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301178](/post/id/301178)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/hardcoded-cloud-credentials-found-in-popular-mobile-apps-a-major-security-flaw/)

如若转载,请注明出处： <https://securityonline.info/hardcoded-cloud-credentials-found-in-popular-mobile-apps-a-major-security-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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