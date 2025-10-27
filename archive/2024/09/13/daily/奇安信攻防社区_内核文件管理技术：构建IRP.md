---
title: 内核文件管理技术：构建IRP
url: https://forum.butian.net/share/3713
source: 奇安信攻防社区
date: 2024-09-13
fetch_date: 2025-10-06T18:21:05.618702
---

# 内核文件管理技术：构建IRP

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

### 内核文件管理技术：构建IRP

前言
Windows内核下的Rootkit开发技术学习。
用户数据都以文件的形式存储在本地磁盘上，Rootkit等恶意软件想要获取用户的隐私数据就需要有操作文件的功能，包括但不限于增、删、查、改。一般有...

前言
==
Windows内核下的Rootkit开发技术学习。
用户数据都以文件的形式存储在本地磁盘上，Rootkit等恶意软件想要获取用户的隐私数据就需要有操作文件的功能，包括但不限于增、删、查、改。一般有三种文件管理的方式，一是基于导出的内核API直接操作文件，二是通过程序直接构造输入输出请求包（I/O Request Package,IRP)并发送IRP来操作文件，三是根据文件系统格式（New Technology File System,NTFS)来解析硬盘上的二进制数据。
Windows处理I/O请求是一个从外到内的流程，用户层发起函数调用经过系统服务调度到内核层，操作系统内核创建对应的IRP，FSD接收到IRP后再传递给驱动程序进行操作文件等一系列操作。由于IRP经过系统服务调度后到达的FSD，所以一些内核级的恶意软件可以模拟操作系统构造IRP，以此来绕过一些API HOOK的操作，或直接操作本地磁盘的文件。
初探IRP
=====
简单的介绍一下IRP和Windows处理IRP的流程。
IRP简介
-----
IRP（I/O 请求包，I/O Request Packet）是Windows操作系统内核中用于I/O操作的一个数据结构，IRP 是在驱动程序之间传递的请求，用于描述并跟踪 I/O 操作的状态，它是驱动程序与操作系统之间处理 I/O 请求的关键机制。
IRP大多数由I/O管理器从非分页池分配，也可能由驱动程序创建，这通常用于将请求传递给另一个驱动程序。注意，谁分配了IRP谁就要负责释放。IRP的各个字段也算由I/O管理器或驱动程序进行初始化，之后IRP会被传递给设备栈的驱动程序，每个驱动程序都会处理IRP，并根据需求将其传递给下一个驱动程序。
IRP的结构
------
IRP从不单独分配，它总是伴随着一个或多个I/O栈位置结构（IO\\_STACK\\_LOCATION）。事实上，当一个IRP分配时，调用者必须要指定有多少个I/O栈位置需要跟IRP一起分配。这些栈位置紧跟着IRP，I/O栈位置的数量就是设备栈中设备对象的数量。当驱动程序接收到一个IRP时，它得到的是指向IRP结构的指针，后面跟着一组I/O栈位置，其中一个是给驱动程序使用的。
IRP的结构中还包含许多成员变量，用于存储I/O请求的相关信息。
一些重要字段：
上面成员的部分解释：
- \*\*MdlAddress\*\*：指向描述内存缓冲区的内存描述符列表 (MDL)，用于 DMA 或零拷贝传输。
- \*\*AssociatedIrp\*\*：该联合中\*\*`SystemBuffer`\*\*: 指向系统分配的缓冲区，用于 I/O 操作的数据传输，通常用于直接访问数据的操作。
- \*\*IoStatus\*\*：包含操作的状态信息和返回的字节数等。
- \*\*UserEvent\*\*：指向用户模式的事件对象，用于在 I/O 操作完成时通知用户模式。通常用于同步I/O操作。
- \*\*UserBuffer\*\*：指向用户模式的缓冲区，通常用于输入或输出数据。
除了上面的还有一些比较常见的：
- \*\*UserIosb\*\*：指向用户模式的I/O状态块，用于存储 I/O 操作的最终状态和信息。
- \*\*RequestorMode\*\*：表示发出 I/O 请求的模式，通常为 `UserMode` 或 `KernelMode`。
- \*\*Flags\*\*：存储与 `IRP` 相关的标志位。例如，`IRP\_SYNCHRONOUS\_API` 表示这是一个同步 API 调用。
还有很多就不一一列出了。具体参考[Wdm.h IRP结构](https://learn.microsoft.com/zh-cn/windows-hardware/drivers/ddi/wdm/ns-wdm-\_irp)
\*\*`IO\_STACK\_LOCATION` 结构\*\*
`IO\_STACK\_LOCATION`结构是紧跟着IRP后面的一个结构，用于描述IRP在驱动程序中每一层的具体处理信息（IRP到了这一层后应该干什么）。下图是`IO\_STACK\_LOCATION`结构的一些重要成员
最关键的`MajorFunction`：IRP的主功能代码（IRP\\_MJ\\_READ、IRP\\_MJ\\_CREATA)，在例程中，这个字段决定了驱动程序需要执行的主要操作。
`MinorFunction`次功能代码，表示一些特殊的或次要的操作。
`Parameters`：一个联合体，其中包含了与不同类型的 I/O 请求相关的参数。具体内容取决于`MajorFunction`的值。当主功能代码是`IRP\_MJ\_READ`，它将包含与读操作相关的信息（如偏移量和读取长度）。
`FileObject`: 指向与当前操作相关的文件对象。这个对象通常表示打开的文件或设备实例。
`DeviceObject`: 指向当前处理IRP的设备对象。通过这个字段，驱动程序可以访问对应的设备对象。
Windows驱动程序处理I/O请求的机制过程
=======================
假设在用户模式中调用`CreateFile`函数，Windows操作系统会将该请求转化成一个IRP，并通过驱动程序栈传递到适当的驱动程序进行处理。
驱动程序栈
-----
驱动程序栈指的是在Windows操作系统中，不同类型的驱动程序被组织成一个层次结构，每个驱动程序在这个栈中占据一个特定的层级位置。（一个驱动程序“堆叠”在另一个驱动程序上面），每个驱动程序都处理特定的I/O请求，并将处理后的请求传递给下一个层级的驱动程序。
\*\*驱动程序栈的基本层次结构：\*\*
\*\*最顶层：文件系统驱动程序（FSD）\*\*
- \*\*FSD\*\*（File System Driver）处理文件系统相关的请求，如读取、写入、创建文件等。例如，NTFS 和 FAT 是常见的文件系统驱动程序。
- 用户模式的 I/O 请求（如 `CreateFile`、`ReadFile`）通常首先被传递到 FSD 进行处理。
\*\*中间层：文件系统过滤驱动程序（Filter Driver）\*\*
- 这些驱动程序可以在 FSD 和底层硬件驱动程序之间工作，修改或监控 I/O 请求。例如，杀毒软件可能会通过过滤驱动程序检查文件系统活动。
- 过滤驱动程序不直接与硬件通信，而是拦截并处理从上层传递下来的 IRP。
\*\*底层：设备驱动程序（Device Driver）\*\*
- 这些驱动程序直接与硬件设备进行交互，如磁盘驱动程序（例如 `disk.sys`）。
- 设备驱动程序处理特定硬件设备的操作，并最终将请求传递给物理设备。
\*\*最底层：总线驱动程序（Bus Driver）\*\*
- 负责管理系统中不同的硬件总线（如 PCI、USB 等），以及连接到这些总线的设备。
- 总线驱动程序还会处理设备的即插即用（PnP）和电源管理。
FSD（文件系统驱动程序）
-------------
FSD（File System Driver，文件系统驱动程序）是操作系统中管理文件系统操作的关键组件，它负责处理与文件和目录相关的所有操作，如创建、打开、读取、写入、删除文件，以及管理文件系统和结构和元数据。它是操作系统内核的一部分，负责将用户模式的文件操作转换成内核模式的实际磁盘操作。
FSD一般位于驱动程序栈的最上层，负责接收IRP，FSD会解析这些请求，进行路径解析、权限检查等操作。主要是根据IRP的`MajorFunction`来进行特定的处理，假设操作涉及到具体的物理设备（磁盘），FSD会将其请求传递给下一层的设备驱动程序。当FSD完成了这个IRP或者设备驱动程序完成了，它们都会将处理结果返回给I/O管理器。
常见的一些FSD，例如NTFS，这是Windows 操作系统的默认文件系统驱动程序，支持文件加密、压缩、大文件和长文件名。FAT/FAT32，这是用于旧版本的Windows和便携式存储设备的文件系统。CDFS/UDFFS用于光盘文件系统的驱动程序。
I/O请求处理过程
---------
假设在用户模式下调用`CreateFile`函数，Windows操作系统会将该请求转化成一个IRP，并通过驱动程序栈传递到适当的驱动程序进行处理。
\*\*1. 系统服务调度\*\*
- `CreateFile`会调用内核原生API`NtCreateFile`，将请求发送给内核。
- `NtCreateFile`会做一系列创建I/O请求的操作，其中之一的请求便是创建IRP
\*\*2. 创建IRP并发送\*\*
- 操作系统内核（大多数是I/O管理器）会创建一个IRP并初始化，IRP包含了所有必要的信息，如文件名、访问模式等。然后发送给FSD文件系统驱动程序。
\*\*3. 驱动程序接收IRP\*\*
- FSD接收到IRP后，根据`MajorFunction`主要函数码的类型，将请求传递给相应的分发例程。
\*\*4. 分发例程处理IRP\*\*
- 分发例程解析IRP，执行相应操作。例如对于`IRP\_MJ\_CREATE`请求，驱动程序会检查文件是否存在、验证是否有访问权限等。如果文件存储在设备中，也可以将IRP传递给下一个驱动程序。
- 传递给下一个驱动程序（例如设备驱动程序），设备驱动程序可能会创建新的子IRP或发起DMA等操作来与硬件进行通信。
\*\*5. 完成IRP\*\*
- 一旦文件系统驱动程序或设备驱动程序完成了相应的操作，它们会将处理结果填入IRP结构的成员`IoStatus`中。然后调用函数`IoCompleteRequest`，表示该IRP已完成。
- I/O管理器会接收IRP返回的信息，并将其传递给用户模式的调用者。
分发例程
----
IRP分发例程是驱动程序用来处理各种IRP请求的核心。它负责接收操作系统发送的IRP，根据相应的类型（`MajorFunction`）做出相应的处理。
一般情况下，分发例程被定义为一个回调函数，并且需要特定的函数签名。
函数原型一般如下：
```c
 NTSTATUS MyDriverDispatchRoutine(
     PDEVICE\_OBJECT DeviceObject,
     PIRP Irp
 );
```
- `DeviceObject`指向与该请求相关联的设备对象
- `Irp`指示I/O请求包的指针（即IRP结构图中最顶上的irp）
\*\*分发例程的类型：\*\*
| MajorFunction | API | 含义 |
|---|---|---|
| IRP\\_MJ\\_CREATE | CreateFile、ZwCreateFile | 处理创建文件或设备的请求 |
| IRP\\_MJ\\_CLOSE | CloseHandle、ZwClose | 处理关闭文件或设备的请求 |
| IRP\\_MJ\\_READ | ReadFile、ZwReadFile | 处理读请求 |
| IRP\\_MJ\\_WRITE | WriteFile、ZwWriteFile | 处理写请求 |
| IRP\\_MJ\\_DEVICE\\_CONTROL | DeviceToControl、ZwDeviceToControl | 处理设备控制请求（如 IOCTL 操作） |
分发例程处理IRP请求后，必须要结束这个请求，即告诉操作系统该操作已完成。（如果不这么做，句柄就会泄露，请求进程无法真正终止，进而导致它的包含进程持续存在，从而导致“僵尸进程”）
这时分发例程需要调用`IoCompleteRequest`，这其实是一个宏，它指示调用者已完成对给定 I/O 请求的所有处理并将给定的 IRP 返回给 I/O 管理器。要注意的是，切勿在持有自旋锁时调用`IoCompleteRequest`，在持有自旋锁时尝试完成 IRP 可能会导致死锁。
一个分发例程的示例代码：
```c
 NTSTATUS MyDriverCreate(
     PDEVICE\_OBJECT DeviceObject,
     PIRP Irp
 )
 {
     UNREFERENCED\_PARAMETER(DeviceObject);
 ​
     // 设置 IRP 的状态
     Irp-&gt;IoStatus.Status = STATUS\_SUCCESS;
     Irp-&gt;IoStatus.Information = 0;
 ​
     // 完成 IRP
     IoCompleteRequest(Irp, IO\_NO\_INCREMENT);
 ​
     return STATUS\_SUCCESS;
 }
```
构建IRP创建文件
=========
函数介绍
----
关于IRP的各种机制，缓冲I/O和直接I/O等等等等的内容，留待后续深入研究。
Windows操作系统提供了很多函数来构建IRP，例如：
- `IoAllocateIrp`，该函数仅分配并初始化一个空的IRP，提供了一个基本框架，用于创建和发送自己的I/O请求。
- `IoBuildSynchronousFsdRequest`，该函数不仅分配一个IRP，还根据指定的操作类型（如读、写、创建等）初始化这个IRP。它专门用于构建\*\*同步\*\*的FSD请求，比如读取、写入文件或者创建文件。
- `IoBuildDeviceIoControlRequest`，该函数构建一个IRP，用于设备 I/O 控制请求（IOCTL）。
- `IoBuildAsynchronousFsdRequest`，该函数构建一个IRP，用于\*\*异步\*\*的FSD请求。
除了这四种还有很多针对不同场景和需求的函数，可以自行文档查阅。
### IoAllocateIrp
函数签名：
PIRP IoAllocateIrp(
CCHAR StackSize,
BOOLEAN ChargeQuota
);
- `StackSize`：指定I/O Stack Location的数量。
- `ChargeQuota`：将此设置为TRUE会导致分配给 IRP 的内存占用当前进程的配额。应由中间驱动程序设置为FALSE 。
- 该函数返回一个指向分配并初始化好的 IRP 的指针。
### IoBuildSynchronousFsdRequest
函数签名：
```c
 PIRP IoBuildSynchronousFsdRequest(
     ULONG MajorFunction, //主函数代码
     PDEVICE\_OBJECT DeviceObject, //指向目标设备对象的指针。
     PVOID Buffer, //指向要读取或写入的数据缓冲区的指针。
     ULONG Length, // 要读取或写入的字节数。
     PLARGE\_INTEGER StartingOffset, //指定文件中的偏移量，从该偏移量开始进行读或写操作。
     PKEVENT Event, //向 KEVENT 结构的指针，该结构用于同步操作。
     PIO\_STATUS\_BLOCK IoStatusBlock //指向 IO\\_STATUS\\_BLOCK 结构的指针，该结构用于存储操作的状态和信息。
 );
```
### IoCallDriver
该函数用于将IRP传递给下一个驱动程序（驱动程序之间的通信，通常是传递给更低一级的驱动程序）。
函数签名：
```c
 NTSTATUS IoCallDriver(
   \_In\_ PDEVICE\_OBJECT DeviceObject,
   \_Inout\_ PIRP Irp
 );
```
- `DeviceObject`: 指向下一个驱动程序的设备对象，该驱动程序将接收和处理传递的 IRP。
- `Irp`: 指向要传递的 IRP 数据结构。
先前说过，IRP结构中由多少个I/O堆栈位置，对应了设备驱动栈中的驱动程序有多少。也就是说，`IoCallDriver`函数的目标驱动程序在该IRP中必须要有相应的堆栈位置。同时，一个传递给`IoCallDriver`的IRP传递给较低级的驱动程序后，该IRP不能再被高层的IRP访问，除非高级驱动程序调用了`IoSetCompletionRoutine`为IRP安装一个`IoCompletion`完成例程。
### IoCreateFile
该例程可以创建新的文件或目录，或者打开现有文件、设备、目录或卷，并为调用者提供文件对象的句柄。
函数定义同`ZwCreateFile`有点类似，但它更高级一点，是内核模式专用的文件操作函数。
### ObReferenceObjectByHandle
用于通过给定的句柄获取一个对象的引用指针。
```c
 NTSTATUS ObReferenceObjectByHandle(
   HANDLE Handle,
   ACCESS\...