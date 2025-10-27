---
title: 微软发现具有高级混淆策略的新XCSSET macOS恶意软件变体
url: https://www.anquanke.com/post/id/304510
source: 安全客-有思想的安全新媒体
date: 2025-02-20
fetch_date: 2025-10-06T20:33:12.067026
---

# 微软发现具有高级混淆策略的新XCSSET macOS恶意软件变体

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

# 微软发现具有高级混淆策略的新XCSSET macOS恶意软件变体

阅读量**57870**

|评论**1**

发布时间 : 2025-02-19 15:17:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/microsoft-uncovers-new-xcsset-macos.html>

译文仅供参考，具体内容表达以及含义原文为准。

微软表示，在对野外有限的攻击活动进行监测时，发现了一种已知的苹果 macOS 恶意软件 XCSSET 的新变种。

微软威胁情报团队在 X 平台（原推特）上发布的一篇文章中称：“这是自 2022 年以来该恶意软件的首个已知变种，最新的 XCSSET 恶意软件具备更强的混淆手段、更新的持久化机制以及新的感染策略。”

“这些增强的功能在该恶意软件家族先前已知的能力基础上更进一步，比如攻击数字钱包、从便笺应用程序中收集数据，以及窃取系统信息和文件等。”

XCSSET 是一种复杂的模块化 macOS 恶意软件，已知它通过感染苹果 Xcode 项目来攻击用户。2020 年 8 月，趋势科技首次记录了该恶意软件。

后续发现的该恶意软件迭代版本能够适应并攻击更新版本的 macOS 系统以及苹果自家的 M1 芯片组。2021 年年中，这家网络安全公司指出，XCSSET 已更新，能够从谷歌浏览器、电报、印象笔记、欧朋浏览器、Skype、微信以及苹果的第一方应用程序（如通讯录和便笺）等各种应用程序中窃取数据。

同一时期，Jamf 公司的另一份报告显示，该恶意软件能够利用 CVE-2021-30713 漏洞（这是一个透明度、同意和控制（TCC）框架绕过漏洞）作为零日漏洞，在无需额外权限的情况下对受害者的桌面进行截图。

一年多后，它再次更新，增加了对 macOS Monterey 系统的支持。截至撰写本文时，该恶意软件的来源仍然未知。

微软的最新发现标志着自 2022 年以来的首次重大更新，该变种使用了改进的混淆方法和持久化机制，目的是增加分析难度，并确保每次启动新的 shell 会话时恶意软件都会被启动。

XCSSET 设置持久化的另一种新方式是从命令控制服务器下载一个已签名的 dockutil 实用工具，用于管理程序坞中的项目。

微软表示：“然后，该恶意软件会创建一个虚假的启动台应用程序，并将程序坞中合法启动台的路径条目替换为这个虚假的条目。这就确保了每次从程序坞启动启动台时，合法的启动台和恶意负载都会被执行。”

鉴于 XCSSET 是通过受感染的项目传播的，建议用户在使用从代码库下载或克隆的任何 Xcode 项目之前，务必检查并验证其安全性。同时也建议仅从可信来源（如软件平台的官方应用商店）安装应用程序。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/microsoft-uncovers-new-xcsset-macos.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304510](/post/id/304510)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/microsoft-uncovers-new-xcsset-macos.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/microsoft-uncovers-new-xcsset-macos.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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