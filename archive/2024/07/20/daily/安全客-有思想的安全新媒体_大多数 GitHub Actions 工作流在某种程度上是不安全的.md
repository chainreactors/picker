---
title: 大多数 GitHub Actions 工作流在某种程度上是不安全的
url: https://www.anquanke.com/post/id/298117
source: 安全客-有思想的安全新媒体
date: 2024-07-20
fetch_date: 2025-10-06T17:42:29.885022
---

# 大多数 GitHub Actions 工作流在某种程度上是不安全的

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

# 大多数 GitHub Actions 工作流在某种程度上是不安全的

阅读量**107061**

发布时间 : 2024-07-19 11:36:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Help Net Security，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/07/17/insecure-github-actions-workflows/>

译文仅供参考，具体内容表达以及含义原文为准。

### GitHub Actions 安全漏洞带来重大风险

该报告发现，GitHub Actions市场的安全状况尤其令人担忧，大多数自定义操作未经验证，由一个开发人员维护，或根据OpenSSF记分卡生成低安全分数。

[![]()](https://helpnet.link/4d2df8)

GitHub Actions 安全性是开源安全性的一个重要方面。不安全的 GitHub Actions 可能允许攻击者破坏开源并发起供应链攻击，或将其用作使用 GitHub 的组织的初始攻击媒介。

“GitHub 是一个非常受欢迎的平台。事实上，超过 1 亿开发人员和超过 90% 的财富 100 强公司使用它，“Legit Security 研究主管 Roy Blit 说。

“然而，尽管它很受欢迎，但大多数 GitHub Actions 工作流程在某种程度上都是不安全的——从过度特权到具有高风险依赖关系。例如，我们过去的研究发现，即使是来自谷歌和Apache等全球企业的项目也存在缺陷。这些发现令人震惊，因为 GitHub Actions 提供了关键基础设施的关键。它们连接到组织的源代码及其部署环境，因此一旦被利用，组织就完全掌握在攻击者的手中，“Blit补充道。

GitHub 已迅速成为开发人员社区的重要资源，它使开发人员能够在开发项目上协同工作并实时查看彼此的更改。GitHub Actions 通过事件驱动的触发器将自动化添加到软件开发生命周期中。这些触发器是指定的事件，范围从创建拉取请求到在存储库中构建新分支。

毫不奇怪，GitHub 用户继续增长，截至 2023 年 1 月，拥有 400 多万个组织和超过 4.2 亿个存储库，其中超过 2800 万个公共用户。

### 在 GitHub Actions 工作流中发现的漏洞

研究人员在 7,000 多个工作流程中发现了不受信任输入的插值;在 2,500 多个工作流中执行不受信任的代码;以及在 3,000 多个工作流中使用不可信的工件。

Legit 检查了触发器、作业、步骤、运行器和权限，发现了重大风险。例如，作业和步骤使用的 98% 的引用不遵循依赖项固定的最佳做法（可防止意外更改或更新），并且 86% 的工作流不限制令牌权限。

Legit 发现社区为增强 GitHub Actions 功能而开发的 Actions 的安全状态令人担忧。在市场中的 19,113 个自定义 GitHub Actions 中，只有 913 个是由经过验证的 GitHub 用户创建的;18%的人有脆弱的依赖性;762 个已存档，不接收定期更新;OSSF 的平均安全得分为 4.23 分（满分 10 分）;大多数由单个开发人员维护。

### 对团队进行 GitHub Action 安全性培训

与任何开源开发人员一样，自定义操作开发人员没有义务发布其代码中发现的漏洞的 CVE，有时他们明确拒绝这样做。

自定义操作的贡献者数量强烈反映了其可信度。贡献者数量越多，表明社区参与范围越广，发展越积极。这种协作努力可以提高安全性、测试和整体质量。

不幸的是，市场上的大多数 GitHub Actions 都是由单个开发人员维护的。之所以会出现这种情况，是因为许多自定义操作的范围很小，不需要花费大量精力来创建和维护。

为了降低风险，组织必须优先教育其开发和运营团队了解与 GitHub Actions 相关的安全风险，包括正确处理机密、代码注入的危险以及使用第三方操作的最佳实践。

此外，组织应使用 GitHub 的内置功能来控制 GitHub Actions 行为，以强制实施最佳实践，并利用与 GitHub 无缝集成的安全工具进行持续安全扫描。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/07/17/insecure-github-actions-workflows/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298117](/post/id/298117)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/07/17/insecure-github-actions-workflows/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/07/17/insecure-github-actions-workflows/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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