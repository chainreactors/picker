---
title: Black Basta 通过 Microsoft Teams 对员工进行网络钓鱼操作
url: https://www.anquanke.com/post/id/301347
source: 安全客-有思想的安全新媒体
date: 2024-10-30
fetch_date: 2025-10-06T18:46:53.669182
---

# Black Basta 通过 Microsoft Teams 对员工进行网络钓鱼操作

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

# Black Basta 通过 Microsoft Teams 对员工进行网络钓鱼操作

阅读量**79398**

发布时间 : 2024-10-29 10:40:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/10/28/black-basta-operators-phish-employees-via-microsoft-teams/>

译文仅供参考，具体内容表达以及含义原文为准。

Black Basta 勒索软件的附属软件仍在试图通过冒充服务台工作人员来诱骗企业员工安装远程访问工具，现在也是通过 Microsoft Teams。

**通过 MS Teams 进行网络钓鱼**

今年早些时候，Rapid7 曾警告过 Black Basta 使用以下社交工程伎俩：他们在目标员工的收件箱中塞满垃圾邮件（通常来自自动系统或服务发送的确认或通知），然后冒充企业的 IT 服务台给他们打电话提供帮助。

不过最近，他们也开始使用 Microsoft Teams 来联系潜在受害者。

“在大量垃圾邮件事件之后，目标用户被添加到与外部用户的 Microsoft Teams 聊天中。”ReliaQuest 研究人员发现：“这些外部用户通过他们创建的 Entra ID 租户冒充支持、管理或服务台人员。”

看到的域包括

* securityadminhelper.onmicrosoft[.]com
* supportserviceadmin.onmicrosoft[.]com
* supportadministrator.onmicrosoft[.]com
* cybersecurityadmin.onmicrosoft[.]com

“在我们观察到的几乎所有情况下，显示名称都包括’Help Desk’字符串，其周围通常有空白字符，这很可能会使名称在聊天中居中。”研究人员指出：”我们还观察到，目标用户通常会被添加到‘一对一’聊天中。”

研究人员指出：“最终目的是让目标员工安装 QuickAssist 或 AnyDesk 等远程监控和管理工具，表面上是为了方便支持和修复，实际上是为了获得目标环境的初始访问权，并安装抓取凭证的恶意软件和网络映射工具。”

目标还被引导至托管有二维码页面的域，但其功能尚不清楚。研究人员补充说：“实际上，这些二维码有可能将用户导向更多的恶意基础设施。”

**给企业的建议**

通过暗网提供的垃圾邮件服务可以轻松实现向收件箱发送垃圾邮件。如果组织没有禁用或限制来自 Teams 中外部租户/域的通信，那么通过 Microsoft Teams 联系目标员工也很容易。(甚至可以通过 Teams 发送恶意软件）。

由于 “域创建和 Cobalt Strike 配置存在共性”，研究人员将这些攻击归咎于 Black Basta。不幸的是，他们并不是唯一使用这种攻击途径的威胁方。

ReliaQuest 的研究人员建议企业在 Teams 中禁用外部用户的通信，或只允许来自特定可信域的联系。

他们还应该调整电子邮件反垃圾邮件策略，为 Teams 启用日志记录功能（以方便调查），创建标记特定网络钓鱼聊天请求和后剥削活动的规则，并向员工宣传最新威胁。

Rapid7 此前曾建议企业阻止执行未经批准的 RMM 解决方案，并建立和定义员工可用于联系 IT 部门的渠道/方法。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/10/28/black-basta-operators-phish-employees-via-microsoft-teams/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301347](/post/id/301347)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/10/28/black-basta-operators-phish-employees-via-microsoft-teams/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/10/28/black-basta-operators-phish-employees-via-microsoft-teams/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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