---
title: 内核逐客令：wesp.sys 透露的 Windows Endpoint Security Platform
url: https://mp.weixin.qq.com/s/CT7apVB4sYUWznyksoTOUQ
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:41:43.671939
---

# 内核逐客令：wesp.sys 透露的 Windows Endpoint Security Platform

# 内核逐客令：wesp.sys 透露的 Windows Endpoint Security Platform

原创

Pavel
Pavel

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 原文：https://www.elastic.co/security-labs/blog/windows-endpoint-security-platform-wesp
> 作者：Pavel Yosifovich（Elastic，Principal Software Engineer II）
> 发布时间：2026-10-26
> 翻译模型：GLM-5.3

编者按：作者是 Pavel Yosifovich，《Windows Kernel Programming》《Windows 10 System Programming》的作者，Windows 内核开发圈的老熟人。2024 年 7 月 CrowdStrike 一次配置更新让 850 万台 Windows 机器蓝屏之后，微软着手把第三方安全产品请出内核，Windows Endpoint Security Platform（WESP）就是这条路线的产物。这篇来得早：WESP 的二进制刚进 Insider 预览版，微软还没有任何文档，作者靠一轮本地内核调试加上 PE 静态分析，把“微软牌 EDR 驱动”wesp.sys 的骨架摸了出来：文件系统 mini-filter、altitude 329500、经 filter communication port 与用户态单向通信，配套的 espclient.dll 导出约 120 个 Esp 前缀函数。想跟进“EDR 出内核”这条线的读者，值得从这篇读起。

微软正在为 EDR 产品铺一条“跑在 Windows 内核之外”的路，名字叫 Windows Endpoint Security Platform（WESP），它的两个二进制已经进入 Windows Insider 预览版：一个是内核驱动 wesp.sys，另一个是用户态 API espclient.dll。2024 年 7 月 CrowdStrike 更新弄崩 850 万台机器之后，微软想要的，是用一个由自己维护的内核驱动，取代如今每家安全厂商各自装进内核的那一个。WESP 没有文档，但二进制带着公开符号，开一次内核调试会话就能挖到不少东西。wesp.sys 是一个 altitude 329500 的文件系统 mini-filter，通过 filter communication port 与用户态通信。

## 内核态 vs 用户态：今天的 EDR 怎么跑

受够了 Windows 蓝屏吗？微软这次动真格了，决定把安全产品从 Windows 内核里请出去——能让 Windows 蓝屏的正是内核组件，而这种事影响能有多大，几年前一个第三方内核组件的 bug 已经演示过了。

典型的 EDR（Endpoint Detection and Response）软件由两个主要部分组成：一个内核态驱动和一个用户态服务，两者以某种方式通信，如下图所示：

![EDR 架构图：内核边界两侧分别是内核态驱动与用户态服务](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVANXRogLI0VX8fl1B8z5IVGZPhHHbh6qgZwibrm0rZWvwtQ965SZib1HZtevxRPZmq8jiaJcp7GdeA8yVlibpe5t238Izt9Xiaex88/640?wx_fmt=png&from=appmsg)

图里的进程框代表系统上运行的普通用户应用，比如 Word、Explorer、Paint。Service 和 Kernel Driver 由 EDR 产品安装。

内核驱动的主要用途是注册各种内核通知，比如进程创建、文件写入。值得关注的通知一般会转发给用户态服务，在那里做进一步处理：

* 把通知数据上报给服务器，做进一步的分析与聚合；
* 查一套规则，规则可能要求把操作整个拦下来；
* 向人类用户告警，有时需要人来做交互决策。

只要一切按计划运行，这套架构没什么问题。麻烦在于，内核驱动经不起“非法操作”——比如解引用一个坏指针。真出了这种事，系统就以臭名昭著的蓝屏（BSOD）收场，重启机器是唯一的恢复办法——前提还是那个肇事的驱动在开机早期加载时别再崩一次。

### CrowdStrike 事件为什么让微软改了主意

2024 年 7 月 19 日发生的就是这一幕：一份有问题的配置文件更新，让 CrowdStrike 的 EDR 内核驱动在全球数百万台机器上崩溃。内核驱动把系统带崩的风险，从 Windows 诞生起就存在，但这次尤其难看——大量机器直接不可用，机场、银行和其他关键设施瘫痪了几个小时。

微软把这事记在了心上——毕竟那是 Windows。他们启动了一个新计划，把 EDR 产品搬出内核，让类似事故不再发生。不过这件事并不简单，有几个原因：

* Windows 内核现在必须把 EDR 内核驱动赖以工作的那些通知，送到 EDR 的用户态服务手里，而且必须够高效，否则没法用；
* 就算微软给出完整方案，现有产品的迁移也需要时间，所以旧的运行方式必须继续支持；
* 这样一个框架必须足够灵活、足够完整，才能被真正采用。EDR 需要的能力但凡缺一块，采用和迁移就最多是部分的。

