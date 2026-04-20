---
title: 【翻译】windows10内核堆池研究
url: https://mp.weixin.qq.com/s/ikuiJNzbCf532qzPVqZ1YA
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:53:32.199903
---

# 【翻译】windows10内核堆池研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bz5OjA3RpuicucMWuydolWLaRKnwWNKEypXuuEpGHBptG1gOofXjZaWLc398ibTbEoQJo6eOHUPks7zCIoPPvHveHdRFCdBTspvCxNJlOoCdI/0?wx_fmt=jpeg)

# 【翻译】windows10内核堆池研究

原创

joe1sn
joe1sn

不止Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文：SSTIC2020-Article-pool\_overflow\_exploitation\_since\_windows\_10\_19h1-bayet\_fariello

https://www.sstic.org/media/SSTIC2020/SSTIC-actes/pool\_overflow\_exploitation\_since\_windows\_10\_19h1/SSTIC2020-Article-pool\_overflow\_exploitation\_since\_windows\_10\_19h1-bayet\_fariello.pdf

# Scoop the Windows 10 pool!

Corentin Bayet and Paul Fariellocorentin.bayet@synacktiv.compaul.fariello@synacktiv.comSynacktiv

**摘要**：堆溢出是应用程序中一种相当常见的漏洞。利用此类漏洞往往需要对用于管理堆的底层机制有深入的理解。Windows 10 近期更改了其在内核空间中管理堆的方式。本文旨在介绍 Windows NT 内核中堆管理机制的最新演进，并展示针对内核池（Kernel Pool）的全新漏洞利用技术。

# 1. 引言

在 Windows 系统中，“池”（Pool）是指为内核空间预留的堆内存区域。多年来，内核空间的池分配器一直具有高度的特殊性，且与用户空间的分配器截然不同。然而，自 2019 年 3 月发布的 Windows 10 19H1 更新以来，这一状况发生了改变。用户空间中那个广为人知且已有详尽文档记录的“分段堆”（Segment Heap）[7] 被引入到了内核空间。尽管如此，内核中所实现的分段堆分配器与用户空间的版本之间仍存在某些差异，因为内核空间依然存在一些特定的资源与需求。本文将从漏洞利用（Exploitation）的视角出发，重点探讨内核分段堆中那些独有的内部机制。本文所呈现的研究内容专门针对 x64 架构。针对其他不同架构所需的适配与调整，本文暂未进行深入探究。在简要回顾了内核池分配器的历史演变及内部机制之后，本文将详细阐述分段堆在内核中的具体实现方式，以及它对内核池特有资源所产生的影响。随后，本文将介绍一种针对内核池内部机制的新型攻击手段，该攻击可用于利用内核池中的堆溢出漏洞。最后，本文将展示一种通用的漏洞利用技术：该技术仅需极小且可控的堆溢出条件，即可实现本地权限提升，将权限层级从“低完整性”（Low Integrity）提升至“SYSTEM”级别。

## 1.1 内存池内部机制

本文将不深入探讨内存池分配器的内部细节，因为这一主题此前已在诸多文献中得到广泛阐述 [5]；不过，为了确保读者能对本文内容有全面的理解，在此仍需简要回顾一些关键的内部机制。本节将介绍 Windows 7 系统中内存池的一些内部结构，以及过去几年间针对内存池所引入的各类缓解措施与改进。此处所阐述的内部机制将重点聚焦于那些恰好容纳在单个内存页（page）内的内存块（chunk），因为这类分配是内核中最常见的内存分配类型。至于大小超过 0xFE0 字节的内存分配，其行为模式有所不同，因此不在本文的探讨范围之内。

**内存池分配**：Windows 内核中用于分配和释放内存的主要函数，分别是 `ExAllocatePoolWithTag` 和 `ExFreePoolWithTag`。

```
PVOIDExAllocatePoolWithTag(
  [in] __drv_strictTypeMatch(__drv_typeExpr)POOL_TYPEPoolType,
  [in] SIZE_T                                         NumberOfBytes,
  [in] ULONG                                          Tag
);
```

```
VOIDExFreePoolWithTag(
  [in] PVOIDP,
  [in] ULONGTag
);
```

`PoolType` 是一个位字段，其关联的枚举如下：

```
NonPagedPool                          = 0
PagedPool                             = 1
NonPagedPoolMustSucceed               = 2
DontUseThisType                       = 3
NonPagedPoolCacheAligned              = 4
PagedPoolCacheAligned                 = 5
NonPagedPoolCacheAlignedMustSucceed   = 6
MaxPoolType                           = 7
PoolQuota                             = 8
NonPagedPoolSession                   = 20h
PagedPoolSession                      = 21h
NonPagedPoolMustSucceedSession        = 22h
DontUseThisTypeSession                = 23h
NonPagedPoolCacheAlignedSession       = 24h
PagedPoolCacheAlignedSession          = 25h
NonPagedPoolCacheAlignedMustSSession  = 26h
NonPagedPoolNx                        = 200h
NonPagedPoolNxCacheAligned            = 204h
NonPagedPoolSessionNx                 = 220h
```

