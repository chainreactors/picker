---
title: Seccomp BPF初探
url: https://blog.nsfocus.net/seccomp-bpf/
source: 绿盟科技技术博客
date: 2024-11-02
fetch_date: 2025-10-06T19:17:06.967884
---

# Seccomp BPF初探

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Seccomp BPF初探

### Seccomp BPF初探

[2024-11-01](https://blog.nsfocus.net/seccomp-bpf/ "Seccomp BPF初探")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 3,351

## 一、背景介绍

参看

————————————————————————–
Seccomp BPF (SECure COMPuting with filters)
https://www.kernel.org/doc/html/v4.19/userspace-api/seccomp\_filter.html

prctl(2)

seccomp(2)
https://man7.org/linux/man-pages/man2/seccomp.2.html
————————————————————————–

Linux Kernel 2.6.23开始提供”Seccomp BPF”功能，可通过BPF编程对目标进程所用系统调用进行检查、过滤，包括但不限于记录目标进程发起的系统调用，阻断目标进程发起的特定系统调用，后者可增加目标进程抗Exploit的能力。

prctl(PR\_SET\_SECCOMP)兼容性更好，Kernel 3.17及以上，新增seccomp(2)系统调用。

## 二、测试环境

$ cat /proc/config.gz| zcat | grep -i CONFIG\_SECCOMP

没有config.gz时，换用下列命令

$ grep -i CONFIG\_SECCOMP /boot/config-$(uname -r)
CONFIG\_SECCOMP=y
CONFIG\_SECCOMP\_FILTER=y
# CONFIG\_SECCOMP\_CACHE\_DEBUG is not set

若CONFIG\_SECCOMP\_FILTER未启用，则prctl不能使用SECCOMP\_MODE\_FILTER。

$ cat /proc/sys/kernel/seccomp/actions\_avail
kill\_process kill\_thread trap errno user\_notif trace log allow

$ cat /proc/sys/kernel/seccomp/actions\_logged
kill\_process kill\_thread trap errno user\_notif trace log

## 三、SeccompBPF\_log

————————————————————————–
#include <stdio.h>
#include <stddef.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/unistd.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>

#define X32\_SYSCALL\_BIT 0x40000000

static int install\_filter ( int arch )
{
struct sock\_filter filter[] =
{
BPF\_STMT( BPF\_LD + BPF\_W + BPF\_ABS, (offsetof(struct seccomp\_data, arch)) ),
BPF\_JUMP( BPF\_JMP + BPF\_JEQ + BPF\_K, arch, 0, 2 ),

BPF\_STMT( BPF\_LD + BPF\_W + BPF\_ABS, (offsetof(struct seccomp\_data, nr)) ),
BPF\_JUMP( BPF\_JMP + BPF\_JGE + BPF\_K, X32\_SYSCALL\_BIT, 0, 1 ),
BPF\_STMT( BPF\_RET + BPF\_K, SECCOMP\_RET\_KILL\_PROCESS ),

BPF\_STMT( BPF\_RET + BPF\_K, SECCOMP\_RET\_LOG ),
};
struct sock\_fprog fprog =
{
.len = ( unsigned short )( sizeof( filter ) / sizeof( filter[0] ) ),
.filter = filter,
};
if ( prctl( PR\_SET\_NO\_NEW\_PRIVS, 1, 0, 0, 0 ) )
{
perror( “prctl(PR\_SET\_NO\_NEW\_PRIVS)” );
return -1;
}
if ( prctl( PR\_SET\_SECCOMP, SECCOMP\_MODE\_FILTER, &fprog ) )
{
perror( “prctl(PR\_SET\_SECCOMP)” );
return -1;
}
return 0;
}

int main ( int argc, char \* argv[] )
{
if ( argc < 2 )
{
fprintf( stderr, “Usage: %s <command> [args…]\n”, argv[0] );
return -1;
}
if ( install\_filter( AUDIT\_ARCH\_X86\_64 ) )
{
fprintf( stderr, “Failed to install syscall filter\n” );
return -1;
}
execvp( argv[1], &argv[1] );
perror( “execvp” );
return -1;
}
————————————————————————–

本例用SECCOMP\_RET\_LOG记录目标进程所有的系统调用，可用ausearch查看记录结果。

以scz身份执行

./SeccompBPF\_log cat /etc/passwd

以root身份执行

$ ausearch -ui scz –format text -ts today 13:00:00 -c cat | awk ‘{print $7}’ | sort -u
access
arch\_prctl
brk
close
exit\_group
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
set\_robust\_list
set\_tid\_address
write

## 四、SeccompBPF\_block

————————————————————————–
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <errno.h>
#include <sys/prctl.h>
#include <linux/unistd.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>

#define X32\_SYSCALL\_BIT 0x40000000

static int install\_filter ( int nr, int arch, int error )
{
struct sock\_filter filter[] =
{
BPF\_STMT( BPF\_LD + BPF\_W + BPF\_ABS, (offsetof(struct seccomp\_data, arch)) ),
BPF\_JUMP( BPF\_JMP + BPF\_JEQ + BPF\_K, arch, 0, 2 ),

BPF\_STMT( BPF\_LD + BPF\_W + BPF\_ABS, (offsetof(struct seccomp\_data, nr)) ),
BPF\_JUMP( BPF\_JMP + BPF\_JGE + BPF\_K, X32\_SYSCALL\_BIT, 0, 1 ),
BPF\_STMT( BPF\_RET + BPF\_K, SECCOMP\_RET\_KILL\_PROCESS ),

BPF\_STMT( BPF\_LD + BPF\_W + BPF\_ABS, (offsetof(struct seccomp\_data, nr)) ),
BPF\_JUMP( BPF\_JMP + BPF\_JEQ + BPF\_K, nr, 0, 1 ),
BPF\_STMT( BPF\_RET + BPF\_K, SECCOMP\_RET\_ERRNO | (error & SECCOMP\_RET\_DATA) ),

BPF\_STMT( BPF\_RET + BPF\_K, SECCOMP\_RET\_ALLOW ),
};
struct sock\_fprog fprog =
{
.len = ( unsigned short )( sizeof( filter ) / sizeof( filter[0] ) ),
.filter = filter,
};
if ( prctl( PR\_SET\_NO\_NEW\_PRIVS, 1, 0, 0, 0 ) )
{
perror( “prctl(PR\_SET\_NO\_NEW\_PRIVS)” );
return -1;
}
if ( prctl( PR\_SET\_SECCOMP, SECCOMP\_MODE\_FILTER, &fprog ) )
{
perror( “prctl(PR\_SET\_SECCOMP)” );
return -1;
}
return 0;
}

int main ( int argc, char \* argv[] )
{
if ( argc < 3 )
{
fprintf( stderr, “Usage: %s <syscall> <command> [args…]\n”, argv[0] );
return -1;
}
int nr = (int)strtol( argv[1], NULL, 0 );
fprintf( stdout, “syscall [%d] will be blocked\n”, nr );
if ( install\_filter( nr, AUDIT\_ARCH\_X86\_64, EPERM ) )
{
fprintf( stderr, “Failed to install syscall filter\n” );
return -1;
}
execvp( argv[2], &argv[2] );
perror( “execvp” );
return -1;
}
————————————————————————–

本例针对目标进程阻断指定的系统调用。

$ ausyscall –exact close
3

$ ./SeccompBPF\_block 3 cat /etc/passwd
syscall [3] will be blocked
cat: error while loading shared libraries: libc.so.6: cannot close file descriptor: Operation not permitted

## 五、 libseccomp-dev

aptitude install libseccomp-dev

libseccomp-dev提供了一组封装过的函数，以避免直接进行BPF编程

seccomp\_init(3)
seccomp\_rule\_add(3)
seccomp\_load(3)
seccomp\_release(3)

2) SeccompBPF\_log\_3

