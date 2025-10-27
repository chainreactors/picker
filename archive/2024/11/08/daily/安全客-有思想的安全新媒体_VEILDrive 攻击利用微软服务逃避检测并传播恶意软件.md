---
title: VEILDrive 攻击利用微软服务逃避检测并传播恶意软件
url: https://www.anquanke.com/post/id/301621
source: 安全客-有思想的安全新媒体
date: 2024-11-08
fetch_date: 2025-10-06T19:13:52.977680
---

# VEILDrive 攻击利用微软服务逃避检测并传播恶意软件

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

# VEILDrive 攻击利用微软服务逃避检测并传播恶意软件

阅读量**84840**

发布时间 : 2024-11-07 11:08:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/veildrive-attack-exploits-microsoft.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，一个名为 VEILDrive 的持续威胁活动利用微软的合法服务（包括 Teams、SharePoint、Quick Assist 和 OneDrive）作为其作案手法的一部分。

以色列网络安全公司Hunters在一份新报告中称：“利用微软的SaaS服务（包括Teams、SharePoint、Quick Assist和OneDrive），攻击者利用之前被入侵组织的可信基础设施来发布鱼叉式网络钓鱼攻击和存储恶意软件。”

“这种以云为中心的策略使威胁行为者得以避开传统监控系统的检测。”

Hunters 称，204 年 9 月，该公司在应对一起针对美国关键基础设施组织的网络事件后发现了这一活动。它没有透露这家公司的名称，而是将其命名为 “Org C”。

据信，该活动在一个月前开始，攻击最终导致部署了基于 Java 的恶意软件，该恶意软件使用 OneDrive 进行命令和控制 （C2）。

据说，幕后的威胁行为者冒充 IT 团队成员向 C机关的四名员工发送了团队信息，并请求通过快速协助工具远程访问他们的系统。

这种最初的入侵方法之所以引人注目，是因为攻击者利用了属于先前潜在受害者（机关 A）的用户账户，而不是为此创建一个新账户。

Hunters说：“C机关的目标用户收到的Microsoft Teams消息是通过Microsoft Teams的‘外部访问’功能实现的，该功能默认情况下允许与任何外部组织进行一对一通信。”

下一步，威胁实施者通过聊天工具分享了一个指向 ZIP 压缩文件（“Client\_v8.16L.zip”）的 SharePoint 下载链接，该文件托管在另一个租户（B 组织）上。除其他文件外，该 ZIP 压缩包还嵌入了另一个名为 LiteManager 的远程访问工具。

通过 “快速助手 ”获得的远程访问权限被用于在系统上创建计划任务，以定期执行 LiteManager 远程监控和管理 (RMM) 软件。

同时下载的还有第二个 ZIP 文件（“Cliento.zip”），该文件使用了相同的方法，包括 Java 存档 (JAR) 形式的 Java 恶意软件和整个 Java 开发工具包 (JDK) 以执行该恶意软件。

恶意软件被设计为使用硬编码的 Entra ID（前身为 Azure Active Directory）凭据连接到对手控制的 OneDrive 帐户，将其用作 C2，通过使用 Microsoft Graph API 在受感染系统上获取和执行 PowerShell 命令。

它还内置了一种后备机制，可将 HTTPS 套接字初始化到远程 Azure 虚拟机，然后利用该套接字接收命令并在 PowerShell 上下文中执行这些命令。

这已经不是快速辅助程序第一次以这种方式被使用了。今年 5 月早些时候，微软曾警告说，一个名为 Storm-1811 的网络犯罪团伙滥用快速辅助功能，假装成 IT 专业人员或技术支持人员，获取访问权限并投放 Black Basta 勒索软件。

在此之前几周，这家 Windows 制造商还表示，它已经观察到滥用 SharePoint、OneDrive 和 Dropbox 等合法文件托管服务作为逃避检测手段的活动。

“这种依赖 SaaS 的策略使实时检测变得复杂，并绕过了传统的防御手段，”Hunters 说。“这款恶意软件采用零混淆和结构良好的代码，打破了以规避为重点的典型设计趋势，使其具有非同寻常的可读性和直观性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/veildrive-attack-exploits-microsoft.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301621](/post/id/301621)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/veildrive-attack-exploits-microsoft.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/veildrive-attack-exploits-microsoft.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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