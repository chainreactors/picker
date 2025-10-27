---
title: Linux进程注入
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488156&idx=1&sn=54483b86bec29cecaa82c668a1dd0963&chksm=fdf97989ca8ef09fcd9cae0f3ab1578868f0b8f1d1333e3a49fac6791f3d679ff63f00c9b534&scene=58&subscene=0#rd
source: debugeeker
date: 2023-02-03
fetch_date: 2025-10-04T05:35:27.951859
---

# Linux进程注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbysxfWWu1PuWt3mPzndpeOzqX6GXZeLknadvjia37Qcmb3SND1ZAicWrg5PdrhBJhlSFpmUNZHgeo3g/0?wx_fmt=jpeg)

# Linux进程注入

原创

debugeeker

奶牛安全

> 本文展示进程注入的技术，可惜只是上一部分代码。作者也没有再写。
>
> 译自https://www.tarlogic.com/blog/linux-process-infection-part-i/

红蓝对抗中，在蓝队各种不同任务中，有一样任务是精巧而不同凡响的：放一个APT进到电脑系统并保证它的持续性。不幸的是，大多数持续性机制基于在不同路径下保持恶意文件的拷贝，携带一种或多种触发技术（`shell`脚本，命令别名，链接，系统启动脚本）。因此一个练队安全专家只需要找出一个文件在运行中的拷贝，然后在他的电脑上分析。

虽然安全专家迟早会发现一些事情，但确实有一些技术可以实现，使得在感染的机器上检测APT非常困难。在本文，会详细讲述一个基于进程树的持续性机制，而不通过基于文件系统存储的机制。

## 前提

这个技术是在x86-64 GNU/Linux下使用，虽然这个理论可以轻易扩充到任意带有或多或少调试API的操作系统。前提非常简单：任何一个现代GCC版本。

## 把其它进程的地址空间作为数据仓库

这种技术背后的直觉是将正在运行的非特权进程的地址空间用作存储区域，方法是将两个线程注入其中：第一个线程将尝试感染其余进程，而另一个线程将包含恶意负载(在本例中，这将仅确保文件系统持久性)。如果删除该文件，则将使用不同的名称恢复该文件。

要紧记，这个技术非常受限于机器的运行时间，所以应该使用在那些不经常重启的系统。在其他系统中，它可以被视为一种补充的持久性机制。

## 注入方案分析

很明显，这个技术一个最关键的步骤就是代码注入。由于不可能事先知道代码在受害者地址空间的位置，这个代码应该是位置无关代码。那么，动态链接库就是自然而然的选择。但它有下面的不足：

* 大多数被注入的内容只是元数据（ELF头部和段信息之类）
* 解析和加载库所需的代码虽然不太复杂，但与有效负载的大小相比不可忽略
* 共享库使用众所周知的文件格式，使得它非常容易被分析

理想情况下，注入应该尽可能小：几个代码页，可能一个额外的页存放着。所有这些都可以通过链接器脚本实现。然而，对于这个POC，我们将满足于将共享库作为“第一个容器”。

另一个限制是目标进程并不需要是动态执行文件（C库可能不是动态加载的）。因此，在加载的共享库进行手工符号解析非常痛苦，依赖于ABI，基本无法维护。这意味着，许多标准C函数要重新手工实现。

同时，这个注入是基于`ptrace`系统调用。如果进程没有足够权限，这个技术是失效的。

最后，动态内存使用的限制也会出现。动态内存使用涉及到堆，堆的内部结构远远没有标准化。通常，在程序的地址空间中保留较大的内存占用量是不可取的。应尽量少使用动态内存，以尽可能减少内存占用。

## 路线图

这个POC会做下列事情：

* 库会有两个入口。它们的位置会事先知道（它们有相对执行文件基址的固定偏移量）并会关联到被感染线程的主函数开始。
* 感染线程会遍历系统所有运行进程，找到可被攻击的潜在进程
* `ptrace(PTRACE_SEIZE)`会尝试附加到每个进程，并读取它们的内存看是否已经被感染了
* 系统调用必须被注入。这些系统调用必须分配必要的内存页来存储注入的代码。
* 启动这两个进程，继续被调试进程的执行。

每一个步骤都需要精心的准备。下面会详细介绍。

## 准备环境

为了保证代码尽量干净，一个编译成共享库的C程序会作为起点。另外，为了在程序完成前进行接口测试，需要提供一个C编写的小程序来调用库中指定的函数。为了减低整体开发工作量，也需要提供一个包含所有构建规则的makefile。