`PoolType` 中可以存储多项信息：

* 所使用的内存类型，包括 `NonPagedPool`、`PagedPool`、`SessionPool` 或 `NonPagedPoolNx`；
* 分配操作是否为关键操作（第 1 位）且必须成功。如果分配失败，将触发 `BugCheck`（系统崩溃）；
* 分配的内存是否按缓存行大小对齐（第 2 位）；
* 分配操作是否使用了 PoolQuota 机制（第 3 位）；
* 其他未文档化的机制。

所使用的内存类型至关重要，因为它能将不同的内存分配操作隔离在不同的内存区域中。两种主要的内存类型是`PagedPool`和 `NonPagedPool`。MSDN 文档对此作了如下描述：

> 非分页池(`NonPagedPool`)是不可分页的系统内存。它可以在任何 IRQL 级别下被访问，但由于它是一种稀缺资源，驱动程序应仅在必要时才对其进行分配。分页池是可分页的系统内存，仅可在 `IRQL < DISPATCH_LEVEL` 的级别下进行分配和访问。

正如第1.2节所述，`NonPagedPoolNx` 已在 Windows 8 中引入，且必须用于替代 `NonPagedPool`。

`SessionPool` 用于会话空间的内存分配，且对于每个用户会话而言都是唯一的。它主要由`win32k` 组件使用。

最后，标签（Tag）是一个非零的字符字面量，长度为一至四个字符（例如：`'Tag1'`）。建议内核开发人员针对不同的代码路径使用唯一的内存池标签（Pool Tag），以协助调试器和验证工具识别特定的代码路径。

**`POOL_HEADER`**：在内存池中，所有能够容纳于单个页面的内存块（Chunk）均以一个 `POOL_HEADER` 结构体作为起始。该结构体包含了内存分配器所需的各类信息，以及前述的标签。当尝试利用 Windows 内核中的堆溢出（Heap Overflow）漏洞时，首当其冲会被覆盖的便是 `POOL_HEADER` 结构体。攻击者此时面临两种选择：一是妥善重写 `POOL_HEADER` 结构体，进而攻击紧邻的下一个内存块中的数据；二是直接针对 `POOL_HEADER` 结构体本身发起攻击。

在这两种攻击场景中，`POOL_HEADER` 结构体均会被覆盖；因此，若要成功利用此类漏洞，必须对该结构体中的每一个字段及其具体用途有着透彻的理解。本文将重点探讨那些直接针对 `POOL_HEADER` 结构体发起的攻击手段。

```
structPOOL_HEADER
{
    char  PreviousSize;
    char  PoolIndex;
    char  BlockSize;
    char  PoolType;
    int   PoolTag;
Ptr64ProcessBilled;
};

0: kd>dtnt!_POOL_HEADER
   +0x000 PreviousSize     : Pos0, 8Bits
   +0x000 PoolIndex        : Pos8, 8Bits
   +0x002 BlockSize        : Pos0, 8Bits
   +0x002 PoolType         : Pos8, 8Bits
   +0x000 Ulong1           : Uint4B
   +0x004 PoolTag          : Uint4B
   +0x008 ProcessBilled    : Ptr64_EPROCESS
   +0x008 AllocatorBackTraceIndex : Uint2B
   +0x00a PoolTagHash      : Uint2B
```

![image-20260417142711869](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpuic3o7yibIxicAGytTl2T7gia2V4dhiaibkwEwNyQvJW0SaVMKT20H8aL5ezLzGYySOy350djmfFwCEvPezEumpYicA2tgSR5vuibhMezU/640?wx_fmt=png&from=appmsg)

Fig.3. Simplified POOL\_HEADER structure in Windows 1809

如图 [3] 所示的 `POOL_HEADER` 结构，虽然随时间推移发生过细微演变，但其主要字段始终保持不变。在 Windows 1809 版本中（即 Windows 19H1 之前），该结构的所有字段均处于使用状态：

* **`PreviousSize`**： 表示前一个内存块的大小除以 16 的值；
* **`PoolIndex`** 是 `PoolDescriptor` 数组中的一个索引；
* **`BlockSize`** 表示当前分配块的大小除以 16 的值；
* **`PoolType`** 是一个位字段，用于存储有关分配类型的信息；
* **`ProcessBilled`** 是指向执行该内存分配操作的 `KPROCESS` 对象的指针。仅当 `PoolType` 字段中设置了 `PoolQuota` 标志时，该指针才会被赋值。

## 1.2 自 Windows 7 以来的攻击与缓解措施

Tarjei Mandt 及其论文《Windows 7 内核池利用》（Kernel Pool Exploitation on Windows 7）[5] 是针对内核池攻击领域的权威参考资料。该论文详尽阐述了内核池的内部机制及多种攻击手段，其中部分攻击专门针对 `POOL_HEADER` 结构。

