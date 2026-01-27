---
title: 破坏与野外利用：LA-Studio Element Kit中发现严重后门
url: https://www.anquanke.com/post/id/314510
source: 安全客-有思想的安全新媒体
date: 2026-01-26
fetch_date: 2026-01-27T03:36:58.237893
---

# 破坏与野外利用：LA-Studio Element Kit中发现严重后门

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

# 破坏与野外利用：LA-Studio Element Kit中发现严重后门

阅读量**25858**

发布时间 : 2026-01-26 14:13:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/sabotage-exploited-in-the-wild-critical-backdoor-found-in-la-studio-element-kit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

WordPress 社区近日遭遇一起严重安全事件：在 **LA-Studio Element Kit for Elementor** 插件中发现了一个**后门漏洞**。该插件在超过 **20,000 个网站**上运行。漏洞编号为 **CVE-2026-0920**，CVSS 评分高达 **9.8（严重）**，允许**未授权攻击者**立即创建管理员账号，从而完全接管受影响网站。

但与普通编码错误导致的漏洞不同，这个漏洞似乎是**蓄意破坏行为**。

漏洞被发现后，插件厂商做出了令人震惊的承认：恶意代码是由**前员工植入**的。

“厂商在回应我们的询问时表示，一名前雇员将后门代码添加到了插件中。”Wordfence 的报告指出。时间点非常关键：该开发者在 12 月底离职，而 “对后门的最后一次修改正是在那个时候”，这表明代码是在其离职前不久被改动的。

后门被隐藏在插件的用户注册处理逻辑中。技术分析显示，`ajax_register_handle()` 函数包含 “将管理员权限添加到新用户的混淆代码”。

攻击者只需发送一个包含特定参数 **`lakit_bkrole`** 的注册请求即可触发该后门。代码被刻意混淆以避免被发现。研究人员指出：“特别值得注意的是，该功能明显经过混淆处理，这似乎是为了逃避检测。”

此次事件的后果极其严重。“一旦攻击者获得 WordPress 网站的管理员权限，他们就能像普通管理员一样操纵目标网站上的任何内容。” 包括上传恶意文件、注入垃圾内容或将访问者重定向到危险网站。

目前已在野外检测到攻击活动。Wordfence 在过去 24 小时内就拦截了 **216 次**针对该漏洞的攻击。

在 2026 年 1 月 13 日收到 Wordfence 的通知后，LA-Studio 团队迅速采取行动，于次日发布了补丁。

用户被敦促**立即升级到 1.6.0 版本**以移除后门。这一事件为科技公司敲响了警钟：“它提醒我们必须重视内部威胁，并在员工离职时确保有适当的控制和检查机制。”

本文翻译自securityonline [原文链接](https://securityonline.info/sabotage-exploited-in-the-wild-critical-backdoor-found-in-la-studio-element-kit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314510](/post/id/314510)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sabotage-exploited-in-the-wild-critical-backdoor-found-in-la-studio-element-kit/)

如若转载,请注明出处： <https://securityonline.info/sabotage-exploited-in-the-wild-critical-backdoor-found-in-la-studio-element-kit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **960**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30

### 相关文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30
* ##### [Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备](/post/id/314522)

  2026-01-26 14:12:18
* ##### [CVE-2026-22822：External Secrets Operator严重漏洞破坏命名空间隔离机制](/post/id/314529)

  2026-01-26 14:11:37
* ##### [Google推出「个人智能」AI模式，打造专属个性化搜索体验](/post/id/314541)

  2026-01-26 14:07:37

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