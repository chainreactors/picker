---
title: linux跟踪技术之ebpf
url: https://www.secpulse.com/archives/194396.html
source: 安全脉搏
date: 2022-12-31
fetch_date: 2025-10-04T02:47:11.126244
---

# linux跟踪技术之ebpf

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

# linux跟踪技术之ebpf

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-30

43,660

## ebpf简介

eBPF是一项革命性的技术，起源于 Linux 内核，可以在操作系统内核等特权上下文中运行沙盒程序。它可以安全有效地扩展内核的功能，而无需更改内核源代码或加载内核模块。比如，使用ebpf可以追踪任何内核导出函数的参数，返回值，以实现kernel hook 的效果；通过ebpf,还可以在网络封包到达内核协议栈之前就进行处理，这可以实现流量控制，甚至隐蔽通信。

## ebpf追踪

ebpf本质上只是运行在linux 内核中的虚拟机，要发挥其强大的能力还是要跟linux kernel 自带的追踪功能搭配：

* • kprobe
* • uprobe
* • tracepoint
* • USDT

通常可以通过以下三种工具使用ebpf：

* • bcc
* • libbpf
* • bpftrace

## bcc

BCC 是一个用于创建高效内核跟踪和操作程序的工具包，包括几个有用的工具和示例。它利用扩展的 BPF（Berkeley Packet Filters），正式名称为 eBPF，这是 Linux 3.15 中首次添加的新功能。BCC 使用的大部分内容都需要 Linux 4.1 及更高版本。

### 源码安装bcc v0.25.0

首先clone bcc 源码仓库

> git clone https://github.com/iovisor/bcc.git git checkout v0.25.0 git submodule init git submodule update

bcc 从v0.10.0开始使用libbpf 并通过submodule 的形式加入源码树，所以这里需要更新并拉取子模块

安装依赖

> apt install flex bison libdebuginfod-dev libclang-14-dev

编译bcc

> mkdir build && cd build cmake -DCMAKE\_BUILD\_TYPE=Release .. make -j #n取决于机器的cpu核心数

编译安装完成后，在python3中就能使用bcc模块了 安装bcc时会在/usr/share/bcc目录下安装bcc自带的示例脚本和工具脚本，以及manual 文档 可以直接使用man -M /usr/share/bcc/man 来查询

### 使用python + bcc 跟踪内核函数

bcc 自带的工具execsnoop可以跟踪execv系统调用，其源代码如下：

```
#!/usr/bin/python
# @lint-avoid-python-3-compatibility-imports
#
# execsnoop Trace new processes via exec() syscalls.
#           For Linux, uses BCC, eBPF. Embedded C.
#
# USAGE: execsnoop [-h] [-T] [-t] [-x] [-q] [-n NAME] [-l LINE]
#                  [--max-args MAX_ARGS]
#
# This currently will print up to a maximum of 19 arguments, plus the process
# name, so 20 fields in total (MAXARG).
#
# This won't catch all new processes: an application may fork() but not exec().
#
# Copyright 2016 Netflix, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")
#
# 07-Feb-2016   Brendan Gregg   Created this.

from __future__ import print_function
from bcc import BPF
from bcc.containers import filter_by_containers
from bcc.utils import ArgString, printb
import bcc.utils as utils
import argparse
import re
import time
import pwd
from collections import defaultdict
from time import strftime

def parse_uid(user):
    try:
        result = int(user)
    except ValueError:
        try:
            user_info = pwd.getpwnam(user)
        except KeyError:
            raise argparse.ArgumentTypeError(
                "{0!r} is not valid UID or user entry".format(user))
        else:
            return user_info.pw_uid
    else:
        # Maybe validate if UID < 0 ?
        return result

# arguments
examples = """examples:
    ./execsnoop           # trace all exec() syscalls
    ./execsnoop -x        # include failed exec()s
    ./execsnoop -T        # include time (HH:MM:SS)
    ./execsnoop -U        # include UID
    ./execsnoop -u 1000   # only trace UID 1000
    ./execsnoop -u user   # get user UID and trace only them
    ./execsnoop -t        # include timestamps
    ./execsnoop -q        # add "quotemarks" around arguments
    ./execsnoop -n main   # only print command lines containing "main"
    ./execsnoop -l tpkg   # only print command where arguments contains "tpkg"
    ./execsnoop --cgroupmap mappath  # only trace cgroups in this BPF map
    ./execsnoop --mntnsmap mappath   # only trace mount namespaces in the map
"""
parser = argparse.ArgumentParser(
    description="Trace exec() syscalls",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=examples)
parser.add_argument("-T", "--time", action="store_true",
    help="include time column on output (HH:MM:SS)")
parser.add_argument("-t", "--timestamp", action="store_true",
    help="include timestamp on output")
parser.add_argument("-x", "--fails", action="store_true",
    help="include failed exec()s")
parser.add_argument("--cgroupmap",
    help="trace cgroups in this BPF map only")
parser.add_argument("--mntnsmap",
    help="trace mount namespaces in this BPF map only")
parser.add_argument("-u", "--uid", type=parse_uid, metavar='USER',
    help="trace this UID only")
parser.add_argument("-q", "--quote", action="store_true",
    help="Add quotemarks (") around arguments."
    )
parser.add_argument("-n", "--name",
    type=ArgString,
    help="only print commands matching this name (regex), any arg")
parser.add_argument("-l", "--line",
    type=ArgString,
    help="only print commands where arg contains this line (regex)")
parser.add_argument("-U", "--print-uid", action="store_true",
    help="print UID column")
parser.add_argument("--max-args", default="20",
    help="maximum number of arguments parsed and displayed, defaults to 20")
parser.add_argument("--ebpf", action="store_true",
    help=argparse.SUPPRESS)
args = parser.parse_args()

# define BPF program
bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>

#define ARGSIZE  128

enum event_type {
    EVENT_ARG,
    EVENT_RET,
};

struct data_t {
    u32 pid;  // PID as in the userspace term (i.e. task->tgid in kernel)
    u32 ppid; // Parent PID as in the userspace term (i.e task->real_parent->tgid in kernel)
    u32 uid;
    char comm[TASK_COMM_LEN];
    enum event_type type;
    char argv[ARGSIZE];
    int retval;
};

BPF_PERF_OUTPUT(events);

static int __submit_arg(struct pt_regs *ctx, void *ptr, struct data_t *data)
{
    bpf_probe_read_user(data->argv, sizeof(data->argv), ptr);
    events.perf_submit(ctx, data, sizeof(struct data_t));
    return 1;
}

static int submit_arg(struct pt_regs *ctx, void *ptr, struct data_t *data)
{
    const char *argp = NULL;
    bpf_probe_read_user(&argp, sizeof(argp), ptr);
    if (argp) {
        return __submit_arg(ctx, (void *)(argp), data);
    }
    return 0;
}

int syscall__execve(struc...