---
title: 最新的 WatchGuard 报告显示，利用远程访问的威胁行为者有所增加
url: https://www.anquanke.com/post/id/298098
source: 安全客-有思想的安全新媒体
date: 2024-07-20
fetch_date: 2025-10-06T17:42:25.575472
---

# 最新的 WatchGuard 报告显示，利用远程访问的威胁行为者有所增加

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

# 最新的 WatchGuard 报告显示，利用远程访问的威胁行为者有所增加

阅读量**79308**

发布时间 : 2024-07-19 11:41:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Marc Laliberte，文章来源：cyber defense magazine

原文地址：<https://www.cyberdefensemagazine.com/latest-watchguard-report-reveals-rise-in-threat-actors-exploiting-remote-access/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全威胁持续增长，威胁形势不断演变，黑客采用越来越复杂和不可预测的方法。随着网络安全技能的持续短缺，对托管服务提供商 （MSP）、统一安全和自动化平台的需求从未如此强烈，以加强网络安全并保护组织免受不断变化的威胁环境的影响。

WatchGuard Technologies每季度都会发布一份互联网安全报告，该报告提供了对过去三个月主要恶意软件趋势和网络安全威胁的见解。Threat Labs 2023 年第三季度互联网安全报告的主要发现显示，远程访问软件滥用事件不断增加，网络对手使用密码窃取程序和信息窃取程序来获取有价值的凭据，威胁行为者从利用脚本转向使用其他离地技术来发起端点攻击。

在主要调查结果中，包含 2023 年第三季度数据的互联网安全报告显示：

* **威胁行为者越来越多地使用远程管理工具和软件来逃避反恶意软件检测。**联邦调查局和CISA也注意到了这一趋势。例如，在研究顶级网络钓鱼域时，威胁实验室观察到一个技术支持骗局，该骗局将导致受害者下载预先配置的未经授权的TeamViewer版本，这将允许攻击者完全远程访问他们的计算机。
* **美杜莎勒索软件变种在第三季度激增，推动端点勒索软件攻击增加 89%。**从表面上看，端点勒索软件检测在第三季度出现下降。然而，首次出现在十大恶意软件威胁中的美杜莎勒索软件变种是通过威胁实验室的自动签名引擎检测到的通用签名。考虑到美杜莎检测，勒索软件攻击环比增长了 89%。
* **威胁行为者不再使用基于脚本的攻击，而是越来越多地使用其他离地技术。**恶意脚本作为攻击媒介在第二季度下降了 41% 之后，在第三季度下降了 11%。尽管如此，基于脚本的攻击仍然是最大的攻击媒介，占攻击总数的 56%，而 PowerShell 等脚本语言通常用于生存的离地攻击。与此同时，Windows 的陆地二进制文件增加了 32%。这些发现向威胁实验室研究人员表明，威胁行为者继续利用多种离地生存技术，可能是为了响应围绕 PowerShell 和其他脚本的更多保护措施。生存的陆上攻击构成了最多的端点攻击。
* **通过加密连接到达的恶意软件下降到 48%，**这意味着检测到的所有恶意软件中只有不到一半来自加密流量。这个数字值得注意，因为它比前几个季度大幅下降。总体而言，恶意软件检测总数增加了 14%。
* **基于电子邮件的 dropper 系列提供恶意负载，在第三季度检测到的前 5 个加密恶意软件中占了四个。**前 5 名中除了一个变体外，其他所有变体都包含名为 Stacked 的滴管系列，该系列在电子邮件鱼叉式网络钓鱼尝试中作为附件出现。威胁行为者将发送带有恶意附件的电子邮件，这些附件似乎来自已知发件人，并声称包含发票或重要文档以供审查，旨在诱骗最终用户下载恶意软件。其中两个 Stacked 变体 – Stacked.1.12 和 Stacked.1.7 – 也出现在前 10 名恶意软件检测中。
* **商品化的恶意软件应运而生。**在顶级恶意软件威胁中，一个新的恶意软件系列Lazy.360502进入了前10名。它提供广告软件变体 2345explorer 以及 Vidar 密码窃取程序。这种恶意软件威胁与一个提供凭据窃取程序的中国网站有关，其运行方式似乎类似于“密码窃取程序即服务”，威胁行为者可以为被盗的凭据付费，这说明了商品化恶意软件的使用方式。
* **网络攻击在第三季度增长了 16%。**ProxyLogon 是网络攻击的头号漏洞，占所有网络检测总数的 10%。
* **前 50 名网络攻击中出现了三个新签名。**其中包括 2012 年的 PHP 通用网关接口 Apache 漏洞，该漏洞会导致缓冲区溢出。另一个是2016年的Microsoft .NET Framework 2.0漏洞，可能导致拒绝服务攻击。从2014年开始，开源CMSDrupal中也存在SQL注入漏洞。此漏洞允许攻击者远程利用 Drupal，而无需任何身份验证。

鉴于威胁行为者试图通过多种方式访问敏感信息，组织需要全面的多层网络安全策略，包括网络、端点、Wi-Fi 和身份保护等不同类型的安全措施，以加快威胁检测和响应流程。同样重要的是要记住，即使是最好的防御措施也可能被社会工程攻击所破坏。用户需要明白，他们通常是防止恶意行为者渗透组织的最后一道防线。

本文翻译自cyber defense magazine [原文链接](https://www.cyberdefensemagazine.com/latest-watchguard-report-reveals-rise-in-threat-actors-exploiting-remote-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298098](/post/id/298098)

安全KER - 有思想的安全新媒体

本文转载自: [cyber defense magazine](https://www.cyberdefensemagazine.com/latest-watchguard-report-reveals-rise-in-threat-actors-exploiting-remote-access/)

如若转载,请注明出处： <https://www.cyberdefensemagazine.com/latest-watchguard-report-reveals-rise-in-threat-actors-exploiting-remote-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

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