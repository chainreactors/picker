---
title: Kernel PWN从入门到提升
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499012&idx=1&sn=cc2bec22b8100661d3be4914e2cac64a&chksm=b18e874e86f90e58b02344269b99dc2f451d5f855c3288b328da9c9747640b3ccbfb7ba8d45b&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-23
fetch_date: 2025-10-04T10:23:00.851216
---

# Kernel PWN从入门到提升

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hk1Sic8zlRIa5ibwYu6OWUQh5YX1WJs3YrV4qT8uopDShBqDQF2bibGD4qVGY3cywEBciaUse1WTe1iaQ/0?wx_fmt=jpeg)

# Kernel PWN从入门到提升

kotoriseed

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hk1Sic8zlRIa5ibwYu6OWUQhyn7831GiaYLNtqA6rWqtsnJoj39uPJgSibyU1nRWR7TasZ9e3SQNb39A/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：kotoriseed

#

介于本人在入门kernel pwn的时候觉得当前trick种类繁多，前置知识也多得吓人，有点不知所措，且有些大佬的博客经常对一些我个人认为比较重要的点一句话带过，导致缺乏经验的我在学习过程中屡屡碰壁。所以我决定用此文章结合一道不错的例题尽可能详细的来讲一下kernel pwn从入门过渡到较高难度的部分，供想要学习kernel pwn的小伙伴们参考。

在开始看这篇文章之前，我希望小伙伴们已经掌握了kernel pwn一些最基本的操作，例如装好kernel pwn所需要的的前置环境。这一部分内容的优秀教程并不少。

另外，如果在阅读的过程中发现任何问题，都欢迎来和我交流指正。

#

#

```
一

BASIC
```

##

## **environment**

在学习kernel pwn之前，需要搭建好很多前置环境。

* qemu
* busybox
* 编译linux内核（可选）

至于具体的安装过程并不在本文的讨论范围内，如果还没完成，先自行百度解决。

##

## **文件系统**

kernel题一般都会给出一个打包好的文件系统，因此需要掌握常用到的打包/解包命令。

```
find . | cpio -o --format=newc > ./rootfs.cpiocpio -idmv < ./rootfs.cpio
```

（有时解包出来很奇怪，可能是原始cpio文件其实是以gz格式压缩后的，先gunzip解压一遍）

##

## **cred结构体**

kernel使用cred结构体记录了进程的权限，如果能劫持或伪造cred结构体，就能改变当前进程的权限。

原型如下：

```
struct cred {    atomic_t    usage;#ifdef CONFIG_DEBUG_CREDENTIALS    atomic_t    subscribers;    /* number of processes subscribed */    void        *put_addr;    unsigned    magic;#define CRED_MAGIC    0x43736564#define CRED_MAGIC_DEAD    0x44656144#endif    kuid_t        uid;        /* real UID of the task */    kgid_t        gid;        /* real GID of the task */    kuid_t        suid;        /* saved UID of the task */    kgid_t        sgid;        /* saved GID of the task */    kuid_t        euid;        /* effective UID of the task */    kgid_t        egid;        /* effective GID of the task */    kuid_t        fsuid;        /* UID for VFS ops */    kgid_t        fsgid;        /* GID for VFS ops */    unsigned    securebits;    /* SUID-less security management */    kernel_cap_t    cap_inheritable; /* caps our children can inherit */    kernel_cap_t    cap_permitted;    /* caps we're permitted */    kernel_cap_t    cap_effective;    /* caps we can actually use */    kernel_cap_t    cap_bset;    /* capability bounding set */    kernel_cap_t    cap_ambient;    /* Ambient capability set */#ifdef CONFIG_KEYS    unsigned char    jit_keyring;    /* default keyring to attach requested                     * keys to */    struct key __rcu *session_keyring; /* keyring inherited over fork */    struct key    *process_keyring; /* keyring private to this process */    struct key    *thread_keyring; /* keyring private to this thread */    struct key    *request_key_auth; /* assumed request_key authority */#endif#ifdef CONFIG_SECURITY    void        *security;    /* subjective LSM security */#endif    struct user_struct *user;    /* real user ID subscription */    struct user_namespace *user_ns; /* user_ns the caps and keyrings are relative to. */    struct group_info *group_info;    /* supplementary groups for euid/fsgid */    struct rcu_head    rcu;        /* RCU deletion hook */} __randomize_layout;
```

一般而言，我们需要想办法将uid和gid设置为0（root的uid和gid均为0）

如果能劫持到程序流程，执行以下函数也可以达到相同效果：

```
commit_creds(prepare_kernel_cred(0));commit_creds(init_cred);
```

##

## **内核态函数**

运行在内核态的函数会和用户态有些许不同。

printf -> kprintf

memcpy -> copy\_to\_user / copy\_from\_user

内核的动态分配并不会采用用户态的glibc，他的堆分配器是SLAB或SLUB。常使用的函数如下：

malloc -> kmalloc

free -> kfree

为了安全考虑，内核态也只能运行内核态的函数（smep），想要运行system等函数，必须手动切换回用户态。

常用的指令是swapgs和iretq（或者swapgs\_restore\_regs\_and\_return\_to\_usermode函数，直接对CR3寄存器的第13位取反来完成切换页表的操作，该函数在KPTI开启的版本中依然有效，而swapgs往往会寄）

然后需要在栈上存一些上下文：

```
struct pt_regs {
/* ...................... */
/* Return frame for iretq */    unsigned long ip;    unsigned long cs;    unsigned long flags;    unsigned long sp;    unsigned long ss;/* top of stack page */};
```

##

## **gdb远程调试**

