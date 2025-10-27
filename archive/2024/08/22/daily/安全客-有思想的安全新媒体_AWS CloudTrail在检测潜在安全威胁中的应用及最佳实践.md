---
title: AWS CloudTrail在检测潜在安全威胁中的应用及最佳实践
url: https://www.anquanke.com/post/id/299333
source: 安全客-有思想的安全新媒体
date: 2024-08-22
fetch_date: 2025-10-06T18:01:20.022966
---

# AWS CloudTrail在检测潜在安全威胁中的应用及最佳实践

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

# AWS CloudTrail在检测潜在安全威胁中的应用及最佳实践

阅读量**38473**

发布时间 : 2024-08-21 14:16:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 The Hacker News ，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html>

译文仅供参考，具体内容表达以及含义原文为准。

随着云基础设施成为现代企业的支柱，确保这些环境的安全至关重要。由于AWS（亚马逊网络服务）仍然是占主导地位的云，因此对于任何安全专业人员来说，知道在哪里寻找妥协迹象非常重要。AWS CloudTrail 是跟踪和记录 API 活动的重要工具，可提供 AWS 账户内所执行操作的全面记录。将 AWS CloudTrail 视为在您的 AWS 账户中进行的所有 API 调用的审计或事件日志。对于安全专业人员来说，监控这些日志至关重要，尤其是在检测潜在的未经授权的访问时，例如通过被盗的 API 密钥。这些技术以及我在 AWS 工作过的事件中学到的许多其他技术，我们将这些技术内置到 SANS FOR509（企业云取证）中。

## 1. 不寻常的 API 调用和访问模式

### A. API 请求的突然激增

潜在安全漏洞的最初迹象之一是 API 请求的意外增加。CloudTrail 会记录在您的 AWS 账户内进行的每个 API 调用，包括何人发出的调用、何时进行以及从何处发出。拥有被盗 API 密钥的攻击者可能会在短时间内发起大量请求，要么探测帐户以获取信息，要么尝试利用某些服务。

需要注意什么：

* API 活动突然出现非同寻常的激增。
* 来自异常 IP 地址的 API 调用，尤其是来自合法用户不操作的区域的 API 调用。
* 访问尝试访问各种服务，尤其是在您的组织通常不使用这些服务的情况下。

请注意，Guard Duty（如果启用）将自动标记此类事件，但您必须密切关注才能找到它们。

### B. 未经授权使用root账户

AWS 强烈建议避免使用根账户进行日常操作，因为它具有很高的权限级别。对 root 账户的任何访问，尤其是在使用与其关联的 API 密钥时，都是一个重要的危险信号。

需要注意什么：

* 使用 root 账户凭证进行的 API 调用，尤其是在通常不使用 root 账户的情况下。
* 更改帐户级别设置，例如修改帐单信息或帐户配置。

## 2. 异常IAM活动

### A. 可疑的访问密钥创建

攻击者可能会创建新的访问密钥，以建立对受感染帐户的持久访问。监控 CloudTrail 日志以创建新的访问密钥至关重要，尤其是在为通常不需要这些密钥的账户创建这些密钥时。

需要注意什么：

* 为 IAM 用户创建新的访问密钥，尤其是那些以前不需要它们的用户。
* 立即使用新创建的访问密钥，这可能表明攻击者正在测试或使用这些密钥。
* 与“CreateAccessKey”、“ListAccessKeys”和“UpdateAccessKey”相关的 API 调用。

### C. 角色承担模式

AWS 允许用户代入角色，向他们授予特定任务的临时凭证。监视异常角色承担模式至关重要，因为攻击者可能会承担角色以在环境中进行透视。

需要注意什么：

* 不寻常或频繁的“AssumeRole”API 调用，尤其是对具有提升权限的角色的调用。
* 来自通常不与合法用户关联的 IP 地址或区域的角色代入。
* 角色假设之后，执行与正常业务操作不一致的操作。

## 3. 异常数据访问和移动

### A. 异常的 S3 存储桶访问

Amazon S3 通常是攻击者的目标，因为它可以存储大量可能敏感的数据。监控 CloudTrail 是否存在对 S3 存储桶的异常访问对于检测泄露的 API 密钥至关重要。

需要注意什么：

