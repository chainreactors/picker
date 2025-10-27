---
title: 软件供应链攻击导致 Solana 的 web3.js 库在 npm 注册表上出现恶意版本
url: https://www.anquanke.com/post/id/302473
source: 安全客-有思想的安全新媒体
date: 2024-12-06
fetch_date: 2025-10-06T19:33:50.307826
---

# 软件供应链攻击导致 Solana 的 web3.js 库在 npm 注册表上出现恶意版本

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

# 软件供应链攻击导致 Solana 的 web3.js 库在 npm 注册表上出现恶意版本

阅读量**66405**

发布时间 : 2024-12-05 15:11:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/>

译文仅供参考，具体内容表达以及含义原文为准。

一次软件供应链攻击导致在 npm 注册表上发布了恶意版本的 Solana web3.js 库。

与最近发生的 Lottie Player 供应链泄露事件一样，这次攻击据说也是由于 npm.js 账户凭据被泄露（钓鱼）而导致的。

**发生了什么？**

“今天早些时候，@solana/web3.js 的一个发布访问账户被入侵，这是 Solana [去中心化应用程序] 常用的 JavaScript 库。这使得攻击者可以发布未经授权和恶意修改的软件包，从而窃取私钥材料，并从直接处理私钥的 dapp（如机器人）中抽走资金，”该库的维护者之一 Steven Luscher 周二证实。

“这不是 Solana 协议本身的问题，而是特定 JavaScript 客户端库的问题，而且似乎只影响直接处理私钥的项目，以及在 2024 年 12 月 2 日星期二下午 3:20 UTC 和晚上 8:25 UTC 窗口内更新的项目。”

该库的 1.95.6 和 1.95.7 版本已受到攻击，并已 “解除发布”。1.95.8版本是Solana应用程序开发人员被要求升级到的 “干净 ”版本。

Luscher 总结说：“开发人员如果怀疑自己的密钥可能被泄露，应该轮换任何可疑的授权密钥，包括多重加密、程序授权、服务器密钥对等。”

**影响**

SaaS云监控公司Datadog的安全研究员Christophe Tafani-Dereeper解释了被入侵的库版本中注入的恶意代码是如何通过CloudFlare标头渗出私钥的。

Helius 首席执行官默特-蒙塔兹（Mert Mumtaz）表示，这次攻击的影响尚未显现，不过看起来主要的钱包和应用程序都没有受到影响。

他说：“一般来说，钱包应该不会受到影响，因为它们不会暴露私钥–最大的影响是在后台（即不面向用户）运行JS机器人的人，如果他们在规定时间内（补丁发布前的最后几个小时）更新到这个版本，那么这些服务器上的私钥\*\*会受到影响。”

“如果您是 Solana 开发人员，请立即检查您的软件包，确保现在或将来都不会使用这些版本，尤其是检查任何自动化程序。”

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302473](/post/id/302473)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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