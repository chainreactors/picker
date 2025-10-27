---
title: 虚假的DSA电子邮件诱骗用户安装ScreenConnect RAT
url: https://www.anquanke.com/post/id/307155
source: 安全客-有思想的安全新媒体
date: 2025-05-08
fetch_date: 2025-10-06T22:24:30.206927
---

# 虚假的DSA电子邮件诱骗用户安装ScreenConnect RAT

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

# 虚假的DSA电子邮件诱骗用户安装ScreenConnect RAT

阅读量**84390**

发布时间 : 2025-05-07 17:00:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/fake-ssa-emails-trick-users-installing-screenconnect-rat/>

译文仅供参考，具体内容表达以及含义原文为准。

网络犯罪分子正在使用虚假的社会保障管理局电子邮件来分发ScreenConnect RAT(远程访问木马)并破坏用户计算机。

网络安全专家已经发现了正在进行的计划,犯罪分子正在利用美国社会保障管理局(SSA)欺骗人们在计算机上安装一个名为ScreenConnect的危险远程访问木马(RAT)。一旦安装,这个程序给攻击者完全的远程控制,允许他们窃取个人信息,并安装更多有害软件。

[noticed](https://www.malwarebytes.com/blog/news/2025/04/fake-social-security-statement-emails-trick-users-into-installing-remote-tool)Malwarebytes的研究人员首先注意到这些虚假的电子邮件,这些电子邮件通知人们他们的“社会保障声明现在可用”,并敦促他们下载附件或点击链接查看它。这些电子邮件被设计成看起来非常真实,使人们很难说它们是假的。

[![假SSA电子邮件欺骗用户安装ScreenConnect RAT]()](https://hackread.com/wp-content/uploads/2025/05/fake-ssa-emails-trick-users-into-installing-dangerous-screenconnect-rat.jpg)

这些电子邮件中的链接或附件导致下载安装 ScreenConnect 客户端的文件。为了让人们认为它是安全的,这些文件有时会给出误导性的名字,例如“`ReceiptApirl2025Pdfc.exe`“或”`SSAstatment11April.exe`”

[ScreenConnect](https://hackread.com/black-basta-gang-ms-teams-email-bombing-malware/)ScreenConnect本身是公司用于IT支持的真正工具,让技术人员远程帮助用户。然而,在罪犯手中,它变得非常危险。一旦他们通过ScreenConnect控制计算机,他们可以查看文件,运行程序,并窃取敏感数据,如银行详细信息和个人识别号码。这背后的罪犯,[有时被称为莫拉托里集团](https://threatfox.abuse.ch/browse/tag/Molatori/),主要想要进行金融欺诈。

[reported](https://cofense.com/blog/hackers-spoof-social-security-administration-to-deliver-screenconnect-remote-access-tool)Cofense的安全专家还报告了类似的网络钓鱼活动,模仿SSA。这些电子邮件经常声称提供更新的福利声明,使用不匹配的链接或在按钮后面隐藏恶意链接。

“虽然电子邮件的确切结构从样本到样本都发生了变化,但该活动始终向ConnectWise RAT安装程序提供嵌入式链接,”Cofense研究人员在他们的闪光警报中指出。

他们的研究结果表明,这些虚假电子邮件旨在安装ConnectWise RAT,这是合法软件ConnectWise Control(以前是ScreenConnect)的受污染版本。这场竞选活动导致2024年美国总统大选的活动增加,在2024年11月中旬左右达到顶峰。

是什么让这些攻击难以发现是罪犯如何运作。[他们经常从被泄露的网站发送这些网络钓鱼 ema](https://hackread.com/native-language-phishing-resolverrat-healthcare/) ils,使电子邮件地址看起来合法。他们还经常将电子邮件内容作为图像嵌入,从而阻止电子邮件过滤器能够读取和阻止有害消息。此外,由于ScreenConnect是一个广泛使用的程序,常规防病毒软件可能不会自动将其标记为威胁。

这不是犯罪分子第一次滥用合法的远程访问工具。正如Hackread.[com之前报道的那样](https://hackread.com/scammers-fake-linkedin-inmail-deliver-connectwise-trojan/),类似的策略也被用于虚假的LinkedIn电子邮件来传播ConnectWise RAT。

这些假消息模仿了真实的InMail通知,使用旧的设计看起来令人信服。网络犯罪分子还使用复杂的网络钓鱼电子邮件,模仿知名品牌窃取信息。

例如[,](https://hackread.com/phishing-emails-impersonate-qantas-credit-card-info/)最近的一项活动针对澳大利亚航空公司澳航(Qantas),虚假电子邮件旨在看起来像该航空公司的真实营销信息。这些由Cofense Intelligence发现的电子邮件欺骗用户泄露了他们的信用卡详细信息和个人信息。

本文翻译自hackread [原文链接](https://hackread.com/fake-ssa-emails-trick-users-installing-screenconnect-rat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307155](/post/id/307155)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-ssa-emails-trick-users-installing-screenconnect-rat/)

如若转载,请注明出处： <https://hackread.com/fake-ssa-emails-trick-users-installing-screenconnect-rat/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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