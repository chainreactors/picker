---
title: Qilin EDR 杀手感染链分析
url: https://mp.weixin.qq.com/s/QEE7NF5w9k-F6oMkQqZz7w
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:16:43.343437
---

# Qilin EDR 杀手感染链分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSgVPAMicXCkib42y3ZQ57OOOialia4ibibrMKHW0Wc1mNCHn6vG0Ya1VuMHKQGyzYbJuuiaBEpCk4mylarRgrWfnQELkKpLc1YicjzMDro/0?wx_fmt=jpeg)

# Qilin EDR 杀手感染链分析

Takahiro Takeda
Takahiro Takeda

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://blog.talosintelligence.com/qilin-edr-killer/ | Takahiro Takeda, Holger Unterbrink |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSia0icW3aGlTJnAh1OGaiaNVzCzRVySl3FVuzBsGzPG6C6AWLUBcLNXH8L4xibXricHNiarOE4Jqtn6xu9kickWvsluH08JC3P3xU7pMs/640?wx_fmt=jpeg&from=appmsg)

Thursday, April 2, 2026 06:00

## PE loader section ("msimg32.dll")

* 端点检测与响应 (EDR) 工具已被广泛部署，其能力也远超传统防病毒软件。因此，攻击者会借助 EDR 杀手工具将其禁用或绕过。
* 禁用遥测数据采集（进程、内存、网络活动）会压缩防御者的可见范围与分析空间。
* 随着防御者持续强化行为检测能力，攻击者愈发频繁地将防御层本身列为初始入侵或早期执行阶段的攻击目标。
* 本文对 Qilin 勒索软件攻击中所使用的恶意 "msimg32.dll" 进行了深入分析。该文件是一条针对 EDR 系统的多阶段感染链，能够终止市场上几乎所有主流厂商的 300 余种 EDR 驱动程序。
* 我们将详细介绍该恶意软件用于规避并最终瘫痪 EDR 解决方案的多种技术，包括基于 SEH/VEH 的混淆、内核对象操控，以及多种 API 与系统调用绕过方法。

---

本文对恶意动态链接库 (DLL) "msimg32.dll" 进行了深入的技术分析。Cisco Talos 发现该 DLL 被部署于 Qilin 勒索软件攻击活动中。关于 Qilin 更广泛的攻击活动，此前已在此处的博文中进行了介绍。

该 DLL 是一条复杂多阶段感染链的初始阶段，旨在禁用受感染系统上本地部署的端点检测与响应 (EDR) 解决方案。图 1 展示了该感染链整体执行流程的高层次示意图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nShASkq0ziaHKAHwGRkdy8tvam30bQfs6ILwrmkewdZhricWaUy0GyMY9Irz5N1TdgicdJKCL6jQ7w16iaVJE2A2b1wicDK01KBfCHs0/640?wx_fmt=jpeg&from=appmsg)

图 1. 感染链概览。

第一阶段为 PE 加载器，负责为 EDR 杀手组件准备执行环境。该次级载荷以加密形式内嵌于加载器中。

加载器实现了高级 EDR 规避技术：采用类似 Halo's Gate 的方式，在运行时中和用户态钩子，并抑制 Windows 事件跟踪 (ETW) 的事件生成；同时大量使用结构化异常处理 (SEH) 与向量化异常处理 (VEH) 来混淆控制流、掩盖 API 调用特征。借助上述技术，EDR 杀手载荷得以完全在内存中完成解密、加载与执行，而不会触发本地 EDR 解决方案的检测。

激活后，EDR 杀手组件将加载两个辅助驱动程序：第一个（"rwdrv.sys"）负责访问系统物理内存，第二个（"hlpdrv.sys"）用于终止 EDR 进程。在加载第二个驱动程序之前，EDR 杀手组件会注销 EDR 所建立的监控回调，确保进程终止过程不受干扰。

