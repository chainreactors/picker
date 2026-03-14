---
title: 汽车网络信息安全-通信安全方案
url: https://mp.weixin.qq.com/s/rNLLqrsfWmG4simRoYqFRg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:05:38.327433
---

# 汽车网络信息安全-通信安全方案

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAHx8rKDicn6eiatRicbphfa3qnIVzVj3Yap6f1sjyFa9VnYGTY1N88Is0LWDShIibJ0Ak5XZ2ribJTY0Zbk3npQ5hBbeiabXASmVpibk/0?wx_fmt=jpeg)

# 汽车网络信息安全-通信安全方案

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDpvdTdBRjiczomXoHVGoUN5dQSQrGJEbM9aQpmx9kcX43aibdRzt4QqqUVTXhlKPDiaggLqK4ibaFBb45y5yXlZxWzbdQCUn9bfjI/640?wx_fmt=png&from=appmsg)

**01**

**车载以太网**

首先先了解一下车载以太网：

我们常用的以太网和车载以太网主要是在物理层不同，基本架构依然是MAC +PHY芯片+传输链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB8icMRiaR9kGbV8MhiaZ3TibDyBI8L9iarQ97e0ibrsbTuFQjk6QqxgdK26QudWSCM1vO0TEEcG8chCLPho57KHR0vRusLLHl6cNULI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC0fe9tsZN2CazvEVtjT2JoE5pJwpIJpN8krHTfREPxengbIB1J28fHkviafE5EyhFMwRNHWroiafTJxVuMMSv4Ug82Nv63YD5iaQ/640?wx_fmt=png&from=appmsg)

车载以太网构成了一个相对封闭的网络环境，其复杂性远不及互联网。由于车内通信参与者固定，IP地址和端口可提前设定，从而省去了DHCP协议动态分配地址的繁琐。同时，整车网络内的虚拟子网也已预先划分。

以下是车载以太网网络中的几种关键角色：

1. Switch（交换机）：负责在特定VLAN内，基于层2地址（即MAC地址）转发以太网帧。
2. Router （路由器）：在VLAN间基于层3地址（即IP地址）转发以太网帧。
3. ECU节点（无转发功能）：负责验证接收的以太网帧合法性，主要依据通信矩阵定义和预定义通信协议。

为避免大量无关信息在车内网络中泛滥，我们常利用VLAN将网络按功能域划分为多个虚拟子网，如娱乐、驾驶辅助、舒适等系统。当需要跨VLAN通信时，则借助上述的Router角色。

**02**

**SecOC**

安全车载通信（Secure Onboard Communication，简称SecOC）主要的作用就是为汽车嵌入式网络总线上的数据传输提供身份验证和防止重放攻击的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAO9k4oP7HqZYu415KbsDAHN6ZVXyYOzb3CTjQ81DfDL76fQ4SFPoXlVrbicUkcTcaCQUzmeflk6mt3aibN7cdbv4Zqxicdncd5Tk/640?wx_fmt=png&from=appmsg)

* Protects integrity on PDU level.
* Symmetric key used for transmission and reception

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB4jB5NFGEmguuFhJ4QVRTnz6IblyRMmcQuuTTAhs6htxfjTsDsM8G8drf0mBWG1kPypU2KtufDHodcbmHrcRnw20yHrfJOibyA/640?wx_fmt=png&from=appmsg)

**03**

**TLS**

TLS 属于工作在传输层的协议，它介于传输层底层协议和上层应用协议之间。而以太网的传输层主要有两大底层协议：TCP （Transmission Control Protocol）和UDP（UserDatagram Protocol）。二者各有特点，互为补充。不管在传统互联网上，还是车载以太网上，两者都是常见的传输层底层协议。不同的传输层底层协议实际上对应着不同的传输层安全保护协议，采用TCP 传输的，就用TLS 保护。采用UDP 传输的，就用DTLS 保护。DTLS 的全称是Datagram Transport Layer Security，比TLS 多出来的“D” ，指的就是UDP 中的“D” 。TLS 和DTLS 各有不同的版本，目前主流支持的还是1.2 和1.3版本。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD8kc0uYx7pxv2EAZbiajB7qWMgIhhQuRyOKribV236IR7aGhUuIL7iat5qGiaEhCO4nqicLZftaMAicicwt17TuWeM5iaPZC6TGdxZgNM/640?wx_fmt=png&from=appmsg)

