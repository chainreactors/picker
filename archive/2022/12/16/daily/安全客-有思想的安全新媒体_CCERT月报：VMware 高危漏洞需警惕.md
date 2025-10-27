---
title: CCERT月报：VMware 高危漏洞需警惕
url: https://www.anquanke.com/post/id/284329
source: 安全客-有思想的安全新媒体
date: 2022-12-16
fetch_date: 2025-10-04T01:37:35.886633
---

# CCERT月报：VMware 高危漏洞需警惕

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

# CCERT月报：VMware 高危漏洞需警惕

阅读量**175069**

发布时间 : 2022-12-15 10:12:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 edu，文章来源：edu.cn

原文地址：<https://www.edu.cn/xxh/cernet/ccert/202212/t20221214_2261216.shtml>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期网络安全形势较为平稳，无重大的安全事件发生。安全投诉事件与往期基本相同。

　　在病毒与木马方面，一个VMware的高危漏洞（CVE-2022-22954）正在被利用，来进行挖矿木马和勒索病毒传播，虽然今年4月VMware官方已经在新版本中修补了此漏洞，但由于很多虚拟平台的管理员出于各种原因没有及时进行版本更新，导致漏洞仍然存在并被利用。攻击者利用该漏洞可以控制虚拟主机进行挖矿或是加密数据进行勒索。

**近期新增严重漏洞评述**

　　01

　　微软2022年11月的例行安全更新共涉及漏洞数68个，其中严重等级的12个、重要等级的55个、中危等级的1个。受影响的产品包括：Microsoft Windows和Windows组件、Microsoft Windows Netlogon、Microsoft Dynamics、Microsoft Excel、Microsoft Windows Print Spooler Components、Microsoft Windows Human Interface Devices等。这些漏洞中有6个属于0day漏洞，分别是Windows Scripting Languages远程代码执行漏洞（CVE-2022-41128）、Windows Mark of the Web安全功能绕过漏洞（CVE-2022-41091）、Windows Print Spooler特权提升漏洞（CVE-2022-41073）、Windows CNG Key Isolation Service特权提升漏洞（CVE-2022-41125）、Microsoft Exchange Server特权提升漏洞（CVE-2022-41040）、Microsoft Exchange Server远程代码执行漏洞（CVE-2022-41082），上述6个漏洞均已发现在野的攻击利用行为，9月底曝出的被大量利用的两个Exchange Server 0day漏洞在11月的例行更新中得到了修补。鉴于上述漏洞的危害性，建议用户尽快使用系统自带的更新功能进行补丁更新。

　　02

　　谷歌发布了Chrome浏览器最新版本（Windows版本107.0.5304.87/.88、Mac及Linux版本107.0.5304.87），用于修补之前版本中存在的一个V8 JavaScript引擎的类型混淆漏洞，利用该漏洞，攻击者可以在用户的系统上以当前用户的权限执行任意代码。目前该漏洞已经存在在野的攻击，建议用户尽快使用系统自带的更新功能进行更新。

　　03

　　VMware官方发布了安全公告，用于修补VMware Cloud Foundation产品中的一个严重漏洞（CVE-2021-39144）。由于漏洞已被大量利用并危害巨大，VMware官方破例对之前停止支持的版本也进行了补丁开发。建议使用VMware Cloud Foundation产品的管理员尽快进行更新，尤其是那些使用低版本的用户。

　　04

　　苹果公司最近在iOS的版本更新中修补了一个高危的越界写入漏洞（CVE-2022-42827），该漏洞是由软件在当前内存缓冲区边界之外写入数据引起的，可能导致数据损坏、应用程序崩溃或代码执行。这是苹果今年以来修补的第9个0day漏洞。用户可以通过系统更新来修补该漏洞。

　　05

　　OpenSSL的3.0.0-3.0.6版本中的两个高危安全漏洞，分别是X.509电子邮件地址4字节缓冲区溢出漏洞（CVE-2022-CCERT月报3602）和X.509电子邮件地址可变长度缓冲区溢出漏洞（CVE-2022-3786）。攻击者可以使用包含恶意字符邮件地址的证书引诱用户访问，当用户的系统在验证该证书时可能导致拒绝服务攻击或任意代码执行。目前OpenSSL官方已发布新版本修复上述漏洞，建议受影响的用户升级至OpenSSL3.0.7及以上安全版本。

**安全提示**

　　近期国家有关部门发布了一批网络安全相关的管理办法、规定、标准和通知，需要引起重视，包括：

　　1. 工业和信息化部发布《网络产品安全漏洞收集平台备案管理办法》对网络安全漏洞收集平台的注册、备案、信息变更、注销等程序提出了系统要求，该办法将于2023年1月1日起施行。

　　2. 国家市场监管总局标准技术司、中央网信办网络安全协调局、公安部网络安全保卫局联合发布了《信息安全技术关键信息基础设施安全保护要求》（GB/T39204-2022）国家标准。该标准是关键信息基础设施安全保护标准体系的构建基础，将于2023年5月1日正式实施。

　　3. 中央网信办印发《关于切实加强网络暴力治理的通知》，要求各地网信部门提高政治站位，指导和督促网站平台开展网暴问题治理工作，增强网暴问题治理能力和水平，完善网暴问题治理的长效机制。

　　4. 国家互联网信息办公室发布新修订的《互联网跟帖评论服务管理规定》，用于加强对互联网跟帖评论服务的规范管理，维护国家安全和公共利益，保护公民、法人和其他组织的合法权益，促进互联网跟帖评论服务健康发展。该规定自2022年12月15起实施。

　　作者：郑先伟（中国教育和科研计算机网应急响应组）
责编：项阳

本文翻译自edu.cn [原文链接](https://www.edu.cn/xxh/cernet/ccert/202212/t20221214_2261216.shtml)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284329](/post/id/284329)

安全KER - 有思想的安全新媒体

本文转载自: [edu.cn](https://www.edu.cn/xxh/cernet/ccert/202212/t20221214_2261216.shtml)

如若转载,请注明出处： <https://www.edu.cn/xxh/cernet/ccert/202212/t20221214_2261216.shtml>

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