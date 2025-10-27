---
title: 字节跳动开源Linux内核网络抓包工具netcap
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508962&idx=1&sn=dd1c14ad39aef41f90e3ab1a7527d9ae&chksm=e9d36800dea4e1165a27bf413f5aa104a26e131ded29c000d816f82c024744610fec54ae078c&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-21
fetch_date: 2025-10-06T18:04:48.391936
---

# 字节跳动开源Linux内核网络抓包工具netcap

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOju8BKicLibhRsrkaJJpBfiajG1iaLK8ibWHMCiacicQQGsZKYXxRVxjPkteiaND6vFdoGt0wcDMXDnkZZNbA/0?wx_fmt=jpeg)

# 字节跳动开源Linux内核网络抓包工具netcap

字节跳动技术团队

以下文章来源于字节跳动SYS Tech
，作者字节跳动STE团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6uUM5Ku4VPaMibzyXia8bJZJsrcIVT7KGMQFvYZQQucicYg/0)

**字节跳动SYS Tech**
.

聚焦系统技术领域，分享前沿技术动态、技术创新与实践、行业技术热点分析。

**一、背景介绍**

在 Linux 内核网络开发过程中，网络丢包问题是一个常见的挑战。传统的网络抓包工具（如 tcpdump）虽然能够帮助开发者定位问题，但其效率较低，且在深度网络问题定位方面能力有限。随着 eBPF 技术的快速发展，出现了更高级的问题跟踪能力。字节跳动 STE 团队基于此技术开发了**下一代内核网络抓包工具**：**netcap**（net capture，内部原名：xcap**）**，并**正式对外开源**，GitHub 地址：https://github.com/bytedance/netcap

与 tcpdump 工具只能作用于内核网络协议栈准备发包和收包的固定点相比，netcap 可以几乎跟踪整个内核网络协议栈（有skb作为参数的函数）。字节跳动 STE 团队使用 tcpdump 语法作为过滤条件，以 skb（socket buffer）为上下文，可以轻松掌握整个报文在内核网络协议栈的完整踪迹，从而帮助开发者大大提高内核网络丢包问题的定位效率。

**二、使用举例**

**例1**：查看 ip 10.227.0.45 的 icmp 包是否到达内核预期的函数调用点， 这样做的好处是：在定位排查网络问题的时候，可以方便的缩小怀疑范围，提高效率。

```
netcap skb -f icmp_rcv@1 -i eth0 -e "host 10.227.0.45" -t "-nnv"
```

其中 -f 后面的参数是 kprobe 或者 tracepoint 的具体函数（默认是kprobe），并且需要告诉 netcap，skb 在这个函数(本例是 icmp\_rcv )的第几个参数（从1开始），本例是第1个。

* -i 后面是指skb的dev参数对应的网卡，这里要谨慎使用，因为有些函数的 skb 是没有设置 dev 的。
* -e 的参数是 tcpdump 的过滤语法。
* -t 的参数是 tcpdump 的显示方式，netcap 并没有自己显示数据包内容，而是借用了 tcpdump 的显示方式。

**例2**：查看内核对于 tcp 端口 9000 的报文的丢包位置

```
netcap skb -f tracepoint:skb:kfree_skb -e "tcp port 9000" -S
```

其中 -f 后面的参数是 kprobe 或者 tracepoint 的具体函数，tracepoint 不需要传递 skb 是第几个参数。

-S 表示连带着打印出此调用的 stack，本例中通过 stack 可以看到是哪里丢包的。

举个例子，在机器上配置一个丢包的 iptables 规则把来访的 tcp 9000 的包丢掉，如下图所示：

```
iptables -A INPUT -p tcp --dport 9000 -j DROP
```

然后使用 netcap上面的命令观察丢包情况：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Z4txjviceemO93lGPnmOwyj2iaNfKWnpFQicibeibfo2AaEm8nib71KasFJaAbtrr3Db2F2q0jEiagvE4KDseaiaKujPMQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其它命令行参数可以通过阅读开源代码的 README 或命令 netcap help skb 来详细了解。

**三、设计与实现**

