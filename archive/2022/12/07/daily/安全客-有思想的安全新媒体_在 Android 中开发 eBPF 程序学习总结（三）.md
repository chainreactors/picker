---
title: 在 Android 中开发 eBPF 程序学习总结（三）
url: https://www.anquanke.com/post/id/283911
source: 安全客-有思想的安全新媒体
date: 2022-12-07
fetch_date: 2025-10-04T00:37:57.679316
---

# 在 Android 中开发 eBPF 程序学习总结（三）

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 在 Android 中开发 eBPF 程序学习总结（三）

阅读量**400049**

发布时间 : 2022-12-06 16:29:39

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在研究uprobe的过程中，发现了Linux内核一个好用的功能。

本来是打算研究一下，怎么写uprobe的代码，写好后怎么部署，然后又是怎么和相应的程序对应上的。但是资料太少了，基本上都是写使用bpftrace或者bcc的例子，但是都不是我想要的，后面考虑研究一下bpftrace或者bcc的源码。

不过在这个过程中，却发现了一个Linux系统内置的uprobe插桩的功能。

一般在`/sys/kernel/debug/tracing/`目录下，有一个`uprobe_events`文件，在Android设备下，没有`debug`目录，所以路径一般为: `/sys/kernel/tracing/uprobe_events`

那么我们怎么通过这个文件进行uprobe插桩呢？

首先，我们写一个测试代码：

```
#include <stdio.h>
int main(int argc, char *argv[])
{
  printf("Hello World!\n");
  return 0;
}
```

一个很简单的，使用C语言开发的Hello World程序，编译一下：`$ gcc test.c -o /tmp/test`

接着，我们再写一个脚本：

```
#!/bin/bash
ADDR=`python3 -c 'from pwn import ELF,context;context.log_level="error";e=ELF("/tmp/test");print(hex(e.symbols["main"]))'`
echo "p /tmp/test:$ADDR %x0 %x1" > /sys/kernel/debug/tracing/uprobe_events
echo 1 | tee /sys/kernel/debug/tracing/events/uprobes/p_*/enable
echo 1 | tee /sys/kernel/debug/tracing/tracing_on
cat /sys/kernel/debug/tracing/trace_pipe
```

把这个脚本运行起来，接着，我们再开一个终端，运行一下`/tmp/test`，随后我们就能看到前一个终端里有输出了：

```
root@ubuntu:~# /tmp/test.sh
1
1
            test-3326935 [001] ..... 1187528.405340: p_test_0x76c: (0xaaaaddbc076c) arg1=0x1 arg2=0xffffe00fb1d8
```

接下来，我来对这个解释一下，这个过程中我做的事情：

1. 首先使用pwntools计算出/tmp/test的main函数的地址
2. 因为我的测试环境是arm64的Linux，所以参数寄存器是`x0, x1......`，如果是amd64架构的，参数寄存器就是`di, si, dx......`
3. `p /tmp/test:$ADDR %x0 %x1`的含意就是在/tmp/test程序的ADDR地址处进行插桩，插入的代码目的是输出第一个参数和第二个参数的值，所以我们可以从结果中看到`arg1=0x1 arg2=0xffffe00fb1d8`，也就是说`argc=0x1, argv = 0xffffe00fb1d8`
4. 当我们把上面的语句写入到`uprobe_events`中后，将会在`events/uprobes`目录下生成相应的事件目录，默认情况下是以`p_(filename)_(addr)`的形式命名，所以，在当前测试环境中，这个目录的路径为: `/sys/kernel/debug/tracing/events/uprobes/p_test_0x76c/`
5. 把1写入到上面这个目录的enable文件中，表示激活该事件，接着就是把1写入到`tracing_on`，激活内核的日志跟踪功能。
6. 最后，我们就能从`/sys/kernel/debug/tracing/trace_pipe`目录中看到相关的输出了。

再来看看输出的数据格式：

```
test-3326935, 监控到的程序名-该程序的pid
[001], CPUID
1187528.405340, 时间戳相关？
p_test_0x76c, 事件名
0xaaaaddbc076c, ELF地址
arg1 arg2,  就是我们自己定义的输出内容
```

当我发现Linux内核功能，我是很惊讶的，竟然能这么容易的监控到任意程序的指定地址的信息，就是不知道对于一个程序来说，是否能发现自己被uprobe插桩了。

