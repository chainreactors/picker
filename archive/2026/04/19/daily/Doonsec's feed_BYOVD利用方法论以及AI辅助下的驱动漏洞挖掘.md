---
title: BYOVD利用方法论以及AI辅助下的驱动漏洞挖掘
url: https://mp.weixin.qq.com/s/G8_l-vt7UauiQyyJTAddxQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:59.006096
---

# BYOVD利用方法论以及AI辅助下的驱动漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SxWiaVqD6JsmhHhViap0bcs9ThXeTDPW3iahTc5IQcBoKt8iaAZAcfOz7HyXcvTqt68WZE5eUCe7dnibotzSIicH9T5wibveUFOW8IDopzmCbJOgzs/0?wx_fmt=jpeg)

# BYOVD利用方法论以及AI辅助下的驱动漏洞挖掘

原创

网络保安29
网络保安29

红蓝攻防研究实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 0x01 BYOVD原理

BYOVD 是指滥用具有合法数字签名但存在设计缺陷或已知漏洞的驱动程序，以内核权限执行恶意操作，绕过用户态安全机制的防护。一般是驱动暴露的接口未能对来自用户态的请求进行严格的参数验证导致漏洞，最常见的有：驱动提供了读写任意内核地址的原语、驱动允许用户态程序指定一个内核函数地址并执行、驱动提供物理内存映射能力等。

漏洞利用程序通过 DeviceIoControl 函数，向驱动的设备对象发送精心构造的 IOCTL 请求。由于驱动的IOCTL处理程序存在漏洞，根据不同的驱动暴露的功能，攻击者一般能执行以下一个或多个操作：

1、定位内核对象：利用任意读原语，通过 PsInitialSystemProcess 或遍历 ActiveProcessLinks 链表，定位关键数据结构，如目标进程的 EPROCESS 结构、线程的 ETHREAD 结构。

2、终止进程：调用 ZwTerminateProcess、PsTerminateProcess 等内核函数强制终止进程；或终止进程的所有线程使其自然结束。

3、禁用回调：通过 PsRemoveCreateProcessNotifyRoutine、PsRemoveLoadImageNotifyRoutine 等公开 API，移除安全软件注册的内核回调（需知道回调地址或 Cookie），使其无法监控系统活动。

4、提升权限：替换当前进程的 TOKEN 为 SYSTEM 进程的 TOKEN，或将 TOKEN 中的权限位提升，实现权限提升至 SYSTEM 级别。

......

## 0x02 驱动基础

以下是对驱动中重要数据结构的说明，挺长的，建议简单看一下。不想看的直接到下一章。

### 1、驱动初始化

#### 1.1 DriverEntry

**DriverEntry**是内核驱动程序的入口点，等同于用户模式程序的 main 函数。当驱动被操作系统的I/O管理器加载时，此函数被自动调用。

```
NTSTATUS DriverEntry(    _In_ PDRIVER_OBJECT DriverObject,  // 系统分配的驱动对象指针    _In_ PUNICODE_STRING RegistryPath   // 指向该驱动在注册表中配置项路径的指针);
```

```
在 DriverEntry 中，驱动程序必须完成一系列关键的初始化步骤，其核心任务流程如下：
```

1、I/O管理器加载驱动并调用 DriverEntry

2、初始化派遣函数数组（MajorFunction）

3、创建设备对象（IoCreateDevice）

4、创建符号链接（IoCreateSymbolicLink）

5、注册卸载例程 （DriverUnload）

#### 1.2 DriverObject

**DriverObject** 是内核为驱动创建的一个核心数据结构，驱动通过初始化此对象的各个字段来告知系统其可以做什么。例如 MajorFunction 数组用于处理 I/O 请求，DriverUnload 指针用于指定清理函数。

RegistryPath 通常用于从注册表（如 ...\Services\<DriverName>\Parameters）读取驱动特定的配置参数，实现驱动行为的外部定制。

