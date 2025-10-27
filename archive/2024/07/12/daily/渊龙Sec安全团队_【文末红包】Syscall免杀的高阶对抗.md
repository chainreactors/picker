---
title: 【文末红包】Syscall免杀的高阶对抗
url: https://mp.weixin.qq.com/s?__biz=Mzg4NTY0MDg1Mg==&mid=2247485559&idx=1&sn=0fd4d31956824b33c2abb39ab2d76374&chksm=cfa4938cf8d31a9ab1b1b01201c728563850296998e6c6c6401a9b6820d8a5b95c91b7a6263b&scene=58&subscene=0#rd
source: 渊龙Sec安全团队
date: 2024-07-12
fetch_date: 2025-10-06T17:44:53.751717
---

# 【文末红包】Syscall免杀的高阶对抗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6Nrv2DSQYOpPgFBvrtOKVOjJRiawvWl7SQ3g4PicOITHaAGooPc4aw8ew/0?wx_fmt=jpeg)

# 【文末红包】Syscall免杀的高阶对抗

原创

凝

渊龙Sec安全团队

> 微信公众号：**渊龙Sec安全团队**
> 为国之安全而奋斗，为信息安全而发声！
> 如有问题或建议，请在公众号后台留言
> **如果你觉得本文对你有帮助，欢迎在文章底部赞赏我们**

### 1# 免杀现状概述

从现在杀软对抗的角度和技术来讲，`syscall` 可以说是 `loader` 中一个不可缺少的技术。为什么 `syscall` 逐渐成为主流？

很早之前杀软其实只会对 `kernel32` 中一些函数进行 `hook`，所以恶意程序开发者使用 `ntdll` 中的函数去实现 `loader` 的免杀效果是远高于直接或者间接使用 `kernel32` 中的函数，比如 `VirtualAlloc` 之类的函数。

我们又不能直接通过动态调用的方式的去加载 `ntdll` 中的函数，原因是调用链比较明显（使用 `GetModuleHandle`，`GetProcAddress`）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6OhibZP6cgCjFUhJOOq1ZOegCL0QMiaPdPGGMa7SbMJcFJ69KgC8a5ZSQ/640?wx_fmt=png&from=appmsg)

随着时代的进步，逐渐有人创造**间接调用**这个概念，也就是我们现在熟悉的**地狱之门**，当然这里我们不再去深度讨论一些关于地狱之门之类的话题。

当然俗话说的好，魔高一尺道高一丈，杀软也已经开始 `hook ntdll` 了，当然目前来说`r3` 层 `hook` 杀软已经不再是主流，像卡巴已经移除了 `r3` 层的 `hook`。

> 注明：本文中的 `Syscall` 调用适用于任意版本Windows系统，只支持x64系统。

### 2# Syscall由浅入深

知己知彼，百战不殆。只有深入了解执行架构的相关原理，才能更好的理清楚思路做好免杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6rxKjMicXOJn0iaUVpXTcqUwrS7MLwhCJKfQapfWSxbzDbJWrE1fVu6vw/640?wx_fmt=png&from=appmsg)

在Windows系统中，调用 `syscalls` 充当程序与系统交互的接口，使它们能够请求特定服务，例如读取或写入文件、创建新进程或分配内存。

例如：当调用 `WinAPIs` 函数时会触发 `NtAllocateVirtualMemory` 系统调用。然后，此 `syscall` 将用户在上一个函数调用中提供的参数移动到 Windows内核，执行请求的操作并将结果返回给程序。

所有系统调用都会返回一个指示代码的**NTSTATUS 值**,如果系统调用成功执行操作，则返回（零）`STATUS_SUCCESS`。

参考链接：https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55

大多数系统调用都没有在 Microsoft 中记录，因此系统调用模块将参考下面显示的文档：

* Undocumented NTinternals：http://undocumented.ntinternals.net/
* ReactOS's NTDLL Reference：https://doxygen.reactos.org/dir\_a7ad942ac829d916497d820c4a26c555.html

## 2.1 NTDLL 和系统调用

大多数系统调用都是从 `ntdll.dll` DLL导出的。

## 2.2 Zw 与 Nt 系统调用

有两种类型的系统调用，一种以 **开头Nt**，另一种以 **开头Zw**。

* NT 系统调用是用户模式程序的主要接口，这些是大多数 Windows 程序通常使用的系统调用。
* Zw 系统调用是操作系统的低级内核模式接口，它们通常由设备驱动程序和其他需要直接访问操作系统功能的内核模式代码使用。

总而言之，Zw 系统调用在设备驱动程序开发中用于内核模式，而Nt 系统调用则从用户模式程序执行。

虽然可以从用户模式程序中使用两者，但仍然可以实现相同的结果。这可以在下图中注意到，其中同一系统调用的Zw和Nt版本共享相同的函数地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6QPtm1mVFsVmLEvWictJvHiarGnET4NXYMrRWG9eQCsEvoZvUxwDpd4Xg/640?wx_fmt=png&from=appmsg)

## 2.3 Syscall 结构

系统调用结构通常是相同的，看起来像下面显示的代码片段。

