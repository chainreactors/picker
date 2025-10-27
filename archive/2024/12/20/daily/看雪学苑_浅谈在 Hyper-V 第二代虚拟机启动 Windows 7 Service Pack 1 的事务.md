---
title: 浅谈在 Hyper-V 第二代虚拟机启动 Windows 7 Service Pack 1 的事务
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587465&idx=1&sn=8fe03d2e09b694ac803148f7a2e7b779&chksm=b18c21c386fba8d505936823c9529af5f8f735b616ded9fdbd8b60b04d0aa0e2fa31e284a407&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-20
fetch_date: 2025-10-06T19:38:52.894062
---

# 浅谈在 Hyper-V 第二代虚拟机启动 Windows 7 Service Pack 1 的事务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnK64s6ynCyx5WwduY9qSibiaa0u5mSpm87vsvNy0icDz8T1vpXCDKgXrP1spKy3gTEeqwqXMINibSKQ/0?wx_fmt=jpeg)

# 浅谈在 Hyper-V 第二代虚拟机启动 Windows 7 Service Pack 1 的事务

Mouri\_Naruto

看雪学苑

作为一个热衷于尽可能使用像 C/C++ 这样的高级语言编写裸机应用的人，我非常喜欢 Hyper-V 第二代虚拟机的设计，因为这是经过了时间考验的流行的半虚拟化平台之一且看起来这家伙拥有目前最激进的半虚拟化设计:

◆无 CSM 支持，仅提供 64 位 UEFI Class 3 固件

◆无仿真设备，仅提供基于 VMBus 的设备

◆无软驱控制器、DMA 控制器、PCI 总线、传统可编程中断控制器 (PIC)、传统可编程间隔定时器 (PIT) 和超级 I/O 设备这样的传统 x86 设备，需要客户机操作系统明确适配

这样的设计对于我来说是极好的，我只需要编写仅支持 Hyper-V 第二代虚拟机的 UEFI 应用程序作为原型就足够我向他人展示我的一些想法了。这可以帮助我避免适配需要编写大量汇编代码的特定硬件。同时，我喜欢这样的轻量级设计 (笑)

注：Windows 自带的 Hyper-V 客户端对我来说很不好用，这使得我在是否选择 Hyper-V 作为我的裸机应用原型开发平台而陷入了犹豫。直到有一天Ben (Bingxing) Wang告诉我你可以使用当时还算新鲜出炉的 Hyper-V Host Compute System API 去实现一个第三方的 Hyper-V 客户端，尤其是这家伙的无状态设计会很合你的胃口，并且你可以通过 ILSpy 去学习如何使用这家伙。我用了数个月写了一个这样的家伙并且开源到了 GitHub。如果一些朋友需要使用我编写的基于 Hyper-V Host Compute System API 的第三方客户端，可以参考NanaBox。我希望该项目能帮助到和我有类似感受的朋友们。

以 Hyper-V 第二代虚拟机的设计，支持在 Hyper-V 第二代虚拟机启动的最低版本的 Windows 操作系统是 64 位的 Windows 8 和 Windows Server 2012。并且微软在Generation 2 FAQ指出:

> Q: Why are 64-bit versions of Windows Server 2008 R2 and Windows 7 not supported as generation 2 guest operating systems?

> A: Although Windows Server 2008 R2 and Windows 7 support UEFI, they depend on a programmable interrupt controller (PIC), which is not present in generation 2 virtual machine hardware.

翻译一下中文就是：

> Q: 为什么 64 位的 Windows Server 2008 R2 和 Windows 7 无法在 Hyper-V 第二代虚拟机启动？

> A: 虽然 Windows Server 2008 R2 和 Windows 7 支持 UEFI，但它们需要依赖 Hyper-V 第二代虚拟机上不存在的传统可编程中断控制器 (PIC)。

但是这样的理由并不足以说服我。我大约在半年前开始做一些实验去了解其真正的缘由。最终，我意外地在 Hyper-V 第二代虚拟机上成功启动了 Windows 7 Service Pack 1。在下面的章节中，我将分享我是如何做到的。

警告：我没有编写 Windows 内核驱动程序的经验，因为我买不起 Windows 驱动程序需要的签名证书。也许我在本文中提到的方法过于狂野，希望大家见谅。

## 基本常识

在开始之前，我们需要了解一些基本常识：

### 最低支持 Hyper-V 第二代虚拟机的 Windows 客户机版本

首先，我们需要支持实际上支持 Hyper-V 第二代虚拟机的最低的 Windows 客户机版本。这能帮助我们了解微软那群人是如何进行适配的。

这件事其实非常简单，毕竟我们只需要测试并找出哪个是支持在 Hyper-V 第二代虚拟机上启动的最老 Windows 版本。

众所周知，64 位 Windows 8 和 Windows Server 2012 是支持在 Hyper-V 第二代虚拟机上启动的最老版本。于是我们只需要测试Windows 8 - BetaWiki和Windows Server 2012 - BetaWiki中提到的 Windows 版本。

我们可以把这些 Windows 版本分类成以下类别：

