---
title: Windows内核：初探 ELAM
url: https://forum.butian.net/share/3953
source: 奇安信攻防社区
date: 2024-12-27
fetch_date: 2025-10-06T19:33:05.517682
---

# Windows内核：初探 ELAM

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

### Windows内核：初探 ELAM

前言
学习一下Windows内核的一种安全机制：Windows 8 中引入的Early Launch Anti-Malware（ELAM）模块。该机制旨在防止内核地址空间中执行未经授权的代码，对于Rootkit来说，就是使Rootkit更加...

前言
==
学习一下Windows内核的一种安全机制：Windows 8 中引入的Early Launch Anti-Malware（ELAM）模块。该机制旨在防止内核地址空间中执行未经授权的代码，对于Rootkit来说，就是使Rootkit更加难以破坏系统。
ELAM模块
======
ELAM模块是一种用于Windows系统的检测机制，它允许第三方安全软件（如杀软）注册一个内核模式驱动程序，该驱动程序保证再启动过程的早期执行，即再其它第三方驱动程序加载之前。因此，当攻击者试图将恶意组件加载到Windows内核地址空间时，安全软件可以检查并阻止恶意驱动程序加载，因为ELAM驱动程序以及处于激活状态。
工作原理
----
### 驱动加载过程
在Windows系统引导过程中讲过，Windows 系统的启动分为多个阶段，简化下：
- 固件初始化
- 引导加载程序
- Windows 启动管理器
- Windows 内核加载
- 内核初始化
- 会话管理器初始化
- 用户登录
在 Windows 内核加载阶段，控制权会移交给Windows加载器`Winload.exe`，它会加载必要的内核文件如`Ntoskrnl.exe`，在此时会加载注册表中配置为 引导启动类型（Boot Start Type）的驱动程序，包括ELAM模块。
在内核加载后，但又未开始初始化驱动程序时，Windows会首先加载ELAM驱动程序。ELAM驱动程序被定义为Boot Start 驱动程序，优先级最高。
驱动程序在注册表中的位置：
```css
HKLM\SYSTEM\CurrentControlSet\Services\[ELAMDriverName]
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c13a32b4533b9e4e0a309b7f90ff079d191e20e4.png)
start值为0x0，表明它是一个引导启动驱动程序，但这里我电脑是0x3，说明它是手动启动的状态。type为0x1，表明这是一个内核驱动程序。
当ELAM驱动程序被加载到内存后，初始化例程（`DriverEntry`）开始执行。
### API回调例程
ELAM驱动程序通过特定的API注册回调例程，内核使用这些例程来评估系统注册表配置单元和引导驱动程序中的数据。这些回调检测恶意数据和模块，并防止它们被Windows加载和初始化。
Windows内核通过实现以下API例程注册和注销这些回调函数：
- `CmRegisterCallbackEx`和`CmUnRegisterCallback` 注册和注销监视注册表数据回调.
ELAM 驱动可以通过注册这些回调来拦截对关键注册表数据（如 `HKLM\SYSTEM` 或特定安全策略）的访问，分析和阻止恶意修改。
`CmRegisterCallbackEx`函数原型：
```c
NTSTATUS CmRegisterCallbackEx(
PCALLBACK\_FUNCTION CallbackFunction, 指向回调函数的指针。
PCUNICODE\_STRING Altitude, 回调的优先级，通常为字符串表示，如 `"320000"`。
PVOID DriverObject, 驱动的 `DRIVER\_OBJECT` 指针。
PVOID Context, 回调的上下文信息。
PLARGE\_INTEGER Cookie 用于标识注册的回调实例，稍后通过 `CmUnRegisterCallback` 取消注册。
);
```
`CmUnRegisterCallback`函数原型：
```c
NTSTATUS CmUnRegisterCallback(
LARGE\_INTEGER Cookie 对应于 `CmRegisterCallbackEx` 的返回值，用于取消回调
);
```
- `IoRegisterBootDriverCallback`和`IoUnRegisterBootDriverCallback`注册和注销启动驱动程序的回调。
ELAM 驱动程序使用这些回调函数，决定后续引导驱动程序是否允许加载。
`IoRegisterBootDriverCallback`函数原型：
```c
NTSTATUS IoRegisterBootDriverCallback(
PIO\_BOOT\_DRIVER\_CALLBACK CallbackFunction, 指向回调函数的指针。
PVOID Context 回调的上下文信息。
);
```
`IoUnRegisterBootDriverCallback`函数原型：
```c
NTSTATUS IoUnRegisterBootDriverCallback(
PIO\_BOOT\_DRIVER\_CALLBACK CallbackFunction 对应于 `IoRegisterBootDriverCallback` 的注册回调。
);
```
这些例程使用标准的 `EX\_CALLBACK\_FUNCTION` ,原型如下：
```c
typedef VOID (\*EX\_CALLBACK\_FUNCTION)(
PVOID CallbackContext,
PVOID Argument1,
PVOID Argument2
);
```
- \*\*`CallbackContext`\*\*：上下文信息，由注册回调时提供。
- \*\*`Argument1` 和 `Argument2`\*\*：回调的特定参数，因 API 而异。
一旦驱动程序执行了上述回调例程之一来注册回调，则参数`CallbackContext`会从ELAM驱动程序接收上下文。上下文是指向内存缓冲区的指针，该缓冲区包含ELAM驱动程序特定的参数，任何回调例程都可以访问该参数。此上下文还是一个用于存储ELAM驱动程序当前状态的指针。
#### 回调类型
上面原型中的Argument1也是指回调类型，对于引导启动驱动程序，它可以是下列类型之一：
- `BdCbStatusUpdate`向ELAM驱动程序提供有关驱动程序依赖项或引导驱动程序的加载的状态更新。
当 `Argument1` 为 `BdCbStatusUpdate` 时，`Argument2` 通常是指向 `BOOT\_DRIVER\_STATUS\_UPDATE` 数据结构的指针。示例结构：
```c
typedef struct \_BOOT\_DRIVER\_STATUS\_UPDATE {
UNICODE\_STRING DriverPath; // 当前驱动的路径
NTSTATUS Status; // 加载状态，例如 STATUS\_SUCCESS 或错误代码
} BOOT\_DRIVER\_STATUS\_UPDATE, \*PBOOT\_DRIVER\_STATUS\_UPDATE;
```
- `BdCbInitializeImage`提供引导驱动程序的元数据，允许 ELAM 驱动对其进行分类。
LAM 驱动基于驱动程序的签名、路径或自定义策略分类驱动：
- `BootDriverGood`: 信任并加载。
- `BootDriverBad`: 阻止加载。
- `BootDriverUnknown`: 未知状态，可根据策略处理。
当 `Argument1` 为 `BdCbInitializeImage` 时，`Argument2` 通常是指向 `BOOT\_DRIVER\_INFO` 数据结构的指针。示例结构：
```c
typedef struct \_BOOT\_DRIVER\_INFO {
UNICODE\_STRING FilePath; // 驱动程序的文件路径
PVOID ImageBase; // 驱动程序在内存中的基地址
ULONG ImageSize; // 驱动程序映像的大小
ULONG Classification; // 当前分类状态（由回调函数更新）
} BOOT\_DRIVER\_INFO, \*PBOOT\_DRIVER\_INFO;
```
#### 引导驱动程序的分类
Argument2参数表示操作系统对引导驱动程序的分类信息，如上所说的，分为三类：非恶意（信任并加载）、恶意（阻止加载）以及未知。
然而，ELAM驱动程序只能基于以下有限的数据对驱动程序映像进行分类：
- 映像名称
- 映像注册为引导驱动程序的注册表位置
- 映像文件的证书发布者和所有者
- 映像的散列值和对应的算法名称
- 证书指纹和指纹算法的名称
ELAM驱动程序密钥获取到映像的基质，就无法访问硬件驱动器上的二进制映像文件，因为存储设备驱动程序栈尚未初始化（系统尚未完全启动）。它只能基于映像的散列值和证书来决定要加载的驱动程序，而不能观察映像本身。因此，在这个阶段对驱动程序的保护不是很有效。
#### ELAM执行策略
Windows根据该注册表项中指定的ELAM策略值`HKLM\System\CurrentControlSet\Control\EarlyLaunch\DriverLoadPolicy`来决定是否加载已知的恶意驱动或未知驱动。
下面是允许加载的驱动程序类型和对应的ELMA策略值。
| \*\*策略值名称\*\* | \*\*策略值\*\* | \*\*描述\*\* |
|---|---|---|
| PNP\\_INITIALIZE\\_DRIVERS\\_DEFAUL | `0x00` | 仅加载已知为非恶意的驱动程序 |
| PNP\\_INITIALIZE\\_UNKNOWN\\_DRIVERS | `0x01` | 仅加载已知未非恶意和未知的驱动程序 |
| PNP\\_INITIALIZE\\_BAD\\_CRITICAL\\_DRIVERS | `0x03` | 加载已知未非恶意、未知的和已知为恶意的关键驱动程序（这是默认设置） |
| PNP\\_INITIALIZE\\_BAD\\_DRIVERS | `0x07` | 加载所有驱动程序 |
可以看到，默认的ELAM策略`PNP\_INITIALIZE\_BAD\_CRITICAL\_DRIVERS`允许加载恶意的关键驱动程序。这意味着，如果一个关键驱动程序被ELAM归类为已知的恶意驱动程序，系统也会加载它。这种策略背后的基本原理是，关键系统驱动程序是操作系统的重要组成部分，因此任何初始化失败都会导致操作系统无法启动。也就是说，除非成功加载并初始化了所有关键请重新，否则系统不会启动。因此，此ELMA策略会损害某些安全性，以提高可用性和可维护性。
但是，这个策略不会加载已知为恶意的非关键驱动程序，或者那些非必要的驱动程序。这就是`PNP\_INITIALIZE\_BAD\_CRITICAL\_DRIVERS`和`PNP\_INITIALIZE\_BAD\_DRIVERS`策略之间的主要区别：后者允许加载所有驱动程序，包括已知为恶意的非关键驱动程序。
BOOTKIT绕过
---------
ELAM可以有效的抵御Rootkit的威胁，但在低于Bootkit方面却没有什么用（它并非为Bootkit设计的）。
ELAM只能监视合法加载的驱动程序，但是大多数Bootkit会使用未注册的操作系统功能来加载内核模式驱动程序。这意味着尽管有ELAM，Bootkit也可以绕过安全性强制措施并将其代码注入内核地址空间。此外，Bootkit的恶意代码可以在初始化操作系统内核和加载任何内核模式驱动程序（包括ELAM）之前允许。这意味着它可以避开ELAM保护。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d35dbaf0a07db9ce12c6cdfb209b4823ffa0c4be.png)
在所有的操作系统子系统（I/O子系统、对象管理器、即插即用管理器等）被初始化之后，以及执行ELAM之前，大多数Bootkit都会在内核初始化期间加载它们的内核模式代码。
简单的ELAM驱动
---------
```c++
#include <ntddk.h>
// 上下文结构体
typedef struct \_ELAM\_CONTEXT {
BOOLEAN AllowUnknownDrivers; // 策略：是否允许未知驱动
} ELAM\_CONTEXT, \*PELAM\_CONTEXT;
// 回调函数原型
VOID ElamBootDriverCallback(PVOID CallbackContext, PVOID Argument1, PVOID Argument2);
// 上下文全局变量
ELAM\_CONTEXT g\_ElamContext = { TRUE }; // 默认允许未知驱动
// DriverEntry - 驱动入口点
NTSTATUS DriverEntry(PDRIVER\_OBJECT DriverObject, PUNICODE\_STRING RegistryPath) {
NTSTATUS status;
// 注册 ELAM 回调函数
status = IoRegisterBootDriverCallback(ElamBootDriverCallback, &g\_ElamContext);
if (!NT\_SUCCESS(status)) {
KdPrint(("Failed to register ELAM callback. Status: 0x%x\n", status));
return status;
}
KdPrint(("ELAM driver loaded successfully.\n"));
// 设置驱动卸载函数
DriverObject->DriverUnload = [](PDRIVER\_OBJECT DriverObject) {
// 注销回调
IoUnRegisterBootDriverCallback(ElamBootDriverCallback);
KdPrint(("ELAM driver unloaded.\n"));
};
return STATUS\_SUCCESS;
}
// ELAM 回调函数
VOID ElamBootDriverCallback(PVOID CallbackContext, PVOID Argument1, PVOID Argument2) {
PELAM\_CONTEXT pContext = (PELAM\_CONTEXT)CallbackContext;
// 检查回调类型
if ((ULONG\_PTR)Argument1 == BdCbInitializeImage) {
// 获取驱动信息
PBOOT\_DRIVER\_INFO BootDriverInfo = (PBOOT\_DRIVER\_INFO)Argument2;
// 检查驱动路径
if (wcsstr(BootDriverInfo->FilePath.Buffer, L"TrustedDriver.sys")) {
BootDriverInfo->Classification = BootDriverGood; // 可信驱动
KdPrint(("Driver %wZ classified as Good.\n", &BootDriverInfo->FilePath));
} else if (pContext->AllowUnknownDrivers) {
BootDriverInfo->Classification = BootDriverUnknown; // 未知驱动
KdPrint(("Driver %wZ classified as Unknown.\n", &BootDriverInfo->FilePath));
} else {
BootDriverInfo->Classification = BootDriverBad; // 阻止加载
KdPrint(("Driver %wZ classified as Bad.\n", &BootDriverInfo->FilePath));
}
}
}
```

* 发表于 2024-12-26 10:06:05
* 阅读 ( 3347 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Sciurdae](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bc2f26335b817b6b3b3f133f3743e19ccb490ef.png)](https://...