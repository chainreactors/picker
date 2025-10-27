---
title: 模糊测试 ASan 模式下有关堆的 ASan Redzone 和 Check 的源码解析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578852&idx=1&sn=ce8b39f33a8b477944a917e6e1cec9ef&chksm=b18ddf2e86fa5638101e6e245ec0988622454fdd9f9cd0adc671f9c04a10eac67788a60210df&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-20
fetch_date: 2025-10-06T18:50:04.019297
---

# 模糊测试 ASan 模式下有关堆的 ASan Redzone 和 Check 的源码解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOE6UzaKiaOYPEQjricZChU1icziaj02t8rFUSwAln7kNfyR6VzziahibWBfibw/0?wx_fmt=jpeg)

# 模糊测试 ASan 模式下有关堆的 ASan Redzone 和 Check 的源码解析

Loserme

看雪学苑

##

```
一

引言
```

###

### **模糊测试与 ASan 的概述**

模糊测试（Fuzz Testing）是一种自动化的软件测试技术，旨在通过向程序提供随机或异常输入来检测其漏洞与崩溃。它能够有效捕捉输入处理中的异常，特别是与内存相关的问题。模糊测试在寻找未知错误方面尤为有用，因为它无需预定义输入模式，通过生成各种异常数据，增加程序失效的可能性。

AddressSanitizer（ASan）是一种强大的内存错误检测工具，主要用于检测运行时的内存问题，如缓冲区溢出、内存越界、未初始化内存的使用以及内存泄漏。ASan 在模糊测试中至关重要，因为它可以捕获许多模糊测试过程中暴露出的内存错误，帮助开发者更快、更有效地定位潜在问题。

### **文章目的**

本篇文章的目的是深入解析 ASan 模式下，堆内存的保护机制，尤其是 Redzone 和 Check 的相关源码。文章将通过对源码的详细解读，揭示 ASan 如何通过 Redzone 和 Check 机制标记和监控内存的使用状态，进而检测越界访问和内存泄漏等问题。
文章主要大纲:

◆堆的 ASan Redzone 标记机制解析

◆堆的ASan Check 机制解析

##

```
二

ASan 原理概述
```

**ASan 的工作的简单案例**

写了一个Makefile 定义了两种不同版本的内存错误检测程序的编译流程，分别是带有 ASAN 插桩的版本和普通版本。ASAN 插桩版本用于动态检测程序中的内存错误（如使用释放的内存、越界访问等），而未插桩版本则是用于对比执行的正常程序版本。源码可以直接让GPT生成这里就不给出了代码文件了,就给出makefile文件。

Makefile文件:

```
# 定义编译器和编译选项
CC = gcc
CFLAGS = -g -Wall
ASAN_FLAGS = -fsanitize=address

# 要编译的源文件
SRCS = use_after_free.c heap_out_of_bounds.c stack_out_of_bounds.c \
       global_out_of_bounds.c return_local_variable.c memory_leak.c

# 生成的可执行文件 (插桩和未插桩)
INSTRUMENTED_TARGETS = use_after_free_asan heap_out_of_bounds_asan  \
                        memory_leak_asan
NON_INSTRUMENTED_TARGETS = use_after_free heap_out_of_bounds  \
                            memory_leak

# 默认目标: 编译插桩和未插桩版本
all: instrumented non_instrumented

# 编译插桩版本
instrumented: $(INSTRUMENTED_TARGETS)

use_after_free_asan: use_after_free.c
    $(CC) $(CFLAGS) $(ASAN_FLAGS) -o $@ $<

heap_out_of_bounds_asan: heap_out_of_bounds.c
    $(CC) $(CFLAGS) $(ASAN_FLAGS) -o $@ $<

memory_leak_asan: memory_leak.c
    $(CC) $(CFLAGS) $(ASAN_FLAGS) -o $@ $<

# 编译未插桩版本
non_instrumented: $(NON_INSTRUMENTED_TARGETS)

use_after_free: use_after_free.c
    $(CC) $(CFLAGS) -o $@ $<

heap_out_of_bounds: heap_out_of_bounds.c
    $(CC) $(CFLAGS) -o $@ $<

memory_leak: memory_leak.c
    $(CC) $(CFLAGS) -o $@ $<

# 清理编译生成的文件
clean:
    rm -f $(INSTRUMENTED_TARGETS) $(NON_INSTRUMENTED_TARGETS)

.PHONY: all clean instrumented non_instrumented
```

#### UAF漏洞爆出(ERROR:Addresssanitizer:heap-use-after-free)

以asan模式手动编译的命令:

