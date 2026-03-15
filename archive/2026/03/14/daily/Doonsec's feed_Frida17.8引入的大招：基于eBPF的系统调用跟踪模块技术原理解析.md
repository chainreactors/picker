---
title: Frida17.8引入的大招：基于eBPF的系统调用跟踪模块技术原理解析
url: https://mp.weixin.qq.com/s/RYcgkWEWocrKH3QmCHlt4Q
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:54.242324
---

# Frida17.8引入的大招：基于eBPF的系统调用跟踪模块技术原理解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Sq4BUsrXeT9icEN108yyWE38kD6v86RAErDCj3HM1QUzEPsd3fVA8l2gFt1YrtCCk1pXcBOT9ibJzzticjR0E2xMLZ3tmD8ccjKyVeWHU3XQS4/0?wx_fmt=jpeg)

# Frida17.8引入的大招：基于eBPF的系统调用跟踪模块技术原理解析

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器中沉浸阅读

# Frida17.8引入的大招：基于eBPF的系统调用跟踪模块技术原理解析

## ![图片](https://mmbiz.qpic.cn/mmbiz_svg/Hp9HAaP9GFDF2miblYnrDUyJOAnDMA3816E00o98ST65vJ7aVXFNGusNsibYibCDwmROHjAlMDibhrNzzDPA2IdKp27n2d2uCrOn/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 背景

Frida17.8.0（2026年3月9日）将`frida-strace`纳入主线发布。官方发布页给出了Android与iOS的实测命令。本次发布的核心价值在于将系统调用跟踪能力统一收敛到同一套跨平台服务协议。

从实现演进看，17.7.3优先修复了系统调用解码与内存安全边界问题，17.8.0完成协议收敛与Linux eBPF链路增强。本文聚焦`syscall-tracer`主链路与eBPF实现细节，并对关键提交进行归纳分析。

话多说一句，这个功能挺适合用来做样本行为分析的。用来定位反调试与检测也很有用。后面我会用这个功能尝试找样本检测特征。

## 分析范围与方法

分析窗口覆盖`17.7.3..17.8.0`，以`subprojects/frida-core`与`subprojects/frida-tools`为核心。

本文聚焦以下代码落点：

1. Linux内核侧采集：`src/linux/helpers/syscall-tracer.bpf.c`
2. Linux用户态桥接：`src/linux/syscall-tracer.vala`
3. 服务协议层：`src/linux/linux-host-session.vala`内`LinuxSyscallTraceServiceSession`
4. CLI消费层：`frida_tools/stracer.py`

## syscall-tracer总体架构

Frida17.8的系统调用跟踪由四层组成：

1. eBPF采集层 监听`raw_syscalls/sys_enter`和`raw_syscalls/sys_exit`，并用`kprobe/uprobe_mmap`、`kprobe/uprobe_munmap`维护`map_gen`状态。
2. eBPF数据面 通过`syscall_events`和`map_events`两个ringbuf向用户态输出事件。
3. 用户态追踪核心 `SyscallTracer`对象负责拉取ringbuf、解析事件、维护进程映射快照与栈采样索引。
4. 服务与工具 `LinuxSyscallTraceServiceSession`导出统一请求协议，`frida-strace`按协议批量拉取并做展示合并。

该设计的关键点是“采集与展示解耦”：内核仅负责稳定产出结构化事件，交互逻辑全部放在用户态。

## eBPF实现细节

使用Frida脚本可以弄一个frida-strace出来不算难。但基于eBPF实现的官方版本很有看头。主要是eBPF这内核级别的能力过检测怪好用的。

### 1 挂载点选择与触发时机

挂载点的选择兼容了安卓与传统Linux内核。GKI2.0的安卓关掉了FTRACE\_SYSCALLS，要想开启就得编译内核源码并刷机，就光这个很多学员朋友就难弄成功。后面我在eBPF课程的第六季里，所有的系统调用相关的挂载点也使用`sys_enter`了。这样除了效率低那么一点点外，eBPF代码改一下系统调用号的判断处理，整体在Hook功能上其实变化不大。

目前，Frida选择的Linux链路使用三类挂载点：

1. `tracepoint/raw_syscalls/sys_enter`

   在系统调用入口采集调用号、线程信息、入参与部分可安全读取的附件。
2. `tracepoint/raw_syscalls/sys_exit`

   在系统调用返回点采集返回值，并按inflight状态复制输出参数。
3. `kprobe/uprobe_mmap`

   与`kprobe/uprobe_munmap` 追踪进程地址空间变化，驱动`map_gen`递增，给后续符号化提供一致性锚点。

这比纯`sys_enter/sys_exit`多了一层“映射变化追踪”，是Frida这版实现最关键的工程点。

### 2 map设计

`syscall-tracer.bpf.c`里核心map如下：

1. `target_tgids`

   与`target_uids` 目标过滤入口。只有命中目标PID或UID的线程才会被采集。
