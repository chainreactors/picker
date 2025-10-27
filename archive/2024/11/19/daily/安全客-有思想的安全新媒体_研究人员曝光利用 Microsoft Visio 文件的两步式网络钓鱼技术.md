---
title: 研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术
url: https://www.anquanke.com/post/id/301944
source: 安全客-有思想的安全新媒体
date: 2024-11-19
fetch_date: 2025-10-06T19:13:36.625396
---

# 研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术

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

# 研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术

阅读量**52469**

发布时间 : 2024-11-18 14:31:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/two-step-phishing-technique-leveraging-microsoft-visio-files-exposed-by-researchers/>

译文仅供参考，具体内容表达以及含义原文为准。

![two-step phishing technique]()

Perception Point 的最新发现揭露了一种先进的两步式网络钓鱼技术，该技术利用 Microsoft Visio 文件（.vsdx）和 SharePoint 发起极具欺骗性的凭证盗窃活动。

Microsoft Visio 文件传统上用于绘制流程图和网络地图等专业图表，但现在已被武器化。Perception Point 的报告显示：“在最近的网络钓鱼活动中，Visio 文件正被用来传递恶意 URL，在两步攻击路径中创建一个欺骗性传递点。”

这种方法利用了用户对 SharePoint 和 Microsoft Visio 等熟悉平台的信任。通过在被入侵的 SharePoint 账户托管的 .vsdx 文件中嵌入恶意 URL，攻击者可以绕过许多标准安全措施。

攻击分为两步，旨在逃避检测和利用用户行为：

1. **第一步：诱惑**
   攻击者首先利用被攻破的电子邮件账户向目标发送网络钓鱼电子邮件。“这些电子邮件因其来源而看似合法，通常包含令人信服的叙述，如紧急商业提案或采购订单。”这些电子邮件可能包含一个链接或 .eml 文件附件，其中包含一个指向 SharePoint 托管的 Visio 文件的 URL。
2. **第二步：陷阱**
   点击链接后，受害者会重定向到一个托管 Visio 文件的受攻击 SharePoint 页面。该文件包含一个嵌入式 “行动召唤 ”按钮，通常标注为 “查看文档”。受害者被指示按住 Ctrl 键并点击，这个简单的操作可以绕过自动安全系统。一旦点击，嵌入的 URL 就会将用户引导到一个伪造的 Microsoft 365 登录页面，该页面的目的是收集凭证。“该报告解释说：”与链接互动会将受害者重定向到一个冒充 Microsoft 365 的钓鱼页面。

![]()

图片 感知点 X-Ray

这种网络钓鱼技术结合了复杂的技术和心理操纵。通过要求用户执行按住 Ctrl 键等手动操作，攻击者可以躲避自动电子邮件安全扫描仪和检测工具。此外，合法品牌（包括组织徽标）的使用也增加了恶意 Visio 文件的可信度。

Perception Point 的研究人员观察到，使用这种方法的攻击明显增加，目标是全球数百家组织。报告警告说，这些活动 “旨在逃避检测和利用用户的信任”，强调了在企业环境中保持警惕的重要性。

本文翻译自securityonline [原文链接](https://securityonline.info/two-step-phishing-technique-leveraging-microsoft-visio-files-exposed-by-researchers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301944](/post/id/301944)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/two-step-phishing-technique-leveraging-microsoft-visio-files-exposed-by-researchers/)

如若转载,请注明出处： <https://securityonline.info/two-step-phishing-technique-leveraging-microsoft-visio-files-exposed-by-researchers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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