---
title: 如何使用eBPF观测用户空间应用程序
url: https://www.cnxct.com/ebpf-uprobe-userspace-app/
source: CFC4N的博客
date: 2022-10-28
fetch_date: 2025-10-03T21:07:32.151462
---

# 如何使用eBPF观测用户空间应用程序

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
现在觉得踏实，真踏实，由里到外的舒服

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# 如何使用eBPF观测用户空间应用程序

[2022/10/272023/01/20](https://www.cnxct.com/ebpf-uprobe-userspace-app/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [译者注](#ftoc-heading-1)
2. [前言](#ftoc-heading-2)
3. [用于检测应用程序的eBPF技术](#ftoc-heading-3)
   1. [静态声明USDT](#ftoc-heading-4)
   2. [动态声明USDT](#ftoc-heading-5)
      1. [使用 uprobes 进行动态跟踪](#ftoc-heading-6)
   3. [跟踪示例](#ftoc-heading-7)
      1. [C语言程序](#ftoc-heading-8)
      2. [JAVA语言程序](#ftoc-heading-9)
      3. [Go语言程序](#ftoc-heading-10)
4. [结论](#ftoc-heading-11)

# 译者注

近来这一年，很多刚接触eBPF的朋友会问我，eCapture的原理是什么，为什么区分OpenSSL、Gnutls、Nspr等类库实现？为什么要设定OpenSSL类库地址？为什么C、JAVA、Go实现的https通讯程序，在eCapture上实现却不一样。对于这些问题，我觉得核心问题是大家对「eBPF实现用户空间的行为跟踪」原理不了解，一直想写一篇文章介绍这个知识点，但总是太忙，没时间。这几天看到外网一篇简单的介绍，文章名是[How to Instrument UserLand Apps with eBPF](https://sematext.com/blog/ebpf-userland-apps/)，我在这里翻译、调整一下，分享给大家。

# 前言

eBPF彻底改变了Linux内核中的可观察性。在之前的博客文章中，我介绍了eBPF生态系统的基本构建，揭开了XDP的面纱，并展示了它与eBPF基础设施如何紧密合作，以便在网络堆栈中引入快速处理的数据路径。 然而，eBPF并不是`kernel-space内核空间`跟踪所独有的。如果我们能够检测在生产环境中运行的应用程序，同时享受eBPF驱动的跟踪的好处，那不是很赞吗？

这就是`eBPF uprobe`的价值所在。可以直白地把它们看成附加到用户空间的跟踪点，跟内核符号的`kprobe`类似。

许多语言的运行时、数据库系统以及其他软件堆栈都包含可供BCC工具使用的钩子。具体地说，`ustat`工具会收集有价值的事件，例如`垃圾回收`事件、`对象创建`统计信息、`方法调用`等等。

但是“，很多官方语言运行时版本，都不附带对`DTrace`支持，比如`Node.js`和`Python`等，这意味着您必须从源代码构建时，就设定好参数。也就是说，编译python这个解释语言时，就需要在参数中指定。将`--with -dtrace`标志传递给编译器。当然，这不是必要条件。对于ELF文件，只要符号表可用，就可以对它`Section段`中的任何符号进行应用动态跟踪。对`Go`或`Rust stdlib`的函数调用是通过这种方式完成的。

也就是说，对于eCapture来说，哪怕是TLS类库是静态编译的或者没有符号表的，也是可以通过自行确定Offset的方式，来实现对指定偏移地址进行动态跟踪。在eHIDS-Agent也有过一个例子，[user/probe\_ujava\_rasp.go](https://github.com/ehids/ehids-agent/blob/master/user/probe_ujava_rasp.go)的92行：

```
/*
      openjdk version "1.8.0_292"
      OpenJDK Runtime Environment (build 1.8.0_292-8u292-b10-0ubuntu1-b10)
      OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)
    */
    //ex, err := link.OpenExecutable("/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/libjava.so")

    // sub_19C30  == JDK_execvpe(p->mode, p->argv[0], p->argv, p->envv);
    //    md5sum : 38590d0382d776234201996e99487110  /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/libjava.so
    Probes: []*manager.Probe{
      {
        Section:          "uprobe/JDK_execvpe",
        EbpfFuncName:     "java_JDK_execvpe",
        AttachToFuncName: "JDK_execvpe",
        UprobeOffset:     0x19C30,
        BinaryPath:       "/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/libjava.so",
      },
    }
```

对于相应JVM的`libjava.so`中，符号表是少了`JDK_execvpe`这个函数。但是，依旧可以通过IDA pro等工具，对so文件进行静态分析，定位到`JDK_execvpe`的偏移地址是`0x19C30`，从而使用eBPF uprobe的HOOK方式完成HOOK。

> 其实，在eBPF的加载器类库中，不管是C的libbbpf还是Go的`cilium/ebpf`，都会自行读取uprobe的二进制ELF文件，自行读取符号表，进行被HOOK函数的偏移地址定位，最终依旧使用偏移地址作为HOOK参数。

# 用于检测应用程序的eBPF技术

有多种方法可以跟踪用户空间进程：

1. 静态声明的`USDT`
2. 动态声明`USDT`
3. 使用`uprobe`进行动态跟踪

## 静态声明USDT

USDT（Userland Statically Defined Tracing）体现了直接在用户代码中嵌入探针的想法。该技术的起源可以追溯到`Solaris/BSD DTrace`时代，包括使用`DTRACE_PROBE()`宏来声明策略代码位置的跟踪点。与普通符号不同，USDT钩子可以保证在代码被重构的情况下保持稳定。下图描述了在用户代码中声明`USDT`跟踪点，以及其在内核中执行的整个过程。

![](//image.cnxct.com/2022/10/ebpf-uprobe-userspace.png)

开发人员将首先通过`DTRACE_PROBE`和`DTRACE_PROBE1`宏来植入跟踪点，用来圈定感兴趣的代码块。这两个宏都接受几个强制性参数，例如`provider/probe`的名称，然后是你想从追踪点了解的任何值。编译器会在目标二进制文件的ELF部分中压制USDT追踪点。同时，编译器和追踪工具之间有个契约规定，也就是USDT的元数据所在的`.note.stapstd`段必须存在。

USDT跟踪工具会对ELF部分进行自检，并在跟踪点得位置放置一个断点，该断点将转换为`int 3`中断。每当在跟踪点的标记处执行控制流时，都会触发中断处理程序，并在内核中调用与uprobe关联的程序来处理事件并将它们发送到用户空间，执行相应的数据聚合等处理。

## 动态声明USDT

由于USDT被推入静态生成的ELF部分，对于在解释型语言或基于JIT的语言上运行的软件来说，它违背了声明`USDT`的目的。幸运的是，可以通过`libstapsdt`在运行时定义跟踪点。它生成一个带有 USDT 信息的小型共享对象，该对象映射到进程的地址空间，因此跟踪工具可以附加到期望的目标跟踪点。`libstapsdt`的绑定在大部分语言中都有。可以阅读[这个示例](https://github.com/sthima/node-usdt#example)，来了解如何在`Node.js`中安装 `USDT` 探针。

### 使用 uprobes 进行动态跟踪

这种类型的跟踪机制除了目标程序的符号表是可访问以外，不需要何额外功能。这是最通用、最强大的插桩方法，因为它允许在任意指令上注入断点，甚至无需重新启动目标进程。

## 跟踪示例

在简单的理论介绍之后，让我们看看一些具体的例子，看看如何针对不同的语言的应用程序进行插桩。

### C语言程序

`Redis` 是用 C 语言实现的热门KV对数据结构服务器。查看一下 `Redis` 符号表会发现大量函数可以通过 `uprobes` 捕获。

```
$ objdump -tT /usr/bin/redis-server
…
000000000004c160 g    DF .text  00000000000000cc  Base
addReplyDouble
0000000000090940 g    DF .text  00000000000000b0  Base        sha1hex
00000000000586e0 g    DF .text  000000000000007c  Base
replicationSetMaster
00000000001b39e0 g    DO .data  0000000000000030  Base
dbDictType
00000000000ace20 g    DF .text  0000000000000030  Base
RM_DictGetC
0000000000041bc0 g    DF .text  0000000000000073  Base
sdsull2str
00000000000bba00 g    DF .text  0000000000000871  Base        raxSeek
00000000000ac8c0 g    DF .text  000000000000000c  Base
RM_ThreadSafeContextUnlock
00000000000e3900 g    DF .text  0000000000000059  Base
mp_encode_lua_string
00000000001cef60 g    DO .bss   0000000000000438  Base        rdbstate
0000000000047110 g    DF .text  00000000000000b5  Base
zipSaveInteger
000000000009f5a0 g    DF .text  0000000000000055  Base
addReplyDictOfRedisInstances
0000000000069200 g    DF .text  000000000000004a  Base
zzlDelete
0000000000041e90 g    DF .text  00000000000008ba  Base
sdscatfmt
000000000009ac40 g    DF .text  000000000000003a  Base
sentinelLinkEstablishedCallback
00000000000619d0 g    DF .text  0000000000000045  Base
psetexCommand
00000000000d92f0 g    DF .text  00000000000000fc  Base
luaL_argerror
00000000000bc360 g    DF .text  0000000000000328  Base
raxRandomWalk
0000000000096a00 g    DF .text  00000000000000c3  Base
rioInitWithFdset
000000000003d160 g    DF .text  0000000000000882  Base
serverCron
0000000000032907 g    DF .text  0000000000000000  Base
je_prof_thread_name_set
0000000000043960 g    DF .text  0000000000000031  Base        zfree
00000000000a2a40 g    DF .text  00000000000001ab  Base
sentinelFailoverDetectEnd
00000000001b8500 g    DO .data  0000000000000028  Base
je_percpu_arena_mode_names
00000000000b5f90 g    DF .text  0000000000000018  Base
geohashEstimateStepsByRadius
00000000000d95e0 g    DF .text  0000000000000039  Base
luaL_checkany
0000000000048850 g    DF .text  00000000000002d4  Base
createClient
...
```

Redis 内部使用了一个有趣的`createStringObject`函数来分配`robj`结构的字符串。Redis 命令是以`createStringObject`调用名义生成的。我们可以通过挂钩这个函数来监视发送到 Redis 服务器的任何命令。为此，我将使用BCC工具箱中的跟踪工具来演示。

```
$ /usr/share/bcc/tools/trace '/usr/bin/redis-server:createStringObject "%s" arg1'
PID     TID     COMM            FUNC             -
8984    8984    redis-server    createStringObject b'COMMANDrn'
8984    8984    redis-server    createStringObject
b'setrn$4rnoctirn$4rnfestrn'
8984    8984    redis-server    createStringObject b'octirn$4rnfestrn'
8984    8984    redis-server    createStringObject b'festrn'
8984    8984    redis-server    createStringObject b'getrn$4rnoctirn'
8984    8984    redis-server    createStringObject b'octirn'
```

以上是在Redis CLI客户端执行`set octi fest`和`get octi`所产生的输出。

### JAVA语言程序

现代的JVM版本带有对USDT的内置支持。所有的探针都是以libjvm共享对象的名义带来的。我们可以在ELF部分挖掘出可用的追踪点。

```
$ readelf -n /usr/lib/jvm/jdk-11-oracle/lib/server/libjvm.so
...
stapsdt              0x00000037       NT_STAPSDT (SystemTap probe
descriptors)
  Provider: hs_private
  Name: cms__initmark__end
  Location: 0x0000000000e2420c, Base: 0x0000000000f725b4, Semaphore: 0x0000000000000000
  Arguments:
stapsdt              0x00000037       NT_STAPSDT (SystemTap probe descriptors)
  Provider: hs_private
  Name: cms__remark__begin
  Location: 0x0000000000e24334, Base: 0x0000000000f725b4, Semaphore: 0x0000000000000000
  Arguments:
stapsdt              0x00000035       NT_STAPSDT (SystemTap probe descriptors)
  Provider: hs_private
  Name: cm...