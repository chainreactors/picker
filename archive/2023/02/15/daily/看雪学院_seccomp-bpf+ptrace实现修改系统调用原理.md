---
title: seccomp-bpf+ptrace实现修改系统调用原理
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458494656&idx=1&sn=432a18ba6908b78c9198d1c8f90fed62&chksm=b18e964a86f91f5cb8c81e10f1926461a2819c26ac08d9ad02bd9ee25c5f9acf55e0acde7d7b&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-02-15
fetch_date: 2025-10-04T06:37:54.980581
---

# seccomp-bpf+ptrace实现修改系统调用原理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H4yqSxOmHFDodVVkgicYkhSiaqaXXnkc5tZZxrwwiaM8PqWjkbWEVW2PNmGiaQHbMNWslXI2X9Gicn3rQ/0?wx_fmt=jpeg)

# seccomp-bpf+ptrace实现修改系统调用原理

王麻子本人

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H4yqSxOmHFDodVVkgicYkhSREibHXRxlAia2GHFXq3AVQz45QGoOKIVtz87rgVjLaKdDHWiaZCaYGL4g/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：王麻子本人

目前绝大部分app都会频繁的使用syscall去获取设备指纹和做一些反调试，使用常规方式过反调试已经非常困难了，使用内存搜索svc指令已经不能满足需求了，开始学习了一下通过ptrace/ptrace配合seccomp来解决svc反调试难定位难绕过等问题。

#

# **seccomp**

Linux 2.6.12中的导入了第一个版本的seccomp，通过向/proc/PID/seccomp接口中写入“1”来启动通过滤器只支持几个函数。

```
read()，write()，_exit()，sigreturn()
```

使用其他系统调用就会收到信号(SIGKILL)退出。测试代码如下：

```
#include <fcntl.h>#include <stdio.h>#include <unistd.h>#include <sys/prctl.h>#include <linux/seccomp.h> void configure_seccomp() {    printf("Configuring seccomp\n");    prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);}int main(int argc, char* argv[]) {    int infd, outfd;    if (argc < 3) {        printf("Usage:\n\t%s <input path> <output_path>\n", argv[0]);        return -1;    }    printf("Starting test seccomp Y/N?");    char c = getchar();    if (c == 'y' || c == 'Y') configure_seccomp();    printf("Opening '%s' for reading\n", argv[1]);    if ((infd = open(argv[1], O_RDONLY)) > 0) {        ssize_t read_bytes;        char buffer[1024];        printf("Opening '%s' for writing\n", argv[2]);        if ((outfd = open(argv[2], O_WRONLY | O_CREAT, 0644)) > 0) {            while ((read_bytes = read(infd, &buffer, 1024)) > 0)                write(outfd, &buffer, (ssize_t)read_bytes);        }        close(infd);        close(outfd);    }    printf("End!\n");     return 0;}
```

可以看到执行到22行就结束了没执行到 Eed.
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H4yqSxOmHFDodVVkgicYkhSJnAMPbDmF5aL0WWqqHevfcFonEnicQ3Oe1sQnDkWmckJdib4yHIHH0iaw/640?wx_fmt=png)

#

# **seccomp-bpf**

Seccomp-BPF（Berkeley Packet Filter）是Linux内核中的一种安全机制，用于限制进程对系统调用的访问权限。它主要用于防止恶意软件对系统的攻击，提高系统的安全性。

Seccomp-BPF使用BPF（Berkeley Packet Filter）技术来实现系统调用过滤，可以使用BPF程序指定哪些系统调用可以被进程访问，哪些不能。BPF程序由一组BPF指令组成，可以在系统调用执行之前对其进行检查，以决定是否允许执行该系统调用。

Seccomp-BPF提供了两种模式：白名单模式和黑名单模式。白名单模式允许所有系统调用，除非明确指定不允许的系统调用。黑名单模式禁止所有系统调用，除非明确指定允许的系统调用。这两种模式的选择取决于您的实际需求。

Seccomp-BPF提供了一个钩子函数，在系统调用执行之前会进入到这个函数，对系统调用进行检查，如果BPF程序允许执行该系统调用，则进程可以继续执行，否则会抛出一个异常。

##

## **1.BPF确定了一个可以在内核内部实现的虚拟机，该虚拟机具有以下特性：**

```
简单指令集    小型指令集    所有的命令大小相一致    实现过程简单、快速只有分支向前指令    程序是有向无环图(DAGs)，没有循环易于验证程序的有效性/安全性    简单的指令集⇒可以验证操作码和参数    可以检测死代码    程序必须以 Return 结束    BPF过滤器程序仅限于4096条指令
```

##

## **2.Seccomp-BPF 使用的也只是BPF的子集功能：**

```
Conditional JMP(条件判断跳转)    当匹配条件为真，跳转到true指定位置    当 匹配条件为假，跳转到false指定位置    跳转偏移量最大255JMP(直接跳转)    跳转目标是指令偏移量    跳转 偏移量最大255Load(数据读取)    读取程序参数    读取指定的16位内存地址Store(数据存储)    保存数据到指定的16位内存地址中支持的运算    + - * / & | ^ >> << !返回值    SECCOMP_RET_ALLOW -  允许继续使用系统调用    SECCOMP_RET_KILL - 终止系统调用    SECCOMP_RET_ERRNO -  返回设置的errno值    SECCOMP_RET_TRACE -  通知附加的ptrace（如果存在）    SECCOMP_RET_TRAP - 往进程发送 SIGSYS信号最多只能有4096条命令不能出现循环
```

Seccomp-BPF程序 接收以下结构作为输入参数：

