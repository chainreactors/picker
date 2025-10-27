---
title: Unix系列(18)--Seccomp BPF初探
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487677&idx=1&sn=4c7898115aa1f8067ccfee1ab93a38e0&chksm=fab2d382cdc55a9469320db9ecdacba324436ac3e85d3c7ccc1cae13e7678449158492cebde2&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-10-12
fetch_date: 2025-10-06T18:53:06.216361
---

# Unix系列(18)--Seccomp BPF初探

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPPibp3E2RLy4BgmJMWzeG4dLk69mPmtgzABJmvE6ZCHR6EJbunL6vAxBUvayhmKGhtSpcXYNYqfia8w/0?wx_fmt=jpeg)

# Unix系列(18)--Seccomp BPF初探

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-09-25 13:38
https://scz.617.cn/unix/202409251338.txt
```

---

```
目录:

    ☆ 背景介绍
    ☆ 测试环境
    ☆ SeccompBPF_log
    ☆ SeccompBPF_block
    ☆ scmp_sys_resolver
    ☆ libseccomp-dev
        2) SeccompBPF_log_3
        3) SeccompBPF_block_2
```

☆ 背景介绍

参看

```
Seccomp BPF (SECure COMPuting with filters)
https://www.kernel.org/doc/html/v4.19/userspace-api/seccomp_filter.html

prctl(2)

seccomp(2)
https://man7.org/linux/man-pages/man2/seccomp.2.html
```

Linux Kernel 2.6.23开始提供"Seccomp BPF"功能，可通过BPF编程对目标进程所用系统调用进行检查、过滤，包括但不限于记录目标进程发起的系统调用，阻断目标进程发起的特定系统调用，后者可增加目标进程抗Exploit的能力。

prctl(PR\_SET\_SECCOMP)兼容性更好，Kernel 3.17及以上，新增seccomp(2)系统调用。

☆ 测试环境

```
$ cat /proc/config.gz| zcat  | grep -i CONFIG_SECCOMP
```

没有config.gz时，换用下列命令

```
$ grep -i CONFIG_SECCOMP /boot/config-$(uname -r)
CONFIG_SECCOMP=y
CONFIG_SECCOMP_FILTER=y
# CONFIG_SECCOMP_CACHE_DEBUG is not set
```

若CONFIG\_SECCOMP\_FILTER未启用，则prctl不能使用SECCOMP\_MODE\_FILTER。

```
$ cat /proc/sys/kernel/seccomp/actions_avail
kill_process kill_thread trap errno user_notif trace log allow

$ cat /proc/sys/kernel/seccomp/actions_logged
kill_process kill_thread trap errno user_notif trace log
```

☆ SeccompBPF\_log

```
#include <stdio.h>
#include <stddef.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/unistd.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>

#define X32_SYSCALL_BIT 0x40000000

static int install_filter ( int arch )
{
    struct sock_filter  filter[]    =
    {
        BPF_STMT( BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, arch)) ),
        BPF_JUMP( BPF_JMP + BPF_JEQ + BPF_K, arch, 0, 2 ),

        BPF_STMT( BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, nr)) ),
        BPF_JUMP( BPF_JMP + BPF_JGE + BPF_K, X32_SYSCALL_BIT, 0, 1 ),
        BPF_STMT( BPF_RET + BPF_K, SECCOMP_RET_KILL_PROCESS ),

        BPF_STMT( BPF_RET + BPF_K, SECCOMP_RET_LOG ),
    };
    struct sock_fprog   fprog        =
    {
        .len    = ( unsigned short )( sizeof( filter ) / sizeof( filter[0] ) ),
        .filter = filter,
    };
    if ( prctl( PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0 ) )
    {
        perror( "prctl(PR_SET_NO_NEW_PRIVS)" );
        return -1;
    }
    if ( prctl( PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fprog ) )
    {
        perror( "prctl(PR_SET_SECCOMP)" );
        return -1;
    }
    return 0;
}

int main ( int argc, char * argv[] )
{
    if ( argc < 2 )
    {
        fprintf( stderr, "Usage: %s <command> [args...]\n", argv[0] );
        return -1;
    }
    if ( install_filter( AUDIT_ARCH_X86_64 ) )
    {
        fprintf( stderr, "Failed to install syscall filter\n" );
        return -1;
    }
    execvp( argv[1], &argv[1] );
    perror( "execvp" );
    return -1;
}
```

本例用SECCOMP\_RET\_LOG记录目标进程所有的系统调用，可用ausearch查看记录结果。

以scz身份执行

```
./SeccompBPF_log cat /etc/passwd
```

以root身份执行

```
$ ausearch -ui scz --format text -ts today 13:00:00 -c cat | awk '{print $7}' | sort -u
access
arch_prctl
brk
close
exit_group
fadvise64
getrandom
mmap
mprotect
munmap
newfstatat
openat
pread
prlimit64
read
rseq
set_robust_list
set_tid_address
write
```

☆ SeccompBPF\_block

```
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <errno.h>
#include <sys/prctl.h>
#include <linux/unistd.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>

#define X32_SYSCALL_BIT 0x40000000

