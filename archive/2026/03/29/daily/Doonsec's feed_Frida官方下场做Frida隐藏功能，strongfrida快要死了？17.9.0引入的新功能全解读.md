---
title: Frida官方下场做Frida隐藏功能，strongfrida快要死了？17.9.0引入的新功能全解读
url: https://mp.weixin.qq.com/s/Iv_uN2qkIAdEqv0wunLvww
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:43:54.360495
---

# Frida官方下场做Frida隐藏功能，strongfrida快要死了？17.9.0引入的新功能全解读

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Sq4BUsrXeTicIHMalBlNjC6twOZXoGibWJYiafXFjRsWxsMCnzdoJVoO0hSyicibrBnBTRMDHXRTflM0ia8lFFJsmoRSCZN1B3L3iagy8dTCicQghia4/0?wx_fmt=jpeg)

# Frida官方下场做Frida隐藏功能，strongfrida快要死了？17.9.0引入的新功能全解读

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器中沉浸阅读

# Frida17.9.0引入的新功能解读

Frida这个版本的更新看上去是将eBPF的能力继续辐射到更多的Frida功能组件上。而且重点是官方将Frida隐藏作为重要的功能提上了日程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTiccTx7hJPibj4D1Wy2a2kJpGOcex2E6lnPpFoNK2XqRsfXuTbcQDUVfxtNreYqaYXgmUaBR1D0b31Gj2XvTCa7sRibdzNPvJ2icX8/640?wx_fmt=png&from=appmsg)

这个版本的更新里面，Frida隐藏的部分有：

* 将ptrace特征彻底隐藏
* 隐藏Frida监听端口
* 隐藏子进程创建监控的特征

关于子进程创建监控的特征，我们这里再多说几句。国内X加密的企业版本在检测Frida时，使用了一个比较取巧的方法。重点在于监控进程的fork操作的：https://github.com/frida/frida-core/blob/main/lib/payload/fork-monitor.vala 。它会对`fork`与`vfork`进行监控。里面有一行代码：

```
interceptor.replace (vfork_impl, fork_impl);
```

意味着它会对这两个接口进行InlineHook，但它们的处理器使用同一个，这两者在进程空间的数据同步上有着一些差异，比如在父进程中的一个全局变量，子进程中它们的数据访问同步规则不同，这就可以用来检测`fork`与`vfork`是否被Hook，进而检测Frida。目前Frida官方并没有实现它的过检测，希望官方能够对其进行处理。这其实需要对`interceptor.replace`这类接口做eBPF的大手术，可能会有难度与兼容性的问题出现。

## 背景

Frida 17.9.0（2026年3月26日）紧跟17.8.0发布，带来了几项对安全研究者非常实用的新能力。三个核心更新值得重点关注：

1. **Linux eBPF spawn gater**

   ——在内核层面拦截`execve`，实现比传统ptrace方案更隐蔽、更高效的进程捕获。
2. **Group-stopped PIDs注入**

   ——解决了eBPF spawn gater将进程SIGSTOP后无法注入的工程难题。
3. **control-endpoint后端选项**

   ——允许自定义frida-server连接端点，可通过`localabstract:`等非标准端口绕过Frida端口检测。

从演进线看，17.8.0完成了eBPF syscall-tracer主线收编，17.9.0则将eBPF的应用范围扩展到spawn gating领域，并围绕它做了完整的工程闭环——从内核拦截到用户态注入再到端口隐藏，形成了一条完整的反检测链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8gkibNZglS5TNPASVRgHnqTpFoXyYdtRhlF1mJACJXKKzSoVgj9z3yVicA4E0UryTWTJ59pqlQBnImx2xJCXL0AgyHoAsF3UATs/640?wx_fmt=png&from=appmsg)

## 分析范围与方法

分析窗口以17.9.0新增功能为主线（frida-core commit `4e5a60a5..c3864a15`），同时覆盖17.8.x开发周期中的关键架构变更。涉及以下子项目：

| 子项目 | 17.9.0核心提交 | 聚焦方向 |
| --- | --- | --- |
| frida-core | 7 | spawn gater、group-stopped注入、control-endpoint |
| frida-gum | - | 无17.9.0专属提交 |
| frida-python | 3 | override\_option绑定、spawn gating示例 |
| frida-tools | - | releng同步 |

本文聚焦以下代码：