```
typedef struct _DRIVER_OBJECT {  CSHORT             Type;  CSHORT             Size;  PDEVICE_OBJECT     DeviceObject;  ULONG              Flags;  PVOID              DriverStart;  ULONG              DriverSize;  PVOID              DriverSection;  PDRIVER_EXTENSION  DriverExtension;  UNICODE_STRING     DriverName;  PUNICODE_STRING    HardwareDatabase;  PFAST_IO_DISPATCH  FastIoDispatch;  PDRIVER_INITIALIZE DriverInit;  PDRIVER_STARTIO    DriverStartIo;  PDRIVER_UNLOAD     DriverUnload;  PDRIVER_DISPATCH   MajorFunction[IRP_MJ_MAXIMUM_FUNCTION + 1];} DRIVER_OBJECT, *PDRIVER_OBJECT;
```

```
1.3 MajorFunction
```

DRIVER\_OBJECT->MajorFunction派遣函数数组，DRIVER\_OBJECT 结构中的 MajorFunction 是一个函数指针数组，每个索引对应一个特定的“主功能代码”。

驱动程序不具有主线程，而是由内核可以在特定条件下调用的例程组成。驱动程序需要向 I/O 管理器注册分发例程（在 DriverEntry 中将其实现的处理例程赋值给相应的 MajorFunction 数组索引），来处理来自用户空间或其他驱动程序的请求。当在设备上调用 Windows API 时，驱动程序会通过运行特定例程来响应，每个 API 调用都映射到 MajorFunctions 数组中的特定索引，确保了在调用 API 函数后执行对应的例程。

```
// 注册特定的分发例程 - 为特定IRP类型指定具体的处理函数    DriverObject->MajorFunction[IRP_MJ_READ] = MyDispatchRead;    // 处理ReadFile    DriverObject->MajorFunction[IRP_MJ_WRITE] = MyDispatchWrite; // 处理WriteFile    DriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = MyDispatchDeviceControl; // 处理DeviceIoControl    DriverObject->MajorFunction[IRP_MJ_CREATE] = MyDispatchCreate; // 处理CreateFile    DriverObject->MajorFunction[IRP_MJ_CLOSE] = MyDispatchClose;   // 处理CloseHandle
```

在 MajorFunction 数组中，有一个标识为 IRP\_MJ\_DEVICE\_CONTROL 的专用条目，驱动程序在此位置存储其分发例程的函数指针，当应用程序对设备调用 DeviceIoControl 时会触发该指针，这个例程接收的参数之一是 I/O 控制代码 (IOCTL)。IOCTL 是用户态应用程序和内核态设备驱动之间的桥梁，驱动内部通过解析不同的命令码来执行相应的操作。

DeviceIoControl 是用户态程序与内核驱动通信的核心 API。

```
WINBASEAPI BOOL WINAPI DeviceIoControl(    _In_ HANDLE hDevice,    _In_ DWORD dwIoControlCode, //I/O 控制代码    _In_reads_bytes_opt_(nInBufferSize) LPVOID lpInBuffer,//输入缓冲区    _In_ DWORD nInBufferSize,    _Out_writes_bytes_to_opt_(nOutBufferSize,*lpBytesReturned) LPVOID lpOutBuffer,    _In_ DWORD nOutBufferSize,    _Out_opt_ LPDWORD lpBytesReturned,    _Inout_opt_ LPOVERLAPPED lpOverlapped    );
```

```
2、IOCTL 结构
```

IOCTL 代码是一个 32 位的值，包含了多个预定义的字段，其结构如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **比特位范围** | **字段名称** | **说明** | **示例值** |
| 31-16 | **设备类型** | 标识设备的大类，如磁盘、串口等。  0x22 常代表 FILE\_DEVICE\_UNKNOWN | 0x22 |
| 15-14 | **必需的访问权限** | 应用程序需要什么样的权限来打开设备，如 FILE\_ANY\_ACCESS | 0 |
| 13-2 | **功能代码** | 驱动自定义的操作代码，这是核心，指明要执行的具体操作。 | 0x802 |
| 1-0 | **传输方法** | 定义内核与用户模式程序如何交换数据，如 METHOD\_BUFFERED | 0 |

