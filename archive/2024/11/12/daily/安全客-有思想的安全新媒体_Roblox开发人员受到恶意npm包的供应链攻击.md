---
title: Roblox开发人员受到恶意npm包的供应链攻击
url: https://www.anquanke.com/post/id/301697
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:20.487203
---

# Roblox开发人员受到恶意npm包的供应链攻击

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

# Roblox开发人员受到恶意npm包的供应链攻击

阅读量**50558**

发布时间 : 2024-11-11 14:36:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/roblox-developers-targeted-in-supply-chain-attack-with-malicious-npm-packages/>

译文仅供参考，具体内容表达以及含义原文为准。

![Skuld infostealer]()

Socket 的威胁研究团队最近发现了针对 Roblox 开发者社区的新攻击。威胁行为者分发了五个恶意 npm 软件包，包括 node-dlls、ro.dll 和 rolimons-api，这些软件包伪装成平台上开发者广泛使用的合法工具。这次攻击的目的是让开发人员感染 Skuld 信息窃取程序和 Blank Grabber 恶意软件，这些软件包在被删除前已被下载了 320 多次。

攻击者依靠错别字，使用具有欺骗性的软件包名称来冒充可信软件包。例如，他们模仿流行的 node-dll 软件包，发布了一个外观相似的 node-dlls 软件包，而类似的 rolimons-api 软件包则是针对 Roblox 数据集成的著名 API。根据 Socket 的报告，“恶意 npm 软件包包含经过混淆的 JavaScript 代码，旨在从外部源下载和执行恶意可执行文件”。这种混淆使攻击者得以隐藏其恶意意图，并利用毫无戒心的开发人员对熟悉名称的信任。

一旦安装，代码就会执行一系列命令，下载和部署托管在 GitHub 上的恶意软件，而 GitHub 是开发者的常用平台，可以帮助恶意软件绕过安全过滤器。

用 Go 语言编写的 Skuld 信息窃取程序以 Roblox 开发人员的系统为目标，提取敏感信息。Socket 报告说，Skuld “采用了逃避调试、禁用防病毒保护和提升权限的技术，从而可以捕获凭证、cookie 和财务信息”。第二款恶意软件 Blank Grabber 是一款基于 Python 的工具，主要用于窃取 Discord 令牌、浏览器数据甚至加密货币钱包信息。它还包括一个图形用户界面生成器，允许威胁行为者定制其功能，并有可能逃避检测。

为了传递窃取的数据，该恶意软件使用了 Discord webhooks 和 Telegram，这使得检测工作变得更加复杂，因为这两个平台都是可信平台。Socket 的分析强调，“如果平台开发者出于合法目的使用 Discord 和 Telegram 进行 C2 通信，会使检测工作复杂化”。通过利用这些渠道，攻击者可以避免触发传统的安全警报，从而提高攻击的有效性。

Socket 建议开发人员采取积极主动的安全措施，定期监控 npm 软件包是否有被篡改的迹象，并仔细核实软件包名称以避免错字抢注攻击。用他们的话说，“威胁行为者利用信任和人为错误，模仿受信任的软件包，将恶意代码引入应用程序”。

本文翻译自securityonline [原文链接](https://securityonline.info/roblox-developers-targeted-in-supply-chain-attack-with-malicious-npm-packages/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301697](/post/id/301697)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/roblox-developers-targeted-in-supply-chain-attack-with-malicious-npm-packages/)

如若转载,请注明出处： <https://securityonline.info/roblox-developers-targeted-in-supply-chain-attack-with-malicious-npm-packages/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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