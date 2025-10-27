---
title: 使用 eBPF-TC 在内核中安全地改变数据包
url: https://buaq.net/go-144577.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:45.288838
---

# 使用 eBPF-TC 在内核中安全地改变数据包

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3a07b25810d0b29123da67231be9e041.jpg)

使用 eBPF-TC 在内核中安全地改变数据包

介绍eBPF 允许你在 OS 内核中安全地运行沙箱程序，用于安全性和网络等功能，而无需修改内核源代码或加载内核模块。eBPF-TC 具有牢固的数据包处理能力，并支持入口和出口操作，而且性能很高。这
*2023-1-7 20:21:1
Author: [www.cnxct.com(查看原文)](/jump-144577.htm)
阅读量:30
收藏*

---

### 介绍

eBPF 允许你在 OS 内核中安全地运行沙箱程序，用于安全性和网络等功能，而无需修改内核源代码或加载内核模块。eBPF-TC 具有牢固的数据包处理能力，并支持入口和出口操作，而且性能很高。

这是我使用 `TC-eBPF` 构建插件 TPROXY 截流防火墙 (IFW) 来截取并将数据包发送到我的目标应用程序 OpenZiti Edge Routers 的方法。你可以使用类似的 eBPF-TC 实现来截取要发送到你特定可观察性、安全性或网络应用程序的数据包。代码和 README.md 在这里：[GitHub – r-caamano/ebpf-tproxy-splicer](https://github.com/r-caamano/ebpf-tproxy-splicer)。流程图和数据流图在本文末尾。

### 项目背景 – 将数据包发送到 OpenZiti 端点

OpenZiti（开源零信任网络平台）能够在完整网络覆盖网络中建立私有连接。Ziti 端点作为代码嵌入在应用程序中（通过 Ziti SDK），并作为 OS 代理、守护程序、容器或虚拟机部署。你可以在你的私有网络中启动任意数量的 Ziti 路由器 – 如果你部署了两个路由器，它看起来像这样：

![](https://image.cnxct.com/2023/01/qJTZ9uPxE.jpg)

Ziti Edge 路由器通常在 Linux 上使用，默认使用 iptables 将传入的感兴趣流量映射到服务侦听端口，使用 IP 表 Tproxy 目标。如果你正在运行 Ubuntu 和 FWD，这就很好用了。然而，还有许多带有关键差异的 Linux 发行版。因此，我使用 TC-eBPF 为支持 eBPF 的 Linux 发行版构建了更通用的选项，使这些发行版能够截取感兴趣的流量。eBPF 特性集还提供了 iptables/nftables 原生不支持的附加数据包过滤和操作。

### TC-eBPF IFW – tproxy 目标条目

因此，在开始构建 eBPF IFW 之前，我需要反向工程 OpenZiti 边缘路由器如何将服务本地转换为 iptables 规则 – 基于路由器从 OpenZiti Controller 学习的服务，需要添加/删除哪些 TPROXY 目标语句。以下是通过 iptables 创建 tproxy 目标条目所使用的信息。

```
IP Destination Prefix: Dotted Decimal IP/mask bit-length
TCP/UDP port range in the format Decimal Low_Port:High_Port
Protocol: TCP/UDP
TPROXY Listening port: Decimal port
```

现在，有了这些信息，我可以开始考虑我将使用的 eBPF map 类型和结构，以便在用户空间映射工具和 IFW 之间进行通信，以动态更新规则。

由于我希望我的程序的功能与 `ufw/iptables` 类似，所以我选择了 TC-eBPF 作为我的插入点，因为它在接口级别的组合（在转发到 Linux IP 栈之前丢弃数据包的能力）和当前可用的 sk 帮助程序（用于 socket 查找/拼接）。

为了检查传入的数据包是否与 Ziti 网络管理员创建的截获策略（Ziti 特别定义了流量，而不是默认截获所有流量）匹配，我需要一个支持结构体键类型的固定映射。eBPF 哈希映射允许使用结构体作为键，这使我能够自定义查找，并随着用例的发展添加或删除标准。使用固定映射允许多个 ebpf 程序的副本运行（每个入站接口上运行一个），并共享由映射工具/Ziti 更新的映射。

下图描述了我选择的初始映射定义：

```
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(id, BPF_MAP_ID_IFINDEX_IP);
    __uint(key_size, sizeof(uint32_t));
    __uint(value_size, sizeof(struct ifindex_ip4));
    __uint(max_entries, 50);
    __uint(pinning, LIBBPF_PIN_BY_NAME);
} ifindex_ip_map SEC(".maps");
The initial key I chose a struct of the following form:
struct tproxy_key {
    __u32 dst_ip;
    __u16 prefix_len;
    __u16 protocol;
}
```

这些数据结构允许基于目的 IP 前缀、CIDR 长度和 IP 协议（tcp/udp）进行查找，这些都可以从传入的数据包中推断出来。 对于值，我使用了以下格式的结构体：

```
struct tproxy_tuple {
   __u16 index_len; /*tracks the number of entries in the index_table*/
   __u16 index_table[MAX_INDEX_ENTRIES];
  /* Array used as index table which points to Struct *tproxy_port_mapping in the
  port_maping array with each poulated index representing a udp or tcp tproxy
  mapping in the port_mapping */

struct tproxy_port_mapping port_mapping[MAX_TABLE_SIZE];
  /* Array to store unique tproxy mappings with each index match the low_port of the
  struct  tproxy_port_mapping{
  __u16 low_port;
  __u16 high_port;
  __u16 tproxy_port;
  __u32 tproxy_ip;
  }
  */
}
```

由于 OpenZiti 基于 IP 的服务策略可以在任何粒度级别定义，包括网络 CIDR 块，所以我不希望为包含在块中的每个主机地址生成哈希条目。因此，我实现了一种最长匹配查找算法，该算法逐次扩大掩码检查，以查看传入的 IP 元组是否直接匹配主机地址，或者是否在与 `tproxy_key` 中的 `ip_dest/prefix_len` 字段匹配的 CIDR 块范围内，以及匹配 IP 运输协议（TCP 或 UDP）。

```
struct tproxy_tuple *tproxy
__u32 exponent=24;  /* unsugend integer used to calulate prefix matches */
__u32 mask = 0xffffffff;  /* starting mask value used in prefix match calculation */
__u16 maxlen = 32; /* max number ip ipv4 prefixes */

for (__u16 count = 0;count <= maxlen; count++){
    struct tproxy_key key = {(tuple->ipv4.daddr & mask), maxlen-count,protocol}
    if ((tproxy = get_tproxy(key))){
            { Redacted for brevity}

    /*algorithm used to calucate mask while traversing each octet.*/
    if(mask == 0x00ffffff){
       exponent=16;
    }
    if(mask == 0x0000ffff){
       exponent=8;
    }
    if(mask == 0x000000ff){
       exponent=0;
    }
    if(mask == 0x00000080){
       return TC_ACT_SHOT;
    }
    if((mask >= 0x80ffffff) && (exponent >= 24)){
       mask = mask - (1 << exponent);
    }else if((mask >= 0x0080ffff) && (exponent >= 16)){
       mask = mask - (1 << exponent);
    }else if((mask >= 0x000080ff) && (exponent >= 8)){
       mask = mask - (1 << exponent);
    }else if((mask >= 0x00000080) && (exponent >= 0)){
       mask = mask - (1 << exponent);
            }
    exponent++;
}
```

此外，由于 Ziti 最终用户可以将任意数量的端口范围与协议基础上的目标关联，在这第一次尝试中，我不希望为每个端口创建哈希映射条目，因为可能存在大的端口范围，例如 1-65535。相反，我在索引表中创建了一个条目，其中每个条目都指向 port\_mapping 表中已填充的数组索引，其中索引是映射规则的 low\_port 值。这将查找端口匹配的搜索限制为仅已填充的端口范围条目，而不是直接在端口映射表中的顺序索引搜索。我计划测试为每个成员端口创建哈希映射条目与范围起始的索引查找的性能和资源限制。下面是一个用于基于传入的 `tuple->ipv4.dport` 查找匹配的代码片段。

```
for (int index = 0; index < max_entries; index++) {
    /* set port_key equal to the port value stored at current Index */
    int port_key = tproxy->index_table[index];
    /*
check if tuple destination port is greater than low port and lower than high
port at mapping[port_key]
if matched get associated tproxy port and attempt to find listening socket
if successfull jump to assign:
   */
     if ((bpf_ntohs(tuple->ipv4.dport) >= bpf_ntohs(tproxy->port_mapping[port_key].low_port))
          && (bpf_ntohs(tuple->ipv4.dport) <=bpf_ntohs(tproxy>port_mapping[port_key].high_port))){
          If(local){ /* if tuple->daddr == router’s ip then forward to stack */
              return TC_ACT_OK;
         }
         /* construct tuple to used to lookup TPROXY sk */
         sockcheck.ipv4.daddr = tproxy->port_mapping[port_key].tproxy_ip;
         sockcheck.ipv4.dport = tproxy->port_mapping[port_key].tproxy_port;
         /* look up sk based on protocol in map key */
         if(protocol == 6){
              sk = bpf_skc_lookup_tcp(skb, &sockcheck, sizeof(sockcheck.ipv4),
                 BPF_F_CURRENT_NETNS, 0);
         }else{
             sk = bpf_sk_lookup_udp(skb, &sockcheck,  sizeof(sockcheck.ipv4),
                 BPF_F_CURRENT_NETNS, 0);
         }
         if(!sk){
             return TC_ACT_SHOT;
         }
         if((protocol == IPPROTO_TCP) && (sk->state != BPF_TCP_LISTEN)){
             bpf_sk_release(sk);
             return TC_ACT_SHOT;
         }
         goto assign;
     }
}
assign:
    /*attempt to splice the skb to the tproxy or local socket*/
    ret = bpf_sk_assign(skb, sk, 0);
    /*release sk*/
    if(ret == 0){
       //if succedded forward to the stack
       return TC_ACT_OK;
    }
    /*else drop packet if not running on loopback*/
    if(skb->ingress_ifindex == 1){
        return TC_ACT_OK;
    }else{
        return TC_ACT_SHOT;
    }
}
```

### TC-eBPF – 有状态防火墙

由于我希望 eBPF 执行有状态防火墙的功能（至少在对于从该主机接收的已确认数据包必须有一个活动的出站会话到主机的程度上），我需要考虑如何使程序管理 UDP 和 TCP 的会话状态。最初我认为这可能很复杂。然而，在使用用于拼接套接字的 ebpf 帮助程序时，我意识到可以使用相同的帮助程序来检查是否已发起了出站套接字。在传入数据包元组与现有出站会话匹配的情况下，拼接传入的 skb 到现有的 sk 中，同时执行与程序已经为 openziti 服务 tproxy sk(s) 执行的相同查找。下面的代码摘录显示了我用于 TCP 的基本状态检查代码：

```
/* if tcp based tuple implement statefull inspection to see if they were
initiated by the local OS if not pass on to tproxy logic to determin if theopenziti router has tproxy
intercepts defined for the flow
 */
sk = bpf_skc_lookup_tcp(skb, tuple, tuple_len,BPF_F_CURRENT_NETNS, 0);
if(sk){
  if (sk->state != BPF_TCP_LISTEN){
     goto assign;
  }
  bpf_sk_release(sk);
}

assign:
    /*attempt to splice the skb to the tproxy or local socket*/
    ret = bpf_sk_assign(skb, sk, 0);
    /*release sk*/
    if(ret == 0){
       //if succeeded forward to the stack
       return TC_ACT_OK;
    }
/*else drop packet if not running on loopback*/
    if(skb->ingress_ifindex == 1){
        return TC_ACT_OK;
    }else{
        return TC_ACT_SHOT;
    }
}
```

### TC-eBPF IFW – 入站

SSH 将事情进一步，我希望默认情况...