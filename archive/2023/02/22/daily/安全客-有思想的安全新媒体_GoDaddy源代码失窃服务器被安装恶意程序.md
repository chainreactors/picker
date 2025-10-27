---
title: GoDaddy源代码失窃服务器被安装恶意程序
url: https://www.anquanke.com/post/id/286541
source: 安全客-有思想的安全新媒体
date: 2023-02-22
fetch_date: 2025-10-04T07:41:33.602647
---

# GoDaddy源代码失窃服务器被安装恶意程序

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

# GoDaddy源代码失窃服务器被安装恶意程序

阅读量**128951**

发布时间 : 2023-02-21 10:00:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第460期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、GoDaddy源代码失窃服务器被安装恶意程序

[![]()](https://p1.ssl.qhimg.com/t01d0468797b74eb99c.png)

Web 托管巨头 GoDaddy 证实它遭到了持续多年的入侵，源代码失窃服务器也被安装恶意程序。

GoDaddy 是在去年 12 月初收到客户报告其网站被重定向到随机域名后发现未知攻击者入侵了它的 cPanel 共享托管环境。它的调查显示攻击者在它的服务器上活跃了多年，近几年披露的多起安全事故都与此相关。黑客在它的服务器上安装了恶意程序，还窃取到部分服务相关的源代码。它在 2021 年 11 月和 2020 年 3 月披露的安全事件都与此相关。其中 2021 年 11 月的事件影响到了它管理的 120 万 WordPress 客户，攻击者利用一个窃取的密码入侵了它的 WordPress 托管环境，窃取到了客户的邮件地址、管理员密码、sFTP 和数据库凭证，以及部分 SSL 私钥。[[阅读原文]](https://www.bleepingcomputer.com/news/security/godaddy-hackers-stole-source-code-installed-malware-in-multi-year-breach/)

## 2、恶意程序滥用微软IIS功能在Windows上执行恶意代码

[![]()](https://p1.ssl.qhimg.com/t01d148c43cc572f563.png)

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。

微软 IIS（Internet Information Services）是广泛使用的 Web 服务器，它的一项功能叫 Failed Request Event Buffering（FREB），旨在帮助管理员诊断错误，FREB 能从缓存中将部分错误相关的请求写入磁盘。黑客找到了滥用该功能的方法，攻击者首先需要入侵运行 IIS 的 Windows 系统，启用 FREB，通过将恶意代码注入 IIS 进程内存劫持执行，它随后就能拦截所有 HTTP 请求，寻找特殊格式的请求，这种特殊的请求能以隐蔽的方式执行远程代码，系统上没有可疑文件或进程在运行。研究人员将这种恶意程序命名为 Frebniis。

## 3、Mirai 恶意软件新变种感染 Linux 设备

[![]()](https://p5.ssl.qhimg.com/t015bed99cb03572246.png)

一个被追踪为“V3G4”的 Mirai 恶意软件新变种异常活跃，正在利用基于Linux 服务器和物联网设备中的13个漏洞，展开 DDoS（分布式拒绝服务）攻击。

据悉，该恶意软件通过暴力破解弱的或默认的 telnet/SSH 凭据并利用硬编码缺陷在目标设备上执行远程代码执行来传播。一旦设备遭到破坏，恶意软件就会感染该设备并将其招募到僵尸网络群中。

Palo Alto Networks（第 42 单元）的研究人员在三个不同的活动中发现了该特定恶意软件，他们报告称在 2022 年 7 月至 2022 年 12 月期间监测了恶意活动。[[阅读原文]](https://www.bleepingcomputer.com/news/security/new-mirai-malware-variant-infects-linux-devices-to-build-ddos-botnet/)

## 4、ClamAV 开源防病毒软件中发现严重的 RCE 漏洞

[![]()](https://p4.ssl.qhimg.com/t0148fc18d77e0d421e.png)

日前，思科推出了安全更新，以解决 ClamAV 开源防病毒引擎中报告的一个严重缺陷，该缺陷可能导致在易受感染的设备上远程执行代码。

据悉，该漏洞被跟踪为CVE-2023-20032（CVSS 评分：9.8），问题与驻留在 HFS+ 文件解析器组件中的远程代码执行案例有关。

该缺陷影响版本 1.0.0 及更早版本、0.105.1 及更早版本以及 0.103.7 及更早版本。谷歌安全工程师 Simon Scannell 因发现并报告了该漏洞而受到赞誉。“这个漏洞是由于缺少缓冲区大小检查，可能导致堆缓冲区溢出写入，”Cisco Talos在一份公告中说。“攻击者可以通过提交一个精心制作的 HFS+ 分区文件来利用此漏洞，以便在受影响的设备上由 ClamAV 扫描。”成功利用该弱点可能使对手能够以与 ClamAV 扫描进程相同的权限运行任意代码，或使进程崩溃，从而导致拒绝服务 (DoS) 情况。[[阅读原文]](https://thehackernews.com/2023/02/critical-rce-vulnerability-discovered.html)

## 5、斯堪的纳维亚航空公司称网络攻击导致乘客数据泄露

![]()

斯堪的纳维亚航空公司 (SAS) 已发布通知警告乘客，其网站和移动应用程序最近数小时的中断是由同时暴露客户数据的网络攻击造成的。网络攻击导致航空公司的在线系统出现某种形式的故障，导致乘客数据对其他乘客可见。这些数据包括联系方式、之前和即将到来的航班，以及信用卡号的最后四位数字。

该航空公司运营着131架飞机的机队，将乘客送往168个目的地，该公司表示，这种暴露的风险很小，因为泄露的财务信息只是部分信息，不易被利用。此外，它澄清说没有护照详细信息被泄露。[[阅读原文]](https://www.bleepingcomputer.com/news/security/scandinavian-airlines-says-cyberattack-caused-passenger-data-leak/)

## 6、专家警告 RambleOn Android 恶意软件针对韩国记者

[![]()](https://p2.ssl.qhimg.com/t01d85bffde91ec9002.png)

作为社会工程活动的一部分，疑似国家背景黑客组织使用带有恶意软件的 Android 应用程序瞄准韩国一记者。

调查结果来自总部位于韩国的非营利组织 Interlab，该组织创造了新的恶意软件RambleOn。Interlab 威胁研究员 Ovi Liber 在本周发布的一份报告中表示，恶意功能包括“从目标受到攻击时开始读取和泄露目标联系人列表、短信、语音通话内容、位置和其他内容的能力” 。该间谍软件伪装成名为 Fizzle ( ch.seme ) 的安全聊天应用程序，但实际上，它充当传递托管在 pCloud 和 Yandex 上的下一阶段有效载荷的管道。[[阅读原文]](https://thehackernews.com/2023/02/experts-warn-of-rambleon-android.html)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286541](/post/id/286541)

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

* [1、GoDaddy源代码失窃服务器被安装恶意程序](#h2-1)
* [2、恶意程序滥用微软IIS功能在Windows上执行恶意代码](#h2-2)
* [3、Mirai 恶意软件新变种感染 Linux 设备](#h2-3)
* [4、ClamAV 开源防病毒软件中发现严重的 RCE 漏洞](#h2-4)
* [5、斯堪的纳维亚航空公司称网络攻击导致乘客数据泄露](#h2-5)
* [6、专家警告 RambleOn Android 恶意软件针对韩国记者](#h2-6)

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