```
clang use_after_free.c -fsanitize=address -o use_after_free_asan
或者
gcc use_after_free.c -fsanitize=address -o use_after_free_asan
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOsiawAKbZnJaWoV9w8xvjcGMEkuRWOCfgUzkUmjZwU96DVibCeOBNeNkw/640?wx_fmt=png&from=appmsg)

####

#### 栈溢出漏洞爆出(ERROR:Addresssanitizer:stack-buffer-overflow)

以asan模式手动编译的命令:

```
clang stack_out_of_bounds.c -fsanitize=address -o stack_out_of_bounds
或者
gcc stack_out_of_bounds.c -fsanitize=address -o stack_out_of_bounds
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaORAiaM78QYCicLUgkyrLibo2gPjOeZZRRaWU6bYyXNI6UvtVW53aj4Qg4w/640?wx_fmt=png&from=appmsg)

####

#### 其他可以用的Asan模式编译选项

**Address Sanitizer(-fsanitize=address)**:用于检测运行时的内存错误，例如**越界访问**、**使用已释放的内存**（UAF，Use-After-Free）、**堆栈溢出**、**双重释放**、以及其他与内存管理相关的错误。

**Memory Sanitizer (-fsanitize=memory)**：主要用于检测**未初始化内存的使用**和**对已释放内存的操作**。它可以帮助发现未初始化的变量或内存空间的读取，这是常见的、难以追踪的错误。

**UndefinedBehaviorSanitizer (-fsanitize=undefined)**：检测程序中潜在的**未定义行为**，例如**整数溢出**、**空指针解引用**、**未对齐的内存访问**等。C 和 C++ 中的许多行为在标准中是未定义的，此工具可以帮助识别这些问题。

**Thread Sanitizer (-fsanitize=thread)**：专门用于检测**多线程程序中的数据竞争**问题。它可以监视多个线程对同一变量或内存位置的并发访问，帮助识别和修复潜在的并发 bug，如**数据竞争**和**死锁**。

**Address Sanitizer with Leak Detection (-fsanitize=leak)**：AddressSanitizer 的一个扩展，用于检测**内存泄漏**。内存泄漏是指分配的内存没有被释放，从而导致内存的浪费，长时间运行会导致程序崩溃或资源耗尽。

**Coverage Sanitizer (-fsanitize=coverage)**：专为**Linux 内核模块开发**设计，用于检测内核中的**内存错误**。这是内核版本的 AddressSanitizer，检测内核模块中的内存越界、使用已释放内存等错误。

**Kernel****Address Sanitizer (-fsanitize=kernel-address)**：针对 Linux 内核模块开发，用于检测内核中的内存错误。

### **ASan 的工作原理**

#### 1.ASAN 是用于动态检测内存错误的工具

ASAN 可以通过编译时的插桩（instrumentation）和运行时的动态检查，帮助开发者检测和调试内存相关的错误。它在编译期间会为每个内存分配和释放操作添加额外的代码，确保在运行过程中对内存的每次读写都经过 ASAN 的验证，从而发现内存问题。

#### 2. ASAN 将数据区域分为两种：可访问区域和不可访问区域 （redzone）

在程序运行时，ASAN 会为每个内存块设置边界标记。每次内存分配时，ASAN 在正常的可用内存区域周围插入一些不可访问的区域，称为**redzone**。这些区域主要用于检测越界访问。

◆**可访问区域**是正常分配的内存空间，供程序读取和写入数据。

◆**不可访问区域 (redzone)**是在内存块两侧添加的一些填充区域，作为缓冲区，防止越界访问。redzone 的存在可以捕获那些访问未分配或已经释放的内存操作。

这些 redzone 通常不会引发程序立即崩溃，而是被 ASAN 用来记录和标记潜在的内存问题。这样，当发生越界访问时，ASAN 能够识别并报告这些问题，帮助开发者找到问题所在。

#### 3. ASAN 影子内存 (Shadow Memory) 的作用

ASAN 引入了一种称为**影子内存 (shadow memory)**的技术，用于跟踪主内存的可访问性状态。影子内存和正常内存的比例是**1:8**，即每 1 字节的影子内存可以描述 8 字节的正常内存。这意味着，影子内存中的每个字节对应主内存中的 8 个字节，用于标记这些字节是否可访问。

◆如果主内存的某一部分是可访问的，影子内存中的相应位就会被标记为“可访问”。

◆如果主内存的某一部分处于 redzone，影子内存中的相应位就会被标记为“不可访问”。

在每次内存访问时，ASAN 会查询影子内存以判断该访问是否合法。如果访问的是不可访问区域，ASAN 会立即报告错误并提示开发者。

#### 4.**影子内存的布局和工作机制**

影子内存的具体实现与内存的映射有关。ASAN 会通过影子内存中的字节位信息来判断内存的状态：

◆对于正常的 8 字节内存，影子内存中的值为 0，表示这 8 字节都是可访问的。

◆如果某些字节不可访问（如处于 redzone 或者被释放），影子内存中的值会被设置为特定的标记。

◆ASAN 的检测代码会在每次内存访问时通过影子内存验证目标地址的状态，如果发现异常立即触发报错。

##

```
三

堆的 ASan Redzone 标记机制解析
```

### **Redzone 的设置和取消**

#### 堆溢出案例分析

