---
title: Linux内核学习笔记
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493067&idx=1&sn=67464053a78548c2b29abd59ecd456f4&chksm=b18e900186f9191747c2f400abef5a0e77781c2dfc59a0921f98d04d0f2541be1987ffbaeed8&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-20
fetch_date: 2025-10-04T04:23:09.353836
---

# Linux内核学习笔记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GtjFCicShxWBP39EGM7MybTwn2n9VY3AvpquibpHUAm23G4jP7QIljiaB4pQt3ib96o5mpNPFrnbGC0g/0?wx_fmt=jpeg)

# Linux内核学习笔记

e\*16 a

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GtjFCicShxWBP39EGM7MybTEkQfGaj1O7QF87bQ81A3ial67xUMog6kCMeMyhxjS5SbYfVDV72kGuw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：e\*16 a

以下是基于linux0.11的代码。

#

#

```
一

内核的五大结构
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HGXJIRb0n0OHImmLILKpctm8Mu1iabdukuvwlxkhNw66CkTEXVgjfBZWeZsh6BR1JGmibiaXibc9OGlQ/640?wx_fmt=png)

#

#

```
二

中断工作流程
```

##

## **1、ARM回忆**

（1）做CPU工作模式的转化

（2）进行寄存器的拷贝与压栈

（3）设置中断向量表

（4）保存正常运行的函数返回值

（5）跳转到对应的中断服务函数上运行

（6）进行模式的复原及寄存器的复原

（7）跳转回正常工作的函数地址继续运行

##

## **2、linux中中断的工作流程**

（1）将所有寄存器值入栈

（2）将异常吗入栈(中断号)

（3）将当前函数的返回地址入栈

（4）调用中断函数

（5）返回地址出栈

（6）寄存器值出栈

##

##

## **3、中断源码**

中断前后的处理 中断的执行

硬件中断的处理过程 asm.s trap.c

软件及系统调用的处理过程 system\_call.s fork.c/signal.c/exit.c/sys.c

### ① asm.s代码及trap.c分析 (OPENING)

### ② system\_call.s代码及fork.c/signal.c/exit.c/sys.c分析

####

#### （1） fork.c

在system\_call.s内有存在fork的系统调用，先call \_find\_empty\_process，然后call \_copy\_process。

```
.align 2_sys_fork:    call _find_empty_process    testl %eax,%eax    js 1f    push %gs    pushl %esi    pushl %edi    pushl %ebp    pushl %eax    call _copy_process    addl $20,%esp1:    ret
```

```
#include <errno.h>#include <linux/sched.h>#include <linux/kernel.h>#include <asm/segment.h>#include <asm/system.h> extern void write_verify(unsigned long address); long last_pid=0; void verify_area(void * addr,int size){    unsigned long start;     start = (unsigned long) addr;    size += start & 0xfff;    start &= 0xfffff000;    start += get_base(current->ldt[2]);    while (size>0) {        size -= 4096;        write_verify(start);        start += 4096;    }} int copy_mem(int nr,struct task_struct * p){    unsigned long old_data_base,new_data_base,data_limit;    unsigned long old_code_base,new_code_base,code_limit;     code_limit=get_limit(0x0f);    data_limit=get_limit(0x17);    old_code_base = get_base(current->ldt[1]);    old_data_base = get_base(current->ldt[2]);    if (old_data_base != old_code_base)        panic("We don't support separate I&D");    if (data_limit < code_limit)        panic("Bad data_limit");    new_data_base = new_code_base = nr * 0x4000000;    p->start_code = new_code_base;    set_base(p->ldt[1],new_code_base);    set_base(p->ldt[2],new_data_base);    if (copy_page_tables(old_data_base,new_data_base,data_limit)) {        free_page_tables(new_data_base,data_limit);        return -ENOMEM;    }    return 0;} /* *  Ok, this is the main fork-routine. It copies the system process * information (task[nr]) and sets up the necessary registers. It * also copies the data segment in it's entirety. */int copy_process(int nr,long ebp,long edi,long esi,long gs,long none,        long ebx,long ecx,long edx,        long fs,long es,long ds,        long eip,long cs,long eflags,long esp,long ss){    struct task_struct *p;   //创建子进程的task_struct结构体    int i;    struct file *f;     p = (struct task_struct *) get_free_page();    if (!p)        return -EAGAIN;    task[nr] = p;   //将子进程存到task链表中    *p = *current;    /* NOTE! this doesn't copy the supervisor stack */    //下面开始设置结构体内容    p->state = TASK_UNINTERRUPTIBLE;    p->pid = last_pid;    p->father = current->pid;    p->counter = p->priority;    p->signal = 0;    p->alarm = 0;    p->leader = 0;        /* process leadership doesn't inherit */    p->utime = p->stime = 0;    p->cutime = p->cstime = 0;    p->start_time = jiffies;    p->tss.back_link = 0;    p->tss.esp0 = PAGE_SIZE + (long) p;    p->tss.ss0 = 0x10;    p->tss.eip = eip;    p->tss.eflags = eflags;    p->tss.eax = 0;    p->tss.ecx = ecx;    p->tss.edx = edx;    p->tss.ebx = ebx;    p->tss.esp = esp;    p->tss.ebp = ebp;    p->tss.esi = esi;    p->tss.edi = edi;    p->tss.es = es & 0xffff;    p->tss.cs = cs & 0xffff;    p->tss.ss = ss & 0xffff;    p->tss.ds = ds & 0xffff;    p->tss.fs = fs & 0xffff;    p->tss.gs = gs & 0xffff;    p->tss.ldt = _LDT(nr);    p->tss.trace_bitmap = 0x80000000;    if (last_task_used_math == current)        __asm__("clts ; fnsave %0"::"m" (p->tss.i387));  //如果父进程用了协处理器，需要在tss段进行设置    if (copy_mem(nr,p)) {  //内存拷贝        task[nr] = NULL;        free_page((long) p);        return -EAGAIN;    }    for (i=0; i<NR_OPEN;i++)        if (f=p->filp[i])            f->f_count++;    if (current->pwd)        current->pwd->i_count++;    if (current->root)        current->root->i_count++;    if (current->executable)        current->executable->i_count++;    set_tss_desc(gdt+(nr<<1)+FIRST_TSS_ENTRY,&(p->tss));    set_ldt_desc(gdt+(nr<<1)+FIRST_LDT_ENTRY,&(p->ldt));    p->state = TASK_RUNNING;    /* do this last, just in case */    return last_pid; } int find_empty_process(void){    int i;     repeat:        if ((++last_pid)<0) last_pid=1;        for(i=0 ; i<NR_TASKS ; i++)            if (task[i] && task[i]->pid == last_pid) goto repeat;    for(i=1 ; i<NR_TASKS ; i++)        if (!task[i])              return i;    return -EAGAIN;}
```

① 在task链表中找一个进程空位存放

② 创建一个task\_struct

③ 设置task\_struct

####

#### （2）signal.c

这里只是进行一个简单的分析，详细分析请见第五章。

```
#include <linux/sched.h>#include <linux/kernel.h>#include <asm/segment.h> #include <signal.h> volatile void do_exit(int error_code); int sys_sgetmask(){    return current->blocked;} int sys_ssetmask(int newmask){    int old=current->blocked;     current->blocked = newmask & ~(1<<(SIGKILL-1));    return old;} static inline void save_old(char * from,char * to){    int i;     verify_area(to, sizeof(struct sigaction));    for (i=0 ; i< sizeof(struct sigaction) ; i++) {        put_fs_byte(*from,to);        from++;        to++;    }} static inline void get_new(char * from,char * to){    int i;     for (i=0 ; i< sizeof(struct sigaction) ; i++)        *(to++) = get_fs_byte(from++);} int sys_signal(int signum, long handler, long restorer){    struct sigaction tmp;     if (signum<1 || signum>32 || signum==SIGKILL) //判断信号值是否合法        return -1;    tmp.sa_handler = (void (*)(int)) handler;    tmp.sa_mask = 0;    tmp.sa_flags = SA_ONESHOT | SA_NOMASK;    tmp.sa_restorer = (void (*)(void)) restorer;   //设置sigaction结构体    handler = (long) current->sigaction[signum-1].sa_handler;    current->sigaction[signum-1] = tmp; //将当前进程对应的信号结构体改为新分配的结构体    return handler; //返回处理函数} int sys_sigaction(int signum, const struct sigaction * action,    struct sigaction * oldaction){    struct sigaction tmp;     if (signum<1 || signum>32 || signum==SIGKILL)        return -1;    tmp = current->sigaction[signum-1];    get_new((char *) action,        (char *) (signum-1+current->sigaction));    if (oldaction)        save_old((char *) &tmp,(char *) oldaction);    if (current->sigaction[signum-1].sa_flags & SA_NOMASK)        current->sigaction[signum-1].sa_mask = 0;    else        current->sigaction[signum-1].sa_mask |= (1<<(signum-1));    return 0;} void do_signal(long signr,long eax, long ebx, long ecx, long edx,    long fs, long es, long ds,    long eip, long cs, long eflags,    unsigned long * esp, long ss){    unsigned long sa_handler;    long old_eip=eip;    struct sigaction * sa = current->sigaction + signr - 1;    int longs;    unsigned long * tmp_esp;     sa_handler = (unsigned long) sa->sa_handler;    if (sa_handler==1)        return;    if (!sa_handler) {        if (signr==SIGCHLD)            return;        else            do_exit(1<<(signr-1));    }    if (sa->sa_flags & SA_ONESHOT)        sa->sa_handler = NULL;    *(&eip) = sa_handler;    longs = (sa->sa_flags & SA_NOMASK)?7:8;    *(&esp) -= longs;    verify_area(esp,longs*4);    tmp_esp=esp;    put_fs_long((long) sa->sa_restorer,tmp_esp++);    put_fs_long(signr,tmp_esp++);    if (!(sa->sa_flags & SA_NOMASK))        put_fs_long(current->blocked,tmp_esp++);    put_fs_long(eax,tmp_esp++);    put_fs_long(ecx,tmp_esp++);    put_fs_long(edx,tmp_esp++);    put_fs_long(eflags,tmp_esp++);    put_fs_long(old_eip,tmp_esp++);    current->blocked |= s...