一个完整的 IOCTL 代码就是由这些字段组合而成的，在 Windows 上，驱动开发者使用  CTL\_CODE宏来生成这个值。

### 3、IPR 结构

当用户应用程序通过 CreateFile 打开设备，并使用 DeviceIoControl 发送控制代码时，I/O 管理器会创建一个IRP（I/O Request Packet，I/O请求包），并将其路由到驱动中相应的派遣函数。IRP 用于在 I/O 操作过程中传递请求和控制信息，是在驱动程序间传递 I/O 请求的基本单位。

#### 3.1 IRP 结构核心成员

需要重点关注的是 AssociatedIrp 和 Tail.Overlay.CurrentStackLocation，它们分别与数据传输方式和IOCTL码有关。当在逆向驱动时看到对这两个数据结构的访问，很可能就是在取传递的参数和IOCTL码。

```
typedef struct _IRP {  CSHORT  Type;                    // +0x00  USHORT  Size;                    // +0x02  PMDL    MdlAddress;              // +0x08（直接I/O用）  ULONG   Flags;                   // +0x10  union {    struct _IRP *MasterIrp;    PVOID        SystemBuffer;     // +0x18 ★缓冲I/O的输入参数在这里  } AssociatedIrp;  ...  PVOID   UserBuffer;              // +0x60（METHOD_NEITHER用）  union {    PETHREAD Thread;               // +0x68 发起请求的线程    struct _IO_STACK_LOCATION *CurrentStackLocation; // ★IOCTL在这里    ...  } Tail;} IRP;
```

```
3.2 IO_STACK_LOCATION 结构
```

每个 IRP 有一个 IO\_STACK\_LOCATION，包含当前请求的详细信息：

```
typedef struct _IO_STACK_LOCATION {  UCHAR MajorFunction;             // +0x00 请求类型（IRP_MJ_DEVICE_CONTROL=0xE）  UCHAR MinorFunction;             // +0x01  ...  union {    struct {      ULONG IoControlCode;         // ★ IOCTL 值      ULONG InputBufferLength;     // ★ 输入缓冲区长度      ULONG OutputBufferLength;    // 输出缓冲区长度    } DeviceIoControl;    ...  } Parameters;} IO_STACK_LOCATION;
```

### 4、驱动的数据传递方式

驱动程序处理 I/O 缓冲区数据主要有三种方式，这通常由设备对象创建时的标志（DO\_BUFFERED\_IO、DO\_DIRECT\_IO）或 IOCTL 码的最后2位比特位决定 。

|  |  |  |
| --- | --- | --- |
| **比特位** | **传输方法** | **说明** |
| 00 | METHOD\_BUFFERED | **缓冲 I/O**。I/O 管理器将用户模式的输入/输出数据复制到内核模式下的非分页池中（Irp->AssociatedIrp.SystemBuffer）。驱动通过该系统缓冲区安全访问数据。**最常用、最安全**。 |
| 01 | METHOD\_IN\_DIRECT | **直接输入 I/O**。对于输入数据，I/O 管理器将其复制到系统缓冲区（同 METHOD\_BUFFERED）。对于输出数据，I/O 管理器锁定用户输出缓冲区的物理内存页，并构建一个 MDL（Irp->MdlAddress）供驱动访问。适用于设备向应用程序**输出大量数据**。 |
| 10 | METHOD\_OUT\_DIRECT | **直接输出 I/O**。与 METHOD\_IN\_DIRECT相反，输入数据通过 MDL 访问，输出数据则通过系统缓冲区。适用于应用程序向设备**输入大量数据**。 |
| 11 | METHOD\_NEITHER | **其他 I/O**。I/O 管理器不提供任何缓冲区或 MDL，直接将用户模式的输入和输出缓冲区虚拟地址传递给驱动（通过 IrpStackLocation->Parameters.DeviceIoControl.Type3InputBuffer和 Irp->UserBuffer）。**性能最高，但也最危险**，驱动必须在正确的进程上下文和低 IRQL 下小心访问这些地址。 |