接着，我就继续深入的研究了该功能，看看使用场景如何。

### 自定义事件名

事件名我们是可以自定义的，比如，我只要把事件语句改为：`"p:test_main /tmp/test:$ADDR %x0 %x1"`。

那么事件名就为`test_main`了，生成的相应目录就是`/sys/kernel/debug/tracing/events/uprobes/test_main/`。

### 输出字符串

通过研究发现，可以使用`-/+`加上`offset`，加上`(addr)`来输出指定地址的内存，然后加上`:type`来指定该数据的类型，并且该操作是可以嵌套的，所以是可以输出任意类型的结构体的。

比如我把事件语句改为: `p:test_main /tmp/test:$ADDR %x0 %x1 +0(%x1):x64 +0(+0(%x1)):string`

我们可以看看现在的输出：

```
root@ubuntu:~# /tmp/test.sh
1
1
            test-3331614 [001] ..... 1189161.610316: test_main: (0xaaaad45607ac) arg1=0x2 arg2=0xffffff3cfef8 arg3=0xffffff3d06ea arg4="/tmp/test"
```

`0xffffff3cfef8`地址的内存为`0xffffff3d06ea`，而`0xffffff3d06ea`地址的内容为字符串：`/tmp/test`，也就是`argv[1]`的内容了。

### 返回值插桩

事件语句的开始是p，表示对当前地址进行插桩，但是如果换成r，那么就是对返回地址进行插桩，比如：`r:test_main /tmp/test:0x7d4 %x0`

`0x7d4`为main函数的ret指令的地址，然后得到的输出为：

```
$ /tmp/test.sh "r:test_main /tmp/test:0x7d4 %x0"1
1
            test-3333703 [000] ..... 1189862.625909: test_main: (0xffffa1239e10 <- 0xaaaac4fa07d4) arg1=0x0
```

数据中多了一个：从当前地址`0xaaaac4fa07d4`要返回到地址`0xffffa1239e10`。

### libc库插桩

libc库的插桩跟普通程序没啥区别，比如，一般https请求都是通过`SSL_write`和`SSL_read`来进行对明文的读写，从socket抓包，抓到的肯定是看不懂的密文。但是从`SSL_write`和`SSL_read`的第二个参数来抓取，得到的就是明文了。

我们来测试一下，一般curl使用的库都是：`/lib/aarch64-linux-gnu/libssl.so.1.1`。

所以我们首先需要使用pwntools从这个libc库中获取到`SSL_write`和`SSL_read`的地址，但是SSL\_read又不同，因为函数入口点buf数据是无用的，需要该函数调用结束后，里面才有有效数据，但是在ret返回的时候，没有寄存器储存buf的地址，目前也没找到办法在函数入口的地方定义一个变量，然后返回的时候再取。

接着，我把libssl.so丢入了ida，找到了`SSL_read`函数：

```
__int64 __fastcall SSL_read(__int64 a1, __int64 a2, int a3)
{
  __int64 result; // x0
  unsigned int v4; // [xsp+20h] [xbp+20h] BYREF

  if ( (a3 & 0x80000000) != 0 )
  {
    ERR_put_error(20LL, 223LL, 271LL, "../ssl/ssl_lib.c", 1777LL);
    return 0xFFFFFFFFLL;
  }
  else
  {
    LODWORD(result) = sub_34830(a1, a2, a3, &v4, 0LL);
    if ( (int)result <= 0 )
      return (unsigned int)result;
    else
      return v4;
  }
}
```

通过`SSL_read`函数，我找到了`sub_34830`函数：