该论文中所描述的一种攻击手段是“配额进程指针覆盖”（`Quota Process Pointer Overwrite`）。这种攻击利用堆溢出漏洞，覆盖了已分配内存块（chunk）中的 `ProcessBilled` 指针。当该内存块被释放时，如果其 `PoolType` 字段包含 `PoolQuota` 标志（0x8），系统便会利用该指针进行解引用操作。通过控制这一指针，攻击者便获得了“任意解引用”这一原语，这足以实现从用户态到更高权限的提权。图4展示了这一攻击过程。

![image-20260417142837372](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibcIBWcX23aDDKMOAD5L5ALUchCicVgkmGe6NAOzkWeROdxb4UlvXUlzFMwFRCcCt6omtGU7hvcYICgYp7QFCu4OtlSJklhO1XM/640?wx_fmt=png&from=appmsg)

自 Windows 8 起，随着 `ExpPoolQuotaCookie` 的引入，这一攻击手段已得到缓解。该 `Cookie` 在系统启动时随机生成，用于保护指针免受攻击者的覆盖。例如，它被用于对 `ProcessBilled` 字段执行异或（XOR）运算：

```
ProcessBilled=KPROCESS_PTR^ExpPoolQuotaCookie^CHUNK_ADDR
```

当该内存块被释放时，内核会检查编码后的指针是否为一个有效的 KPROCESS 指针：

```
//ExFreeHeapPool

PsInitialSystemProcess= (chunkAddr^ExpPoolQuotaCookie^chunkAddr->ProcessBilled);
      if ( PsInitialSystemProcess )
      {
        if ( PsInitialSystemProcess<0xFFFF800000000000uLL|| (PsInitialSystemProcess->Header.Type&0x7F) !=3 )
          KeBugCheckEx([...]);
        //...;
```

![image-20260417143406635](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu9Fq3cZF66EGM6ypn8vGLich3Pyw5umxoXduzKwvUwsP76UZ3XgkURSSjce6yLlibj5m0Te4WuWlK4WIQW8L33xxouV7CiaNomIVA/640?wx_fmt=png&from=appmsg)

若无法获知内存块（chunk）的地址以及 `ExpPoolQuotaCookie` 的数值，便无法构造出有效的指针，从而也就无法实现任意地址解引用。不过，通过在 `PoolType` 字段中不设置 `PoolQuota` 标志位，仍然可以成功重写 `POOL_HEADER` 结构体，进而实施全面的数据攻击。关于“配额进程指针覆盖攻击”（Quota Process Pointer Overwrite attack）的更多详情，可参阅 Nuit du Hack XV 大会上的相关议题 [1]。

**`NonPagedPoolNx`**：自 Windows 8 起，引入了一种新型的内存池类型：`NonPagedPoolNx`。它的工作机制与 `NonPagedPool` 如出一辙，唯一的区别在于其内存页不再具备可执行属性；这一特性有效遏制了所有利用此类内存来存储 Shellcode 的攻击手段。此前分配于 `NonPagedPool` 中的内存资源，现已转由 `NonPagedPoolNx` 进行分配；不过，`NonPagedPool` 这一类型仍被保留了下来，主要是为了确保与第三方驱动程序的兼容性。即便在当下的 Windows 10 系统中，仍有大量的第三方驱动程序在使用具备可执行属性的 `NonPagedPool`。

随着时间的推移，各项缓解措施相继引入，使得利用堆溢出攻击 `POOL_HEADER` 的手法不再具有吸引力。如今，更简便的攻击方式是妥善重写 `POOL_HEADER`，进而攻击紧邻的下一个堆块（chunk）中的数据。然而，随着“分段堆”（Segment Heap）机制被引入到内存池中，`POOL_HEADER` 的使用方式也随之发生了改变；本文将展示如何再次针对 `POOL_HEADER` 发起攻击，从而利用内核内存池中的堆溢出漏洞。

# 2 结合分段堆的池分配器

## 2.1 分段堆的内部机制

自 Windows 10 19H1 版本起，分段堆（Segment Heap）便已应用于内核空间，且其设计与用户空间所使用的分段堆颇为相似。本节旨在介绍分段堆的主要特性，并重点阐述其与用户空间分段堆之间的差异。关于用户空间分段堆内部机制的详尽解析，可参阅文献 [7]。

正如用户空间的分段堆一样，内核分段堆旨在根据分配请求的大小，提供不同的功能特性。为此，系统定义了四种所谓的“后端”（backends）。

* 低碎片堆（Low Fragmentation Heap 简称 LFH）：`RtlHpLfhContextAllocate`
* 可变大小（Variable Size  简称 VS）：`RtlHpVsContextAllocateInternal`
* 段分配（Segment Alloc 简称 Seg）：`RtlHpSegAlloc`
* 大块分配（Large Alloc）：`RtlHpLargeAlloc`

请求分配大小与所选后端之间的映射如图 5 所示。

前三个后端`Seg`、`VS` 和 `LFH`，分别关联着一个上下文：`_HEAP_SEG_CONTEXT`、`_HEAP_VS_CONTEXT` 和 `_HEAP_LFH_CONTEXT`。这些后端上下文存储在 `_SEGMENT_HEAP` 结构中。

![image-20260417144601866](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibGYSOiaAOe7...