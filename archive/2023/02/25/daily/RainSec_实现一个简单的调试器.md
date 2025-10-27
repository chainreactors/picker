---
title: 实现一个简单的调试器
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzczOTA3OQ==&mid=2247485824&idx=1&sn=4e89f7b19e854644f595249a8ff571c7&chksm=cf1f24a8f868adbe536e9f7372bd25aebc8c1e7e0e9b92afc993b40df7a350a8d17fb190cae7&scene=58&subscene=0#rd
source: RainSec
date: 2023-02-25
fetch_date: 2025-10-04T08:05:13.371490
---

# 实现一个简单的调试器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LxlshmzkAkaKns4LWooxTNiabTOgobYcsEWTxAsBxTrkPdibBnr3TxvxKleRIFzzWGOAthhGiaZQBbKavcEonXdsQ/0?wx_fmt=jpeg)

# 实现一个简单的调试器

原创

崎山松形

RainSec

# 实现一个简单的调试器

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkaKns4LWooxTNiabTOgobYcsfOWfRS7ibfGwbEOjIDZEp6uhVVn3Xia6q4icRPMOMdAPgyWEMVoeYyRBg/640?wx_fmt=png)

  以经典的GDB为例其项目代码共有十几万行代码，但是很多情况下只会使用到几个常用功能：单步，断点，查看变量，线程/进程切换。而GDB基本上是依赖于`ptrace`系统调用，主要用于编写调试程序。大部分实现思路参考Writing a Linux Debugger Part 2: Breakpoints (tartanllama.xyz)系列文章，强烈推荐阅读

目标功能：

* • 单步
* • 断点
* • 查看内存/寄存器
* • 查看汇编

# ptrace 原理

先来看看ptrace系统调用的函数签名：

```
#include <sys/ptrace.h>

long ptrace(enum __ptrace_request request, pid_t pid, void *addr, void *data);
/*DESCRIPTION
       The  ptrace()  system  call  provides  a  means  by  which one process (the
       "tracer") may observe and control the execution  of  another  process  (the
       "tracee"), and examine and change the tracee's memory and registers.  It is
       primarily used to implement breakpoint debugging and system call tracing.
       即ptrace系统调用提供给tracer控制，读取，修改另一个进程(tracee)的能力，由此可以实现断点和系统调用追踪

       A tracee first needs to be attached to the tracer.  Attachment  and  subse‐
       quent commands are per thread: in a multithreaded process, every thread can
       be individually attached to a (potentially different) tracer, or  left  not
       attached  and  thus  not debugged.  Therefore, "tracee" always means "(one)
       thread", never "a (possibly multithreaded) process".  Ptrace  commands  are
       always sent to a specific tracee using a call of the form
       即tracer通过ptrace进行附加(attach)和发送命令都是针对某一个线程的而不是进程
*/
```

* • request：调试者(**tracer**)要执行的操作，常见的有PTRACE\_TRACEME，PTRACE\_ATTACH，PTRACE\_PEEKUSER，PTRACE\_SINGLESTEP等
* • pid：被调试进程(**tracee**)pid
* • addr：要读写的内存地址
* • data：如果要向目标进程写入数据那么data就是我们数据地址；如果要读取目标进程数据那么data就是保留数据的地址

ptrace系统调用会根据不同的request完成不同功能如：

* • PTRACE\_TRACEME：表示此进程即将被父进程trace，此时其他参数被忽略
* • PTRACE\_PEEKTEXT, PTRACE\_PEEKDATA：读取tracee在**addr**(虚拟内存空间)处的一个字，返回值就是读取到的字
* • PTRACE\_PEEKUSER：读取tracee的**USER area**，其包含了该进程的寄存器以及其他信息
* • PTRACE\_POKETEXT, PTRACE\_POKEDATA：复制**data**所指向的一个字到tracee的**addr**(虚拟内存空间)处
* • PTRACE\_POKEUSER：复制data所指的一个字带tracee的**USER area**
* • PTRACE\_GETREGS, PTRACE\_GETFPREGS：复制**tracee**的`通用寄存器`或者`浮点寄存器`到**tracer**的**data**所指的位置，addr被忽略
* • PTRACE\_SETREGS, PTRACE\_SETFPREGS：修改tracee的通用寄存器或者浮点寄存器
* • PTRACE\_CONT：运行被暂停的tracee进程。如果data参数非0那么就表示data是传给tracee的**信号数值**
* • PTRACE\_SYSCALL, PTRACE\_SINGLESTEP：运行被暂停的tracee进程就像PTRACE\_CONT功能，不同的是PTRACE\_SYSCALL表示运行到下一个系统调用(进入或返回)，PTRACE\_SINGLESTEP表示仅运行一条指令便停止

以下是Linux-2.4.16内核的ptrace系统调用内部实现源码：