————————————————————————–
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <seccomp.h>

static int install\_filter ( void )
{
scmp\_filter\_ctx ctx;
int rc;

ctx = seccomp\_init( SCMP\_ACT\_LOG );
if ( ctx == NULL )
{
perror( “seccomp\_init(SCMP\_ACT\_LOG)” );
return -1;
}

rc = seccomp\_load( ctx );
if ( rc < 0 )
{
perror( “seccomp\_load” );
seccomp\_release( ctx );
return -1;
}

seccomp\_release( ctx );
return 0;
}

int main ( int argc, char \* argv[] )
{
if ( argc < 2 )
{
fprintf( stderr, “Usage: %s <command> [args…]\n”, argv[0] );
return -1;
}
if ( install\_filter() )
{
fprintf( stderr, “Failed to install syscall filter\n” );
return -1;
}
execvp( argv[1], &argv[1] );
perror( “execvp” );
return -1;
}
————————————————————————–

以scz身份执行

./SeccompBPF\_log\_3 cat /etc/passwd

以root身份执行

ausearch -ui scz –format text -ts today 16:17:00 -c cat | awk ‘{print $7}’ | sort -u

3) SeccompBPF\_block\_2

————————————————————————–
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <seccomp.h>

static int install\_filter ( int nr, int error )
{
scmp\_filter\_ctx ctx;
int rc;

ctx = seccomp\_init( SCMP\_ACT\_ALLOW );
if ( ctx == NULL )
{
perror( “seccomp\_init(SCMP\_ACT\_ALLOW)” );
return -1;
}

rc = seccomp\_rule\_add( ctx, SCMP\_ACT\_ERRNO(error), nr, 0 );
if ( rc < 0 )
{
perror( “seccomp\_rule\_add(SCMP\_ACT\_ERRNO)” );
seccomp\_release( ctx );
return -1;
}

rc = seccomp\_load( ctx );
if ( rc < 0 )
{
perror( “seccomp\_load” );
seccomp\_release( ctx );
return -1;
}

seccomp\_release( ctx );
return 0;
}...