---
title: Trustwave 的威胁情报团队发现了名为 Pronsis Loader 的新型恶意软件
url: https://www.anquanke.com/post/id/300658
source: 安全客-有思想的安全新媒体
date: 2024-10-10
fetch_date: 2025-10-06T18:51:45.858436
---

# Trustwave 的威胁情报团队发现了名为 Pronsis Loader 的新型恶意软件

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

# Trustwave 的威胁情报团队发现了名为 Pronsis Loader 的新型恶意软件

阅读量**153618**

发布时间 : 2024-10-09 11:24:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/pronsis-loader-the-emerging-threat-behind-jphp-driven-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![2023 Threat Report]()

由 Cris Tomboc 和 King Orande 领导的 Trustwave 威胁情报团队最近发布了一份报告，公布了一种新发现的名为 Pronsis Loader 的恶意软件。该恶意软件于 2023 年 11 月首次出现，与 2024 年初出现的类似威胁 D3F@ck Loader 进行了比较。Pronsis Loader 的显著特点是它能发送 Lumma Stealer 和 Latrodectus 等恶意软件，给受害者带来巨大风险。发现其基础设施与 Lumma Stealer 相关联，凸显了这一不断演变的威胁的规模。

Pronsis Loader 与其他加载程序的不同之处在于它使用了 JPHP（一种 PHP 的 Java 实现）。“研究人员解释说：”两者都使用 JPHP 编译的可执行文件，因此很容易互换。不过，与使用 Inno Setup Installer 的 D3F@ck Loader 不同，Pronsis Loader 部署的是 Nullsoft Scriptable Install System（NSIS）。这种开源工具可以定制 Windows 安装程序，使 Pronsis Loader 在安装技术上具有明显优势。

Pronsis 加载器

![Pronsis Loader]()
Pronsis Loader 使用 NSIS | 图片： Trustwave

有趣的是，JPHP 在恶意软件开发者中并不广泛使用，这使得 Pronsis Loader 对这种语言的依赖偏离了典型的恶意软件环境。这种实现方式允许创建 .phb 文件，而使用传统的 Java 工具无法轻松反编译这些文件。尽管存在这种复杂性，但由于这些文件中存在 CAFEBABE 标头，威胁分析人员可以在提取后对其进行反编译，从而揭示其真实性质。

Pronsis Loader 的安装程序包含大量有效载荷，其中大部分由良性文件组成，旨在掩盖内嵌的恶意代码。据研究人员称，“安装程序的大部分内容由良性文件组成，旨在掩盖恶意文件”。这些文件被放入 %Temp% 目录，但其中隐藏着一个关键的可执行文件–FailWorker-Install.exe，它包含真正的恶意软件。

该可执行文件会触发一系列事件，通过 NSIS 插件调用 Nact.dll 文件来运行 JPHP 编译的加载程序。提取后，可以在 JPHP-INF 目录中找到主模块，其中 launcher.conf 文件指定了 app\modules 目录的初始 .bootstrap 文件。Pronsis Loader 的结构允许它从指定 URL 下载有效载荷，然后发送 Latrodectus 恶意软件。该恶意软件主要通过钓鱼邮件传播，与 IcedID 等其他已知威胁如出一辙。

Pronsis Loader 具有逃避检测的嵌入式功能。其中一种规避技术是通过隐藏在 MainForm.phb 文件中的 PowerShell 脚本实现的。这个编码脚本会禁用 Windows Defender 对用户配置文件目录的扫描，使恶意软件更容易运行而不被发现。“报告强调说：”这个 PowerShell 命令将被放置在一个批处理文件中，文件名为随机数字，并通过 cmd.exe 执行。

通过部署 Lumma Stealer 和 Latrodectus，进一步证明了 Pronsis Loader 提供多种有效载荷的能力。Latrodectus 于 2023 年 10 月首次被观察到，因其激进的感染技术而备受关注。受感染的机器会加载一系列批处理文件和可执行文件，以方便恶意软件的安装和持续运行。

在一个实例中，Latrodectus 通过一个名为 todaydatabase.zip 的文件发送，该文件将一个可执行文件放入 %Temp% 目录，启动了感染过程。安装完成后，Latrodectus 会使用计划任务来确保持久性，每 10 分钟运行一次，重新执行其恶意组件。此外，该恶意软件还创建了一个名为 runnung 的互斥程序来管理持续感染。

Pronsis Loader 的推出标志着 JPHP 作为恶意软件平台的使用发生了重大转变。通过利用 NSIS 安装程序和规避典型的安全协议，Pronsis Loader 对网络安全防御者提出了严峻的挑战。报告强调，这种加载器 “突出了它与 D3F@ck Loader 的相似之处，以及它在提供 Lumma Stealer 和 Latrodectus 作为主要有效载荷方面的作用”。

本文翻译自securityonline [原文链接](https://securityonline.info/pronsis-loader-the-emerging-threat-behind-jphp-driven-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300658](/post/id/300658)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pronsis-loader-the-emerging-threat-behind-jphp-driven-malware/)

如若转载,请注明出处： <https://securityonline.info/pronsis-loader-the-emerging-threat-behind-jphp-driven-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**7赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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