2. `excluded_syscalls`

   排除表，key为`(abi<<32)|nr`，支持`native/compat32`分离排除。
3. `syscall_events`

   与`map_events` 两个ringbuf，分别承载syscall事件和映射快照事件。
4. `process_states`

   保存`abi`与`map_gen`。用于“当前事件对应`map_gen`”的判定。
5. `stacks`

   `BPF_MAP_TYPE_STACK_TRACE`，配合`bpf_get_stackid()`采样用户栈。
6. `inflight`

   按`tid`记录“enter阶段计划在exit阶段补拷的输出参数”。
7. `stats`

   按CPU统计发射与丢弃字节数、事件数。
8. `scratch_area`

   临时缓冲区，主要用于内核路径拼接。

该map拆分遵循一个原则：将高频路径状态尽量平铺到定长结构，降低验证器与运行时分支复杂度。

### 3 事件结构设计

事件分两大类：

1. Syscall事件

* 公共头：`time_ns`、`tgid`、`tid`、`type`、`attachment_count`
* syscall扩展：`syscall_nr`、`stack_id`、`map_gen`
* enter携带`args[6]`
* exit携带`retval`

2. Map事件

* `NEED_SNAPSHOT`
* `MAP_CREATE`
* `MAP_DESTROY_RANGE`

每个事件后可附加若干`AttachmentHeader+payload`。`AttachmentHeader`明确了`arg_index/capacity/size`，这是17.7.3之后多attachment解析稳定的关键。

### 4 入参与出参采集策略

eBPF对参数采集不是“一刀切”，而是分层处理：

1. 入口直接可读参数 例如`openat`路径、`mount`多路径参数、`connect/bind/sendto`的`sockaddr`，在enter阶段直接拷贝。
2. 需要返回后才有意义的输出参数 例如`readlinkat`输出字符串、`fstat/statx`输出结构体、`recvfrom/accept`输出地址。 这些在enter阶段只登记inflight计划，exit阶段依据返回值与长度再执行`bpf_probe_read_user`。
3. 专门类型解码入口 用户态会按签名尝试把`timespec`、`sockaddr`从bytes转成结构化值。

这种“enter登记，exit补拷”的双阶段模型，能在保证信息完整度的同时，避免在enter路径做过度读取。

### 5 首次进程快照握手

`ensure_process_state()`是整个链路最重要的同步点：

1. 若`process_states`里没有该`tgid`，先插入初始状态。
2. 发出`NEED_SNAPSHOT`到`map_events`。
3. 调用`bpf_send_signal(SIGSTOP)`暂停当前线程。
4. 用户态收到`NEED_SNAPSHOT`后刷新映射快照，并把`map_gen`置为1。
5. 用户态再`SIGCONT`恢复目标线程。

这解决了一个经典问题：如果在没有初始映射快照时就开始做栈符号化，地址到模块的映射会出现系统性错位。

### 6 map\_gen一致性机制

`map_gen`是Frida这版实现里最有工程价值的字段之一： 这里的`map_gen`由`mmap/munmap`变化驱动，与`eBPF Map`容器不是同一概念。

1. 每条syscall事件都携带`map_gen`。
2. `mmap/munmap`

   触发时递增该进程`map_gen`。
3. 用户态符号解析请求会带上`pid+gen+addresses`。

效果是：同一条栈地址在不同`map_gen`下可映射到不同模块视图，避免动态加载场景下“符号飘移”。

### 7 ABI判定与compat32支持

17.8阶段Linux链路把ABI判定前移到内核态：

1. 通过`thread_info.flags`检测`compat32`位。
2. 事件在内核侧即写入`abi`语义并参与排除匹配。
3. 用户态按`native/compat32`签名表分别解码。

这样做避免了旧方案“用户态推测ABI”的竞态与误判。

### 8 排除syscall在内核侧生效

排除规则不是UI过滤，而是采集前过滤：

1. `exclude-syscalls`

   请求写入`excluded_syscalls` map。
2. eBPF在enter/exit入口先查表。
3. 命中后直接返回，不产生事件。

这对高频噪声syscall（如轮询、心跳）很关键，因为它直接减少内核到用户态带宽与ringbuf占用。

### 9 verifier友好化改造

17.8.0前的关键重构目标是“更容易通过verifier”：

1. 减少包装函数层级，降低控制流深度。
2. 对结构体使用显式零初始化（如`Inflight v = {}`）。
3. 对长度变量加掩码与`barrier_var`，让边界推导更确定。
4. 对字符串与buffer复制分支做上限收敛。

配套地，BPF加载日志缓冲区提升到128KiB，能明显改善调试失败时的可观测性。

## 用户态调用链细节

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9WOYOFbxib3TVYxtngFNVY4abMoIqWaC4OUdOp6Fd7ibMfxzhBhkibWR0ibNicF4J1Z2TJ2zdQrPj14Z7xzYicicgGGrOlaNNZaYap9I/640?wx_fmt=png&from=appmsg)

