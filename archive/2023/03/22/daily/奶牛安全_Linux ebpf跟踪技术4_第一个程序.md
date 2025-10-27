---
title: Linux ebpf跟踪技术4:第一个程序
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488559&idx=1&sn=2fcba659e766b505bb39168a2723fcac&chksm=fdf97f3aca8ef62c51193d2706475465df25d116a70a45b78402d7f715525ea205032f8ae731&scene=58&subscene=0#rd
source: 奶牛安全
date: 2023-03-22
fetch_date: 2025-10-04T10:15:59.765321
---

# Linux ebpf跟踪技术4:第一个程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwDTB48r6TM5adbqSbQniblklQIqu1zCWvunomuEDNozBfEw38V7AEsrEQWmQV9xlb4BA2VzyCe19g/0?wx_fmt=jpeg)

# Linux ebpf跟踪技术4:第一个程序

原创

debugeeker

奶牛安全

[Linux ebpf跟踪技术1：Linux跟踪技术纵览](http://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488110&idx=1&sn=58139c5db600b518c81c0e837b42fffb&chksm=fdf9797bca8ef06d0bf8e3678f63af11261f63be89910dc5fce2c025e363795da2f01a4eaf3a&scene=21#wechat_redirect)

[Linux ebpf跟踪技术2：BCC介绍](http://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488117&idx=1&sn=77dc597d0ccad3f145b0169849be7b61&chksm=fdf97960ca8ef0763d625dc09f828f13cfc28304b527861dd22d3aeffc4b76ec58059c2aa25a&scene=21#wechat_redirect)

[Linux ebpf跟踪技术3：BCC工具开发提示](http://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488122&idx=1&sn=62f22e6a5bb0079319833dfb2e45c130&chksm=fdf9796fca8ef079728f25897d4b682d75535a704d1d8036afc6296b539d8bf5141c1d8b5b9b&scene=21#wechat_redirect)

第一个程序是使用`kprobe`挂钩到`sys_sync`系统调用。第一次实现时，先用`bpf_trace_printk`把跟踪结果输出到用户态。

## 使用`bpf_trace_printk`

这个程序作用是：当用户每次执行`sync`命令，它就会打印出`hello world`。

```
#!/usr/bin/python

from bcc import BPF
import

# Define BPF program
bpf_txt = """

int hello_world_printk(void *ctx) {
   bpf_trace_printk("Hello World!\\n");
   return 0;
}
"""

# Load BPF program
bpf_ctx = BPF(text=bpf_txt)
bpf_ctx.attach_kprobe(event=bpf_ctx.get_syscall_fnname("sync"),
   fn_name="hello_world_printk")

# Print header
print("%s" % "MESSAGE")

# Format output
while 1:
   try:
       bpf_ctx.trace_print(fmt="{5}")
   except KeyboardInterrupt:
       print()
       sys.exit(1)
```

这个程序分为两部分：`BPF`的`C`语言片段和`python`片段。

`bpf_txt`: `BPF`片段, 只包括着一个函数`hello_world_printk`。它的作用如下

> 1. 每次系统调用`sys_sync`命中，`bpf_trace_printk`会打印"hello world"到`/sys/kernel/debug/tracing/trace_pipe`
> 2. 每个在`BPF`片段要在`probe`或跟踪点执行的`C`函数的参数都要包括`pt_regs *ctx`(在这个例子不需要用上，直接用`void* ctx`)。返回值一定要`int`类型

`bpf_ctx = BPF(text=bpf_txt)`: 加载`BPF`片段，并且编译，校验和在内核运行它，再返回一个`BPF`对象用于获取事件。

`attach_kprobe(event='...', fn_name='...')`：指定`BPF`片段里函数(`fn_name`指定)挂钩到哪些跟踪点(`event`指定)

`bpf_ctx.trace_print(fmt="{5}")`：从`/sys/kernel/debug/debug/tracing/trace_pipe`读取`BPF`片段的结果，每条记录都会包括这些字段：

1. {1}: 进程ID
2. {2}: 执行的CPU核
3. {3}: 标志
4. {4}: `unix`时间戳
5. {5},{6},{7}：自定义字段，这里只用了{5}，是"hello world"

## 使用`BPF_PERF_OUTPUT`

由于`trace_pipe`是通用的，所以，从它出来的结果可能会和其它`BPF`程序结果交叠。所以改用`BPF_PERF_OUTPUT`来获得单独通道获取`BPF`的结果。

```
#!/usr/bin/python

from bcc import BPF
import sys

# Define BPF program
bpf_txt = """

#define MY_STR_LEN 12
BPF_PERF_OUTPUT(events);

struct data_t {
    char str[MY_STR_LEN];
};

int hello_world_perf(struct pt_regs *ctx) {
    struct data_t data = {};
    __builtin_memcpy(&data.str, "Hello World!", sizeof(data.str));

    events.perf_submit(ctx, &data, sizeof(data));
    return 0;
}
"""

def handle_event(cpu, data, size):
    output = bpf_ctx["events"].event(data)
    print("%s" % output.str)

# Load BPF program
bpf_ctx = BPF(text=bpf_txt)
bpf_ctx.attach_kprobe(event=bpf_ctx.get_syscall_fnname("sync"),
    fn_name="hello_world_perf")

# Print header
print("%s" % "MESSAGE")

# Open perf "events" buffer, loop with callback to handle_event
bpf_ctx["events"].open_perf_buffer(handle_event)

# Format output
while 1:
    try:
        bpf_ctx.perf_buffer_poll()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
```

和第一次的实现有些不一样：

* 使用`BPF_PERF_OUTPUT`创建一个`events`表，允许`BPF`片段通过环形缓存向用户态推送结果
* `struct data_t`定义推送结果的数据结构
* `__builtin_memcpy`用于初始化单个数据
* `events.perf_submit`往`events`推送结果
* `bpf_ctx["events"].open_perf_buffer(handle_event)`把环形缓存的数据流和`python`处理函数`handle_event`关联起来
* `perf_buffer_poll`执行从环形缓存抽取结果的动作
* `handle_event`必须要有`cpu`,`data`,`size`三个参数
* `bpf_ctx["events"].event(data)`从`events`获取结果。这个`events`一定要在`BPF`有定义，这个执行的返回结果一定是在`events`里的数据格式，在这里的是`data_t`

**暗号：05c7c**

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