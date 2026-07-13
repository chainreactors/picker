---
title: 什么是 ICMP（互联网控制消息协议）？
url: https://mp.weixin.qq.com/s/oyw22ybn3bPwx9TF4jkdYw
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:27:05.671745
---

# 什么是 ICMP（互联网控制消息协议）？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa1e0pygdby4ELXPTibLA61Vy3zSMeKDCqKM6RWf8Z2qwvS8YOlYhFBQPvneD7LzPPQaibFuEBVpPLKiaicVwVr0hicnCbSBAU3KhyG0/0?wx_fmt=jpeg)

# 什么是 ICMP（互联网控制消息协议）？

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

分类：网络协议 / DDoS 攻击     标签：ICMP  Ping  Traceroute  网络层  DDoS

摘要：互联网控制消息协议（ICMP）是网络设备用来诊断网络通信问题的网络层协议。本文介绍 ICMP 的用途、工作原理、数据包结构，以及它在 DDoS 攻击中如何被利用。

|  |
| --- |
| 阅读本文后，你将能够：  定义 ICMP；说明 ping 与 traceroute 的工作方式；理解 ICMP 协议如何被用于 DDoS 攻击。 |

一、什么是互联网控制消息协议（ICMP）？

互联网控制消息协议（Internet Control Message Protocol，简称 ICMP）是一种由网络设备用来诊断网络通信问题的网络层协议。ICMP 主要用于判断数据是否能够及时到达其预定目的地。它通常运行在路由器等网络设备上。

ICMP 对于错误报告和测试至关重要，但它同样可能被用于分布式拒绝服务（DDoS）攻击。

二、ICMP 有什么用途？

1. 错误报告

ICMP 的主要用途是错误报告。当两台设备通过互联网连接时，若有任何数据未能到达其预定目的地，ICMP 会生成错误消息，反馈给发送方设备。

例如，如果某个数据包对于路由器来说过大，路由器会丢弃该数据包，并向数据的原始来源发送一条 ICMP 消息。

2. 网络诊断：ping 与 traceroute

ICMP 的次要用途是执行网络诊断。常用的终端工具 traceroute 和 ping 都通过 ICMP 运行。

traceroute 用于显示两台互联网设备之间的路由路径——即请求在到达目的地之前必须经过的、由相连路由器组成的实际物理路径。从一个路由器到另一个路由器的过程被称为一跳（hop），traceroute 还会报告沿途每一跳所需的时间，这对于确定网络延迟的来源非常有用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3K9d3mhcvksrdNBZJXULDl3ULOYkr2zOryjJibREEmNGr4aQcnGdD5TZhNXqeMdiaNf9iaLE7uicyhiaMReq8xHhWric1GFSY4QQbmE/640?wx_fmt=png)

图 1　traceroute 逐跳追踪两台设备之间的路由路径

ping 是 traceroute 的简化版本。ping 会测试两台设备之间连接的速度，并精确报告一个数据包到达目的地并返回发送方设备所需的时间。虽然 ping 不提供关于路由或跳数的数据，但它仍是衡量两台设备之间延迟（latency）的非常有用的指标。执行 ping 时，通常使用 ICMP 的回显请求（echo-request）和回显应答（echo-reply）消息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1lvuq3icRboZywfo5jf19jtVUpIJxLdYUCMxUSEMF1Qw3dFQr5EIRneQYAADwoGfG29Z8FWyYvB2eqZxs1C3iarOWQ2bqZxl9k4/640?wx_fmt=png)

图 2　ping 通过回显请求与回显应答测量往返延迟

|  |
| --- |
| ⚠ 安全提示  遗憾的是，网络攻击可能利用这一过程，制造出诸如 ICMP 洪水攻击 和 死亡之 Ping（ping of death） 之类的破坏手段。 |

三、ICMP 如何工作？

与互联网协议（IP）不同，ICMP 不与诸如 TCP 或 UDP 之类的传输层协议相关联。这使得 ICMP 成为一种无连接协议：一台设备在发送 ICMP 消息之前，无需与另一台设备建立连接。

