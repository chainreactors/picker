---
title: 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-攻击的主要阶段
url: https://mp.weixin.qq.com/s/UNu8yHO9Oz3LbRFLAxTi2w
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:51.822871
---

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-攻击的主要阶段

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OGY0zAl6wlkl0GcQRSZPbichCe9k6H8hEqnFVRkRic4aFl43bURKGZUWaI1PzAia5ibNWSk4LZFWJj3w/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-攻击的主要阶段

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7UnMUNqGIz071DWbJdrzpdJpDxlHDFtnMDlvK8TeibfibdovgH3vMKfIloQibicL6TTiaXQib28nacKJv8qx7AJNnm8g/640?wx_fmt=gif)

**点击蓝字**

**关注我们**

关注我，带给你不一样的精彩

世界因你的沉淀而出彩

**始于理论，源于实践，终于实战**

**老付话安全，每天一点点**

**激情永无限，进步看得见**

![](https://mmbiz.qpic.cn/mmbiz_png/lB1oaPhdMNvxZ67rEjeQWUFqwCxiacBblWHRAxzuoMfYPQXETZ7Y5bsGSLBPy2QGDKIbia74ruAWgJXhWkMlGgkA/640?wx_fmt=png)

**严正声明**

本号所写文章方法和工具只用于学习和交流，严禁使用文章所述内容中的方法未经许可的情况下对生产系统进行方法验证实施，发生一切问题由相关个人承担法律责任，其与本号无关。

特此声明！！！

本文字数：

3103字

阅读时间：

15分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

黑客攻击已成为一个专业化职业。我们不再需要过多担心那些窝在父母家地下室的“脚本小子”、像Nimda那样肆意传播的恶意软件，或是零散、随机的机会主义攻击。现在，我们面对的是高度组织化、专业分工明确、并且聚焦于特定目标的精英团队——无论他们的目标是什么。

**一些高级 ICS 攻击者的主要目标包括：**

* **破坏生产流程与可用性** – 通过操纵控制逻辑或发起拒绝服务，导致生产线停工、供应链中断或公共服务瘫痪。
* **造成物理设备损坏** – 利用控制指令超限运行（如超速、超压、过热），直接损坏压缩机、涡轮机、发电机等关键资产。
* **窃取专有工艺与工程数据** – 获取工艺配方、逻辑图、参数配置等敏感信息，用于复制、逆向工程或后续攻击。
* **实施勒索或商业胁迫** – 加密上位机或控制器数据，同时威胁破坏物理过程，迫使受害者支付高额赎金。
* **远程获得持久控制权** – 在 ICS 环境中植入隐蔽后门或高级持续威胁（APT），为后续的破坏、间谍或切换攻击奠定基础。

攻击阶段和任务

|  |  |  |
| --- | --- | --- |
| 目标开发 （TD） | 利用与转移（E&P） | 攻击行动 |
| 研究调查 | 入侵点利用 | 绕过&逃逸 |
| 目标网络地图 | 特权提升(EoP)技术 | C&C基础设施 |
| 确定潜在的入侵点 | 转储技术 | 持久化，远程访问 |
| 制定攻击计划 | 目标网络横向移动 | 恶意软件更新 |
| 构建工具包 |  | 系统数据获取 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmib5jThSNz8J1FtFrDib5rYgbtgiblqstSXRo4ZuSmPbtMV5RiczOD96cL8afQKf1xib7pIaeMSUolawic933x9UA1tNOszREonjXCRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tE7RtngPUmibdGNbuxs1F4uWonjQ0TlJ1LWjWWbSuPOeRsr1szDoCrKnTIDrbicfa6nkyjhYq9JKicaHQ9YhTFjsBebvgMLoX1hAicUbke6Diahw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tE7RtngPUmibNZX5fnpa2auSSEj6Bpm8NBcJ3wiag79YQkC7YG0Vx7icETz2DKFLDrUGWfspbjfNIVic1BWpNQn0JwQsNaJlNZApfWs5fZGM70E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUm8GZrk7KVjRqqPTWThKUe5b33vFcL79PLiaK7PZpyAszwd1f29Dc8MH8xj2X1R6x8cq2icOicJiazSrhiafuRH6rE0rxJbyPib2ll5Ko/640?wx_fmt=png&from=appmsg)

