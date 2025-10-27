---
title: FortiGuard Labs 将新的 EC2 Grouper 黑客与 AWS 凭证漏洞联系起来
url: https://www.anquanke.com/post/id/303176
source: 安全客-有思想的安全新媒体
date: 2025-01-03
fetch_date: 2025-10-06T20:07:40.859097
---

# FortiGuard Labs 将新的 EC2 Grouper 黑客与 AWS 凭证漏洞联系起来

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

# FortiGuard Labs 将新的 EC2 Grouper 黑客与 AWS 凭证漏洞联系起来

阅读量**55120**

发布时间 : 2025-01-02 14:19:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/fortiguard-labs-ec2-grouper-aws-credential-exploits/>

译文仅供参考，具体内容表达以及含义原文为准。

**摘要**

* **发现 EC2 Grouper：** 研究人员发现 EC2 Grouper 使用 “ec2group12345 ”等独特模式利用 AWS 凭据和工具。
* **凭据破坏：**他们主要从与有效账户绑定的代码库中获取凭据。
* **依赖 API：** 该小组避免手动活动，而是使用 API 进行侦查和资源创建。
* **检测挑战：** 命名约定和用户代理等指标对于一致检测来说并不可靠。
* **安全建议：** 使用 CSPM 工具，监控凭证滥用，并检测异常 API 活动，以降低风险。

云环境不断受到攻击，复杂的威胁行为者利用各种技术获取未经授权的访问。其中一种被称为 EC2 Grouper 的行为者已成为安全团队的显著对手。

根据Fortinet的FortiGuard实验室威胁研究团队的最新研究，该组织的特点是在攻击中持续使用AWS工具和独特的安全组命名规则。由于类似的用户代理和安全组命名约定，研究人员在几十个客户环境中追踪到了这个角色。

最新消息是在顶级黑客组织越来越多地利用 AWS 基础设施的情况下披露的。2024 年 12 月，有报告显示 ShinyHunters 和 Nemesis Group 合作攻击配置错误的服务器，尤其是 AWS S3 Buckets。

EC2 Grouper 通常利用 PowerShell 等 AWS 工具发起攻击，并经常使用独特的用户代理字符串。此外，该组织还持续创建具有 “ec2group”、“ec2group1”、“ec2group12 ”等命名模式的安全组。此外，他们在云攻击中还经常使用代码库来获取凭证，这些凭证通常来自有效账户。这种方法被认为是获取凭证的主要方法。

进一步探测发现，Grouper 使用 API 进行侦查、安全组创建和资源调配，避免了入站访问配置等直接操作。

研究人员克里斯-霍尔（Chris Hall）在与 hackread.com 分享的博文中指出，虽然这些指标可以提供初步线索，但往往不足以进行可靠的威胁检测。这是因为仅仅依靠这些指标可能会产生误导。攻击者可以轻易修改其用户代理，并可能偏离其通常的命名惯例。

研究人员没有观察到对 AuthorizeSecurityGroupIngress 的调用，该调用对于配置安全组启动的 EC2 的入站访问至关重要，但他们观察到了用于远程访问的 CreateInternetGateway 和 CreateVpc。

此外，在被入侵的云环境中，没有任何行动是基于目标或手动活动的。EC2 Grouper 在升级时可能是有选择性的，或者是在升级前检测到并隔离了受损账户。

![FortiGuard Labs Links EC2 Grouper Hackers to AWS Credential Exploits]()
截图： FortiGuard 实验室

不过，研究人员指出，通过分析凭证泄露和 API 使用等信号，安全团队可以制定可靠的检测策略，帮助企业抵御 EC2 Grouper 这样的复杂对手。他们建议，更有效的方法是监控与合法秘密扫描服务相关的可疑活动，以识别潜在的凭据泄露，而凭据泄露是 EC2 Grouper 的主要访问来源。

为了保证安全，企业还必须利用云安全态势管理（CSPM）工具来持续监控和评估云环境的安全态势。实施异常检测技术来识别云环境中的异常行为，如意外的 API 调用、资源创建或数据外渗，也会有所帮助。

本文翻译自hackread [原文链接](https://hackread.com/fortiguard-labs-ec2-grouper-aws-credential-exploits/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303176](/post/id/303176)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fortiguard-labs-ec2-grouper-aws-credential-exploits/)

如若转载,请注明出处： <https://hackread.com/fortiguard-labs-ec2-grouper-aws-credential-exploits/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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