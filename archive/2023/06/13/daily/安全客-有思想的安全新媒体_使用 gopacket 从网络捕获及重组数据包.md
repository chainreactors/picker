---
title: 使用 gopacket 从网络捕获及重组数据包
url: https://www.anquanke.com/post/id/288460
source: 安全客-有思想的安全新媒体
date: 2023-06-13
fetch_date: 2025-10-04T11:46:03.584192
---

# 使用 gopacket 从网络捕获及重组数据包

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

# 使用 gopacket 从网络捕获及重组数据包

阅读量**387971**

发布时间 : 2023-06-12 15:58:16

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

gopacket 是谷歌开源的项目，它为 Golang 提供捕获及处理网络数据包的能力。其底层基于 libpcap（在 Linux 上）和 npcap（在 Windows 上）。

# 概述

包 gopacket 为 Go 语言提供数据包解码功能。

gopacket 包含多个带有额外功能的子包，包括：

1. layers：每次都可能使用该子包。它包含内置于 gopacket 的用于解码数据包协议的逻辑。注意，下面的所有示例代码假定已经导入 gopacket 和 gopacket/layers。
2. pcap：使用 libpcap 从网络读取数据包的 C 绑定。
3. pfring：使用 PF\_RING 从网络读取数据包的 C 绑定。
4. afpacket：从网络上读取数据包的 Linux AF\_PACKET 的 C 绑定。
5. tcpassembly：TCP 流重组。

此外，如果打算直接编写代码，那么请查看 examples （https://github.com/google/gopacket/tree/master/examples）子目录，其中包含许多使用 gopacket 库构建的简单二进制示例。

由于 x/sys/unix 依赖，pcapgo/EthernetHandle、afpacket 和 bsdbpf 至少需要 Go 1.7。除此之外，所需的最小 Go 版本是 1.5。

## 基本应用

gopacket 以 []byte 的形式接收数据包数据，并且将其解码为具有非零“层”数的数据包。每层对应于字节中的一个协议。解码数据包后，可以从数据包中请求数据包的层。

// Decode a packet

packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Default)

// Get the TCP layer from this packet

if tcpLayer := packet.Layer(layers.LayerTypeTCP); tcpLayer != nil {

fmt.Println(“This is a TCP packet!”)

// Get actual TCP data from this layer

tcp, \_ := tcpLayer.(\*layers.TCP)

fmt.Printf(“From src port %d to dst port %d\n”, tcp.SrcPort, tcp.DstPort)

}

// Iterate over all layers, printing out each layer type

for \_, layer := range packet.Layers() {

fmt.Println(“PACKET LAYER:”, layer.LayerType())

}

可以从许多起始点解码数据包。许多基础类型都实现了 Decoder 接口，这使我们能够解码我们没有完整数据的数据包。

// Decode an ethernet packet

ethP := gopacket.NewPacket(p1, layers.LayerTypeEthernet, gopacket.Default)

// Decode an IPv6 header and everything it contains

ipP := gopacket.NewPacket(p2, layers.LayerTypeIPv6, gopacket.Default)

// Decode a TCP header and its payload

tcpP := gopacket.NewPacket(p3, layers.LayerTypeTCP, gopacket.Default)

## 从源读取数据包

大多数情况下，你不会只是拥有数据包数据的 []byte。相反，你将希望从某处（文件、接口等）读取数据包，然后处理它们。为此，需要构建 PacketSource。

首先，需要构造实现 PacketDataSource 接口的对象。在 gopacket/pcap 和 gopacket/pfring 子包中，有该接口的实现…请查看文档，了解关于其用法的更多信息。一旦拥有 PacketDataSource，可以将其与选择的解码器一起传进 NewPacketSource，创建 PacketSource。

一旦拥有 PacketSource，可以以多种方式从其中读取数据包。请查看 PacketSource 的文档，了解更多细节。最简单的方式是 Packets 函数，该函数返回一个 Channel，然后异步地将数据包写进该 Channel，如果 packetSource 达到文件结束（end-of-file），则关闭 Channel。

packetSource := … // construct using pcap or pfring

for packet := range packetSource.Packets() {

handlePacket(packet) // do something with each packet

}

可以通过设置 packetSource.DecodeOptions 中的字段更改 packetSource 的解码选项…查看下面的部分，了解更多细节。

## 惰性解码

gopacket 选择性地惰性解码数据包数据，这意味着它只在需要处理函数调用时解码数据包层。

// Create a packet, but don’t actually decode anything yet

packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Lazy)

// Now, decode the packet up to the first IPv4 layer found but no further.

// If no IPv4 layer was found, the whole packet will be decoded looking for

// it.

ip4 := packet.Layer(layers.LayerTypeIPv4)

// Decode all layers and return them. The layers up to the first IPv4 layer

// are already decoded, and will not require decoding a second time.

layers := packet.Layers()

惰性解码的数据包不是并发安全的（concurrency-safe）。由于并非所有层都已解码，所以每次调用 Layer() 或 Layers() 都可能修改数据包，以解码下一层。如果在多个协程中并发地使用数据包，那么不要使用 gopacket.Lazy 选项。此时，gopacket 将完全解码数据包，所有未来的函数调用将不修改该对象。

## 无拷贝解码

默认情况下，gopacket 将拷贝传递给 NewPacket 的切片，在数据包内存储该拷贝。因此对切片下层的字节的修改不会影响数据包及其层。如果可以保证不更改底层切片字节，那么使用 NoCopy 告诉 gopacket.NewPacket，它将使用被传入的切片本身。

// This channel returns new byte slices, each of which points to a new

// memory location that’s guaranteed immutable for the duration of the

// packet.

for data := range myByteSliceChannel {

p := gopacket.NewPacket(data, layers.LayerTypeEthernet, gopacket.NoCopy)

doSomethingWithPacket(p)

}