正常的 IP 流量使用 TCP 发送，这意味着任何两台交换数据的设备都会先进行 TCP 握手，以确保双方都已准备好接收数据。而 ICMP 不会以这种方式建立连接，ICMP 协议也不允许针对设备上的特定端口。

四、什么是 ICMP 数据包？

ICMP 数据包是使用 ICMP 协议的数据包。ICMP 数据包在普通的 IP 头部之后包含一个 ICMP 头部。当路由器或服务器需要发送错误消息时，ICMP 数据包的正文（数据段）始终包含引发该错误的数据包的 IP 头部副本。

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa3jvQVbBoxTz0pRJSXEpLy6K87vzUhXH7vnxGnwWxZqrvfUhwzqUlibeKPBEncWy7LbNwJqZEibib4bHTBKb2So0Ga5fXJoL6Unrk/640?wx_fmt=png)

图 3　ICMP 数据包结构：IP 头部 + ICMP 头部 + 数据段

五、ICMP 如何被用于 DDoS 攻击？

1. ICMP 洪水攻击

Ping 洪水（ping flood）或 ICMP 洪水，是指攻击者试图用 ICMP 回显请求数据包淹没目标设备。目标必须处理并回应每一个数据包，从而消耗其计算资源，直到合法用户无法获得服务。

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa3BtUvdOs6P8YZVzUbsEmM3h6b0c9a08hkIv9xw0JasEokCxtRtCwy2TtmF2liaC55VsLtAvdpjTic51GY6VpHlU34HVCOHpPcr8/640?wx_fmt=png)

图 4　ICMP 洪水：大量回显请求与回显应答

2. 死亡之 Ping（Ping of Death）

死亡之 Ping 攻击，是指攻击者向目标机器发送一个大于数据包最大允许尺寸的 ping，导致机器冻结或崩溃。数据包在到达目标的途中会被分片，但当目标将其重组为原始的、超过最大尺寸的大小时，数据包的尺寸会引发缓冲区溢出。

|  |
| --- |
| 📌 历史背景  死亡之 Ping 攻击如今在很大程度上已成为历史，不过较老旧的网络设备仍可能易受其影响。 |

3. Smurf 攻击

在 Smurf 攻击中，攻击者发送一个带有伪造源 IP 地址的 ICMP 数据包。网络设备会回应该数据包，将应答发送到被伪造的 IP，从而用不需要的 ICMP 数据包淹没受害者。与死亡之 Ping 一样，如今 Smurf 攻击只有在使用老旧设备时才有可能实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3USdmgwiaTEqrVSa8Pkib3TQCtcCbry5e77fvia5quibNkwqY0aAAibat31qVOgYmXFoPX1usT2icRbpBZ5dtJB935ZGI1OGGicBj9Rk/640?wx_fmt=png)

图 5　Smurf 攻击：伪造源 IP，使应答流量涌向受害者

ICMP 并非三层（L3）DDoS 攻击中使用的唯一网络层协议。例如，攻击者过去也曾使用 GRE 数据包。

通常，网络层 DDoS 攻击的目标是网络设备和基础设施，这与以 Web 资产为目标的应用层 DDoS 攻击不同。

六、小结

●ICMP 是一种网络层协议，主要用于错误报告和网络诊断。

●ping 与 traceroute 都基于 ICMP：前者测量往返延迟，后者逐跳追踪路由路径。

●ICMP 是无连接协议，不依赖 TCP/UDP，也不针对特定端口。

●ICMP 可被滥用于 ICMP 洪水、死亡之 Ping、Smurf 等 DDoS 攻击；后两者如今主要影响老旧设备。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa1SibU9u3OqdKX5WMO8J5SW6AUgJiahD4yxRdHuUW7nZVUD4eYrgoUNEZgC2A10nia8rXz2WvL7rhLp9FnPicITMLxdBwKtwvMkjIk/0?wx_fmt=png)

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