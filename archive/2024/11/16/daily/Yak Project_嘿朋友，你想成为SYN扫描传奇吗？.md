---
title: 嘿朋友，你想成为SYN扫描传奇吗？
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247524976&idx=1&sn=fd762032a5437797410068fbccab08ca&chksm=c2d11ed4f5a697c2df5970ef95c9005903b06394b87835913e45d9469d7de155b470191887e4&scene=58&subscene=0#rd
source: Yak Project
date: 2024-11-16
fetch_date: 2025-10-06T19:18:35.958488
---

# 嘿朋友，你想成为SYN扫描传奇吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0UYQWvz2Adm4xIGetlaYwaIHJuvJLzlPjPoWaJYxsfCqY4o7aeq9Vlw/0?wx_fmt=jpeg)

# 嘿朋友，你想成为SYN扫描传奇吗？

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)周五周五，敲锣打鼓！

周五周五，脱胎换骨！

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0DcooDj7qwXrqUWdTn7siaY7nqzsvOBeiaaoyFJKTThtEcqXH7SBNmugg/640?wx_fmt=png&from=appmsg)

等等，我知道你很急但你先别急

SYN扫描原理 奇妙至极~

朋友，想成为SYN扫描传奇吗？

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0VNmBjcyLt7PUV08libAc8EmnhuFSzlnIiaJThN911S7468pdssPD8hgw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hnaBOeMYPPSp3R6xO58xbFxrEStgljbvaX7N5718pp0OQXoNDcK09EUw/640?wx_fmt=png&from=appmsg)

**发送SYN包：**扫描器向目标端口发送一个SYN（同步序列编号）数据包，它正试图建立一个正常的连接。

**等待响应：**

* 如果收到SYN-ACK（同步确认）响应，这意味着端口是开放的，因为目标已准备好完成连接。
* 如果收到RST（重置）响应，这意味着端口是关闭的，目标没有等待任何连接在该端口上。
* 如果没有响应，可能端口被防火墙过滤或丢弃了SYN包。

**不完成握手：**在收到SYN-ACK后，扫描器通常会发送一个RST包来中断连接过程，因此不会建立一个完整的TCP连接。

使用 Wireshark 查看对IP 192.167.3.3的80端口进行SYN 扫描的数据包如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdWNlBPmFibay3nmrFWt2ajAbqqhculSAQloNiaYgRLHl79qWIQTqjF3GaxiaRCfx0oUkDVzvD1ibyW2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hnvAhAO4cicg4uyYWHQ7qXQj7eIL9QgK9ibYSlpGB3PaG472c7iaFnGeVSA/640?wx_fmt=png&from=appmsg)

要构建一个完整的数据包，需要按照协议栈的层次结构依次封装这些层。

例如，一个完整的TCP/IP数据包会包括：

1. 以太网帧头（包括源和目的MAC地址）
2. IP头（包括源和目的IP地址，以及其他IP相关设置）
3. TCP头（包括端口号，序列号，确认号等）
4. 数据负载（如果有的话）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hnf6jBwfjOuYhEwK2EYjwz4VIZrM0dEqO28G6ibnFTCHQ7Fic6GeX5Pfibg/640?wx_fmt=png&from=appmsg)

对于 IP 和 TCP 头的构建，比较简单，只需要填写，源/目的IP(端口)，设置 TCP Flags，以及一些 Option。

部分代码如下：

