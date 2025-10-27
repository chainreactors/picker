---
title: xv6-sh 超小os内核shell实现详解
url: https://buaq.net/go-138697.html
source: unSafe.sh - 不安全
date: 2022-12-06
fetch_date: 2025-10-04T00:32:37.228771
---

# xv6-sh 超小os内核shell实现详解

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/1beea0c60dc5d4e470167fd40af8b749.jpg)

xv6-sh 超小os内核shell实现详解

前言关于xv6抄了一下百度百科Xv6是由麻省理工学院(MIT)为操作系统工程的课程（代号6.828）,开发的一个教学目的的操作系统。Xv6是在x86处理器上(
*2022-12-5 23:1:6
Author: [yyz9.cn(查看原文)](/jump-138697.htm)
阅读量:26
收藏*

---

## 前言

### 关于xv6

抄了一下百度百科

> Xv6是由[麻省理工学院](https://baike.baidu.com/item/%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2?fromModule=lemma_inlink)(MIT)为操作系统工程的课程（代号6.828）,开发的一个教学目的的操作系统。
>
> Xv6是在x86处理器上(x即指x86)用[ANSI标准](https://baike.baidu.com/item/ANSI%E6%A0%87%E5%87%86/3127116?fromModule=lemma_inlink)C重新实现的Unix第六版(Unix V6，通常直接被称为V6)。Unix V6是1975年发布的，基于DEC PDP-11小型机，当时还没有x86系列CPU，而现在PDP的机器已经很少见了，当时使用是在标准ANSI C发布之前的旧式C语言。
>
> 与Linux或BSD系统不同，Xv6很简单，可以在一个学期讲完，全部代码只有8千行多，但仍包括了Unix的重要概念和组织结构。由于是基于较早的Unix V6，Xv6的结构与现代操作系统，如Linux，Windows的差距较大。
>
> 在MIT以外，很多其它大学也在操作系统课程中使用了Xv6或其变种，如耶鲁，清华等。
>
> 另外一个类似的教学用类Unix系统是著名的Minix。

### 关于xv6-sh魔改版

这是南京大学操作系统的[yjj](https://jyywiki.cn/)老师从xv6本身的sh实现中魔改的一个版本

它拥有如下优点：

* 能够实现基本的shell的大部分操作，包括：
  + 命令执行
  + 管道符
  + ()括号表达式
  + <>输出输入重定向
  + ；分号分隔命令
  + & 后台运行
* 库函数0依赖，不需要依赖libc，甚至不需要main函数
* 通过`_start`函数作为程序入口，通过`-ffreestanding`来编译，可以直接作为操作系统的`init`程序
* 可以学到一些c语言编写技巧

当然，他也有很多局限性，远远达不到现代可使用的优秀的shell的功能，比如没有环境变量。

## 分析

先给出源码，这里删掉了许多注释，在文章的最后我会给出带注释版本的源码

需要注意的是，程序的编译需要使用`-ffreestanding`参数

> gcc -ffreestanding -static -O2 -g -c sh-xv6.c && ld sh-xv6.o && ./a.out

```
 #include <fcntl.h>
 #include <stdarg.h>
 #include <stddef.h>
 #include <sys/syscall.h>
 enum { EXEC = 1, REDIR, PIPE, LIST, BACK };
 ​
 #define MAXARGS 10
 #define NULL ((void *)0)
 ​
 struct cmd {
   int type;
 };
 ​
 struct execcmd {
   int type;
   char *argv[MAXARGS], *eargv[MAXARGS];
 };
 ​
 struct redircmd {
   int type, fd, mode;
   char *file, *efile;
   struct cmd* cmd;
 };
 ​
 struct pipecmd {
   int type;
   struct cmd *left, *right;
 };
 ​
 struct listcmd {
   int type;
   struct cmd *left, *right;
 };
 ​
 struct backcmd {
   int type;
   struct cmd* cmd;
 };
 ​
 struct cmd* parsecmd(char*);
 ​
 long syscall(int num, ...) {
   va_list ap;
   va_start(ap, num);
   register long a0 asm ("rax") = num;
   register long a1 asm ("rdi") = va_arg(ap, long);
   register long a2 asm ("rsi") = va_arg(ap, long);
   register long a3 asm ("rdx") = va_arg(ap, long);
   register long a4 asm ("r10") = va_arg(ap, long);
   va_end(ap);
   asm volatile("syscall"
     : "+r"(a0) : "r"(a1), "r"(a2), "r"(a3), "r"(a4)
     : "memory", "rcx", "r8", "r9", "r11");
   return a0;
 }
 ​
 size_t strlen(const char *s) {
   size_t len = 0;
   for (; *s; s++) len++;
   return len;
 }
 ​
 char *strchr(const char *s, int c) {
   for (; *s; s++) {
     if (*s == c) return (char *)s;
   }
   return NULL;
 }
 ​
 void print(const char *s, ...) {
   va_list ap;
   va_start(ap, s);
   while (s) {
     syscall(SYS_write, 2, s, strlen(s));
     s = va_arg(ap, const char *);
   }
   va_end(ap);
 }
 ​
 ​
 #define assert(cond) \
   do { if (!(cond)) { \
     print("Assertion failed.\n", NULL); \
     syscall(SYS_exit, 1); } \
   } while (0)
 ​
 static char mem[4096], *freem = mem;
 void *zalloc(size_t sz) {
   assert(freem + sz < mem + sizeof(mem));
   void *ret = freem;
   freem += sz;
   return ret;
 }
 ​
 // Execute cmd.  Never returns.
 void runcmd(struct cmd* cmd) {
   int p[2];
   struct backcmd* bcmd;
   struct execcmd* ecmd;
   struct listcmd* lcmd;
   struct pipecmd* pcmd;
   struct redircmd* rcmd;
 ​
   if (cmd == 0) syscall(SYS_exit, 1);
 ​
   switch (cmd->type) {
     case EXEC:
       ecmd = (struct execcmd*)cmd;
       if (ecmd->argv[0] == 0) syscall(SYS_exit, 1);
       syscall(SYS_execve, ecmd->argv[0], ecmd->argv, NULL);
       print("Failed to exec ", ecmd->argv[0], "\n", NULL);
       break;
 ​
     case REDIR:
       rcmd = (struct redircmd*)cmd;
       syscall(SYS_close, rcmd->fd);
       if (syscall(SYS_open, rcmd->file, rcmd->mode, 0644) < 0) {
         print("Failed to open ", rcmd->file, "\n", NULL);
         syscall(SYS_exit, 1);
       }
       runcmd(rcmd->cmd);
       break;
 ​
     case LIST:
       lcmd = (struct listcmd*)cmd;
       if (syscall(SYS_fork) == 0) runcmd(lcmd->left);
       syscall(SYS_wait4, -1, 0, 0, 0);
       runcmd(lcmd->right);
       break;
 ​
     case PIPE:
       pcmd = (struct pipecmd*)cmd;
       assert(syscall(SYS_pipe, p) >= 0);
       if (syscall(SYS_fork) == 0) {
         syscall(SYS_close, 1);
         syscall(SYS_dup, p[1]);
         syscall(SYS_close, p[0]);
         syscall(SYS_close, p[1]);
         runcmd(pcmd->left);
       }
       if (syscall(SYS_fork) == 0) {
         syscall(SYS_close, 0);
         syscall(SYS_dup, p[0]);
         syscall(SYS_close, p[0]);
         syscall(SYS_close, p[1]);
         runcmd(pcmd->right);
       }
       syscall(SYS_close, p[0]);
       syscall(SYS_close, p[1]);
       syscall(SYS_wait4, -1, 0, 0, 0);
       syscall(SYS_wait4, -1, 0, 0, 0);
       break;
 ​
     case BACK:
       bcmd = (struct backcmd*)cmd;
       if (syscall(SYS_fork) == 0) runcmd(bcmd->cmd);
       break;
 ​
     default:
       assert(0);
   }
   syscall(SYS_exit, 0);
 }
 ​
 int getcmd(char* buf, int nbuf) {
   print("@ ", NULL);
   for (int i = 0; i < nbuf; i++) buf[i] = '\0';
 ​
   while (nbuf-- > 1) {
     int nread = syscall(SYS_read, 0, buf, 1);
     if (nread <= 0) return -1;
     if (*(buf++) == '\n') break;
   }
   return 0;
 }
 ​
 void _start() {
   static char buf[100];
 ​
   // Read and run input commands.
   while (getcmd(buf, sizeof(buf)) >= 0) {
     if (buf[0] == 'c' && buf[1] == 'd' && buf[2] == ' ') {
       // Chdir must be called by the parent, not the child.
       buf[strlen(buf) - 1] = 0;  // chop \n
       if (syscall(SYS_chdir, buf + 3) < 0) print("Can not cd to ", buf + 3, "\n", NULL);
       continue;
     }
     if (syscall(SYS_fork) == 0) runcmd(parsecmd(buf));
     syscall(SYS_wait4, -1, 0, 0, 0);
   }
   syscall(SYS_exit, 0);
 }
 ​
 // Constructors
 ​
 struct cmd* execcmd(void) {
   struct execcmd* cmd;
   cmd = zalloc(sizeof(*cmd));
   cmd->type = EXEC;
   return (struct cmd*)cmd;
 }
 ​
 struct cmd* redircmd(struct cmd* subcmd, char* file, char* efile, int mode,
                      int fd) {
   struct redircmd* cmd;
 ​
   cmd = zalloc(sizeof(*cmd));
   cmd->type = REDIR;
   cmd->cmd = subcmd;
   cmd->file = file;
   cmd->efile = efile;
   cmd->mode = mode;
   cmd->fd = fd;
   return (struct cmd*)cmd;
 }
 ​
 struct cmd* pipecmd(struct cmd* left, struct cmd* right) {
   struct pipecmd* cmd;
 ​
   cmd = zalloc(sizeof(*cmd));
   cmd->type = PIPE;
   cmd->left = left;
   cmd->right = right;
   return (struct cmd*)cmd;
 }
 ​
 struct cmd* listcmd(struct cmd* left, struct cmd* right) {
   struct listcmd* cmd;
 ​
   cmd = zalloc(sizeof(*cmd));
   cmd->type = LIST;
   cmd->left = left;
   cmd->right = right;
   return (struct cmd*)cmd;
 }
 ​
 struct cmd* backcmd(struct cmd* subcmd) {
   struct backcmd* cmd;
 ​
   cmd = zalloc(sizeof(*cmd));
   cmd->type = BACK;
   cmd->cmd = subcmd;
   return (struct cmd*)cmd;
 }
 ​
 // Parsing
 ​
 char whitespace[] = " \t\r\n\v";
 char symbols[] = "<|>&;()";
 ​
 int gettoken(char** ps, char* es, char** q, char** eq) {
   char* s;
   int ret;
 ​
   s = *ps;
   while (s < es && strchr(whitespace, *s)) s++;
   if (q) *q = s;
   ret = *s;
   switch (*s) {
     case 0:
       break;
     case '|': case '(': case ')': case ';': case '&': case '<':
       s++;
       break;
     case '>':
       s++;
       if (*s == '>') {
         ret = '+'; s++;
       }
       break;
     default:
       ret = 'a';
       while (s < es && !strchr(whitespace, *s) && !strchr(symbols, *s)) s++;
       break;
   }
   if (eq) *eq = s;
 ​
   while (s < es && strchr(whitespace, *s)) ...