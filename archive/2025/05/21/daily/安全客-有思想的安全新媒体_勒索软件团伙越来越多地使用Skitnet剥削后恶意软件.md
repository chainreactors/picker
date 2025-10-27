---
title: 勒索软件团伙越来越多地使用Skitnet剥削后恶意软件
url: https://www.anquanke.com/post/id/307581
source: 安全客-有思想的安全新媒体
date: 2025-05-21
fetch_date: 2025-10-06T22:25:28.478222
---

# 勒索软件团伙越来越多地使用Skitnet剥削后恶意软件

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

# 勒索软件团伙越来越多地使用Skitnet剥削后恶意软件

阅读量**72914**

发布时间 : 2025-05-20 15:11:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 比尔·图拉斯，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/ransomware-gangs-increasingly-use-skitnet-post-exploitation-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![勒索软件]()

勒索软件团伙成员越来越多地使用一种名为Skitnet(“Bossnet”)的新恶意软件,在被破坏的网络上进行隐秘的剥削后活动。

自2024年4月以来,该恶意软件已在RAMP等地下论坛上出售,但根据Prodaft研究人员的说法,自2025年初以来,它开始在勒索软件团伙中获得显着的吸引力。

Prodaft告诉BleepingComputer,他们观察到多个勒索软件操作在现实世界中部署了Skitnet,包括Microsoft Teams针对企业的网络钓鱼攻击中的BlackBasta和Cactus。

![在地下论坛上推广的恶意软件]()

**在地下论坛上推广的恶意软件**
*来源:Prodaft*

##

### 隐身和强大的后门

Skitnet感染始于基于Rust的加载器在目标系统上下放并执行,该系统解密了ChaCha20加密的Nim二进制文件并将其加载到内存中。

Nim 有效载荷建立了一个基于 DNS 的反向外壳,用于与命令和控制 (C2) 服务器通信,通过随机 DNS 查询启动会话。

恶意软件启动三个线程,一个用于发送心跳DNS请求,一个用于监视和泄露shell输出,一个用于侦听和解密DNS响应的命令。

要执行的通信和命令通过 HTTP 或 DNS 发送,基于通过 Skitnet C2 控制面板发出的命令。C2 面板允许操作员查看目标的 IP、位置、状态和发出执行命令。

![Skitnet 管理面板]()

**Skitnet 管理面板**
*来源:Prodaft*

支持的命令有:

* **startup –** 通过下载三个文件(包括恶意DLL)并在启动文件夹中创建合法华硕可执行文件(ISP.exe)的快捷方式来建立持久性。这触发了执行PowerShell脚本(pas.ps1)以进行持续C2通信的DLL劫持。
* **屏幕** – 使用 PowerShell 捕获受害者桌面的屏幕截图,将其上传到 Imgur,然后将图像 URL 发送回 C2 服务器。
* **Anydesk** Anydesk – 下载并默默地安装AnyDesk,一个合法的远程访问工具,同时隐藏窗口和通知托盘图标。
* **Rutserv** – 下载并默默地安装RUT-Serv,另一个合法的远程访问工具。
* **Shell** – 启动 PowerShell 命令循环。发送初始“壳牌开始……”消息,然后反复投票(?m) 使用 Invoke-Expression 执行的新命令,服务器每 5 秒一次,并发送结果。
* **Av** – 通过查询 WMI(在 root\SecurityCenter2 命名空间中的 SELECT \* FROM AntiVirusProduct ) 来枚举已安装的防病毒和安全软件。将结果发送到 C2 服务器。

除了核心命令集之外,操作人员还可以利用涉及 .NET加载器,允许他们在内存中执行PowerShell脚本,以进行更深入的攻击定制。

![Skitnet的。NET 装载机]()

**Skitnet的。NET 装载机**
*来源:Prodaft*

虽然勒索软件组经常使用针对特定操作量身定制的定制工具,并且具有低AV检测,但这些开发成本高昂,并且需要技术娴熟的开发人员,这些开发人员并不总是可用的,特别是在低层组中。

使用像Skitnet这样的现成恶意软件更便宜,部署速度更快,并且可以使归因更加困难,因为许多威胁行为者使用它。

在勒索软件领域,这两种方法都有空间,甚至是两者的混合,但Skitnet的功能使其特别吸引黑客。

Prodaft 在其 [GitHub](https://github.com/prodaft/malware-ioc/tree/master/Skitnet) 存储库中发布了与 Skitnet 相关的折衷指标 (IoCs)。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/ransomware-gangs-increasingly-use-skitnet-post-exploitation-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307581](/post/id/307581)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/security/ransomware-gangs-increasingly-use-skitnet-post-exploitation-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/ransomware-gangs-increasingly-use-skitnet-post-exploitation-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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