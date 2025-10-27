---
title: Linux kernel 堆溢出利用方法（二）
url: https://www.secpulse.com/archives/205619.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:13.922495
---

# Linux kernel 堆溢出利用方法（二）

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

# Linux kernel 堆溢出利用方法（二）

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

8,525

## 前言

本文我们通过我们的老朋友`heap_bof`来讲解`Linux kernel`中`off-by-null`的利用手法。在通过讲解另一道相对来说比较困难的`kernel off-by-null + docker escape`来深入了解这种漏洞的利用手法。（没了解过docker逃逸的朋友也可以看懂，毕竟有了`root`权限后，`docker`逃逸就变的相对简单了）。

## off by null

我们还是使用上一篇的例题`heap_bof`来讲解这种利用手法，现在我们假设这道题没有提供`free`，并且只有单字节溢出，并且溢出的单字节只能是`NULL`，那么我们应该怎麼去利用呢？

### 利用思路

**boot.sh**

```
#!/bin/bash

qemu-system-x86_64 \
  -initrd rootfs.img \
  -kernel bzImage \
  -m 1G \
  -append 'console=ttyS0 root=/dev/ram oops=panic panic=1 quiet nokaslr' \
  -monitor /dev/null \
  -s \
  -cpu kvm64 \
  -smp cores=1,threads=2 \
  --nographic
```

**poll系统调用**

```
/*
*   @fds: pollfd类型的一个数组
*   @nfds: 前面的参数fds中条目的个数
*   @timeout: 事件发生的毫秒数
*/
int poll(struct pollfd *fds, nfds_t nfds, int timeout);
```

`poll_list` 结构体对象是在调用 `poll()` 时分配，该调用可以监视 `1` 个或多个文件描述符的活动。

```
struct pollfd {
    int fd;
    short events;
    short revents;
};

struct poll_list {
    struct poll_list *next; // 指向下一个poll_list
    int len; // 对应于条目数组中pollfd结构的数量
    struct pollfd entries[]; // 存储pollfd结构的数组
};
```

`poll_list` 结构如下图所示，前 `30` 个 `poll_fd` 在栈上，后面的都在堆上，最多 `510` 个 `poll_fd` 在一个堆上的 `poll_list` 上，堆上的 `poll_list` 最大为 `0x1000`。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411071659933.png)

**poll\_list 分配/释放**

`do_sys_poll` 函数完成 `poll_list` 的分配和释放。`poll_list` 的是超时自动释放的，我们可以指定 `poll_list` 的释放时间。

