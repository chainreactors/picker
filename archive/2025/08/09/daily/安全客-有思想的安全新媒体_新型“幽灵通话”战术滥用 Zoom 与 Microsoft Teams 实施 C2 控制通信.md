---
title: 新型“幽灵通话”战术滥用 Zoom 与 Microsoft Teams 实施 C2 控制通信
url: https://www.anquanke.com/post/id/310933
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:35.480769
---

# 新型“幽灵通话”战术滥用 Zoom 与 Microsoft Teams 实施 C2 控制通信

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

# 新型“幽灵通话”战术滥用 Zoom 与 Microsoft Teams 实施 C2 控制通信

阅读量**69557**

发布时间 : 2025-08-08 17:06:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-ghost-calls-tactic-abuses-zoom-and-microsoft-teams-for-c2-operations/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为“幽灵通话”（Ghost Calls）的新型后渗透阶段指挥与控制（C2）规避手法被披露。该技术滥用了 Zoom、Microsoft Teams 等会议应用所使用的 TURN 服务器，通过可信基础设施实现 C2 通信流量的隧道化。

**Ghost Calls 技术依赖合法凭据、WebRTC 协议以及定制工具，在无需利用漏洞的情况下，绕过大多数现有防御机制和反滥用措施。**

该技术由 Praetorian 安全研究员 Adam Crosser 在 Black Hat USA 大会上首次公布，演讲中指出，该技术可被红队在渗透测试模拟中使用，以提升攻击隐蔽性。

Crosser 在演讲资料中表示：“我们利用的是网页会议协议，这类协议专为实时、低延迟通信设计，通常通过全球分布的媒体服务器运行，这些服务器本身就具备天然的流量中继功能，这种方法允许攻击者将交互式 C2 会话伪装为企业网络中的正常通信流量，外观上与临时加入的一场在线会议并无二致。”

“幽灵通话”（Ghost Calls）技术的运作机制如下：

**TURN（Traversal Using Relays around NAT）**是一种常用于视频通话、VoIP 和 WebRTC 服务的网络协议，旨在帮助处于 NAT 防火墙后的设备在无法建立直接连接时实现通信。

在 Zoom 或 Microsoft Teams 客户端加入会议时，客户端会接收**临时的 TURN 凭据**。Ghost Calls 技术可劫持这些凭据，在攻击者与受害者之间建立基于 TURN 的 WebRTC 隧道连接。

一旦**隧道建立**，攻击者即可通过该通道代理任意数据流，或将指挥控制（C2）通信伪装为常规视频会议流量，从而**利用 Zoom 或 Teams 的可信基础设施隐藏恶意行为**。

由于这些通信流量通过 Zoom 或 Teams 的合法域名和 IP 地址路由，这些地址广泛存在于企业环境中，因此**可绕过传统防火墙、代理服务器及 TLS 流量检测机制**。此外，WebRTC 通信本身即为加密流量，进一步增强了隐蔽性。

通过滥用上述工具，攻击者既无需暴露其自身域名和基础设施，又能获得高性能、稳定的连接，并灵活使用 **UDP** 和 **TCP**（均通过 443 端口）进行通信。

相比之下，传统的 C2 通信方式通常速度较慢、容易暴露，且往往缺乏执行远程桌面控制（如 VNC）所需的实时交互能力。

![]()

Crosser 的研究成果最终促成了一款名为 **“TURNt”** 的开源工具的开发（现已在 GitHub 上发布），该工具可通过 Zoom 和 Microsoft Teams 提供的 WebRTC TURN 服务器对 C2（指挥与控制）流量进行隧道传输。

Crosser 的研究最终开发出一个名为 **“TURNt”** 的开源实用工具（已在 GitHub 上发布），可用于通过 Zoom 和 Teams 提供的 WebRTC TURN 服务器对 C2 流量进行隧道传输。

TURNt 包含两个组件，分别是运行在攻击者一侧的 **Controller** 和部署在被入侵主机上的 **Relay**。

Controller 运行一个 SOCKS 代理服务器，用于接收通过 TURN 隧道传输的连接。Relay 使用 TURN 凭据连接回 Controller，并通过提供商的 TURN 服务器建立 WebRTC 数据通道。

![]()

TURNt 可执行 SOCKS 代理转发、本地或远程端口转发、数据外泄，以及隐藏的 VNC（虚拟网络计算）流量隧道传输。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-ghost-calls-tactic-abuses-zoom-and-microsoft-teams-for-c2-operations/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310933](/post/id/310933)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-ghost-calls-tactic-abuses-zoom-and-microsoft-teams-for-c2-operations/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-ghost-calls-tactic-abuses-zoom-and-microsoft-teams-for-c2-operations/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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