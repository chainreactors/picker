---
title: eBPF：恶意软件的新领域
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247483990&idx=1&sn=af8e4889ae16457c13a23e80d769b975&chksm=fcdd025bcbaa8b4d2703588835daa4cf659b3fd5136400d0f4002bdd8ba1760c55a99347a791&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2023-02-23
fetch_date: 2025-10-04T07:51:53.806791
---

# eBPF：恶意软件的新领域

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvOjoESIa5NsZkhRptPasiaRXtgibYKKw744matiavhZibKorOek6Ub6AN5mQ/0?wx_fmt=jpeg)

# eBPF：恶意软件的新领域

丰生强

软件安全与逆向分析

eBPF （**扩展的Berkeley数据包过滤器**）席卷了Linux 世界。它于 2013 年首次推出以支持可编程网络，现在用于可观察性、安全性、网络等。许多大公司——包括 Meta、谷歌、微软和 Netflix——都致力于帮助开发和支持它。

注意：“eBPF”和“BPF”实际上是同义词，社区经常互换使用这些术语，部分原因是 eBPF 几乎完全取代了经典的 BPF 技术。

在本文中，我们将研究 eBPF 的一个相对较新的用例。在过去的几年里，研究人员一直在研究 eBPF 在开发恶意软件方面的作用。最近，有一些实际恶意软件在野外利用该技术的报告示例。有关恶意软件利用 eBPF 的众多演讲、研究项目和报告的列表，请参阅本文末尾的附录。

eBPF 为恶意软件作者提供了一套全新的工具，其中大部分工具并不为大众所了解。本文旨在向读者介绍 eBPF 是什么，并研究基于 eBPF 的恶意软件的一些基本构建块。最后，我们将讨论如何预防和检测恶意软件的这一新兴趋势。

## 什么是 eBPF？

eBPF 代表扩展伯克利包过滤器。它是原始 Berkeley Packet Filter (BPF) 设计的扩展，BPF 是一种用于网络过滤的非常简单的结构。eBPF 的用例最初是为了支持可编程网络而开发的，后来扩展到包括安全性、可观察性、跟踪和许多其他应用程序。它有自己的网站，是Linux 基金会的一部分，并得到许多公司的支持。

eBPF 的核心是一种指令集架构(ISA)，可以在 Linux 内核内的类似虚拟机的结构中运行。它具有寄存器、指令和堆栈，仅举几个组件。为了使用 eBPF，用户创建 eBPF 程序并将它们附加到系统周围的适当位置，通常是在内核中。当与附加点相关的事件发生时，程序运行并有机会从系统读取数据并将该数据返回给用户空间中的控制应用程序。总而言之，eBPF 允许用户动态安装可在内核上下文中执行但可从用户空间编排的代码。它有点像用户空间应用程序和 Linux 内核模块之间的混合体。

## eBPF 程序的生命周期

为了更好地理解 eBPF 的工作原理，让我们简要检查一下 eBPF 程序的生命周期：

以下图片来自eBPF 官方网站的资源。

1. eBPF 程序通常以“受限”C 程序开始。受限意味着堆栈大小、程序大小、循环、可用函数等与普通 C 程序相比受到限制。C 代码被编译成 eBPF 字节码。

   ![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvO0rLChVx3q3QDpdLicjGZLlhvjoibdWCyhicRaSlbiajOpOOibZSv9zhibZlQ/640?wx_fmt=png)
2. 然后通过调用 bpf 系统调用将该字节代码加载到内核中，通常使用更高级的库，例如 Cilium、bcc、oxideBPF、libbpfgo 或 Aya，仅举几例。

   ‍

   ![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvODnm9XhJKAavGuHKa0icic3nx27rDYw83O29XQWNkvGuwC4goibNYMeSWQ/640?wx_fmt=png)
3. 在 eBPF 代码完全加载到内核之前，它会通过验证器运行。验证者的工作是确定 eBPF 程序是否可以安全运行。“安全”是指它不会陷入无限循环，没有不安全的内存操作，并且低于最大复杂度/代码大小。

   ![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvO3waMFqmHXcVNZ2axcdBboXdtCciaVuYPDiaPCwMuBXXjJ6VgKcXiaJFTg/640?wx_fmt=png)
4. 内核组件验证程序后，它会将自己附加到内核中的适当位置。这种情况的发生方式因 eBPF 程序的类型而异。例如，通常用于高速数据包管理的 XDP 程序附加到网络接口。跟踪点程序附加到内核中用于跟踪的许多预定义位置之一。Uprobe 程序可以附加到用户空间应用程序中的任意位置。因此，重申一下，如何附加、附加到何处以及附加什么程序将根据程序类型而有很大差异。

   ![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvONjrw89hSyEFUPO3g6wuPPEicTheteRLZnicXdGKZHib1vBUCJAgkDTicBA/640?wx_fmt=png)
5. 现在程序已经过验证和附加，我们只需等待。eBPF 程序一般是事件驱动的，所以程序只会在特定事件发生时运行。那时，代码在它所附加的上下文中执行（通常在内核空间中）。

下图总结了 eBPF 程序的整个生命周期：

