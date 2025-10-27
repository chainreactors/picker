---
title: 攻击者在不使用勒索软件的情况下加密 AWS S3 数据
url: https://www.anquanke.com/post/id/303485
source: 安全客-有思想的安全新媒体
date: 2025-01-15
fetch_date: 2025-10-06T20:07:17.838229
---

# 攻击者在不使用勒索软件的情况下加密 AWS S3 数据

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

# 攻击者在不使用勒索软件的情况下加密 AWS S3 数据

阅读量**87326**

发布时间 : 2025-01-14 11:17:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/01/13/codefinger-encrypting-aws-s3-data-without-ransomware-sse-c/>

译文仅供参考，具体内容表达以及含义原文为准。

一个名为 “Codefinger ”的勒索软件团伙正在使用 AWS 的服务器端加密选项和客户提供的密钥（SSE-C）对目标组织的 AWS S3 存储桶中存储的数据进行加密，并要求客户交出他们使用的密钥。

他们不会事先将数据外泄，而是将加密文件标记为在七天内删除，从而增加了企业支付赎金的压力。

**攻击是如何展开的？**

威胁者利用目标之前泄露的（无论是被盗还是无意泄露的）AWS 密钥，这些密钥拥有读写 S3 对象的权限。

“攻击者通过调用 x-amz-server-side-encryption-customer-algorithm 标头，利用他们生成并存储在本地的 AES-256 加密密钥启动加密过程，”Halcyon 研究团队解释道。

“AWS 会在加密操作过程中处理密钥，但不会将其存储起来。相反，AWS CloudTrail 中只记录了一个 HMAC（基于散列的消息验证码）。这个HMAC不足以重建密钥或解密数据。”

因此，如果目标组织没有加密数据的备份，实际上就会被迫付费。而且，在谈判过程中，他们无法对账户权限进行更改，因为攻击者威胁要保持沉默，让受害者束手无策。

**避免成为受害者**

该团队表示，将数据存储在 AWS S3 存储桶中的组织应该重视这些信息，并在这种攻击方法被更广泛地采用之前采取行动，使这种攻击成为不可能。(据他们所知，最近几周就有两家机构受到了攻击）。

“使用 IAM 策略中的 “条件 ”元素来防止 SSE-C 应用于 S3 存储桶。可以对策略进行配置，将此功能限制在授权数据和用户范围内，”他们建议说。

“定期检查所有 AWS 密钥的权限，确保它们拥有最低要求的访问权限。禁用未使用的密钥，并经常轮换使用中的密钥。”

他们还建议为 S3 操作启用详细的日志记录，以便能够快速检测到异常活动并采取相应措施。

当 AWS 发现公开暴露的客户密钥时，会将其自动 “隔离”，从而限制对其进行的操作（尽管研究人员此前发现，即使这样也不足以防止潜在的破坏）。

“AWS提供了一套丰富的功能，无需在源代码或配置文件中存储凭据，”亚马逊的云计算子公司对Halcyon的研究结果发表了评论。

“IAM 角色使应用程序能够安全地从 EC2 实例、ECS 或 EKS 容器或 Lambda 功能发出签名 API 请求，并使用自动部署、频繁轮换的短期凭证，无需客户管理。”他们说：“即使是 AWS 云之外的计算节点，也可以使用 Roles Anywhere 功能，在没有长期 AWS 凭据的情况下进行经过验证的调用。”

“开发人员工作站使用身份中心来获取由受 MFA 令牌保护的长期用户身份支持的短期凭证。所有这些技术都依赖于 AWS 安全令牌服务（AWS STS）来发布临时安全凭证，这些凭证可以控制对 AWS 资源的访问，而无需在应用程序（无论是代码还是配置文件）中分发或嵌入长期 AWS 安全凭证。”

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/01/13/codefinger-encrypting-aws-s3-data-without-ransomware-sse-c/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303485](/post/id/303485)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/01/13/codefinger-encrypting-aws-s3-data-without-ransomware-sse-c/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/01/13/codefinger-encrypting-aws-s3-data-without-ransomware-sse-c/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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