---
title: Tinyproxy 严重漏洞导致超过 50,000 台主机可以远程执行代码
url: https://www.anquanke.com/post/id/296259
source: 安全客-有思想的安全新媒体
date: 2024-05-09
fetch_date: 2025-10-06T17:13:52.599795
---

# Tinyproxy 严重漏洞导致超过 50,000 台主机可以远程执行代码

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

# Tinyproxy 严重漏洞导致超过 50,000 台主机可以远程执行代码

阅读量**68465**

发布时间 : 2024-05-08 10:47:17

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html>

译文仅供参考，具体内容表达以及含义原文为准。

90,310 台主机中超过 50% 被发现在互联网上暴露了Tinyproxy 服务，该服务容易受到 HTTP/HTTPS 代理工具中未修补的严重安全漏洞的影响。

该问题被追踪为CVE-2023-49606，根据 Cisco Talos 的 CVSS 评分为 9.8 分（满分 10 分），该问题将其描述为影响版本 1.10.0 和 1.11.1 的释放后使用错误。后者是最新版本。

Talos在上周的一份公告中表示： “特制的 HTTP 标头可能会触发先前释放的内存的重用，从而导致内存损坏并可能导致远程代码执行。” “攻击者需要发出未经身份验证的 HTTP 请求才能触发此漏洞。”

换句话说，未经身份验证的威胁参与者可以发送特制的HTTP 连接标头来触发内存损坏，从而导致远程代码执行。

根据攻击面管理公司 Censys 共享的数据，截至 2024 年 5 月 3 日，在向公共互联网公开 Tinyproxy 服务的 90,310 台主机中，其中 52,000 台（约 57%）运行着存在漏洞的 Tinyproxy 版本。

大多数可公开访问的主机位于美国（32,846）、韩国（18,358）、中国（7,808）、法国（5,208）和德国（3,680）。

Talos 于 2023 年 12 月 22 日报告了该问题，还发布了该缺陷的概念验证 (PoC)，描述了如何利用解析 HTTP Connection 连接的问题来触发崩溃，并且在某些情况下，代码执行。

Tinyproxy 的维护者在周末做出的一系列承诺中，指责 Talos 将报告发送到可能“过时的电子邮件地址”，并补充说，Debian Tinyproxy 软件包维护者于 2024 年 5 月 5 日通知了他们。

“没有提交 GitHub 问题，也没有人提到提到的 IRC 聊天中的漏洞，”rofl0r在提交中说。 “如果这个问题在 Github 或 IRC 上报告，这个错误就会在一天之内得到修复。”

**更新**
建议用户从 git 拉取最新的 master 分支，或者手动将上述提交作为版本 1.11.1 的补丁应用，直到 Tinyproxy 1.11.2 可用。还建议不要将 Tinyproxy 服务暴露在公共互联网上。

本文翻译自 [原文链接](https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296259](/post/id/296259)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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