* 与通常看不到此类活动的存储桶的“ListBuckets”、“GetObject”或“PutObject”相关的 API 调用。
* 在 S3 存储桶之间下载或上传大规模数据，尤其是在正常工作时间之外发生时。
* 尝试访问存储敏感数据（例如备份或机密文件）的存储桶。

### B. 数据外泄尝试

攻击者可能会尝试将数据移出您的 AWS 环境。CloudTrail 日志可以帮助检测此类渗透尝试，尤其是在数据传输模式不寻常的情况下。

需要注意什么：

* 从 S3、RDS（关系数据库服务）或 DynamoDB 等服务传输大量数据，尤其是向外部或未知 IP 地址传输的数据。
* 与您的环境中通常不使用的 AWS DataSync 或 S3 Transfer Acceleration 等服务相关的 API 调用。
* 尝试创建或修改数据复制配置，例如涉及 S3 跨区域复制的配置。

## 4. 意外的安全组修改

安全组控制 AWS 资源的入站和出站流量。攻击者可能会修改这些设置以打开其他攻击媒介，例如启用来自外部 IP 地址的 SSH 访问。

需要注意什么：

* 更改了安全组规则，这些规则允许来自受信任网络外部的 IP 地址的入站流量。
* 与“AuthorizeSecurityGroupIngress”或“RevokeSecurityGroupEgress”相关的 API 调用与正常操作不一致。
* 创建具有过于宽松规则的新安全组，例如允许公共端口上的所有入站流量。

## 5. 降低 API 密钥被盗风险的步骤

### A. 执行最小特权原则

为了最大程度地减少攻击者使用被盗的 API 密钥可能造成的损害，请在您的 AWS 账户中实施最小权限原则。确保 IAM 用户和角色仅具有执行其任务所需的权限。

### B. 实施多重身份验证 （MFA）

要求对所有 IAM 用户（尤其是具有管理权限的用户）进行 MFA。这增加了一层额外的安全保护层，使攻击者更难获得访问权限，即使他们窃取了 API 密钥。

### C. 定期轮换和审核访问密钥

定期轮换访问密钥，并确保它们与实际需要它们的 IAM 用户相关联。此外，审核访问密钥的使用情况，以确保它们不会被滥用或从意外位置使用。

### D. 启用和监控 CloudTrail 和 GuardDuty

确保在所有区域都启用了 CloudTrail，并且日志已集中进行分析。此外，AWS GuardDuty 可以提供对恶意活动的实时监控，从而提供另一层保护，防止凭据泄露。考虑使用 AWS Detective，在调查结果的基础上构建一些智能。

### E. 使用 AWS Config 进行合规性监控

AWS Config 可用于监控对安全最佳实践的遵守情况，包括 IAM 策略和安全组的正确使用。此工具可以帮助识别可能使您的帐户容易受到攻击的错误配置。

## 结论

AWS 环境的安全性取决于对 CloudTrail 日志中异常的警惕监控和快速检测。通过了解合法使用的典型模式并警惕与这些模式的偏差，安全专业人员可以在造成重大损害之前检测并响应潜在的入侵，例如涉及被盗 API 密钥的入侵。随着云环境的不断发展，在安全方面保持积极主动的态度对于保护敏感数据和确保 AWS 基础设施的完整性至关重要。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299333](/post/id/299333)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

### 热门推荐

文章目录

* [1. 不寻常的 API 调用和访问模式](#h2-0)
  + [A. API 请求的突然激增](#h3-1)
  + [B. 未经授权使用root账户](#h3-2)
* [2. 异常IAM活动](#h2-3)
  + [A. 可疑的访问密钥创建](#h3-4)
  + [C. 角色承担模式](#h3-5)
* [3. 异常数据访问和移动](#h2-6)
  + [A. 异常的 S3 存储桶访问](#h3-7)
  + [B. 数据外泄尝试](#h3-8)
* [4. 意外的安全组修改](#h2-9)
* [5. 降低 API 密钥被盗风险的步骤](#h2-10)
  + [A. 执行最小特权原则](#h3-11)
  + [B. 实施多重身份验证 （MFA）](#h3-12)
  + [C. 定期轮换和审核访问密钥](#h3-13)
  + [D. 启用和监控 CloudTrail 和 GuardDuty](#h3-14)
  + [E. 使用 AWS Config 进行合规性监控](#h3-15)
* [结论](#h2-16)

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