```
#define POLL_STACK_ALLOC    256
#define PAGE_SIZE 4096
//(4096-16)/8 = 510(堆上存放pollfd最大数量)
#define POLLFD_PER_PAGE  ((PAGE_SIZE-sizeof(struct poll_list)) / sizeof(struct pollfd))
//(256-16)/8 = 30 (栈上存放pollfd最大数量)
#define N_STACK_PPS ((sizeof(stack_pps) - sizeof(struct poll_list))  / sizeof(struct pollfd))

[...]

static int do_sys_poll(struct pollfd __user *ufds, unsigned int nfds,
        struct timespec64 *end_time)
{

    struct poll_wqueues table;
    int err = -EFAULT, fdcount, len;
    /* Allocate small arguments on the stack to save memory and be
       faster - use long to make sure the buffer is aligned properly
       on 64 bit archs to avoid unaligned access */

    /*
    *  [1] stack_pps 256 字节的栈缓冲区, 负责存储前 30 个 pollfd entry
    */
    long stack_pps[POLL_STACK_ALLOC/sizeof(long)];
    struct poll_list *const head = (struct poll_list *)stack_pps;
    struct poll_list *walk = head;
    unsigned long todo = nfds;

    if (nfds > rlimit(RLIMIT_NOFILE))
        return -EINVAL;
    /*
    *  [2] 前30个 pollfd entry 先存放在栈上，节省内存和时间
    */
    len = min_t(unsigned int, nfds, N_STACK_PPS);

    for (;;) {
        walk->next = NULL;
        walk->len = len;
        if (!len)
            break;

        if (copy_from_user(walk->entries, ufds + nfds-todo, sizeof(struct pollfd) * walk->len))
            goto out_fds;

        todo -= walk->len;
        if (!todo)
            break;
        /*
        *   [3] 如果提交超过30个 pollfd entries，就会把多出来的 pollfd 放在内核堆上。
        *   每个page 最多存 POLLFD_PER_PAGE (510) 个entry,
        *   超过这个数，则分配新的 poll_list, 依次循环直到存下所有传入的 entry
        */
        len = min(todo, POLLFD_PER_PAGE);
        /*
        *   [4] 只要控制好被监控的文件描述符数量，就能控制分配size，从 kmalloc-32 到 kmalloc-4k
        */
        walk = walk->next = kmalloc(struct_size(walk, entries, len), GFP_KERNEL);
        if (!walk) {
            err = -ENOMEM;
            goto out_fds;
        }
    }

    poll_initwait(&table);
    /*
    *   [5] 分配完 poll_list 对象后，调用 do_poll() 来监控这些文件描述符，直到发生特定 event 或者超时。
    *   这里 end_time 就是最初传给 poll() 的超时变量, 这表示 poll_list 对象可以在内存中保存任意时长，超时后自动释放。
    */
    fdcount = do_poll(head, &table, end_time);
    poll_freewait(&table);

    if (!user_write_access_begin(ufds, nfds * sizeof(*ufds))and)
        goto out_fds;

    for (walk = head; walk; walk = walk->next) {
        struct pollfd *fds = walk->entries;
        int j;

        for (j = walk->len; j; fds++, ufds++, j--)
            unsafe_put_user(fds->revents, &ufds->revents, Efault);
    }
    user_write_access_end();

    err = fdcount;
out_fds:
    walk = head->next;
    while (walk) {      // [6] 释放 poll_list: 遍历单链表, 释放每一个 poll_list, 这里可以利用
        struct poll_list *pos = walk;
        walk = walk->next;
        kfree(pos);
    }

    return err;

Efault:
    user_write_access_end();
    err = -EFAULT;
    goto out_fds;
}
```

我们可以去找到一些结构体，其头 `8` 字节是一个指针，然后利用 `off by null` 去损坏该指针，比如使得 `0xXXXXa0` 变成 `0xXXXX00`，然后就可以考虑利用堆喷去构造 `UAF` 了。

**详细流程**

1. 首先分配 `kmalloc-4096` 大小的结构题在`ptr[0]`；
2. 然后构造这样的`poll_list`结构体。

   ![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411071659934.png)
3. 利用`off-by-null`将`poll_list->next`的最后一个字节改为空。然后大量分配`kmalloc-32`的`obj`内存，这里只所以是 `32` 字节大小是因为要与后面的 `seq_operations` 配合，并且 `32` 大小的 `object` 其低字节是可能为 `\x00` 的，其低字节为 `0x20`、`0x40`、`0x80` 、`0xa0`、`0xc0`、`0xe0`、`0x00`。运气好可以被我们篡改后的`poll_list->next`指到。但对于这道题来说我们没有足够的堆块用于堆喷，所以成功率是极低的。

   ![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411071659935.png)
4. 等待`poll_list`线程执行完毕，并且我们分配的`kmalloc-32`被错误释放，分配大量的`seq_operations`，运气好可以正好被分配到我们释放的`kmalloc-32`，形成`UAF`，这样我们就可以利用`UAF`修改`seq_operations->start`指针指向提权代码。
5. 提权可以参考上一篇文章，利用栈上的残留值来`bypass kaslr`。

### exp

```
#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

#include <asm/ldt.h>
#include <assert.h>
#include <ctype.h>
#include <errno.h>
#include <fcntl.h>
#include <linux/keyctl.h>
#include <linux/userfaultfd.h>
#include <poll.h>
#include <pthread.h>
#include <sched.h>
#include <semaphore.h>
#include <signal.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/ipc.h>
#include <sys/mman.h>
#include <sys/msg.h>
#include <sys/prctl.h>
#include <sys/sem.h>
#include <sys/sh...