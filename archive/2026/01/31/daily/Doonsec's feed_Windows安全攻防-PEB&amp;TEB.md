---
title: Windows安全攻防-PEB&amp;TEB
url: https://mp.weixin.qq.com/s/RTyafWl13djCI5ua6LFQ6w
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:21:58.773840
---

# Windows安全攻防-PEB&amp;TEB

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9bOzaictich6TDx3pgUJHaiajicrr5DWwWP0BhDs7zM1qQ84g38YibaJbIj81lCYe30mOsOe7NhAMF0feIc63lXcTzQ/0?wx_fmt=jpeg)

# Windows安全攻防-PEB&TEB

原创

R0x7e
R0x7e

剑外思归客

![]()

在小说阅读器中沉浸阅读

# 基础介绍

在 Windows 操作系统中，每个运行的程序（即进程）和其中的执行单元（即线程）都由内核对象来表示，但同时在用户空间也存在对应的数据结构，即 PEB 和 TEB，它们为用户模式代码提供了一种快速访问进程和线程信息的方式。

* **TEB (Thread Environment Block)**: 线程环境块，也称为线程信息块（Thread Information Block, TIB）。顾名思义，它存储了与单个线程相关的特定信息。**每个线程都拥有一个独立的 TEB**。其内容包括线程ID (TID)、线程的栈基址和栈顶限制、指向线程局部存储 (Thread Local Storage, TLS) 的指针，以及一个指向其所属进程 PEB 的关键指针。
* **PEB (Process Environment Block)**: 进程环境块。与 TEB 不同，一个进程只有一个 PEB，它存储了该进程范围内的全局信息。这些信息对于进程的整个生命周期都至关重要，例如进程加载了哪些动态链接库 (DLL)、完整的命令行参数、可执行文件的内存基址（`Image Base Address`）、进程堆信息以及一些用于调试和系统兼容性的标志位。**核心关系**：TEB 是通往 PEB 的桥梁。在用户模式下，代码首先访问当前线程的 TEB，然后通过 TEB 中的一个特定字段（`ProcessEnvironmentBlock`）找到其所属进程的 PEB 地址。这种“线程→进程”的链式访问结构，为任何在线程上下文中运行的代码提供了一条稳定、高效的路径来获取关于自身进程的丰富信息。

# 定义和结构

## TEB 线程环境块

TEB 是一个用于存储单个线程状态的结构。其定义在 Windows SDK 的 `winternl.h` 中，包含大量字段来描述线程的各种属性。由于版本更新，TEB 的结构可能有所变化，微软建议不要直接访问 TEB 结构的字段，除非使用官方提供的 API 。例如，`TlsSlots` 和 `TlsExpansionSlots` 字段需要通过 `TlsGetValue` 等函数访问，`ReservedForOle` 字段需要通过 `CoGetContextToken` 访问 。 TEB 的结构非常复杂，包含许多成员。根据微软官方头文件和 Wine 项目的实现，TEB 通常以 `_TEB` 或 `NT_TIB` 为前缀定义。下面是一个简化的 TEB 结构定义示例：

```
typedef struct _TEB {
    NT_TIB NtTib;                         // 包含栈信息、SEH 链表等关键信息
    PVOID EnvironmentPointer;
    CLIENT_ID ClientId;                   // 包含 UniqueProcess (PID) 和 UniqueThread (TID)
    PVOID ActiveRpcHandle;
    PVOID ThreadLocalStoragePointer;      // 指向线程本地存储 (TLS) 数组
    struct _PEB *ProcessEnvironmentBlock; // 指向所属进程的 PEB
    ULONG LastErrorValue;                 // GetLastError() 返回的值就存在这里
    ULONG CountOfOwnedCriticalSections;
    PVOID CsrClientThread;
    PVOID Win32ThreadInfo;                // 指向内核层的 W32THREAD 结构
    // ... 后面还有数百个成员，包括语言 ID、混淆种子等
} TEB, *PTEB;
```

### NT\_TIB 子结构

这是 TEB 的头。它包含了栈的基址 (`StackBase`) 和限制 (`StackLimit`)。最著名的是 `ExceptionList`（在 x86 下），它是 SEH（结构化异常处理）链表的头，其结构定义如下：

```
typedef struct _NT_TIB {
    struct _EXCEPTION_REGISTRATION_RECORD *ExceptionList;  // SEH 链头
    PVOID StackBase;                // 堆栈基址
    PVOID StackLimit;               // 堆栈限制
    PVOID SubSystemTib;
    union {
        PVOID FiberData;
        ULONG Version;
    };
    PVOID ArbitraryUserPointer;
    struct _NT_TIB *Self;           // 指向自身的指针（FS:[0x18]）
} NT_TIB;
```

### ProcessEnvironmentBlock

**指向PEB的指针**。这是从线程信息通往进程信息的唯一官方入口，是所有PEB相关操作的起点，在`x86`环境下偏移为`0x30`，`x64`环境下偏移为`0x60`

### ClientId

