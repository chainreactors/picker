---
title: GitHub 开源项目出现攻击媒介，多家公司受影响
url: https://www.anquanke.com/post/id/299156
source: 安全客-有思想的安全新媒体
date: 2024-08-16
fetch_date: 2025-10-06T17:59:19.852386
---

# GitHub 开源项目出现攻击媒介，多家公司受影响

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

# GitHub 开源项目出现攻击媒介，多家公司受影响

阅读量**54981**

发布时间 : 2024-08-15 14:27:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/github-attack-vector-google-microsoft-aws-projects>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员发现了一种攻击媒介，该攻击媒介影响了 Google，Microsoft，Amazon Web Services和其他公司拥有的GitHub开源项目，这些项目是通过滥用作为软件开发工作流程的一部分生成的工件来执行的。

根据首席研究员Yaron Avital昨天发表的一篇博客文章，Palo Alto Networks的Unit 42的研究人员发现了这次攻击，该攻击对“世界上最大的公司拥有的备受瞩目的开源项目”有效 。因此，这些项目的妥协“可能会对数百万消费者产生潜在影响”。

其他公司的项目受到攻击媒介的影响，该攻击媒介滥用了所谓的 GitHub Actions 工件，包括 Canonical （Ubuntu）、OWASP 基金会和 Red Hat 等。Avital写道，该向量导致工件泄漏第三方云服务以及GitHub令牌的令牌，使任何对存储库具有“读取访问权限”的人都可以使用它们。

他解释说：“这使得有权访问这些工件的恶意行为者有可能破坏这些秘密授予访问权限的服务。Avital补充说，在活动中发现的最常见的泄漏是GitHub令牌的泄漏，“允许攻击者对触发的GitHub存储库采取行动”。

他解释说，这种暴露最终可能允许攻击者通过持续集成和持续交付/部署（CI/CD）管道将恶意代码推送到生产环境，或者访问存储在GitHub存储库和组织中的秘密。

Avital写道，Unit 42与受影响项目的所有公司和维护者合作，并“得到了所有团队的大力支持”，以便“快速有效地”缓解了所有发现。然而，其他未知的私人和公共项目也可能受到攻击。

## 毒害开发周期

CI/CD 环境、流程和系统是现代软件开发的关键部分，涉及构建、测试和将代码交付到生产环境的流程。也就是说，它们为攻击者提供了一个绝佳的机会，因为他们使用高度敏感的凭据来对各种类型的服务进行身份验证，“对保持高水平的凭据卫生构成了重大挑战，”Avital写道。

发现的攻击以 GitHub Actions 为中心，GitHub Actions 是工作流构建工件，允许开发人员在同一工作流中的作业之间持久保存和共享数据。“这些工件可以是在构建过程中生成的任何文件，例如编译的代码、测试报告或部署包，”Avital 解释说。

项目可确保关键数据在工作流完成后不会丢失，从而使其可供以后的分析或部署访问。Avital 指出，这“对于在依赖作业之间共享测试结果或部署包特别有用”。

GitHub Actions 工作流经常使用机密与各种云服务以及 GitHub 本身进行交互。这些机密又包括用于对仓库执行操作的临时自动创建的 GitHub 令牌。

Avital 解释说：“Actions 构建工件是由工作流执行生成的输出，一旦创建，它们将存储长达 90 天。“在开源项目中，这些工件是公开的，任何人都可以使用。”

他发现的攻击流允许攻击者下载公开可用的工件，提取令牌，并将恶意代码推送到开源项目的存储库中。然后，代码成为项目的一部分，因此可以作为最终用户最终访问的软件或服务的一部分执行。

Unit 42 的帖子包括一个已知受到攻击媒介影响的 GitHub 开源项目列表。

## 需要一种全面的防御方法

GitHub 已成为威胁行为者的主要目标，因为它作为一种访问无数软件和服务的方式具有吸引力，只需在存储库中毒害几行代码。

Avital写道，新的攻击向量表明，在GitHub上，“我们当前关于工件扫描的安全对话存在差距” ，这意味着使用工件机制的组织应该“重新评估他们使用它的方式”。

他还建议防御者对软件开发采用整体方法，并仔细检查软件开发的每个阶段（从代码到生产）以发现潜在的漏洞。“像构建工件这样被忽视的元素往往会成为攻击者的主要目标，”Avital写道。

他指出，组织还应该根据最小权限减少运行器令牌的工作流权限，并审查其 CI/CD 管道中的工件创建，作为积极和警惕的安全方法的一部分，以加强开发项目的安全态势。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/github-attack-vector-google-microsoft-aws-projects)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299156](/post/id/299156)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/github-attack-vector-google-microsoft-aws-projects)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/github-attack-vector-google-microsoft-aws-projects>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [毒害开发周期](#h2-0)
* [需要一种全面的防御方法](#h2-1)

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