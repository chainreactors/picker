---
title: 专家揭露导致远程代码执行、数据窃取及服务全面接管的严重AWS漏洞
url: https://www.anquanke.com/post/id/299033
source: 安全客-有思想的安全新媒体
date: 2024-08-13
fetch_date: 2025-10-06T18:00:27.699943
---

# 专家揭露导致远程代码执行、数据窃取及服务全面接管的严重AWS漏洞

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

# 专家揭露导致远程代码执行、数据窃取及服务全面接管的严重AWS漏洞

阅读量**35560**

发布时间 : 2024-08-12 14:22:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员在 Amazon Web Services （AWS） 产品中发现了多个严重漏洞，如果成功利用这些漏洞，可能会导致严重后果。

“这些漏洞的影响范围包括远程代码执行（RCE）、全方位服务用户接管（可能提供强大的管理访问权限）、操纵人工智能模块、暴露敏感数据、数据泄露和拒绝服务，”云安全公司Aqua在与The Hacker News分享的一份详细报告中说。

在 2024 年 2 月负责任地披露后，亚马逊在 3 月至 6 月的几个月内解决了这些缺点。研究结果在 2024 年美国黑帽大会上公布。

该问题的核心被称为“桶垄断”，是一种称为“影子资源”的攻击向量，在本例中，它指的是在使用 CloudFormation、Glue、EMR、SageMaker、ServiceCatalog 和 CodeStar 等服务时自动创建 AWS S3 存储桶。

以这种方式创建的 S3 存储桶名称既是唯一的，又遵循预定义的命名约定（例如，“cf-templates-{Hash}-{Region}”）。攻击者可利用此行为在未使用的 AWS 区域中设置存储桶，并等待合法的 AWS 客户使用易受攻击的服务之一来秘密访问 S3 存储桶的内容。

根据授予对手控制的 S3 存储桶的权限，该方法可用于升级以触发 DoS 条件，或执行代码、操纵或窃取数据，甚至在用户不知情的情况下完全控制受害者账户。

为了最大限度地提高成功的机会，使用 Bucket Monopoly，攻击者可以在所有可用区域提前创建无人认领的存储桶，并在存储桶中存储恶意代码。当目标组织首次在新区域中启用其中一项易受攻击的服务时，恶意代码将在不知不觉中被执行，从而可能导致创建可以向攻击者授予控制权的管理员用户。

但是，重要的是要考虑到，攻击者必须等待受害者首次在新区域部署新的 CloudFormation 堆栈才能成功发起攻击。修改 S3 存储桶中的 CloudFormation 模板文件以创建流氓管理员用户还取决于受害者账户是否具有管理 IAM 角色的权限。

Aqua 表示，它发现其他五项 AWS 服务依赖于类似的 S3 存储桶命名方法——{服务前缀}-{AWS 账户 ID}-{区域}——从而使它们暴露于影子资源攻击，并最终允许威胁行为者提升权限并执行恶意操作，包括 DoS、信息泄露、数据操纵和任意代码执行 –

* AWS Glue：aws-glue-assets-{账户 ID}-{区域}
* AWS Elastic MapReduce （EMR）：aws-emr-studio -{Account-ID}-{Region}
* AWS SageMaker：sagemaker-{区域}-{账户ID}
* AWS CodeStar：aws-codestar-{区域}-{账户 ID}
* AWS 服务目录：cf-templates-{Hash}-{Region}

该公司还指出，AWS账户ID应该被视为秘密，这与亚马逊在其文档中所说的相反，因为它们可能被用来发动类似的攻击。

此外，可以使用 GitHub 正则表达式搜索或 Sourcegraph 来发现用于 AWS 账户的哈希值，或者通过抓取未解决的问题来发现，从而即使在没有直接从账户 ID 或任何其他账户相关元数据计算哈希值的情况下，也可以将 S3 存储桶名称拼凑在一起。

Aqua 说：“这种攻击媒介不仅影响 AWS 服务，还影响组织用来在其 AWS 环境中部署资源的许多开源项目。“许多开源项目会自动创建 S3 存储桶作为其功能的一部分，或者指示其用户部署 S3 存储桶。”

“建议为每个区域和账户生成唯一的哈希或随机标识符，并将此值合并到 S3 存储桶名称中，而不是在存储桶名称中使用可预测或静态标识符。这种方法有助于防止攻击者过早地认领您的存储桶。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299033](/post/id/299033)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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