综上所述，该恶意软件能够禁用来自众多厂商的 300 余种 EDR 驱动程序。尽管该攻击活动此前已由、及其他研究人员在较高层面进行了报道，本文将聚焦于感染链中尚未公开披露的技术细节，例如 SEH/VEH 技巧以及针对特定内核对象的覆写操作。

## PE loader section ("msimg32.dll")

该恶意 DLL 极有可能被某个从 "msimg32.dll" 导入函数的合法应用程序进行 DLL 侧加载。为保留预期功能，原始 API 调用会被转发至位于 "C:\Windows\System32" 的合法库。

威胁行为者部署的 "msimg32.dll" 版本在其 `DllMain`函数内部触发恶意逻辑。因此，一旦合法应用程序加载该 DLL，载荷便立即执行。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjCFtBwLtgHg7wYNfQ33e8CCFatSWmfBDU96P89rxAYTjuYs3vwhnibsUEh1VXxHLwgRs4wF4c7PAmWKuSSibBadx57hotPXOJDE/640?wx_fmt=png&from=appmsg)

图 2. "msimg32.dll" 的恶意版本。

Sophos 在其早期博客中也对该加载器提供了部分技术与历史见解，文中将该加载器称为 Shanya。

### 初始化阶段

初始化期间，加载器在进程内存中分配一块堆缓冲区，用作槽位策略表。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaEmJGgnY3AXxRUicVY1xDdFnmLAjTtN690GShgZIFdF4KsHEymR3Lng3U9pOWfBA5XTc7Qia9BkKY5l3HOWwHx5WPr6ib848zicWc/640?wx_fmt=png&from=appmsg)

图 3a. 为槽位策略表分配缓冲区。

该缓冲区的大小计算方式为：将 "ntdll.dll" 的 `OptionalHeader.SizeOfCode`除以 16（即 `SizeOfCode >> 4`），每个 16 字节代码槽位对应一个字节，完整覆盖由 `OptionalHeader.SizeOfCode`所定义的代码区域（通常为 .text 范围）。表中每个条目均对应相对于 `BaseOfCode`的固定 16 字节块。

随后，加载器遍历 "ntdll.dll" 的导出表。对于每个名称以 "Nt" 开头的导出函数，解析对应 syscall stub 的虚拟地址，并据此计算槽位索引：slot\_idx = (FuncVA - BaseOfCode)/16

该索引用于标记槽位策略表中的对应条目。所有 Nt\* stub 被赋予默认策略，而下列选定函数则被显式标记为特殊策略：

* `NtTraceEvent`
* `NtTraceControl`
* `NtAlpcSendWaitReceivePort`

最终结果是对相关 syscall stub 完成数据驱动的分类，且不对 "ntdll.dll" 的可执行代码做任何修改。生成的槽位策略表如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgwzPNbp3y0pDfvnIKhvAgjndp6xQx0NyXcvZ4aIiaAumQmDpfT62hgDow6ZA7EvFhIsHyaiaoAm78icXVXdECUCaH5SuYWTvsUJI/640?wx_fmt=png&from=appmsg)

图 3b. 槽位策略表。

实际的加载器函数远比上述复杂，并融入了额外的混淆技术，例如运行时基于哈希的 API 解析。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShVpBk2qpLoBcqE3REiaUrqOIsHn3HjUZYMGyCUuHNpl7CnHndL6w1IunE1cDWSvGmnfH2onbEdicrf7N8wg1icSvbrfPia61F9ia00/640?wx_fmt=png&from=appmsg)

图 4. 依据 "Nt" syscall stub 函数填充槽位策略表。

完成表格构建后，样本动态解析 `ntdll!LdrProtectMrdata`（详见后续章节），并调用该例程将 `.mrdata`节的保护属性修改为可写。该节包含异常分发器回调指针及其他关键运行时数据。

节权限变为可写后，加载器便用其自定义异常处理程序覆写分发器槽位。此后，每当异常被触发，该例程便会被执行。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgicn7Gxzoe2dbPdSGYtHMuJriaaR5FJ3JjciciaNcbY9TKwqUawoTKRdBhs0Sy5gTpWOInuATdr9YWFS7TwYHTiaIDR7hBU5JeJc4Q/640?wx_fmt=png&from=appmsg)