```
mov r10, rcx
mov eax, SSN
syscall
```

例如，`NtAllocateVirtualMemory` 在64位系统上如下所示:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6ibkGFfF4g2t4vbUx2AaribJMV1wXj0QtcJibW3tfwLWvJ2svcQudslaEA/640?wx_fmt=png&from=appmsg)

如下 `NtProtectVirtualMemory` 所示:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6umCXCaLMOy48I4ItGsfE6uM5DAic8DlGvTVxWngpJ5TfkkwNbxMHtsg/640?wx_fmt=png&from=appmsg)

## 2.4 NtAPI调用说明

**需要注意，并非所有 `NtAPI` 都是系统调用！**

需要注意的是，虽然某些 `NtAPI` 返回 `NTSTATUS`，但它们不一定是系统调用。

这些 `NtAPI` 可能是 `WinAPI` 或系统调用使用的低级函数。某些 `NtAPI` 不属于系统调用的原因，是它们不符合系统调用的结构。

例如没有系统调用编号或 `mov r10`, `rcx` 开头缺少通常的指令。下面显示了非系统调用的 NtAPI 的示例：

* `LdrLoadDll` - `WinAPI` 使用它 `LoadLibrary` 来将图像加载到调用进程。
* `SystemFunction032` 并且 `SystemFunction033` 这些 `NtAPI` 是之前引入的，并执行 `RC4` 加密/解密操作。
* `RtlCreateProcessParametersEx` - `WinAPI` 使用它 `CreateProcess` 来创建进程的参数。

##### 加载动态链接库

`LdrLoadDll` 的指令如下所示。请注意，它不遵循典型的系统调用结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6R95ssxuQj6yjJFZr5EWXjEnwVfbKAYlmaXm2WLOficBSSaDYibueiaUXg/640?wx_fmt=png&from=appmsg)

## 2.5 绕过用户空间系统调用钩子

直接使用系统调用是绕过用户空间钩子的一种方法。例如，在为有效载荷分配内存时使用 `NtAllocateVirtualMemory` 而不是 `WinAPI`：

* 使用直接系统调用
* 使用间接系统调用
* 解钩（脱钩）

### 3# 直接和间接系统调用

## 3.1 直接系统调用

通过获取用汇编语言编写的 `syscall` 函数版本，并直接从汇编文件中调用该精心设计的
 `syscall`，可以实现对用户空间 `syscall` 挂钩的规避。

难点在于确定 `syscall` 服务编号(SSN)，因为该编号因系统而异。为了克服这个问题，`SSN` 可以硬编码在汇编文件中，也可以在运行时动态计算。

以下 `.asm` 文件介绍了汇编文件中精心设计的 `syscall` 示例。

不同于本课程中之前所做的 `NtAllocateVirtualMemory` 使用 `GetProcAddress` 和进行调用 `GetModuleHandle`，下面的汇编函数可用于获得相同的结果。这样就无需 `NtAllocateVirtualMemory` 从安装钩子的 `NTDLL` 地址空间内进行调用，从而避免了钩子。

```
NtAllocateVirtualMemory PROC
    mov r10, rcx
    mov eax, (ssn of NtAllocateVirtualMemory)
    syscall
    ret
NtAllocateVirtualMemory ENDP

NtProtectVirtualMemory PROC
    mov r10, rcx
    mov eax, (ssn of NtProtectVirtualMemory)
    syscall
    ret
NtProtectVirtualMemory ENDP

// other syscalls ...
```

此方法被SysWhispers和HellsGate等工具所采用，这两个工具将在后续模块中讨论:

* SysWhispers:https://github.com/jthuraisamy/SysWhispers
* HellsGate:https://github.com/am0nsec/HellsGate

## 3.2 间接系统调用

间接系统调用的实现方式与直接系统调用类似，后者必须先手动编写汇编文件。

两者的区别在于，汇编 `syscall` 函数中没有指令，而是直接跳转到该指令。下图显示了一个直观的表示:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg6P4txiaFZW7K9LRccukqsQ9QNfkTxWlwFeYGlu4aN5O9L12icdf34yWrw/640?wx_fmt=png&from=appmsg)

`NtAllocateVirtualMemory` 和的汇编函数 `NtProtectVirtualMemory` 如下所示：

```
NtAllocateVirtualMemory PROC
    mov r10, rcx
    mov eax, (ssn of NtAllocateVirtualMemory)
    jmp (address of a syscall instruction)
    ret
NtAllocateVirtualMemory ENDP

NtProtectVirtualMemory PROC
    mov r10, rcx
    mov eax, (ssn of NtProtectVirtualMemory)
    jmp (address of a syscall instruction)
    ret
NtProtectVirtualMemory ENDP

// other syscalls ...
```

##### 间接系统调用的好处

执行间接系统调用而非直接系统调用的好处是：安全解决方案会查找从 `NTDLL` 地址空间之外调用的系统调用，并将其视为可疑系统调用。

使用间接系统调用时，系统调用指令会从 `NTDLL` 的地址空间执行，就像正常的系统调用一样。

因此，与直接系统调用相比，间接系统调用更容易躲过安全解决方案的检查。

