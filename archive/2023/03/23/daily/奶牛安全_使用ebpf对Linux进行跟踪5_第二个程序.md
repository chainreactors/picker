---
title: 使用ebpf对Linux进行跟踪5:第二个程序
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488565&idx=1&sn=12908409ea749e226396640f221e180f&chksm=fdf97f20ca8ef636d8d0b26af0ad099c1264bc49c8abde6fae43dc99d12d359816b41b8d8a4c&scene=58&subscene=0#rd
source: 奶牛安全
date: 2023-03-23
fetch_date: 2025-10-04T10:22:57.115455
---

# 使用ebpf对Linux进行跟踪5:第二个程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbzS1uB63gPoMQtCibjKLZ8D3IkDXwXNKjCiacDTl9eaibdaicFSnkn2E9wJ2ECO6nDNjLIX5seHH8iaacA/0?wx_fmt=jpeg)

# 使用ebpf对Linux进行跟踪5:第二个程序

原创

debugeeker

奶牛安全

在这个例子，尝试跟踪一下`execve`系统调用，看能够获取什么有意思的信息。

在每一个事件，我们希望获取到这些数据：

1. 时间戳
2. 进程ID
3. 执行程序名称
4. `execve`在内核执行的时间

按照前一篇文章的办法，可以很容易获取到前面三个字段。第四个字段怎么获取呢？

在前一篇文章里，在`kprobe`事件挂钩，这只是用于函数开始执行时的场景。而跟踪这系列第一篇文章，还有`kretprobe`用于挂钩函数返回的场景,可以通过它来获取`execve`返回时的时间。

当然，把这两次事件放到用户态来对比也可以获取`execve`在内核执行的时间，但在内核里处理会更快。

为了保存开始时间，使用`BPF_HASH(name,key,value)`，`key`是进程ID，而`value`是开始时间戳。

```
#!/usr/bin/python

from bcc import BPF
from sys import exit

# Define BPF program
bpf_txt = """

#include <linux/sched.h>

// Default key value is u64, but PID is u32
BPF_HASH(start, u32);

BPF_PERF_OUTPUT(events);

struct data_t {
    u32 pid;
    u64 ts;
    char comm[TASK_COMM_LEN];
    u64 exe_time;
};

int start_execve(struct pt_regs *ctx) {
    u64 ts;
    u32 pid;

    // Get PID and timestamp (in ns)
    pid = bpf_get_current_pid_tgid();
    ts = bpf_ktime_get_ns();

    // Save the start time (with key=PID) and return
    start.update(&pid, &ts);
    return 0;
}

int end_execve(struct pt_regs *ctx) {
    u64 *tsp, ts, delta;
    struct data_t data = {};

    // Get PID and end timestamp (in ns)
    data.pid = bpf_get_current_pid_tgid();
    ts = bpf_ktime_get_ns();

    // Get the process's name
    bpf_get_current_comm(&data.comm, sizeof(data.comm));

    // Lookup start time for corresponding PID
    tsp = start.lookup(&data.pid);
    if (tsp != NULL) {

        // Start time is also the timestamp, find delta
        data.ts = *tsp;
        data.exe_time = ts - *tsp;

        // Delete the hash entry and submit data
        start.delete(&data.pid);
        events.perf_submit(ctx, &data, sizeof(data));
    }

    return 0;
}
"""

def handle_event(cpu, data, size):
    output = bpf_ctx["events"].event(data)
    print("%-18d %-16s %-6d %-16d" %
        (output.ts, output.comm, output.pid, output.exe_time))

# Load BPF program
bpf_ctx = BPF(text=bpf_txt)
event_name = bpf_ctx.get_syscall_fnname("execve")
bpf_ctx.attach_kprobe(event="event_name", fn_name="start_execve")
bpf_ctx.attach_kretprobe(event="event_name", fn_name="end_execve")

# Print header
print("%-18s %-16s %-6s %-16s" %
    ("TIME(ns)", "COMM", "PID", "EXE TIME(ns)"))

# Open perf "events" buffer
bpf_ctx["events"].open_perf_buffer(handle_event)

# Poll for events
while 1:
    try:
        bpf_ctx.perf_buffer_poll()
    except KeyboardInterrupt:
        print()
        exit(1)
```

结果输出：

```
TIME(ns)           COMM             PID    EXE TIME(ns)
442209714069764    ls               55937  201051
442222059918600    df               55950  197757
442227147857252    lscpu            55955  186674
442236219753381    ip               55963  166857
442244634509346    unix_chkpwd      55972  385405
442244644602391    sh               55973  563984
442244645938214    logrotate        55973  345753
```

和前一篇文章的例子不一样的地方：

1. 改造了`struct data_t data`，增加了一些字段：进程ID，时间戳，执行程序名称和执行时间
2. `start_execve`获取`execve`开始执行时的信息，而`end_execve`获取`execve`结束执行的信息
3. `BPF_HASH(start, u32)`定义一个`hash`映射，用于存放`pid`和时间戳
4. `bpf_get_current_pid_tgid`获取进程ID（低32位，内核态的进程ID）和线程组ID（高32位，用户态看到的进程ID），这里只拿内核态进程ID
5. `bpf_ktime_get_ns`获取以纳秒为单位的时间戳
6. `bpf_get_current_comm`获取当前进程名称
7. `start.lookup`，`start.delete`,`start.update`对hash映射操作
8. `attach_kretprobe`对函数返回进行挂钩

