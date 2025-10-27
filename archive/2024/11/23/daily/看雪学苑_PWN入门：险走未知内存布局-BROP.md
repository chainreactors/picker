---
title: PWN入门：险走未知内存布局-BROP
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458583664&idx=2&sn=80fd69df6cab019c3a1f3094e095ee4c&chksm=b18c32fa86fbbbec1266ee429c3b2e6370b34843c6d0d4d8ab934a664633fa6d8b5184de3fd8&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-23
fetch_date: 2025-10-06T19:18:38.970823
---

# PWN入门：险走未知内存布局-BROP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HprcLHZFMUZ3KNdpeqwlyan7gXjLjJDm4eh0h1uVssyXjvYDZ2kZykqibT4ickjpPGiafCMKicDlMgPg/0?wx_fmt=jpeg)

# PWN入门：险走未知内存布局-BROP

福建炒饭乡会

看雪学苑

# BROP介绍

BROP的全称是`Bind ROP`，之在不知道程序内存布局的情况下完成ROP攻击，在这里BROP有两个基础的要求，一是程序在崩溃后自带重新启动，二是重新启动后内存布局不会发生变化。

有了这两个基础条件的加持，我们就可以保证找到的地址是可以一直使用的，不至于产生“过期”的问题。

当正确的地址应该怎么样确定呢？既然地址不会“过期”，那遍历当然是一个非常有效的手段。

对于一个64位系统而言，尽管寻址时它只是使用48位（即2482^{48}248字节，相当于256TB）地址空间进行寻址，但这个地址空间范围也是相当大了。

想要遍历地址也要有个范围吧！

```
用户态空间：0x0000000000000000 - 0x00007FFFFFFFFFFF
内核态空间：0xFFFF800000000000 - 0xFFFFFFFFFFFFFFFF
```

不错，Linux系统是的确给了个范围，在Linux系统当中将用户态空间和内核态空间做了隔离，内核通过`TASK_SIZE_MAX`宏分为“楚河汉届”，该宏标明了用户态空间的最大地址。

## 用户态程序地址的规律

当你熟悉Linux系统之后就会知道，用户态的地址是由规律可言的，下面会介绍这些规律。

在了解这些规律之前，我们首先需要知道什么是PIE。

### PIE为什么存在？

在现代计算机系统当中，虽然内存资源是有限的，但是进程间的地址空间都是独立的，即在进程眼中自己都是占用着完整的内存空间，无需操心内存情况，至于物理内存资源是否真的可用，就要看操作系统如何进行调度了。

在独立的进程空间中，进程拥有了自由度，因此给不同的进程分配同样的内存布局也不会出现问题，直接在编译期分配固定的内存地址也不会带来问题。

尽管进程直接使用固定的内存地址不会带来内存使用方面的问题，但是固定的内存地址却会给黑客带来极大方便，为了缓解这一安全问题，Linux和GCC引入了PIE机制。

PIE的全称是`Position-independent Executable`，其含义是与位置无关的可执行文件，当然也可也将它称作是PIC（`Position-independent Code`与位置无关的代码）。

PIE机制允许程序不使用固定的内存地址，使得程序可以被加载到任意的内存地址上，进而使得黑客无法方便的得知程序的内存布局情况。

开启PIE机制后会导致性能受到影响，LD程序允许通过`LD_DEBUG=statistics`查看程序加载过程中的性能统计信息。

```
LD_DEBUG=statistics

6544:
6544:     runtime linker statistics:
6544:       total startup time in dynamic loader: 4001326 cycles
6544:                 time needed for relocation: 24288 cycles (.6%)
6544:                      number of relocations: 83
6544:           number of relocations from cache: 7
6544:             number of relative relocations: 0
6544:                time needed to load objects: 41238 cycles (1.0%)
```

下面列出如何控制LD链接器开关PIE功能。

```
开启PIE：ld -fPIE    -pie    -fPIC
关闭PIE：ld -fno-PIE -no-pie -fno-PIC
```

### 无PIE时的内存地址规律

当PIE功能关闭时，程序的固定地址是由LD动态链接器进行设置的，可以通过`-verbose`查看指定的`text-segment`代表的起始地址，如果想要查看其他的架构情况。

```
amd64：
ld -verbose | grep -i text-segment
PROVIDE (__executable_start = SEGMENT_START("text-segment", 0x400000)); . = SEGMENT_START("text-segment", 0x400000) + SIZEOF_HEADERS;

i386：
ld -melf_i386 -verbose | grep -i text-segment
PROVIDE (__executable_start = SEGMENT_START("text-segment", 0x08048000)); . = SEGMENT_START("text-segment", 0x08048000) + SIZEOF_HEADERS;
```

