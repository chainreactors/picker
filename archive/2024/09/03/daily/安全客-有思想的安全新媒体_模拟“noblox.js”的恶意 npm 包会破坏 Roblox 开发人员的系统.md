---
title: 模拟“noblox.js”的恶意 npm 包会破坏 Roblox 开发人员的系统
url: https://www.anquanke.com/post/id/299708
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:24:03.295011
---

# 模拟“noblox.js”的恶意 npm 包会破坏 Roblox 开发人员的系统

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

# 模拟“noblox.js”的恶意 npm 包会破坏 Roblox 开发人员的系统

阅读量**79743**

发布时间 : 2024-09-02 16:48:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html>

译文仅供参考，具体内容表达以及含义原文为准。

Roblox 开发人员是一场持续活动的目标，该活动试图通过伪造的 npm 包破坏系统，这再次强调了威胁行为者如何继续利用对开源生态系统的信任来传递恶意软件。

“通过模仿流行的’noblox.js’库，攻击者发布了数十个旨在窃取敏感数据和破坏系统的软件包，”Checkmarx 研究员 Yehuda Gelb 在一份技术报告中说。

ReversingLabs 于 2023 年 8 月首次记录了有关该活动的详细信息，作为一项活动的一部分，该活动提供了一个名为 Luna Token Grabber 的窃取程序，它表示这是 2021 年 10 月“两年前发现的攻击的重播”。

自今年年初以来，另外两个名为 noblox.js-proxy-server 和 noblox-ts 的软件包被确定为恶意软件包，并冒充流行的 Node.js 库来提供窃取恶意软件和名为 Quasar RAT 的远程访问木马。

“该活动的攻击者采用了包括品牌劫持、组合抢注和劫持星权在内的技术，为他们的恶意包创造了一种令人信服的合法性假象，”Gelb 说，

为此，通过将包命名为 noblox.js-async、noblox.js-thread、noblox.js-threads 和 noblox.js-api，这些包被赋予了合法性的外衣，给毫无戒心的开发人员留下了这些库与合法的 “noblox.js” 包相关的印象。

软件包下载统计数据如下 –

* noblox.js-async （74 下载）
* noblox.js线程 （117 次下载）
* noblox.js 线程 （64 次下载）
* noblox.js-API （64 下载）

采用的另一种技术是 starjacking，其中虚假软件包将源存储库列为实际 noblox.js 库的源代码库，以使其看起来更有信誉。

![]()

嵌入在最新版本中的恶意代码充当网关，用于提供 GitHub 存储库上托管的其他有效负载，同时窃取 Discord 令牌，更新 Microsoft Defender Antivirus 排除列表以逃避检测，并通过 Windows 注册表更改设置持久性。

“恶意软件有效性的核心是其持久性方法，利用 Windows 设置应用程序来确保持续访问，”Gelb 指出。“因此，每当用户尝试打开 Windows 设置应用程序时，系统都会无意中执行恶意软件。”

攻击链的最终目标是部署 Quasar RAT，使攻击者能够远程控制受感染的系统。收集到的信息使用 Discord webhook 泄露到攻击者的命令和控制 （C2） 服务器。

这些发现表明，尽管采取了删除措施，但仍有源源不断的新程序包被发布，这使得开发人员必须对持续的威胁保持警惕。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299708](/post/id/299708)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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