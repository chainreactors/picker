---
title: APT29利用Windows功能入侵欧洲外交实体网络
url: https://www.anquanke.com/post/id/283066
source: 安全客-有思想的安全新媒体
date: 2022-11-12
fetch_date: 2025-10-03T22:28:35.079477
---

# APT29利用Windows功能入侵欧洲外交实体网络

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

# APT29利用Windows功能入侵欧洲外交实体网络

阅读量**344202**

发布时间 : 2022-11-11 10:00:09

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第399期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、希腊将立法禁止销售网络间谍软件

[![]()](https://p2.ssl.qhimg.com/t017e79a4eff6753830.jpg)

希腊政府表示将立法禁止销售间谍软件。

在这之前，总理 Kyriakos Mitsotakis 的政府被指使用 Cytrox 公司开发的间谍软件 Predator 对数十名知名政治家、记者和商人进行监控。Mitsotakis 周一称这一指控是“最不可信的谎言”，他表示希腊将成为首个制定立法，明确禁止在国内销售此类软件的国家。社会主义反对派领导人 Nikos Androulakis 在今年七月向最高检察官提起诉讼，指控有人尝试用间谍软件入侵其手机。Mitsotakis 否认对黑客攻击知情，表示永远不会批准此类行动。[[阅读原文]](https://www.solidot.org/story?sid=73312)

## 2、微软发布11月安全更新，修复6个0day漏洞

[![]()](https://p5.ssl.qhimg.com/t0164ed031f90b4d01e.jpg)

周二，微软发布了 11 月的例行安全更新，修复了 6 个正被利用的 0day。其中两个 CVE-2022-41040 和 CVE-2022-41082 位于 Exchange 服务器中，属于高危漏洞，黑客组合利用这两个漏洞能在服务器上执行恶意代码。

漏洞被统称为 ProxyNotShell，Shodan 搜索显示在漏洞公开之际有大约 22 万个服务器存在该漏洞，微软上个月称使用简体中文的黑客正在利用该漏洞。第三个 0day 是 Windows 高危漏洞 CVE-2022-41128，能被攻击者远程执行恶意代码，它是 Google 的 Threat Analysis Group 安全研究人员发现的。另外两个 0day 属于提权漏洞，其中 CVE-2022-41073 位于微软的打印后台服务中，CVE-2022-41125 位于 Windows CNG Key Isolation Service 中。最后一个 0day CVE-2022-41091 允许黑客创建恶意文件躲避 Mark of the Web。微软本月的安全更新共修复了 68 个漏洞，11 个为高危漏洞。[[阅读原文]](https://www.solidot.org/story?sid=73307)

## 3、微软：基于密码的黑客攻击年增长74%

[![]()](https://p5.ssl.qhimg.com/t01c26dd9b169285e53.jpg)

根据一份新的报告，每秒钟有近1000次基于密码的攻击，与去年相比增加了74%。这些数据来自微软的《2022年数字防御报告》，该报告分析了来自微软全球产品和服务生态系统的数万亿信号，以揭示全球网络威胁的规模。

黑客事件的数量从今年年初至今大幅增加，这主要是由于俄罗斯在2月份入侵乌克兰，以及由此引发的国家间的网络战争。但黑客仍然喜欢基于密码的攻击；微软估计，每分钟有921起这样的攻击发生。

暴力穷举仍然是未经授权访问密码系统的一种常见方法。NVIDIA的RTX 4090显卡的强大计算能力使得这类攻击更加有效（在特定情况下）。研究人员最近展示了Lovelace旗舰显卡产品如何在短短48分钟内循环完成一个八字密码的所有2000亿次尝试。

由于许多人在多个网站和服务中循环使用账户凭证，大规模数据泄露后在线泄露的密码是黑客的主要收获地。2012年发生的大规模LinkedIn漏洞被认为使黑客能够在2016年进入马克·扎克伯格的Twitter和Pinterest账户。

目标窃取密码的钓鱼式攻击仍然很猖獗。最近，犯罪分子一直试图利用Twitter的验证改革，通过钓鱼方式获取已验证账户的密码，甚至Steam用户也成为了目标。这种增长的部分原因是微软在Windows11 22H2更新中加入了增强的网络钓鱼保护。

微软写道，90%的黑客账户没有受到”强认证”的保护，”强认证”是指正在使用的单层保护，不包括多因素认证（MFA）。微软警告说，使用MFA的账户数量很低，甚至在管理员账户中也是如此，尽管这些额外的保护层并不能保证账户100%安全。

除了在有MFA的地方使用MFA之外，如果你想让黑客难以下手，通常的建议也适用：避免重复使用密码（考虑一个好的密码管理器），保持你的软件有最新的补丁，并避免那些仍然莫名其妙地流行的可怕的弱密码。[[阅读原文]](https://baijiahao.baidu.com/s?id=1749038473764048493&wfr=spider&for=pc)

## 4、欧盟政府被指存在间谍软件滥用问题

[![]()](https://p5.ssl.qhimg.com/t011a27def89e393232.jpg)

欧洲议会某委员会的一份新报告草案指出，欧盟各国政府出于政治目的，对公民使用间谍软件并掩盖腐败和犯罪活动。

报告指出，Pegasus项目中存在工具滥用的问题，并指责欧洲理事会在欧盟内部滥用间谍软件的情况下实施一种名为“omertà”的静默代码，并呼吁欧盟委员会“对欧盟间谍软件的滥用和交易进行全面和深入的调查”，同时强调“对所有针对欧盟委员会官员使用间谍软件的指控和怀疑进行全面调查。 ”[[阅读原文]](https://therecord.media/eu-governments-accused-of-using-spyware-to-cover-up-corruption-and-criminal-activity/)

## 5、APT29利用Windows功能入侵欧洲外交实体网络

[![]()](https://p5.ssl.qhimg.com/t018a346f4bed6d51bd.jpg)

近日，有安全研究人员称，发现俄罗斯背景APT组织 APT29 利用“鲜为人知”的 Windows 功能，对未具名欧洲外交实体进行网络攻击活动。安全研究人员称，以外交实体为目标与APT29组织长期行动目标一致。

据悉，APT29 是一个拥有俄罗斯背景的黑客组织，也称为 Cozy Bear、Iron Hemlock 和 The Dukes，主要以政府实体为攻击目标。[[阅读原文]](https://thehackernews.com/2022/11/apt29-exploited-windows-feature-to.html)

## 6、Amadey恶意软件被用于部署LockBit 3.0勒索软件

[![]()](https://p2.ssl.qhimg.com/t01f5c99030505720e2.jpg)

Amadey恶意软件被用于在受感染的系统上部署 LockBit 3.0 勒索软件。

近日，有研究人员警告称，Amadey 恶意软件正被用于在受感染的系统上部署LockBit 3.0勒索软件。Amadey 是一种数据窃取恶意软件，于 2018 年首次被发现，它还允许操作员安装额外的有效负载。该恶意软件可在非法论坛上出售，曾被 TA505 等网络犯罪团伙用来安装 GandCrab 勒索软件或 FlawedAmmyy  RAT。

安全研究人员分析称，目前，Amadey 恶意软件正在由SmokeLoader分发，该恶意软件隐藏在多个站点上可用的软件破解和串行生成程序中。[[阅读原文]](https://securityaffairs.co/wordpress/138292/malware/amadey-malware-deploying-lockbit-3-0.html)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283066](/post/id/283066)

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

![](https://p1.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* [1、希腊将立法禁止销售网络间谍软件](#h2-1)
* [2、微软发布11月安全更新，修复6个0day漏洞](#h2-2)
* [3、微软：基于密码的黑客攻击年增长74%](#h2-3)
* [4、欧盟政府被指存在间谍软件滥用问题](#h2-4)
* [5、APT29利用Windows功能入侵欧洲外交实体网络](#h2-5)
* [6、Amadey恶意软件被用于部署LockBit 3.0勒索软件](#h2-6)

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