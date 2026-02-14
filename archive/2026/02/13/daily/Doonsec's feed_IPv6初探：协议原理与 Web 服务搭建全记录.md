---
title: IPv6初探：协议原理与 Web 服务搭建全记录
url: https://mp.weixin.qq.com/s/I6ku4MA_bge3E6fZoiPhSA
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:03:48.774830
---

# IPv6初探：协议原理与 Web 服务搭建全记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rOFdN8iclAcW6IsAVD2D5IOpMXS0PjCaWxgTuCnna7nrFkP9BQsicPheAoyDMJNADosI0Kae6icUTicdaWlW2Cm2QrKuDxxbsbnyYqAd2iabR9U0/0?wx_fmt=jpeg)

# IPv6初探：协议原理与 Web 服务搭建全记录

M3ng9e
M3ng9e

萌蘖向阳成参天

![]()

在小说阅读器中沉浸阅读

近日，有幸接手了人生中第一个 IoT 设备安全测试项目——一款智能摄像头，这次的难点在于需要聚焦 **IPv6 暴露面** 下的安全评估和漏洞挖掘。

作为一个 IoT 安全新手，复杂的环境搭建以及如何触发 IPv6 下的 P2P 通信，让我花费了很多时间。但其实测试的本质逻辑未变：IPv6 只是通道。

**本文作为系列首篇，将重点记录我对 IPv6 的协议原理探究与学习心得。**

# **IPv6的学习探究**

## **IPv6 产生的动机**

#### **核心动机：地址不够用了**

IPv4协议32bit的地址空间已经被用完啦，IPv4理论上最多只有约 43 亿 （2^{32}）个IP地址。

而IPv5协议是一个实验室研究的协议，研究发现设计的有些问题，最终被废弃掉了。

后边研究了IPv6协议，地址从IPv4的32位，变成了128位，2^{128}个地址，彻底解决了地址短缺问题。

#### **进阶动机：为了更快、更强（了解即可）**

除了地址不够，IPv4 在设计上也有一些年代久远的“包袱”。IPv6 借机优化了头部格式，目的是**加速处理/转发**和提升服务质量 (QoS)。

* **头部 Checksum (校验和) 的移除：**

+ **IPv4:** 每个路由器收到数据包，都要算一下校验和，看看数据有没有坏。如果坏了就丢弃。而且因为 TTL 变了，校验和每次都要重算，非常耗时。
+ **IPv6:直接取消了头部校验和**。设计者认为现在的链路（光纤等）错误率很低，且上层协议（TCP/UDP）已经有校验了。**路由器不再计算校验和，处理速度大大加快。**

* **分片 (Fragmentation) 机制的改变：**

+ **IPv4:** 如果一个数据包太大，路由器有义务把它切碎（分片）再转发。这对路由器来说负担很重。
+ IPv6:路由器不再负责分片。如果包太大，路由器直接丢弃并通知发送端：“包太大，请你自己切好再发”。这大大减轻了中间路由器的压力。

* **TTL-1 (Time To Live / Hop Limit):**

+ 这是防止数据包在网络中无限循环的机制。每经过一个路由器，这个值就要减 1。
+ 在 IPv6 中，由于不需要重新计算 Checksum，这个“减 1”的操作变得非常快。

* **帮助 QoS (服务质量)：**

+ IPv6 头部引入了Flow Label (流标签)。这让路由器能识别出哪些包属于同一个“流”（比如一个视频会议的实时数据流），从而优先处理这些对延迟敏感的数据，保证网络质量。

## **IPv6 数据报格式 (Datagram Format)**

基于上述的优化动机，IPv6 确定了新的格式规则：

**固定的 40 字节头部：**

![image-20260213181916250](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcU0ib2Yc3faFtpuR5jNIDNe0BDfAv9drzDvduvgNOWiaqvb9vDe1BMjWor68iakkxes9fTu4VxlQ6pyZSribLYpDNIuresITtxGQ78/640?wx_fmt=png&from=appmsg)