![](https://mmbiz.qpic.cn/mmbiz_svg/hqDXUD6csUicaib5bGnRK1LpE7Q9zLzxKhfhD2NF1efsITAu1fNOIWbFRdGNFADAruibkpWd5tQlT9MfIeRiaob42YVZ93m7ltsM/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**主体框架**

netcap 通过 kprobe / tracepoint 方式实现函数的 hook，通过函数参数获取 skb 和 sock 关键结构体，拿到网络包的数据，通过 bpf map 和用户态进行数据传递。

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFBPQ9BVf6HD1jdwCU98AbWjEL3siaTvusZdYm71QnuvogSM4ia5XBrrNcg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_svg/hqDXUD6csUicaib5bGnRK1LpE7Q9zLzxKhfhD2NF1efsITAu1fNOIWbFRdGNFADAruibkpWd5tQlT9MfIeRiaob42YVZ93m7ltsM/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**实现原理**

netcap 的 工作原理大体如下：在 eBPF 程序中完成数据包的过滤，找出 tcpdump 语法过滤的包，然后把这个包给到 netcap 应用程序，netcap 应用程序再把这个包发去给 tcpdump 显示，或者直接输出 pcap 文件。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFBfWNYknkCuCrdmiagAYt5MLZSmW2etyYMY6TibGv9yhHkLaNnZStBXwfw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**1. 如何按 tcpdump 语法过滤**

tcpdump 的过滤语法是基于 cBPF的，使用开源库：https://github.com/cloudflare/cbpfc 这里可以把 tcpdump 的过滤语法转化成一个 C 函数，这个 C 函数可以嵌入到 netcap 的 eBPF 的程序中。转成 C 函数的基本原理如下：先利用 libpcap 库把 tcpdump 过滤语法转成 cBPF 指令码，然后基于此指令码转化成 C 语言的函数。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFB7KWrdSAo9hMWiboqd5LzNiaGXicmJrGT4a7h00icV7ZjINj444PZDxOQIw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**2. 如何把数据包内容用 tcpdump 显示出来**

netcap 程序启动后，也会启动一个 tcpdump 的程序，tcpdump 的标准输入接收 pcap 格式的输入流，然后以不同的参数（例如 -e 是显示 mac 地址）从其标准输出打印出解析后的格式。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFBD4MVDVpYHZn4EtJIicMrHBI0vwKYSrAUVzEuAhKCycYDaunEQ2TicccQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**3. 如何找到数据包的内容**

在内核中，是用 skb 来描述数据包的，找到 skb 中所指定的不同 header 的位置，就可以找到整个数据包，skb 的结构大体如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFBy4eNvLnqSHdLfrfK1LEMknQRyyvQkX5Y7dqEVy4CptLbqLlUnI6yWA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**4. 发送方向数据包不完整，如何过滤数据包**

在发送数据包的时候，例如 \_\_ip\_finish\_output 函数，有时未填充完整的 eth头、ip 头、tcp 头，那么是怎么得到完整的包呢？

netcap 会尽力根据 skb 的 sock 结构来推导，还原数据包，此时抓出来的包有些非关键信息会与实际情况不一致（比如 ip 头的 id 字段）。skb 通过sock来推导数据包内容的逻辑大体如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemPDSgt1F8rRSQpVEygG6KFBBdlxG4DIIgnuZ8ofytqxYgGrL6of2PX8BMOFkqUbgLUyVkibianYhqZA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**四、其他用法及扩展**

![](https://mmbiz.qpic.cn/mmbiz_svg/hqDXUD6csUicaib5bGnRK1LpE7Q9zLzxKhfhD2NF1efsITAu1fNOIWbFRdGNFADAruibkpWd5tQlT9MfIeRiaob42YVZ93m7ltsM/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**多Trace点汇总分析**

netcap 可以统计数据包经过多个点的时间，然后汇总输出，从而分析性能，举个例子，使用下面的命令：

```
netcap skb -f tracepoint:net:netif_receive_skb,ip_local_deliver@1,ip_local_deliver_finish@3,icmp_rcv@1 -e "host 10.227.0.72 and icmp" -i eth0  --gather --gather-output-color cyan
```

可以观察到输出如下，根据到达 trace 点的时间，就能够分析出数据包性能损耗在哪里，或者在哪里可能引入了延迟。

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemO93lGPnmOwyj2iaNfKWnpFQnLMEE09f1iaIUSjMvWpRPnKe9e4oGgDAPnsxMMibAaYvG7fOH9yVknDg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_svg/hqDXUD6csUicaib5bGnRK1LpE7Q9zLzxKhfhD2NF1efsITAu1fNOIWbFRdGNFADAruibkpWd5tQlT9MfIeRiaob42YVZ93m7ltsM/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**扩展功能**

用户可以自定义自己的过滤函数和输出函数，这里举例如下，

```
netcap skb -f icmp_rcv@1 -e "host 10.227.0.72" -i eth0 --user-filter skb_user_filter.c --user-action skb_user_action.c --user-output-color green
```

其中扩展过滤文件 skb\_user\_filter.c 如下：

```
// Return 0 means it's not need, pls filter out it.static inline int xcap_user_filter(void *ctx, void *pkt, u16 trace_index) {    return 1;}
```

这个扩展函数的返回值如果是 0，表示在 tcpdump 语法的过滤后，再进行一次用户自定义过滤，比如可以方便的写几行脚本，然后按照 skb->mark 来过滤。

其中扩展输出文件 skb\_user\_action.c 如下：

```
struct  xcap_user_extend {    int         a; // format: 0x%x    uint32_t    b; //
    int64_t     c;         uint8_t       x1; // format: %c    uint8_t       x2; // format: 0x%x    uint16_t      x3; // format: 0x%x};
// Return 0 means not need to ouputstatic inline int xcap_user_action(void *ctx, void *pkt, u32 pkt_len, struct xcap_user_extend *user, u16 trace_index){    user->a = 0x12345678;    user->b = 1000;    user->c = 2002;    user->x1 = 'M';    user->x2 = 0x11;    user->x3 = 0xabcd;
    return 1;}
```

其中 struct xcap\_user\_extend 是用户自定义的结构体，想输出什么信息，就在这个结构体定义并赋值即可。结构体可支持的类型如下 (注:不支持指针，也不支持数组)：int8\_t, uint8\_t, char, int16\_t, uint16\_t, int, uint32\_t,int64\_t, uint64\_t 。

这样就可以附带一些信息输出了，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/Z4txjviceemO93lGPnmOwyj2iaNfKWnpFQM6eV3C5ftIVfm5MueKYgLDj9GgGGLn6WBgyADGOttWekBsEyg6ARzA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**五、未来展望**

在开发者的日常工作中，网络抓包工具成为了网络工程师、测试工程师等必备的技能之一，字节跳动 STE 团队开源的 netcap 网络抓包工具，期望能够帮助大家提高定位内核网络丢包问题的效率，非常欢迎开发者们一起加入并贡献 PR，共同推进开源项目发展。未来我们也将在以下几个方向进行优化，敬请关注。

* 对 DPDK 的进一步支持，由于 usdt 的上游库存在问题，故无法支持应用程序的 usdt，有兴趣的读者可以修改支持。
* 对多内核版本的统一支持。
* 在自定义输出的时候，数据包较多的情况下，会出现打印错乱，原因是 tcpdump 的输出信息和用户自定义的输出信息共同使用了标准输出，未来也将针对该问题做后续优化。

**往期精彩**

# [字节跳动STE团队6个议题中选Linux网络开发者会议——Netdev](http://mp.weixin.qq.com/s?__biz=Mzg3Mjg2NjU4NA==&mid=2247485028&idx=1&sn=2b2d4298c3334d0bb40ccdc286457eac&chksm=cee9f013f99e79054bafaee40b884fac8ab40a5ea251c6c8fa26e5e6f740d63724cdc8c72ee1&scene=21#wechat_redirect)

# [字节跳动系统智能运维实践 | DataFun大会分享回顾](http://mp.weixin.qq.com/s?__biz=Mzg3Mjg2NjU4NA==&mid=2247485022&idx=1&sn=5a5e931716d90d00159ad5893b5fa4f4&chksm=cee9f029f99e793f5ed362564307a9fe9aad1578e11102994a0e5173da195850fcccd31b470d&scene=21#wechat_redirect)

# [字节跳动STE团队2篇论文入选国际峰会 IEEE RAS in Data Centers Summit](http://mp.weixin.qq.com/s?__biz=Mzg3Mjg2NjU4NA==&mid=2247484946&idx=1&sn=c3e8117a5a810cb5a7be75b1b5112d86&chksm=cee9f065f99e79732861ac8ca6307c84d61aceab474f0c95a3dbc36bfb49fd25ee605f6bcf8c&scene=21#wechat_redirect)

# [OpenBMC：coredump自动发现及调试实践](http://mp.weixin.qq.com/s?__biz=Mzg3Mjg2NjU4NA==&mid=2247484933&idx=1&sn=9d034bab4cda9c09b84c5626b134892a&chksm=cee9f072f99e7964a35eb1dcd4e34b21d6fa2e7723a0805b45f...