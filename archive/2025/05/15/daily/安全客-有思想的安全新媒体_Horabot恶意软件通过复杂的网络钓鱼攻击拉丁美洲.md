---
title: Horabot恶意软件通过复杂的网络钓鱼攻击拉丁美洲
url: https://www.anquanke.com/post/id/307373
source: 安全客-有思想的安全新媒体
date: 2025-05-15
fetch_date: 2025-10-06T22:23:21.562099
---

# Horabot恶意软件通过复杂的网络钓鱼攻击拉丁美洲

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

# Horabot恶意软件通过复杂的网络钓鱼攻击拉丁美洲

阅读量**62843**

发布时间 : 2025-05-14 15:32:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/horabot-malware-targets-latin-america-with-sophisticated-phishing/>

译文仅供参考，具体内容表达以及含义原文为准。

![冀]()

在最近的一项调查中，FortiGuard Labs 揭露了一个复杂的网络钓鱼活动，该活动传播了 Horabot 恶意软件系列，这是一种针对拉丁美洲讲西班牙语的用户的欺骗性强大威胁。Horabot 利用熟悉的业务通信（西班牙语的假发票电子邮件）将社会工程与分层脚本技术相结合，以实现持久性、凭据盗窃和自动横向传播。

根据 Fortinet 的说法，Horabot“*主要针对讲西班牙语的用户*”，通过发送网络钓鱼电子邮件，“*冒充发票或财务文件，诱骗受害者打开恶意附件*”。这些电子邮件通常被精心设计成来自墨西哥企业的合法信件，其中包含带有恶意 HTML 文件的 ZIP 附件。在内部，HTML 文件包含 Base64 编码的数据，这些数据通过远程服务器启动多阶段感染链。

感染链结合了 VBScript、AutoIt 和 PowerShell，以逃避检测并传递有效负载。VBScript 阶段执行反分析检查，例如如果存在 Avast 防病毒软件或系统似乎在虚拟机中运行，则终止该检查。然后，它执行侦察，收集系统和网络详细信息，并通过 POST 请求将它们发送到攻击者控制的基础设施。

![Horabot，网络钓鱼恶意软件]()

攻击链 |图片来源： Fortinet

AutoIt 脚本在解密和执行有效负载方面起着核心作用。该恶意软件会下载 AutoIt3.exe 和 Aut2Exe.exe 等合法的 AutoIt 工具，以及混淆的有效负载。它使用硬编码密钥 （99521487），解密恶意 DLL 并通过 AutoIt 执行它，确保“*这些关键文件的属性是隐藏的、系统的和只读*的”。

一旦激活，Horabot 的解密 DLL 就会从基于 Chromium 的浏览器（如 Chrome、Edge、Brave 和 Opera）中窃取有价值的信息，包括作系统详细信息、防病毒存在和敏感浏览器数据。该恶意软件还能够注入虚假的弹出窗口，旨在网络钓鱼以获取登录凭据，通过将这些覆盖层嵌入 DLL 的 RCData 部分，这种作变得更加隐蔽。

Horabot 特别危险的是它能够通过受害者的 Outlook 电子邮件客户端传播自身。Fortinet 解释说，Horabot“*利用 Outlook COM 自动化从受害者的邮箱发送网络钓鱼邮件”，*使其能够在公司和个人网络中传播。

此电子邮件自动化系统过滤掉 Gmail、Hotmail 和 .edu 等域，以避开消费者帐户和学术机构，而是专注于收集企业联系人。它使用预先编写的西班牙语消息和相同的恶意发票附件构建网络钓鱼电子邮件，从而维持合法业务通信的假象。

在发送其有效载荷和网络钓鱼电子邮件后，Horabot 会删除其存在的所有痕迹。脚本 “a6” 可清理伪像、删除有效负载，并确保留下最少的取证证据 — 这是专业恶意软件作的标志。

组织必须增强其电子邮件过滤系统，密切监控脚本执行行为，并培训员工对意外附件持怀疑态度 – 即使它们似乎来自受信任的来源。

本文翻译自securityonline [原文链接](https://securityonline.info/horabot-malware-targets-latin-america-with-sophisticated-phishing/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307373](/post/id/307373)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/horabot-malware-targets-latin-america-with-sophisticated-phishing/)

如若转载,请注明出处： <https://securityonline.info/horabot-malware-targets-latin-america-with-sophisticated-phishing/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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