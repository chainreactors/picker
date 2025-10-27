---
title: 威胁者利用 Bitbucket Artifacts 以纯文本形式泄露 AWS 机密
url: https://www.anquanke.com/post/id/296718
source: 安全客-有思想的安全新媒体
date: 2024-05-24
fetch_date: 2025-10-06T16:48:56.547167
---

# 威胁者利用 Bitbucket Artifacts 以纯文本形式泄露 AWS 机密

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

# 威胁者利用 Bitbucket Artifacts 以纯文本形式泄露 AWS 机密

阅读量**75460**

发布时间 : 2024-05-23 10:49:01

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/bitbucket-artifacts-could-expose-aws-secrets/>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员发现，Atlassian 的 Bitbucket 代码存储库工具中存在一个缺陷，威胁行为者可以通过使用在 Bitbucket 工件中以明文形式泄露的身份验证机密来成功破坏 AWS 帐户。

Bitbucket 提供了一种存储变量的方法，允许开发人员在编写代码时快速引用它们。管理员还可以将变量设置为 Bitbucket Pipelines 中的“安全”，以防止其值以纯文本形式被读取。

然而，该系统中最近发现的缺陷可能会导致管道运行期间生成的工件对象以明文格式公开这些受保护的变量。

**BitBucket Artifacts 包含明文秘密**
Bitbucket Pipelines CI/CD 服务集成在 Bitbucket 中，使用工件对象来存储变量、文件和目录，以便在构建和测试过程的后续阶段使用。 Bitbucket 的“安全变量”功能据称可以安全地存储AWS 密钥等敏感信息，因为它们在 Bitbucket 环境中进行了加密，从而防止直接访问和记录其值。

开发人员使用 printenv 命令将所有环境变量（包括安全变量）存储在文本文件中，然后将其包含在工件对象中。

然而，Mandiant 的研究人员发现，该系统的一个严重缺陷导致管道运行期间生成的工件对象以明文形式包含这些受保护的变量。由于开发人员不知道这些机密在工件文件中暴露，他们可能会无意中导致机密值被推送到公共存储库，威胁行为者可以从中窃取它们。

研究人员表示，威胁行为者只需打开文本文件即可查看纯文本中的敏感变量，轻松窃取可用于窃取数据或执行其他恶意活动的身份验证机密。

研究人员指出，开发团队在 Web 应用程序源代码中使用 Bitbucket 工件进行故障排除，在不知不觉中暴露了密钥的明文值。这导致这些密钥在公共互联网上暴露，攻击者可以利用它们进行未经授权的访问。

**研究人员分享复制 BitBucket 漏洞的指南**
研究人员分享了在 Bitbucket 环境中重现秘密泄露的分步说明，作为漏洞的证据。这些步骤包括定义安全变量、更新 bitbucket-pipelines.yml 文件以创建环境工件，以及下载和访问该工件以查看公开的秘密。

研究人员分享了以下保护 BitBucket Pipeline 机密的建议：

* 将机密存储在专用的机密管理器中，然后在存储在 Bitbucket 存储库中的代码中引用这些变量。
* 仔细检查 Bitbucket 工件对象，以确保它们不会将秘密泄露为纯文本文件。
* 在管道的整个生命周期内部署代码扫描，以便在将代码部署到生产之前捕获存储在代码中的机密。

然而，研究人员表示，这些发现并不是对 BitBucket 的控诉，而是对看似无害的行为如何迅速发展成严重安全问题的观察。

本文翻译自 [原文链接](https://thecyberexpress.com/bitbucket-artifacts-could-expose-aws-secrets/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296718](/post/id/296718)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/bitbucket-artifacts-could-expose-aws-secrets/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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