```
// IPv4opts = append(opts, pcapx.WithIPv4_Flags(layers.IPv4DontFragment))opts = append(opts, pcapx.WithIPv4_Version(4))opts = append(opts, pcapx.WithIPv4_NextProtocol(layers.IPProtocolTCP))opts = append(opts, pcapx.WithIPv4_TTL(64))opts = append(opts, pcapx.WithIPv4_ID(40000+rand.Intn(10000)))opts = append(opts, pcapx.WithIPv4_SrcIP(srcIP))opts = append(opts, pcapx.WithIPv4_DstIP(dstIP)) // 要扫描的IPopts = append(opts, pcapx.WithIPv4_Option(nil, nil))
// TCPopts = append(opts,    pcapx.WithTCP_SrcPort(srcPort),    pcapx.WithTCP_DstPort(port),    // 要扫描的端口    pcapx.WithTCP_Flags(pcapx.TCP_FLAG_SYN),    pcapx.WithTCP_Window(1024),    pcapx.WithTCP_Seq(500000+rand.Intn(10000)),)
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hn5KLH4F1qfvHhEicon8UkBQ2m3xOLZhF34mJVN9GKfoPEQPfwLHs89GQ/640?wx_fmt=png&from=appmsg)

以太网帧头指的是在以太网层（或称为数据链路层）中，每个数据包开头的部分，用于定义数据包的一些基本属性。

以太网帧头通常包括以下几个关键部分：

1. **目标MAC地址（Destination MAC Address）：**接收数据包的设备的硬件地址。
2. **源MAC地址（Source MAC Address）：**发送数据包的设备的硬件地址。
3. **类型/长度字段（Type/Length Field）：**字段可以是两种形式之一：

* **类型（Type）****：**表示随后数据包内容的协议类型（如IPv4, IPv6, ARP等），通常使用2字节来表示。
* **长度（Length）****：**在某些协议（如IEEE 802.3）中，这个字段表示数据字段的长度。

其中，源MAC地址就相当于是本机发包网卡的MAC地址，目的MAC地址则需要我们通过其他方法获取，因此在构建一个完整的数据包前，我们还需要一些前置工作。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hn0eiaoTLuSzuaSJynicKpvxpk06wR2NU0u5YlOW1Zko5bhxbEUjSjkvtQ/640?wx_fmt=png&from=appmsg)

路由表包含了一系列的路由条目，这些条目指导数据包如何从一个网络传输到另一个网络。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hnPicicRkAKiatmibUlKzDUjAv6u3vD7Sx9kHCSUfia8TuE3a6l1qwXNWiaiaXw/640?wx_fmt=png&from=appmsg)

本地子网检测：

* 当数据包的目的IP地址与源IP地址处于同一子网时，即目的地址与源地址的网络部分相同（根据子网掩码计算），这被认为是内网路由。

例如，如果源IP是192.168.1.100，子网掩码是255.255.255.0，目的IP是192.168.1.101，那么这两个IP都在192.168.1.0/24网络内。

对于同一个子网掩码地址内的两个内网IP通信相对简单，因为它们位于同一个局域网（LAN）内。这种情况下，数据包通常不需要经过路由器进行路由，而是直接通过交换机或者集线器在内部网络中传输。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hngzia7hab1I4yRNDor2QibbibMtvKRIIzbfzAT7ml64jZRqO6nW86nfnAg/640?wx_fmt=png&from=appmsg)

**目的IP非本地子网：**

* 当数据包的目的IP地址不在同一子网时，设备必须通过一个或多个路由器发送数据包到目的地。
* 例如，如果源IP是192.168.1.100，目的IP是8.8.8.8，由于8.8.8.8不在本地网络，数据包需要被路由到外部网络。

**默认网关：**

* 设备配置有默认网关（通常是本地网络的路由器），所有非本地目的地的数据包都会发送到这个网关。
* 网关检查其路由表，决定如何进一步转发数据包。

```
IPv4 路由表===========================================================================活动路由:网络目标        网络掩码          网关       接口   跃点数          0.0.0.0          0.0.0.0      192.168.3.1      192.168.3.3     30        127.0.0.0        255.0.0.0            在链路上         127.0.0.1    331        127.0.0.1  255.255.255.255            在链路上         127.0.0.1    331  127.255.255.255  255.255.255.255            在链路上         127.0.0.1    331     172.22.160.0    255.255.240.0            在链路上      172.22.160.1   5256     172.22.160.1  255.255.255.255            在链路上      172.22.160.1   5256   172.22.175.255  255.255.255.255            在链路上      172.22.160.1   5256      172.25.16.0    255.255.240.0            在链路上       172.25.16.1   5256      172.25.16.1  255.255.255.255            在链路上       172.25.16.1   5256    172.25.31.255  255.255.255.255            在链路上       172.25.16.1   5256      192.168.3.0    255.255.255.0            在链路上       192.168.3.3    286      192.168.3.3  255.255.255.255            在链路上       192.168.3.3    286    192.168.3.255  255.255.255.255            在链路上       192.168.3.3    286        224.0.0.0        240.0.0.0            在链路上         127.0.0.1    331        224.0.0.0        240.0.0.0            在链路上       192.168.3.3    286        224.0.0.0        240.0.0.0            在链路上       172.25.16.1   5256        224.0.0.0        240.0.0.0            在链路上      172.22.160.1   5256  255.255.255.255  255.255.255.255            在链路上         127.0.0.1    331  255.255.255.255  255.255.255.255            在链路上       192.168.3.3    286  255.255.255.255  255.255.255.255            在链路上       172.25.16.1   5256  255.255.255.255  255.255.255.255            在链路上      172.22.160.1   5256===========================================================================
```

比如，我要扫描 192.168.3.100 ，根据路由表，这个地址在192.168.3.0/24网络内，数据包将直接从接口192.168.3.3发送，路由表中的“在链路上”的条目表明数据包将直接在本地网络接口上发送，不经过任何路由器。

又比如，我要扫描  8.8.8.8，根据路由表，该地址不属于本地定义的任何子网。路由表中的默认路由（0.0.0.0/0.0.0.0，网关192.168.3.1）将被用来处理这种情况。这意味着所有不属于本地子网的IP地址都将数据包发送到网关192.168.3.1。后续可能是根据路由器中的路由表，决定下一跳的地址。

通过路由表，我们知道了两个最关键的信息：

1. 内网扫描时，目标IP 的MAC 地址通过 ARP 协议请求目标 IP 获取。
2. 外网扫描时，目标IP 的MAC 地址通过 ARP 协议请求路由器 IP 获取。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hn3Yib8lsNyRPJh0iatWN3nfybheZ801z3pu8J6NG6rEVYRLnQhvKGzR3g/640?wx_fmt=png&from=appmsg)

通过前文得知，最终我们需要先通过构造ARP数据包来拿到相应的目的MAC地址。

ARP 数据包的构造相对简单很多:

1. **确定MAC地址：**

1. 对于ARP请求，目的MAC地址通常是广播地址（FF:FF:FF:FF:FF:FF），这意味着请求将被发送到局域网上的所有设备。
2. 对于ARP响应，目的MAC地址是发起ARP请求的设备的MAC地址。

2. **填充以太网帧头：**

1. 填入源MAC地址和目的MAC地址。
2. 类型字段设置为ARP协议的值（0x0806）。

3. **填充ARP数据包：**

1. 填写操作码(ARPRequest |ARPReply )，源IP，源MAC，目的IP即可。

```
eth := layers.Ethernet{    SrcMAC:       sender.adapterDevice.Mac,    DstMAC:       net.HardwareAddr{0xff, 0xff, 0xff, 0xff, 0xff, 0xff},    EthernetType: layers.EthernetTypeARP,}arp := layers.ARP{    AddrType:          layers.LinkTypeEthernet,    Protocol:          layers.EthernetTypeIPv4,    HwAddressSize:     6,    ProtAddressSize:   4,    Operation:         layers.ARPRequest,    SourceHwAddress:   srcMAC,    SourceProtAddress: srcIP,    DstHwAddress:      []byte{0, 0, 0, 0, 0, 0},    DstProtAddress:    dstIP,}
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdWNlBPmFibay3nmrFWt2ajAj5T2HzjXia0syZn4icRhfOe8m85xhht8A3Zt6ic4vjtOBpdxooChrA4Ww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcwRHcRrcjVAgBhh8ibWe5hn6MXVD1G1JNO2Rd8WWkI0faVz8icLlc6DIIia4nXRFHWDnJdbP2LUbBEA/640?wx_fmt=png&from=appmsg)

至此，我们已经完成了所有的前置工作，最终的关键扫描逻辑大致如下

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef04Te45g6HekibgJoOibQ6wvHTQ12kBOjFbcbll0YhnyRNa071ENjJK8hw/640?wx_fmt=png&from=appmsg)

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yakl...