```
__int64 __fastcall sub_34830(__int64 a1, __int64 a2, __int64 a3, _QWORD *a4)
{
  unsigned int v6; // w21
  int v7; // w1
  __int64 v12; // x3
  __int64 v13; // x3
  __int64 v14[3]; // [xsp+40h] [xbp+40h] BYREF
  int v15; // [xsp+58h] [xbp+58h]
  __int64 v16; // [xsp+60h] [xbp+60h]

  if ( *(_QWORD *)(a1 + 48) )
  {
    v6 = *(_DWORD *)(a1 + 68) & 2;
    if ( v6 )
    {
      v6 = 0;
      *(_DWORD *)(a1 + 40) = 1;
    }
    else
    {
      v7 = *(_DWORD *)(a1 + 132);
      if ( v7 == 1 || v7 == 8 )
      {
        ERR_put_error(20LL, 523LL, 66LL, "../ssl/ssl_lib.c", 1744LL);
      }
      else
      {
        sub_49588(a1, 0LL);
        if ( (*(_DWORD *)(a1 + 1496) & 0x100) != 0 && !ASYNC_get_current_job() )
        {
          v12 = *(_QWORD *)(a1 + 8);
          v14[0] = a1;
          v14[1] = a2;
          v13 = *(_QWORD *)(v12 + 56);
          v14[2] = a3;
          v15 = 0;
          v16 = v13;
          v6 = sub_32AD8(a1, v14, sub_329A0);
          *a4 = *(_QWORD *)(a1 + 6168);
        }
        else
        {
          return (*(unsigned int (__fastcall **)(__int64, __int64, __int64, _QWORD *))(*(_QWORD *)(a1 + 8) + 56LL))(
                   a1,
                   a2,
                   a3,
                   a4);
        }     // 猜测这里是ctx->method->ssl_read
      }
    }
  }
  else
  {
    v6 = -1;
    ERR_put_error(20LL, 523LL, 276LL, "../ssl/ssl_lib.c", 1733LL);
  }
  return v6;
}
```

查看调用`ctx->method->ssl_read`的汇编代码:

```
.text:00000000000348A4 loc_348A4                               ; CODE XREF: sub_34830+68↑j
.text:00000000000348A4                 LDR             X4, [X19,#8]
.text:00000000000348A8                 MOV             X3, X24
.text:00000000000348AC                 MOV             X2, X23
.text:00000000000348B0                 MOV             X1, X22
.text:00000000000348B4                 MOV             X0, X19
.text:00000000000348B8                 LDR             X4, [X4,#0x38]
.text:00000000000348BC                 BLR             X4
.text:00000000000348C0                 MOV             W21, W0
.text:00000000000348C4                 LDP             X23, X24, [SP,#0x70+var_40]
.text:00000000000348C8                 B               loc_348E8
```

我们能发现，buf被储存在了X22寄存器里，然后当调用完`ctx->method->ssl_read`，这个时候X22寄存器里就是有效的明文数据了，所以我们可以把uprobe插在`0x348C4`，然后我们以字符串输出寄存器X22，这就是明文数据了。

最后我们可以得到以下事件语句：

```
ADDR=`python3 -c 'from pwn import ELF,context;context.log_level="error";e=ELF("/lib/aarch64-linux-gnu/libssl.so.1.1");print(hex(e.symbols["SSL_write"]))'`
p:SSL_write /lib/aarch64-linux-gnu/libssl.so.1.1:$ADDR +0(%x1):string
p:SSL_read /lib/aarch64-linux-gnu/libssl.so.1.1:0x348C4 +0(%x22):string
```

然后启动我们的脚本，再另一个终端里使用curl访问百度，我们可以得到以下输出：

```
root@ubuntu:~# /tmp/test.sh
1
1
            curl-3339154 [001] ..... 1191831.068149: SSL_write: (0xffffa4b5fc70) arg1="GET / HTTP/1.1
Host: www.baidu.com
User-Agent: curl/7.68.0
Accept: */*

"
            curl-3339154 [001] ..... 1191831.088676: SSL_read: (0xffffa4b5f8c4) arg1="HTTP/1.1 200 OK
Accept-Ranges: bytes
......
```

## 实际应用场景

### 普通程序

Android设备上的ssl库是`/system/lib64/libssl.so`，如果使用该库，那么uprobe插桩的思路跟上面的例子讲的一样。

### 某信APP

研究中发现，插桩了`libssl.so`，但是却没有办法得到Chrome或者某信的流量。经过一番研究，我发现了这篇文章：[自动定位webview中的SLL\_read和SSL\_write

](#jump1)

原来某信用的是webview，其libc位于：`/data/data/com.xxxx/app_xwalk_4317/extracted_xwalkcore/libxwebcore.so`

随后就把这个libc掏出来，丢入IDA，根据上面这篇文章中所说的，去定位`SSL_write`和`SSL_read`。

然后就能成功获取到流量了：

```
$ ./uprobe_test.sh
......
  NetworkService-19594 [006] .... 338986.936127: SSL_write: (0x75c2f17548) buf="GET /webview/xxxxx
......
  NetworkService-19594 [006] .... 338987.021581: SSL_read:...