图 5. 覆写异常处理程序分发器槽位。

### 运行时异常处理

该函数主要执行两项任务：处理断点异常与单步异常。

对断点异常（0xCC）的处理相对简单：仅在 INT3（0xCC）之后紧接的指令处恢复执行。Talos 尚不确定采用此方式的原因。它可能作为针对弱分析系统的轻量级反模拟、反分析或反沙箱机制；也可能为更高级的反调试技术奠定基础；或者为类似第 2 阶段和第 3 阶段中所观察到的基于 VEH 逻辑的未来控制流操控做准备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjYyxoDJlGDwCPvknztQvLuKVTbYFLaFlugMjURk8nNyhfLuHQ7rQso48DCHJYZpX7lgicvEmzBFMnIqjWKHFKZ930fmIJRnIsw/640?wx_fmt=png&from=appmsg)

图 6. `hook_function_ExceptionCallback`函数的断点逻辑。

函数的单步部分则复杂得多，这正是前文介绍的槽位策略表发挥作用的地方。`ctx->ntstub_class_map`指向初始化期间分配的映射缓冲区。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjNEIAVzqvgqzTCtemPdMEMW1gjQfOb1UOJ7M4jLdeO83b2DLnA4DIn7McgvBvF6NYT0Dricl14zibrW7iceicuuXlSKx7JibQgC9yA/640?wx_fmt=png&from=appmsg)

图 7. `hook_function_ExceptionCallback`函数的单步逻辑。

简化后，初始化与分发函数的逻辑以伪代码表示如下。`InitCtxAndPatchNtdllMrdataDispatch`为初始化函数，`hook_function_ExceptionCallback`为上文提及的分发函数。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShCvqPUpPsDjDQptURIUiatM7XG17sSzRbltcx2tEGh7xQmulJZfn5y2k6QXesdxM2grsWib7cicvBWBEqIDIAGXvjuiardyh1BU9I/640?wx_fmt=png&from=appmsg)

图 8. 简化的单步 SEH 逻辑。

图 7 中展示的 `find_syscall`例程实现了一种系统调用恢复技术，详见下图。该例程在 "ntdll.dll" 中进行双向扫描，以定位完整的系统调用 stub，并识别可复用的相邻系统调用。

简化后的逻辑如下：

* 通过双向扫描间接确定目标系统调用号。
* 定位一个干净的相邻 stub。
* 手动将正确的系统调用 ID 加载到 `eax`中。
* 使用 syscall 指令直接切换到内核模式（即使用位于干净相邻 stub 内的 syscall 指令）。

通过复用相邻系统调用的 stub 来调用目标系统调用，加载器在不修改被 hook 代码本身的前提下，绕过了 EDR hook 的系统调用。Windows 内核仅校验 `eax`中的系统调用 ID，而不验证是哪个导出 API 函数发起了该调用。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiap8yFnbreborUcqZmDk2Qtb3V8ucYSfoaL0tOtJlFgpvia7Zznd5Jkdy09sCVatgSrp468X92zEIRz55CfEibTacyVwr1ePfABc/640?wx_fmt=png&from=appmsg)

图 9. Halo's Gate：`find_syscall`函数。

如前所述，恶意软件的实际代码远比此复杂（例如，前文提及的 `ntdll!LdrProtectMrdata`运行时解析）。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShmdIp9AAoxGNnD1allQBdVRph2kjnWC8iaBTibIGticZH0xdZpZLgt9oKoiaqSmmh4j5s64dafffcRWVScu6icekpub50ibmmbJmmgA/640?wx_fmt=png&from=appmsg)

图 10. `ntdll!LdrProtectMrdata`的运行时解析。

加载器以隐蔽的方式解析 `ntdll!LdrProtectMrdata`函数，并非通过名称或 hash 来解析 `LdrProtectMrdata`，而是采取如下步骤：

