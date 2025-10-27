---
title: 使用 DLL 侧加载技术的 Yokai 后门活动瞄准泰国官员
url: https://www.anquanke.com/post/id/302730
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:48.112937
---

# 使用 DLL 侧加载技术的 Yokai 后门活动瞄准泰国官员

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

# 使用 DLL 侧加载技术的 Yokai 后门活动瞄准泰国官员

阅读量**75081**

|评论**1**

发布时间 : 2024-12-16 10:46:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html>

译文仅供参考，具体内容表达以及含义原文为准。

泰国政府官员成为了一个新活动的目标，该活动利用一种名为 DLL 侧载的技术来传播一种以前未被记录的被称为 “Yokai ”的后门程序。

Netskope 安全效率团队高级工程师 Nikhil Hegde 告诉《黑客新闻》：“根据诱饵的性质，威胁行为者的目标是泰国官员。Yokai后门本身不受限制，可用于攻击任何潜在目标。”

攻击链的起点是一个 RAR 存档，其中包含两个以泰语命名的 Windows 快捷方式文件，分别翻译为 “United States Department of Justice.pdf” 和 “United States government requests international cooperation in criminal matters.docx”。

尽管 Hegde 推测很可能是鱼叉式网络钓鱼，但由于采用了诱饵，而且 RAR 文件一直被用作网络钓鱼电子邮件中的恶意附件，因此目前尚不清楚用于传输有效载荷的确切初始载体。

启动快捷方式文件会分别打开一个诱饵 PDF 和 Microsoft Word 文档，同时还会在后台隐蔽地投放一个恶意可执行文件。这两个诱骗文件都与 Woravit Mektrakarn 有关，他是泰国人，因与一名墨西哥移民的失踪有关而被美国通缉。Mektrakarn 于 2003 年被控谋杀，据说已逃往泰国。

就可执行文件而言，它的设计目的是再投放三个文件： 一个与 iTop Data Recovery 应用程序相关的合法二进制文件（“IdrInit.exe”）、一个恶意 DLL（“ProductStatistics3.dll”）和一个包含由攻击者控制的服务器发送的信息的 DATA 文件。在下一阶段，“IdrInit.exe ”被滥用来侧载 DLL，最终导致后门的部署。

Yokai 负责在主机上设置持久性，并连接到命令与控制 (C2) 服务器，以接收命令代码，从而生成 cmd.exe，并在主机上执行 shell 命令。

Zscaler威胁实验室（Zscaler ThreatLabz）透露，他们发现了一个利用Node.js编译的Windows可执行文件传播加密货币矿机和信息窃取程序（如XMRig、Lumma和Phemedrone Stealer）的恶意软件活动。这些流氓应用程序的代号为 NodeLoader。

这些攻击利用嵌入在 YouTube 视频描述中的恶意链接，将用户引向 MediaFire 或虚假网站，敦促他们下载伪装成视频游戏黑客的 ZIP 压缩包。攻击的最终目的是解压缩并运行 NodeLoader，然后下载一个 PowerShell 脚本，负责启动最后阶段的恶意软件。

Zscaler 表示：“NodeLoader 使用了一个名为 sudo-prompt 的模块，这是 GitHub 和 npm 上的一个公开工具，用于权限升级。威胁者采用社交工程和反规避技术来传播 NodeLoader，而不被发现。”

这也是继传播市售 Remcos RAT 的网络钓鱼攻击激增之后，威胁者通过使用 Visual Basic Script (VBS) 脚本和 Office Open XML 文档作为触发多阶段进程的启动平台，对感染链进行了改造。

在一组攻击中，执行 VBS 文件会导致高度混淆的 PowerShell 脚本下载临时有效载荷，最终将 Remcos RAT 注入合法的 Microsoft .NET 可执行文件 RegAsm.exe。

另一个变种需要使用 Office Open XML 文档加载一个 RTF 文件，该文件易受 CVE-2017-11882 的影响（CVE-2017-11882 是 Microsoft Equation Editor 中的一个已知远程代码执行漏洞），以获取一个 VBS 文件，然后继续获取 PowerShell，以便将 Remcos 有效载荷注入 RegAsm.exe 的内存中。

值得指出的是，这两种方法都避免将文件写入磁盘，而是将其加载到有效进程中，故意逃避安全产品的检测。

McAfee 实验室的研究人员说：“由于这种远程访问木马继续通过钓鱼电子邮件和恶意附件瞄准消费者，因此采取积极主动的网络安全措施比以往任何时候都更为重要。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302730](/post/id/302730)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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