---
title: 60秒学会用eBPF-BCC hook系统调用
url: https://buaq.net/go-135262.html
source: unSafe.sh - 不安全
date: 2022-11-12
fetch_date: 2025-10-03T22:28:43.850717
---

# 60秒学会用eBPF-BCC hook系统调用

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/131dd17910cf8cea11df6187d9c004dc.jpg)

60秒学会用eBPF-BCC hook系统调用

本文为看雪论坛优秀文章看雪论坛作者ID：爱吃菠菜备注1: 前面是为了格式工整, 建议直接从11 hello world开始看。备注2: 60秒指的是在Linux上, 如果是Android可能要在基础再
*2022-11-11 18:29:6
Author: [mp.weixin.qq.com(查看原文)](/jump-135262.htm)
阅读量:35
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGnpeDINFQBd3mSrn2WRuZQU03BhDwKiaqDqeUlbFhc14ibdQ1blicOQdJQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：爱吃菠菜

备注1: 前面是为了格式工整, 建议直接从11 hello world开始看。
备注2: 60秒指的是在Linux上, 如果是Android可能要在基础再上加点。

Linux内核中运行的虚拟机,
可以在外部向其注入代码执行。

理解成BFP PLUS++

BPF虚拟机只运行BPF指令, 直接敲BPF指令比较恶心。
BCC可以理解成辅助写BPF指令的工具包，
用python和c语言间接生成EBPF指令。

指的是开源项目&&开发者社区，
BCC是IOVisor项目下的编译器工具集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderibsn13kZOYDVQIDKn9jYE8BR4zjoHX5d0n12bvF8mTXncO16mTRCkxQ/640?wx_fmt=png)

```
[email protected]:~/Desktop/bcc/build$ uname -aLinux ubuntu 5.15.0-52-generic #58~20.04.1-Ubuntu SMP Thu Oct 13 13:09:46 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4052245BD4284CDDecho "deb https://repo.iovisor.org/apt/$(lsb_release -cs) $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/iovisor.listsudo apt-get updatesudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r)
```

```
echo "deb [trusted=yes] https://repo.iovisor.org/apt/xenial xenial-nightly main" | sudo tee /etc/apt/sources.list.d/iovisor.listsudo apt-get updatesudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderdlVYquS09Fpn0TFXtpstfhxv0zfSRDJT6IJbNZzjVPtZiakI3UcGDlA/640?wx_fmt=png)

```
lsb_release -aNo LSB modules are available.Distributor ID:    UbuntuDescription:    Ubuntu 20.04.5 LTSRelease:    20.04Codename:    focal
```

```
# For Focal (20.04.1 LTS)sudo apt install -y bison build-essential cmake flex git libedit-dev \libllvm12 llvm-12-dev libclang-12-dev python zlib1g-dev libelf-dev libfl-dev python3-distutils
```

```
git clone https://github.com/iovisor/bcc.gitmkdir bcc/build; cd bcc/buildcmake ..makesudo make installcmake -DPYTHON_CMD=python3 .. # build python3 bindingpushd src/python/makesudo make installpopd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderjqqicvTicy9xhugrJJPCbfPv7sIxjLILlbnAIEOVTxdTxPeDibItGA27g/640?wx_fmt=png)
**运行hello\_fields.py**

这个脚本是一样的逻辑, 不过输出格式对齐了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderw2Aptxzk8iaZsezQuTWX8KEmFtP10kNHqicVGRrYDBcicLqqDdzu4JBtg/640?wx_fmt=png)

进入bcc/tools/目录,运行opensoop.py脚本。
然后自己开clion编一个demo，
调用open触发eBFP的callback。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZdervRicuylxicvltLAHqDlZOCbct213hHvpJz1Wpn7l5vl0MEMGa8duLPRw/640?wx_fmt=png)

我打开那个脚本看了一下, blabla一大堆, 基本都在处理兼容和格式,

我把不关心的东西都删了, 留下核心的代码, 写好注释放这里了。

