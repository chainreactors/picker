---
title: 使用ebpf对Linux进行跟踪7:使用kernel tracepoints跟踪
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488593&idx=1&sn=4452a69802d336bd25a387c493dcaa4f&chksm=fdf97f44ca8ef652bcbba062eda91774b6e28663ab5fbd769f8aa385fff5cd9423c290386b50&scene=58&subscene=0#rd
source: 奶牛安全
date: 2023-03-25
fetch_date: 2025-10-04T10:37:48.879217
---

# 使用ebpf对Linux进行跟踪7:使用kernel tracepoints跟踪

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAKBqVp3a3Qw3jCzKh7rqMXPSeM5z3DahEv6KyGOaK6YwqkpNVAE6IyQ/0?wx_fmt=jpeg)

# 使用ebpf对Linux进行跟踪7:使用kernel tracepoints跟踪

原创

debugeeker

奶牛安全

`uprobes, kprobes, uretprobes, kretprobes`非常棒，但它们也有自己劣处。当函数参数改变了，或想从函数内部获取信息。

还是接着`virtio`的话题，在上一篇提到过，内核端的`virtio`是`vhost-net`。看一下它在内核代码里`linux-uek/drivers/vhost/net.c`的接收和发送处理函数

```
static void handle_rx(struct vhost_net *net) {
    ...
    do {
        ...
    } while (likely(!vhost_exceeds_weight(vq, ++recv_pkts, total_len)));
    ...
}

static void handle_tx(struct vhost_net *net) {
    ...
    do {
        ...
    } while (likely(!vhost_exceeds_weight(vq, ++sent_pkts, total_len)));
    ...
}
```

在这里可以继续用`kprobes`和`kretprobes`，但由于这两个函数没有任何返回值，所以`kretprobes`获取不到任何信息，而`kprobes`也只能获取到`vhost_net`这个数据结构的数据。虽然这个数据结构可以提供一些信息，但像接收包数量`recv_pkts`和发送包数量`sent_pkts`的信息，却没办法获取得了。

如果获取这些信息，其中一个方法是使用`kernel tracepoints`。`kernel tracepoints`是静态检测的一种形式，因此需要直接在代码中定义和实现跟踪点函数。

## 实现kernel tracepoints

比如想跟踪`total_len`

```
static void handle_rx(struct vhost_net *net) {
    ...
    do {
        ...
    } while (likely(!vhost_exceeds_weight(vq, ++recv_pkts, total_len)));

    trace_vhost_net_rx_end(recv_pkts, total_len);
    ...
}

static void handle_tx(struct vhost_net *net) {
    ...
    do {
        ...
    } while (likely(!vhost_exceeds_weight(vq, ++sent_pkts, total_len)));

    trace_vhost_net_tx_end(sent_pkts, total_len);
    ...
}
```

这里需要定义和实现了两个`kernel tracepoint`:`trace_vhost_net_rx_end`,`trace_vhost_net_rx_end` 。

那么在哪里和怎样定义和实现它们呢。一般的位置是在`linux-uek/include/trace/events`。这个位置每个头文件都包含很多`kernel tracepoint`。

原则上，所有系统或子系统的跟踪点定义在它们相应的头文件中。所以,这里的头文件为 `linux-uek/include/trace/events/vhost_net.h`

```
/* Kernel tracepoints for vhost_net virtio functions */
#undef TRACE_SYSTEM
#define TRACE_SYSTEM vhost_net

#if !defined(_TRACE_VHOST_NET_H) || defined(TRACE_HEADER_MULTI_READ)
#define _TRACE_VHOST_NET_H

#include <linux/tracepoint.h>
#include <linux/vhost.h>

TRACE_EVENT(vhost_net_rx_end,

        TP_PROTO(int recv_pkts, int total_len),

        TP_ARGS(recv_pkts, total_len),

        TP_STRUCT__entry(
            __field(    int,    recv_pkts   )
            __field(    int,    total_len   )
        ),

        TP_fast_assign(
            __entry->recv_pkts = recv_pkts;
            __entry->total_len = total_len;
        ),

        TP_printk("recv_pkts=%d, total_len=%d",
            __entry->recv_pkts,
            __entry->total_len)
);

TRACE_EVENT(vhost_net_tx_end,

        TP_PROTO(int sent_pkts, int total_len),

        TP_ARGS(sent_pkts, total_len),

        TP_STRUCT__entry(
            __field(    int,    sent_pkts   )
            __field(    int,    total_len   )
        ),

        TP_fast_assign(
            __entry->sent_pkts = sent_pkts;
            __entry->total_len = total_len;
        ),

        TP_printk("sent_pkts=%d, total_len=%d",
            __entry->sent_pkts,
            __entry->total_len)
);

#endif /*_TRACE_VHOST_NET_H */

/* This part must be outside protection */
#include <trace/define_trace.h>
```