可注入库的入口基本模板如下：

```
void persist(void)
{
  /* Implement me */
}

void propagate(void)
{
  /* Implement me */
}
```

测试可注入的库的小程序`spawn.c`

```
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

int main(int argc, char *argv[])
{
  void *handle;
  void (*entry)(void);

  if (argc != 3)
  {
    fprintf(stderr, "Usage\n%s file symbol\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  if ((handle = dlopen(argv[1], RTLD_NOW)) == NULL)
  {
    fprintf(stderr, "%s: failed to load %s: %s\n", argv[0], argv[1], dlerror());
    exit(EXIT_FAILURE);
  }

  if ((entry = dlsym(handle, argv[2])) == NULL)
  {
    fprintf(stderr, "%s: symbol `%s' not found in %s\n", argv[0], argv[2], argv[1]);
    exit(EXIT_FAILURE);
  }

  printf("Symbol `%s' found in %p. Jumping to function...\n", argv[2], entry);

  (entry) ();

  printf("Function returned!\n");

  dlclose(handle);
  return 0;
}
```

`Makefile`

```
CC=gcc
INF_CFLAGS=--shared -fPIE -fPIC -nostdlib

all : injectable.so spawn

injectable.so : injectable.c
        $(CC) $(INF_CFLAGS) injectable.c -o injectable.so

spawn : spawn.c
        $(CC) spawn.c -o spawn -ldl
```

看看结果

```
$ make
(…)
$ ./spawn ./injectable.so propagate
Symbol `propagate' found in 0x7ffff76352ea. Jumping to function...
Function returned!
```

## 系统调用

上面`Makefile`关于`injectable.so`的一个显著点是使用`-nostdlib`编译选项，这意味着无法使用上层的`C`接口。要克服这个限制，只能通过C和内联汇编的混合编程来和操作系统打交道。

一般，`x86-64 Linux`系统调用都是通过`syscall`指令（旧标准是通过中断号`0x80`）。反正，基本思路都是一样的：往寄存器里塞系统调用的参数，然后通过一些特殊指令调用系统。`rax`存放着系统调用号，系统调用的参数依次放在`rdi`,`rsi`,`rdx`,`r10`,`r8`,`r9`，返回值放在`rax`，负数表示错误（是`errno`的相反数）。一个简单的`hello world`程序使用`write`系统调用在汇编的表示可能如下

```
    movq $1, %rax             // Syscall code for write(): 1
    movq $1, %rdi             // Arg 1: File descriptor (stdout)
    leaq %rip(greeting), %rsi // Arg 2: Buffer address
    movq $12, %rdx            // Arg 3: size (12 bytes)
    syscall                   // All set, call the kernel
[…]
greeting: .ascii "Hello world\n"
```

由于`GCC`的内联汇编语法，在C里使用内联汇编也非常简单。一个`write`封装可以变成这样

```
#include <unistd.h>
#include <syscall.h>

ssize_t write(int fd, const void *buffer, size_t size)
{
  size_t result;
  asm volatile("syscall" : "=a" (result) : "a" (__NR_write), "D" (fd), "S" (buffer), "d" (size);
  return result;
}
```

那些在`syscall`后面传递的值指定了在执行汇编代码前寄存器如何初始化。在这里，`rax`用`__NR_write`初始化（`write`的宏定义，在`/usr/include/x86_64-linux-gnu/asm/unistd_64.h`定义），`rdi`（说明符“D"） 存放`fd`，`rsi`(说明符“S"）用`buffer`, `rdx`（说明符”d"）用`size`，返回值放在`rax`

字符串处理是普遍操作，所以需要写`strlen`（根据`string.h`的原型）来计算字符串长度：

```
size_t strlen(const char *buffer)
{
  size_t len = 0;

  while (*buffer++)
    ++len;

  return len;
}
```

再定义下面的宏

```
#define puts(string) write(1, string, strlen(string))
```

来屏幕上显示调试信息（使用1表明是标准输出）

```
void persist(void)
{
  puts("This is persist()\n");
}

void propagate(void)
{
  puts("This is propagate()\n");
}
```

运行结果如下

```
% ./spawn ./injectable.so persist
Symbol `persist' found in 0x7f3eb58403be. Jumping to function...
This is persist()
Function returned!
% ./spawn ./injectable.so propagate
Symbol `propagate' found in 0x7fb8874403db. Jumping to function...
This is propagate()
Function returned!
```

