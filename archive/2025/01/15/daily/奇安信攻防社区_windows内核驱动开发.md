---
title: windows内核驱动开发
url: https://forum.butian.net/share/4034
source: 奇安信攻防社区
date: 2025-01-15
fetch_date: 2025-10-06T20:09:13.692231
---

# windows内核驱动开发

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

### windows内核驱动开发

* [渗透测试](https://forum.butian.net/topic/47)

在现代操作系统开发领域，Windows内核开发 是一项涉及系统底层机制的重要技术。本篇文章将围绕 Windows内核架构 和 驱动开发 展开讨论，旨在为读者提供一个全面而深入的学习路径，尤其适合对内核编程和设备驱动开发感兴趣的技术人员。

IO系统
====
I/O（输入/输出）系统通过抽象化简化了逻辑和物理设备的交互，许多 I/O 操作是在操作系统的执行层中进行的。该系统具备统一命名和安全机制，支持异步通信、即插即用功能、驱动程序的动态加载和卸载以及电源管理等多种重要功能
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-29a01fc614e0690620445e2dee61a8f4280879ce.png)
上图为 I/O 系统组件的层次结构，应用程序和服务负责与用户交互。中间层是用户模式和内核模式的接口，包括 WMI 服务、PnP 管理器以及安装组件等。WMI 例程、I/O 管理器、PnP 管理器和电源管理器处于内核模式，负责处理 I/O 操作、即插即用设备的管理和电源管理。最底层是驱动程序和硬件抽象层 (HAL)，实现硬件与软件之间的通信
硬件抽象层 (HAL)： 硬件抽象层（HAL，Hardware Abstraction Layer）是操作系统中的一个关键组件，负责将操作系统与底层硬件设备隔离开来。它通过提供一种标准化的接口，使得操作系统能够与各种硬件平台交互，而不必针对特定硬件进行修改和优化
用户模式与内核模式
---------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b15119cd0eab9eae22f2c8d6083a7d8d51ab18f9.png)
当cpu在执行时，会记录当前程序的权限级别，上图是基于x86架构的，Ring3是最小权限环，在这一环里有很多限制，比如说不能设置cr3寄存器，不能和硬件外设交互，不能执行HLT之类的，当软件在这一环上运行，需要和系统进行交互时，就会转换到Ring0，这里还有Ring2和Ring1，最初它们是为设备驱动准备的，区分了不同的访问级别，但是很少会用到，Ring0是主管模式，在这一环里是没有限制的，可以做任何事，这也是内核运行的地方
```php
Ring 3：用户模式，权限最低，限制较多，无法访问CR3等内核模式寄存器，无法执行HLT指令等。
Ring 0：内核模式，权限最高，可以执行任何指令和访问所有寄存器。
Ring -1：管理模式（主要用于虚拟化），可以拦截敏感操作，确保虚拟机中的用户内核无法无限制地访问主机硬件。
```
Ring -1
-------
还有一个Ring -1环，但是内核是在Ring 0环的，随着虚拟机的兴起，管理模式的特权开始引发问题。虚拟机的“用户”内核不应该能够无限制地访问主机的物理硬件，Ring -1，管理程序模式。能够拦截用户执行的敏感 Ring 0 操作并在主机操作系统中处理它们
设备驱动程序
------
设备驱动程序是操作系统和硬件设备之间的桥梁，主要分为用户模式和内核模式。用户模式驱动程序通常应用于较简单的设备（如打印机），并通过 UMDF 框架运行。内核模式驱动程序则负责更为核心的功能，如文件系统、即插即用设备和其他非即插即用设备的管理。设备驱动程序作为可加载模块，通过与内核集成，确保第三方硬件可以与操作系统无缝协作
UMDF：UMDF（User-Mode Driver Framework，用户模式驱动程序框架）是微软为 Windows 操作系统提供的一种框架，用于编写在用户模式下运行的设备驱动程序。与传统的内核模式驱动程序不同，UMDF 驱动程序在用户模式下运行，主要用于一些低风险、低复杂度的设备
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-02355704f464de73328189be07f5848f04b9c2e7.png)
上图展示了从用户模式到内核模式调用设备驱动程序的过程。当应用程序请求读取文件时，它通过用户模式的 API（如 `ReadFile`）调用，最终通过系统调用机制（如 `sysenter` 或 `syscall`）切换到内核模式。在内核模式下，将执行进一步的处理，调用对应的驱动程序函数（如 `NtReadFile`），并通过驱动程序 `driver.sys` 执行底层硬件的 I/O 操作
设备访问
----
为了访问设备，应用程序必须通过 `CreateFile` 或类似函数打开一个设备句柄。这些函数可以用于用户模式和内核模式下的设备访问，但名称格式和路径指向的是设备的符号链接，而非传统的文件路径。在计算机中，必须使用特定格式（如 `\\.\name`）来访问设备
这里用winobj展示，WinObj 是 Windows 内部工具之一，它是一个 GUI 工具，用于显示和管理 Windows 操作系统中的对象管理器命名空间。对象管理器是 Windows 内核的一部分，负责管理系统中的各种对象（如设备、文件、注册表项、符号链接、命名管道等）
winobj下载地址：
```php
https://learn.microsoft.com/en-us/sysinternals/downloads/winobj
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e02171ff5778cd279123cef39ebeecd35d89fbc5.png)
`GLOBAL??` 是一个特殊目录，通常用于定义设备符号链接，方便用户模式程序访问内核对象。在 Windows 中，设备符号链接是用于提供设备的用户友好名称（例如 `COM1`），使得用户模式应用程序可以通过符号链接而不是设备名称直接访问设备，例如 `C:` 盘符被链接到 `\Device\HarddiskVolume3`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7ff4504939c3fa326d5b63307249d2ad3c84cc48.png)
在Device目录下的这些长名称实际上是硬件设备的符号链接，用于将系统中的逻辑路径映射到底层的物理设备，这里用代码简单演示调用设备的过程
`Device` 目录直接包含设备对象，每个设备在创建时会在 `Device` 目录中注册。内核模式驱动程序通常通过设备对象与系统和用户模式程序通信。`Device` 目录下的对象表示设备在内核空间中的具体表示，通常不直接对用户模式程序可见。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-85f88c46478dabe598ded955386efa3b853adb1f.png)
假如我要创建访问这个Psched设备
```php
#include <Windows.h>
#include <stdio.h>
int main() {
HANDLE hDevice = CreateFile(L"\\\\.\\Pcsched", GENERIC\_WRITE, 0, nullptr, OPEN\_EXISTING, 0, nullptr);
CloseHandle(hDevice);
}
```
这行代码 `HANDLE hDevice = CreateFile(L"\\\\.\\Psched", GENERIC\_WRITE, 0, nullptr, OPEN\_EXISTING, 0, nullptr);` 试图打开一个设备或文件句柄。路径 `\\\\.\\Psched` 是设备或文件的符号链接，`\\\\.` 前缀表示访问设备对象，之后使用 `CloseHandle(hDevice)` 关闭句柄，释放句柄
`CreateFile` 是 Windows API 中用于创建或打开文件或设备对象的函数。该函数不仅用于处理文件系统中的文件，还可用于打开与设备（如磁盘驱动器、串口设备等）相关的句柄。在使用 `CreateFile` 操作设备时，通常需要指定 `OPEN\_EXISTING`，表示仅打开已经存在的设备或文件，而不会创建新的设备
```php
HANDLE CreateFile(
LPCTSTR lpszName, // 文件或设备的名称
DWORD fdwAccess, // 访问模式 (读取、写入等)
DWORD fdwShareMode, // 共享模式
LPSECURITY\_ATTRIBUTES lpsa, // 安全性和继承属性
DWORD fdwCreate, // 创建标志
DWORD fdwAttributes, // 文件属性和标志
HANDLE hTemplateFile // 要复制的文件属性的句柄
);
```
返回值是文件或设备的句柄，若操作失败，则返回 `INVALID\_HANDLE\_VALUE`，可以通过 `GetLastError` 获取具体的错误信息
IO操作
----
调用设备常用的四个函数：
`ReadFile` 用于从文件或设备句柄读取数据。参数包括文件句柄、数据存储的缓冲区、缓冲区的大小，以及指向实际读取字节数的指针
```php
BOOL ReadFile(
HANDLE hFile, // 文件句柄
LPVOID lpBuffer, // 接收数据的缓冲区
DWORD nBufferSize, // 缓冲区大小
LPDWORD lpBytesRead, // 实际读取的字节数
LPOVERLAPPED lpOverlapped // 用于异步 I/O
);
```
`WriteFile` 用于将数据写入文件或设备。参数包括文件句柄、指向要写入数据的缓冲区、缓冲区的大小，以及指向实际写入字节数的指针
```php
BOOL WriteFile(
HANDLE hFile, // 文件句柄
LPCVOID lpBuffer, // 要写入设备的缓冲区
DWORD nBufferSize, // 缓冲区大小
LPDWORD lpBytesWritten,// 实际写入的字节数
LPOVERLAPPED lpOverlapped // 用于异步 I/O
);
```
`DeviceIoControl` 是 Windows 中用于与设备驱动程序进行交互的重要 API。通过这个函数，应用程序可以向设备发送 I/O 控制请求（IOCTL），从而执行特定的设备操作。这些操作超出了标准的读写功能，通常包括一些硬件特定的控制功能
例如，调用 `DeviceIoControl` 可以用来获取设备状态信息、执行设备特定的操作，或将控制命令发送到硬件设备。参数中最关键的是 `dwIoControlCode`，它决定了请求的类型，而输入和输出缓冲区提供了操作所需的额外数据或接收设备的响应
```php
BOOL DeviceIoControl(
HANDLE hDevice, // 设备或文件的句柄
DWORD dwIoControlCode, // IOCTL 控制码
LPVOID lpInBuffer, // 输入缓冲区
DWORD nInBufferSize, // 输入缓冲区大小
LPVOID lpOutBuffer, // 输出缓冲区
DWORD nOutBufferSize, // 输出缓冲区大小
LPDWORD lpBytesReturned, // 实际返回的字节数
LPOVERLAPPED lpOverlapped // 用于异步操作
);
```
`CloseHandle` 是一个 Windows API，用于关闭文件、设备或其他内核对象的句柄。句柄是指向特定系统资源的引用，当不再需要该资源时，必须调用 `CloseHandle` 来释放
```php
BOOL CloseHandle(HANDLE hFile); // 关闭内核对象句柄
```
设备驱动程序
------
内核设备驱动程序是 Windows 操作系统中运行在内核模式下的程序，它们与硬件设备直接交互。与用户模式程序不同，内核驱动程序有更高的权限，能够访问系统的核心资源。因此，它们如果出现未处理的异常，会导致整个系统崩溃（即蓝屏）。这些驱动通常以 `.SYS` 作为文件扩展名，并通过系统 API 函数（如 `ReadFile`、`WriteFile` 和 `DeviceIoControl`）与用户模式程序交互。驱动程序还会导出多个功能入口点，供操作系统调用以完成设备管理和控制
这里用process explorer演示，下载地址：
```php
https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
```
选择system，然后查看dll
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-047658282c46a884c37d3ab76f6506590c9bec99.png)
在上图可以看到加载到系统空间中的所有设备驱动程序
即插即用设备程序
--------
即插即用驱动程序的目的是与即插即用（PnP）管理器和电源管理器进行通信，从而在硬件设备连接到系统时自动识别、配置并加载相应的驱动程序。PnP 驱动程序分为三类：功能驱动程序、总线驱动程序和过滤驱动程序
```php
功能驱动程序 是与硬件设备直接交互的主要驱动程序，负责设备的管理。
总线驱动程序 管理连接多个设备的总线，例如 PCI 或 USB。
过滤驱动程序 则可以在驱动堆栈中拦截和修改 I/O 请求，以执行额外的处理。
```
Windows 驱动模型 (WDM)
------------------
Windows 驱动模型 (WDM) 是为解决不同 Windows 版本之间的驱动程序兼容性问题而设计的驱动程序开发框架。它使得开发者可以为多种设备（如 PCI 设备、USB 设备等）编写通用的驱动程序，且在 Windows 98/ME 和 Windows 2000/XP 之间共享代码，减少开发和维护的复杂性。
WDM 驱动程序支持的设备类型非常广泛，并且具有向后兼容性和可扩展性，支持未来的总线和设备标准，文件系统驱动和视频驱动并不包含在 WDM 模型中，需要使用其他专门的驱动模型来开发
Windows 驱动框架 (WDF)
------------------
Windows 驱动框架 (WDF) 是为简化和统一 Windows 驱动程序开发而引入的一种框架。它分为 KMDF 和 UMDF，分别用于内核模式和用户模式驱动程序开发。KMDF 是 WDM（Windows 驱动模型）的进化和替代品，提供了更简洁、更模块化的驱动开发方式
WDF 的特点包括基于对象的编程模型，开发者只需关注事件处理而无需处理底层细节。同时，它还提供了即插即用 (PnP) 和电源管理的自动实现，使驱动开发更加高效。KMDF 具有向后兼容性，支持在旧版 Windows 上运行，同时也支持版本控制，使驱动可以在多个 Windows 版本之间并行运行
安装windows内核开发环境
===============
visual studio 2022下载地址：
```php
https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false
```
安装图中勾选的内容
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-65ccfec9c63507be50a75217c95c022e9f97c4dc.png)
wdk下载地址：
```php
https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7889004b75986d12bcae470b6b42225c48b223fa.png)
或者直接在安装界面安装
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024...