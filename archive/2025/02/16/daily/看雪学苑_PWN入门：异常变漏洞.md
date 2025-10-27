---
title: PWN入门：异常变漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589653&idx=1&sn=433781729a15abe45f89994393707a90&chksm=b18c295f86fba049f7d3a9a651c1a29212fd93ba75177fa85cf5d761f8cb9ad75936c62a81b0&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-16
fetch_date: 2025-10-06T20:36:57.991887
---

# PWN入门：异常变漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G8whKABhLC3yWDPia7Y6RdgXzDumzR17RFZXhZmlYZm0vay0Je0whWYrx98ztLgFTuKV8eVe1p07w/0?wx_fmt=jpeg)

# PWN入门：异常变漏洞

福建炒饭乡会

看雪学苑

```
一

异常处理机制解析
```

程序出现错误是难免的情况，程序语言和系统为了辅助程序排查问题，设立了各种机制。

**第一种机制是断言检查`assert`，**该函数接受一个表达式作为参数，如果表达式值为假，就会输出错误信息并终止程序。

```
#include <assert.h>
void assert(scalar expression);
```

打印示例如下：

```
main: Assertion `argc > 1' failed.
Aborted (core dumped)
```

**第二种是信号捕捉机制，**信号由内核传递给用户态程序，一般来讲程序收到信号后会执行默认操作，比如收到`SIGKILL`后直接杀死程序，当然C语言中允许程序自定义信号处理函数。

由于信号对于程序来讲是未知的，所以信号捕捉机制可以帮助我们了解程序收到了什么信号，以及什么程序发出的信号等等问题，缓解了未知信号对程序的影响。

**第三种是错误码机制，**不管是函数的返回值还是`errno`都算作是错误码机制，它们用于衡量执行体是否产生了预期内的错误，当错误产生后，返回值和`errno`都会被赋上一个特殊值，当判断语句检测到特殊值后，会进行相应的处理。

一般来讲非指针类型的返回值，在没有发生错误时，会将返回值设置成0，发生错误时会设置成负数。指针类型的返回值，在没有发生错误时，会返回正常的地址，发生错误时会返回NULL。

C语言中的`errno`是ISO C和POSIX标准共同定义的，标准C定义了一系列的已知错误，每种错误信息都有唯一的序号，GLibC中定义了一个名为`errno`的全局变量，用于记录最近发生的已知错误序号，程序可以通过`errno.h`头文件使用该全局变量。

`errno`只是一个数字，它是晦涩难懂的，因此GLibC封装了`perror`函数，该函数会根据`errno`，打错误序号对应的警告信息。

```
void perror(const char *s);
```

**第四种是异常处理机制，**在程序语言中，经常可以看到`try {...} catch {...}`语句的身影，它代表程序会捕捉`try {}`中执行体发生的异常，然后交给`catch {}`处理。

异常机制可以算作是信号机制的扩展，它们都是在捕获到某信息后，把执行流程交给指定的执行体处理，区别在于异常机制不止可以捕获信号。

异常机制还能捕获哪些信息呢？还包含编程语言或系统环境抛出的错误信息。

那么异常处理机制是如何实现的呢？下面以C与C++作为目标语言，以Windows和Linux两大平台为例进行探讨。

## Windows平台

如果你熟悉C语言，应该会知道标准C是没有提供异常处理机制的。这点被延续到Linux当中。

如果你熟悉Windows开发，并对Windows历史有一些了解的话，应该会知道Windows下C语言开发常常会使用一些Winodws自定义的东西，但它们又好像不是标准C的东西。

是的，Windows对标准C的语法进行了扩展，C与C++使用同一套异常处理机制。

### Windows下的异常机制简介

Windows针对异常机制，基于标准C扩展出了下面三条语句，其中`__try {}`标明了捕获结构化异常的范围，位于范围外的语句产生异常时，并不会被捕捉到。

```
Windows中的头文件：
#include <excpt.h>

Windows中的定义：
__try {...}
__except {...}
__finial {...}
```

当`__try {}`中语句出现导致程序产生异常事件时，`__except {}`会将该事件拦截下来，将控制权交到自己手上。

`__finial {}`会在`__try {}`结束后执行，不管异常是否出现，它都会执行。

Windows提供`AbnormalTermination`接口，用于了解程序是否非正常退出`__try`，才进入到`__finial`内部（正常退出返回假，反之则返回真）。

```
Bool AbnormalTermination(void);
```

严格来讲，不只是异常导致的退出才算非正常退出，像`break`、`goto`等流程控制语句离开`__try`时，也算作是非正常退出。

除了这些，Windows还定义了两种接口用于获取异常信息，`GetExceptionInformation`接口用于获取异常描述信息`EXCEPTION_POINTERS`的结构体指针，`GetExceptionCode`接口用于获取异常序号，这个两个接口可以帮助我们了解到底什么原因导致了异常产生。

```
LPEXCEPTION_POINTERS GetExceptionInformation(VOID);
DWORD GetExceptionCode(VOID);
```

基于`__try`的异常捕获机制，在Windows中也被称作是结构化异常`SEH Structured Exception Handling`，它需要与函数体中的执行体绑定，当函数体内出现`__try`语句时，函数会绑定一个异常处理器（多个`__try`语句也是一样），异常处理器会遵循`__except`和`__finial`中设定好的逻辑对异常和终止进行处理。

在WinDBG中，可以借助扩展命令`!exchain`，查看当前线程下的有效处理器。`!exchain`会逐栈帧进行遍历，查找函数中存在的处理器。

```
!exchain
12 stack frames, scanning for handlers...
Frame 0x01: ntdll!RtlDispatchException+0xae (00007ff9`4d03f13e)
  ehandler ntdll!_GSHandlerCheck (00007ff9`4d14a94c)
