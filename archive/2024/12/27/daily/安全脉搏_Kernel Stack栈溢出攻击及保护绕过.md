---
title: Kernel Stack栈溢出攻击及保护绕过
url: https://www.secpulse.com/archives/205462.html
source: 安全脉搏
date: 2024-12-27
fetch_date: 2025-10-06T19:35:22.892054
---

# Kernel Stack栈溢出攻击及保护绕过

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Kernel Stack栈溢出攻击及保护绕过

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-26

15,186

# 前言

本文介绍Linux内核的栈溢出攻击，和内核一些保护的绕过手法，通过一道内核题及其变体从浅入深一步步走进kernel世界。

# QWB\_2018\_core

## 题目分析

**start.sh**

```
qemu-system-x86_64 \
    -m 128M \
    -kernel ./bzImage \
    -initrd  ./core.cpio \
    -append "root=/dev/ram rw console=ttyS0 oops=panic panic=1 quiet kaslr" \
    -s \
    -netdev user,id=t0, -device e1000,netdev=t0,id=nic0 \
    -nographic  \
```

开启了`kaslr`保护。

> 如果自己编译的 qemu 可能会报错`network backend ‘user‘ is not compiled into this binary`，解决方法就是`sudo apt-get install libslirp-dev`，然后重新编译 `./configure --enable-slirp`。

**init**

解压 `core.cpio`(最简单的方式就是在ubuntu里，右击提取到此处)，分析 `init` 文件：

```
#!/bin/sh
mount -t proc proc /proc
mount -t sysfs sysfs /sys
mount -t devtmpfs none /dev
/sbin/mdev -s
mkdir -p /dev/pts
mount -vt devpts -o gid=4,mode=620 none /dev/pts
chmod 666 /dev/ptmx
cat /proc/kallsyms > /tmp/kallsyms
echo 1 > /proc/sys/kernel/kptr_restrict
echo 1 > /proc/sys/kernel/dmesg_restrict
ifconfig eth0 up
udhcpc -i eth0
ifconfig eth0 10.0.2.15 netmask 255.255.255.0
route add default gw 10.0.2.2
insmod /core.ko # 加载内核模块core.ko

setsid /bin/cttyhack setuidgid 1000 /bin/sh
echo 'sh end!\n'
umount /proc
umount /sys

poweroff -d 0  -f
```

* 第 9 行中把 `kallsyms` 的内容保存到了 `/tmp/kallsyms` 中，那么我们就能从 `/tmp/kallsyms` 中读取 `commit_creds`，`prepare_kernel_cred` 的函数的地址了。
* 第 10 行把 `kptr_restrict` 设为 1，这样就不能通过 `/proc/kallsyms` 查看函数地址了，但第 9 行已经把其中的信息保存到了一个可读的文件中，这句就无关紧要了。
* 第 11 行把 `dmesg_restrict` 设为 1，这样就不能通过 `dmesg` 查看 kernel 的信息了。
* 第 18 行设置了定时关机，为了避免做题时产生干扰，直接把这句删掉然后重新打包。

里面还有一个 gen\_cpio.sh 脚本，用于快速打包。

```
find . -print0 \
| cpio --null -ov --format=newc \
| gzip -9 > $1
```

> * **`KASLR`**：
>
>   `Kernel Address Space Layout Randomization`(内核地址空间布局随机化)，开启后，允许`kernel image`加载到`VMALLOC`区域的任何位置。在未开启KASLR保护机制时，内核代码段的基址为 `0xffffffff81000000`，`direct mapping area` 的基址为 `0xffff888000000000`。
> * **`FG-KASLR`**：
>
>   `Function Granular Kernel Address Space Layout Randomization`细粒度的 `kaslr`，函数级别上的 `KASLR` 优化。该保护只是在代码段打乱顺序，在数据段偏移不变，例如 `commit_creds` 函数的偏移改变但是 `init_cred` 的偏移不变。
> * **`Dmesg Restrictions`**：
>
>   通过设置`/proc/sys/kernel/dmesg_restrict`为1, 可以将`dmesg`输出的信息视为敏感信息(默认为0)
> * **`Kernel Address Display Restriction`**：
>
>   内核提供控制变量 `/proc/sys/kernel/kptr_restrict` 用于控制内核的一些输出打印。
>
> + `kptr_restrict == 2` :内核将符号地址打印为全 0 , root 和普通用户都没有权限.
> + `kptr_restrict == 1` : root 用户有权限读取,普通用户没有权限.
> + `kptr_restrict == 0` : root 和普通用户都可以读取.

**core.ko**

检查一下保护。

```
❯ checksec core/core.ko
[*] '/home/pwn/kernel/pwn/give_to_player/core/core.ko'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x0)
```