第一个困难有了解决方法：

1. 对于需要用到的系统调用，用混合编程的方式封装
2. 对于所需的库函数按需要用标准头文件原型实现

## 列举进程

为了把恶意代码注入到其它进程，第一步是列举系统可用的进程。有两种方法可以实现：

1. 遍历`/proc`文件系统
2. 使用`kill`探测系统所有进程ID，从2到`PID_MAX`

第一种方法最快实现，但它却是最复杂。因为：

1. `/proc`可能没有加载
2. 不使用`libc`的函数，需要基于`open/getdents`系统调用实现`opendir/readdir`函数
3. `/proc`下的文件名需要转换成整型，需要实现字符串到整型的函数

第二种方法，表面上看很复杂，实际上在现在操作系统都可用。这种方法是对这些进程ID发送信号0,如果返回为0,就说明进程存在，否则就不存在。

> 译者注：不少发现隐藏进程的方法是使用`kill`这种方式来发现，把返回的结果和`/proc`或（`ps`，有些机器是没有加载`/proc`）的结果对比，多出来的就是隐藏进程。

唯一的麻烦是`PID_MAX`的取值，它在每个系统的值都不一样。不过，在大多数情况下，它的值都是默认值（32768）。由于并没有信号发出,`kill`实际上很快，33000来次完全没问题。

为了使用这个技术，封装`kill`是很有必要。

```
int kill(pid_t pid, int sig)
{
  int result;
  asm volatile("syscall" : "=a" (result) : "a" (__NR_kill), "D" (pid), "S" (sig));
  return result;
}
```

由于没有`printf`之类的函数，`write`只能把字符串打印在屏幕上，所以需要写一个函数把数字打印在屏幕上

```
void puti(unsigned int num)
{
  unsigned int max = 1000000000;
  char c;
  unsigned int msd_found = 0;

  while (max > 0)
  {
    c = '0' + num / max;
    msd_found |= c != '0' || max == 1;

    if (msd_found)
      write(1, &c, 1);

    num %= max;
    max /= 10;
  }
}
```

现在把`propagate`函数修改，让它可以枚举进程

```
void propagate(void)
{
  pid_t pid;

  for (pid = 2; pid < PID_MAX; ++pid) if (kill(pid, 0) >= 0)
  {
      puts("Process found: ");
      puti(pid);
      puts("\n");
    }
}
```

编译后，得到结果如下

```
$ ./spawn ./injectable.so propagate
Process found: 1159
Process found: 1160
Process found: 1166
Process found: 1167
Process found: 1176
Process found: 1324
Process found: 1328
Process found: 1352
…
```

一般情况下，都可以发现有100多个用户进程，这说明有100多个潜在感染目标。

## 尝试`PTRACE_SEIZE`

这个技术有一个很大弱点：有些被枚举的进程由于访问限制并不能被调试。对每个进程使用`ptrace`的`PTRACE_SEIZE`请求可以发现哪些进程是可调试的。

> 不使用`PTRACE_ATTACH`，而是使用`PTRACE_SEIZE`，是因为前者会停止目标进程，除非随后使用`PTRACE_CONT`才会恢复运行，而后者是不会停止目标进程的。

`ptrace`是一个可变参数的，这里可以暂时把它简化成4参数的函数

```
long ptrace4(int request, pid_t pid, void *addr, void *data)
{
  long result;
  register void* r10 asm("r10") = data;
  asm volatile("syscall" : "=a" (result) : "a" (__NR_ptrace), "S" (pid), "D" (request), "d" (addr));
  return result;
}
```

现在`propagate`函数就如下了

```
void propagate(void)
{
  pid_t pid;
  int err;

  for (pid = 2; pid < PID_MAX; ++pid) if (kill(pid, 0) >= 0)
  {
      puts("Process found: ");
      puti(pid);
      puts(": ");
      if ((err = ptrace4(PTRACE_SEIZE, pid, NULL, NULL)) >= 0)
      {
        puts("seizable!\n");
        ptrace4(PTRACE_DETACH, pid, NULL, NULL);
      }
      else
      {
        puts("but cannot be debugged : ( [errno=");
        puti(-err);
        puts("]\n");
      }
    }
}
```

它会列出系统里所有可调试的函数

## 结论

之前的测试让我们对这项技术的可行性有了一个快速的了解。从现在开始，剩下的代码将不会离我们期望的常规调试器太远，这是我们的代码将以自动方式运行的最大区别。

***暗号：9ede1***

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过