![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvO5vFFZDqLyOExDpjjiaBczK3u6AyNlADwdVk6Eib7V3GadD1ib1xoG5oPQ/640?wx_fmt=png)

## eBPF 变成超级赛亚人

现在我们了解了什么是 eBPF，是什么让恶意软件作者对它如此感兴趣？为了理解这个问题的答案，我们需要检查 eBPF 多年来获得的一些权力。

如前所述，它最初的设计考虑到了网络。从那时起，许多新的和不同类型的 eBPF 程序极大地扩展了它的范围和功能。让我们看一些程序类型，它们对于理解 eBPF 恶意软件的典型工作方式至关重要。

#### 套接字过滤器

套接字过滤器是经典 BPF 的原始用例。套接字过滤器是一个可以附加到套接字的 eBPF 程序。然后该程序可以过滤该套接字的传入流量。Berkley Packet Filter 的名称暗示它是一种旨在过滤数据包数据的技术。这个功能甚至一直保留到现代 eBPF 中。

#### kprobes、uprobes 和跟踪点

eBPF 程序可以附加到内核探测 ( kprobe )、用户探测 ( uprobe ) 或跟踪点。Kprobes 和 uprobes 可以分别附加到内核空间或用户空间中的几乎任何位置。另一方面，跟踪点只能附加到内核或用户空间中的预定义位置。任何时候该函数或地址运行时，eBPF 程序都会被调用，该程序将能够及时检查有关该函数调用和系统的信息。

#### eXpress 数据路径 (XDP)

XDP 程序附加在数据包处理管道的早期。这允许快速有效的数据包处理。它通常用于DDoS 缓解、数据包流管理和路由等用途，仅举几个用例。它具有修改或重定向数据包的能力。XDP 仅在数据包接收时运行。

#### 交通管制 (TC)

TC 程序类似于 XDP。主要区别在于它在网络堆栈中运行得稍晚一些。它还可以在数据包入口和出口上运行。稍后在网络堆栈中运行的好处是它提供了更多关于数据包的上下文。这允许收集更多关于数据包及其去向的数据。

## eBPF 的阴暗面

基于 eBPF 的快速采用，它显然会继续存在——并且可能会变得更加强大。现在让我们深入了解 eBPF 的阴暗面，看看研究人员和恶意软件是如何开始利用这些强大功能的。

#### `bpf_probe_write_user`

eBPF 程序可以访问一组有限的辅助函数。这些函数内置于内核中。基于 eBPF 的恶意软件使用的一个助手是`bpf_probe_write_user`. 此函数允许 eBPF 程序写入当前正在运行的进程的用户空间内存。恶意软件可以使用这种能力在系统调用期间修改进程的内存，例如bad-bpf`sudo`如何在读取时写入用户空间内存`/etc/sudoers`。它注入了一个额外的行，允许特定用户使用该`sudo`命令。

限制：

* 如果内存被换出或未标记为可写，该函数将失败
* 一条警告消息会打印到内核日志中，说明正在使用该函数。这是为了警告用户程序正在使用具有潜在危险的 eBPF 辅助函数

#### `bpf_override_return`

另一个 eBPF 辅助函数，`bpf_override_return`允许程序覆盖返回值。恶意软件开发人员可以利用它来阻止他们认为不受欢迎的操作。例如，如果你想运行`kill -9 <pid-of-ebpf-malware>`，恶意软件可以将 kprobe 附加到适当的内核函数以处理 kill 信号，返回错误，并有效地阻止系统调用的发生。ebpfkit使用它来阻止可能导致发现控制 eBPF 程序的用户空间进程的操作。

限制：

* 有一个内核构建时选项可以启用它：`CONFIG_BPF_KPROBE_OVERRIDE`
* `ALLOW_ERROR_INJECTION`它仅适用于使用宏的函数
* 目前仅支持 x86
* 它只能与 kprobes 一起使用

#### XDP 和 TC

ebpfkit利用 XDP 和 TC 进行不显眼的通信。下面是一张来自 Blackhat 会议演讲的幻灯片，其中 ebpfkit 的创建者（Guillaume Fournier、Sylvain Afchain 和 Sylvain Baubeau）概述了他们如何使用 XDP 和 TC 隐藏发送到 ebpfkit 的命令。主机上运行的 XDP 程序接收并处理请求。该程序将其识别为对主机上运行的恶意软件的请求，并将数据包修改为对主机上运行的 Web 应用程序的普通 HTTP 请求。在出口处，ebpfkit 使用 TC 程序捕获来自 webapp 的响应，并使用来自 ebpfkit 的响应数据修改其输出。

限制：

* XDP 程序运行得太早，数据与进程或套接字无关，因此数据包周围几乎没有上下文

![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZV56AVNE4Qf8pIhXRRMIvOnG0icgaTPLnsyW0AJzDAePHx8nq1T9pyNaQyeK9LNaJhzeLSOGLLZ4w/640?wx_fmt=png)

注意：我们从 DataDog 研究人员的 Black Hat 2021 演讲中获取了上图，标题为“有像 eBPF 这样的朋友，谁需要敌人？”

#### 套接字过滤器

