---
title: Pwn 2 Own：Firefox被JavaScript黑客攻击Zero-Days -漏洞利用的详细信息
url: https://www.anquanke.com/post/id/307562
source: 安全客-有思想的安全新媒体
date: 2025-05-21
fetch_date: 2025-10-06T22:25:32.422446
---

# Pwn 2 Own：Firefox被JavaScript黑客攻击Zero-Days -漏洞利用的详细信息

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

# Pwn 2 Own：Firefox被JavaScript黑客攻击Zero-Days -漏洞利用的详细信息

阅读量**41944**

发布时间 : 2025-05-20 14:48:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pwn2own-firefox-hacked-with-javascript-zero-days-details-on-the-exploits/>

译文仅供参考，具体内容表达以及含义原文为准。

![Firefox 安全, JavaScript 漏洞利用]()

Mozilla已经迅速采取行动,修补了Firefox中两个关键的零日漏洞,这两个漏洞在上周在柏林举行的Pwn2Own 2025黑客竞赛中被利用。

这场备受瞩目的活动以让精英安全研究人员与流行的软件目标对抗而闻名,Firefox通过高级JavaScript引擎漏洞入侵了两次。作为回应,Mozilla发布了Firefox和Firefox ESR的紧急安全更新,在一天内解决了问题。

来自Palo Alto Networks的安全研究人员Edouard Bochin(@le\_douds)和Tao Yan(@Ga1ois)demonstratedvulnerability展示了使用涉及JavaScript Promise对象的超限写入漏洞对Firefox的成功利用。vulnerability此漏洞现在被跟踪为CVE-2025-4918,允许未经授权的内存访问,可能导致代码执行或浏览器崩溃。

![]()

图片来源:Zeroday Initiative

两人的研究为他们赢得了50,000美元和5个Pwn积分大师,这是对杰出Pwn2Own参与者的着名荣誉。

著名的Pwn2Own冠军曼弗雷德·保罗(Manfred Paulexploited)利用了Firefox的渲染器,使用临界整数溢出。该漏洞被跟踪为CVE-2025-4919,它植根于JavaScript数组索引误判,这可能导致超出限制的读或写——升级和远程代码执行的经典路径。

![]()

图片来源:Zeroday Initiative

保罗被授予$ 50,000和5大师Pwn点数,他的创意和精确的攻击向量。

根据Mozilla的说法,这些问题影响了:

* Firefox 版本 前 138.0.4
* Firefox ESR 版本在 128.10.1 之前
* Firefox ESR 版本在 115.23.1 之前

尽管 Streamy Micro 的 Zero Day Initiative (ZDI) 授予了通常的 90 天补丁窗口,Mozilla 仍以紧迫和透明的方式行事。修复程序在公开演示漏洞后不到一周就推出 – 远远早于ZDI的典型披露时间表。vulnerabilities这两个漏洞都强调了现代JavaScript引擎的持续风险,其中只有一个内存操作可能会危及整个浏览器。随着Firefox在个人和企业环境中的广泛使用,这些错误构成了真实而直接的威胁,特别是在熟练的攻击者手中。

所有 Firefox ensure用户都应该确保他们正在运行:

* Firefox 138.0.4 或更高版本
* Firefox ESR 128.10.1 或更高版本
* Firefox ESR 115.23.1 或更高版本

要验证您的版本,请访问菜单 → 帮助 → 关于 Firefox

本文翻译自securityonline [原文链接](https://securityonline.info/pwn2own-firefox-hacked-with-javascript-zero-days-details-on-the-exploits/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307562](/post/id/307562)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pwn2own-firefox-hacked-with-javascript-zero-days-details-on-the-exploits/)

如若转载,请注明出处： <https://securityonline.info/pwn2own-firefox-hacked-with-javascript-zero-days-details-on-the-exploits/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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