image-20260213181916250

![image-20260213183522146](https://mmbiz.qpic.cn/sz_mmbiz_png/rOFdN8iclAcVAIxgOYiaZOmiadLdG5Jl9iajrxXofE2vrTibRJa057PLtP6p16hLhKiajRIiaW1eYA548WMgL7uWBN1MBYLYe7jxxVzw6WlibtzVibEw/640?wx_fmt=png&from=appmsg)

image-20260213183522146

* ver是版本的意思，一个字节，可以看到是6。
* pri是优先级的意思，但是在wireshark叫 **`Traffic Class`** (流量类别)，这里是0x00，没有要求路由器给它开 VIP 通道（比如插队优先转发）。一般普通上网流量都是 0。
* flow label是流标签的意思，这里是第 0xc8f12号数据流。
* Payload Length是载荷长度，这里是20，意味着 IPv6 头部后面紧跟的数据只有 20 字节，因为这是一个ACK包
* Next Header是下一个头部的意思，标识上层协议是什么，图中表示的是TCP(6)。

  | **十进制值** | **十六进制 (Hex)** | **含义 (协议/扩展头)** | **说明** |
  | --- | --- | --- | --- |
  | **6** | `0x06` | **TCP** | 传输层协议 |
  | **17** | `0x11` | **UDP** | 传输层协议 |
  | **58** | `0x3a` | **ICMPv6** | IPv6 的 Ping、邻居发现、报错 |
  | **0** | `0x00` | **Hop-by-Hop** | 逐跳选项头 (每个路由器都要处理的) |
  | **43** | `0x2b` | **Routing** | 路由头 (指定数据包走的路径) |
  | **44** | `0x2c` | **Fragment** | 分片头 (还记得吗？中间路由器不分片，源端分片就用这个头) |
  | **59** | `0x3b` | **No Next Header** | 后面没有头部了 (通常用于测试或空包) |
* Hop Limit 是跳数限制的意思，和IPv4的TTL是一样的。

* IPv4 的头部长度是可变的（20~60字节），路由器处理起来比较麻烦，需要去“猜”头在哪里结束。
* IPv6 强制头部固定为 40 字节。这让硬件处理变得极其简单高效，因为机器可以预知每个字段的确切位置。

![image-20260213181633846](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcXCNw2I6iafosKwyBAEHwM5dMGw89lVvaTwKwMkFqicxVubAAhDp1ibjxIuOLuGibqbZ3pmBp1x4VDoX6El5YNPMljlfC3Z0nvv6E8/640?wx_fmt=png&from=appmsg)

image-20260213181633846

**传输过程中不允许分片：**

+ 中间路径上的路由器（Routers）绝对不会去处理分片工作，而是通过路由器生成一个 **ICMPv6 (Type 2, Packet Too Big)** 消息，发回给**数据的发送者（源端）**，以此保证数据高速通过。

  ![image-20260213185020448](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcW31omjMiansxVibOgqE8P8ISRoaC6SL1ZKHh378BEqcBxcAziakyxnOL0nxAcl1icdJpibW0VD7ian3XW99KV8HSqST1uaH8sPbhaibo/640?wx_fmt=png&from=appmsg)

  image-20260213185020448

## **IPv6 地址书写格式**

![image-20260213174329437](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcUFzrlt3yfKb4ww2DjHctf99kW4z715kIK1icsLteAUibFq1UdbwEiay5YaE0uqwicgzhgaeF88d4k95YbZYrN1bohlUxoN2J1B1aQ/640?wx_fmt=png&from=appmsg)

image-20260213174329437

128位的IPv6地址被分为8组，每组的16位用4个十六进制字符（0～9，A～F）来表示，组和组之间用冒号（:）隔开。

每组中的前导“0”都可以省略，例如2001:db8:130F:0000:0000:09C0:876A:130B-->2001:db8:130F:0:0:9C0:876A:130B

连续两个或多个均为0的组，可以用双冒号“::”来代替，例如2001:db8:130F:0:0:9C0:876A:130B-->2001:db8:130F::9C0:876A:130B

## **IPv6 地址结构**

![image-20260213190808597](https://mmbiz.qpic.cn/sz_mmbiz_png/rOFdN8iclAcXibYicQDqXg04a5JTYcCWLmEhJVZNCQ39gF3Ymiap4Rc095pKicGIvAsSE0GrpZds438GswxLs7GrhE5J9aNWbKo2lL467OZFgr1M/640?wx_fmt=png&from=appmsg)

image-20260213190808597

一般来说IPv6 分为`网络前缀 (Network Prefix)+接口标识 (Interface ID)`，都是64bit。

Network Prefix又可以划分为

* **前 48 位 (Global Routing Prefix)：** 比如 `2409:8c54:0870`。这是运营商分给你家光猫的大网段。
* **中间 16 位 (Subnet ID)：** 比如 `0002`。这是你自己家路由器分的“子网”。你可以在家划分出 2^{16}=65536 个子网（比如客厅网、客房网），非常富裕。

## **IPv6 地址类型**

| **类型** | **前缀 (Prefix)** | **样子 (示例)** | **对应 IPv4 概念** | **能否上外网？** |
| --- | --- | --- | --- | --- |
| **全球单播 (GUA)** | `2000::/3` | `2409:8c54...` | 公网 IP (`8.8.8.8`) | **能** |
| **唯一本地 (ULA)** | `fd00::/8` | `fd12:3456...` | 私网 IP (`192.168.1.x`) | **不能** |
| **链路本地 (LLA)** | `fe80::/10` | `fe80::1a2b...` | APIPA (`169.254.x.x`) | **不能** |
| **回环地址** | `::1/128` | `::1` | Localhost (`127.0.0.1`) | 本机自嗨 |

## **IPv6和IPv4怎么通信？大家都在用IPv4，如何慢慢升级为IPv6？**

这些问题我推荐看B站中科大郑烇老师讲的，5分钟，用一个例子讲的特别明白，太妙了。

https://www.bilibili.com/video/BV1JV411t7ow?spm\_id\_from=333.788.videopod.episodes&vd\_source=ade4be45ef14d1451786aaf8cff87aa6&p=32（1h42min开始讲IPv6）

**简单点说，IPv6目前是少数，所以如果通信转发的时候，会将IPv6封装在IPv4里传输，当IPv6多起来，以后IPv4借助IPv4的封装传输，直到最后都升级成了IPv6。这个叫平滑升级。**

## **IPv6的获取方式**

1. SLAAC (Stateless Address Autoconfiguration)

   路由器只负责把网络前缀 Prefix给出来，具体的接口 ID自己设置，也就是对应静态配置。

   **过程：**

1. **RS (Router Solicitation):** 电脑刚开机，不知道谁是老大，于是发一个广播：“网关你在哪？”
2. **RA (Router Advertisement):** 路由器听到后，回复：“我是网关，这是我们的网络前缀（比如 `2409:8c54::/64`），剩下的你自己看着办。”
3. **自造 IP：** 电脑拿到前缀，自己生成后 64 位（用 MAC 地址算，或者随机生成），拼在一起，就是一个完整的 IPv6 地址。
4. **查重 (DAD):** 电脑最后会问一声：“这地址有人用吗？”没人吭声，它就正式启用了。

2. DHCPv6 (Stateful)

   和DHCPv4一样，电脑必须找 DHCPv6 服务器申请，服务器记录在案，分配一个固定的 IP 给你。

   ![image-20260213204710157](https://mmbiz.qpic.cn/sz_mmbiz_png/rOFdN8iclAcUnsveZiadc22VE4h73Imt3WjicibJNLaiaZevdmicDgyqAWOEOf69YKGkibxJm2kQU3iaFQ5N2E7gLf698icqhPsFToF3ALrPqVzlvhDk/640?wx_fmt=png&from=appmsg)

   image-20260213204710157
3. Stateless DHCPv6 —— 混合模式

   这是目前最主流的家用模式。

* **IP 地址：** 用 SLAAC 自动生成（快）。
* **DNS 服务器：** 用 DHCPv6 获取（因为 RA 广播里以前不能带 DNS 信息）。

## **IPv6的底层通信 (NDP)**

在 IPv6 里，ARP 死了，被 NDP (Neighbor Discovery Protocol) 取代了。

NDP 基于 ICMPv6，它非常强大，依靠 **5 种报文** 搞定了一切：

| **报文类型** | **名字** | **作用 (通俗解释)** | **对应 IPv4** |
| --- | --- | --- | --- |
| **RS** (Type 133) | 路由器请求 | "网关大哥你在哪？" | DHCP Discover |
| **RA** (Type 134) | 路由器通告 | "我是网关，前缀是这个..." | (无) |
| **NS** (Type 135) | 邻居请求 | "谁是 `2409::1`？请把 MAC 地址告诉我！" | **ARP Request** |
| **NA** (Type 136) | 邻居通告 | "我是 `2409::1`，我的 MAC 是 xx:xx..." | **ARP Reply** |
| **Redirect** (Type 137) | 重定向 | "别走我这儿，走那个路由更快。" | ICMP Redirect |

## **IPv6的DNS**

在 IPv4 里，查域名的记录叫 **A 记录**。

在 IPv6 里，查 IP 地址的记录叫 **AAAA 记录**（因为 128 位是 32 位的 4 倍，所以叫 4 个 A）。

```
nslookup -qt=AAAA www.google.com
```

![image-20260213193254741](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcVRhLaZMuDu3Dw4iah6ogUHrjHBaVWdB9MGMibWicT8JULk9aUoRGI8R9oUTD2UPmpy3w2TbicPpMOpWGJh4SF9WV1od6BQOVjzhaM/640?wx_fmt=png&from=appmsg)

image-20260213193254741

![image-20260213193157988](https://mmbiz.qpic.cn/sz_mmbiz_png/rOFdN8iclAcVQico0xdWnAz6JJ3ibRpOAa5XfysX15nKKzOTbUvEjDQmpEbWYpLEfgbB6xEAmTQ8OkBDbbFbBweMOcAHzEkMO6u0KHns54NrNU/640?wx_fmt=png&from=appmsg)

image-20260213193157988

# **使用IPv6将本机作为Web服务器的探究**

## **申请IPv6地址**

首先我连接了一个可以分配ipv6的光猫（路由器手机热点都可以，主要能获取IPv6地址），于是我就具有了ipv6地址。

![image-20260129142128086](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcVDnCmzTsMgT3X1iaEazEtNOia861ib6icL7SUDSz3ZL1BfcRfbBBvZsZPfaEnuSzmeN7yjZtQMPumb6omZK5F1vQYJUUVnZvADsPI/640?wx_fmt=png&from=appmsg)

image-20260129142128086

## **打通网络**

这个时候我的设备1还没有暴露在公网，是因为具有防火墙的限制。

现在尝试关闭防火墙让其暴露在公网（最好是在防火墙里设置只允许某些服务通过，我这里是做实验图简单）。

1. 打开控制面板\系统和安全\Windows Defender 防火墙
2. 直接关闭防火墙或者打开ipv6的通信
3. 并且我使用phpstudy搭建了一个web服务

然后我使用了另外一个设备2（使用手机sim卡数据流量开热点，这样就可以具有不同网络下的ipv6地址了）进行尝试ping，nmap扫描，以及访问web服务，可以看到ping，端口扫描都是可以看得到的，但是web服务访问不到。

![image-20260129144326982](https://mmbiz.qpic.cn/mmbiz_png/rOFdN8iclAcWW4S9zicCEfmTsicCfe0hPjoTZGXlrwicYl2v0XibZf2f45aUB5adDQQq7nUd7E4FGxV6LrFKpibFuZcFod1bKe5ia0PicfGm6aIwnuk/640?wx_fmt=png&from=appmsg)

image-20260129144...