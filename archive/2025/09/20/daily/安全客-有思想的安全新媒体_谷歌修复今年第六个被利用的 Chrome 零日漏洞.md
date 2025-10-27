---
title: 谷歌修复今年第六个被利用的 Chrome 零日漏洞
url: https://www.anquanke.com/post/id/312263
source: 安全客-有思想的安全新媒体
date: 2025-09-20
fetch_date: 2025-10-02T20:24:30.165579
---

# 谷歌修复今年第六个被利用的 Chrome 零日漏洞

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

# 谷歌修复今年第六个被利用的 Chrome 零日漏洞

阅读量**76874**

发布时间 : 2025-09-19 18:42:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/google-patches-sixth-chrome-zero-day-exploited-in-attacks-this-year/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌已发布紧急安全更新，用于修复一个 **Chrome 零日漏洞**。这是自今年年初以来，第六个已确认在攻击中被利用的漏洞。

虽然谷歌并未明确说明该漏洞是否仍在野外被积极利用，但公司警告称，漏洞已存在公开的利用程序，这通常意味着漏洞正在被利用。

谷歌在周三发布的安全公告中表示：

> “谷歌已知 CVE-2025-10585 在野外存在利用代码。”

这一高危零日漏洞源于 **V8 JavaScript 引擎中的类型混淆（type confusion）** 弱点，由谷歌威胁分析小组（TAG）于周二报告。

谷歌 TAG 经常揭露政府支持的威胁行为者在间谍软件行动中利用零日漏洞的情况，这类行动通常针对高风险人群，包括但不限于反对派政治人物、异议人士和记者。

谷歌在接到报告一天后，迅速发布了安全更新：

* **Windows/Mac**：140.0.7339.185 / .186
* **Linux**：140.0.7339.185

这些版本将在未来几周内推送至 Chrome 稳定桌面渠道。

虽然 Chrome 会在新补丁可用时自动更新，但用户也可以手动加速更新：进入 **Chrome 菜单 > 帮助 > 关于 Google Chrome**，等待更新完成后点击 **“重新启动”** 按钮即可立即安装补丁。

![]()

尽管谷歌已确认 **CVE-2025-10585** 在攻击中被利用，但尚未公布更多关于野外利用的细节。

谷歌表示：

> “在大多数用户完成更新之前，漏洞细节和相关链接将会保持限制。若该漏洞存在于第三方库且尚未被修复，我们也会继续保留限制。”

这已经是谷歌今年修复的第六个被积极利用的 **Chrome 零日漏洞**，此前五个分别在 **3 月、5 月、6 月和 7 月**被修复。

* **7 月**：谷歌修复了另一个零日漏洞（**CVE-2025-6558**），由 TAG 研究人员发现，攻击者可利用该漏洞逃逸浏览器沙箱。
* **5 月**：谷歌发布紧急更新，修复了可被攻击者用来劫持账户的零日漏洞（**CVE-2025-4664**），并修复了 V8 引擎中的越界读写漏洞（**CVE-2025-5419**），该漏洞同样由 TAG 发现。
* **3 月**：谷歌修复了由卡巴斯基报告的一个严重沙箱逃逸漏洞（**CVE-2025-2783**），该漏洞被用于针对政府机构和媒体的间谍活动。

去年，谷歌还修复了 **10 个零日漏洞**，其中一些在 Pwn2Own 黑客大赛上被演示，另一些则已在攻击中被利用。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/google-patches-sixth-chrome-zero-day-exploited-in-attacks-this-year/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312263](/post/id/312263)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/google-patches-sixth-chrome-zero-day-exploited-in-attacks-this-year/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/google-patches-sixth-chrome-zero-day-exploited-in-attacks-this-year/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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