以babydriver这题为例，先使用脚本extract-vmlinux提取出带符号的源码。

```
./extract-vmlinux ./bzImage > ./vmlinux
```

(脚本源码:

https://github.com/torvalds/linux/blob/master/scripts/extract-vmlinux)

(或者用这个https://github.com/marin-m/vmlinux-to-elf)

在qemu中找到babydriver.ko代码段的起始地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNQicaNbhGDU9QHecOgJsTLL3P4EwIXnIbutjyMCtSyR9W8GeL4ZoReUg/640?wx_fmt=png)

启动gdb过后导入符号表。

```
add-symbol-file ./lib/modules/4.4.72/babydriver.ko 0xffffffffc0000000
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNHuZlD7sr6g2qwLTuP12xrKDj5D5FVXoAyEu4gqfCQYibrTZ2Sqvq6Zg/640?wx_fmt=png)
然后在boot.sh中添加以下参数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchN0Q9o4HboiaMsVia22XMausx922j4ibZ7WCiaoeKA9meQQqqgTbia03gbndg/640?wx_fmt=png)

(直接-s也行)

重新启动qemu过后，gdb远程连接。

```
pwndbg> target remote 127.0.0.1:1234
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNdcVc3sg5GiclKzOicDKPkS13Cc9dPKSDELONxmlseKiansHaHHZBbGftg/640?wx_fmt=png)

这里给出我常用的一些打包和调试的脚本。

pack.sh

```
#!/bin/zsh
gcc \    ./exp.c \    -o exp    \    -masm=intel \    --static  \    -g
chmod 777 ./exp
find . | cpio -o --format=newc > ./rootfs.cpiochmod 777 ./rootfs.cpio
```

gdbinit

```
file ./vmlinuxtarget remote 127.0.0.1:1234c
```

##

## **远程脚本**

为了减小远程exp的体积，使用musl进行静态编译（）

```
import sysimport osfrom pwn import *import string
context.log_level='debug'
sla = lambda x,y : p.sendlineafter(x,y)sa =  lambda x,y : p.sendafter(x,y)ru =  lambda x   : p.recvuntil(x)
p = remote('127.0.0.1', 1234)
def send_cmd(cmd):    sla('$ ', cmd)
def upload():    lg = log.progress('Upload')    with open('exp', 'rb') as f:        data = f.read()    encoded = base64.b64encode(data)    encoded = str(encoded)[2:-1]    for i in range(0, len(encoded), 300):        lg.status('%d / %d' % (i, len(encoded)))        send_cmd('echo -n "%s" >> benc' % (encoded[i:i+300]))    send_cmd('cat benc | base64 -d > bout')    send_cmd('chmod +x bout')    lg.success()
os.system('musl-gcc -w -s -static -o3 exp.c -o exp')upload()
p.interactive()
```

#

#

```
二

ATTACK
```

##

## **Kernel UAF**

###

### babydriver

####

#### 分析

这是ciscn2017年的一道经典kernel pwn入门题。

解压rootfs.cpio后，在/lib/modules/4.4.72中找到了LKM文件babydriver.ko。

checksec只开了nx，且没有去除符号表，很方便调试和分析。

直接丢ida分析。

```
int __fastcall babyrelease(inode *inode, file *filp){  _fentry__(inode, filp);  kfree(babydev_struct.device_buf);  printk("device release\n");  return 0;}
```

在babyrelease中kfree()之后没有将babydev\_struct.device\_buf清空，从而导致了uaf漏洞。

而且babydev\_struct是一个babydevice\_t类型的公共变量，结构如下。

```
struct babydevice_t{    char *device_buf;    size_t device_buf_len;};
```

device\_buf是存一个缓冲区的指针，device\_buf\_len存该缓冲区大小。

其他的函数都很常规，

babyopen在打开一个设备的时候简单设置了一下babydev\_struct的值。

```
int __fastcall babyopen(inode *inode, file *filp){  _fentry__(inode, filp);  babydev_struct.device_buf = (char *)kmem_cache_alloc_trace(kmalloc_caches[6], 0x24000C0LL, 0x40LL);  babydev_struct.device_buf_len = 64LL;  printk("device open\n");  return 0;}
```

babywrite和babyread都只检查了一下device\_buf指针是否为空和是否越界, 然后对device\_buf进行常规的读写。

```
ssize_t __fastcall babywrite(file *filp, const char *buffer, size_t length, loff_t *offset){  size_t v4; // rdx  ssize_t result; // rax  ssize_t v6; // rbx
  _fentry__(filp, buffer);  if ( !babydev_struct.device_buf )    return -1LL;  result = -2LL;  if ( babydev_struct.device_buf_len > v4 )  {    v6 = v4;    copy_from_user();    result = v6;  }  return result;}
```

```
ssize_t __fastcall babyread(file *filp, char *buffer, size_t length, loff_t *offset){  size_t v4; // rdx  ssize_t result; // rax  ssize_t v6; // rbx
  _fentry__(filp, buffer);  if ( !babydev_struct.device_buf )    return -1LL;  result = -2LL;  if ( babydev_struct.device_buf_len > v4 )  {    v6 = v4;    copy_to_user(buffer);    result = v6;  }  return result;}
```

babyioctl比较有意思，当第二个参数command为0x10001时，可以重新kmalloc一块指定大小的object到babydev\_struct.device\_buf，从而修改了babydev\_struct的device\_buf\_len为一个新值。

```
__int64 __fastcall babyioctl(file *filp, unsigned int command, unsigned __int64 arg){  size_t v3; // rdx  size_t v4; // rbx  __int64 result; // rax
  _fentry__(filp, command);  v4 = v3;  if ( co...