## 3.3 解钩（脱钩）

解除挂钩是另一种逃避挂钩的方法，即将加载到内存中的挂钩 `NTDLL` 库替换为未挂钩的版本。

可以从多个地方获取未挂钩的版本，但常用方法之一是直接从磁盘加载。这样做将删除放置在 NTDLL 库内的所有挂钩。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fiajytAx7Ibcibu0JQgxKv6sNsic1a1kibg60CKdI1coDNe0XHjthcSTu2ZK9eRauv39tqF6YnPf35WDXLEibdnia01g/640?wx_fmt=png&from=appmsg)

### 4# 优缺点总结和利用代码

## 4.1 Syscall的优点

优势就笔者个人的经验来说，使用某特别的方式间接调用 `nt`函数，杀软没法直接或者快速查询你的函数使用。

但这里我们其实不能说你使用的所有 `nt` 函数或者操作行为就是安全的，比如注入这种在 `loader` 中我个人是不太喜欢的使用的，行为过于明显。

## 4.2 Syscall的缺点

劣势也是非常的明显，在不 `unhook r3` 层，你的 `nt` 函数使用依旧是受到杀软监管的，当然让笔者认为最大的劣势还是在于调用链的不够完整。

这个所谓的调用链不够完整是什么意思，打个比方，我们在使用 `VirtualAlloc` 函数的时候，它的调用链是从 `kernel32` 到 `kernelbase` 最后到 `ntdll`，最后使用 `NtAllocateVirtualMemory`，简而言之就是加载的底层函数是 `NtAllocateVirtualMemory`。

如果我们使用市面上大部分的间接调用技术我们的调用将会直接的跳过 `kernel32` 和 `kernelbase`，直接走到 `ntdll` 当中。这就会让杀软认为你的函数调用链存在差异，当然这种调用链的缺失并不是所有杀软的都会特别在意或者成为立即查杀你的原因，但为了能更长期的稳定运行，我们或许可以尝试伪造一个完整的调用链，接下来我们会实现 `unhook` 以及尝试构造一个伪链来帮我们处理 `syscall`。

## 4.3 原理讲解

我们这里暂不深入讨论内存存根的问题，从 `\KnwonDlls\` 目录 `unhook` 并不是绕过 `r3 hook` 的新方法。但是我们会尝试避免在执行此操作时分配 `RWX` 内存。

例如其中需要 `RWX` 权限来替换挂钩模块的文本部分，同时允许执行这些文本部分中的函数，我们将先暂停正在运行的线程，试图阻止从目标文本部分中调用任何函数，从而无需在 `unhook` 之前将它们设置为 `RWX` ，从而只需要 `RW` 权限。

但是，这种方法产生了另一个问题；在 `unhook` `NtProtectVirtualMemory` 系统调用和其他系统调用使用 `ntdll` 模块内的系统调用指令作为间接系统调用方法，`unhook` 的模块将被标记为 `RW` 权限，因此无法执行间接系统调用。

因为我们要跳转到的系统调用指令现在无法执行，所以我们必须跳转到另一个可执行位置，那么我们可以尝试在 `system32` 下面寻找一个可作为跳板的dll来实现这个，这里我们选择 `win32u.dll`/`win32u.dll`存在一些最终同样使用 `nt`函数的基础函数，基础函数你可理解为类似于 `VirtualAlloc` 这样的函数。当我们完成一些列的操作之后，我们将恢复暂停的线程，并实现我们的目的 `uhook` 加间接调用。

## 4.4 利用代码细节

汇编代码如下：

```
.data
    dwSyscallNumber        DWORD   0h          ; the SSn
    qSyscallInsAddress    QWORD   0h          ; the address of a "syscall; ret;" instruction

.code

    public SetConfig
SetConfig proc
    mov dwSyscallNumber, ecx
    mov qSyscallInsAddress, rdx
    ret
SetConfig endp

    public HellHall
HellHall proc
    mov r10, rcx
    mov eax, dwSyscallNumber
    jmp qword ptr [qSyscallInsAddress]
    ret
HellHall endp

end
```

第一步，加载 `shell32.dll`，`SHGetFolderPathW` 会强制加载 `win32u.dll`，无需我们直接加载：

```
HRESULT AddWin32uToIat()
{
    WCHAR szPath[MAX_PATH] = { 0 };
    return SHGetFolderPathW(NULL, CSIDL_MYVIDEO, NULL, NULL, szPath);
}
```

第二步，初始化我们的 `syscall` 方法并通过 `peb` 找到 `ntdll`，并检查是否被`hook`：

```
BOOL InitilizeNtdllConfig() {
    //  CHECK
    if (NtdllSt.pdwArrayOfFunctions != NULL && NtdllSt.pdwArrayOfNames != NULL && NtdllSt.pwArrayOfOrdinals != NULL)
        return TRUE;
    PPEB                    pPeb = NULL;
    PLDR_DATA_TABLE_ENTRY   pDte = NULL;
    PBYTE                   uNtdll = NULL;

    RtlSecureZeroMemory(&NtdllSt, sizeof(NTDLL));

    //  PEB
    pPeb = (PPEB)__re...