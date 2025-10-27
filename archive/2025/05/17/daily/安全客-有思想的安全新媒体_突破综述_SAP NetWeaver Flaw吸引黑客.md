---
title: 突破综述:SAP NetWeaver Flaw吸引黑客
url: https://www.anquanke.com/post/id/307468
source: 安全客-有思想的安全新媒体
date: 2025-05-17
fetch_date: 2025-10-06T22:26:21.425377
---

# 突破综述:SAP NetWeaver Flaw吸引黑客

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

# 突破综述:SAP NetWeaver Flaw吸引黑客

阅读量**84117**

发布时间 : 2025-05-16 15:57:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 安维克沙，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/breach-roundup-sap-netweaver-flaw-draws-hackers-a-28410>

译文仅供参考，具体内容表达以及含义原文为准。

![突破综述:SAP NetWeaver Flaw吸引黑客]()

*每周,信息安全媒体集团都会收集世界各地的网络安全事件和违规行为。本周,SAP NetWeaver漏洞吸引了黑客,在Ivanti Endpoint Mobile Manager中锁定了零日,DOGE员工在信息窃贼转储中发现的凭据以及Nucor停止运营。朝鲜黑客以虚假会议邀请为目标,俄罗斯黑客针对网络邮件服务器,微软发布了72个补丁。*[另请参阅:2025年十大技术预测](https://www.govinfosecurity.com/top-10-technical-predictions-for-2025-a-27521?rf=RAM_SeeAlso)

### SAP NetWeaver Flaw 吸引黑客

勒索软件团伙RansomEXX和BianLian加入了对SAP NetWeaver服务器的持续攻击,针对跟踪CVE-2025-31324的关键漏洞[CVE-2025-31324](https://nvd.nist.gov/vuln/detail/CVE-2025-31324),该漏洞可实现未经身份验证的远程代码执行。SAP于4月24日发布了紧急补丁,此前网络安全公司ReliaQuest标记了对该漏洞的疯狂利用。

该漏洞使攻击者能够在没有凭据的情况下上传恶意文件,可能导致完整的系统泄露。ReliaQuest表示,[RansomEXX演员在一次事件中使用了他们的PipeMagic后门和Windows CLFS漏洞。](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29824)

中国民族国家集团也在利用这个漏洞。[Forescout将攻击与Chaya\_004组联系起来](https://www.forescout.com/blog/threat-analysis-sap-vulnerability-exploited-in-the-wild-by-chinese-threat-actor/),识别出581个后门NetWeaver系统,并计划针对1800多个。

美国[added](https://www.cisa.gov/news-events/alerts/2025/04/29/cisa-adds-one-known-exploited-vulnerability-catalog)网络安全和基础设施安全局将CVE-2025-31324添加到其已知的受剥削脆弱性目录中,要求美国联邦机构在5月20日之前进行修补。

### 黑客 链 Ivanti 端点 经理 移动 缺陷

[warned](https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM?language=en_US)陷入困境的边缘设备制造商Ivanti周一警告客户,黑客正在使用其Endpoint Manager Mobile平台中的两个零日漏洞来获得未经身份验证的访问权限,然后执行远程代码。

这家犹他州公司表示,在意识到“披露时解决方案被利用的客户数量非常有限”后,它发布了更新。[CVE-2025-4427](https://nvd.nist.gov/vuln/detail/CVE-2025-4427)[CVE-2025-4428](https://nvd.nist.gov/vuln/detail/CVE-2025-4428)这些缺陷被追踪为CVE-2025-4427和CVE-2025-4428。

Ivanti已经进行了两年的旅程,发现其产品的可破解程度([*见:Ivanti使用报废操作系统,软件包*](https://www.govinfosecurity.com/ivanti-uses-end-life-operating-systems-software-packages-a-24368))。

在这种情况下,Ivanti说这个漏洞最终不是源于它,而是来自未命名的第三方开源库。该公司正在“与维护者接触”,它说。

在一篇博客文章中,[网络安全公司Watchtowr预测](https://labs.watchtowr.com/expression-payloads-meet-mayhem-cve-2025-4427-and-cve-2025-4428/),Ivanti对“非常有限数量”的受影响客户的描述可能不会保持这种状态。“我们确切知道的是 – 一旦’高度针对性’的行动得到公开,我们已经看到攻击者只是在互联网上大规模 pwn 获得任何剩余价值,”它写道。

[一位Tenable研究人员写道](https://www.tenable.com/blog/cve-2025-4427-cve-2025-4428-ivanti-endpoint-manager-mobile-epmm-remote-code-execution),CVE-2025-4427允许远程攻击者访问EPMM应用程序编程接口,这通常只对身份验证用户访问。CVE-2025-4428是一个远程代码执行缺陷。“成功利用这些漏洞的攻击者可以将它们链接在一起,在没有身份验证的情况下在易受攻击的设备上执行任意代码。

### DOGE 员工证书在 Infostealer 转储中发现

活动编码员Micah spottedLee上周四发现了数据泄露记录和四个与政府效率部个人Gmail员工Kyle Schutt相关的信息窃取日志转储,用于违规跟踪服务Have I Been Pwned。

舒特是一名软件工程师,自今年早些时候埃隆·马斯克(Elon Musk)领导的DOGE开始进行削减成本和重写美国政府内部不确定合法性的代码重写运动以来,已经出现在各种联邦机构。据报道,他已进入核心财务管理系统和联邦紧急事务管理局[,](https://www.wired.com/story/doge-cisa-coristine-cybersecurity/)并加入了网络安全和基础设施安全局。

Lee说,Schutt的凭据出现在大量数据转储中,如Naz.API,Alien txtbase和Telegram泄漏日志。李说,目前还不清楚舒特何时或多久被黑客入侵,但敦促DOGE工作人员避免使用个人设备进行政府工作。

### 网络攻击迫使Nucor停止一些行动

北美最大的钢铁制造商Nucor在涉及未经授权访问其IT系统的网络安全事件后暂时关闭了特定地点的运营。这家北卡罗来纳州公司表示,它启动了事件响应计划,将受影响的系统脱机,并正在努力恢复。它没有透露其大约300个设施中的哪一个受到影响。

### APT37通过假会议邀请韩国人

朝鲜黑客组织APT37,也称为ScarCruft,Reaper和InkySquid,在3月份使用鱼叉式网络钓鱼电子邮件,用伪装成国家安全会议邀请和部队移动情报的恶意软件附件瞄准韩国个人。

韩国Genians的研究人员发现,APT37通过Dropbox提供恶意LNK文件,在受害者设备上部署RoKRAT恶意软件。一场战役冒充了一名地区专家,并声称提供有关朝鲜在俄罗斯部署部队的情报。另一个模仿了一个名为“特朗普2.0时代:前景和韩国的反应”的真实事件。在这两种情况下,APT37都使用与主题相关的图像和 Dropbox 托管的有效载荷来欺骗受害者。

RoKRAT一旦部署,就会窃取系统数据,捕获屏幕截图,执行命令并收集文件。LNK文件运行隐藏的PowerShell脚本,同时显示诱饵文档以分散受害者的注意力。Genians将恶意软件与使用K Messenger聊天室的早期活动联系起来,并指出Dropbox,Yandex,Google Drive和OneDrive等云服务持续滥用于命令和控制。

### 克里姆林宫黑客瞄准Webmail服务器进行间谍活动

俄罗斯网络间谍行动正在攻击乌克兰政府机构和保加利亚和罗马尼亚国防公司使用的网络邮件服务器客户端,这些客户端生产乌克兰军方使用的苏联时代武器。

来自Eset的安全研究人员表示,自2023年以来,他们观察到俄罗斯主要情报局(Russian Main Intelligence Directorate)的网络服务器黑客模式,该单位被称为APT28,Fancy Bear或Forest Blizzard。Eset追踪它作为Sednit。

在Eset dubs Operation RoundPress的竞选活动中,俄罗斯国家黑客在网络邮件服务器中使用了跨站点脚本漏洞,最初专注于Roundcube软件,但在2024年扩展到针对Horde,MDaemon和Zimbra。Sednit可能在MDaemon中发现了一个零日漏洞,[跟踪为CVE-2024-11182](https://www.cve.org/CVERecord?id=CVE-2024-11182),但使用已知的漏洞攻击其他网络邮件服务器。

为了伤害受害者,黑客在鱼叉式网络钓鱼电子邮件中传播了XSS漏洞,该电子邮件下载了包含“Spyrpress”恶意软件变体的恶意JavaScript代码,这些恶意软件欺骗浏览器和密码管理器将webmail凭据填充到隐藏表单中。一些样本通过将用户从其网络邮件中注销并显示虚假登录页面来欺骗用户。

2023年,乌克兰计算机应急小组[(](https://cert.gov.ua/article/4905829)Ukraney Computer Emergency Response Team)警告说,俄罗斯的一场运动利用了三个RoundCube漏洞。Eset表示,其他RoundPress行动的目标包括非洲,欧盟和南美洲的政府机构。

Webmail服务器仍然是黑客的目标,因为许多组织未能保持其系统最新。“由于可以通过发送电子邮件远程触发漏洞,因此攻击者针对此类服务器进行电子邮件盗窃非常方便,”Eset研究人员补充道。

### 微软在5月份修补了72个缺陷

微软的May Patch周二解决了72个漏洞的安全修复问题,其中包括五个已经被利用的零日和两个被公开披露的漏洞。修补的漏洞中有六个被评为关键,大多数涉及远程代码执行,其余则涉及特权升级,拒绝服务,欺骗和信息披露问题。

[被积极利用的漏洞包括Windows](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-30400) DWM核心库中的一个严重缺陷,使攻击者能够通过无使用后漏洞提升系统的权限。Windows [和 Ancillary Function Driver](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-32709) WinSock 中发现了类似的权限升级漏洞。影响 Microsoft Scripting Engine 的第五个被利用的 bug,如果用户被欺骗在 Edge 或 Internet Explorer 中单击有条目的链接,则可以执行远程代码。

微软还解决了Microsoft Defender for [Identity中公开披露的欺骗漏洞,](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-26685)该漏洞使同一网络上的攻击者能够冒充帐户。Visual Studio 中另一个公开披露的漏洞可以启用命令注入和本地代码执行。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/breach-roundup-sap-netweaver-flaw-draws-hackers-a-28410)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307468](/post/id/307468)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/breach-roundup-sap-netweaver-flaw-draws-hackers-a-28410)

如若转载,请注明出处： <https://www.govinfosecurity.com/breach-roundup-sap-netweaver-flaw-draws-hackers-a-28410>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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

* [![安全KER](https://p0....