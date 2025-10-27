---
title: RustoBot 利用路由器漏洞，借 Rust 语言发动 DDoS 跨境攻击
url: https://www.anquanke.com/post/id/306777
source: 安全客-有思想的安全新媒体
date: 2025-04-23
fetch_date: 2025-10-06T22:04:46.914964
---

# RustoBot 利用路由器漏洞，借 Rust 语言发动 DDoS 跨境攻击

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

# RustoBot 利用路由器漏洞，借 Rust 语言发动 DDoS 跨境攻击

阅读量**59918**

发布时间 : 2025-04-22 12:20:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/rustobot-botnet-exploits-router-flaws-in-sophisticated-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![RustoBot, Router Vulnerability]()

FortiGuard Labs 最近发现了名为 RustoBot 的恶意程序，它是用 Rust 语言编写的。Rust 是一种以性能和安全性著称的内存安全型语言。RustoBot 是一个复杂的僵尸网络，它利用了 TOTOLINK 和 DrayTek 路由器中的漏洞，从而在日本、越南和墨西哥的技术基础设施中占据了一席之地。

在 2025 年初，FortiGuard Labs 的分析师注意到，利用 TOTOLINK 的 cstecgi.cgi 脚本中存在已久的漏洞进行的攻击尝试数量急剧上升。这个组件负责配置更改和身份验证，其中存在多个命令注入漏洞。

所利用的关键漏洞包括：

1.CVE-2022-26210（通过 setUpgradeFW 利用）

2.CVE-2022-26187（通过 pingCheck 利用）

3.CVE-2024-12987（通过 /cgi-bin/mainfunction.cgi/apmcfgupload 影响DrayTek的路由器）

这些漏洞使攻击者获得了远程代码执行能力，为 RustoBot 的感染埋下了隐患。

![RustoBot, Router Vulnerability]()

TOTOLINK devices 命令注入漏洞的有效载荷 |图片来源： FortiGuard Labs

一旦获得了初始访问权限，RustoBot 就会使用四个下载器脚本中的一个进行部署，这些脚本通过 wget 或 tftp 命令获取。该恶意软件针对多种架构 ——arm5、arm6、arm7、mips、mpsl 和 x86—— 确保与易受攻击的路由器具有广泛的兼容性。

Fortinet 指出：“在观察到的大多数事件有效载荷中，专门针对使用 mpsl 架构的 TOTOLINK 设备。”

RustoBot 的独特之处在于它使用了 Rust 语言。它的二进制结构通过基于异或（XOR）的加密和全局偏移表（GOT）操纵进行了混淆处理，这使其具有隐蔽性，并增加了逆向工程的难度。

解密后的配置揭示了 RustoBot 的真实意图。它执行两项核心恶意操作：

1.解析多个命令与控制（C2）域名，如 dvrhelper [.] anondns [.] net，所有这些域名都指向 5 [.] 255 [.] 125 [.] 150。

2.按命令发起分布式拒绝服务（DDoS）攻击。

这个僵尸程序首先使用基于 HTTPS 的 DNS（DoH）获取受感染设备的公共 IP 地址，巧妙地将恶意流量与正常的 HTTPS 活动混在一起。然后，它从命令与控制（C2）服务器接收攻击指令，包括：

1.DDoS 攻击方法（例如，UDP）

2.目标 IP 地址和端口

3.攻击持续时间

4，数据包长度

Fortinet 表示：“它可以使用三种不同的协议发起 DDoS 攻击：原始 IP、TCP 和 UDP。”

到目前为止，RustoBot 攻击活动已经影响了以下设备：

1.TOTOLINK 型号：N600R、A830R、A3100R、A950RG、A800R、A3000RU、A810R

2.DrayTek 型号：Vigor2960、Vigor300B

受害者主要位于日本、越南和墨西哥的科技领域，这表明这可能是一次有针对性的攻击活动。

对于 RustoBot，攻击者使用 Rust 语言不仅仅是为了新奇，更是看中了它的性能以及对基于内存攻击的抵抗力。正如 Fortinet 所警告的：

“物联网和网络设备往往是防护薄弱的端点，这使它们成为有吸引力的攻击目标…… 加强端点监控和身份验证可以显著降低风险。”

各组织应立即修补已知漏洞，对暴露的设备进行审计，并监控出站流量模式以检测异常行为 —— 尤其是基于 HTTPS 的 DNS 活动或未经授权的固件更新。

本文翻译自securityonline [原文链接](https://securityonline.info/rustobot-botnet-exploits-router-flaws-in-sophisticated-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306777](/post/id/306777)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/rustobot-botnet-exploits-router-flaws-in-sophisticated-attacks/)

如若转载,请注明出处： <https://securityonline.info/rustobot-botnet-exploits-router-flaws-in-sophisticated-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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