Frame 0x03: KERNELBASE!RaiseException+0x8a (00007ff9`4a4b837a)
  ehandler KERNELBASE!_GSHandlerCheck (00007ff9`4a51ff8c)
Frame 0x04: ConsoleApplication1!test+0xf9 (00007ff7`63d860a9)
  ehandler ConsoleApplication1!ILT+770(__GSHandlerCheck_SEH) (00007ff7`63d81307)
Frame 0x07: ConsoleApplication1!__scrt_common_main_seh+0x132 (00007ff7`63d823d2)
  ehandler ConsoleApplication1!ILT+45(__C_specific_handler) (00007ff7`63d81032)
Frame 0x0b: ntdll!RtlUserThreadStart+0x2c (00007ff9`4d0ffbcc)
  ehandler ntdll!_C_specific_handler (00007ff9`4d143d00)
```

###

### 二进制文件对SEH的支持

Windows程序在编译会在`.pdata`段中产生一段特殊的数据，这段数据可以看作是一张表，该表包含程序所有用到的函数，表中元素由`RUNTIME_FUNCTION`结构体定义，其中的`UnwindInfo`成员指的是栈展开信息，其余两个成员分别函数起始地址和结束地址。

栈展开信息通常都是和异常处理绑定的。

大部分支持递归的程序语言都会使用栈记录正在执行的函数信息，当异常抛出时，栈上可能还停留着未释放的变量，通过栈展开信息我们可以将函数栈复原，并对未释放变量进行销毁。

```
dt _IMAGE_RUNTIME_FUNCTION_ENTRY
   +0x000 BeginAddress     : Uint4B
   +0x004 EndAddress       : Uint4B
   +0x008 UnwindInfoAddress : Uint4B
   +0x008 UnwindData       : Uint4B

struct RUNTIME_FUNCTION
{
    void *__ptr32 FunctionStart __offset(OFF64|RVAOFF);
    void *__ptr32 FunctionEnd __offset(OFF64|RVAOFF|PASTEND);
    void *__ptr32 UnwindInfo __offset(OFF64|RVAOFF);
};

struct UNWIND_INFO_HDR
{
    char Ver3_Flags __hex;
    char PrologSize __hex;
    char CntUnwindCodes __hex;
    char FrReg_FrRegOff __hex;
};

dt _UNWIND_INFO
ConsoleApplication1!_UNWIND_INFO
   +0x000 Version          : Pos 0, 3 Bits
   +0x000 Flags            : Pos 3, 5 Bits
   +0x001 SizeOfProlog     : UChar
   +0x002 CountOfCodes     : UChar
   +0x003 FrameRegister    : Pos 0, 4 Bits
   +0x003 FrameOffset      : Pos 4, 4 Bits
   +0x004 UnwindCode       : [1] _UNWIND_CODE
```

目前已知的情况是`test`函数内部有三个`__try`语句，其中两个是嵌入包含的关系，有两个`__try`语句匹配`__finally`语句，一个`__try`语句匹配`__except`语句。

```
test
__try {
    ......
    __try {
        ......
    }
    __finally {
        ......
    }
}
__except (puts("filter"), EXCEPTION_EXECUTE_HANDLER) {
    ......
}
__try {
    ......
}
__finally {
    ......
}
```

在生成的`.pdata`中，我们可以看到针对`test`函数生成的信息，一般来讲，一个函数只对应一个`RUNTIME_FUNCTION`表现，这里`test`函数因为异常处理的原因，多个很多表项。

```
.pdata
1. RUNTIME_FUNCTION <rva test, rva byte_140016165, rva stru_14001CCA4>
2. RUNTIME_FUNCTION <rva test$fin$0, rva test$filt$1, rva stru_14001CC88>
3. RUNTIME_FUNCTION <rva test$filt$1, rva test$fin$2, rva stru_14001CC94>
4. RUNTIME_FUNCTION <rva test$fin$2, rva byte_140018475, rva stru_14001C694>
```

1号`RUNTIME_FUNCTION`中的`UnwindInfo`信息是记录处理器的地方。

```
stru_14001CCA4  UNWIND_INFO_HDR <19h, 49h, 5, 45h>
    ......
    dd rva j___GSHandlerCheck_SEH