##

### 1 service入口与请求分发

`LinuxHostSession.do_open_service()`收到`syscall-trace`协议后，实例化`LinuxSyscallTraceServiceSession`。

该session支持的核心请求有：

1. `get-signatures`
2. `add-targets`

   与`remove-targets`
3. `exclude-syscalls`
4. `read-events`
5. `resolve-stacks`
6. `resolve-symbols`
7. `read-stats`

`read-events`会返回`events+processes+status`，其中`status`用于指示是否还要继续拉取下一批。

### 2 ringbuf到事件批次

用户态`SyscallTracer`的工作流是：

1. 监听ringbuf可读。
2. 收到`events_available`后触发drain。
3. 把原始二进制事件转成协议Variant。
4. 在`MAX_BATCH_BYTES`限制内打包返回。

这使`frida-strace`能在高吞吐场景下做受控拉取，而不是被动洪泛。

### 3 CLI事件合并与延迟符号化

目前用户态的工具主要是frida-tools中给出的`frida-strace`。它的实现代码`frida_tools/stracer.py`重点做三件事：

1. enter/exit按`(pid,tid,nr)`合并，形成更接近传统strace的单行视图。
2. 对`stack_id`做按需解析，用户滚动到对应事件时再触发`resolve-stacks`和`resolve-symbols`。
3. 支持运行时排除，排除后可同步清理已缓存事件。

该策略在交互体验与性能之间实现了较好的平衡。

## 如何使用eBPF实现同类系统调用跟踪

如果你要自己做一个“Frida风格”的eBPF syscall tracer，可以按下面步骤落地。

1. 定义事件协议并固定字段布局，然后编写eBPF程序 事件字段需要优先稳定，特别是`pid/tid`类型、stack\_id、附件布局。
2. 把“过滤”放在内核入口 PID/UID过滤、syscall排除都应在`sys_enter/sys_exit`入口就生效。
3. 把“输出参数拷贝”拆成enter登记＋exit执行 不要在enter阶段盲拷输出缓冲区。
4. 为符号化准备`map_gen` 引入`map_gen`与映射变化事件，避免地址解析漂移。
5. 做首次快照握手 新进程首次出现时，用`NEED_SNAPSHOT+SIGSTOP/SIGCONT`把初始化过程做成原子阶段。
6. 设计用户态服务协议 至少要有`read-events`、`resolve-stacks`、`resolve-symbols`、`read-stats`。
7. 最后再做CLI交互 交互层只负责展示与检索，不要把核心状态机放在CLI。

一个简化伪代码如下：

```
// eBPF侧简化流程
on_sys_enter(ctx) {
if (!target_match()) return;
    abi = detect_abi();
if (excluded(abi, nr)) return;

if (!ensure_process_state_and_snapshot()) return;

    ev = reserve_event();
    fill_common(ev, ENTER, nr, map_gen, stack_id);
    fill_args(ev, ctx);
    schedule_inflight_if_needed(tid, nr, ctx);
    submit(ev);
}

on_sys_exit(ctx) {
if (!target_match()) return;
    abi = detect_abi();
if (excluded(abi, nr)) return;

if (!ensure_process_state_and_snapshot()) return;

    ev = reserve_event();
    fill_common(ev, EXIT, nr, map_gen, stack_id);
    fill_retval(ev, ctx->ret);
    maybe_copy_out_args_from_inflight(ev, tid, nr, ctx->ret);
    submit(ev);
}
```

## 实战使用

最小命令：

```
frida-strace -U -f com.example.app
```

多目标与排除示例：

```
frida-strace -U -f com.a -x futex -x epoll_wait
```

常用调试思路：

1. 先不做符号化，只看syscall序列与关键参数。
2. 锁定可疑调用后再展开stack解析。
3. 对高频噪声调用进行排除，随后观察有效信号。

## 总结

Frida17.8的`syscall-tracer`并非简单的系统调用打印工具，而是形成了一套可扩展的跟踪基础设施：

1. 内核侧有过滤、有双阶段参数采集、有版本一致性。
2. 用户态有快照握手、有批量协议、有按需符号化。
3. 工具侧有合并显示、有动态排除、有交互可操作性。

## 参考链接

1. Frida17.7.3发布说明：https://frida.re/news/2026/02/16/frida-17-7-3-released/
2. Frida17.8.0发布说明：https://frida.re/news/2026/03/09/frida-17-8-0-released/
3. Frida主仓库：https://github.com/frida/frida

## 附录：frida-strace执行时序图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT9fPrydsV9Xubq9TO5AmjuEZWdk1ggOnGLIVibHzlucNEqJnt4HicgTo6zeZsGEcpT1acOfXCkgKiawBKc9bqeoLV7Vqlco85TaxY/640?wx_fmt=png&from=appmsg)

##

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmib...