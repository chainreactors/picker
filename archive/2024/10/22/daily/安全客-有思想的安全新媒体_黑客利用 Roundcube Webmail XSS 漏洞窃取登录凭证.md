---
title: 黑客利用 Roundcube Webmail XSS 漏洞窃取登录凭证
url: https://www.anquanke.com/post/id/301087
source: 安全客-有思想的安全新媒体
date: 2024-10-22
fetch_date: 2025-10-06T18:48:05.455113
---

# 黑客利用 Roundcube Webmail XSS 漏洞窃取登录凭证

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

# 黑客利用 Roundcube Webmail XSS 漏洞窃取登录凭证

阅读量**74423**

发布时间 : 2024-10-21 10:58:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，不明威胁行为者试图利用开源 Roundcube 网络邮件软件中一个现已打补丁的安全漏洞，作为旨在窃取用户凭证的网络钓鱼攻击的一部分。

俄罗斯网络安全公司 Positive Technologies 称，该公司上个月发现有人向独立国家联合体（独联体）国家的一个未指定的政府组织发送了一封电子邮件。但值得注意的是，该邮件最初是在 2024 年 6 月发送的。

“本周早些时候发布的一份分析报告称：”这封电子邮件似乎是一封没有文本的邮件，只包含一份附件文档。

“然而，电子邮件客户端并没有显示附件。邮件正文包含带有语句 eval(atob(……)) 的独特标签，可解码并执行 JavaScript 代码”。

根据 Positive Technologies 的说法，该攻击链试图利用 CVE-2024-37383（CVSS 得分：6.1），这是一个通过 SVG animate 属性存储的跨站脚本 (XSS) 漏洞，允许在受害者网络浏览器的上下文中执行任意 JavaScript。

换句话说，远程攻击者只需诱使电子邮件收件人打开特制邮件，即可加载任意 JavaScript 代码并访问敏感信息。截至 2024 年 5 月，该问题已在 1.5.7 和 1.6.7 版本中得到解决。

“Positive Technologies 指出：“通过插入 JavaScript 代码作为 ”href “的值，每当 Roundcube 客户端打开恶意电子邮件时，我们就可以在 Roundcube 页面上执行该代码。

在这种情况下，JavaScript 有效载荷会保存空的 Microsoft Word 附件（“Road map.docx”），然后使用 ManageSieve 插件从邮件服务器获取邮件。它还会在显示给用户的 HTML 页面中显示登录表单，以欺骗受害者提供他们的 Roundcube 凭据。

在最后阶段，捕获的用户名和密码信息会外泄到 Cloudflare 托管的远程服务器（“libcdn[.]org”）。

目前尚不清楚是谁在幕后操纵这一漏洞利用活动，但此前在 Roundcube 中发现的漏洞已被 APT28、Winter Vivern 和 TAG-70 等多个黑客组织滥用。

该公司表示：“虽然 Roundcube Webmail 可能不是使用最广泛的电子邮件客户端，但由于政府机构普遍使用，它仍然是黑客攻击的目标。对该软件的攻击可能会导致重大损失，使网络犯罪分子得以窃取敏感信息。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301087](/post/id/301087)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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