最常用的是缓冲 I/O 方式，识别数据传递方式是为了在逆向驱动时确认用户程序是如何将参数传递给驱动的，确认了这个才能构造POC。

### 5、驱动与用户程序的通信

为了使驱动程序能够从用户模式访问，它必须建立一个通信接口，首先通过 IoCreateDevice 创建一个设备对象，然后通过 IoCreateSymbolicLink 在内核设备名和用户可见的符号链接名之间建立映射关系，为设备创建一个用户应用程序可以引用的符号链接。

设备对象充当用户进程与驱动程序功能进行交互的入口点，符号链接则充当别名，让开发人员可以通过常见的 Win32 API 在用户空间中引用设备，而无需了解内部内核命名空间。在逆向驱动程序时，如果遇到这两个函数被依次调用，就代表找到了负责将驱动程序暴露给用户模式的代码。

## 0x03 漏洞驱动挖掘方法

1、加载驱动样本

在 IDA 中打开驱动文件，定位 DriverEntry 入口点。

2、定位设备名称和符号链接

在 DriverEntry 或其调用的初始化函数中搜索 IoCreateDevice 和 IoCreateSymbolicLink 调用，这两个 API 依次出现是驱动暴露用户模式接口的标志。记录设备名（如 \Device\xxx）和符号链接（如 \\.\xxx），后者是 PoC 中 CreateFile 要打开的目标。

3、定位敏感内核 API

打开 Imports 窗口，查找高风险内核函数：

```
进程操作类：ZwTerminateProcess, ZwOpenProcess, PsTerminateProcess （最常用）；内存操作类：MmMapIoSpace, ZwReadVirtualMemory, ZwWriteVirtualMemory；回调操作类：PsRemoveCreateProcessNotifyRoutine, PsRemoveLoadImageNotifyRoutine；
```

4、追踪调用链

对敏感 API（如 ZwTerminateProcess）行交叉引用搜索，找到调用该 API 的函数，进入该函数分析其逻辑。继续向上追踪，找到调用该函数的上层函数，直至到达 IRP\_MJ\_DEVICE\_CONTROL 处理函数

5、提取 IOCTL 值

在 IOCTL 处理函数中，通常会有条件判断语句（如 if 语句），提取对应的 IOCTL 数值，这是 PoC 中 DeviceIoControl 要发送的控制码。然后分析 IOCTL 对应的输入参数结构（如需要传入 PID、地址、数据长度等），用于在 POC 中构造传参。

6、分析参数验证逻辑

检查 IOCTL 处理函数是否对输入参数进行验证，例如缓冲区长度检查、地址范围验证、权限检查等，缺乏验证或验证不严格的地方即为漏洞点。

我建议直接从 www.loldrivers.io 这个网站，寻找未被杀软标记的可利用驱动，会省事很多。当前很多安全产品对这种攻击手法的防御方式还停留在将驱动的哈希加黑，进行落地查杀或加载拦截的层面上。

```
7、实战挖掘
```

以驱动 HWAudioX64.sys 为例（MD5：F76031D7790ED141BE89FB1DA288CBB3）

定位设备名称和符号链接：

![](https://mmbiz.qpic.cn/mmbiz_png/SxWiaVqD6Jsn8pPU1icdiap0ict8mHuhDaFhHDWxDFbdNTjdibtWIIqa3m1MLmtTODdLqOd4c0ZpgZfK6krg9eLUX2OCChIdfbuicAYL2TT03Oc8E/640?wx_fmt=png&from=appmsg)

找到 ZwTerminateProcess 调用点：

![](https:...