使用 IDA 继续分析.ko文件。

`init_module()` 注册了 `/proc/core`，`core_fops` 时其注册的`file_operations`结构体实例，会面会做介绍。

```
__int64 init_module()
{
  core_proc = proc_create("core", 438LL, 0LL, &core_fops);
  printk(&unk_2DE);
  return 0LL;
}
```

`exit_core()`删除 `/proc/core`。

```
__int64 exit_core()
{
  __int64 result; // rax

  if ( core_proc )
    result = remove_proc_entry("core");
  return result;
}
```

`core_ioctl()` 定义了三条命令，分别调用 `core_read(), core_copy_func()`和设置全局变量 `off`。

```
__int64 __fastcall core_ioctl(__int64 a1, int a2, __int64 a3)
{
  switch ( a2 )
  {
    case 0x6677889B:
      core_read(a3);
      break;
    case 0x6677889C:
      printk(&unk_2CD);
      off = a3;
      break;
    case 0x6677889A:
      printk(&unk_2B3);
      core_copy_func(a3);
      break;
  }
  return 0LL;
}
```

`core_read()` 从 `v4[off]` 拷贝 64 个字节到用户空间，但要注意的是全局变量 `off` 是我们能够控制的，因此可以合理的控制 `off` 来 `leak canary` 和一些地址 。

```
void __fastcall core_read(__int64 a1)
{
  __int64 v1; // rbx
  char *v2; // rdi
  signed __int64 i; // rcx
  char v4[64]; // [rsp+0h] [rbp-50h]
  /*
  * canary保存在rsp+0x40的位置，
  * 我们通过设置off为0x40，即可将其读取出来。
  */
  unsigned __int64 v5; // [rsp+40h] [rbp-10h]

  v1 = a1;
  v5 = __readgsqword(0x28u);
  printk("\x016core: called core_read\n");
  printk("\x016%d %p\n");
  v2 = v4;
  for ( i = 16LL; i; --i )
  {
    *(_DWORD *)v2 = 0;
    v2 += 4;
  }
  strcpy(v4, "Welcome to the QWB CTF challenge.\n");
  if ( copy_to_user(v1, &v4[off], 64LL) )
    __asm { swapgs }
}
```

`core_copy_func()` 从全局变量 `name` 中拷贝数据到局部变量中，长度是由我们指定的，当要注意的是 `qmemcpy` 用的是 `unsigned __int16`，但传递的长度是 `signed __int64`，因此如果控制传入的长度为 `0xffffffffffff0000|(0x100)` 等值，就可以栈溢出了。

```
__int64 __fastcall core_copy_func(__int64 a1)
{
  __int64 result; // rax
  _QWORD v2[10]; // [rsp+0h] [rbp-50h] BYREF

  v2[8] = __readgsqword(0x28u);
  printk(&unk_215);
  // 这里用的jg判断，为有符号判断，0xffffffffffff0000|(0x100) 会判定为负从而绕过。
  if ( a1 > 63 )
  {
    printk(&unk_2A1);
    return 0xFFFFFFFFLL;
  }
  else
  {
    result = 0LL;
    // 栈溢出。
    qmemcpy(v2, &name, (unsigned __int16)a1);
  }
  return result;
}
```

`core_write()` 向全局变量 `name` 上写，这样通过 `core_write()` 和 `core_copy_func()` 就可以控制 `ropchain` 了 。

```
signed __int64 __fastcall core_write(__int64 a1, __int64 a2, unsigned __int64 a3)
{
  unsigned __int64 v3; // rbx

  v3 = a3;
  printk("\x016core: called core_writen");
  if ( v3 <= 0x800 && !copy_from_user(name, a2, v3) )
    return (unsigned int)v3;
  printk("\x016core: error copying data from userspacen");
  return 0xFFFFFFF2LL;
}
```

> **字符驱动设备**
>
> 内核注册字符设备驱动设备时会用到`file_operations`结构体，`file_operations` 结构体中的成员函数是字符设备驱动程序设计的主体内容，结构体中的一些指针比如`open()` 、`write()` 、`read()` 、`close()` 等系统调用时最终会被内核调用，我们可以通过指定指针指向的内容修改其默认值为我们自定义的函数，这样我们在类似`read(dev_fd, buf, 0x100)`时就会调用我们自定义的`my_read`函数。
>
> 它还有一个指针为`unlocked_ioctl`，我们在用户态时可以使用系统调用`ioctl`去访问控制内核注册的设备（`ioctl`系统调用号为`0x10`，由`rax`保存，需要注意的时，系统调用和用户传参的`rdi,rsi,rdx,rcx,r8,r9`不同，系统调用第四个传参寄存器为r10，即`rd...