**`ClientId`** 是一个 `_CLIENT_ID` 结构体，包含了两个至关重要的标识符：`UniqueProcess`（即进程ID, PID）和 `UniqueThread`（即线程ID, TID）。这两个ID是线程在整个系统中的唯一坐标，恶意软件可用于识别自身或目标进程，在`x86`环境下偏移为`0x20`，`x64`环境下偏移为`0x40`

### TlsSlots/TlsExpansionSlots

线程局部存储 (TLS) 槽。可被恶意软件用于在线程级别存储数据，或通过操纵TLS槽来绕过某些EDR的钩子检测。在`x86`环境下偏移为`0xE10`，`x64`环境下偏移为`0x1480`

### ExceptionList

指向线程异常处理（SEH）链表的头部。攻击者可以通过覆盖这个链表来劫持异常处理流程，实现代码执行，这是一种经典的漏洞利用和反调试技术。偏移为`0x00`

### LastErrorValue

当调用 `SetLastError` 或 `GetLastError` 时，底层其实就是在读写这个字段。

### ThreadLocalStoragePointer

指向线程本地存储 (TLS) 数组的指针 。每个线程都有一个 TLS 数组，用于存储线程特定的数据。

| 字段名 | x86 偏移量 (FS) | x64 偏移量 (GS) | 描述 |
| --- | --- | --- | --- |
| `ExceptionList` (NT\_TIB) | `0x00` | `0x00` | 指向SEH链表头的指针 (\_EXCEPTION\_REGISTRATION\_RECORD\*) |
| `StackBase` (NT\_TIB) | `0x04` | `0x08` | 线程栈的基地址（高地址） |
| `StackLimit` (NT\_TIB) | `0x08` | `0x10` | 线程栈的上限地址（低地址） |
| `Self` (NT\_TIB) | `0x18` | `0x30` | 指向TEB结构自身的指针 (PTEB) |
| `ClientId.UniqueProcess` | `0x20` | `0x40` | 进程ID (PID) |
| `ClientId.UniqueThread` | `0x24` | `0x48` | 线程ID (TID) |
| `ThreadLocalStoragePointer` | `0x2C` | `0x58` | 指向静态TLS数组的指针 |
| `ProcessEnvironmentBlock` | `0x30` | `0x60` | 指向进程环境块的指针 (PPEB) |
| `LastErrorValue` | `0x34` | `0x68` | 线程的最后错误码 (ULONG) |
| `TlsSlots` | `0xE10` | `0x1480` | 动态TLS插槽数组 (PVOID[64]) |

### 通过`WinDbg`查看TEB信息

在`windbg`中可以通过`dt _teb`命令进行查看结构信息

