---
title: PWN入门-SROP拜师
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-30
fetch_date: 2025-10-06T18:52:37.264288
---

# PWN入门-SROP拜师

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Huzf4HibBCw9DnCH936QTu7ibYg3RDaEJJRv9cQ0Y60iaC4aTvtuxicmzGFuz17XB121Gl24dqIwGGww/0?wx_fmt=jpeg)

# PWN入门-SROP拜师

福建炒饭乡会

看雪学苑

##

```
一

进程的贴身行囊 - 信号
```

#

# 信号是用户态进程与内核进行通信的一种方式，它是陷阱（软中断）的一种。如果想要查看所有的信号类型可以查询Linux手册。

信号抵达进行需要经过两个步骤，一是发送信号，而是接收信号。

## 信号与进程组

在Linux中进程的待处理的信号由`task_struct`结构体中的`signal`成员和`pending`成员进行记录,`signal`成员和`pending`成员的区别在于，`signal`成员中存放的待处理信号对整个进程组都是生效的，而`pending`成员只对指定的线程有效。

`signal`成员由`signal_struct`结构体定义，该结构体中的`shared_pending`成员是管理共享信号的主要成员，它由由`sigpending`结构体定义，`task_struct`结构体中的`pending`成员也由`sigpending`结构体定义。

```
struct signal_struct {
    refcount_t		sigcnt;
    ......
    struct sigpending	shared_pending;
    ......
    struct rw_semaphore exec_update_lock;
} __randomize_layout;

struct sigpending {
    struct list_head list;
    sigset_t signal;
};

struct taks_struct {
    ......
    struct signal_struct			*signal;
    struct sighand_struct __rcu		*sighand;
    struct sigpending				pending;
    ......
}
```

`sigpending`结构体中的`list`成员指向了待处理信号队列，从下面的定义中可以看到`info`记录了关键的信号信息。

`sigpending`结构体中还可以看到一个`list`成员的身影，既然`sigpending`结构体中的`list`成员已经可以管理待处理信号队列了，那么`sigpending`结构体中的`list`成员又有什么用呢？

```
#define __SIGINFO 			\
struct {				\
    int si_signo;			\
    int si_code;			\
    int si_errno;			\
    union __sifields _sifields;	\
}

typedef struct kernel_siginfo {
    __SIGINFO;
} kernel_siginfo_t;

struct sigqueue {
    struct list_head list;
    int flags;
    kernel_siginfo_t info;
    struct ucounts *ucounts;
};
```

要知道，在Linux中信号分成常规信号和实时信号，这里我们需要先了解一下它们的区别。

### 常规信号与实时信号

Linux中1号 - 31号是常规信号，32号+是实时信号。它们的区别在于，同进程下同类型的常规信号只能存在一个，当常规信号被响应后，下一个同类型的常规信号才可以进入队列。

对于实时信号来讲则不是这样，同进程下可以存在多个同类型的实时信号，系统会根据实时信号在队列中的数量进行多次响应。

因此`sigpending`结构体中的`list`成员管理着不同类型的信号，此链表中的信号类型是不能重复的，`sigpending`结构体中的`list`成员管理着同类型的信号，如果有需要且信号是实时信号，那么待处理信号就会被插入`sigpending`结构体中的`list`成员对应的队列中。

### 驱动验证

通过内核驱动（见附件）指定函数和进程ID，可以将进程尚未处理的信号信息打印出来，从下面可以看到，进程收到了信号`SIGTERM`，`SIGTERM`信号的序号是15，该信号是对整个进程组生效的。

```
arch_do_signal_or_restart

[16176.561445]  pending signal ->
[16176.561447]  shared pending signal ->
[16176.561448]          00000000 - signal num = 15 ;
```

## 信号的发送

信号发送的原因可以分成三种，一是内核检测到错误发送（比如段错误，但并不是所有的错误都会导致信号产生）进而向进程组发送信号，二是主动发送信号（比如调用`kill`函数、`alarm`函数或者使用`kill`程序），三是外部事件触发的信号（如I/O设备、其他进程）。

通过Shell运行的进程，通过键盘输入`CTRL + C`或`CTRL + Z`可以向进程发送`SIGINT`或`SIGTSTP`信号。

## 信号的接收

进程接收到信号后，会根据信号的类型执行默认的行为（终止进程、终止进程并转储、挂起、忽略信号）。

在C语言中允许程序通过`sigaction`函数（更加强大，`signal`函数是`sigaction`函数的子集）设置指定信号的处理方法，而不是按照默认行为处理。

```
void (*signal(int sig, void (*func)(int)))(int);

int sigaction(int signum,
    const struct sigaction *_Nullable restrict act,
    struct sigaction *_Nullable restrict oldact);

特殊的处理函数 ->
    SIG_DFL：执行默认操作
    SIG_IGN：忽略信号
```

C语言提供的信号处理函数并不是所有的信号都可以处理的，比如信号`SIGKILL`和`SIGSTOP`，它们就必须执行默认行为。

### 用户态程序查看信号的发出方

有时候程序接收到信号后，我们会想要知道信号发出方的信息，因此下面给出了一种自定义信号处理函数获取发出方信息的办法。

下方直接给出了自定义信号处理操作的示例代码，代码由信号处理、全局跳转、退出处理三个部分组成。

自定义的信号处理函数会打印信号信息以及发送信息方的信息，发送方的信息被存储在`my_signal_handle`中的`siginfo`变量内。

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <ucontext.h>

typedef void (*signal_handle_func)(int, siginfo_t*, void*);