1. eBPF内核侧拦截：`src/linux/helpers/spawn-gater.bpf.c`
2. 用户态spawn管理：`src/linux/spawn-gater.vala`
3. 宿主会话集成：`src/linux/linux-host-session.vala`
4. Group-stopped注入逻辑：`src/linux/frida-helper-backend.vala`内`InjectSession`
5. 设备选项覆盖：`src/frida.vala`内`override_option()`
6. Droidy/Fruity后端：`src/droidy/droidy-host-session.vala`与`src/fruity/fruity-host-session.vala`

## 核心功能一：eBPF spawn gater

### 1 设计动机

Frida在macOS上早已通过DTrace实现spawn gating——当目标系统上有新进程`exec`时，先暂停该进程，通知Frida用户决定是否注入，再恢复执行。但Linux上一直缺少内核级的spawn gating实现，此前只在Android上通过Zygote子进程gating部分覆盖了这一需求。

17.9.0引入的eBPF spawn gater填补了这一空白。它的核心思路极为精炼：**在`execve`系统调用入口处用eBPF程序发送`SIGSTOP`信号，把新进程冻住，同时通过ringbuf通知用户态**。

这个方案的工程价值在于：eBPF程序运行在内核态，不需要ptrace附加目标进程，也不会在目标进程的`/proc/pid/status`中留下TracerPid痕迹，具有天然的反检测优势。

### 2 eBPF内核程序：spawn-gater.bpf.c

完整的eBPF程序只有55行，非常精炼。核心代码如下：

```
#include"frida-linux-syscalls.h"
#include<linux/bpf.h>
#include<bpf/bpf_helpers.h>
#include<bpf/bpf_tracing.h>

#define SIGSTOP 19
#define MAX_FILENAME 256

typedefstruct _ExecveEventExecveEvent;

struct _ExecveEvent
{
int pid;
char command[MAX_FILENAME];
};

struct
{
  __uint (type, BPF_MAP_TYPE_RINGBUF);
  __uint (max_entries, 1 << 22);
}
events SEC(".maps");

structtrace_event_raw_sys_enter
{
  __u64 unused;
long id;
unsignedlong args[6];
};

SEC ("tracepoint/raw_syscalls/sys_enter")
int
on_execve_enter(struct trace_event_raw_sys_enter * ctx)
{
  __s32 nr = (__s32) ctx->id;
if (nr != FRIDA_LINUX_SYSCALL_EXECVE)
return0;

  ExecveEvent * e = bpf_ringbuf_reserve (&events, sizeof (ExecveEvent), 0);
if (e == NULL)
return0;

  e->pid = bpf_get_current_pid_tgid () >> 32;
constchar * filename = (constchar *) ctx->args[0];
  bpf_probe_read_user_str (e->command, sizeof (e->command), filename);

  bpf_ringbuf_submit (e, 0);

  bpf_send_signal (SIGSTOP);

return0;
}

char LICENSE[] SEC ("license") = "Dual BSD/GPL";
```

逐层分析关键设计决策：

**挂载点选择：`tracepoint/raw_syscalls/sys_enter`**

与17.8.0的syscall-tracer一脉相承，使用`raw_syscalls/sys_enter`而非`tracepoint/syscalls/sys_enter_execve`。原因是Android GKI 2.0内核默认关闭了`FTRACE_SYSCALLS`，而`raw_syscalls`是always-on的。通过在eBPF内部手动判断`ctx->id == FRIDA_LINUX_SYSCALL_EXECVE`来过滤，虽然多了一次比较，但换来了对所有Linux/Android内核的兼容性。

`FRIDA_LINUX_SYSCALL_EXECVE`定义在`frida-linux-syscalls.h`中，会根据目标架构自动选择正确的系统调用号（x86\_64上为59，arm64上为221等），预编译产物覆盖了arm、arm64、x86、x86\_64、mips、mips64共10个架构变体。

**事件结构：ExecveEvent**

```
struct _ExecveEvent {
int pid;                    // 进程TGID
char command[MAX_FILENAME]; // execve第一个参数：可执行文件路径
};
```

结构极简，只包含PID和命令路径。使用`bpf_get_current_pid_tgid() >> 32`获取TGID（即进程PID），通过`bpf_probe_read_user_str`从用户空间安全读取`execve`的第一个参数（文件名）。

**核心机制：bpf\_send\_signal(SIGSTOP)**

这是整个设计最精妙的一行。`bpf_send_signal()`是Linux 5.3引入的BPF helper，允许eBPF程序直接向当前任务发送信号。调用`bpf_send_signal(SIGSTOP)`会让正在执行`execve`的进程立即被内核暂停——进程进入**group-stop**状态。

这与ptrace的`PTRACE_ATTACH`完全不同：