* 在 "ntdll.dll" 映像中定位 .mrdata 节；
* 检查当前分发器 slot 指针（`dispatch_slot`）是否位于 .mrdata 内；
* 若是，则以一个已知的 ntdll 导出函数（`RtlDeleteFunctionTable`，通过 hash 定位）作为锚点；
* 从该锚点起扫描 CALL rel32 指令（0xE8），并提取其目标地址；
* 该调用目标即为 `LdrProtectMrdata`的地址，并存储到 `ctx->LdrProtectMrdata`中。

前面描述的初始化例程还包含若干基本的反调试措施。例如，它会验证 `KiUserExceptionDispatcher`上是否设置了断点——若检测到此类断点，进程将被故意崩溃。此检查在分发器被覆写之前执行，这意味着由此产生的异常将由原始的默认异常处理程序负责处理。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjORLapTI8bcgFkQg2vsYg9SDNPlARGGPVwjQfbh5B9IZricUlrBeBDaCnbqJyXIPQSGb4TZYW0aszXPd4v9ibmwribAtvfoCQWQ0/640?wx_fmt=png&from=appmsg)

图 11. `KiUserExceptionDispatcher`断点检查。

加载器还实现了地理围栏功能，排除了配置为前苏联国家常用语言的系统。此检查在早期阶段执行，若检测到排除列表中的区域语言，加载器将立即终止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaxs0ticeqEBpmmhejbLqjpcEP5EKAtZ2etDzVsCNvgr2au4lPsCdy6UeOicIjqCquTibF6D8c8OKBAfmibFrUcIptLeDibSyhRS4Eg/640?wx_fmt=png&from=appmsg)

图 12. 地理围栏函数。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgCMjnl0fvnHLRRkAFPG1cz5AEo8YCSB5PZZXeS8V12XDGezxZPq5w6icul3Y4ZLgp7zE2k46QDD0MZmvNIxvCGicYB90UCB1FOM/640?wx_fmt=png&from=appmsg)

图 13. 地理围栏排除国家列表。

完成第 1 阶段初始化后，加载器继续解包后续阶段。它创建一个由分页文件支持的节（section），并将该节的两个视图映射到进程地址空间中。此方面未做深入分析；然而，创建同一节的两个视图是恶意软件用于隐藏可读写可执行（READ-WRITE-EXECUTABLE）内存区域的常见手法。通常，其中一个视图仅配置为 WRITE 访问权限，从而掩盖底层节的有效可执行权限。该共享内存区域在解包后将包含后续的恶意软件阶段，同时也使分析过程中的内存转储更加困难。当虚拟内存页当前不在 RAM 中（present 位已清除）时，访问该页会触发缺页中断，内核随后负责解决（例如，将页面从页面文件加载到物理内存中）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgj9TsWSNH82TwiaibeHrb5Pic3j9cibUUOiaW1vdkJnprWicKOYHNtYOvON6dta1IDia2uhh3cwicI69iceFCoGMfEEoK3BHXIw91aKHvo/640?wx_fmt=png&from=appmsg)

图 14. `CreateFileMappingA`解析函数，返回句柄 0x174。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjpPXXjD7ByVddGtaNxG4myebp5vYI7Wd4BajcgsKvoGVdJ63OSfdKnmJQsutiaAZMjm6ic1cVibv1gbx8JXNlV0RfLb3ic07NKsicM/640?wx_fmt=png&from=appmsg)

图 15. 第一个“只写”视图，`FILE_MAP_WRITE`（0x2）。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaRV7e8fK0ko2uuHDLKW13SHgACm2XIreBe8O6zgibHAoYCE3KeXPXQpyv7zQNVvlLqYqr87bsN3ia1noKCsZsDFdlSED6mEhw6M/640?wx_fmt=png&from=appmsg)

图 16. 第二个“R-W-X”视图，`0x24 = FILE_MAP_READ (0x4) | FILE_MAP_EXECUTE (0x20)`。
...