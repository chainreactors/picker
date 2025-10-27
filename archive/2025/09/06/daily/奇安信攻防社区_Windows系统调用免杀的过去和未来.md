---
title: Windows系统调用免杀的过去和未来
url: https://forum.butian.net/share/4527
source: 奇安信攻防社区
date: 2025-09-06
fetch_date: 2025-10-02T19:43:00.105801
---

# Windows系统调用免杀的过去和未来

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Windows系统调用免杀的过去和未来

* [安全工具](https://forum.butian.net/topic/53)

本文将介绍Windows系统调用在免杀对抗中需要解决的问题以及各个免杀的系统调用项目是如何解决这些问题的，通过本文的学习能让大家更加深入地了解Windows系统调用的过程并了解运用系统调用去规避AV/EDR的检测的一些技巧。

前言
==
大家好，我是拖更博主r0leG3n7。本文将介绍Windows系统调用在免杀对抗中需要解决的问题以及各个免杀的系统调用项目是如何解决这些问题的，通过本文的学习能让大家更加深入地了解Windows系统调用的过程并了解运用系统调用去规避AV/EDR的检测的一些技巧。如有任何错误和不足欢迎各位师傅指正，转载请注明文章出处。
注意:下面的大部分内容都只介绍系统调用从用户态准备到进入内核态的过程，并不会详细介绍内核态中的细节以及怎么从内核态回到用户态，因为对于免杀，我们通常只需要处理系统调用从用户态转到内核态转变过程，这个过程是AV/EDR重点监测的过程。
基础知识
====
ntoskrnl.exe
------------
ntoskrnl.exe(NT Operating System Kernel Executable)是Windows 操作系统内核的核心组件。它是 Windows NT 系列操作系统（包括 Windows XP 及之后的版本）的内核执行体，负责管理系统资源、硬件抽象和核心系统服务。
ntoskrnl.exe对系统调用入口的意义:
1、SSDT表管理：维护系统服务描述符表（KeServiceDescriptorTable），存储所有内核 API 地址(如NtOpenprocess)；
2、响应系统调用指令（int 2Eh / sysenter / syscall）。
\*\*syscall stub\*\*
----------------
系统调用存根（syscall stub） 是用户空间程序与操作系统内核之间交互的桥梁，用于触发系统调用（syscall）。它是 Windows NT 系列操作系统（包括 Windows XP 及之后的版本）的内核执行体，负责管理系统资源、硬件抽象和核心系统服务。
系统调用号（System Call Number）是用户态程序通过系统调用进入内核时传递的一个数字，用于索引系统服务调度表（SSDT）中的函数指针。在用户态，每个系统调用在 ntdll.dll 中都有一个对应的存根函数（stub）。这些存根函数的主要工作就是将系统调用号放入特定的寄存器（如 eax 或 rax），然后执行触发系统调用的指令（如 int 0x2E 或 syscall）。因此，可以通过反汇编 ntdll.dll 中对应的存根函数来获取系统调用号，不同的系统版本对应函数的系统调用号是不一样的。
系统调用号（System Call Number）与系统服务号SSN（System Service Number）指的是同一个东西。
\\_KUSER\\_SHARED\\_DATA
---------------------
\\_KUSER\\_SHARED\\_DATA 是 Windows 操作系统内核与用户态程序之间共享数据的关键结构体，位于固定的内存地址，用于高效传递系统信息。
在 User 层和 Kernel 层分别定义了一个 \\_KUSER\\_SHARED\\_DATA 结构区域，用于 User 层和 Kernel 层共享某些数据，它们使用固定的地址值映射， \\_KUSER\\_SHARED\\_DATA 结构区域在 User 和 Kernel 层地址分别为:
User 层地址为：0x7ffe0000
Kernel 层地址为：0xffdf0000
这两个地址映射的物理页是相同的，但在User层是只读的，在Kernel层是可写的
\\_KUSER\\_SHARED\\_DATA结构体如下:
```php
kd> dt \_KUSER\_SHARED\_DATA
ntdll!\_KUSER\_SHARED\_DATA
+0x000 TickCountLowDeprecated : Uint4B
+0x004 TickCountMultiplier : Uint4B
+0x008 InterruptTime : \_KSYSTEM\_TIME
+0x014 SystemTime : \_KSYSTEM\_TIME
+0x020 TimeZoneBias : \_KSYSTEM\_TIME
+0x02c ImageNumberLow : Uint2B
+0x02e ImageNumberHigh : Uint2B
+0x030 NtSystemRoot : [260] Wchar
+0x238 MaxStackTraceDepth : Uint4B
+0x23c CryptoExponent : Uint4B
+0x240 TimeZoneId : Uint4B
+0x244 LargePageMinimum : Uint4B
+0x248 Reserved2 : [7] Uint4B
+0x264 NtProductType : \_NT\_PRODUCT\_TYPE
+0x268 ProductTypeIsValid : UChar
+0x26c NtMajorVersion : Uint4B
+0x270 NtMinorVersion : Uint4B
+0x274 ProcessorFeatures : [64] UChar
+0x2b4 Reserved1 : Uint4B
+0x2b8 Reserved3 : Uint4B
+0x2bc TimeSlip : Uint4B
+0x2c0 AlternativeArchitecture : \_ALTERNATIVE\_ARCHITECTURE\_TYPE
+0x2c4 AltArchitecturePad : [1] Uint4B
+0x2c8 SystemExpirationDate : \_LARGE\_INTEGER
+0x2d0 SuiteMask : Uint4B
+0x2d4 KdDebuggerEnabled : UChar
+0x2d5 NXSupportPolicy : UChar
+0x2d8 ActiveConsoleId : Uint4B
+0x2dc DismountCount : Uint4B
+0x2e0 ComPlusPackage : Uint4B
+0x2e4 LastSystemRITEventTickCount : Uint4B
+0x2e8 NumberOfPhysicalPages : Uint4B
+0x2ec SafeBootMode : UChar
+0x2ed TscQpcData : UChar
+0x2ed TscQpcEnabled : Pos 0, 1 Bit
+0x2ed TscQpcSpareFlag : Pos 1, 1 Bit
+0x2ed TscQpcShift : Pos 2, 6 Bits
+0x2ee TscQpcPad : [2] UChar
+0x2f0 SharedDataFlags : Uint4B
+0x2f0 DbgErrorPortPresent : Pos 0, 1 Bit
+0x2f0 DbgElevationEnabled : Pos 1, 1 Bit
+0x2f0 DbgVirtEnabled : Pos 2, 1 Bit
+0x2f0 DbgInstallerDetectEnabled : Pos 3, 1 Bit
+0x2f0 DbgSystemDllRelocated : Pos 4, 1 Bit
+0x2f0 DbgDynProcessorEnabled : Pos 5, 1 Bit
+0x2f0 DbgSEHValidationEnabled : Pos 6, 1 Bit
+0x2f0 SpareBits : Pos 7, 25 Bits
+0x2f4 DataFlagsPad : [1] Uint4B
+0x2f8 TestRetInstruction : Uint8B
+0x300 SystemCall : Uint4B
+0x304 SystemCallReturn : Uint4B
+0x308 SystemCallPad : [3] Uint8B
+0x320 TickCount : \_KSYSTEM\_TIME
+0x320 TickCountQuad : Uint8B
+0x320 ReservedTickCountOverlay : [3] Uint4B
+0x32c TickCountPad : [1] Uint4B
+0x330 Cookie : Uint4B
+0x334 CookiePad : [1] Uint4B
+0x338 ConsoleSessionForegroundProcessId : Int8B
+0x340 Wow64SharedInformation : [16] Uint4B
+0x380 UserModeGlobalLogger : [16] Uint2B
+0x3a0 ImageFileExecutionOptions : Uint4B
+0x3a4 LangGenerationCount : Uint4B
+0x3a8 Reserved5 : Uint8B
+0x3b0 InterruptTimeBias : Uint8B
+0x3b8 TscQpcBias : Uint8B
+0x3c0 ActiveProcessorCount : Uint4B
+0x3c4 ActiveGroupCount : Uint2B
+0x3c6 Reserved4 : Uint2B
+0x3c8 AitSamplingValue : Uint4B
+0x3cc AppCompatFlag : Uint4B
+0x3d0 SystemDllNativeRelocation : Uint8B
+0x3d8 SystemDllWowRelocation : Uint4B
+0x3dc XStatePad : [1] Uint4B
+0x3e0 XState : \_XSTATE\_CONFIGURATION
```
MSR寄存器
------
MSR(Model Specific Register)模型特定寄存器是x86/x64架构CPU中的一组64位专用寄存器，主要用于配置硬件参数、监控运行状态及支持特定功能。
快速调用依赖MSR寄存器，MSR寄存器保存着内核入口点、内核栈指针等重要信息。
快速调用sysenter用到的MSR寄存器:
1、IA32\\_SYSENTER\\_CS：内核代码段选择；
2、IA32\\_SYSENTER\\_EIP：内核入口点（如 KiFastCallEntry）；
3、IA32\\_SYSENTER\\_ESP：内核栈指针。
快速调用syscall用到的MSR寄存器:
1、IA32\\_LSTAR：64 位内核入口点（如 KiSystemCall64）；
2、IA32\\_STAR：高 32 位指定内核 CS/SS，低 32 位指定用户态返回的 CS/SS。
用户态调用 syscall时，CPU 从 IA32\\_LSTAR 加载 RIP，返回地址存入 RCX。
KiIntSystemCall / KiSystemService
---------------------------------
KiIntSystemCall是用户模式中断门（INT 2E）发起系统调用的函数，CPU 执行 INT 2E 指令触发软中断，通过中断描述符表（IDT）找到对应的中断服务例程（ISR）KiSystemService，KiIntSystemCall执行的是完整的KiSystemService。KiSystemService 是(内核模式)系统调用的统一入口，其关键步骤包括：
1、定位 SSDT 表：通过 KeServiceDescriptorTable（全局变量）获取 SSDT 基地址（ServiceTableBase），附SSDT表结构:
```php
typedef struct \_SYSTEM\_SERVICE\_TABLE {
PVOID ServiceTableBase; // 函数地址数组基址
PVOID ServiceCounterTable;
ULONG NumberOfServices; // 服务数量
PVOID ParamTableBase; // 参数表基址（SSPT）
} SYSTEM\_SERVICE\_TABLE, \*PSYSTEM\_SERVICE\_TABLE;
```
2、索引服务函数：以 EAX 中的服务号为索引，从 ServiceTableBase 指向的数组中取出目标函数地址。
```php
PULONG function\_address = ServiceTableBase[EAX];
```
3、通过 SSPT（System Service Parameter Table） 获取参数大小（ParamTableBase\[EAX\]），将用户栈参数复制到内核栈。
4、构建完整的陷阱帧（\\_KTRAP\\_FRAME），保存线程状态。
KiFastSystemCall / KiFastCallEntry
----------------------------------
KiFastSystemCall是用户模式快速系统调用指令（sysenter）的入口，CPU 执行 sysenter 指令，直接跳转到预设的 MSR（模型特定寄存器）指定的地址（即 KiFastCallEntry）。
内核模式下，KiFastCallEntry的核心操作:
1、将用户栈切换成内核栈；
2、保存关键寄存器，将用户态的 RIP、CS、RFLAGS、RS等 存入内核栈，形成精简陷阱帧(\\_KTRAP\\_FRAME)，保护现场;
3、执行KiSystemService 的核心逻辑，但不是完整的KiSystemService。
这时你可能会问这个这个快速调用的KiFastCallEntry和上面中断门的KiSystemService有什么相同和不同？
两者都会执行上面提到的KiSystemService 的关键步骤；但中断门会将通用寄存器（RAX、RCX、RDX 等）不只是关键的寄存器存入，形成完整的陷阱帧（\\_KTRAP\\_FRAME），而快速调用只保存关键寄存器形成精简的陷阱帧，两者最终会被KiSystemService补全成完整的陷阱帧，只是补全前保存的寄存器的数量不同，所以快速调用比中断门的系统开销更低，所以快速调用更"快"，这个"快"强调的是进入ring 0的快；快速调用的"快"还体现在它不用像中断门那样去查中断描述符表（IDT）才能找到入口，快速调用是直接去MSR寄存器找到入口，再去跳转KiSystemService的关键步骤。
Zw\\*开头的函数和Nt\\*开头的函数
-------------------
在用户模式(ring3)下，二者实现的功能完全相同，且都需要进行参数校验和模式切换，由于调用源自用户模式，所有参数均被严格检查，防止非法内存访问或权限越界。
在内核模式(ring0)下，二者实现的功能完全相同,但有以下区别:
1、调用Zw\\*开头时,函数会将系统服务号SSN传入eax，将传入的函数指针传入edx，将Previous Mode设置为内核模式(Kernel Mode)，然后调用KiSystemService，KiSystemService会根据eax中的服务号，到SSDT表中查找对应的Nt函数地址,但由于Previous Mode是信任的内核模式，所以不会进行如缓冲区溢出等严格的参数检查(可以说在内核模式下，Zw\\*开头的函数是Nt\\*开头函数的代理)。此过程严重依赖SSDT表，所以很容被SSDT Hook。
2、调用Nt\\*开头时,其不会改变当前Previous Mode，而是继承调用者模式，也就是说此时的Previous Mode有可能是用户模式也有可能是内核模式，Nt 函数会执行严格的参数检查。这个过程不依赖SSDT，可以绕过SSDT Hook直接调用服务函数。
Windows异常处理机制
-------------
1、CPU检测到异常；
2、查IDT寻找处理函数；
3、保存现场执行中断函数，触发系统中断进入ring0；
4、（ring0）CommonDispatchException把异常代码、异常发生的地址等信息存入\\_EXCEPTION\\_RECORD结构体,KiDispatchException分发异常信息至\\_Trap\\_Frame结构体,这个过程会判断是否存在调试器，如果存在调试器则发送给调试器处理异常，直至调试器处理异常完毕否则一直处于中断状态；如果不存在调试器，则在判断是否是在ring 0发生的异常，是则交给对应的ring 0异常处理函数(如果是ring 0的的异常且没有函数处理，系统将直接蓝屏)，不是则返回ring 3；
5、返回ring 3后执行ntdll.dll的KiUserExceptionDispa...