```
asmlinkage int sys_ptrace(long request, long pid, long addr, long data)  //asmlinkage是指明该函数用堆栈来传递参数
{
    struct task_struct *child;
    struct user * dummy = NULL;
    int i, ret;

    lock_kernel();
    ret = -EPERM;
    if (request == PTRACE_TRACEME) {  /*检查traced状态是否重复*/
        /* are we already being traced? */
        if (current->ptrace & PT_PTRACED)
            goto out;
        /* set the ptrace bit in the process flags. */
        current->ptrace |= PT_PTRACED;  //current指向当前进程(task_struct)，因此PTRACE_TRACEME将当前进程设置为PT_PTRACED状态(traced)即被trace者(tracee)
        ret = 0;
        goto out;
    }
    ret = -ESRCH;
    read_lock(&tasklist_lock);    //调度链表上读锁
    child = find_task_by_pid(pid);   //获取目标pid进程结构体(task_struct)
    if (child)
        get_task_struct(child);
    read_unlock(&tasklist_lock);
    if (!child)
        goto out;

    ret = -EPERM;
    if (pid == 1)  /* you may not mess with init */
        goto out_tsk;
    /*就像gdb有直接启动并调试一个程序和附加一个进程并调试两个功能，也是基于ptrace的PTRACE_ATTACH让目标进程处于traced状态*/
    if (request == PTRACE_ATTACH) {
        ret = ptrace_attach(child);
        goto out_tsk;
    }

    ...
    /*这就是ptrace的主体，通过switch case和request完成，这里先了解部分*/
    switch (request) {
    /* when I and D space are separate, these will need to be fixed. */
    /*PTRACE_PEEKTEXT，PTRACE_PEEKDATA功能相同都是从虚拟地址addr中读取数据到data指针中*/
    case PTRACE_PEEKTEXT: /* read word at location addr. */
    case PTRACE_PEEKDATA: {
        unsigned long tmp;
        int copied;

        copied = access_process_vm(child, addr, &tmp, sizeof(tmp), 0);
        ret = -EIO;
        if (copied != sizeof(tmp))
            break;
        ret = put_user(tmp,(unsigned long *) data);
        break;
    }

    /* read the word at location addr in the USER area. */
    /*可以检查用户态内存区域(USER area),从USER区域中读取一个字节，偏移量为addr*/
    case PTRACE_PEEKUSR: {
        unsigned long tmp;

        ret = -EIO;
        if ((addr & 3) || addr < 0 ||
            addr > sizeof(struct user) - 3)
            break;

        tmp = 0;  /* Default return condition */
        if(addr < FRAME_SIZE*sizeof(long))
            tmp = getreg(child, addr);
        if(addr >= (long) &dummy->u_debugreg[0] &&
           addr <= (long) &dummy->u_debugreg[7]){
            addr -= (long) &dummy->u_debugreg[0];
            addr = addr >> 2;
            tmp = child->thread.debugreg[addr];
        }
        ret = put_user(tmp,(unsigned long *) data);
        break;
    }

    /* when I and D space are separate, this will have to be fixed. */
    /*PTRACE_POKETEXT和PTRACE_POKEDATA功能相同都是向虚拟地址addr写入来自data的数据*/
    case PTRACE_POKETEXT: /* write the word at location addr. */
    case PTRACE_POKEDATA:
        ret = 0;
        if (access_process_vm(child, addr, &data, sizeof(data), 1) == sizeof(data))
            break;
        ret = -EIO;
        break;

    case PTRACE_POKEUSR: /* write the word at location addr in the USER area */
        ret = -EIO;
        if ((addr & 3) || addr < 0 ||
            addr > sizeof(struct user) - 3)
            break;

        if (addr < FRAME_SIZE*sizeof(long)) {
            ret = putreg(child, addr, data);
            break;
        }
        /* We need to be very careful here.  We implicitly
           want to modify a portion of the task_struct, and we
           have to be selective about what portions we allow someone
           to modify. */

          ret = -EIO;
          if(addr >= (long) &dummy->u_debugreg[0] &&
             addr <= (long) &dummy->u_debugreg[7]){

              if(addr == (long) &dummy->u_debugreg[4]) break;
              if(addr == (long) &dummy->u_debugreg[5]) break;
              if(addr < (long) &dummy->u_debugreg[4] &&
                 ((unsigned long) data) >= TASK_SIZE-3) break;

              if(addr == (long) &dummy->u_debugreg[7]) {
                  data &= ~DR_CONTROL_RESERVED;
                  for(i=0; i<4; i++)
                      if ((0x5f54 >> ((data >> (16 + 4*i)) & 0xf)) & 1)
                          goto out_tsk;
              }

              addr -= (long) &dummy->u_debugreg;
              addr = addr >> 2;
              child->thread.debugreg[addr] = data;
              ret = 0;
          }
          break;
    /*都是让tracee继续运行，只是啥时候停止不同*/
    case PTRACE_SYSCALL: /* continue and stop at next (return from) syscall */
    case PTRACE_CONT: { /* restart after signal. */
        long tmp;

        ret = -EIO;
        if ((unsigned long) data > _NSIG) //data为tracer传给tracee的信号数值，这里检查范围
            break;
        if (request == PTRACE_SYSCALL)
            child->ptrace |= PT_TRACESYS; //设置PT_TRACESYS标志，为了在下一个系统调用处停止
        else
            child->ptrace &= ~PT_TRACESYS; //清除PT_TRACESYS标志，不停止
        child->exit_code = data;
    /* make sure the single step bit is not set. 清除EFLAGS的单步标志(Trap Flag)*/
        tmp = get_stack_long(child, EFL_OFFSET) & ~TRAP_FLAG;
        put_stack_long(child, EFL_OFFSET,tmp);
        wake_up_process(child);    //唤醒进程
        ret = 0;
        break;
    }

/*
 * make the child exit.  Best I can do is send it a sigkill.
 * perhaps it should be put in the status that it wants to
 * exit.
 */
    case PTRACE_KILL: {
        long tmp;

        ret = 0;
        if (child->state == TASK_ZOMBIE) /* already dead */
            break;
        child->exit_code = SIGKILL;
        /* make sure the single step bit is not set....