```
/** * struct seccomp_data - the format the BPF program executes over. * @nr: the system call number * @arch: indicates system call convention as an AUDIT_ARCH_* value *        as defined in <linux/audit.h>. * @instruction_pointer: at the time of the system call. * @args: up to 6 system call arguments always stored as 64-bit values *        regardless of the architecture. */struct seccomp_data {    int nr;    __u32 arch;    __u64 instruction_pointer;    __u64 args[6];};
```

**使用示例：**

在这种情况下，seccomp-BPF 程序将允许使用 O\_RDONLY 参数打开第一个调用 , 但是在使用 O\_WRONLY | O\_CREAT 参数调用 open 时终止程序。

```
#include <stdio.h>#include <fcntl.h>#include <unistd.h>#include <stddef.h>#include <sys/prctl.h>#include <linux/seccomp.h>#include <linux/filter.h>#include <linux/unistd.h> void configure_seccomp() {  struct sock_filter filter [] = {    BPF_STMT(BPF_LD | BPF_W | BPF_ABS, (offsetof(struct seccomp_data, nr))),    BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_write, 0, 1),    BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW),    BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_open, 0, 3),    BPF_STMT(BPF_LD | BPF_W | BPF_ABS, (offsetof(struct seccomp_data, args[1]))),    BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, O_RDONLY, 0, 1),    BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW),    BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL)  };  struct sock_fprog prog = {       .len = (unsigned short)(sizeof(filter) / sizeof (filter[0])),       .filter = filter,  };   printf("Configuring seccomp\n");  prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);  prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog);} int main(int argc, char* argv[]) {  int infd, outfd;  ssize_t read_bytes;  char buffer[1024];   if (argc < 3) {    printf("Usage:\n\tdup_file <input path> <output_path>\n");    return -1;  }  printf("Ducplicating file '%s' to '%s'\n", argv[1], argv[2]);   configure_seccomp(); //配置seccomp   printf("Opening '%s' for reading\n", argv[1]);  if ((infd = open(argv[1], O_RDONLY)) > 0) {    printf("Opening '%s' for writing\n", argv[2]);    if ((outfd = open(argv[2], O_WRONLY | O_CREAT, 0644)) > 0) {        while((read_bytes = read(infd, &buffer, 1024)) > 0)          write(outfd, &buffer, (ssize_t)read_bytes);    }  }  close(infd);  close(outfd);  return 0;}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H4yqSxOmHFDodVVkgicYkhSFW2kaBCSnrQw6holUpGzrtdIyfAICGkjTNFCSUPDia6sVG4eiccN9thQ/640?wx_fmt=png)

#

# **使用ptrace修改系统调用**

将getpid()的实现改为mkdir()的实现。主要是通过ptrace函数来跟踪子进程，获取其寄存器中的信息，然后根据需求替换对应的系统调用。

```
#include <stdio.h>#include <stdlib.h>#include <errno.h>#include <unistd.h>#include <ctype.h>#include <sys/types.h>#include <sys/stat.h>#include <sys/user.h>#include <sys/signal.h>#include <sys/wait.h>#include <sys/ptrace.h>#include <sys/fcntl.h>#include <syscall.h>  void die (const char *msg){  perror(msg);  exit(errno);} void attack(){  int rc;  syscall(SYS_getpid, SYS_mkdir, "dir", 0777);} int main(){  int pid;  struct user_regs_struct regs;  switch( (pid = fork()) ) {    case -1:  die("Failed fork");    case 0:               ptrace(PTRACE_TRACEME, 0, NULL, NULL);              kill(getpid(), SIGSTOP);              attack();              return 0;  }   waitpid(pid, 0, 0);   while(1) {    int st;     ptrace(PTRACE_SYSCALL, pid, NULL, NULL);    if (waitpid(pid, &st, __WALL) == -1) {      break;    }     if (!(WIFSTOPPED(st) && WSTOPSIG(st) == SIGTRAP)) {      break;    }     ptrace(PTRACE_GETREGS, pid, NULL, &regs);    printf("orig_rax = %lld\n", regs.orig_rax);      if (regs.rax != -ENOSYS) {      continue;    }      if (regs.orig_rax == SYS_getpid) {      regs.orig_rax = regs.rdi;      regs.rdi = regs.rsi;      regs.rsi = regs.rdx;      regs.rdx = regs.r10;      regs.r10 = regs.r8;      regs.r8 = regs.r9;      regs.r9 = 0;      ptrace(PTRACE_SETREGS, pid, NULL, &regs);    }  }  return 0;}
```

**使用seccomp-bpf+ptrace加ptrace修改系统调用**

看一下main函数这里设置了跟踪openat系统调用子进程请求父进程附加 父进程开启ptrace+seccomp。

##

## **1.main**

```
int main(){    pid_t pid;    int status;    if ((pid = fork()) == 0) {        /* 目前是跟踪open系统调用 */        struct sock_filter filter[] = {            BPF_STMT(BPF_LD+BPF_W+BPF_ABS, offsetof(struct seccomp_data, nr)),            BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, __NR_openat, 0, 1),            BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_TRACE),            BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_ALLOW),        };        struct sock_fprog prog = {            .filter = filter,            .len = (unsigned short) (sizeof(filter)/sizeof(filter[0])),        };        //告诉父进程允许子进程跟踪        ptrace(PTRACE_TRACEME, 0, 0, 0);        /* 避免需要 CAP_SYS_ADMIN */        if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) == -1) {            perror("prctl(PR_SET_NO_NEW_PRIVS)");            return 1;        }        if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) == -1) {            perror("when setting seccomp filter");            return 1;        }        kill(getpid(), SIGSTOP);        ssize_t count;        char buf[256];        int fd;        fd = syscall(__NR_openat,fd,"/data/local/tmp/tuzi.txt", O_RDONLY...