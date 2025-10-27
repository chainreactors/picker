---
title: 谷歌云文档AI漏洞即使在支付了漏洞赏金后仍允许数据盗窃
url: https://www.anquanke.com/post/id/300154
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:12.986110
---

# 谷歌云文档AI漏洞即使在支付了漏洞赏金后仍允许数据盗窃

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

# 谷歌云文档AI漏洞即使在支付了漏洞赏金后仍允许数据盗窃

阅读量**84942**

发布时间 : 2024-09-18 15:00:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：theregister

原文地址：<https://www.theregister.com/2024/09/17/google_cloud_document_ai_flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

Google Cloud 的 Document AI 服务中过于宽松的设置可能会被数据窃贼滥用，闯入 Cloud Storage 存储桶并窃取敏感信息。

根据威胁检测和响应公司 Vectra AI 及其首席安全研究员 Kat Traxler 的说法，他表示，尽管最终收到了 Google 的漏洞赏金，但这家云巨头尚未修复错误配置，这意味着这个攻击向量仍然敞开。

整个漏洞报告过程有点混乱。Traxler 在 4 月初报告了该漏洞，但谷歌最初确定该文档“不足”，无法为该发现支付赏金。后来，他们改变了路线，奖励了这位漏洞猎人 3133.70 美元的报告——并将状态标记为“已修复”，而 Traxler 则认为这仍然是一个问题。

谷歌没有立即回应 *The Register* 的询问。

“攻击者需要多么老练，”当被问及该问题在实际攻击中被滥用的可能性时，Traxler 告诉 *The Register*。

“如果环境不成熟，可以广泛访问常见且容易找到的数据，那么在 Document AI 中利用这个缺陷就没有必要，”她说。“但是，在更严格遵守最低权限的强化环境中，利用 Document AI 服务泄露数据既符合攻击者的动机，也可能是实现目标的最简单途径。”

Traxler 在周一发布的研究中详细介绍了这次攻击，并附有概念验证 （POC），展示了她如何绕过 Document AI 的访问控制，从源 Google Cloud Storage 存储桶中滑动 PDF，更改文件，然后返回。

该问题存在于 Document AI 中，这是一项 Google Cloud 服务，它使用机器学习从文档中提取信息，旨在使企业能够更轻松、更快速地分析和处理大量文档。客户可以使用预先训练的模型或创建自己的模型，并且他们可以通过标准（在线）jos 或批处理（离线）处理来处理存储在 Google Cloud Storage 中的文档。

在批处理期间，该服务使用称为服务代理的 Google 托管服务账户。它用作批处理中的标识，并提取数据并输出结果。

根据 Traxler 的说法，这就是问题所在。预设的服务代理权限过于宽泛，在批处理模式下，服务使用服务代理的权限，而不是调用方的权限。

授予服务代理的权限允许它访问同一项目中的任何 Google Cloud Storage 存储桶，从而允许该服务移动用户通常无权访问的数据。

“此功能使恶意行为者能够将数据从 GCS 泄露到任意 Cloud Storage 存储桶，绕过访问控制并泄露敏感信息，”Traxler 写道。“利用该服务（及其身份）泄露数据构成传递访问滥用，绕过预期的访问控制并损害数据机密性。”

Traxler 于 4 月 4 日向 Google 的漏洞奖励计划报告了数据泄露问题。经过一番来回讨论（所有这些都在 Vectra 文章中详细说明），VPR 最终于 5 月 7 日确定“此问题的安全影响不符合经济奖励的标准”。相反，Traxler 获得了荣誉奖。

6 月 7 日，Google 将该漏洞的状态更改为“已修复”。同月，Traxler 对这一发现提出异议，然后在 7 月初向 Google 发送了一份 POC，并附上了以下消息：

需要强调的是，可以使用 Document AI 处理（或批处理）文档的主体不需要具有存储权限即可访问 Cloud Storage 中的数据并移动到另一个位置（数据泄露）。这是由于分配给 Document AI P4SA （roles/documentaicore.serviceAgent） 的权限而实现的。我建议为 Document AI 分配一个用户管理服务帐户来处理其数据，类似于 Cloud Workflows。允许 P4SA 移动用户定义的数据不是正确的模式，并且会导致数据泄露漏洞。请更改此问题的状态以指示它尚未修复。公开披露将在 2024 年 9 月的一场备受瞩目的活动中进行。

7 月下旬，Traxler 提醒漏洞赏金团队，她将在今天举行的 fwd：cloudsec Europe 2024 上演示 Document AI 的数据窃取风险，并在 8 月再次建议更改状态，因为她坚持认为，问题仍未解决。

9 月 9 日，Traxler 收到消息，VRP 确实决定向她发放 3133.70 美元的悬赏，以奖励她披露信息。

“恭喜！此决定的理由：正常的 Google 应用程序。漏洞类别是’绕过重要的安全控制’，其他数据/系统，“根据 Vectra 讲述中发布的时间表。“我们应用了降级，因为攻击者需要有权访问受影响受害者的项目。”

*同样，The Register* 已经联系了 Google 了解他们的情况，并希望能够尽快包含评论。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/09/17/google_cloud_document_ai_flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300154](/post/id/300154)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/09/17/google_cloud_document_ai_flaw/)

如若转载,请注明出处： <https://www.theregister.com/2024/09/17/google_cloud_document_ai_flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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