当然上面的地址并不是一定的，LD链接器支持添加链接选项在链接期动态的选择内存地址。

```
-Wl,-Ttext-segment=xxxx

-Wl,-Ttext-segment=0x10000
(gdb) disassemble
Dump of assembler code for function main:
   0x000000000001116d <+0>:     push   %rbp
   0x000000000001116e <+1>:     mov    %rsp,%rbp
   ......
```

但是这个设置的地址是不可以小于0x10000（64kb）的，在计算机中存在着空指针错误，但这个空指针并不一定要是0x0，低于内核设置的`mmap_min_addr`都算作是空指针。

```
sudo sysctl -a | grep mmap

vm.hugetlb_optimize_vmemmap = 0
vm.mmap_min_addr = 65536
vm.mmap_rnd_bits = 28
vm.mmap_rnd_compat_bits = 8

ls /proc/sys/vm
admin_reserve_kbytes         dirtytime_expire_seconds   max_map_count              nr_hugepages              overcommit_ratio               user_reserve_kbytes
compaction_proactiveness     dirty_writeback_centisecs  memory_failure_early_kill  nr_hugepages_mempolicy    page-cluster                   vfs_cache_pressure
compact_memory               drop_caches                memory_failure_recovery    nr_overcommit_hugepages   page_lock_unfairness           watermark_boost_factor
compact_unevictable_allowed  extfrag_threshold          min_free_kbytes            numa_stat                 panic_on_oom                   watermark_scale_factor
dirty_background_bytes       hugetlb_optimize_vmemmap   min_slab_ratio             numa_zonelist_order       percpu_pagelist_high_fraction  zone_reclaim_mode
dirty_background_ratio       hugetlb_shm_group          min_unmapped_ratio         oom_dump_tasks            stat_interval
dirty_bytes                  laptop_mode                mmap_min_addr              oom_kill_allocating_task  stat_refresh
dirty_expire_centisecs       legacy_va_layout           mmap_rnd_bits              overcommit_kbytes         swappiness
dirty_ratio                  lowmem_reserve_ratio       mmap_rnd_compat_bits       overcommit_memory         unprivileged_userfaultfd
```

`mmap_min_addr`用于现在用户态程序可以申请到的最小内存地址，代表着虚拟地址空间的下界。对于C语言来讲，一个指针类型的变量在未初始化时默认就是`NULL`零值，且期望程序访问空指针时出现崩溃，当没有`mmap_min_addr`的限制时，零地址也是可以被使用的（与预期不符），假如零地址上存在被写入的内容，那么攻击者既可以借助任意的未初始化指针对零地址上的资源进行滥用，导致安全问题出现。

```
sudo sysctl -w vm.mmap_min_addr="0"

被映射的空间：
00000000-00001000 rwxp 00000000 00:00 0

源代码：
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <bits/mman-linux.h>

static int vuln(char* data)
{
    char cmd[0x100];

    strncpy(cmd, data, 0x100);
    system(cmd);
}

int main(void)
{
    char* msg = "/bin/sh\0";

    mmap(0, 0x1000, PROT_READ  |PROT_WRITE | PROT_EXEC,
        MAP_FIXED | MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    perror("mmap");
    memcpy(0, msg, sizeof(msg));

    msg = NULL;
    vuln(msg);
}

程序运行结果：
./null_ptr s
mmap: Success
$ ls
main.c  Makefile  null_ptr  obj
$ exit
```

不管是AMD64架构还是i386架构图，它们都选择向更远离`mmap_min_addr`记录的地址处映射程序。

### 有PIE时的内存地址规律

在PIE机制开启时，ELF文件内部就不会在直接分配内存地址，转为只分配偏移值，程序被加载进入内核后，会被分配一个基地址，基地址+偏移值组成了一个可用的内存地址。

### 内核如何区分程序是否启用PIE

不同程序间的虚拟地址空间都是独立的，程序A开启了PIE，程序B关闭了PIE，它们都应该是可用运行的，内核不可能支持一种，但是考虑到内核需要根据PIE决定给不给程序分配基地址，所以内核需要找到一种方法分辨PIE是否开启。

通过file工具观察ELF文件，可以发现该工具可以直接根据ELF文件识别出PIE是否启用，那么它是如何识别的呢？

```
file观察结果：
关闭PIE：ELF 64-bit LSB executable
开启PIE：ELF 64-bit LSB pie executable
```