**如何任意的hook syscall?**

只关心4点:
(1)怎么写before?
(2)怎么写after?
(3)怎么注册hook?
(4)怎么输出日志?
(跟xposed差不多的叙事结构)

```
#!/usr/bin/env python# 该代码在ubuntu 20环境里运行通过from __future__ import print_functionfrom bcc import ArgString, BPFfrom bcc.containers import filter_by_containersfrom bcc.utils import printbimport argparsefrom collections import defaultdictfrom datetime import datetime, timedeltaimport os # 注入到eBPF虚拟机的代码bpf_text = '''#include <uapi/linux/ptrace.h>#include <uapi/linux/limits.h>#include <linux/sched.h> // hook到参数和返回值,放在这两个结构里struct val_t {  u64 id;  char comm[TASK_COMM_LEN];  const char *fname;}; // 同上struct data_t {  u64 id;  int ret;  char comm[TASK_COMM_LEN];  char name[NAME_MAX];};  // 创建一个events (hook到东西后就用它通知python那个callback输出)BPF_PERF_OUTPUT(events);  // 这个api是在创建一个map变量,变量名为infotmp// 因为你不能在eBPF里用std::map, 只能用它提供的这种东西.BPF_HASH(infotmp, u64, struct val_t);  // after函数int after_openat(struct pt_regs *ctx) {  u64 id = bpf_get_current_pid_tgid(); // 获取tid  struct val_t *valp;  struct data_t data = {};  valp = infotmp.lookup(&id); // 在map中查询id  if (valp == 0) {    return 0;  }  // 从map中读取至局部变量  bpf_probe_read_kernel(&data.comm, sizeof(data.comm), valp->comm);  bpf_probe_read_user_str(&data.name, sizeof(data.name), (void *)valp->fname);  data.id = valp->id;  data.ret = PT_REGS_RC(ctx); // before里读取了参数,此时在after里补充返回值  events.perf_submit(ctx, &data, sizeof(data)); // 提交perf poll事件来让perf输出(作用就是,调用它会通知python中那个callback输出日志)  infotmp.delete(&id); // 从map中删除id  return 0;}  int syscall__before_openat(struct pt_regs *ctx, int dfd,                                const char __user *filename, int flags) {  struct val_t val = {};  u64 id = bpf_get_current_pid_tgid();  u32 pid = id >> 32;  // 获取当前进程名  if (bpf_get_current_comm(&val.comm, sizeof(val.comm)) == 0) {    val.id = id;    val.fname = filename;    infotmp.update(&id, &val); // id插入map  }  return 0;};''' # 注册hookb = BPF(text=bpf_text)b.attach_kprobe(event="__x64_sys_openat", fn_name="syscall__before_openat")b.attach_kretprobe(event="__x64_sys_openat", fn_name="after_openat") # 回调函数def my_callback(cpu, data, size):    temp = b["events"].event(data)    if temp.id is not None:        print("[pid]",temp.id & 0xffffffff, end=" ")    if temp.name is not None:        print("[path]",temp.name, end=" ")    if temp.ret is not None:        print("[ret]",temp.ret, end=" ")    if temp.comm is not None:        print("[comm]",temp.comm, end=" ")    print("") b["events"].open_perf_buffer(my_callback, page_cnt=64)while True:    try:        # 等待数据, 触发open_perf_buffer指定的回调函数        b.perf_buffer_poll()    except KeyboardInterrupt:        exit()pass
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZdermOvw3at8rDKDkpMedtPfYUnRy17RzyKf09KNt2dE1ECVmic6gTSBP4A/640?wx_fmt=png)

**看雪ID：爱吃菠菜**

https://bbs.pediy.com/user-home-760871.htm

\*本文由看雪论坛 爱吃菠菜 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FVxohib5yALmewhGYeLiaHcPrGKUuwhsUfgQmA0y0PsDWQAMHVic7ZTO4tEibWookaXKoLibNnyjJS6QA/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪CTF官网：https://ctf.pediy.com/

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic...