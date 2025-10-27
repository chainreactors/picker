---
title: Exim MTA 中的关键漏洞可能允许攻击者向用户收件箱投递恶意软件
url: https://www.anquanke.com/post/id/297885
source: 安全客-有思想的安全新媒体
date: 2024-07-16
fetch_date: 2025-10-06T17:40:41.784959
---

# Exim MTA 中的关键漏洞可能允许攻击者向用户收件箱投递恶意软件

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

# Exim MTA 中的关键漏洞可能允许攻击者向用户收件箱投递恶意软件

阅读量**62134**

发布时间 : 2024-07-15 12:26:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/165649/hacking/critical-flaw-exim-mta.html>

译文仅供参考，具体内容表达以及含义原文为准。

## Exim 邮件服务器中存在一个严重漏洞，使得攻击者能够将恶意可执行附件传递到邮箱。

攻击者可以利用 Exim 邮件传输代理中跟踪为 CVE-2024-39929（CVSS 评分为 9.1）的严重安全漏洞，将恶意附件传递到目标用户的收件箱。

Exim 是一种广泛使用的邮件传输代理 （MTA），旨在路由、传递和接收电子邮件。Exim 最初是为类 Unix 系统开发的，以其灵活性和可配置性而闻名，允许管理员通过配置文件广泛自定义其行为。

Exim 4.97.1 及以下版本受到一个漏洞的影响，该漏洞会误解多行 RFC 2231 标头文件名。此缺陷允许远程攻击者绕过 $mime\_filename 扩展名阻止保护，从而可能将可执行附件传递到用户邮箱。

该漏洞被跟踪为 CVE-2024-39929，CVSS 评分为 9.1 分（满分 10.0 分）。此问题已在版本 4.98 中得到解决。

“Exim 通过 4.97.1 错误地解析了多行 RFC 2231 标头文件名，因此远程攻击者可以绕过 $mime\_filename 扩展名阻止保护机制，并可能将可执行附件传递到最终用户的邮箱，”公告中写道。

根据网络安全公司 Censys 的数据，有 6,540,044 台面向公众的 SMTP 邮件服务器，其中 4,830,719 台 （~74%） 正在运行 Exim。

Censys 研究人员表示，存在针对此问题的概念验证 （PoC） 漏洞，但目前还没有已知的活跃漏洞利用。

“截至 2024 年 7 月 10 日，Censys 观察到 1,567,109 台公开暴露的 Exim 服务器运行着可能易受攻击的版本（4.97.1 或更早版本），主要集中在美国、俄罗斯和加拿大。到目前为止，有82台面向公众的服务器显示出运行4.98补丁版本的迹象。

该公司发布了一组查询，允许识别运行受此 CVE 影响的潜在易受攻击版本的 Censys 可见的面向公众的 Exim 实例。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/165649/hacking/critical-flaw-exim-mta.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297885](/post/id/297885)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/165649/hacking/critical-flaw-exim-mta.html)

如若转载,请注明出处： <https://securityaffairs.com/165649/hacking/critical-flaw-exim-mta.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25

### 热门推荐

文章目录

* [Exim 邮件服务器中存在一个严重漏洞，使得攻击者能够将恶意可执行附件传递到邮箱。](#h2-0)

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