| 级别 | 行为 |
| --- | --- |
| 级别 0 | 启动失败，内核死锁 |
| 级别 1 | 启动失败，ACPI 报错 |
| 级别 2 | 需要替换 bootmgr 才能启动 |
| 级别 3 | 无需魔改即可启动 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnK64s6ynCyx5WwduY9qSibFVnC7uhHVbfM6xmHZcSmibWPgSYmFTc9ibHYia7ickQ5r0ddeb6rXBfzBQ/640?wx_fmt=other&from=appmsg)

在目前来看，我发现等级 3 的最小 Windows 版本是 Build 7990 (fbl\_core1\_hyp\_dev)、Build 8027 (fbl\_fun\_perf) 或者 Build 8028 (winmain)。我发现的等级 2 的最小 Windows 版本是 Build 8002 (fbl\_grfx\_dev1)。

### Hyper-V 客户机接口定义

为了适配 Hyper-V 第二代虚拟机，我们需要了解 Hyper-V 客户机接口定义。我已经将相关信息整理成开源项目Mile.HyperV并且其提供了我从哪里获取相关定义的参考资料文档。

### ReactOS 源代码

由于 Windows 不开源，于是我们需要从 ReactOS 中学习关于 hal 和 ntoskrnl 的事务。即使 ReactOS 的 x64 hal 实现哪怕对于学习来说都非常原始。

但是为了感谢该项目帮助了我学习一些基本常识，我也尝试为 ReactOS 添加了 Hyper-V 第二代虚拟机的支持。但由于 ReactOS 的实现过分原始且缺少一大堆内容，即使使用 ReactOS Longhorn 实验性分支，目前仅能亮机且没有任何的 VMBus 设备支持。当然，The\_DarkFire和Timo Kreuzer在这里帮了我不少。

对于一些方便阅读 ReactOS 源代码的朋友，可以去https://github.com/MouriNaruto/reactos/tree/remilia-hyperv-main-longhorn了解我的魔改分支的内部实现。

### 适合进行适配的 Windows 版本

由于 Hyper-V 第二代虚拟机的虚拟键盘是一个 VMBus 设备，为了体面的用户体验，我们需要使用 6.2.9200.16385 及之后版本的 Hyper-V 集成服务。于是 6.2.9200.16385 版本的 Hyper-V 集成服务的最低要求是我们选择能够进行额外适配的 Windows 版本的基准线。

◆64 位 Windows 7 RTM 或 Service Pack 1

◆Windows Server 2008 R2 RTM 或 Service Pack 1

◆64 位 Windows Vista Service Pack 2

◆64 位 Windows Server 2008 Service Pack 2

◆Windows XP Professional x64 Edition Service Pack 2

◆Windows Server 2003 (x64) Service Pack 2

## 开始狂野之旅

让我们在了解一些基本常识之后开始我们的狂野之旅吧:

### 前置条件

◆使用 Hyper-V 第一代虚拟机安装你希望适配 Hyper-V 第二代虚拟机的 Windows 版本，但是你需要准备一个 100MiB 的 FAT32 格式的分区作为 EFI 系统分区 (ESP)

◆安装 Hyper-V 集成服务 6.2.9200.16385 或更高版本

◆WinDbg 对于调试启动过程非常必要

◆类似 IDA Pro 的工具用于分析和修改二进制

◆类似 PE Tools 这样的工具对修改后的文件重新计算校验值

◆类似 Microsoft Copilot 这样的服务也许可以帮你生成用于修改二进制的机器码 (笑)

### 创建 UEFI 启动所需的启动文件

当我们完成了前置条件之后，我们需要挂载虚拟机的虚拟磁盘文件到你的宿主机用于创建UEFI 启动所需的启动文件。

假定你挂载后的 Windows 分区为 "G:" 和 EFI 系统分区为 "F:"。

首先我们需要创建 UEFI 启动所需的启动文件:

```
bcdboot G:\Windows /s F: /f UEFI
```

然后我们对 Windows 启动管理器启用一些调试设置:

```
bcdedit /store F:\EFI\Microsoft\Boot\BCD /bootdebug {default} on
bcdedit /store F:\EFI\Microsoft\Boot\BCD /debug {default} on
bcdedit /store F:\EFI\Microsoft\Boot\BCD /set {default} sos on
bcdedit /store F:\EFI\Microsoft\Boot\BCD /dbgsettings SERIAL DEBUGPORT:1 BAUDRATE:115200 /start ACTIVE
```

我同时建议你将启动管理器的超时设置为 30 秒:

```
bcdedit /store F:\EFI\Microsoft\Boot\BCD /timeout 30
```

### 修复蓝屏实现以方便我们获取错误信息

如果你这时启动你的虚拟机，你会发现你的 WinDbg 命令窗口中在提示分离 Windows 启动调试器后没有任何输出。并且你会发现虚拟机实例进程的 CPU 使用率很高。有些人会知道这是虚拟机内运行的操作系统内核陷入了死循环。

这里是一个使用 64 位 Windows Vista Service Pack 2 作为示例的截图:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EnK64s6ynCyx5WwduY9qSibYmU9xUS0QZaiaoulErqg16BadKkFpc1jebKYotpalndptLcSXfBjyibw/640?wx_fmt=other&from=appmsg)