## Windows Endpoint Security Platform（WESP）是什么

Windows Endpoint Security Platform 是微软用来把 EDR 产品搬进用户空间的框架。项目还处在早期阶段——Windows Insider 预览版里已经带上了这个新平台的二进制。主体是一个由微软构建的内核驱动 wesp.sys，加上一个实现在 espclient.dll 里的用户态 API：EDR 的用户态服务用它建立连接、接收感兴趣的通知。

实现的核心是一个内核驱动（wesp.sys），看起来有点讽刺，但这绕不开：说到底，通知必须由内核来提供。所以 wesp.sys 扮演的正是 EDR 内核驱动的角色，只不过由微软来实现——这样需要好好测试和调试的驱动就只剩一个，而不是现在这样，每个 EDR 平台都自带一个自研内核驱动。

### EDR 厂商需要 WESP 提供什么

截至本文写作时，WESP 还没有公开文档。但如果 EDR 要采用它，有几样东西是平台必须给出的：

**要全面。** 今天的 EDR 注册通知有好几种途径，机制各不相同：

| 事件类型 | 现有注册机制 |
| --- | --- |
| Process, thread, image, handle | 带回调的注册函数 |
| Registry | 带回调的注册函数 |
| File system | 文件系统 mini-filter |
| Network | WFP callout driver |

这些五花八门的机制都在增加 EDR 驱动的复杂度。WESP 应该把它们全都覆盖；否则 EDR 驱动会继续存在，只是被 WESP 覆盖的部分代码少一些。指望第一天就全部到位不现实，但我预计最终都会补齐。

**要能过滤。** 内核驱动能注册的一些通知非常“吵”。注册表和文件读操作就是典型——无时无刻不在大量发生。跑一下 Sysinternals 的 Process Monitor（ProcMon）就有概念：每秒显示的注册表和文件系统事件（尤其读操作）成百上千。把这类事件全部传到用户态不可行——太慢，至少也低效。这意味着 WESP 必须提供某种过滤能力，让不感兴趣的事件“在源头”（也就是 WESP 驱动里）就被丢弃，而不是送到用户态再丢。这类规则的灵活性至关重要，能显著降低用户态服务的负载。

**要能拦截。** 某些内核通知独有的一种能力是拦截操作，用户态做不到。经典例子就是进程创建——内核驱动可以用 `PsSetCreateProcessNotifyRoutineEx` 注册这类事件，这是所有 EDR 都在用的有文档函数。回调在进程创建进行中就被调用，可以给创建结果设一个失败状态（比如检查新进程的命令行，认定它是恶意的）。用户态没有这种权力——进程创建了你就能收到通知，但你否决不了。WESP 的客户端（用户态）必须被赋予这种权力，才能在特定条件下拦截进程创建；这些条件也要足够灵活，大多数场景都能配置出来。理想情况下，用户态服务应当能先跑自己的代码，再答复驱动放行还是拦截。

**权限上有门槛。** 与 ESP 打交道的客户端进程必须以提升权限运行才能访问平台。它们大概率还得以 Protected Process Light（PPL）运行、由微软签名——今天大多数厂商的 EDR 服务就是这么跑的，尽管目前并未强制。

## 走进 wesp.sys：二进制透露了什么

虽然还没有文档，但翻一翻现成的二进制，也能挖出 WESP 的一些细节。额外的福利是：这些二进制的符号在微软公共符号服务器上都能下到。

在一台装了 WESP 的虚拟机上开本地内核调试会话，能对 WESP 的工作方式有直观了解。首先，WESP 的驱动文件是 wesp.sys，位于 `System32\Drivers` 目录——大多数驱动都住在这里。查一下驱动安装的注册表位置就能确定键名，它同时也是驱动的内核对象名：

![注册表编辑器：wesp 服务键，ImagePath 为 system32\drivers\wesp.sys，Type 为 2（文件系统驱动）](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVZUmjf3ia1ukIkhuXcCmuKnTud915XEn5UdZzPlDBSoeWfDbGT2VD8OS093K1PltvVMKGIG6eG681YF61HaJVq4t4unteb46aY/640?wx_fmt=png&from=appmsg)

很显然，驱动名就叫 `wesp`。有了这个信息，我们可以在 WinDbg 里查看驱动支持的主功能（major function）分发例程（排版做了调整，便于阅读）：

