---
title: 警惕！X 平台将 Signal.me 链接标记为恶意，屏蔽行为引猜测
url: https://www.anquanke.com/post/id/304411
source: 安全客-有思想的安全新媒体
date: 2025-02-19
fetch_date: 2025-10-06T20:36:06.970228
---

# 警惕！X 平台将 Signal.me 链接标记为恶意，屏蔽行为引猜测

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

# 警惕！X 平台将 Signal.me 链接标记为恶意，屏蔽行为引猜测

阅读量**67573**

发布时间 : 2025-02-18 10:31:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/x-now-blocks-signal-contact-links-flags-them-as-malicious/>

译文仅供参考，具体内容表达以及含义原文为准。

![X]()

社交媒体平台 X（原推特）目前正在屏蔽指向 “Signal.me” 的链接，这是加密通讯应用程序 Signal 用于与他人分享账号信息的一个网址。

据 BleepingComputer的测试以及其他用户的报告显示，无论是通过公开帖子、私信还是个人资料简介来发布 Signal.me 的链接，都会收到错误提示，称存在垃圾信息或恶意软件风险。

当发送 Signal.me 链接时显示的一条错误提示内容为：“此请求看起来可能是自动操作。为了保护我们的用户免受垃圾信息和其他恶意活动的侵扰，我们目前无法完成此操作。请稍后重试。”

正如我们下面的测试所示，只有明确包含网址 “signal.me” 的消息才会被屏蔽。

![Failure when attempting to DM Signal.me links]()

尝试通过私信发送 Signal.me 链接时失败
来源：BleepingComputer

最先报道这一问题的记者马特・宾德（Matt Binder）表示，目前尚不清楚该平台从何时开始有这种屏蔽行为。

宾德在他的报道中解释道：“目前尚不清楚 X 平台是从何时开始屏蔽‘Signal.me’链接的。”

“不过，这似乎是一个相当近期的变化，因为此前用户能够在公开帖子和个人资料简介中添加‘Signal.me’链接。其他 Signal 的链接，比如Signal.org，似乎并未被屏蔽。”

与 Signal 相关的其他网址，比如 Signal.link 和 Signal.group 的链接，似乎并未受到此次屏蔽的影响。此外，像 Telegram 等第三方通讯服务的其他联系人链接仍可以像往常一样在 X 平台上分享。

与此同时，在屏蔽措施实施之前就已经发布在 X 平台上的 Signal.me 链接仍然可以点击。不过，用户在点击这些链接时会看到一条警告，提示该链接可能不安全。

![Warning message used for existing links]()

用于已存在链接的警告信息
来源：BleepingComputer

**原因不明**

Signal.me 链接是 Signal 通讯应用程序生成的独特网址，用户可以通过这些链接与他人分享自己的联系方式，以便他人能轻松地在 Signal 上与他们取得联系。

这些链接让人们无需手动交换电话号码就能更便捷地建立联系，为发起对话提供了一种私密且安全的方式。

研究员汤米・米斯克（Tommy Mysk）是本周末最先发现这一问题的人员之一，他告诉 BleepingComputer，目前尚不清楚采取这一行动背后的原因。

米斯克称：“我是偶然发现这个情况的。我无法猜测原因，但这种行为看起来与他们封禁 Mastodon 链接时非常相似。”

2023 年，埃隆・马斯克（Elon Musk）收购推特后，这个社交媒体平台开始屏蔽指向竞争平台的链接，比如脸书（Facebook）、照片墙（Instagram）和长毛象（Mastodon）。在用户抗议后，这一举措很快就被撤回了。

最近，马斯克因他所领导的美国政府部门——政府效率部（DOGE）获取了多个美国政府机构的数据而受到批评。

据报道，Signal 作为一款广受欢迎的端到端加密通讯应用程序，被联邦雇员广泛用于向记者举报美国政府效率部的违规行为。

因此，有人猜测 X 平台屏蔽 Signal.me 链接是出于政治动机。然而，X 平台尚未就这些屏蔽措施发表任何声明，也未回应置评请求。

BleepingComputer已联系 Signal 公司，请其就这一情况发表评论，我们一收到回复就会更新这篇报道。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/x-now-blocks-signal-contact-links-flags-them-as-malicious/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304411](/post/id/304411)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/x-now-blocks-signal-contact-links-flags-them-as-malicious/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/x-now-blocks-signal-contact-links-flags-them-as-malicious/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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