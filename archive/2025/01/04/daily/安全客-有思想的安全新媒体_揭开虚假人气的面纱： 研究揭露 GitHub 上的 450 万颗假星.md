---
title: 揭开虚假人气的面纱： 研究揭露 GitHub 上的 450 万颗假星
url: https://www.anquanke.com/post/id/303233
source: 安全客-有思想的安全新媒体
date: 2025-01-04
fetch_date: 2025-10-06T20:08:44.295155
---

# 揭开虚假人气的面纱： 研究揭露 GitHub 上的 450 万颗假星

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

# 揭开虚假人气的面纱： 研究揭露 GitHub 上的 450 万颗假星

阅读量**70893**

发布时间 : 2025-01-03 10:41:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/unmasking-fraudulent-popularity-study-exposes-4-5-million-fake-stars-on-github/>

译文仅供参考，具体内容表达以及含义原文为准。

![GitHub Fraudulent - security analysis tool]()

在卡内基梅隆大学、北卡罗来纳州立大学和 Socket 的研究人员进行的一项研究中，GitHub 星级评价系统的完整性受到了质疑。研究团队发现，欺诈性 “星级 ”的激增令人震惊，这些 “星级 ”被用来操纵世界领先开源平台上资源库的受欢迎程度。

这项研究利用名为StarScout的检测工具，系统分析了超过20 TB的GitHub元数据，识别出450多万个疑似虚假 “明星”，涉及15000多个软件源。研究人员详细指出，这类明星经常被用来扩大短期恶意软件活动或虚假夸大软件源的可见性，通常伪装成游戏作弊器、加密货币机器人或盗版软件。

GitHub 星级是一个重要的人气信号，会影响开发者的选择，甚至影响软件供应链中的决策。然而，这些星级很容易被滥用。正如研究人员所指出的，“星数是使用最广泛的人气信号，但也存在被人为夸大（即伪造）的风险，从而降低了其作为决策信号的价值，并给所有 GitHub 用户带来了安全风险”。

![GitHub Fraudulent]()
来源：Arxiv

研究发现了多种欺诈行为，包括：

* **僵尸网络：** 自动账户大量生成星星。
* **众包操纵：** 模仿真实活动的人工操作计划。
* **虚假增长黑客：** 为寻求知名度的非恶意资源库增加星数的策略。

从假星中获益的恶意资源库构成了切实的威胁。正如研究人员强调的那样，“大多数虚假星级被用来推广伪装成盗版软件、游戏作弊器或加密货币机器人的短命恶意软件库”。在一个引人注目的案例中，一个虚假声称自己是区块链实用程序的资源库被发现包含严重混淆的恶意软件，旨在窃取加密货币。

分析显示，这些伪造星级的活动在 2024 年达到顶峰，当年 7 月，超过 15.8%的获得 50 个或更多星级的存储库参与了欺诈活动。其中许多存储库在被发现后已被删除，但这一问题的规模凸显了采取应对措施的迫切性。

为了应对这一日益严重的问题，研究人员开发了 StarScout，这是一种可扩展的工具，能够识别明星行为的异常模式。它采用了两种核心检测策略：

1. **低活动签名：** 识别那些只在最低数量的资源库中启动后就不再活跃的账户。
2. **锁定签名：** 检测在短时间内针对特定资源库的账户组的协调活动。

这种方法使研究小组能够发现假冒明星高度集中的资源库，同时将误报率降到最低。

这些发现使人们对 GitHub 星级作为质量或可信度信号的可靠性产生了质疑。研究人员提醒说：“星数是一种不可靠的质量信号，不应用于高风险决策。”

对于GitHub的平台管理者，研究建议采用加权流行度量标准并加强检测机制，以更好地识别和消除欺诈活动。随着软件供应链越来越依赖开源组件，确保星级等信任信号的完整性至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/unmasking-fraudulent-popularity-study-exposes-4-5-million-fake-stars-on-github/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303233](/post/id/303233)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/unmasking-fraudulent-popularity-study-exposes-4-5-million-fake-stars-on-github/)

如若转载,请注明出处： <https://securityonline.info/unmasking-fraudulent-popularity-study-exposes-4-5-million-fake-stars-on-github/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**3赞

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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