攻击者将开始使用Nmap 等发现工具主动映射或探测目标网络，并寻找 SQL 注入漏洞等其他弱 点。结果将被记录和组织以备将来使用。

在此阶段，攻击者将评估收集的所有信息，然后确定运行初 始攻击的最佳位置并确定其优先级。 攻击者将开始利用漏洞发现工具和技术。在漏洞发现过程中，攻击者会探测易受攻 击的服务、软件或配置的目标，以识别潜在的入口点并规划社会工程活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUm8rfovG6nvlnAhRK9liaLysyE2VYEpHhzEjyNFG57OUNmwgoz7j5cjDMpPynTD8Cmja4XfVuuwmgZv13spk3pVIzuC6YorswHfA/640?wx_fmt=png&from=appmsg)

探索潜在的切入点。在此阶段，攻击者将评估收集的所有信息，然后确定运行初 始攻击的最佳位置并确定其优先级。 攻击者将开始利用漏洞发现工具和技术。在漏洞发现过程中，攻击者会探测易受攻 击的服务、软件或配置的目标，以识别潜在的入口点并规划社会工程活动

计划攻击– 一旦收集到数据，攻击者将使用标准项目管理方法来计划攻击。随着项目迈向获得初始入口点 （PoE） 的下一阶段，需要进行分配、分配资源、选择可能的漏洞以及适当的漏洞利用。

构建工具包– 对于此培训，我们将使用 Metasploit 框架 （MSF），但是，专业攻击者拥有自己的高度专业化的工具包。您可能听说过的一些开发工具包是BlackEnergy、Flame和 Regin。

## 攻击者的核心能力维度

**持久化技术** – 攻击者用于最初突破目标并建立长期访问权限的技术、工具或手法。典型示例包括：植入后门、创建计划任务、注册表自启动、或利用合法远程管理工具。

**横向移动技术** – 攻击者在受感染网络内寻找其他高价值目标并加以破坏的技术、工具或手法。其中，“转储”（Pivoting）技术常用于在不同信任级别的网段或系统之间跳跃。

## 攻击者的三重奏

攻击者的三重奏是成功利用系统所必须同时具备的三个要素，三者任意组合即可构成一次有效攻击：

* **有效载荷** – 攻击者在目标系统上获取**执行权限（PoE）** 所使用的代码或指令。例如：反弹Shell、下载器、勒索软件主体。
* **漏洞利用程序** – 针对特定漏洞开发的代码或技术，用于首次进入目标系统，并通常以**权限提升**为目的。
* **攻击路径（传递机制）** – 将漏洞利用程序传递给脆弱目标的手段或通道。例如：钓鱼邮件中的链接、恶意USB设备、供应链污染、远程网络端口扫描+攻击。

系统漏洞

接下来，我们将讨论两种类型的漏洞：系统（或环境）和软件。

NIST SP 800-30 将系统漏洞定义为“系统安全程序、设计、实施或内部控制中的缺陷或弱点，可以被执行 （意外触发或故意利用）并导致安全漏洞或违反系统的安全策略。

系统或环境漏洞的存在是因为目标环境的所有者未适当地设计、实施或维护系统资源。

系统漏洞实例：

* 应用程序和/或服务的默认和/或硬编码和/或容易猜到的密码。
* 安装后未更改（或不能更改）的操作系统。
* 在公布漏洞时未能及时升级、更新或缓解软件。
* 在网络上，没有通过防火墙或网络分段充分隔离关键资源。
* 直接访问和/或从 ICS 系统和设备访问公共互联网。
* 敏感的公司文档在不安全的情况下驻留在面向公众的服务器上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmicT6WhUaK8DPYXtQDWwO2Eb7iayFzxXIcEZibntA3dM0Tiaa2y9WWErcmr6jJj2x3ftp7l8XUnj0npMjr2uM2yBibtZibsaSw6Q5OTs/640?wx_fmt=png&from=appmsg)

