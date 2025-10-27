---
title: Kavach 2FA网络钓鱼攻击活动盯上印度政府
url: https://www.anquanke.com/post/id/284727
source: 安全客-有思想的安全新媒体
date: 2022-12-29
fetch_date: 2025-10-04T02:39:18.545923
---

# Kavach 2FA网络钓鱼攻击活动盯上印度政府

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

# Kavach 2FA网络钓鱼攻击活动盯上印度政府

阅读量**141287**

发布时间 : 2022-12-28 10:00:52

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第429期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、Kavach 2FA网络钓鱼攻击活动盯上印度政府

[![]()](https://p0.ssl.qhimg.com/t0182b3493bff6815ce.png)

日前，网络安全公司Securonix披露称，有证据表明一个新的网络钓鱼攻击针对印度政府官员，Securonix将该活动称为STEPPY KAVACH。

据了解，该最新攻击序列需要使用网络钓鱼电子邮件来引诱潜在受害者打开一个快捷文件，并使用mshta.exe加载HTA的有效负载。该公司表示，该HTML应用程序被发现托管在一个可能受损的网站上，嵌套在一个不起眼的目录中，而该网站就是印度德里地区的所得税部门的官方网站。[[阅读原文]](https://thehackernews.com/2022/12/researchers-warn-of-kavach-2fa-phishing.html)

## 2、Linux Kernel爆可远程执行代码“关键”SMB漏洞

[![]()](https://p4.ssl.qhimg.com/t01442f92e514ae81ce.png)

安全专家近日在Linux Kernel中发现了一个“关键”漏洞（ CVSS 评分为9.6分），黑客可以利用该漏洞攻击SMB服务器，在远程执行任意代码。这个漏洞主要发生在启用了ksmbd的SMB服务器上。

KSMBD是一个Linux内核服务器，在内核空间实现SMB3协议，用于通过网络共享文件。一个未经认证的远程攻击者可以利用该漏洞执行任意代码。

ZDI 在公告中表示：“该漏洞允许远程攻击者在受影响的Linux Kernel安装上执行任意代码。只要系统启用了ksmbd 就容易被黑客攻击，而且这个漏洞不需要用户/管理人员认证。更详细的解释是，该漏洞存在于SMB2\_TREE\_DISCONNECT 命令的处理过程中。这个问题是由于操作对某个对象之前，没有验证该对象是否存在。攻击者可以利用该漏洞在内核中执行任意代码”。

该漏洞于2022年7月26日被Thales Group Thalium团队的研究人员Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier 发现。该漏洞于2022年12月22日被公开披露。[[阅读原文]](https://www.ithome.com/0/663/510.htm)

## 3、安全专家警告利用 WordPress 礼品卡插件的攻击

[![]()](https://p0.ssl.qhimg.com/t0170a3999cb3b7e0d9.png)

黑客正在积极利用一个被追踪为 CVE-2022-45359(CVSS v3: 9.8) 的严重漏洞，影响 WordPress 插件YITH WooCommerce Gift Cards Premium。该插件允许在线商店的网站销售礼品卡，这是一个在50000多个网站上使用的WordPress 插件。

据悉，YITH WooCommerce Gift Cards Premium 插件允许在线商店的网站销售礼品卡，而CVE-2022-45359漏洞是一个任意文件上传问题，允许未经身份验证的攻击者将文件上传到易受攻击的站点，包括提供对该站点的完全访问权限的Web shell。该问题于2022年11月22日被发现，并随着版本3.20.0的发布得到解决。但由于许多网站仍在使用易受攻击的插件版本，不法黑客正在探索野外攻击的缺陷，以便在电子商店上传后门程序。[[阅读原文]](https://securityaffairs.co/140004/hacking/wordpress-gift-card-plugin-attacks.html)

## 4、GuLoader恶意软件利用新技术逃避安全软件

[![]()](https://p2.ssl.qhimg.com/t010c37e734ae7506f7.png)

网络安全研究人员揭示了名为GuLoader的高级恶意软件下载器采用多种技术来逃避安全软件。

日前，CrowdStrike 研究人员 Sarang Sonawane 和 Donato Onofri在上周发表的一篇技术文章中说：“新的 shellcode 反分析技术试图通过扫描整个进程内存中任何与虚拟机 (VM) 相关的字符串来阻止研究人员和敌对环境。”

GuLoader又称CloudEyE，是一种 Visual Basic Sc​​ript (VBS) 下载程序，用于在受感染的计算机上分发远程访问木马，最早于2019年被首次发现野外利用。2021年11月，一种名为 RATDispenser 的 JavaScript 恶意软件变种成为通过 Base64 编码的 VBScript 植入器植入 GuLoader 的渠道。[[阅读原文]](https://thehackernews.com/2022/12/guloader-malware-utilizing-new.html)

## 5、朝鲜黑客发送冒名钓鱼邮件攻击韩外交人员

[![]()](https://p5.ssl.qhimg.com/t01e353ab7a9bc53c53.png)

韩国国际广播电台报道：韩国警方调查发现，朝鲜黑客组织冒充记者或国会议员办公室向韩国外交安全领域专家发送植入恶意代码或附有钓鱼网站地址的邮件，从而窃取专家的邮件内容，不过所幸目前并未造成重大损失。

今年5月，一名韩国外交安全专家收到了一封自称是国会议员办公室发送的邮件，信中称将支付研讨会出席费用，并附上了一份支付文件。这份看似平平无奇的文件实际上是恶意代码，运行后电脑里的所有信息都将外泄。国会议员太永浩表示，这种手段的精巧程度令人吃惊。我刚开始也以为是我们助理发送的邮件，还直接去跟助理进行了确认。

邮件发送人并非国会议员办公室，而是朝鲜黑客组织。该组织在邮件中自称为记者，诱导收信人登录伪装成国内门户网站的钓鱼网站，进而窃取用户名和密码。通过这种方式发送的邮件多达800余封，主要攻击对象为外交安全领域的专家。警察厅网络恐怖活动调查队有关人士表示，这类邮件的一大特点是，攻击对象均为统一、安全、外交、国防领域的专家。

目前有49名专家遭黑客攻击，所幸外交安全领域的主要信息并未外泄。[[阅读原文]](https://world.kbs.co.kr/service/news_view.htm?lang=c&Seq_Code=77866)

## 6、苏黎世保险CEO：网络攻击将“无法投保”

![]()

近年来不断上升的网络损失，促使保险业采取紧急措施，限制自己的风险敞口。一些保险公司在推高保费的同时，还调整了保单，让客户承担更多损失。

欧洲最大保险公司之一的首席执行官警告称，随着黑客攻击造成的破坏继续加剧，网络攻击（而非自然灾害）将变得“无法投保”。

近年来，保险业高管越来越多地谈到系统性风险，如流行病和气候变化，这些风险考验着该行业提供保险的能力。与自然灾害相关的索赔预计将连续第二年超过1000亿美元。[[阅读原文]](https://www.ftchinese.com/interactive/93850?exclusive)

## 7、APT-C-36（盲眼鹰）近期攻击活动分析

![]()

APT-C-36（盲眼鹰）是一个疑似来自南美洲的APT组织，主要目标位于哥伦比亚境内，以及南美的一些地区，如厄瓜多尔和巴拿马。该组织自2018年被发现以来，持续发起针对哥伦比亚国家的政府部门、金融、保险等行业以及大型公司的定向攻击。

APT-C-36近期常采用鱼叉攻击，以PDF文件作为入口点，诱导用户点击文档里面的恶意链接下载RAR压缩包文件。大部分压缩包文件需要密码才能解压，密码基本为4位纯数字，解压后是伪装成PDF文件名的VBS脚本。VBS脚本被用户点击执行后将开启一段复杂多阶段的无文件攻击链，最终加载程序为混淆过的AsyncRAT或NjRAT木马，并且加入了绕过AMSI机制的代码，这都表明该组织在不断优化其攻击武器。[[阅读原文]](https://mp.weixin.qq.com/s/mTmJLHYC9bJDnphf_52JmA)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284727](/post/id/284727)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

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

* [1、Kavach 2FA网络钓鱼攻击活动盯上印度政府](#h2-1)
* [2、Linux Kernel爆可远程执行代码“关键”SMB漏洞](#h2-2)
* [3、安全专家警告利用 WordPress 礼品卡插件的攻击](#h2-3)
* [4、GuLoader恶意软件利用新技术逃避安全软件](#h2-4)
* [5、朝鲜黑客发送冒名钓鱼邮件攻击韩外交人员](#h2-5)
* [6、苏黎世保险CEO：网络攻击将“无法投保”](#h2-6)
* [7、APT-C-36（盲眼鹰）近期攻击活动分析](#h2-7)

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