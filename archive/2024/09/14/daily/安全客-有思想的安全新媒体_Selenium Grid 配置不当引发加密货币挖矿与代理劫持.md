---
title: Selenium Grid 配置不当引发加密货币挖矿与代理劫持
url: https://www.anquanke.com/post/id/300067
source: 安全客-有思想的安全新媒体
date: 2024-09-14
fetch_date: 2025-10-06T18:24:08.690716
---

# Selenium Grid 配置不当引发加密货币挖矿与代理劫持

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

# Selenium Grid 配置不当引发加密货币挖矿与代理劫持

阅读量**89521**

发布时间 : 2024-09-13 15:12:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html>

译文仅供参考，具体内容表达以及含义原文为准。

互联网上暴露的 Selenium Grid 实例正成为不良行为者非法加密货币挖矿和代理劫持活动的目标。

“Selenium Grid 是一个服务器，有助于跨不同浏览器和版本并行运行测试用例，”Cado Security 研究人员 Tara Gould 和 Nate Bill 在今天发表的分析中说。

“但是，Selenium Grid 的默认配置缺乏身份验证，使其容易受到威胁行为者的利用。”

云安全公司 Wiz 此前曾在 2024 年 7 月下旬强调滥用可公开访问的 Selenium Grid 实例来部署加密矿工，作为名为 SeleniumGreed 的活动集群的一部分。

Cado 观察到针对其蜜罐服务器的两种不同的活动，并表示威胁行为者正在利用缺乏身份验证保护来执行恶意操作。

第一个版本利用“goog：chromeOptions”字典注入一个 Base64 编码的 Python 脚本，该脚本反过来检索一个名为“y”的脚本，该脚本是开源的 GSocket 反向 shell。![加密挖矿和代理劫持](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi45nDi2KGBe76rfXK9fWqnYav6fkHQMv5WckJ9C_xrhx5Ubg_9b5gpIRWVkMBj4UjXPUS26Ms-K2VTnvUvVlPRQDGxMrWDUIdOYA0Oops1ObH8ta19HmujuIcWdneaC8Ncuw7Yi9BzsmvulnP53on8p9r8YTI7dnVSmJ1pAi7r_qEDBaX2cwqaP7lH0ysT/s728-rw-e365/unnamed.png "Crypto Mining and Proxyjacking")

反向 shell 随后用作引入下一阶段有效负载的媒介，一个名为“pl”的 bash 脚本，该脚本通过 curl 和 wget 命令从远程服务器检索 IPRoyal Pawn 和 EarnFM。

“IPRoyal Pawns 是一种住宅代理服务，允许用户出售他们的互联网带宽以换取金钱，”Cado 说。

“用户的互联网连接与 IPRoyal 网络共享，该服务使用带宽作为住宅代理，使其可用于各种目的，包括恶意目的。”

EarnFM 也是一种代理软件解决方案，被宣传为一种“开创性”的方式，可以“通过简单地共享您的互联网连接在线产生被动收入”。

第二种攻击，与代理劫持活动一样，遵循相同的路线，通过 Python 脚本传递 bash 脚本，该脚本检查它是否在 64 位计算机上运行，然后继续丢弃基于 Golang 的 ELF 二进制文件。

ELF 文件随后尝试利用 PwnKit 漏洞 （CVE-2021-4043） 升级到根，并丢弃名为 perfcc 的 XMRig 加密货币挖矿程序。

“由于许多组织依赖 Selenium Grid 进行 Web 浏览器测试，因此该活动进一步凸显了配置错误的实例如何被威胁行为者滥用，”研究人员说。“用户应确保已配置身份验证，因为默认情况下未启用它。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300067](/post/id/300067)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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