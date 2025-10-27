---
title: 60秒学会用eBPF-BCC hook系统调用
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458483404&idx=1&sn=a75fd608eb28013525fc031631389488&chksm=b18e4a4686f9c350fa76ae2f3b56b65cd9bee86bfa3dcd793add37fd6d9e2f5fc5f179cf01da&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-12
fetch_date: 2025-10-03T22:32:56.731524
---

# 60秒学会用eBPF-BCC hook系统调用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGwoUzOwAsJQetq7kpric3JoqBH1Br9zlsZcOkZiaF23obObSxhvVvlQvw/0?wx_fmt=jpeg)

# 60秒学会用eBPF-BCC hook系统调用

爱吃菠菜

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLIys7ZeazGxWUPvbfACbGnpeDINFQBd3mSrn2WRuZQU03BhDwKiaqDqeUlbFhc14ibdQ1blicOQdJQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：爱吃菠菜

备注1: 前面是为了格式工整, 建议直接从11 hello world开始看。
备注2: 60秒指的是在Linux上, 如果是Android可能要在基础再上加点。

#

# **1 BPF是什么?**

Linux内核中运行的虚拟机,
可以在外部向其注入代码执行。

# **2 eBPF是什么?**

理解成BFP PLUS++

# **3 BCC是什么?**

BPF虚拟机只运行BPF指令, 直接敲BPF指令比较恶心。
BCC可以理解成辅助写BPF指令的工具包，
用python和c语言间接生成EBPF指令。

# **4 IO Visor是什么?**

指的是开源项目&&开发者社区，
BCC是IOVisor项目下的编译器工具集。

# **5 BCC在内核调试技术栈中的位置?**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderibsn13kZOYDVQIDKn9jYE8BR4zjoHX5d0n12bvF8mTXncO16mTRCkxQ/640?wx_fmt=png)

# **6 不同Linux内核版本对eBPF的支持?**

#

# 参考官方文档

# https://github.com/iovisor/bcc/blob/master/docs/kernel-versions.md

#

# 查看自己Linux 内核版本 (ubuntu)

```
xxx@ubuntu:~/Desktop/bcc/build$ uname -aLinux ubuntu 5.15.0-52-generic #58~20.04.1-Ubuntu SMP Thu Oct 13 13:09:46 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

#

# **7 官方文档**

#

# 项目地址

# https://github.com/iovisor/bcc

#

# 使用bcc快速排除性能/故障/网络问题的例子

# https://github.com/iovisor/bcc/blob/master/docs/tutorial.md

#

# API指南https://github.com/iovisor/bcc/blob/master/docs/reference\_guide.md

#

# python开发者教程https://github.com/iovisor/bcc/blob/master/docs/tutorial\_bcc\_python\_developer.md

#

# examples

# https://github.com/iovisor/bcc/tree/master/examples

# **8 其他参考**

#

# Brendan Gregg出品教程

# https://www.brendangregg.com/ebpf.html

#

# linux内核调试追踪技术20讲https://space.bilibili.com/646178510/channel/collectiondetail?sid=468091

#

# 使用ebpf跟踪rpcx微服务

# https://colobu.com/2022/05/22/use-ebpf-to-trace-rpcx-microservices/

#

# **eBPF监控工具bcc系列**

#

# 一 启航

# https://developer.aliyun.com/article/590484?spm=a2c6h.13262185.profile.109.74541f13UmhQiC

#

# 二 性能问题定位

# https://developer.aliyun.com/article/590865?spm=a2c6h.13262185.profile.108.74541f13UmhQiC

#

# 三 自定义工具trace

# https://developer.aliyun.com/article/590867?spm=a2c6h.13262185.profile.107.74541f13UmhQiC

#

# 四 工具argdist

# https://developer.aliyun.com/article/590869?spm=a2c6h.13262185.profile.106.74541f13UmhQiC

#

# 五 工具funccount

# https://developer.aliyun.com/article/590870?spm=a2c6h.13262185.profile.105.74541f13UmhQiC

#

# 六 工具查询列表

# https://developer.aliyun.com/article/591411?spm=a2c6h.13262185.profile.104.74541f13UmhQiC

#

# 七 开发脚本

# https://developer.aliyun.com/article/591412?spm=a2c6h.13262185.profile.103.74541f13UmhQiC

#

# 八 BPF C

# https://developer.aliyun.com/article/591413?spm=a2c6h.13262185.profile.102.74541f13UmhQiC

#

# 九 bcc Pythonhttps://developer.aliyun.com/article/591415?spm=a2c6h.13262185.profile.101.74541f13UmhQiC

# **9 安装BCC二进制包 (Ubuntu) (测试发现没法用)**

#

# 具体参考官方文档

# https://github.com/iovisor/bcc/blob/master/INSTALL.md

#

# iovisor版 (官网说这个比较旧)

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4052245BD4284CDDecho "deb https://repo.iovisor.org/apt/$(lsb_release -cs) $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/iovisor.listsudo apt-get updatesudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r)
```

#

# Nightly版

```
echo "deb [trusted=yes] https://repo.iovisor.org/apt/xenial xenial-nightly main" | sudo tee /etc/apt/sources.list.d/iovisor.listsudo apt-get updatesudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r)
```

#

# 安装后目录结构

# bcc路径为/usr/share/bcc

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderdlVYquS09Fpn0TFXtpstfhxv0zfSRDJT6IJbNZzjVPtZiakI3UcGDlA/640?wx_fmt=png)

# **10 自行编译安装 (Ubuntu) (推荐)**

#

# 确定版本自己ubuntu版本代码

```
lsb_release -aNo LSB modules are available.Distributor ID:    UbuntuDescription:    Ubuntu 20.04.5 LTSRelease:    20.04Codename:    focal
```

#

# 官网找对应ubuntu版本的依赖

```
# For Focal (20.04.1 LTS)sudo apt install -y bison build-essential cmake flex git libedit-dev \libllvm12 llvm-12-dev libclang-12-dev python zlib1g-dev libelf-dev libfl-dev python3-distutils
```

#

# 下载编译

```
git clone https://github.com/iovisor/bcc.gitmkdir bcc/build; cd bcc/buildcmake ..makesudo make installcmake -DPYTHON_CMD=python3 .. # build python3 bindingpushd src/python/makesudo make installpopd
```

#

# **11 hello world!**

#

# **运行hello\_world.py**

# 进入bcc/examples目录，

# 运行脚本sudo python3 hello\_world.py，

# 它的逻辑是, hook了某个syscall, 每当运行该syscall, 就输出helloworld。

# 你随便点点鼠标, 就能触发它显示日志了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderjqqicvTicy9xhugrJJPCbfPv7sIxjLILlbnAIEOVTxdTxPeDibItGA27g/640?wx_fmt=png)
**运行hello\_fields.py**

这个脚本是一样的逻辑, 不过输出格式对齐了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZderw2Aptxzk8iaZsezQuTWX8KEmFtP10kNHqicVGRrYDBcicLqqDdzu4JBtg/640?wx_fmt=png)

# **12 如何用BCC监控open()函数的执行?**

进入bcc/tools/目录,运行opensoop.py脚本。
然后自己开clion编一个demo，
调用open触发eBFP的callback。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPAEEsGb31Cicic2dbZdervRicuylxicvltLAHqDlZOCbct213hHvpJz1Wpn7l5vl0MEMGa8duLPRw/640?wx_fmt=png)

# **13 如何hook 任意system call?**

#

# **opensoop.py的实现**

# ok, 上面这样eBPF就算跑起来了,

# 接着直奔主题，上面那个脚本是怎么hook的open?

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYaPA...