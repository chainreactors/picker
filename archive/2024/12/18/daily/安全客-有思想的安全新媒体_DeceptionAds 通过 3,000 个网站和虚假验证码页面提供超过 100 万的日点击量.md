---
title: DeceptionAds 通过 3,000 个网站和虚假验证码页面提供超过 100 万的日点击量
url: https://www.anquanke.com/post/id/302770
source: 安全客-有思想的安全新媒体
date: 2024-12-18
fetch_date: 2025-10-06T19:33:11.024833
---

# DeceptionAds 通过 3,000 个网站和虚假验证码页面提供超过 100 万的日点击量

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

# DeceptionAds 通过 3,000 个网站和虚假验证码页面提供超过 100 万的日点击量

阅读量**49213**

|评论**1**

发布时间 : 2024-12-17 14:10:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/deceptionads-delivers-1m-daily.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员揭示了与 ClickFix 式攻击相关的一个以前未记录的方面，这种攻击依赖于利用单一的广告网络服务，作为被称为 DeceptionAds 的恶意广告驱动的信息窃取活动的一部分。

Guardio Labs 负责人 Nati Tal 在与 The Hacker News 分享的一份报告中说：“该活动完全依赖于单一广告网络进行传播，展示了恶意广告的核心机制–（在过去十天内）每天提供超过 100 万次‘广告印象’，并通过 3000 多个内容网站的流量输送网络，每天导致数千名受害者丢失账户和金钱。”

最近几个月，多家网络安全公司记录了这些活动，其中包括将盗版电影网站和其他网站的访问者引导到假的验证码验证页面，指示他们复制并执行 Base64 编码的 PowerShell 命令，最终导致部署 Lumma 等信息窃取程序。

这种攻击已不再局限于单个行为者，Proofpoint 最近指出，多个 “非归属 ”威胁集群已采用巧妙的社交工程方法来传播远程访问木马、窃取程序，甚至是 Brute Ratel C4 等后剥削框架。

Guardio Labs 表示，它能够追踪到活动的源头 Monetag，该平台声称提供多种广告格式来 “为网站、社交流量、Telegram Mini Apps 盈利”，威胁行为者还利用 BeMob 广告跟踪等服务来掩盖其恶意意图。Infoblox 还以 Vane Viper 和 Omnatuor 的名称跟踪 Monetag。

该活动可有效归结为：网站所有者（即威胁行为者）在 Monetag 注册后，流量会被重定向到由恶意广告网络运营的流量分发系统 (TDS)，最终将访问者带到验证码验证页面。

塔尔解释说：“通过向Monetag的广告管理系统提供一个良性的BeMob URL，而不是直接的虚假验证码页面，攻击者利用了BeMob的声誉，使Monetag的内容审核工作变得更加复杂。这个BeMob TDS最终重定向到恶意验证码页面，托管在Oracle Cloud、Scaleway、Bunny CDN、EXOScale甚至Cloudflare的R2等服务上。”

在负责任的披露之后，Monetag 已经删除了 200 多个与该威胁行为者有关联的账户。BeMob 也采取了类似措施，删除了用于隐身的账户。尽管如此，有迹象表明，截至 2024 年 12 月 5 日，该活动已再次恢复。

调查结果再次凸显了内容审核和强大的账户验证以防止虚假注册的必要性。

“从提供盗版或点击诱饵内容的欺骗性出版商网站到复杂的重定向链和隐形技术，这次活动凸显了为合法目的而设计的广告网络是如何被用于恶意活动的，”塔尔说。

“其结果是责任链支离破碎，广告网络、出版商、广告统计服务和托管服务提供商各司其职，却往往逃避责任。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/deceptionads-delivers-1m-daily.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302770](/post/id/302770)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/deceptionads-delivers-1m-daily.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/deceptionads-delivers-1m-daily.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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