最快的解码方式是同时使用 Lazy 和 NoCopy，但是请注意，从上面的许多警告中可以看出，对于某些实现来说，其中之一或两者都可能是危险的。

##

## 已知层的指针

在解码过程中，某些层作为已知的层类型被存储在数据包中。比如 IPv4 和 IPv6 都是 NetworkLayer 层，而 TCP 和 UDP 都是 TransportLayer 层。gopacket 支持 4 个层，对应于 TCP/IP 分层模式的 4 个层（大致相当于 OSI 模型的 2、3、4 和 7 层）。可以使用 packet.LinkLayer、packet.NetworkLayer、packet.TransportLayer 和 packet.ApplicationLayer 函数，访问这些层。这些函数返回相应的接口（gopacket.{Link,Network,Transport,Application}Layer），前三层提供用于获取该特定层的源地址/目标地址的方法，而最后一层提供用于获取负载数据的 Payload 方法。这很有用，比如，获取所有数据包的负载，而不管其底层数据类型如何：

// Get packets from some source

for packet := range someSource {

if app := packet.ApplicationLayer(); app != nil {

if strings.Contains(string(app.Payload()), “magic string”) {

fmt.Println(“Found magic string in a packet!”)

}

}

}

ErrorLayer 是特别有用的层，它在数据包的解析部分存在错误时被设置。

packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Default)

if err := packet.ErrorLayer(); err != nil {

fmt.Println(“Error decoding some part of the packet:”, err)

}

请注意，我们没有从 NewPacket 返回错误，因为我们在遇到错误层之前，可能已经成功解码了许多层。即便 TCP 层格式不正确，仍然可以正确地获取 Ethernet 和 IPv4 层。

## Flow 和 Endpoint

gopacket 有两个有用的对象，Flow 和 Endpoint，用于以协议无关的方式，传达数据包来自于 A，进入 B 的事实。常用的层类型 LinkLayer、NetworkLayer 和 TransportLayer 都提供用于提取其 Flow 信息的方法，而无需关心底层 Layer 的类型。

Flow 是简单的对象，由两个 Endpoint 组成，一个源和一个目的地。它详细地说明数据包的某一层的发送方和接收方。

Endpoint 是源或目的地的可哈希表示。比如，对于 LayerTypeIPv4，Endpoint 包含 v4 IP 数据包的 IP 地址字节。Flow 可以分解为 Endpoint，Endpoint 可以组合成 Flow：

packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Lazy)

netFlow := packet.NetworkLayer().NetworkFlow()

src, dst := netFlow.Endpoints()

reverseFlow := gopacket.NewFlow(dst, src)

Endpoint 和 Flow 都能用作映射键，相等运算符可以比较它们，因此根据端点准则，可以很容易地将所有数据包分组在一起：

flows := map[gopacket.Endpoint]chan gopacket.Packet

packet := gopacket.NewPacket(myPacketData, layers.LayerTypeEthernet, gopacket.Lazy)

// Send all TCP packets to channels based on their destination port.

if tcp := packet.Layer(layers.LayerTypeTCP); tcp != nil {

flows[tcp.TransportFlow().Dst()] <- packet

}

// Look for all packets with the same source and destination network address

if net := packet.NetworkLayer(); net != nil {

src, dst := net.NetworkFlow().Endpoints()

if src == dst {

fmt.Println(“Fishy packet has same network source and dst: %s”, src)

}

}

// Find all packets coming from UDP port 1000 to UDP port 500

interestingFlow := gopacket.FlowFromEndpoints(layers.NewUDPPortEndpoint(1000), layers.NewUDPPortEndpoint(500))

if t := packet.NetworkLayer(); t != nil && t.TransportFlow() == interestingFlow {

fmt.Println(“Found that UDP flow I was looking for!”)

}

出于负载均衡的目的，Flow 和 Endpoint 都拥有 FastHash() 函数，该函数提供其内容的快速、非加密散列。特别重要的是 Flow FastHash() 是对称的：A -> B 与 B -> A 具有相同的哈希值。示例用法如下：

channels := [8]chan gopacket.Packet

for i := 0; i < 8; i++ {

channels[i] = make(chan gopacket.Packet)

go packetHandler(channels[i])

}

for packet := range getPackets() {

if net := packet.NetworkLayer(); net != nil {

channels[int(net.NetworkFlow().FastHash()) & 0x7] <- packet

}

}

这允许我们拆分数据包流，同时仍然确保每个流看到一个 Flow（及其双向的反向）的所有数据包。

## 实现自己的解码器

如果你的网络有一些奇怪的封装，那么可以实现自己的解码器。在本例中，我么处理用 4 字节头封装的 Ethernet 数据包。

// Create a layer type, should be unique and high, so it doesn’t conflict,

// giving it a name and a decoder to use.

var MyLayerType = gopacket.RegisterLayerType(12345, gopacket.LayerTypeMetadata{Name: “MyLayerType”, Decoder: gopacket.DecodeFunc(decodeMyLayer)})

// Implement my layer

type MyLayer struct {

StrangeHeader []byte

payload []byte

}

func (m MyLayer) LayerType() gopacket.LayerType { return MyLayerType }

func (m MyLayer) LayerContents() []byte { return m.StrangeHeader }

func (m MyLayer) LayerPayload() []byte { return m.payload }

// Now implement a decoder… this one strips off the first 4 bytes of the

// packet.

func decodeMyLayer(data []byte, p gopacket.PacketBuilder) error {

// Create my layer

p.AddLayer(&MyLayer{data[:4], data[4:]})

// Determine how to handle the rest of the packet

return p.NextDecoder(layers.LayerTypeEthernet)

}

// Finally, decode your pack...