![](https://mmbiz.qpic.cn/mmbiz_png/9bOzaictich6TDx3pgUJHaiajicrr5DWwWP0gM1o6MJibu5KNhR2glg0XM7Akoa0RFgAh5BaZLGLCgd29icp7VicMAsgg/640?wx_fmt=png&from=appmsg)

通过`!teb`可以查看当前线程的基本信息，如：TEB 地址、栈范围、TLS 等

![](https://mmbiz.qpic.cn/mmbiz_png/9bOzaictich6TDx3pgUJHaiajicrr5DWwWP0pOn7vIeZKwBMuN9jatrJYPaNRRQibDwicStRev6ZQmZicEd0PVfumBqkw/640?wx_fmt=png&from=appmsg)

通过`dt ntdll!_TEB @$teb`可以查看当前线程`TEB`不同字段的内容

![](https://mmbiz.qpic.cn/mmbiz_png/9bOzaictich6TDx3pgUJHaiajicrr5DWwWP08jcK2bpUB9ercRycxkpYSfkXUneuNibUKV2rPy6HQcgtHyLicn7PSKicw/640?wx_fmt=png&from=appmsg)

如果你只想看某一个字段具体的值，可以使用`dt ntdll!_TEB @$teb 字段名`的方式进行查看，如`dt ntdll!_TEB @$teb ProcessEnvironmentBlock`

![](https://mmbiz.qpic.cn/mmbiz_png/9bOzaictich6TDx3pgUJHaiajicrr5DWwWP0GBQo8MUmxg2LFqCcibgiboTtU2tm40mmP73Z2Oc3gia8lgWCiarC3FmLMg/640?wx_fmt=png&from=appmsg)

## PEB 进程环境块

PEB 是连接用户态代码与内核态信息的桥梁，每个进程有且只有一个PEB进程环境块，PEB存储在用户态中，同时也是连接用户态代码与内核态信息的桥梁，一个进程内的所有线程共享同一个 PEB，PEB的结构在不同的windows版本中会有变化，以下是一个简写的`PEB`结构内容：

```
typedef struct _PEB {
    BOOLEAN InheritedAddressSpace;      // 0x000
    BOOLEAN ReadImageFileExecOptions;   // 0x001
    BOOLEAN BeingDebugged;              // 0x002 标志进程是否正在被调试
    union {
        BOOLEAN BitField;               // 0x003
        struct {
            BYTE ImageUsesLargePages : 1;
            BYTE IsProtectedProcess : 1;
            // ... 其他位标志
        };
    };
    HANDLE Mutant;                      // 0x004 (x86) / 0x008 (x64)
    PVOID ImageBaseAddress;             // 程序的加载基地址
    PPEB_LDR_DATA Ldr;                  // 指向加载器数据，包含已加载模块列表 (DLLs)
    PRTL_USER_PROCESS_PARAMETERS ProcessParameters; // 包含命令行、路径等信息
    PVOID SubSystemData;
    PVOID ProcessHeap;                  // 进程默认堆地址
    PRTL_CRITICAL_SECTION FastPebLock;
    // ... 后面还有关于环境变量、会话 ID、代码页等数百个成员
} PEB, *PPEB;
```

本文列举一些较为关键的`PEB`字段

### `BeingDebugged` (BYTE)

当一个进程被调试器附加时，Windows内核会自动将此位置为`1`。因此，检查该字段是最基础、最直接的反调试技术之一。程序可以通过直接读取该内存地址来判断自身是否处于被调试状态，**IsDebuggerPresent()** 这个 API 在底层其实只是简单地读了一下这个字节。

### `ImageBaseAddress`(PVOID)

指向进程主可执行文件（.exe）被加载到内存中的基地址。这个地址是进行内存操作和地址重定位计算的起点。

### `Ldr`(PPEB\_LDR\_DATA)

这是一个指向 `PEB_LDR_DATA` 结构的指针。它维护了三个双向链表，**记录了进程加载的所有模块（`.exe` 和 `.dll`）**。`PEB_LDR_DATA`结构体定义如下：

```
typedef struct _PEB_LDR_DATA {
    ULONG Length;                          // 结构体长度
    BOOLEAN Initialized;                   // 是否已初始化
    HANDLE SsHandle;
    LIST_ENTRY InLoadOrderModuleList;      // DLL 被加载到进程中的先后顺序
    LIST_ENTRY InMemoryOrderModuleList;    // DLL 在内存地址空间中的排列顺序
    LIST_ENTRY InInitializationOrderModuleList; // DLL 初始化函数（DllMain）被调用的顺序
    PVOID EntryInProgress;
    BOOLEAN ShutdownInProgress;
    HANDLE ShutdownThreadId;
} PEB_LDR_DATA, *PPEB_LDR_DATA;
```

其中的三个**双向链表**（`InLoadOrderModuleList`,`InMemoryOrderModuleList`,`InInitializationOrderModuleList`）都指向同一种数据结构`LDR_DATA_TABLE_ENTRY`，之所以存在三个链表，是为了提供不同的检索视角，`LDR_DATA_TABLE_ENTRY`的结构定义如下：

```
typedef struct _LDR_DATA_TABLE_ENTRY {
    LIST_ENTRY InLoadOrderLinks;           // 对应加载顺序链表的指针
    LIST_ENTRY InMemoryOrderLinks;         // 对应内存顺序链表的指针
    LIST_ENTRY InInitializationOrderLinks; // 对应初始化顺序链表的指针
    PVOID DllBase;                         // 关键：DLL 在内存中的基地址
    PVOID EntryPoint;                      // DLL 的入口点 (DllMain)
    ULONG SizeOfImage;                     // DLL 映射在内存中的大小
    UNICODE_STRING FullDllName;            // DLL 的全路径（带路径）
    UNICODE_STRING BaseDllName;            // DLL 的简称（如 kernel32.dll）
    ULONG Flags;
    USHORT LoadCount;
    // ... 后面还有版本信息、时间戳等
} LDR_DATA_TABLE_ENTRY, *PLDR_DATA_TABLE_ENTRY;
```

每个加载的 DLL 都会对应一个这样的结构。 在网络安全攻防中，`shellcode`和免杀技术通常用到的经典操作：**在不调用任何 Windows API 的情况下，找到 `kernel32.dll` 的基地址**，进而通过遍历其导出表来调用 `GetProcAddress`。这里只单独的提一下逻辑：

* 从 `GS:[0x60]` 获取 PEB。
* 从 PEB 获取 `Ldr` 指针。
* 遍历 `InMemoryOrderModuleList` 链表。
* 比较每个节点的 `BaseDllName`，如果是`kernel32.dll`，则取出 `DllBase`。 在用户态`Rootkit`中也会利用`Ldr`来隐藏自身，Windows 的 API（如 `EnumProcessModules` 或 `Toolhelp32Snapshot`）在枚举模块时，本质上也是在遍历这三个链表。如果你手动修改这三个链表的 `Flink` 和 `Blink` 指针，将自己的 DLL 从链表中抠掉（断链），那么常规的工具就看不见这个 DLL 了，但它依然存在于内存中并可以运行。

### `ProcessParameters`

这个结构是进程启动环境的快照，存储了进程创建时传递的命令行参数、可执行文件路径、环境变量块指针等。其中：

* **CommandLine**：存储了完整的启动命令行字符...