> 这里的函数都没有`trace_`前缀，`TRACE_EVENT`这个宏会自动把它展开成`trace_`开头的函数。

在`net.c`文件上包括上这个头文件

```
// Other header files...
...
#define CREATE_TRACE_POINTS
#include <trace/events/vhost_net.h>
...
```

由于`kernel tracepoint`是静态的，需要重新编译内核，在内核代码目录下执行：

```
 make -j 144
 make modules_install
 make install
```

然后重启机器，选择新内核启动。

> 最好在`/etc/default/grub`里菜单加多一项，指向新内核，如果新内核有问题，可以使用之前正常的内核进入系统

使用以下参数启动虚拟机

```
-device virtio-net-pci,netdev=tapnet
-netdev tap,id=tapnet,vhost=on,ifname=tap0,script=/etc/qemu-ifup,downscript=no
```

使用`BCC`工具看一下新的`kernel tracepoint`是否加载

```
python tplist.py | grep vhost
```

开始实现`eBPF`程序：

```
#!/usr/bin/python

from bcc import BPF
from time import sleep

bpf_txt = """

BPF_HISTOGRAM(rx_pkts_hist);
BPF_HISTOGRAM(rx_len_hist);
BPF_HISTOGRAM(tx_pkts_hist);
BPF_HISTOGRAM(tx_len_hist);

struct our_ktp_args {
    u64 __unused__;
    int packets;
    int total_length;
};

int rx_end(struct our_ktp_args *args) {
    int recv_pkts = args->packets;
    int len = args->total_length;

    rx_pkts_hist.increment(bpf_log2l(recv_pkts));
    rx_len_hist.increment(bpf_log2l(len));
    return 0;
}

int tx_end(struct our_ktp_args *args) {
    int sent_pkts = args->packets;
    int len = args->total_length;

    tx_pkts_hist.increment(bpf_log2l(sent_pkts));
    tx_len_hist.increment(bpf_log2l(len));
    return 0;
}
"""
# Load BPF program
bpf_ctx = BPF(text=bpf_txt)
bpf_ctx.attach_tracepoint(tp="vhost_net:vhost_net_rx_end",
                          fn_name="rx_end")
bpf_ctx.attach_tracepoint(tp="vhost_net:vhost_net_tx_end",
                          fn_name="tx_end")

# Print header
print("Aggregating data from vhost-net RX & TX virtqueues... "
      "Hit Ctrl-C to end.")

# Format output
while 1:
    try:
        sleep(1)
    except KeyboardInterrupt:
        print("\n")
        break

# Output
print("Vhost-net RX log2 received packets histogram")
print("--------------------------------------------")
bpf_ctx["rx_pkts_hist"].print_log2_hist("recv pkts")
print("\n")

print("Vhost-net RX log2 total length histogram")
print("----------------------------------------")
bpf_ctx["rx_len_hist"].print_log2_hist("total len")
print("\n")

print("-------------------------------------------------")
print("\n")

print("Vhost-net TX log2 sent packets histogram")
print("----------------------------------------")
bpf_ctx["tx_pkts_hist"].print_log2_hist("sent pkts")
print("\n")

print("Vhost-net TX log2 total length histogram")
print("----------------------------------------")
bpf_ctx["tx_len_hist"].print_log2_hist("total len")
print("\n")
```

运行一把

```
./kernel_tracepts.py
Aggregating data from vhost-net RX & TX virtqueues... Hit Ctrl-C to end.
^C

Vhost-net RX log2 received packets histogram
--------------------------------------------
     recv pkts           : count     distribution
         0 -> 1          : 482291   |****************************************|
         2 -> 3          : 40457    |***                                     |
         4 -> 7          : 534      |                                        |
         8 -> 15         : 4        |                                        |
        16 -> 31         : 2        |                                        |

Vhost-net RX log2 total length histogram
----------------------------------------
     total len           : count     distribution
         0 -> 1          : 330      |                                        |
         2 -> 3          : 0        |                                        |
         4 -> 7          : 0        |                                        |
         8 -> 15         : 0        |                                        |
        16 -> 31         : 0        |                                        |
        32 -> 63         : 8        |                                        |
        64 -> 127        : 32       |                                        |
       128 -> 255        : 9        |                                        |
       256 -> 511        : 8        |                                        |
       512 -> 1023       : 30       |                                        |
      1024 -> 2047       : 15275    |*                                       |
      2048 -> 4095       : 15516    |*                                       |
      4096 -> 8191       : 57986    |*****                                   |
      8192 -> 16383      : 433015   |****************************************|
     16384 -> 32767      : 1060     |                                        |
     32768 -> 65535      : 14       |                                        |
     65536 -> 131071     : 4        |                                        |
    131072 -> 262143     : 1        |                                        |

-------------------------------------------------

Vhost-net TX log2 sent packets histogram
----------------------------------------
     sent pkts   ...