```

2号到4号`RUNTIME_FUNCTION`主要记录了`__finally {}`的起始地址和`__except (xx)`（筛选器）的起始地址信息。

在WinDBG中，可以借助`.fnnet`命令查看指定函数的`RUNTIME_FUNCTION`和`UNWIND_INFO_HDR`信息。

```
.fnent ConsoleApplication1!test
Exact matches:
    ConsoleApplication1!test (int, int, int, int, int, int)

BeginAddress      = 00000000`00015fb0
EndAddress        = 00000000`00016165
UnwindInfoAddress = 00000000`0001cca4

Unwind info at 00007ff6`78e3cca4, 18 bytes
  version 1, flags 3, prolog 49, codes 5
  frame reg 5 (rbp), frame offs 40h
  handler routine: ConsoleApplication1!ILT+770(__GSHandlerCheck_SEH) (00007ff6`78e31307), data 3
  00: offs 20, unwind op 3, op info 4	UWOP_SET_FPREG.
  01: offs 1b, unwind op 1, op info 0	UWOP_ALLOC_LARGE FrameOffset: 198.
  03: offs 14, unwind op 0, op info 7	UWOP_PUSH_NONVOL reg: rdi.
  04: offs 13, unwind op 0, op info 5	UWOP_PUSH_NONVOL reg: rbp.
```

下面会结合二进制文件与`.fnnet`命令输出的`UnwindInfo`信息进行分析。

```
stru_14001CCA4  UNWIND_INFO_HDR <19h, 49h, 5, 45h>
    ; DATA XREF: .pdata:000000014001FD64↓o
    UNWIND_CODE <<20h, 3, 4>> ; UWOP_SET_FPREG
    UNWIND_CODE <<1Bh, 1, 0>> ; UWOP_ALLOC_LARGE
    dw 33h
    UNWIND_CODE <<14h, 0, 7>> ; UWOP_PUSH_NONVOL
    UNWIND_CODE <<13h, 0, 5>> ; UWOP_PUSH_NONVOL
    align 4
    dd rva j___GSHandlerCheck_SEH
```

`Unwind info at`是`UnwindInfo`信息开始标志，后面的地址是`UnwindInfo`信息所在内存的地址，它是基地址加上`UnwindInfoAddress`得到的结果。

`UNWIND_INFO_HDR`中的0x19通过二进制查看，0x19对应二进制`b0001 1001`，前三个比特位`b001`对应`version`，后面的`b011`对应`flags`。

`flags`的数值来源于下方的四种类别，当前值为0x3，说明函数内部同时含有异常处理程序和终止处理程序，这可以和`test`函数呼应上。

```
UNW_FLAG_NHANDLER  | 0x0 | 无处理程序
UNW_FLAG_EHANDLER  | 0x1 | 有异常处理程序
UNW_FLAG_UHANDLER  | 0x2 | 有终止处理程序
UNW_FLAG_CHAININFO | 0x4 | FunctionEntry是先前函数表的表项。
```

0x49对应的是`prolog`，`prolog`对应函数序言的大小。

0x5对应的是`codes`，它记录了`UnwindCode`的数量。

0x45对应的是栈帧信息，它也需要从二进制的角度观察，比特0到比特4对应栈帧寄存器（0x5），其余比特位对应栈帧寄存器偏移（0x40），栈帧寄存器指的就是栈，它保存上的局部变量，0x5代表局部变量区域的起始编号，0x4乘0x10就是局部变量区域相对于栈底`rsp`的偏移值大小。

接下来就是`UnwindCode`，`UnwindCode`记录了函数需要中操作`rsp`和非易失寄存器的指令信息，它由三部分组成`<<1, 2, 3>> xxx`，此处以`<<20h, 3, 4>> UWOP_SET_FPREG`为例进行讲解，0x20代表指令相对于起始地址的偏移值，3与`UWOP_SET_FPREG`是一样的，代表指令类型，4操作的寄存器信息，4对应`rsp`寄存器。

```
起始为0xb0
0xc3 push    rdi
0xc4 sub     rsp,198h
0xcb lea     rbp,[rsp+40h]
0xd0 lea     rdi,[rsp+40h]
```

最后一项就是处理器信息，如果`flags`中显示函数存在处理器，那么这里就会有内容，它是可选的内容，并不是必要的。

### Windows处理异常的基本流程

CPU发现异常时，会先通过IDT表找到内核异常处理函数，当内核发现异常发生在用户态空间时，内核会把控制权交还给用户态程序。

回到用户态程序时，会先进入`KiUserExceptionDispatch`函数处理异常，该函数会通过`RtlDispatchException`函数会查找异常处理器，并对异常进行处理。

```
ntdll!KiUserExceptionDispatch
    -> ntdll!RtlDispatchException
```

这两个函数都源自于动态链接库ntdll，ntdll的全称是`NT Layer DLL`，它是NT内核的一部分，用于提供用户态程序与内核的交互接口，这里的异常处理就是一个实例，RTL的全称是`Runtime Library`，即运行时库，RTL一部分于ntdll中，还有一部分位于ntoskrnl中，ntoskrnl是NT内核的基石，它是Windows上最先启动的进程，当它运行后，其余的所有程序都会在它的管控之下工作。

在了解`RtlDispatchE...