这个问题答案并不复杂，ELF文件会向`.dynamic`动态链接节中的`FLAGS_1`元素添加PIE标志位，内核会根据该标志位是否存在决定分不分配基地址。

```
#define	DF_1_PIE	0x08000000
0x000000006ffffffb (FLAGS_1)            Flags: PIE
```

在Linux内核中，它给程序分配的基地址是根据`TASK_SIZE`（用户态程序的虚拟地址空间最大地址）进行计算的，对于使用48位地址空间的64位内核而言，`TASK_SIZE`的大小一般是0x7ffffffff000，`ELF_ET_DYN_BASE`一般是0x555555554aaa，`load_bias`会根据程序的地址对齐情况，以及ASLR是否开启等情况，进行进一步的变化。

```
TASK_SIZE = 0x7ffffffff000

#define ELF_ET_DYN_BASE		((TASK_SIZE / 3) * 2)

load_bias = ELF_ET_DYN_BASE -> 0x555555554aaa
```

### 地址规律的总结

在Linux系统当中，用户态程序的地址问题首先会根据PIE机制的启用情况决定，未启动PIE程序为了让零地址是有问题的，所以通过`mmap_min_addr`设置虚拟地址空间的下界，保证低地址不会被使用，这个限制可以通过`sysctl`和虚文件取消。

在AMD64架构和i386架构中，LD一般使用0x400000和0x08048000作为最低地址。

对于开启PIE的程序来讲，它会根据`ELF_ET_DYN_BASE`的地址映射到虚拟地址空间中，使用48位地址空间的Linux内核中`ELF_ET_DYN_BASE`的数值一般是0x555555554aaa。

## 难以擦测的地址

在上面的分析中，我们知道了用户态程序被映射到虚拟地址空间的起始地址是有迹可循的，但在PIE关闭时也可以通过链接选项进行自定义设置，而且程序的位数和架构也会对地址产生影响。

因此在不知道足够信息的情况下，我们仍然很难知道大致的地址范围。

## 猜测思路

### 猜测缓冲区长度

此时我们利用的是缓冲区漏洞，但由于程序的二进制和源代码都是未知的，因此我们不能知道缓冲区的大小是多少，为了触发缓冲区漏洞，我们首先需要将缓冲区的长度猜测出来。

猜测缓存区的长度并不复杂，比较暴力的从1开始逐渐累加就是一种比较可靠的方式。

### 程序状态的控制

程序接收到paylaod后的状态可以分成三类，一是直接崩溃，二是运行一段时间后崩溃，三是不崩溃。

在得到缓冲区的长度之后，考虑到程序需要猜测不同的地址以及不断的接收payload，所以我们首先需要让程序重复的进入读取状态，即找到一个让程序不会崩溃的返回地址，且在该返回地址之后还会调用`read`函数。

除了进入读取状态的地址外，考虑到需要判断不同地址的类型，因此这里我们需要用到一个可以直接导致崩溃的地址。

# 示例讲解

下方给出了程序的源代码。

```
#include <stdio.h>
#include <unistd.h>
#include <string.h>

static void vuln(void)
{
    char buf[0x100];

    read(STDIN_FILENO, buf, 0x1000);
}

int main(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    puts("hello brop!");
    vuln();
    puts("bye, brop");
}
```

下面给出了ELF文件中关键的反汇编信息。

```
......
0000000000401020 <puts@plt-0x10>:
  401020:       ff 35 ca 2f 00 00       push   0x2fca(%rip)        # 403ff0 <_GLOBAL_OFFSET_TABLE_+0x8>
  401026:       ff 25 cc 2f 00 00       jmp    *0x2fcc(%rip)        # 403ff8 <_GLOBAL_OFFSET_TABLE_+0x10>
  40102c:       0f 1f 40 00             nopl   0x0(%rax)

0000000000401030 <puts@plt>:
  401030:       ff 25 ca 2f 00 00       jmp    *0x2fca(%rip)        # 404000 <puts@GLIBC_2.2.5>
  401036:       68 00 00 00 00          push   $0x0
  40103b:       e9 e0 ff ff ff          jmp    401020 <_init+0x20>
......
0000000000401060 <_start>:
  401060:       31 ed                   xor    %ebp,%ebp
  401062:       49 89 d1                mov    %rdx,%r9
  401065:       5e                      pop    %rsi
  401066:       48 89 e2                mov    %rsp,%rdx
......
00000000004011d0 <__libc_csu_init>:
  ......
  401222:       5b                      pop    %rbx
  401223:       5d                      pop    %rbp
  401224:       41 5c          ...