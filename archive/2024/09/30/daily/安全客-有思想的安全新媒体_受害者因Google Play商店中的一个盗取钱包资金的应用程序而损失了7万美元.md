---
title: 受害者因Google Play商店中的一个盗取钱包资金的应用程序而损失了7万美元
url: https://www.anquanke.com/post/id/300515
source: 安全客-有思想的安全新媒体
date: 2024-09-30
fetch_date: 2025-10-06T18:20:00.568206
---

# 受害者因Google Play商店中的一个盗取钱包资金的应用程序而损失了7万美元

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

# 受害者因Google Play商店中的一个盗取钱包资金的应用程序而损失了7万美元

阅读量**339344**

发布时间 : 2024-09-29 15:51:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 康纳·琼斯，文章来源：theregister

原文地址：<https://www.theregister.com/2024/09/26/victims_lose_70k_to_play/>

译文仅供参考，具体内容表达以及含义原文为准。

一长串耗尽加密货币钱包的攻击中的最新一次已经从下载了狡猾应用程序的人那里窃取了 70,000 美元，研究人员将其描述为世界首创。

一款欺诈性应用程序以 Google Play 商店上的 web3 用户为目标，利用合法 WalletConnect 协议的名称和声誉，该协议用于连接去中心化应用程序和钱包。它在 Play 商店中也没有官方应用程序。

> CPR 指出，在该应用的 150 名左右受害者中，只有 20 人费心在 Play 商店留下负面评论……

Check Point Research （CPR） 的调查人员表示，这款名为 WalletConnect 并在应用磁贴图像中使用了开源项目的官方徽标的应用程序，是同类产品中第一个专门针对移动用户的消耗器。

该应用程序背后的攻击者显然非常了解他们的市场。他们明白，使用真实 WalletConnect 协议的人遇到的常见问题包括版本兼容性和常用钱包缺乏对协议的普遍支持。

CPR 表示，这款欺诈性应用程序将自己宣传为解决这些问题的简单解决方案，并且在 Play 商店中没有官方应用程序，再加上一连串的虚假评论证明了其有效性，它准备愚弄相当多的用户。事实上，他们中有 10,000 多人。

这并不是说这些下载都导致他们成为受害者。实际上远非如此。CPR 验证了与 150 多个地址相关的交易，这表明这是钱包被突袭的人数。

下载该应用程序后，系统会提示受害者链接他们装满加密货币的钱包，前提是它是值得信赖的，并且可以更顺畅、更安全地访问受支持的 web3 应用程序。

![Infographic representation of the attack chain - courtesy of Check Point Research]( "Infographic representation of the attack chain - courtesy of Check Point Research")

攻击链的信息图表示 – 由 Check Point Research 提供

然后，他们被指示在选择钱包后授权各种交易。选择钱包会触发应用程序将受害者引导至恶意网站，该网站将捕获有关钱包本身、区块链和已知地址的详细信息。

利用智能合约的机制，攻击者可以授权将代币从受害者的钱包转移到他们自己的钱包中，从而优先转移更有价值的加密货币代币，而不是价值较低的加密货币代币。

CPR 指出，在该应用的 150 名左右的受害者中，只有 20 人费心在 Play 商店留下负面评论——这种冷漠让它背后的不法分子有机会发布大量虚假的正面评论，淹没了受害者的声音。

该应用程序于 3 月推出，直到五个月后才被权力发现其真正用途，此时它立即从 Play 商店中删除。

CPR 网络安全、研究和创新经理 Alexander Chailytko 表示：“这一事件为整个数字资产社区敲响了警钟，因为 Google Play 上第一款移动加密消耗器应用程序的出现标志着网络犯罪分子使用的策略的重大升级以及去中心化金融中网络威胁形势的快速发展。

“这项研究凸显了对先进的人工智能驱动型安全解决方案的迫切需求，这些解决方案可以检测和防止此类复杂的威胁。用户和开发人员都必须随时了解情况并采取积极措施来保护他们的数字资产。

尽管 Google 声称在向 Android 用户提供应用程序之前有严格的审查流程，但我们仍然经常听到顽皮的应用程序进入设备。

不过，将应用程序旁加载到 Android 手机上的能力在这方面起着重要作用。

事实上，就在本周，卡巴斯基曝光了一项活动，据估计，有 1100 万 Android 用户下载了秘密加载了 Necro 恶意软件的应用程序，这些恶意软件通过虚假订阅费用从用户那里窃取了钱财。

谷歌发言人在回应调查结果时表示：“在报告发布之前，本报告发现的所有恶意应用程序都已从 Google Play 中删除。

“Google Play Protect 会自动保护 Android 用户免受此恶意软件的已知版本的侵害，默认情况下，在具有 Google Play 服务的 Android 设备上是打开的。Google Play Protect 可以警告用户或阻止已知存在恶意行为的应用，即使这些应用来自 Play 以外的来源。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/09/26/victims_lose_70k_to_play/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300515](/post/id/300515)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/09/26/victims_lose_70k_to_play/)

如若转载,请注明出处： <https://www.theregister.com/2024/09/26/victims_lose_70k_to_play/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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