* Protects integrity and confidentiality on TCP/UDP layer.
* Certificate-based or with pre-shared keys.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA2ToCXxfsAyfkyEibZyQOVNp0fXTtxReseqWLjWoXcuESGN7mXQNYb52IMIy1qV4dGohQcuHuia9PyUtLWLwVicV1zIibYJlsiblnY/640?wx_fmt=png&from=appmsg)

TLS支持应用程序到应用程序（端口到端口）的安全性。TLS能够确保在具有唯一端口号的两个ECU上运行的两个应用程序之间的消息的真实性、机密性和完整性。

**04**

**IPsec**

IPSec是网络层协议，一种使用IP协议保护数据通信安全的方法，能够提供端到端（IP到IP）安全性。

IPSec能够确保具有唯一IP地址的两个ECU之间消息的真实性、机密性和完整性。虚拟专用网络(VPN)使用IPSec协议。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAqTKc3jyPGoQZpBtPmvgicZ5X2lQOBHwVDd0dDOiaq7okfLI77B1RZh3XibibIWJPU6zwCIFyXHVziajxMRia50w6xu6IY9SNNA1icxc/640?wx_fmt=png&from=appmsg)

* Protects integrity and confidentiality on IP layer.
* Certificate-based or with pre-shared keys.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBo4k9KmPECGdVicE6shHtxaBnywMr8p29p8Mic7TSWv2zRHkD6yxtl64FTyO8vg0EXDYDE6v7joicKGficlJOEo4uYibkHaUX3BR48/640?wx_fmt=png&from=appmsg)

IPsec 可以保护 IP 上的所有通信，并支持两种模式（隧道和传输）下的两种协议（AH 和 ESP）。

**05**

**MACsec**

MACsec，全称Media Access Control security，被定义为IEEE 标准 802.1AE，它专注于以太网连接设备之间的点对点数据安全性。与传统的网络安全协议不同，MACsec工作在OSI模型的第二层，即数据链路层，这一层负责在网段上的节点之间传输数据。这种低层次的安全保护确保了数据在传输过程中的机密性和完整性，为整个网络系统提供了坚实的基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCq23RJWllIArw9Uf7cvYTTvzeJ42VYR7AC7Xk7GK2elOfB54KiaFACUzurxYsPxXFdyejUwsJOxEvgGFGJKvyBS7ccDV9nicKLQ/640?wx_fmt=png&from=appmsg)

* Protects integrity and confidentiality on Ethernet layer.
* Certificate-based or with pre-shared keys.
* Hop-by-hop instead of end-to-end.

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAYehNLjZ8WcQWAhKR12zFTxUSAvGJe8XxULChIARiblAzeic5Bojb4O9BYaeyOVf0ey4hzQBvAoKsfriaAhSBETbXp7l0vU5ViaoQ/640?wx_fmt=png&from=appmsg)

Macsec 是一种非常适合于以太网的Hop by Hop 的链路层安全协议，它实现如下三个功能：

1. 报文加密：通过加密算法和密钥，将明文变成乱码的密文，即使被窃听也难以解密。
2. 防重放攻击：防止黑客截获目的主机接收的报文，再次发送给目的主机，达到欺骗目的主机的目的，比如身份认证
3. 防篡改：防止黑客随意篡改原始报文内容，实现不可告人的目的。

Macsec 的实现分两种模式：

1. 面向主机模式：用于终端接入网络的第一跳保护。
2. 面向设备模式：用户设备之间互联链路的保护。

MACsec 作用于：主机到交换机连接和交换机到交换机连接上

MACsec的特性之一是它保护协议栈较低层（以太网）中的数据通信。然而，仅靠MACsec并不能保证端到端的安全。反对为车载通信部署MACsec的几个原因是成本较高、性能下降，并且很少有提供商在其SoC中提供MACsec功能。

来源：CSDN@爱思考的发菜\_汽车网络信息安全

https://blog.csdn.net/2301\_76563067/article/details/144351910?spm=1001.2014.3001.5502

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&s...