---
title: 一次研究如何获得wifi密码的过程
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589548&idx=2&sn=8ba181b790457bb4caa3c3ede284bd45&chksm=b18c29e686fba0f0f6499b70459308c27bbcaae3132c8647a40fecdb13e5428ffdfcb48b80e1&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-14
fetch_date: 2025-10-06T20:36:26.677111
---

# 一次研究如何获得wifi密码的过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbOsJyMbUB6QyakOkqKsTF4at4sklGt7zSVXPuHKJn9lTdof4icXfFbEg/0?wx_fmt=jpeg)

# 一次研究如何获得wifi密码的过程

Nbc

看雪学苑

研究这个的契机是有次跟我的学长@ZIKH26聊智能家居iot安全的时候说的“那不连接wifi怎么去入侵智能家居呢”，然后就引申出这个了，描述概括下核心内容大概是这样。

```
任何设备都可以接收到路由器的信号，因为本身这个信号就是广播的，否则你识别不到路由器怎么去连接。只是要是想通过wifi去上网，就需要输入验证密码，因为数据是加密的。现在我通过可以发射信号的网卡，去向路由器发送一个特别的帧，让路由器以为与设备断卡连接了，而一般断开连接之后会重新连接，我们就可以捕获这个连接的握手包，然后在本地进行破解出密码
```

我一听这个牛掰啊：首先，这样就可以破解任意密码了(错误的，弱口令且字典需要足够强大，后续会说明)