```
lkd> !drvobj wesp f
Driver object (ffffc0e9fe2e6310) is for:
 \FileSystem\wesp
Driver Extension List: (id , addr)
Device Object list:
Flags: 0x00000012
    0x00000002  DRVO_LEGACY_DRIVER
    0x00000010  DRVO_INITIALIZED

DriverEntry:   fffff80564281000	wesp!DriverEntry
DriverStartIo: 00000000
DriverUnload:  00000000
AddDevice:     00000000
Dispatch routines:
[00] IRP_MJ_CREATE            fffff805d07a14d0	nt!IopInvalidDeviceRequest
[01] IRP_MJ_CREATE_NAMED_PIPE fffff805d07a14d0	nt!IopInvalidDeviceRequest
[02] IRP_MJ_CLOSE             fffff805d07a14d0	nt!IopInvalidDeviceRequest
[03] IRP_MJ_READ              fffff805d07a14d0	nt!IopInvalidDeviceRequest
[04] IRP_MJ_WRITE             fffff805d07a14d0	nt!IopInvalidDeviceRequest
[05] IRP_MJ_QUERY_INFORMATION fffff805d07a14d0	nt!IopInvalidDeviceRequest
[06] IRP_MJ_SET_INFORMATION   fffff805d07a14d0	nt!IopInvalidDeviceRequest
[07] IRP_MJ_QUERY_EA          fffff805d07a14d0	nt!IopInvalidDeviceRequest
[08] IRP_MJ_SET_EA            fffff805d07a14d0	nt!IopInvalidDeviceRequest
…
[0e] IRP_MJ_DEVICE_CONTROL     fffff805d07a14d0	nt!IopInvalidDeviceRequest
[0f] IRP_MJ_INTERNAL_DEVICE_CONTROL fffff805d07a14d0	nt!IopInvalidDeviceRequest
[10] IRP_MJ_SHUTDOWN           fffff805d07a14d0	nt!IopInvalidDeviceRequest
[11] IRP_MJ_LOCK_CONTROL       fffff805d07a14d0	nt!IopInvalidDeviceRequest
[12] IRP_MJ_CLEANUP            fffff805d07a14d0	nt!IopInvalidDeviceRequest
[13] IRP_MJ_CREATE_MAILSLOT    fffff805d07a14d0	nt!IopInvalidDeviceRequest
[14] IRP_MJ_QUERY_SECURITY     fffff805d07a14d0	nt!IopInvalidDeviceRequest
[15] IRP_MJ_SET_SECURITY       fffff805d07a14d0	nt!IopInvalidDeviceRequest
…
[1b] IRP_MJ_PNP                fffff805d07a14d0	nt!IopInvalidDeviceRequest
Device Object stacks:
Processed 0 device objects.
```

从输出看，驱动没有提供任何自己的主功能码处理函数（为省篇幅略去了几行，它们全都指向内核提供的 `IopInvalidDeviceRequest`）；实际上，它连设备对象都没有。这意味着与这个驱动通信没法走经典 DeviceIoControl——那需要先用 `CreateFile`（其实是符号链接）或 `NtOpenFile`（真实设备名）按名字打开设备，而这里根本没有设备可开。我们还看到驱动对象放在对象管理器的 `\FileSystem` 目录下——文件系统 mini-filter 通常就存放在这里。注册表里的 `Type` 值为 2 指向同一个结论：这是一个文件系统类驱动。

我们预期 WESP 驱动会像“标准”EDR 驱动那样注册各种通知。用 PE 查看器打开 wesp.sys 就能看到（截图来自我的工具 Total PE）：

![Total PE 查看 wesp.sys 导入表：FLTMGR.SYS，以及 ntoskrnl.exe 的进程、线程、镜像通知例程](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXIslicOYPy7stNVLTuPxkhEHBbCaY4MbyYdE2aeqnDfzSMjQfPZJ4Ho1gHhzUrQQugeJlVZUM5yB8lYVqYOC5r4tqrNygYqS2Q/640?wx_fmt=png&from=appmsg)

它还依赖 `FltMgr.Sys`——Filter Manager 驱动，负责管理文件系统 mini-filter——这坐实了 wesp.sys 就是一个文件系统 mini-filter。在提升权限的命令行窗口里跑内置的 fltmc 工具，可以进一步验证这个结论：

```
Filter Name                     Num Instances    Altitude    Frame
------------------------------  -------------  ------------  -----
bindflt                              1       409800         0
UCPD                                   5       385250.5       0
wesp                            7       329500         0
WdFilter                         5       328010         0
storqosflt                          0       244000         0
wcifs                           0       189900         0
PrjFlt                           0       189800         0
CldFlt                            1       180451         0
FileCrypt                          0        141100         0
luafv                            1       135000         0
UnionFS                            0       130850         0
bfs                               7       100010         0
npsvctrig                         1        46000         0
Wof                              3        40700         0
FileInfo                          5        40500         0
WinSetupMon                         1        40300         0
```

WESP 出现在列表里，还显示了它的 altitude（altitude 越高的驱动，越先收到通知）。

### wesp.sys 怎么和用户态通信

没...