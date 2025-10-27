---
title: 再次发现了 mSpy 的漏洞：数百万监控软件购买者的信息曝光
url: https://www.anquanke.com/post/id/297895
source: 安全客-有思想的安全新媒体
date: 2024-07-16
fetch_date: 2025-10-06T17:40:44.348746
---

# 再次发现了 mSpy 的漏洞：数百万监控软件购买者的信息曝光

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

# 再次发现了 mSpy 的漏洞：数百万监控软件购买者的信息曝光

阅读量**78846**

发布时间 : 2024-07-15 12:24:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 布兰登·维利亚罗洛，文章来源：The Register

原文地址：<https://www.theregister.com/2024/07/15/infosec_roundup/>

译文仅供参考，具体内容表达以及含义原文为准。

信息安全简述商业间谍软件制造商 mSpy 再次遭到入侵，从泄露的记录中可以识别出数百万购买者。

mSpy 于 7 月 11 日出现在 Have I Been Pwned 上，该网站透露黑客行动主义者负责从无法使用该软件的买家那里窃取数百万张 Zendesk 支持票。

mSpy 在商业上销售用于包括允许父母和伴侣监视其家庭成员在内的应用程序。它可作为智能手机应用程序使用，通常被称为“跟踪软件”应用程序。

“包括 142GB 的用户数据和支持票证以及 176GB 的五十多万个附件，这些数据包含 2.4M 唯一的电子邮件地址、IP 地址名称和照片，”我在 Have I Been Pwned 上的 mSpy 条目写道。网站附件包括金融交易的屏幕截图、信用卡照片，甚至还有一些裸体自拍照。

已经联系了违规名单中的几个人，并验证了他们数据的合法性，其他地方也有报道。

mSpy 此前曾在 2015 年遭到破坏，约有 400,000 名用户的数据在暗网上发布——消息、付款详细信息、帐户凭据、照片等被在线倾倒。该公司在 2018 年再次遭到入侵，导致数百万条客户记录被泄露。

mSpy 并不是唯一一家遭受数据泄露的跟踪软件公司：LetMeSpy 在 2023 年受到重创以至于关闭，同样的命运也降临在 pcTattletale 身上，该公司在今年早些时候经历了类似的经历后关闭了商店。

### 严重漏洞：您已经听说过最糟糕的情况

上周可能包括补丁星期二，但在过去七天里出现了其他令人讨厌的事情。

美国网络安全和基础设施安全局警告说，OT中修补了许多漏洞，其中最糟糕的是许可证管理服务器软件中的CVSS 10.0，由一家名为PTC的机构制造。

信不信由你，任何人都可以使用它来做任何他们想做的事情。它被跟踪为 CVE-2024-6071。

### Vel-oops：Linksys路由器向亚马逊发送纯文本数据

人们会期望一个 170 美元的 Wi-Fi 网状路由器足够智能，不会在全球范围内以纯文本形式传输 SSID、密码和会话访问令牌——但我们来了。

据比利时非营利组织Test Aankoop的消费者权益倡导者称，Linksys Velop Pro Wi-Fi 6E和7系列路由器正在这样做，并被发现以纯文本形式将所有这些信息从比利时的路由器一直发送到美国的AWS服务器。

Test Aankoop说，这些会话令牌尤其令人担忧，因为它们很容易被中间人攻击所利用。

如果您拥有一台有问题的路由器，最好尽快更新SSID和密码，在这样做的同时，为什么不也更新路由器固件呢？

### 深色图案……到处都是深色图案

一项针对操纵消费者放弃应用程序和网站上数据和隐私的“黑暗模式”的国际审查发现，您可能已经猜到了：它们无处不在。

“作为审查的一部分，近76%的网站和应用程序采用了至少一种可能的黑暗模式，近67%使用了多种可能的黑暗模式，”联邦贸易委员会在与国际消费者保护和执法网络（International Consumer Protection and Enforcement Network）和全球隐私执法网络（Global Privacy Enforcement Network）的伙伴完成审查后警告说。

三人组审查了 642 种语言的网站和应用程序，发现两种模式占主导地位。美国联邦贸易委员会（FTC）声称，偷偷摸摸的做法涉及隐瞒基本信息，直到过程的后期，而当选择以引导买家的方式制定时，可以看到界面干扰。

该报告没有确定发现的任何模式是否上升到非法程度，因此不太可能进行起诉。

### 恶意软件死灵法师在新型攻击中复活 IE

当我们报告上周[修补](https://www.theregister.com/2024/07/10/july_2024_patch_tuesday/)的 Windows MSHTML 中的一个漏洞正在被积极利用时，我们不知道这将是一个新颖的技巧，但根据 Checkpoint 的说法，情况确实如此。

被利用的漏洞 – 一种欺骗漏洞，使攻击者能够在受害者的机器上执行代码 – 正在通过将Internet Explorer从其位于Windows内部的住所中抬起，并利用其不太安全的性质来安装恶意HTML应用程序。

比利用 IE 做肮脏的工作更糟糕的是，Checkpoint 表示它早在 2023 年初就发现了这个东西——所以它已经存在了一段时间。

### Akira 勒索软件组织以拉丁美洲航空公司为目标

黑莓的安全研究人员警告说，勒索软件攻击者 Akira 的潜在新目标：拉丁美洲航空公司。

黑莓本周报道称，一名配备 Akira 勒索软件（作为服务出售）的威胁行为者闯入了一家未具名航空公司的系统，窃取了大量数据并勒索了系统。黑莓的报告中没有说明是否支付了赎金。

研究人员表示，这种不寻常的攻击目标“凸显了该组织愿意针对其他地区，如果任何组织忽视了对行为者使用的已披露漏洞的修补。

也就是说，值得注意的是违规行为是如何发生的：“内部软件也严重过时，一旦边界被攻破，威胁行为者就会利用这些漏洞，”黑莓指出。

本文翻译自The Register [原文链接](https://www.theregister.com/2024/07/15/infosec_roundup/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297895](/post/id/297895)

安全KER - 有思想的安全新媒体

本文转载自: [The Register](https://www.theregister.com/2024/07/15/infosec_roundup/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/15/infosec_roundup/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
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
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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