#define SIGNAL_REGISTER_FAILED		((signal_handle_func)-1)
#define SETJMP_RET_VAL_1			2333
#define KRNL_UCNTXT_ELE_CNT			5

typedef struct my_signal_info {
    unsigned long sig_num;
    signal_handle_func handle_func;
} my_siginfo;

static void my_signal_handle(int, siginfo_t*, void*);

static my_siginfo my_si[] = {
    {
        .sig_num = SIGKILL,
        .handle_func = my_signal_handle,
    },
    {
        .sig_num = SIGTERM,
        .handle_func = my_signal_handle,
    },
};
static int ret_num = 0;
static jmp_buf test_jmp_context;

static void my_atexit_func(void)
{
    printf("enter %s, program will exit\n", __func__);
}

static void my_atexit_register(void (*func)(void))
{
    int ret;

    ret = atexit(func);
    if (ret != 0) {
        printf("register atexit function failed\n");

        exit(ret);
    }
}

static void siginfo_dump(siginfo_t* si)
{
    if (si) {
        printf(
            "\n[**] signinfo (signinfo_t size 0x%llx) - (_sifields size 0x%llx):\n"
            "si_signo = %08d ; si_errno = %08d ; si_code = %08d ;\n"
            "si_pid   = %08d ; si_uid   = %08d ;\n"
            "[--] _sifields will be displayed differently depending on the signal\n"
            "[--] only pid and uid will be shown here\n",
            sizeof(*si), sizeof(si->_sifields),
            si->si_signo, si->si_errno, si->si_code,
            si->_sifields._pad[0], si->_sifields._pad[1]
        );
    }
}

static void libc_fpstate_dump(fpregset_t fpregs)
{
    printf(
        "\tcwd = %d ; swd = %d ; ftw = %d ; fop = %d ;\n"
        "\trip = 0x%016lx ; rdp = 0x%016lx ;\n"
        "\tmxcsr = 0x%08x ; mxcr_mask = 0x%08x ;\n"
        "\tno [_st] [_xmm]\n",
        fpregs->cwd,
        fpregs->swd,
        fpregs->ftw,
        fpregs->fop,
        fpregs->rip,
        fpregs->rdp,
        fpregs->mxcsr,
        fpregs->mxcr_mask
    );
}

static void ucontext_dump(ucontext_t* ucontext)
{
    ssize_t arr_size, ele_size, ele_cnt;
    int i;

    if (ucontext) {
        printf(
            "\n[**] ucontext (ucontext_t size 0x%llx):\n"
            "uc_flags = 0x%016lx ; uc_link = 0x%016lx ;\n"
            "uc_stack (stack_t size 0x%llx) ->\n"
            "\tss_sp = 0x%016lx ; ss_flags = 0x%016lx ; ss_size = 0x%016lx\n"
            "uc_mcontext (mcontext_t size 0x%llx) ->\n"
            "\t---- gregs start ----",
            sizeof(*ucontext),
            ucontext->uc_flags, (unsigned long)ucontext->uc_link, sizeof(ucontext->uc_stack),
            ucontext->uc_stack.ss_sp, ucontext->uc_stack.ss_flags, ucontext->uc_stack.ss_size,
            sizeof(ucontext->uc_mcontext)
        );

        i = 0;
        while (i < __NGREG) {
            if ((i % 4) == 0) {
                printf("\n\t");
            }

            printf(
                "0x%016lx ; ", ucontext->uc_mcontext.gregs[i]
            );

            i++;
        }

        printf(
            "\n\t---- gregs end ----\n"
            "\t---- fpregs start -----\n"
        );
        libc_fpstate_dump(ucontext->uc_mcontext.fpregs);
        printf("\t---- fpregs end ----\n");

        printf(
            "no uc_sigmask (sigset_t size 0x%llx)\n"
            "__fpregs_mem (_libc_fpstate size 0x%llx) ->\n",
            sizeof(ucontext->uc_sigmask), sizeof(ucontext->__fpregs_mem)
        );
        libc_fpstate_dump(&ucontext->__fpregs_mem);

        i = 0;
        arr_size = sizeof(ucontext->__ssp);
        ele_size = sizeof(unsigned long long);
        ele_cnt = arr_size / ele_size;
        printf(
            "__ssp (array size 0x%llx) ->\n\t",
            arr_size
        );
        while (i < 4) {
            printf("0x%016llx ; ", ucontext->__ssp[i]);

            i++;
        }
        printf("\n");
    }
}

static void my_signal_handle(int signum, siginfo_t* si, void* ucontext)
{
    printf(
        "\n[**] receive signal, signal base info:\n"
        "signal num    = %d \n"
        "signal info   = 0x%016lx\n"
        "user context  = 0x%016lx\n",
        signum, (unsigned long)si, (unsigned long)ucontext
    );

    siginfo_dump(si);
    ucontext_dump(ucontext);
}

static signal_handle_func my_customize_signal_register_process(my_siginfo* msi)
{
    int ret;
    struct sigaction new_act, old_act;

    memset(&new_act, 0, sizeof(struct sigaction));

    sigemptyset(&new_act.sa_mask);
    new_act.sa_flags = SA_SIGINFO;
#ifdef  SA_RESTART
    new_act.sa_flags |= SA_RESTART;
#endif
    new_act.sa_sigaction = msi->handle_func;

    ret = sigaction(msi->sig_num, &new_act, &old_act);
    if (ret != 0) {
        return SIGNAL_REGISTER_FAILED;
    }

    return old_act.sa_sigaction;
}

static void my_signal_register(void)
{
    signal_handle_func tmp_func;
    size_t arry_size, ele_size, ele_cnt;

    arry_size = sizeof(my_si);...