CVSS分数表示漏洞被利用的可能性，具体取决于利用它的难易程度、访问向量、访问复杂性和利用它所需的 身份验证。它还解决了成功利用漏洞在机密性、完整性和可用性方面对目标系统产生的技术影响。CVSS分数 范围从 1 到 10，其中 10代表最高级别的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUm9jZU3PhtJo4YbiacSJnjPzSqibDqD4iaVGib0JW4fZV7rQGUcibVaJnibqyNRthj3R3SJC11dku2lF6cm8eUja45ibpLZo41bZmsGrF4/640?wx_fmt=png&from=appmsg)

漏洞利用是攻击者用来利用漏洞造成意外或意外行为的一种攻击技术。漏洞利用是攻击技术的一个子类别，用于执行特定任务（利用），从而导致目标系统上的入口点。

漏洞利用或 shell代码（漏洞利用的另一个术语）也可能允许攻击者提升权限并在系统上放置有 效负载。然而，随着软件供应商实施安全代码开发程序，这种漏洞利用类型变得越来越不常见。如今，漏洞利用更有可能包含在漏洞利用工具包等有效载荷中。

我们将从以下方面讨论攻击技术或漏洞利用：

* 利用传递位置（远程、本地）
* 目标系统（服务器端、客户端）上的漏洞来源。

远程攻击– 在远程攻击中，攻击者试图利用以下任何系统：

* 可以通过Internet或任何其他网络远程运行到易受攻击的系统
* 不需要攻击者在运行漏洞利用之前登录到目标系统。

远程漏洞利用通常比本地漏洞利用要严重得多，但幸运的是，远程漏洞利用更容易预防，而且通常不太常见。互联网上数以亿计的人中的任何一个人都可以随时发起远程攻击。

最常见的远程漏洞利用是缓冲区溢出和其他未经检查的输入攻击。它们要么是针对公共服务（如 HTTP 和FTP）执行的，要么是在登录受保护服务（如 SSH 和IMAP）时执行的。

注意：具有良好安全编码实践的软件供应商将首先尝试消除可远程利用的漏洞。Microsoft从XP Service Pack 2的发布开始这样做，导致攻击者利用应用程序而不是操作系统。

本地漏洞利用 – 攻击者可以访问相关系统上的帐户，并可以使用该帐户尝试未经授权的任务。

本地漏洞利用更为常见且难以预防。

服务器端攻击 –服务器公开客户端可以与之交互的服务，这些服务包括文件共享等内容。当服务器向客户端 提供服务时，它可能会暴露出可以受到攻击的漏洞。SQL注入是一种服务器端攻击。

客户端攻击 – 客户端攻击针对客户端应用程序中与恶意数据交互的漏洞。不同之处在于客户端是启动不 良连接的客户端。 客户端攻击正变得越来越流行。这是因为服务器端攻击不像以前那么容易了。

攻击者在追踪桌面应用程序（如浏览器、媒体播放器、常见办公应用程序和电子邮件客户端）的弱点时发 现成功。这些客户端应用程序不像服务器应用程序那样侦听 TCP 或UDP 端口上的连接，而是调用服务器。一旦客户端连接到受感染的服务器，服务器就会尝试将漏洞下载到客户端，从而绕过许多面向前向的安全障碍。

end

**往期内容**回顾****

|  |
| --- |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用过程](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486037&idx=1&sn=611a127747a9b05e02a2ef4bf1114e0c&scene=21#wechat_redirect) |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用（一）ICS过程控制漏洞概述](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486039&idx=1&sn=9da3debdeee21e4d6eca9efc0838d3cd&scene=21#wechat_redirect) |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用（二）典型漏洞利用路径](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486040&idx=1&sn=500f7e115c7abb2e44d3ee9326382085&scene=21#wechat_redirect) |

@请赐予我力量，关注和转发是最大的支持@

欢迎扫码进群交流

![](https://mmbiz.qpic.cn/mmbiz_jpg/tE7RtngPUm85FtZKuNRCbqvutVXOSqIphpS43hcaArSJeUjiaWxOLoibkPBlQbE6FdlN2wic4Lf7tqq7ibouYzjfzQcnRkWBGYhp9ZMVOP71PVI/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

老付话安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过