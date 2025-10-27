---
title: 构建并运行 eBPF 应用 - Part one
url: https://cloudsjhan.github.io/2024/07/14/%E6%9E%84%E5%BB%BA%E5%B9%B6%E8%BF%90%E8%A1%8C-eBPF-%E5%BA%94%E7%94%A8-Part-one/
source: cloud world
date: 2024-07-15
fetch_date: 2025-10-06T17:40:22.028019
---

# 构建并运行 eBPF 应用 - Part one

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 构建并运行 eBPF 应用 - Part one

posted

2024-07-14

|

in

[eBPF](/categories/eBPF/)

|

visitors:

|

|

wordcount:

2,308
|

min2read ≈

11

![](https://)

本文将介绍如何使用 C 和 Golang 编写第一个 eBPF 程序。我们将在第一部分介绍实际的 eBPF 程序，在第二部分介绍用户空间应用程序。

### 准备工作

本文运行的操作系统是：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` OS: Ubuntu 22.04 Linux Header Version: 6.5.0–14-generic ``` |

还通过 apt 安装了一些依赖项:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo apt-get -y install libbpf bpfcc-tools ``` |

完成 ebpf 的代码除了需要 Go 的知识之外，读者对 C 语言编程需要熟悉。

### [什么是 eBPF](https://ebpf.io/what-is-ebpf/#what-is-ebpf "what-is-ebpf")？

有许多博客/网站对 eBPF 进行了深入探讨（请查看资源部分），但为了简单起见，我们姑且认为 eBPF 是一种在不修改内核源代码的情况下使用模块扩展 Linux 内核的方法。

笔者认为 eBPF 就是是内核的一个钩子，允许在内核空间运行逻辑。

### User Space vs Kernel Space

当我们谈论内核空间时，通常指的是操作系统。这是一个特权区域，可以完全访问硬件和软件资源。当我们谈论用户空间时，这里通常是你运行日常程序（如谷歌浏览器）的地方。用户空间的访问权限是有限制的。

### 选择要挂钩的事件

这里给大家推荐一个学习上手开发 eBPF 的好的项目：[kepler](https://github.com/sustainable-computing-io/kepler/tree/main "kepler github")
Kepler 的一项工作是通过 CPU 计划切换，计算每个进程（由 PID 标识）使用 CPU 的时间。

[CPU 调度](https://www.studytonight.com/operating-system/cpu-scheduling "cpu-scheduling")是指在正在执行的进程之间进行切换，以便更好地利用处理能力（当一个进程受阻时，CPU 会暂停处理该进程，并切换到另一个进程）。

因此，如果我们想复制这一功能，我们可以这样做：

* 知道某个进程何时将开始使用 CPU
* 知道某个进程何时停止使用 CPU
* 计算这两个时刻之间的时间

这样我们就能大致估算出每个流程需要多少时间，同时要记住，一个流程会被安排多次。

根据上述信息，我们希望:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` tracepoint/sched/sched_switch ``` |

事件，以便在计划进程时收到通知。

### 了解 event 的格式

在 BPF 事件中，每个事件在运行函数时都会包含一些称为 “上下文 “的内容。这些上下文实质上就是事件发出的信息。我们需要定义一个 C 结构来保存这些信息，但首先，我们需要获得该结构的格式。我们可以通过运行下面的代码来实现：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` $ sudo cat /sys/kernel/debug/tracing/events/sched/sched_switch/format name: sched_switch ID: 327 format: field:unsigned short common_type; offset:0; size:2; signed:0; field:unsigned char common_flags; offset:2; size:1; signed:0; field:unsigned char common_preempt_count; offset:3; size:1; signed:0; field:int common_pid; offset:4; size:4; signed:1; field:char prev_comm[16]; offset:8; size:16; signed:0; field:pid_t prev_pid; offset:24; size:4; signed:1; field:int prev_prio; offset:28; size:4; signed:1; field:long prev_state; offset:32; size:8; signed:1; field:char next_comm[16]; offset:40; size:16; signed:0; field:pid_t next_pid; offset:56; size:4; signed:1; field:int next_prio; offset:60; size:4; signed:1; print fmt: "prev_comm=%s prev_pid=%d prev_prio=%d prev_state=%s%s ==> next_comm=%s next_pid=%d next_prio=%d", REC->prev_comm, REC->prev_pid, REC->prev_prio, (REC->prev_state & ((((0x00000000 | 0x00000001 | 0x00000002 | 0x00000004 | 0x00000008 | 0x00000010 | 0x00000020 | 0x00000040) + 1) << 1) - 1)) ? __print_flags(REC->prev_state & ((((0x00000000 | 0x00000001 | 0x00000002 | 0x00000004 | 0x00000008 | 0x00000010 | 0x00000020 | 0x00000040) + 1) << 1) - 1), "|", { 0x00000001, "S" }, { 0x00000002, "D" }, { 0x00000004, "T" }, { 0x00000008, "t" }, { 0x00000010, "X" }, { 0x00000020, "Z" }, { 0x00000040, "P" }, { 0x00000080, "I" }) : "R", REC->prev_state & (((0x00000000 | 0x00000001 | 0x00000002 | 0x00000004 | 0x00000008 | 0x00000010 | 0x00000020 | 0x00000040) + 1) << 1) ? "+" : "", REC->next_comm, REC->next_pid, REC->next_prio ``` |

要处理的信息相当多，但为了简单起见，我们可以说，在这个用例中，我们不需要关心任何以 common\_ 为前缀的字段。这样我们就有了以下字段：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` char prev_comm[16]; pid_t prev_pid; int prev_prio; long prev_state; char next_comm[16]; pid_t next_pid; int next_prio; ``` |

然后我们就可以利用这些信息创建下面的 C 结构：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` struct sched_switch_args {   char prev_comm[16];   int prev_pid;   int prev_prio;   long prev_state;   char next_comm[16];   int next_pid;   int next_prio; }; ``` |

现在，首先要注意的是，我将 pid\_t 类型改为 int。这是因为 pid\_t 的底层类型是 int。我们可以使用 pid\_t 类型，但需要依赖 sys/types.h，而在本例中我们并不需要。有关这方面的更多信息，可以阅读[这篇文章](https://ftp.gnu.org/old-gnu/Manuals/glibc-2.2.3/html_node/libc_554.html#:~:text=The%20pid_t%20data%20type%20is,Function%3A%20pid_t%20getppid%20%28void%29 "glibc-223")。

### 创建 BPF Map

要从内核空间收集数据并在用户空间访问这些数据，我们需要使用一种叫做 BPF 映射的东西。BPF 映射是推送到用户空间的数据结构。在本例中，我们将使用基于 PID 的哈希表类型。这需要我们创建三个结构，即:

* 通过 key struct 识别数据

  |  |  |
  | --- | --- |
  | ``` 1 2 3 4 5 6 ``` | ``` struct key_t {   // This is the process ID   // which we will use to identify   // in the hash map   __u32 pid; }; ``` |
* 存储数据的方式是 value struct

  |  |  |
  | --- | --- |
  | ``` 1 2 3 4 5 6 ``` | ``` struct val_t {   // used to understand the start time of the process   __u64 start_time;   // used to store the elapsed time of the process   __u64 elapsed_time; }; ``` |
* eBpf HashMap 将他们联系在一起

  |  |  |
  | --- | --- |
  | ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` struct {   // The type of BPF map we are creating   __uint(type, BPF_MAP_TYPE_HASH);   // specifying the type to be used for the key   __type(key, struct key_t);   // specifying the type to be used as the value   __type(value, struct val_t);   // max amount of entries to store in the map   __uint(max_entries, 10240);   // name of the map as well as a section macro   // from the bpf lib to designate this type   // as a BPF map } process_time_map SEC(".maps"); ``` |

我已经添加了注释，解释这些结构中每一行的作用。

### 创建 eBPF 函数

最后一步是创建 eBPF 函数。为此，我们需要一个 eBPF 程序。
这是一个 C 语言函数，带有一些宏标识，这样我们就可以使用先前定义的类型进行交互，例如:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` | ``` SEC("tracepoint/sched/sched_switch") int cpu_processing_time(struct sched_switch_args *ctx) {   // get the current time in ns   __u64 ts = bpf_ktime_get_ns();   // we need to check if the process is in our map   struct key_t prev_key = {     .pid = ctx->prev_pid,   };   struct val_t *val = bpf_map_lookup_elem(&process_time_map, &prev_key);   // if the previous PID does not exist it means that we just started   // watching or we missed the start somehow   // so we ignore it for now   if (val) {   // Calculate and store the elapsed time for the process and we reset the   // start time so we can measure the next cycle of that process     __u64 elapsed_time = ts - val->start_time;     struct val_t new_val = {.start_time = ts, .elapsed_time = elapsed_time};     bpf_map_update_elem(&process_time_map, &prev_key, &new_val, BPF_ANY);     return 0;   };   // we need to check if the next process is in our map   // if it's not we need to set initial time   struct key_t next_key = {   .pid = ctx->next_pid,   };   struct val_t *next_val = bpf_map_lookup_elem(&process_time_map, &prev_key);   if (!next_val) {     struct val_t next_new_val = {.start_time = ts};     bpf_map_update_elem(&process_time_map, &next_key, &next_new_val, BPF_ANY);     return 0;   }   return 0; } ``` |

下面的宏指定了该函数要连接的事件。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` SEC("tracepoint/sched/sched_switch") ``` |

这一行就是我们查找 BPF 映射数据的方法。我们使用一个唯一的键，并将其传递给 bpf\_map\_lookup\_elem 函数，该函数将返回一个 val\_t 类型的值（我们之前定义的）。如果该键下没有值，该函数将返回 NULL，请注意我们需要将 BPF 映射类型作为 &process\_time\_map 传递。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` struct val_t *val = bpf_map_lookup_elem(&process_time_map, &prev_key); ``` |

这一行是我们向 BPF 地图添加数据的过程。我们将传递键（本例中为 &prev\_key）和键值（&new\_val），后者将把该值存储到 BPF 映射中。请再次注意，我们传递的是映射类型。BPF\_ANY 用于将键更新为新值，或者在键不存在时创建新值（参见[文档](https://man7.org/linux/man-pages/man2/bpf.2.html)）。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` bpf_map_update_elem(&process_time_map, &prev_key, &new_val, BPF_ANY); ``` |

这样，我们就完成了功能，不过，我们还需要在代码中添加最后一行：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` char _license[] SEC("license") = "Dual MIT/GPL"; ``` |

由于 eBPF 是以 GPL 许可的，这意味着所有集成软件也需要与 GPL 兼容。如果没有这一行，就无法将代码加载到内核中。
因此，我们的最终代码片段如下（我添加了需要包含的 C 头文件）:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``` | ``` #include <linux/sched.h> #include <linux/bpf.h> #include <bpf...