BPFDoor使用套接字过滤器来启用隐蔽通信。它能够在系统的任何端口上接收命令，因为它使用的 eBPF 程序可以看到所有传入流量。Symbiote也利用套接字过滤器，但方式不同。Symbiote 挂钩`setsockopt`函数调用，当它看到套接字过滤器的创建时，会注入自己的代码来过滤它想要隐藏的流量。这允许它逃避数据包分析工具，如`tcpdump`.

这些只是恶意软件如何利用 eBPF 的几个例子。可能还有更多。

#### Windows 当心

顺便说一句，对于所有认为“这只是另一个 Linux 威胁……”的 Windows 用户来说，当心！它已经在 Windows 中了！

不过不要太担心。Windows 的实现仍然非常新，功能集非常有限，因此，我们可能需要一段时间才能在 Windows 上看到基于 eBPF 的恶意软件。

## 预防

那么有希望击败如此强大的敌人吗？当然！与任何恶意软件一样，第一道防线是采取预防措施。如果实施，以下步骤可能有助于安全团队防止 eBPF 恶意软件：

* 确保非特权 eBPF 被禁用。如今，要安装 eBPF 程序，您通常需要 root——或至少需要 CAP\_SYS\_ADMIN 和/或 CAP\_BPF。情况并非总是如此。围绕内核 4.4 引入了非特权 eBPF。请务必通过运行以下命令检查此配置选项：

  ```
  # sysctl kernel.unprivileged_bpf_disabled
  ```
* 禁用不需要的功能。管理员可以通过编程方式禁用诸如 kprobes 之类的东西：

  ```
  # echo 0 > /sys/kernel/debug/kprobes/enabled
  ```
* 在外部防火墙上创建防火墙过滤器以阻止可疑数据包
* 在不支持 kprobes、基于 eBPF 的 TC 过滤器或完全支持 eBPF 的情况下构建内核（尽管这可能不是许多人的选择）
* `CONFIG_BPF_KPROBE_OVERRIDE`除非绝对必要，否则不设置Ensure

## 检测

如果您怀疑您的系统上可能存在基于 eBPF 的恶意软件，那么检测起来会非常困难。安装后，您不能相信从系统工具返回的数据。检测它的最佳机会是在加载时。如果端点检测和响应 (EDR) 产品正在监视正确的事件，则它们非常适合执行此操作。如果在加载基于 eBPF 的恶意软件时没有 EDR 或监控工具存在，您仍然可以做一些事情来尝试检测基于 eBPF 的恶意软件。

寻找加载的意外 kprobes：

```
# cat /sys/kernel/debug/kprobes/列表
ffffffff8ad687e0 r ip_local_out+0x0 [FTRACE]
ffffffff8ad687e0 k ip_local_out+0x0 [FTRACE]
```

用于`bpftool`列出程序。程序之类的一些 eBPF 程序并不少见`cgroup_skb`。

```
# bpftool 程序
176: cgroup_skb 标签 6deef7357e7b4530 gpl
loaded_at 2022-10-31T04:38:09-0700 uid 0
xlated 64B jited 54B 内存锁 4096B
185: kprobe 标签 a7ce508aab49e47f gpl
loaded_at 2022-10-31T10:03:16-0700 uid 0
xlated 112B jited 69B memlock 4096B map_ids 40

# bpftool 性能
pid 543805 fd 22: prog_id 3610 kprobe func tcp_v4_connect 偏移量 0
pid 543805 fd 23: prog_id 3610 kprobe func tcp_v6_connect 偏移量 0
pid 543805 fd 25: prog_id 3611 kretprobe func tcp_v4_connect 偏移量 0
pid 543805 fd 26: prog_id 3611 kretprobe func tcp_v6_connect 偏移量 0
pid 543805 fd 28: prog_id 3612 kretprobe func inet_csk_accept 偏移量 0
```

查找加载的 XDP 程序。您会在输出中看到与此类似的一行。

```
$ ip link show dev <接口>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 xdpgeneric qdisc noqueue state UNKNOWN mode DEFAULT 组默认 qlen 1000
链接/环回 00:00:00:00:00:00 brd 00:00:00:00:00:00
prog/xdp id 220 标签 3b185187f1855c4c jited
```

检查 bpffs（BPF 文件系统）中是否有任何固定对象。

```
$ 挂载 | grep bpf
……
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
……

# ls -la /sys/fs/bpf/
```

检查是否加载了任何 TC 程序。

```
# tc filter show dev <设备名称>
```

监视系统日志中是否提及 BPF 帮助程序生成的警告消息。

```
#dmesg -k | grep 'bpf_probe_write_user'
```

## 结论

总之，eBPF 是合法开发人员和恶意软件作者等人的强大工具。由于这种范式从过去实施恶意软件的方式转变，我们需要继续研究 eBPF 以更好地了解威胁形势。

我们在 Red Canary 的威胁研究团队处于研究和理解新兴威胁的最前沿。随着我们更好地了解如何识别和检测对手对 eBPF 的滥用，我们将继续发布我们的发现。请继续关注，以更深入地了解此类恶意软件的外观、行为方式以及检测它的最佳方式。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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