其实我也是偶然发现是蓝屏导致的。我当时死马当活马医，尝试以添加 0xCC (int 3 指令的操作码) 以调试导致死锁的原因，我发现当我将该操作码添加到 ntoskrnl.exe 的 KeBugCheckEx 函数的开头时，虚拟机会发生三重故障并自动重启。

所以，修复这个问题是很容易的。我们可以将 BugCheck 错误消息报告给 Hyper-V，然后我们可以从 Windows 事件查看器中获取错误消息。

根据 Hyper-V 的 TLFS 规范提到的客户机崩溃报告相关接口，我们可以将以下 C 代码作为 KeBugCheckEx 函数的实现:

```
DECLSPEC_NORETURN void WINAPI KeBugCheckEx(
    ULONG BugCheckCode,
    ULONG_PTR BugCheckParameter1,
    ULONG_PTR BugCheckParameter2,
    ULONG_PTR BugCheckParameter3,
    ULONG_PTR BugCheckParameter4)
{
    // HV_X64_MSR_CRASH_P0
    __writemsr(0x40000100, BugCheckCode);
    // HV_X64_MSR_CRASH_P1
    __writemsr(0x40000101, BugCheckParameter1);
    // HV_X64_MSR_CRASH_P2
    __writemsr(0x40000102, BugCheckParameter2);
    // HV_X64_MSR_CRASH_P3
    __writemsr(0x40000103, BugCheckParameter3);
    // HV_X64_MSR_CRASH_P4
    __writemsr(0x40000104, BugCheckParameter4);
    // HV_X64_MSR_CRASH_CTL with only setting CrashNotify to 1
    __writemsr(0x40000105, 0x8000000000000000);
    _disable();
    __halt();
    return;
}
```

这是上面 C 代码的汇编实现:

```
mov r10, rdx
mov eax, ecx
mov edx, ecx
mov ecx, 40000100h
shr rdx, 20h
wrmsr

mov rdx, r10
mov rax, r10
shr rdx, 20h
mov ecx, 40000101h
wrmsr

mov rdx, r8
mov rax, r8
shr rdx, 20h
mov ecx, 40000102h
wrmsr

mov rdx, r9
mov rax, r9
shr rdx, 20h
mov ecx, 40000103h
wrmsr

mov rdx, [rsp+arg_20]
mov ecx, 40000104h
mov rax, rdx
shr rdx, 20h
wrmsr

xor eax, eax
mov edx, 80000000h
mov ecx, 40000105h
wrmsr

cli
hlt

retn 0
```

使用一些工具将上面的汇编转换为机器码:

```
49 89 D2
89 C8
89 CA
B9 00 01 00 40
48 C1 EA 20
0F 30

4C 89 D2
4C 89 D0
48 C1 EA 20
B9 01 01 00 40
0F 30

4C 89 C2
4C 89 C0
48 C1 EA 20
B9 02 01 00 40
0F 30

4C 89 CA
4C 89 C8
48 C1 EA 20
B9 03 01 00 40
0F 30

48 8B 54 24 28
B9 04 01 00 40
48 89 D0
48 C1 EA 20
0F 30

31 C0
BA 00 00 00 80
B9 05 01 00 40
0F 30

FA
F4

C2 00 00
```

当我们使用类似 IDA Pro 这样的工具将 KeBugCheckEx 函数在 ntoskrnl.exe 中的实现替换为上述机器码后，使用类似 PE Tools 这样的工具重新计算 ntoskrnl.exe 的校验值，然后替换原始的 ntoskrnl.exe。我们可以从 Windows 事件查看器中获取错误消息。

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Hyper-V-Worker" Guid="{51ddfa29-d5c8-4803-be4b-2ecb715570fe}" />
    <EventID>18590</EventID>
    <Version>0</Version>
    <Level>1</Level>
    <Task>0</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8000000000000000</Keywords>
    <TimeCreated SystemTime="2024-12-09T11:31:23.2356205Z" />
    <EventRecordID>35726</EventRecordID>
    <Correlation />
    <Execution ProcessID="1268" ThreadID="3476" />
    <Channel>Microsoft-Windows-Hyper-V-Worker-Admin</Channel>
    <Computer>DESKTOP-OLUNT6J</Computer>
    <Security UserID="S-1-5-83-1-3655396106-1351506743-3915871121-3476744365" />
  </System>
  <UserData>
    <VmlEventLog xmlns="http://www.microsoft.com/Windows/Virtualization/Events">
      <VmName>Virtual Machine</VmName>
      <VmId>D9E0EB0A-5B37-508E-9173-67E9ADE83ACF</VmId>
      <VmErrorCode0>0x79</VmErrorCode0>
      <VmErrorCode1>0x6</VmErrorCode1>
      <VmErrorCode2>0x0</VmErrorCode2>
      <VmErrorCode3>0x0</VmErrorCode3>
      <VmErrorCode4>0x0</VmErrorCode4>
      <VmErrorMessage>
      </VmErrorMessage>
    </VmlEventLog>
  </UserData>...