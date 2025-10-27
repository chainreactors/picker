---
title: AWS 云开发工具包缺陷暴露了可完全接管的账户
url: https://www.anquanke.com/post/id/301266
source: 安全客-有思想的安全新媒体
date: 2024-10-26
fetch_date: 2025-10-06T18:45:38.213775
---

# AWS 云开发工具包缺陷暴露了可完全接管的账户

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

# AWS 云开发工具包缺陷暴露了可完全接管的账户

阅读量**66530**

发布时间 : 2024-10-25 11:13:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：theregister

原文地址：<https://go.theregister.com/feed/www.theregister.com/2024/10/24/aws_cloud_development_kit_flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

亚马逊网络服务公司（Amazon Web Services）修复了其开源云开发工具包（Cloud Development Kit）中的一个漏洞，在适当的条件下，攻击者可以完全劫持用户的账户。

云开发工具包（CDK）是AWS开发的一个开源框架，允许开发人员使用Python、TypeScript、JavaScript、Go等编程语言将云应用基础设施定义为代码，然后通过AWS CloudFormation配置这些资源。

据Aqua公司的安全研究人员Ofek Itach和Yakir Kadkoda称，该公司的漏洞猎手于6月27日发现了CDK问题。大约两周后，这家云计算巨头用CDK v2.149.0版本修补了漏洞。

AWS证实，约有1%的CDK用户容易受到这一安全问题的影响，并向The Register保证，它 “调查并解决了所有报告的问题”。AWS 发言人在一封电子邮件声明中写道，该业务部门对 Aqua 报告该漏洞并与 AWS 合作表示赞赏，并补充说：”AWS 已对所有报告的问题进行了调查和解决：

**2024 年 7 月 12 日，AWS 发布了 AWS 云开发工具包（AWS CDK）CLI 的更新，该更新实施了额外的安全控制，以减少执行 CDK 部署的客户数据泄露的可能性。使用最新版本的客户需要执行一次性操作来升级其引导资源。AWS 已直接联系可能受影响的客户，通知他们需要升级，并在 CLI 中添加了额外检查，以提醒用户升级。**

这个安全问题与早些时候一种被称为 “Bucket Monopoly ”的攻击方法有关（Aqua 也发现了这种方法），在这种方法中，犯罪分子可以预测 AWS S3 存储桶的名称，将恶意代码预先加载到存储桶中，然后坐等目标 org 在不知情的情况下执行这些代码。

一旦发生这种情况，攻击者就可以窃取数据，甚至在用户不知情的情况下接管其账户。

新的问题还涉及这些 S3 存储桶、其名称的可预测性以及攻击者通过 S3 存储桶命名滥用这种可预测性。

在部署任何应用程序之前，CDK 要求用户对其环境进行引导。这会自动创建所需的基础架构组件，包括身份和访问管理（IAM）角色、权限和策略以及 S3 暂存桶。

与之前的 “桶垄断 ”问题一样，这些 CDK 暂存桶遵循一套命名机制–“cdk-{Qualifier}-{Description}-{Account-ID}-{Region}”–只要知道用户的 AWS 帐户 ID 和部署 CDK 的地区，就能轻松预测它们。水叮当二人组指出：

**由于前缀始终是 cdk，限定符默认为 hnb659fds，而 assets 是水桶名称中的常量字符串，因此唯一会改变的变量就是帐户 ID 和地区。**

事实证明，在启动过程中使用默认限定符的情况数以千计。这样一来，就更容易盗用其他用户的 CDK 暂存数据桶名称，然后实施 “数据桶垄断 ”攻击概述中详述的所有恶行。

伊塔奇和卡德科达写道：“在某些情况下，CDK问题可能允许攻击者获得对目标AWS账户的管理访问权限，导致账户被完全接管。”

所有这些用户都已收到 AWS 的通知。作为修复措施的一部分，AWS 现在确保资产只上传到用户账户内的存储桶，从而防止使用任何不属于启动引导过程的账户的数据。

不过，即使是更新的版本，如果您曾使用旧版本进行引导，也需要用户进行操作： CDK 版本 2.148.1（2024 年 7 月 11 日）或更早。为了降低这一风险，Aqua 建议如下：

**如果您正在使用 2.148.1 版或更早版本的 CDK，请升级到 2.149.0 版或更高版本。升级后，重新运行 cdk bootstrap 命令。**

**或者，你也可以不升级 CDK 版本，而是将 IAM 策略条件应用到 FilePublishingRole CDK 角色：cdk-${Qualifier}-file-publishing-role-${AWS::AccountId}-${AWS::Region}，类似于 AWS 补丁。**

此外，正如两人在早期研究中建议的那样，不要使用可预测的 S3 存储桶名称，否则就有可能被攻击者命名为你的存储桶。“取而代之的是，为每个区域和账户生成唯一的哈希值或随机标识符，并将其纳入 S3 存储桶名称中。

本文翻译自theregister [原文链接](https://go.theregister.com/feed/www.theregister.com/2024/10/24/aws_cloud_development_kit_flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301266](/post/id/301266)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://go.theregister.com/feed/www.theregister.com/2024/10/24/aws_cloud_development_kit_flaw/)

如若转载,请注明出处： <https://go.theregister.com/feed/www.theregister.com/2024/10/24/aws_cloud_development_kit_flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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