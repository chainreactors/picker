---
title: eBPF Rootkit检测实战指南
url: https://mp.weixin.qq.com/s/z2PQSBZwfiRHPMB3QEoinw
source: Doonsec's feed
date: 2026-08-07
fetch_date: 2026-08-08T03:22:42.088402
---

# eBPF Rootkit检测实战指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Kric7mM9eA5DhRwasnrsctOr2kfHPLQpw1dsw0Y2qqMicEkx9RVebYaNh8cB0ib8Vxib9hzIl2f5icEOv2iaC0zE6Rw1OqqJm5wsLbEUzwEg7YqpY/0?wx_fmt=jpeg)

# eBPF Rootkit检测实战指南

Dubito
Dubito

云原生安全指北

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 注：本文翻译自 Datadog 的文章《Detection primitives for eBPF rootkits》[1]，可点击文末“阅读原文”按钮查看英文原文。

## 一、引言

在过去几年中，Linux恶意软件开发者开始使用eBPF rootkit来逃避传统和现代防御机制。在野发现的样本能够绕过长期以来被认为难以逃避的工具（如`ss`），以及那些假设攻击者无法触及内核级自检机制的工具（如`bpftool`）。它们还能挫败`ptrace`等常见的追踪原语。LinkPro[2]（译文详见：[LinkPro：针对云环境的eBPF rootkit剖析](https://mp.weixin.qq.com/s?__biz=MzIyMzM2MzE1OQ==&mid=2247484544&idx=1&sn=14c6e5bf123525953e46bd703a7145ca&scene=21#wechat_redirect)）、VoidLink[3]（译文详见：[VoidLink：隐秘的云原生Linux恶意软件框架剖析](https://mp.weixin.qq.com/s?__biz=MzIyMzM2MzE1OQ==&mid=2247485069&idx=1&sn=23b45eab0c68baf15363d30bbf47806f&scene=21#wechat_redirect)）以及最近的Atomic Arch[4]攻击行动都采用了这些手法。

我们不打算逐一完整描述每个恶意软件家族，而是从每个家族中选取一个具有启发性的特性深入剖析，研究其技术原理、防御者应关注的数据以及我们据此构建的检测规则。先从VoidLink开始，它通过将一个调试辅助函数转化为精确的内存编辑器，找到了一种出人意料地干净利落的方式来向`ss`隐藏活跃连接。

### 1.1 VoidLink：bpf\_probe\_write\_user()的巧妙利用

`bpf_probe_write_user()`辅助函数允许从eBPF程序内部覆写用户空间内存。官方文档[5]将其描述为"调试、转移和操控半协作进程执行"的工具。这使其成为rootkit眼中极具吸引力的原语，VoidLink的开发者正是利用它来绕过`ss`。

`ss`工具通过Netlink子系统获取打开的套接字统计信息。当运行`ss -tn`显示活跃TCP连接时，涉及三个系统调用：

1. 1. `socket(AF_NETLINK, SOCK_RAW, NETLINK_INET_DIAG)`打开一个原始Netlink套接字。`AF_NETLINK`告知内核这是一个通向内核子系统的IPC通道，而非网络套接字（socket）。
2. 2. `sendmsg(fd, request)`向内核发送结构化请求。消息包含两部分：（1）Netlink头部，指定消息类型（`SOCK_DIAG_BY_FAMILY`）和请求完整转储的标志（`NLM_F_DUMP`）；随后是（2）`inet_diag_req_v2`请求体。该请求体设置三个字段：协议族（`AF_INET`）、协议（`IPPROTO_TCP`）和套接字ID（置零表示通配，匹配所有套接字）。
3. 3. `recvmsg(fd, buffer)`读取内核响应：一个由`inet_diag_msg`记录组成的多部分数据流，每个套接字对应一条记录，以`NLMSG_DONE`结尾。每条记录包含源/目的IP和端口、TCP状态、所属用户UID以及inode号。

内核将这些响应组织为TLV（类型，长度，值）消息链：每条消息以携带类型和长度的`nlmsghdr`头部开头，紧跟着是载荷。用户空间解析器通过`NLMSG_OK`和`NLMSG_NEXT`等宏遍历这条链，这些宏使用长度字段作为游标，从一条消息前进到下一条。

VoidLink需要在特定端口上隐藏连接，这是rootkit的标准功能。它在`__sys_recvmsg`的入口处放置一个`kprobe`，在系统调用运行前捕获用户空间缓冲区指针——这是唯一能获取系统调用参数的时机。配对的`kretprobe`在内核用套接字数据填充缓冲区之后、用户空间读取之前触发。此时，`bpf_probe_write_user`就地篡改缓冲区：它会增大待隐藏消息**前一条**消息的长度字段，使膨胀后的长度完全吞掉被隐藏的消息，解析器的游标直接跳过它。

![bpf_probe_write_user()篡改前后对比：nlmsg A的长度字段被增大，NLMSG_NEXT直接从A跳到C，完全跳过被隐藏的消息B](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5Drp8MPbDhDdeKK5dv4MkNgXnJhqVYZx4GTKn4DaLdficfk87a5NrAyReH14aeia4mVDR1lkXERXwSyAn06d5T9bI7VfBuvjmfv4/640?from=appmsg "null")

bpf\_probe\_write\_user()篡改前后对比：nlmsg A的长度字段被增大，NLMSG\_NEXT直接从A跳到C，完全跳过被隐藏的消息B

`NLMSG_NEXT`按`NLMSG_ALIGN(h->nlmsg_len)`推进游标。当`A.nlmsg_len=112`时，游标从位置0直接跳到位置112，落在消息C上。而承载rootkit想要隐藏的端口的那条消息B，被完全跳过。

这个技巧不会破坏`ss`的解析，因为`NLMSG_OK`此时只检查一个关键条件：`nlmsg_len <= len`，其中`len`是缓冲区剩余字节数。VoidLink将A的长度精确增大`NLMSG_ALIGN(B.nlmsg_len)`——即缓冲区中实际存在的字节大小——因此膨胀后的长度始终不会超出剩余空间。`NLMSG_OK`持续返回true，`NLMSG_NEXT`正确落在下一条消息上，解析器既不会越界读取，也看不到任何不一致。从`ss`的角度看，消息A只是比平时稍长了一点。

### 1.2 LinkPro：bpf\_override\_return()的威力

`bpf_override_return()`可以从eBPF程序内部替换内核函数的返回值。内核对此有严格限制：该辅助函数只能从附加到内核源码中标记为`ALLOW_ERROR_INJECTION`的函数上的`kprobe`类型程序中调用，且宿主机内核必须以`CONFIG_BPF_KPROBE_OVERRIDE=y`编译。在这些条件下，当`kprobe`触发时，该辅助函数将所选值写入保存的返回寄存器，并完全跳过原函数。对用户空间而言，看起来就像是内核本身产生了那个结果。内核团队设计此辅助函数是为了在`bpf_trace`风格的测试中进行故障注入，但对任何想让内核替自己撒谎的rootkit来说，这显然是一个诱人的原语。

LinkPro使用`bpf_override_return()`来隐藏自身的eBPF程序，使其无法被枚举。该恶意软件的Hide模块在`sys_enter_bpf`（`handleBpfEnter`）上附加了一个跟踪点（tracepoint），监控三个枚举命令——`BPF_PROG_GET_NEXT_ID`(11)、`BPF_MAP_GET_NEXT_ID`(12)和`BPF_LINK_GET_NEXT_ID`(31)——并将调用上下文暂存在以`pid_tgid`为键的map中。配对的`kretprobe`挂在`__x64_sys_bpf`（`handleBpfExit`）上，在返回路径触发，取出暂存的上下文，读取内核即将返回给用户空间的`next_id`，并与`main_ebpf_progs`（用户空间组件用LinkPro自身程序ID填充的允许列表）比对。匹配时，它调用`bpf_override_return(ctx, -ENOENT)`。调用者（`bpftool`、`libbpf`或任何遍历程序列表的工具）看到`-ENOENT`，就会认为没有更多条目了。

这个细节对检测工程师很重要。`-ENOENT`是`GET_NEXT_ID`遍历的自然终止符，因此在迭代的任何位置返回它都会停止枚举器，而不是跳过一条记录。我们在实际内核上验证了这一点：加载模块后，我们用单个良性程序ID填充`main_ebpf_progs`，运行`bpftool prog list`，观察到列表在该ID处被截断。所有更高ID的程序也消失了，无论它们是否在允许列表中。Hide模块的机制比开发者可能预期的更强大，但它也留下了清晰的检测信号：防御者将枚举结果与`bpftool prog show id N`（该命令使用`BPF_PROG_GET_FD_BY_ID`，此hook不会拦截）进行对比，就能发现差异。

LinkPro还留下了看似无意的用户空间痕迹。`handleBpfEnter`和`handleBpfExit`都会调用`bpf_printk`，分别输出`"BPF cmd: %d, start_id: %u"`和`"HIDING NEXT_ID: %u"`，这些输出在每次被拦截的系统调用时以纯文本形式流向`/sys/kernel/debug/tracing/trace_pipe`。防御者和安全软件可以轻易发现这一点，但可能会将其视为恶意软件开发者的遗留物，因此不应将其作为主要检测机制。

```
---------------------------------------------------------------------------
kretprobe___x64_sys_bpf:0000000000002050
kretprobe___x64_sys_bpf:0000000000002050 LBB5_10:                                ; CODE XREF: handleBpfExit+138up j
kretprobe___x64_sys_bpf:0000000000002050                 mov            r2, r10
kretprobe___x64_sys_bpf:0000000000002058                 add            r2, -0xC
kretprobe___x64_sys_bpf:0000000000002060                 lddw           r1, 0
kretprobe___x64_sys_bpf:0000000000002070                 call           1
kretprobe___x64_sys_bpf:0000000000002078                 jeq            r0, 0, LBB5_9
kretprobe___x64_sys_bpf:0000000000002080                 ldxb           r1, [r0]
kretprobe___x64_sys_bpf:0000000000002088                 jne            r1, 1, LBB5_9
kretprobe___x64_sys_bpf:0000000000002090                 ldxw           r3, [r10-0xC]
kretprobe___x64_sys_bpf:0000000000002098                 lddw           r1, 26
kretprobe___x64_sys_bpf:00000000000020A8                 mov            r2, 19
kretprobe___x64_sys_bpf:00000000000020B0                 call           6        ; bpf_trace_printk("HIDING NEXT_ID: %u", 19, next_id): debug log confirming suppression;
kretprobe___x64_sys_bpf:00000000000020B0                                         ; visible in /sys/kernel/debug/tracing/trace_pipe
kretprobe___x64_sys_bpf:00000000000020B8                 mov            r1, r6
kretprobe___x64_sys_bpf:00000000000020C0                 mov            r2, -2   ; -ENOENT: the injected return value;
kretprobe___x64_sys_bpf:00000000000020C0                                         ; tells the caller the next_id does not exist
kretprobe___x64_sys_bpf:00000000000020C8                 call           58       ; call bpf_override_return(ctx, -ENOENT):
kretprobe___x64_sys_bpf:00000000000020C8                                         ; overwrites sys_bpf return value in pt_regs before userspace sees it.
kretprobe___x64_sys_bpf:00000000000020C8                                         ; Requires CONFIG_BPF_KPROBE_OVERRIDE.
kretprobe___x64_sys_bpf:00000000000020C8                                         ; Any tool calling BPF_PROG_GET_NEXT_ID/BPF_MAP_GET_NEXT_ID/BPF_LINK_GET_NEXT_ID
kretprobe___x64_sys_bpf:00000000000020C8                                         ; that receives this next_id will get -ENOENT and skip it, hiding the program from bpftool and libbpf enumeration.
kretprobe___x64_sys_bpf:00000000000020D0                 ja             LBB5_13
kretprobe___x64_sys_bpf:00000000000020D0 ; End of function handleBpfExit
kretprobe___x64_sys_bpf:00000000000020D0
kretprobe___x64_sys_bpf:00000000000020D0 ; end of 'kretprobe___x64_sys_bpf'
kretprobe___x64_sys_bpf:00000000000020D0
license:00000000000020D8 ; ===========================================================================

LinkPro handleBpfExit()函数的注解反汇编
```

### 1.3 Atomic Arch：用bpf\_send\_signal()杀死进程

```
tp_syscalls_sys_enter_ptrace:0000000000000EE8 enter_ptrace:                           ; tracepoint: sys_enter_ptrace, kill callers trying to attach to hidden PIDs
tp_syscalls_sys_enter_ptrace:0000000000000EE8                 ldxdw          r2, [r1+0x10]
tp_syscalls_sys_enter_ptrace:0000000000000EF0                 jeq            r2, 0x4206, loc_F00 ; request == PTRACE_SEIZE (0x4206)?
tp_syscalls_sys_enter_ptrace:0000000000000EF8                 jne            r2, 0x10, unk_F50 ; request == PTRACE_ATTACH (0x10)?
tp_syscalls_sys_enter_ptrace:0000000000000F00
tp_syscalls_sys_enter_ptrace:0000000000000F00 loc_F00:                                ; CODE XREF: tp_syscalls_sys_enter_ptrace:0000000000000EF0up j
tp_syscalls_sys_enter_ptrace:0000000000000F00                 ldxdw          r1, [r1+0x18] ; load target pid from tracepoint ctx->pid (offs...