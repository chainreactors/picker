---
title: 在 Android 中开发 eBPF 程序学习总结（一）
url: https://www.anquanke.com/post/id/282737
source: 安全客-有思想的安全新媒体
date: 2022-11-08
fetch_date: 2025-10-03T21:54:04.564108
---

# 在 Android 中开发 eBPF 程序学习总结（一）

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

# 在 Android 中开发 eBPF 程序学习总结（一）

阅读量**375267**

发布时间 : 2022-11-07 15:00:25

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

<https://paper.seebug.org/2003/>
最近在研究eBPF，做一下学习笔记。

## 起因

其实是想学习一下[ecapture](#jump1)是怎么实现的，但是实际在我`xiaomi 10`手机上测试的过程中（已经有root权限）发现，并没办法运行，因为`ecapture`需要内核开启`CONFIG_DEBUG_INFO_BTF`，这个配置信息可以通过`/proc/config.gz`中来查看是否开启。

我的手机的内核版本是4.19，没有开启BTF，但是BPF是开启了的，接着我继续查看`ecapture`的文档，说如果内核没有开启`BTF`，需要使用`make nocore`编译，在github上有提供直接编译好的`nocore`安卓版，但是测试还是运行不了。接着自己编译了一波，但是仍然失败，感觉可能得严格按文档所述，需要内核版本大于等于5.4。

那么我的手机就没办法运行BPF程序了吗？接着，就开启了我的研究。

## Android BPF demo

在网上搜相关的学习资料，BPF相关的资料本身就挺少的，再过滤一下只限制Android平台，就更少了。

而且大部分能搜到的中文资料，都是一堆废话，或者一堆ctrl+c, ctrl+v的文章，实际有用的太少了。安卓官方的资料中也只有一个简单的demo，而且使用的是Android.bp进行编译的，还需要本地搭建AOSP环境。

### AOSP环境搭建

这破环境真是绝了，挂上daili，我装了一个晚上还没好（速度也有4Mb/s了）。然后第二天搜到了能换国内源，下面放一下我的搭建环境的命令：

```
$ apt-get install -y repo
$ export EPO_URL='https://gerrit-googlesource.proxy.ustclug.org/git-repo'
$ repo init -u git://mirrors.ustc.edu.cn/aosp/platform/manifest -b android-12.1.0_r26
$ repo sync -c -j8
```

简单的几句命令就好了，但是要注意，内存建议大于16G，硬盘最好200G以上。

### 使用AOSP环境编译程序

```
# 初始化一下环境变量
$ source build/envsetup.sh
# 初始化一下你想编译哪个版本的android程序
$ lunch aosp_crosshatch-userdebug
```

接着后续的测试代码可以参考[测试代码](#jump2)，该文章中的代码，在我测试的过程中，没有啥问题，是能正常运行的，但是在第一次编译的时候，可能是AOSP架构的问题，会把整个项目都先编译一次，我安卓也搞的不多，也不知道如果只编译指定项目。不过在第一编译之后，后续只需要使用`m name`，就可以只编译指定项目了。也是因为要编译整个项目，如果内存小于16G，是会编译失败的，如果本身内存不够，可以增加一下交换分区的大小。

## Android上的BPF

通过这个demo，能看出来，android下使用BPF程序的步骤如下：

> 首先把编译好的bpf.o程序放到`/system/etc/bpf/`目录下，这就要求我们需要有`/system`目录的可写权限，但是在我的手机上，就算有root权限了，`system`目录也没办法写。所以我把手机的系统从MIUI12，刷成了`evolution x`系统，然后通过`adb shell mount -o rw,remount /`来重新挂载根目录，这样就能写`/system/etc/bpf`目录了。
> 使用`bpfloader`程序，会自动加载`/system/etc/bpf`目录下的`*.o`文件，然后会在`/sys/fs/bpf`目录生成相应的`prog_xxx`和`map_xx`文件。
> 我们自己的loader文件需要通过`/sys/fs/bpf`目录下的那两个文件来和BPF程序进行交互。

## 深入研究Android下的BPF

我根据Linux下的eBPF文件的资料，自己写了一个DEMO：

BPF程序bpftest.c

```
#include <linux/bpf.h>
#include <stdbool.h>
#include <stdint.h>
#include <bpf_helpers.h>
#include <string.h>

#define MAX_ARGV 128;

#define bpf_printk(fmt, args...) bpf_trace_printk(fmt, sizeof(fmt), ##args)

struct event_execv
{
    uint32_t pid;
    uint32_t gid;
    char cmd[80];
};

DEFINE_BPF_MAP(execve_map, ARRAY, uint32_t, struct event_execv, 256);

struct execve_args
{
    short common_type;
    char common_flags;
    char common_preempt_count;
    int common_pid;
    long __syscall_nr;
    unsigned long args[6];
};

SEC("tracepoint/raw_syscalls/sys_enter")
int trace_execve_event(struct execve_args *ctx)
{
    struct event_execv event;
    uint32_t key = 1;
    int comm;
    char trace_buf[] = "[Debug] pid = %d, gid = %d, comm=%s\n";
    memset(&event, 0, sizeof(event));
    event.pid = bpf_get_current_pid_tgid();
    event.gid = bpf_get_current_uid_gid();

    bpf_execve_map_update_elem(&key, &event, BPF_ANY);
    comm = bpf_get_current_comm(&event.cmd, sizeof(event.cmd));
    if (comm != 0)
    {
        return -1;
    }
    event.cmd[79] = 0;
    bpf_printk(trace_buf, event.pid, event.gid, event.cmd);
    bpf_execve_map_update_elem(&key, &event, BPF_ANY);
    return 0;
}

LICENSE("GPL");
```

### map映射

`DEFINE_BPF_MAP`是对map相关操作的一个宏定义，可以参考：[bpf\_helpers.h](#jump3)

```
#define DEFINE_BPF_MAP_NO_ACCESSORS(the_map, TYPE, TypeOfKey, TypeOfValue, num_entries) \
    struct bpf_map_def SEC("maps") the_map = {                                          \
            .type = BPF_MAP_TYPE_##TYPE,                                                \
            .key_size = sizeof(TypeOfKey),                                              \
            .value_size = sizeof(TypeOfValue),                                          \
            .max_entries = (num_entries),                                               \
    };

#define DEFINE_BPF_MAP(the_map, TYPE, TypeOfKey, TypeOfValue, num_entries)                 \
    DEFINE_BPF_MAP_NO_ACCESSORS(the_map, TYPE, TypeOfKey, TypeOfValue, num_entries)        \
                                                                                           \
    static inline __always_inline __unused TypeOfValue* bpf_##the_map##_lookup_elem(       \
            TypeOfKey* k) {                                                                \
        return unsafe_bpf_map_lookup_elem(&the_map, k);                                    \
    };                                                                                     \
                                                                                           \
    static inline __always_inline __unused int bpf_##the_map##_update_elem(                \
            TypeOfKey* k, TypeOfValue* v, unsigned long long flags) {                      \
        return unsafe_bpf_map_update_elem(&the_map, k, v, flags);                          \
    };                                                                                     \
                                                                                           \
    static inline __always_inline __unused int bpf_##the_map##_delete_elem(TypeOfKey* k) { \
        return unsafe_bpf_map_delete_elem(&the_map, k);                                    \
    };
```

比如我上面的代码为：`DEFINE_BPF_MAP(execve_map, ARRAY, uint32_t, struct event_execv, 256);`

我的map\_name为`execve_map`，所以这个宏定义帮我定义了`bpf_execve_map_update_elem`这类的函数，帮我定义了结构体：

```
struct bpf_map_def SEC("maps") execve_map = {
            .type = BPF_MAP_TYPE_##TYPE,
            .key_size = sizeof(TypeOfKey),
            .value_size = sizeof(TypeOfValue),
            .max_entries = (num_entries),
    };
```

并且在`/sys/fs/bpf`目录下生成的map文件的结构为：`map_(bpf文件名)_(定义的map_name)`，假如我编译的bpf文件名为：`bpftest.o`，放到`/system/etc/bpf/`目录下，那么在`/sys/fs/bpf`目录下生成的为：`map_bpftest_execve_map`。

map可以理解为，内核中的BPF和用户态之间的接口，在内存中是以键值对的形式存在的，按我理解，key和value的类型也是可以自己定义的，可以是int，指针，字符串，或者结构体，因为对于BPF来说，key和value就是内存中的一段值，只需要定义好key和value的size就好了，而在上面的结构体中就定义了key和value的大小。

用户态的loader可以通过`/sys/fs/bpf/map_bpftest_execve_map`和BPF程序来交换数据。

### BPF函数编写

这块知识的文章挺多的，在BPF的函数定义的上头都需要有一个`SEC("xxxx")`，在最开始的demo中还有另一个写法，以下两种写法是等同的：

```
SEC("tracepoint/sched/sched_switch")
int tp_sched_switch(struct switch_args* args)
{
......
}

DEFINE_BPF_PROG("tracepoint/sched/sched_switch", AID_ROOT, AID_NET_ADMIN, tp_sched_switch) (struct switch_args* args) {
......
}
```

SEC里面的字符串是为了定义下面的函数是什么类型的BPF程序，因为BPF程序也有很多中类型，比如`kprobe, kretprobe, uprobe, uretprobe, tracepoint......`。

具体都有啥，可以参见：[libbpf.c](#jump4)

再低一点的版本这个结构体的名字叫`section_names`，不过在我研究了一波之后，我感觉不能通过内核版本来确定我们可以用哪个`section`，需要通过`/sys/kernel/debug/`目录下的情况来确定，但是安卓手机上的情况却有一些不同，目录为: `/sys/kernel/tracing/`，比如我上面代码中的：`SEC("tracepoint/raw_syscalls/sys_enter")`，是因为有以下目录：`/sys/kernel/tracing/events/raw_syscalls/sys_enter/`，并且`struct execve_args`结构体是来源于：`/sys/kernel/tracing/events/raw_syscalls/sys_enter/format`

目前这种方式我觉得只适用于`tracepoint`，其他的还没研究到，后续研究到了再补充。

再android上，`/sys/fs/bpf/prog_xx`的命名方式为：`prog_(文件名)_(section名)_(分类，分类名之类的)`

比如我的代码中，文件名为`bpftest`，section名为`tracepoint`，tracepoint的分类为`raw_syscalls`，分类名为`sys_enter`，所以最后得到的文件为：`/sys/fs/bpf/prog_bpftest_tracepoint_raw_syscalls_sys_enter`

### BPF相关函数

bpf的相关函数可以参考`bpf_helper_defs.h`文件，比如上述的`bpf_get_current_pid_tgid`，表示获取触发该BPF的程序的pid，`bpf_get_current_uid_gid`是获取用户的gid，`bpf_get_current_comm`是获取程序名，还有其他的可以自行去看这个头文件的定义。

### 日志调试

BPF提供一个`bpf_trace_printk`函数来打印调试信息，在android下，可以使用atrace命令来读取。

并且我通过strace对atrace进行跟踪发现，其实只需要执行下面两句命令：

```
$ echo 1 > /sys/kernel/tracing/tracing_on
$ cat /sys/kernel/tracing/trace_pipe
```

我在想，通过这个调试信息，好想也能把BPF的数据传送给用户态的loader程序。

## 参考

1. <https://github.com/ehids/ecapture>
2. <https://zhuanlan.zhihu.com/p/482266243>
3. <https://github.com/omnirom/android_system_bpf/blob/0706429da9a9fb15d93d8ed...