在这基础上，能否提取更多的信息呢？

`execve`系统调用的实现如下：

```
SYSCALL_DEFINE3(execve,
        const char __user *, filename,
        const char __user *const __user *, argv,
        const char __user *const __user *, envp)
{
    return do_execve(getname(filename), argv, envp);
}
```

可以看到，可以进一步获取`execve`的参数和运行结果。

```
#!/usr/bin/python

from bcc import BPF

# Define BPF program
bpf_txt = """

#include <linux/sched.h>

// Default key value is u64, but PID is u32
BPF_HASH(start, u32);

BPF_PERF_OUTPUT(events);
BPF_PERF_OUTPUT(args);

#define ARGSIZE 128
#define MAXARGS 8

struct args {
    char argv[ARGSIZE];
};

struct data_t {
    u32 pid;
    u64 ts;
    char comm[TASK_COMM_LEN];
    u64 exe_time;
    int retval;
};

int start_execve(struct pt_regs *ctx,
    const char __user *filename,
    const char __user *const __user *__argv,
    const char __user *const __user *__envp) {

    u64 ts;
    u32 pid;
    struct args arg_data = {};

    // Get PID and timestamp (in ns)
    pid = bpf_get_current_pid_tgid();
    ts = bpf_ktime_get_ns();

    // Save the start time (with key=PID) and return
    start.update(&pid, &ts);

    // Get full filepath for command
    bpf_probe_read_user(&arg_data.argv, sizeof(arg_data.argv), (void *)filename);
    args.perf_submit(ctx, &arg_data, sizeof(arg_data));

    // Read arguments (up to MAXARGS arguments)
    #pragma unroll
    for (int i = 1; i < MAXARGS; i++) {
        const char *argp = NULL;
        bpf_probe_read_user(&argp, sizeof(argp), (void *)&__argv[i]);
        if (argp) {
            bpf_probe_read_user(&arg_data.argv, sizeof(arg_data.argv), (void *)(argp));
            args.perf_submit(ctx, &arg_data, sizeof(arg_data));
        }
        else break;
    }

    return 0;
}

int end_execve(struct pt_regs *ctx) {
    u64 *tsp, ts, delta;
    struct data_t data = {};

    // Get PID and end timestamp (in ns)
    data.pid = bpf_get_current_pid_tgid();
    ts = bpf_ktime_get_ns();

    // Get the process's name
    bpf_get_current_comm(&data.comm, sizeof(data.comm));

    // Lookup start time for corresponding PID
    tsp = start.lookup(&data.pid);
    if (tsp != NULL) {

        // Start time is also the timestamp, find delta
        data.ts = *tsp;
        data.exe_time = ts - *tsp;

        // Delete the hash entry and submit data
        start.delete(&data.pid);

        // Save return value of execve
        data.retval = PT_REGS_RC(ctx);

        events.perf_submit(ctx, &data, sizeof(data));
    }

    return 0;
}
"""

argvs = ""

def arg_builder(cpu, data, size):
    global argvs
    output = bpf_ctx["args"].event(data)
    argvs = argvs + output.argv + " "

def handle_event(cpu, data, size):
    global argvs
    output = bpf_ctx["events"].event(data)
    print("%-18d %-16s %-6d %-10d %-35s %-5d" %
        (output.ts, output.comm, output.pid, output.exe_time, argvs, output.retval))
    argvs = ""

# Load BPF program
bpf_ctx = BPF(text=bpf_txt)
event_name = bpf_ctx.get_syscall_fnname("execve")
bpf_ctx.attach_kprobe(event="event_name", fn_name="start_execve")
bpf_ctx.attach_kretprobe(event="event_name", fn_name="end_execve")

# Print header
print("%-18s %-16s %-6s %-10s %-35s %-5s" %
    ("TIME(ns)", "COMM", "PID", "EXE TIME", "ARGS", "RETVAL"))

# Open perf "events" buffer
bpf_ctx["events"].open_perf_buffer(handle_event)
bpf_ctx["args"].open_perf_buffer(arg_builder)

# Poll for events
while 1:
    try:
        bpf_ctx.perf_buffer_poll()
    except KeyboardInterrupt:
        print()
        exit()
```

结果

```
TIME(ns)           COMM          PID    EXE TIME   ARGS                           RETVAL
680084610622215    ls            53036  258291     /bin/ls --color=auto -a             0
680088120119237    ls            53039  150290     /bin/ls --color=auto /tmp -lrt      0
680095079987477    ps            53046  191785     /bin/ps -aA                         0
```

这次实现有些不一样的东西：

* `BPF_PERF_OUTPUT(args)`建立一个新表，输出`execve`参数。
* `start_execve`的参数扩展了，除了第一个之外，和`execve`在系统调用的一样了，这样可以获取更多参数。
* `PT_REGS_RC(ctx)`用于获取上下文返回值

暗号：fbb4e

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

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