这是heap\_out\_of\_bounds.c正常编译出来的IDA伪代码:

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+4h] [rbp-Ch]
  int *arr; // [rsp+8h] [rbp-8h]

  arr = (int *)malloc(0x14uLL);
  for ( i = 0; i <= 5; ++i )
    arr[i] = i;
  free(arr);
  return 0;
}
```

这个代码实现的功能是向堆块内写入6个int整数,占用0x20个字节,但是堆块的大小只有0x14个字节存在堆溢出漏洞.正常情况下是不会导致程序奔溃的。

这是heap\_out\_of\_bounds.c以asan模式编译后的IDA伪代码:

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int *v3; // rcx
  int i; // [rsp+4h] [rbp-Ch]
  int *arr; // [rsp+8h] [rbp-8h]

  arr = malloc(0x14uLL);
  for ( i = 0; i <= 5; ++i )
  {
    v3 = &arr[i];
    //在进行赋值前检测内存的可访问性
    if ( *((v3 >> 3) + 0x7FFF8000) != 0 && (((4 * i + arr) & 7) + 3) >= *((v3 >> 3) + 0x7FFF8000) )
      __asan_report_store4(&arr[i]);//发现不可以访问就报错
    *v3 = i;
  }
  free(arr);
  return 0;
}
```

这是堆溢出漏洞经过Asan模式插桩以后的样子,被插入了一段校验代码,每次在向堆写入数据时都会检查是否发生堆溢出。

我们这部分主要是讲解堆内存是如何被标记Redzone即不可访问的!这要引入一个之前提到的影子内存（Shadow Memory）概念,这片内存放了真实内存可以被访问的内存数.通过伪代码可以发现并未实现堆块内存的redzone设置,因为这些操作被隐藏在了malloc函数中,源码如下:

#### malloc申请堆块后标记内存可用区域

当程序通过`malloc`分配内存时，ASan 会相应地在影子内存中标记该内存区域为可用，并且设置两个 redzone 区域，来防止越界访问。

**相关源码位置**:

`llvm-project\compiler-rt\lib\asan\asan_allocator.cpp`
源码位置:llvm-project/compiler-rt/lib/asan/asan\_allocator.cpp at main · llvm/llvm-project (github.com)

```
//源码:asan_allocator.cpp
...
static Allocator instance(LINKER_INITIALIZED);
...
void *asan_malloc(uptr size, BufferedStackTrace *stack) {
  return SetErrnoOnNull(instance.Allocate(size, 8, stack, FROM_MALLOC, true));
}
...

// 拦截器函数：替代 malloc 函数的实现
INTERCEPTOR(void*, malloc, uptr size) {
  if (DlsymAlloc::Use())
    return DlsymAlloc::Allocate(size);  // 使用自定义分配逻辑

  GET_STACK_TRACE_MALLOC;  // 获取堆栈信息
  return asan_malloc(size, &stack);  // 使用 ASan 的内存分配逻辑
}
...
```

首先我们使用的malloc函数不是原来glibc里面的函数了,而是Asan实现的asan\_malloc函数!可以通过源码查找发现他具体进行的操作,继续往内部追寻就可以发现!

```
// -------------------- 分配/释放例程 ---------------
void *Allocate(uptr size, uptr alignment, BufferedStackTrace *stack,
               AllocType alloc_type, bool can_fill) {
  // 如果AddressSanitizer (ASan) 未初始化，则进行初始化
  // UNLIKELY 用于优化分支预测，表示该条件不太可能为真
  if (UNLIKELY(!AsanInited()))
    AsanInitFromRtl();  // 初始化 ASan 运行时库
  ...

  // 如果使用的是次分配器（from_primary为false）或影子内存尚未被污染（即影子内存值为0），则对内存进行标记（污染）
  // MEM_TO_SHADOW将分配的实际内存地址映射到影子内存地址
  if (!from_primary || *(u8 *)MEM_TO_SHADOW((uptr)allocated) == 0) {
    // 计算分配的用户区域结束地址，向上对齐到ASAN_SHADOW_GRANULARITY的倍数（通常为8字节）
    uptr tail_beg = RoundUpTo(user_end, ASAN_SHADOW_GRANULARITY);
    // 计算实际分配的内存块结束地址，包括分配器的管理开销
    uptr tail_end = alloc_beg + allocator.GetActuallyAllocatedSize(allocated);

    // 对分配的左侧redzone区域进行毒化，防止越界写入左侧内存区域
    PoisonShadow(alloc_beg, user_beg - alloc_beg, kAsanHeapLeftRedzoneMagic);
    // 对分配的右侧redzone区域进行毒化，防止越界写入右侧内存区域
    PoisonShadow(tail_beg, tail_end - tail_beg, kAsanHeapLeftRedzoneMagic);
  }

  // 计算对齐后的用户区域大小，向下对齐到ASAN_SHADOW_GRANULARITY的倍数
  uptr size_rounded_down_to_granularity = RoundDownTo(size, A...