* ptrace会在目标进程的`/proc/pid/status`中设置`TracerPid`字段，容易被反调试检测
* `SIGSTOP`

  导致的group-stop是正常的进程状态，不涉及调试器附加
* eBPF程序运行在内核上下文，对目标进程完全透明

**ringbuf通信**

使用`BPF_MAP_TYPE_RINGBUF`（大小4MB，即`1 << 22`）。先`bpf_ringbuf_reserve`预留空间、填充数据、再`bpf_ringbuf_submit`提交。比`BPF_MAP_TYPE_PERF_EVENT_ARRAY`更高效，不需要per-CPU buffer。

### 3 用户态管理：SpawnGater类

`src/linux/spawn-gater.vala`实现了完整的用户态管理逻辑，总计154行。

```
SpawnGater
├── start()          // 加载eBPF程序，attach tracepoint，监听ringbuf
├── stop()           // 卸载eBPF，恢复所有pending进程
├── enumerate_pending_spawn()  // 返回当前被拦截的进程列表
├── try_resume()     // 恢复指定进程
├── signal spawn_added    // 通知上层有新进程被拦截
└── signal spawn_removed  // 通知上层进程已恢复
```

**启动流程**

```
publicvoid start () throws Error {
var obj = BpfObject.open ("spawn-gater.elf",
        Frida.Data.HelperBackend.get_spawn_gater_elf_blob ().data);
var events = obj.maps.get_by_name ("events");
    obj.prepare ();
    events_reader = new BpfRingbufReader (events);
    obj.load ();

foreach (var program in obj.programs) {
var link = program.attach ();
        links.add (link);
    }

// 设置epoll监听ringbuf的fd
    events_channel = new IOChannel.unix_new (events.fd);
var src = new IOSource (events_channel, IOCondition.IN);
var state = new EventsWatchState (this);
    src.set_callback (state.on_ready);
    src.attach (MainContext.get_thread_default ());
    events_source = src;
}
```

这里复用了17.8.0引入的`BpfObject`和`BpfRingbufReader`基础设施。预编译的`spawn-gater.elf`以资源blob形式内嵌在frida-helper中，运行时通过libbpf加载。

`BpfRingbufReader`内部使用epoll监听ringbuf的文件描述符。当内核侧有新事件写入时，通过GLib的`IOSource`回调`on_ready`，进而调用`process_pending_events()`拉取事件。

**事件处理**

```
privatevoid handle_event (ExecveEvent * e) {
var info = HostSpawnInfo (e->pid, (string) e->command);
    pending_spawn[e->pid] = info;
    spawn_added (info);
}
```

每个事件被解析为`HostSpawnInfo`（包含pid和可执行文件路径），存入`pending_spawn`字典，并通过`spawn_added`信号通知上层。

**恢复机制**

```
publicbool try_resume (uint pid) {
    HostSpawnInfo? spawn;
if (!pending_spawn.unset (pid, out spawn))
returnfalse;
    spawn_removed (spawn);
    perform_resume.begin (pid);
returntrue;
}

privateasyncvoid perform_resume (uint pid) {
try {
        yield helper.resume (pid, null);
    } catch (GLib.Error e) {
if (e is Error.INVALID_ARGUMENT)
Posix.kill ((Posix.pid_t) pid, Posix.Signal.CONT);
    }
}
```

恢复时优先尝试通过`helper.resume()`（ptrace方式），如果失败则退回`kill(pid, SIGCONT)`直接发送继续信号。这个双路径设计保证了健壮性：如果进程已经被注入过（由InjectSession管理），走ptrace路径；否则走简单的SIGCONT。

### 4 宿主会话集成

`linux-host-session.vala`中的修改将spawn gater无缝集成到Frida的现有架构中：

```
publicoverrideasyncvoid enable_spawn_gating (...) {
// 先预加载helper（确保64位和32位helper都已就绪）
var helper_process = helper as LinuxHelperProcess;
if (helper_process != null)
        yield helper_process.preload (cancellable);

var gater = ensure_spawn_gater ();
if (gater.state == STOPPED) {
// Android上允许eBPF启动失败（可能缺少CAP_BPF）
// 纯Linux上直接抛异常
        #if ANDROID
try { gater.start (); } catch (Error e) { }
        #else
        gater.start ();
        #endif
    }

    #if ANDROID
    yield robo_launcher.enable_spawn_gating (cancellable);
    #endif
}
```

关键设计点：

1. **预加载helper**

   ：`preload()`方法确保frida-helper-64和f...