其次，这可以直接让区域内设备都上不了网了，这破坏性多大，直接让邻居上不了网(: 当时学长玩这个的时候用的是aircrack-ng*（https://github.com/aircrack-ng/aircrack-ng）*这个工具，说一套下来操作有很多，可以尝试下怎么一键梭哈，在寒假就一起研究了一下原理等的内容。

```
一

抓包过程
```

直接get到学长的无线网卡：

![image-20250127180609755](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbxTpGXUADyEvLQHwbRWhQ4v4X2FCq18fHK7zngSKUiaxCKRvxmNaL8Xw/640?wx_fmt=png&from=appmsg)

先用现成的工具体验一下：

![image-20250124144350637](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYb1PKJ3FHlZ5GqBe10jOZMmoDNjqB0KOqhUp5PmLNdClod5zFEcicSic8Q/640?wx_fmt=png&from=appmsg)

![image-20250124143650486](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbTuPRyZbqmDicLEE8z4EbPgWWxOT2fXBAmRbYOp40ePVzKanSnoACicqA/640?wx_fmt=png&from=appmsg)

工具的具体操作过程这里就不写了，网上有很多文章怎么操作，这里探究怎么写出一键梭哈脚本。

在用工具进行操作时，过程大概是这样的：`启动网卡为监听模式->监听当前环境AP(路由器)->选定AP监听该设备下的连接设备(STA)->发送断开帧->捕获到握手包->破解。`

这时候就存在疑问点：

1.怎么抓包？

2.抓什么包？

3.发送的是什么？

4.发送完之后抓到什么包才能破解出密码呢？

打开wireshark选定我们的无线网卡：

![image-20250124144437747](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbNtNprYib3RK24MribUIKV12QtRia2LeUQSEICIkmib9ylCrU8TmLQI7oZQ/640?wx_fmt=png&from=appmsg)

看到就是一堆包，也看不懂也不知道哪些包是我需要的，所以就要去研究一下原理了。

### Scapy

首先是怎么抓包，可以使用Scapy来操作。

**Scapy**是一个用于**网络数据包处理**和**网络攻击模拟**的强大 Python 库。它允许用户轻松地创建、发送、捕获、解析和修改网络数据包。。

具体可以看文档

Introduction — Scapy 2.6.1 documentation*（https://scapy.readthedocs.io/en/latest/introduction.html）*

我们所使用的模块主要在

scapy.layers.dot11 — Scapy 2.6.1 documentation*（https://scapy.readthedocs.io/en/latest/api/scapy.layers.dot11.html）*

###

### 802.11协议

#### 802.11协议简介

IEEE 802协议簇是指IEEE标准中关于局域网（LAN）和城域网（MAN）的一系列标准。IEEE 802中定义的服务和协议限定在OSI七层网络模型的最低两层，即数据链路层和物理层。实际上，IEEE802又将OSI的数据链路层分成了两个子层，逻辑链路控制层（LLC）和媒介访问控制层（MAC）。IEEE802协议簇由IEEE802标准委员会维护。其中最广泛应用的协议有以太网（802.3）和WLAN（802.11）。每一个工作组专注一个方向，每个工作组由数字编号，比如目前从802.1编到了802.24。

![image-20250124151955891](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbmTIGKHtSPR3dutRE7f0hEicTic4tX9PCzQAkbLM32vPynC36vHGU7jww/640?wx_fmt=png&from=appmsg)

所以802.11协议是IEEE802标准委员会下属的无线局域网工作组制定的无线局域网标准。

详细内容可以看IEEE Xplore Full-Text PDF*（https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9363693）*

#### 802.11 MAC帧结构

802.11 MAC帧格式如图

![image-20250124153816527](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbLHZuGVswbjbuNLIddib9Vz3BkuDEvAQiavlnPiaAOc0zXrp4uiauPRtzPg/640?wx_fmt=png&from=appmsg)

每个MAC帧都包含以下几部分：

1.一个MAC帧头

2.一个可变长度的帧体，包含特定于帧类型或子类型的信息

3.一个帧校验序列，简写为FCS，包含一个32bit的CRC

主要来看一下帧控制字段

![image-20250124155841022](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbL7RL3d4CmUSaHPKRgoibbcLmfLwnGtibrIhmzKEMHrjHM8x8BXQD1m4Q/640?wx_fmt=png&from=appmsg)

◆Protocol Version：帧使用的MAC版本，目前仅支持一个版本，编号为0。

◆Type/Subtype：标识帧类型，包括数据帧、控制帧和管理帧。

> 数据帧：负责传输数据报文，包括一种帧主体部分为空的特殊报文（Null帧）。STA可以通过Null帧通知AP自身省电状态的改变。
>
> 控制帧：协助数据帧的传输，负责无线信道的清空、信道的获取等，还用于接收数据时的确认。常用的控制帧有：
>
> ◆ACK：接收端接收报文后，需要回应ACK帧向发送端确认接收到了此报文。
>
> ◆请求发送RTS（Request To Send）/允许发送CTS（Clear To Send）：提供一种用来减少由隐藏节点问题所造成冲突的机制。发送端向接收端发送数据之前先发送RTS帧，接收端收到后回应CTS帧。通过这种机制来清空无线信道，使发送端获得发送数据的媒介控制权。
>
> 管理帧：负责对无线网络的管理，包括网络信息通告、加入或退出无线网络，射频管理等。常用的管理帧有：
>
> ◆**Beacon：信标帧，AP周期性地宣告无线网络的存在以及支持的各类无线参数（例如，SSID、支持的速率和认证类型等）。**
>
> ◆Association Request/Response：关联请求/应答帧，当STA试图加入到某个无线网络时，STA会向AP发送关联请求帧。AP收到关联请求帧后，会回复应答帧接受或拒绝STA的关联请求。
>
> ◆Disassociation：去关联帧，STA可以发送Disassociation帧解除和AP的关联。
>
> ◆Authentication Request/Response：认证请求/应答帧，STA和AP进行链路认证时使用，用于无线身份验证。
>
> ◆**Deauthentication：去认证帧，STA可以发送Deauthentication帧解除和AP的链路认证。**
>
> ◆Probe Request/Response：探测请求/应答帧，STA或AP都可以发送探测帧来探测周围存在的无线网络，接收到该报文的AP或STA需回应Probe Response，Probe Response帧中基本包含了Beacon帧的所有参数。

◆To DS/From DS：标识帧是否来自和去往一个分布式系统（Distribution System，其实就是指AP）。例如都为1，表示AP到AP之间的帧。

◆More Frag：表示是否有后续分片传送。

◆Retry：表示帧是否重传，用来协助接收端排除重复帧。

◆Pwr Mgmt：表示STA发送完成当前帧序列后将要进入的模式，Active或Sleep。

◆More Data：表示AP向省电状态的STA传送缓存报文。

◆Protected Frame：表示当前帧是否已经被加密。

◆+HTC：为控制帧提供额外的信息支持

详尽在第九章节IEEE Xplore Full-Text PDF*（https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9363693）*

关于地址Address*n*字段：表示MAC地址。4个Address位填法不固定，需要和Frame Control字段中的To DS/From DS位结合来确定。例如，帧从一个STA发往AP，与从AP发往STA，4个Address字段的填法是不一样的。

Address n字段填写规则

| To DS | From DS | Address 1 | Address 2 | Address 3 | Address 4 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 目的地址 | 源地址 | BSSID | 未使用 | 管理帧与控制帧。例如，AP发送的Beacon帧。 |
| 0 | 1 | 目的地址 | BSSID | 源地址 | 未使用 | 如图中的AP1向STA1发送的帧。 |
| 1 | 0 | BSSID | 源地址 | 目的地址 | 未使用 | 如图中的STA2向AP1发送的帧。 |
| 1 | 1 | 目的AP的BSSID | 源AP的BSSID | 目的地址 | 源地址 | 如图中的AP1向AP2发送的帧。 |

![image-20250124165457518](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbNCZCOSsXQdouicuuNxclsaeEp34y8bkBDeWEA00xxIicQiceLYHqTXhLA/640?wx_fmt=png&from=appmsg)

#### 小结

到这里我们就可以有个大概的思路了，如果我们想要知道当前环境下有哪些AP的话，就要捕捉到Beacon帧，因为这个帧是AP用于广播其存在和网络信息的方式。而断开就通过发送Deauthentication帧来中断STA和AP的连接。

这里会存在一个疑问，如何去获得STA的MAC地址呢？我是通过捕获AP发送的Beacon帧的目的地址来获取的，也就是add1。因为AP的Beacon帧是广播的，所以目的地址也会存在"ff:ff:ff:ff:ff:ff"，过滤掉就行了。

![image-20250124184449132](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYb3cmg6K7QgtAma7PoZ7nibZSmWchic4Xb8uaKfWtaDe5tTRccsGddztrw/640?wx_fmt=png&from=appmsg)

现在我们怎么抓包，抓什么包，发送什么都搞清楚了，那破解关键抓的包是什么呢？

### WLAN中的身份认证和访问控制机制

我想既然有密码这里肯定是跟无限网络中的认证有关的，查阅一番后发现了802.1X

#### 802.1X认证

##### 802.1X简介

802.1X认证系统使用可扩展认证协议EAP（Extensible Authentication Protocol）来实现客户端、设备端和认证服务器之间的信息交互。EAP协议可以运行在各种底层，包括数据链路层和上层协议（如UDP、TCP等），而不需要IP地址。因此使用EAP协议的802.1X认证具有良好的灵活性。

◆在客户端与设备端之间，EAP协议报文使用EAPoL（EAP over LANs）封装格式，直接承载于LAN环境中。

◆在设备端与认证服务器之间，用户可以根据客户端支持情况和网络安全要求来决定采用的认证方式。

* EAP终结(解析和处理)方式中，EAP报文在设备端终结并重新封装到RADIUS报文中，利用标准RADIUS协议完成认证、授权和计费。
* EAP中继方式中，EAP报文被直接封装到RADIUS报文中（EAP over RADIUS，简称为EAPoR），以便穿越复杂的网络到达认证服务器。

##### 认证过程

EAP数据首先被封装在EAPOL帧中，传输于申请者（Supplicant）和验证者（Authenticator）之间。随后又封装在RADIUS或Diameter，传输于验证者和验证服务器（Authentication server）之间。

![image-20250124180256281](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYb3S3oEAOe5OC55ZHZg1bmaDVPsV6MfVoribxJd5IDKajlapQL3iaJciaKg/640?wx_fmt=png&from=appmsg)

####

#### 安全策略

到这里要提一下WLAN的安全策略

WLAN安全提供了WEP、WPA、WPA2和WAPI四种安全策略机制。每种安全策略体现了一整套安全机制，包括无线链路建立时的链路认证方式，无线用户上线时的用户接入认证方式和无线用户传输数据业务时的数据加密方式。

现在常用的机制就是WPA/WPA2，在手机中就可以看到：

![image-20250124194715926](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYb6QewoL6mknPrzylAw6NmIe41Iia6ibE12IDPdSdSgSeAGvUiahV9Vqe6g/640?wx_fmt=png&from=appmsg)

#####

##### WPA/WPA2简介

由于WEP共享密钥认证采用的是基于RC4对称流的加密算法，需要预先配置相同的静态密钥，无论从加密机制还是从加密算法本身，都很容易受到安全威胁。为了解决这个问题，在802.11i标准没有正式推出安全性更高的安全策略之前，Wi-Fi联盟推出了针对WEP改良的WPA。WPA的核心加密算法还是采用RC4，在WEP基础上提出了临时密钥完整性协议TKIP（Temporal Key Integrity Protocol）加密算法，采用了802.1X的身份验证框架，支持EAP-PEAP、EAP-TLS等认证方式。

随后802.11i安全标准组织又推出WPA2，区别于WPA，WPA2采用安全性更高的区块密码锁链-信息真实性检查码协议CCMP（Counter Mode with CBC-MAC Protocol）加密算法。

为了实现更好的兼容性，在目前的实现中，WPA和WPA2都可以使用802.1X的接入认证、TKIP或CCMP的加密算法，他们之间的不同主要表现在协议报文格式上，在安全性上几乎没有差别。

##### 密钥协商

在802.11i里定义了两种密钥层次模型，一种是成对密钥层次结构，主要用来保护STA与AP之间往来的数据；一种是群组密钥层次结构，主要用来描述STA与AP之间的广播或组播数据。

密钥协商阶段是根据接入认证生成的成对主钥PMK（Pairwise Master Key）产生成对临时密钥PTK（Pairwise Transient Key）和群组临时密钥GTK（Group Temporal Key）。PTK用来加密单播报文，GTK用来加密组播和广播无线报文。

◆针对802.1X接入认证，生成PMK的流程图如图所示。

![image-20250124183907817](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbOCz2ic3UWNZGMpEfic8WYHw6n3E1vwK2CcSe4U7X48lpibibpgxqZ8NX4g/640?wx_fmt=png&from=appmsg)

◆针对PSK认证，根据设置预共享密钥的方式不同（通过命令行可以选择设置预共享密钥的方式），生成的PMK方式也不同：

* 如果设置的预共享密钥是十六进制，则预共享密钥即是PMK；
* 如果设置的预共享密钥是字符串，则PMK是利用预共享密钥和SSID通过哈希算法计算出来的。

密钥协商包括单播密钥协商和组播密钥协商过程。

###### 单播密钥协商过程

######

密钥协商过程也叫做四次握手过程，是通过EAPOL-Key报文进行信息交互的，如图所示。

![image-20250124184013257](https:/...