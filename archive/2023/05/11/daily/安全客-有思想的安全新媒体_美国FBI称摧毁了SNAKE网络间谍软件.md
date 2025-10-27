---
title: 美国FBI称摧毁了SNAKE网络间谍软件
url: https://www.anquanke.com/post/id/288667
source: 安全客-有思想的安全新媒体
date: 2023-05-11
fetch_date: 2025-10-04T11:36:47.378429
---

# 美国FBI称摧毁了SNAKE网络间谍软件

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

# 美国FBI称摧毁了SNAKE网络间谍软件

阅读量**186737**

发布时间 : 2023-05-10 12:05:37

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

5月9日，FBI发布报告，称其成功入侵并摧毁了网络间谍软件SNAKE。在报告中，FBI指出Snake恶意软件的开发始于2003年底，名为“Uroburos”，而第一个版本的植入程序似乎在2004年初完成。该恶意软件与俄罗斯Turla黑客组织相关联 。

根据9日公开的法庭文件，美国近20年来一直密切关注Snake和与Snake相关的恶意软件工具。

报告中指出，作为“最复杂的长期网络间谍恶意软件植入物”，Snake允许其操作员在受感染的设备上远程安装恶意软件，窃取敏感文档和信息（例如身份验证凭证），保持持久性，并在使用时隐藏他们的恶意活动“隐蔽的点对点网络。

Snake的一个关键方面是它的点对点性质，这使得攻击者可以通过位于受信任位置的受损计算机来路由其间谍和渗透活动，从而使活动更难被发现。

据联合咨询报告，FBI之所以能够解密SNAKE的通信，实际上是利用了SNAKE开发者的错误。在某些看似仓促部署Snake的情况下，操作员忽略了剥离 Snake二进制文件，导致大量函数名称、明文字符串和开发人员评论被泄露。攻击者使用OpenSSL库来处理其Diffie-Hellman密钥交换。

Snake在密钥交换期间创建的Diffie-Hellman密钥集太短而不安全，提供的函数DH\_generate\_parameters的质数长度仅为128位，这对于非对称密钥系统来说是不够的。

几年来，FBI研究了区分、解密和解释Snake网络流量的方法，并开发了一个名为 PERSEUS的工具。它可与特定计算机上的Snake恶意软件植入物建立通信会话，并发出命令使Snake植入物自行禁用而不影响主机或计算机上的合法应用程序。

当前，FBI已经关闭了美国境内所有受感染的设备，而在美国境外，该机构“正在与地方当局合作，以提供有关当局所在国家/地区内 Snake 感染的通知和补救指导。

报告指出，在 50 多个国家/地区检测到的 Snake 恶意软件基础设施被黑客用来从政府网络、研究组织和记者在内的广泛目标收集和窃取敏感数据。

 值得注意的是，FBI的这项行动依赖于一项名为Rule 41的法律条款，该条款允许法官授权美国调查人员访问多个司法管辖区的计算机并采取特定行动。

该规定已用于其他主动的联邦网络行动，包括2022年4月FBI拆除僵尸网络Cyclops Blink。正如美国司法部副部长丽莎·莫纳科(Lisa Monaco)最近所述，所有这三项行动以及其他网络犯罪执法行动都是美国政府持续推动开展更积极主动的网络行动的一部分。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288667](/post/id/288667)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168535)

[安全客](/member.html?memberId=168535)

这个人太懒了，签名都懒得写一个

* 文章
* **122**

* 粉丝
* **0**

### TA的文章

* ##### [注册机内藏勒索软件！收款竟用支付宝？](/post/id/292743)

  2024-01-19 11:10:00
* ##### [全球首发！《2023年度统信UOS安全威胁防御报告》来了](/post/id/292263)

  2023-12-29 11:27:27
* ##### [数字安全“奥斯卡”落幕，ISC 2023创新百强重磅出炉](/post/id/292240)

  2023-12-29 10:24:44
* ##### [一个安全运营工程师的自白](/post/id/291372)

  2023-11-15 10:40:17
* ##### [打造实战型安全人才新高地，360发布ISC安全课SaaS化教培平台](/post/id/291209)

  2023-11-03 17:22:35

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