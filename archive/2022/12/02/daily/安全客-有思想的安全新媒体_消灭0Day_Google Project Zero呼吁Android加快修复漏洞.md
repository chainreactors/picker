---
title: 消灭0Day?Google Project Zero呼吁Android加快修复漏洞
url: https://www.anquanke.com/post/id/283906
source: 安全客-有思想的安全新媒体
date: 2022-12-02
fetch_date: 2025-10-04T00:16:09.456446
---

# 消灭0Day?Google Project Zero呼吁Android加快修复漏洞

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

# 消灭0Day?Google Project Zero呼吁Android加快修复漏洞

阅读量**216070**

发布时间 : 2022-12-01 10:00:08

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第413期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、消灭0Day?Google Project Zero呼吁Android加快修复漏洞

[![]()](https://p4.ssl.qhimg.com/t0107ee425a05cfcf5a.png)

Google Project Zero安全团队想要消灭0day，它采用的一种方法是公开督促企业加快修复漏洞，其中包括Google 自己。

在最新的官方博客中，它批评了Android和Pixel团队。今年6月，Project Zero研究员Maddie Stone报告了一个位于ARM GPU驱动中正被利用的提权漏洞，另一位研究员Jann Horn接下来三周在驱动中发现了多个相关漏洞，这些漏洞允许攻击者获得系统的完整访问权限，绕过Android的权限模型。他们向ARM报告了漏洞，ARM在7月和8月修复了漏洞并公布相关源代码，然而Android至今没有给用户打上补丁。这一次掉链子的是Google和Android OEM。高通使用了自己的GPU，但Google的Tensor SoC使用了ARM GPU，三星和联发科也都使用了ARM GPU，这意味着受影响的设备数量多达数百万部。Google接受采访时表示它正在测试补丁，将会在未来几周释出。[[阅读原文]](https://www.solidot.org/story?sid=73511)

## 2、宏碁电脑存在驱动程序漏洞，启动过程中可部署恶意软件

[![]()](https://p4.ssl.qhimg.com/t01d988f06ceee60edb.png)

近日，Acer发布安全公告，修复了某些Acer笔记本电脑型号中的一个安全绕过漏洞（CVE-2022-4020），该漏洞的CVSSv3评分为8.1。

该漏洞存在于某些Acer笔记本设备上的HQSwSmiDxe DXE 驱动程序中，可能导致高权限恶意用户通过修改BootOrderSecureBootDisable NVRAM变量来修改/禁用UEFI安全启动设置，实现劫持操作系统加载过程并加载未签名的引导加载程序以绕过或禁用保护，并使用系统权限部署恶意Payload等。

目前该漏洞已经修复，受影响用户可将BIOS 更新到最新版本以修复此漏洞。[[阅读原文]](https://www.landiannews.com/archives/96186.html)

## 3、安全团队发现Crysis勒索软件变种Wiki在韩国活动

[![]()](https://p0.ssl.qhimg.com/t014d3a94e4001f71ec.png)

AhnLab于11月25日披露了勒索软件Wiki在韩国的活动。

该勒索软件已被确定为Crysis的变种，伪装成正常程序。在执行实际加密之前，Wiki将自己复制到%AppData%或%windir% system32路径，并添加到注册表中注册为启动程序之一。此外，它还会解码要在内存中终止的与数据库相关的服务和进程名称，并查找当前正在运行的服务和进程并终止它们。由于Crysis类型的勒索软件通常通过RDP分发，研究人员建议注意RDP连接环境。[[阅读原文]](http://www.anquan419.com/knews/24/3751.html)

## 4、北约举行年度“网络联盟”演习

[![]()](https://p2.ssl.qhimg.com/t01c6798a8daf42f076.png)

北约28日起举行一年一度的”网络联盟”演习(Cyber Coalition)，芬兰、瑞典、日本等国以”北约伙伴国”身份派人参加。

据北约当日发布的公告，此次”网络联盟”演习为期5天，至12月2日结束；北约26个成员国、6个伙伴国(芬兰、瑞典、爱尔兰、瑞士、日本、格鲁吉亚)以及欧盟共派出约1000人参加，另有业界和学术界人士。

公告称演习在爱沙尼亚首都塔林举行，参演国家首都和其它地点会有人远程连线；演习期间主要演练如何应对现实网络挑战，如针对电网、项目、北约及成员国资产的网络攻击等，意在提高北约网络防御和网络空间”共同作战”能力。

作为北约机制性网络演习，”网络联盟”演习自2008年开始举行，具有测试性、实战性等特点，与具有培训性、对抗性等特点的”锁盾”演习(Locked Shields)互为补充，并称北约两大网络演习。

目前网络空间与陆海空和太空一道，已成北约作战领域，网络攻击亦可触发北约”集体防御”，为此北约专门成立网络空间行动中心，部署全天候待命的”网络防御快速反应团队”。

北约28日的公告称，网络防御现为北约”集体防御”核心任务之一；在今年6月召开的北约马德里峰会上，北约成员国承诺进一步增强网络防御能力，深化与业界及欧盟等主要利益相关方的合作。[[阅读原文 ]](https://www.163.com/dy/article/HNB88BFM051497H3.html)

## 5、安全专家披露亚马逊网络服务AWS AppSync漏洞

![]()

日前，Amazon Web Services (AWS) 修复了一个跨租户漏洞，该漏洞可能允许攻击者获得对资源的未授权访问。

亚马逊网络服务 (AWS) 解决了其平台中的跨租户混淆代理问题，该问题可能允许威胁行为者获得对资源的未授权访问。Datadog 的研究人员于 2022年9月1日向公司报告了该问题，并于9月6日修复了该漏洞。

当无权执行某项操作的实体可以强制具有更高权限的实体执行该操作时，就会出现混淆代理问题。如果所有者向第三方（称为 跨账户）或其他 AWS 服务（称为 跨服务）提供对您账户中资源的访问权限，AWS 会提供工具来保护账户。

亚马逊调查了在野外攻击中对该问题的潜在利用，并确定没有客户受到影响。[[阅读原文]](https://securityaffairs.co/wordpress/139045/hacking/amazon-web-services-flaw.html)

## 6、Group-IB研究显示：世界杯球迷正在遭遇网络诈骗浪潮

![]()

网络安全公司Group-IB收集的数据显示，随着卡塔尔世界杯进入第二周，国际足联世界杯的诈骗活动正在激增。

研究人员已经确认了多达90个可能被入侵的Hayya账户。Hayya是世界杯观众进入卡塔尔、购买门票和交通等其他服务的强制系统。他们还在谷歌Play Store中发现了大约40个虚假应用程序，承诺可以获得门票，以及至少5个自称是求职申请表的网站，用于获取个人信息。该公司与国际刑警组织分享了调查结果，并与卡塔尔计算机应急响应小组达成合作。[[阅读原文]](http://www.anquan419.com/knews/24/3759.html)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283906](/post/id/283906)

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

* [1、消灭0Day?Google Project Zero呼吁Android加快修复漏洞](#h2-1)
* [2、宏碁电脑存在驱动程序漏洞，启动过程中可部署恶意软件](#h2-2)
* [3、安全团队发现Crysis勒索软件变种Wiki在韩国活动](#h2-3)
* [4、北约举行年度“网络联盟”演习](#h2-4)
* [5、安全专家披露亚马逊网络服务AWS AppSync漏洞](#h2-5)
* [6、Group-IB研究显示：世界杯球迷正在遭遇网络诈骗浪潮](#h2-6)

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