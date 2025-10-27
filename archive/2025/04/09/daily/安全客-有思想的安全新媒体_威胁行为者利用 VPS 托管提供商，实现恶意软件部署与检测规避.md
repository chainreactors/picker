---
title: 威胁行为者利用 VPS 托管提供商，实现恶意软件部署与检测规避
url: https://www.anquanke.com/post/id/306278
source: 安全客-有思想的安全新媒体
date: 2025-04-09
fetch_date: 2025-10-06T22:03:41.784106
---

# 威胁行为者利用 VPS 托管提供商，实现恶意软件部署与检测规避

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

# 威胁行为者利用 VPS 托管提供商，实现恶意软件部署与检测规避

阅读量**54706**

发布时间 : 2025-04-08 14:11:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-leveraging-vps-hosting-providers/>

译文仅供参考，具体内容表达以及含义原文为准。

一场精心策划的恶意软件攻击活动正在向墨西哥、阿根廷和西班牙的用户下手，攻击者通过精心设计的冒充税务机构的网络钓鱼邮件来传播 Grandoreiro 银行木马。

这次攻击利用了一个多阶段的感染链条。一开始，受害者会收到虚假的政府通知，声称他们面临着巨额的税务罚款，这种紧迫感迫使受害者点击这些通信内容中嵌入的恶意链接。

该攻击活动采用了复杂的基础设施，利用了托管在 Contabo 网络上的虚拟专用服务器（VPS），这表明威胁行为者越来越倾向于使用合法的托管服务来逃避检测。攻击者专门利用 contaboserver.net 下的子域名，例如 vmi2500240.contaboserver.net，这些子域名与特定的虚拟机相关联。

这种方法为攻击者提供了一层合法的伪装，同时，当这些域名被安全解决方案标记时，他们能够迅速转移基础设施。

当受害者点击这些网络钓鱼邮件中的链接时，他们会被重定向到这些由 Contabo 托管且设置了地理围栏的网址，这些网址会显示一个虚假的税务文件门户。

该页面上有一个 “下载 PDF” 按钮，点击该按钮后，会启动一系列重定向操作，最终导致受害者从合法的文件共享服务 “Mediafire” 上下载一个受密码保护的 ZIP 文件。

在攻击链条中使用多个合法服务的这种技术，极大地增加了检测的难度。

Forcepoint 的研究人员发现，这些攻击者在每次攻击活动中都会频繁更换 contaboserver.net 下的子域名，这使得安全解决方案很难跟上封堵的步伐。

研究人员注意到，攻击者熟练运用地理围栏技术，针对特定地区发动攻击，同时避开安全研究人员的环境。

****感染机制分析****

当受害者解压这个受密码保护（密码：2025）且包含大量混淆代码的 Visual Basic 脚本的 ZIP 文件时，感染过程就开始了。

这个 VBS 文件包含大量故意设置的干扰信息，使用句点和其他不必要的字符来掩盖其真实功能。

在这个脚本中嵌入了一个经过 Base64 编码的负载，该负载被分割成多个块。

执行脚本时，它会将这些片段连接起来并进行解码，以提取另一个 ZIP 文件，并将其放置在 Public 用户目录中。

这个 ZIP 文件包含一个经过 Delphi 编译的可执行文件，该文件伪装成 PDF 图标，运行时会显示一个虚假的 Adobe Reader 错误消息。

这种社会工程策略让用户相信他们处理的是一个合法的文档问题，而此时恶意软件在后台悄然建立起持久的存在。

根据版本信息，这个可执行文件声称来自 “ByteCore Technologies 706092 Inc.”，它使用不常见的端口配置（例如 42195）连接到命令控制服务器。

该恶意软件专门针对金融信息，扫描比特币钱包目录，并通过注册表查询（如 “HKEY\_LOCAL\_MACHINE\SYSTEM\ControlSet001\Control\NIs\Sorting\Versions”）收集系统信息，以确定语言设置和机器标识符。

Grandoreiro 木马的多层混淆技术以及对合法基础设施的利用，凸显了现代威胁行为者如何不断演变他们的攻击策略以绕过安全控制措施。

企业必须实施多层防御措施，以便能够在整个攻击链条中检测到此类威胁，从最初的网络钓鱼企图，到负载执行以及命令控制通信等各个环节。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-leveraging-vps-hosting-providers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306278](/post/id/306278)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-leveraging-vps-hosting-providers/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-leveraging-vps-hosting-providers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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