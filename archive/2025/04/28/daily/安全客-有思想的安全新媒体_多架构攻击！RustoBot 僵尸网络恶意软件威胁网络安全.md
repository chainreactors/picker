---
title: 多架构攻击！RustoBot 僵尸网络恶意软件威胁网络安全
url: https://www.anquanke.com/post/id/306930
source: 安全客-有思想的安全新媒体
date: 2025-04-28
fetch_date: 2025-10-06T22:04:13.736677
---

# 多架构攻击！RustoBot 僵尸网络恶意软件威胁网络安全

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

# 多架构攻击！RustoBot 僵尸网络恶意软件威胁网络安全

阅读量**73523**

|评论**1**

发布时间 : 2025-04-27 14:50:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-rust-botnet-hijacking-routers/>

译文仅供参考，具体内容表达以及含义原文为准。

一种使用 Rust 编程语言编写的复杂新型僵尸网络恶意软件已被发现，其目标是全球范围内存在漏洞的路由器设备。

由于该恶意软件是基于 Rust 语言编写的，因此被命名为 “RustoBot”。它利用了 TOTOLINK 和 DrayTek 路由器型号中的严重漏洞来执行远程命令注入，这有可能影响到日本、越南和墨西哥的科技产业。

该僵尸网络主要通过 cstecgi.cgi 文件中的漏洞攻击 TOTOLINK 型号的路由器，包括 N600R、A830R、A3100R、A950RG、A800R、A3000RU 和 A810R。cstecgi.cgi 是一个负责处理用户输入和管理命令的 CGI 脚本。

这些脚本包含命令注入缺陷，使得攻击者能够在被入侵的设备上实现远程代码执行。

同样，DrayTek Vigor2960 和 Vigor300B 路由器则受到 CVE-2024-12987 漏洞的影响，该漏洞是位于 cgi-bin/mainfunction.cgi/apmcfgupload 接口中的操作系统命令注入漏洞。

初始的攻击利用从简单但有效的有效载荷开始，这些有效载荷利用了上述漏洞。

对于 TOTOLINK 设备，攻击方会向存在漏洞的 cstecgi.cgi 端点发送精心构造的请求，并附带恶意命令字符串，以实现恶意软件的下载和执行。

它展示了利用有效载荷的攻击技术，该有效载荷使用 wget 命令下载并执行专门针对 TOTOLINK 架构的 “mpsl” 二进制文件。

Fortinet 的研究人员发现，在成功实现初始入侵后，RustoBot 会通过四个不同的下载器脚本部署多个针对特定架构的变体，目标架构包括 arm5、arm6、arm7、mips 和 mpsl。

****多架构攻击方式****

这种多架构的攻击方式确保了该恶意软件在各种路由器型号和嵌入式系统中具有广泛的兼容性。

该恶意软件的复杂设计包括多种用于运行和逃避检测的先进技术。

RustoBot 从全局偏移表（GOT）中检索系统 API 函数，并采用异或（XOR）加密对其配置数据进行编码。

该恶意软件使用复杂的指令序列来计算解码器密钥偏移量：

get\_key\_offset\_4 proc near

xor esi, 803C490h

imul eax, esi, 0B0D0D74h

xor eax, 120ED6A5h

mov ecx, eax

shr ecx, 1Ch

xor ecx, eax

imul eax, ecx, 0D921h

movzx eax, ax

add rax, rdi

retn

get\_key\_offset\_4 endp

一旦在被入侵的设备上站稳脚跟，RustoBot 就会通过解析诸如 dvrhelper.anondns.net、techsupport.anondns.net、rustbot.anondns.net 和 miraisucks.anondns.net 等域名，连接到其命令与控制基础设施，而所有这些域名都解析到同一个 IP 地址（5.255.125.150）。

然后，该僵尸网络等待指令以发动各种分布式拒绝服务（DDoS）攻击，包括 UDP 泛洪攻击。在 UDP 泛洪攻击中，它会生成大量包含 1400 字节有效载荷的 UDP 数据包，并发送到指定的目标 IP 地址和端口，从而使受害者的基础设施不堪重负。

这一新兴威胁凸显了物联网（IoT）和网络设备持续存在的脆弱性，以及僵尸网络恶意软件日益复杂的发展趋势，它们利用像 Rust 这样的现代编程语言来提高稳定性和跨平台兼容性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-rust-botnet-hijacking-routers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306930](/post/id/306930)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-rust-botnet-hijacking-routers/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-rust-botnet-hijacking-routers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**10赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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