static int install_filter ( int nr, int arch, int error )
{
    struct sock_filter  filter[]    =
    {
        BPF_STMT( BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, arch)) ),
        BPF_JUMP( BPF_JMP + BPF_JEQ + BPF_K, arch, 0, 2 ),

        BPF_STMT( BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, nr)) ),
        BPF_JUMP( BPF_JMP + BPF_JGE + BPF_K, X32_SYSCALL_BIT, 0, 1 ),
        BPF_STMT( BPF_RET + BPF_K, SECCOMP_RET_KILL_PROCESS ),

        BPF_STMT( BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, nr)) ),
        BPF_JUMP( BPF_JMP + BPF_JEQ + BPF_K, nr, 0, 1 ),
        BPF_STMT( BPF_RET + BPF_K, SECCOMP_RET_ERRNO | (error & SECCOMP_RET_DATA) ),

        BPF_STMT( BPF_RET + BPF_K, SECCOMP_RET_ALLOW ),
    };
    struct sock_fprog   fprog        =
    {
        .len    = ( unsigned short )( sizeof( filter ) / sizeof( filter[0] ) ),
        .filter = filter,
    };
    if ( prctl( PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0 ) )
    {
        perror( "prctl(PR_SET_NO_NEW_PRIVS)" );
        return -1;
    }
    if ( prctl( PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fprog ) )
    {
        perror( "prctl(PR_SET_SECCOMP)" );
        return -1;
    }
    return 0;
}

int main ( int argc, char * argv[] )
{
    if ( argc < 3 )
    {
        fprintf( stderr, "Usage: %s <syscall> <command> [args...]\n", argv[0] );
        return -1;
    }
    int nr  = (int)strtol( argv[1], NULL, 0 );
    fprintf( stdout, "syscall [%d] will be blocked\n", nr );
    if ( install_filter( nr, AUDIT_ARCH_X86_64, EPERM ) )
    {
        fprintf( stderr, "Failed to install syscall filter\n" );
        return -1;
    }
    execvp( argv[2], &argv[2] );
    perror( "execvp" );
    return -1;
}
```

本例针对目标进程阻断指定的系统调用。

```
$ ausyscall --exact close
3
```

---

```
$ ./SeccompBPF_block 3 cat /etc/passwd
syscall [3] will be blocked
cat: error while loading shared libraries: libc.so.6: cannot close file descriptor: Operation not permitted
```

☆ libseccomp-dev

```
aptitude install libseccomp-dev
```

libseccomp-dev提供了一组封装过的函数，以避免直接进行BPF编程

```
seccomp_init(3)
seccomp_rule_add(3)
seccomp_load(3)
seccomp_release(3)
```

2) SeccompBPF\_log\_3

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <seccomp.h>

static int install_filter ( void )
{
    scmp_filter_ctx ctx;
    int             rc;

    ctx = seccomp_init( SCMP_ACT_LOG );
    if ( ctx == NULL )
    {
        perror( "seccomp_init(SCMP_ACT_LOG)" );
        return -1;
    }

    rc  = seccomp_load( ctx );
    if ( rc < 0 )
    {
        perror( "seccomp_load" );
        seccomp_release( ctx );
        return -1;
    }

    seccomp_release( ctx );
    return 0;
}

int main ( int argc, char * argv[] )
{
    if ( argc < 2 )
    {
        fprintf( stderr, "Usage: %s <command> [args...]\n", argv[0] );
        return -1;
    }
    if ( install_filter() )
    {
        fprintf( stderr, "Failed to install syscall filter\n" );
        return -1;
    }
    execvp( argv[1], &argv[1] );
    perror( "execvp" );
    return -1;
}
```

以scz身份执行

```
./SeccompBPF_log_3 cat /etc/passwd
```

以root身份执行

```
ausearch -ui scz --format text -ts today 16:17:00 -c cat | awk '{print $7}' | sort -u
```

3) SeccompBPF\_block\_2

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <seccomp.h>

static int install_filter ( int nr, int error )
{
    scmp_filter_ctx ctx;
    int             rc;

    ctx = seccomp_init( SCMP_ACT_ALLOW );
    if ( ctx == NULL )
    {
        perror( "seccomp_init(SCMP_ACT_ALLOW)" );
        return -1;
    }

    rc  = seccomp_rule_add( ctx, SCMP_ACT_ERRNO(error), nr, 0 );
    if ( rc < 0 )
    {
        perror( "seccomp_rule_add(SCMP_ACT_ERRNO)" );
        seccomp_release( ctx );
        return -1;
    }

    rc  = seccomp_load( ctx );
    if ( rc < 0 )
    {
        perror( "seccomp_load" );
        seccomp_release( ctx );
        return -1;
    }

    seccomp_release( ctx );
    return 0;
}

int main ( int argc, char * argv[] )
{
    if ( argc < 3 )
    {
        fprintf( stderr, "Usage: %s <syscall> <command> [args...]\n", argv[0] );
        return -1;
    }
    int nr  = (int)strtol( argv[1], NULL, 0 );
    fprintf( stdout, "syscall [%d] will be blocked\n", nr );
    if ( install_filter( nr, EPERM ) )
    {
        fprintf( stderr, "Failed to install syscall filter\n" );
        retur...