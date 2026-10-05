---
title: Black Hat USA 2026：AFD跨驱动信任链
url: https://mp.weixin.qq.com/s/kgClyHNF1MIZHAiKptre9g
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:26.017101
---

# Black Hat USA 2026：AFD跨驱动信任链

# Black Hat USA 2026：AFD跨驱动信任链

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Windows 内核漏洞工厂：AFD 跨驱动信任链

> Black Hat USA 2026 议题笔记：Vulnerabilities Assembled! The Vulnerability Factory Inside the Windows Kernel

Windows 内核里最难处理的一类漏洞，并不一定藏在某个显眼的越界读写中。单看每个函数，它们可能都在做合理的事：AFD 根据套接字状态打开下层传输设备，I/O Manager 解析对象名，低层驱动接收内部 IOCTL，Object Manager 把内核对象转换成用户句柄。问题出在这些动作被跨阶段组合后，安全属性没有一起传递。

Angelboy 的公开课件以 `afd.sys` 为中心，解释了一个很有价值的审计视角：不要只问“这个 IOCTL handler 有没有校验长度”，还要问“谁选择了下游对象、对象身份是否会变化、下游为什么相信请求来自内核、最终句柄以谁的访问模式创建”。当四个问题同时出现缺口，一组看似互不相关的 Windows 组件就可能被组装成稳定的逻辑提权链。

![议题课件封面](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP8534joB7F94MbkgwvI48uiahXTV3CvIjgYD9KhqApk3XdO3XBc0UjK0dkmpftfDRJFowdfibpv1YAkIP49Sykc4jICNHckpkia0xOs/640?from=appmsg)

*图 1：研究重点不是单一内存破坏点，而是 AFD 与多个内核组件之间可组合的信任关系*

本文基于公开课件复盘其工程含义，侧重防守方如何审计驱动、建立跨层不变量和补充遥测。涉及提权的部分只描述必要机制，不提供可直接运行的利用程序、对象重解析脚本或 DLL 劫持载荷。

## 1、三次修补同一问题，说明缺失的是不变量

课件从三起已在野利用的 AFD 漏洞开始：CVE-2024-38193 的问题位于 `AfdConnect`，2024 年 8 月修复；半年后，CVE-2025-21418 可从 `AfdAccept` 绕过先前修复；又过三个月，CVE-2025-32709 经 `AfdSuperAccept` 触发同一底层问题。

![三起 AFD 在野漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP850icNpMia0pbtyHUqsyG74K9LbJ4bWkmpoWcXZ2VicGkjUCAMRQT1SicNpX6GOBakP6pBenQicjhGjVFo2RPUJ8haMRa3Xn5GicaAKdE/640?from=appmsg)

*图 2：一年内出现三起 AFD 在野漏洞，后两次都与前一次的根因和修补边界有关*

![AfdConnect 中的首个问题](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850Qgk6P9BP5iayrnicPWHQ3KyNSBqtY8yUL2DpTOibvMua2YNAR3G5h6B0aFP5wVlaYyict0wTAMgRwIOCjz82E2XeVDtZzFMjlCR8/640?from=appmsg)

*图 3：CVE-2024-38193 来自 `AfdConnect` 路径缺少验证，并导致 Use-After-Free*

![AfdAccept 绕过修复](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852a0LdhOl0PHCWhwUxqMA2ibGDVyeuMmfI1UgaibDWp6CZOV65rSsThgDDo5tOdGrQ4eh7kKPibW2fvoFibrZuGibkliasGzPdPFpo6M/640?from=appmsg)

*图 4：CVE-2025-21418 通过另一条入口到达相同底层状态，说明入口级补丁没有覆盖系统不变量*

![AfdSuperAccept 再次绕过](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850a1S9iaCuPjsmVTyay7xrsQLxSUEdVsO1MskibVVm4LHwkicRlYs16aZhpj5Ce7PJduibuRDdwKLpIlaljmXUNfqFrhM2y9CG0gqg/640?from=appmsg)

*图 5：第三条入口再次击中同类问题，暴露的是状态机级别而非单个函数级别的缺口*

这类修复失败常见于大规模内核代码。开发者在一个调用点加入引用计数、状态判断或访问检查，但同一对象还能从另一个入口进入相同消费函数。补丁在代码层面是正确的，在系统层面却不完整。

审计时应先把约束写成不依赖入口函数的不变量，例如：

text

```
Invariant A：只要连接对象可能被异步使用，就必须持有有效引用。 Invariant B：所有进入同一状态迁移的入口，执行相同的前置校验。 Invariant C：传输对象一旦绑定，其对象身份和安全属性不得被名称重解析改变。 Invariant D：源自用户态的请求，跨驱动转发后仍按 UserMode 做访问检查。 Invariant E：返回用户态的句柄，其权限不得高于原始调用者可直接获得的权限。
```

相应地，补丁 review 不该只看修改过的函数，而要找同一状态迁移的全部 producer：

powershell

```
# 防御性代码审计示例：列出可能进入连接/接受状态的入口与公共后端。$Symbols = @(   'AfdConnect',   'AfdAccept',   'AfdSuperAccept',   'AfdCreateConnection',   'AfdIssueDeviceControl' )  foreach ($Symbolin$Symbols) {   rg --line-number--glob'*.{c,cpp,h}'$Symbol'.\driver-src' }
```

真正要验证的是：这些路径是否在同一个、无法绕过的 helper 中执行检查；检查失败后对象状态能否回滚；异步完成例程是否仍持有引用。把同一段 `if` 复制到三个 dispatch 函数，只会为第四次绕过留下空间。

## 2、AFD 不是普通网络驱动，而是传输设备的调度层

`afd.sys` 是 Winsock 的内核入口。用户态看见的是 socket、bind、connect、send；AFD 看到的则是 endpoint、connection、address file、transport provider 和一系列内部设备控制请求。它自己不是 TCP/IP 协议栈，而是把操作翻译并转交给 `tcpip.sys`、`tdx.sys`、`hvsocket.sys`、`rfcomm.sys` 等下层组件。

![AFD 与连接对象](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852EoOsd68BKstiba8K85dY9usZc43kgOUYjOPLaDrtzvFNpiaBFkEw1ZkunxoaYem4aDKCISd3qHQShficFVwnxJoLhaZLj9zSZgc/640?from=appmsg)

*图 6：AFD endpoint 保存地址对象和传输信息，连接操作再通过文件对象与句柄向下层发请求*

课件将创建 socket 的传输选择分成三类：

* TLI 模式只提供地址族、类型和协议，由 AFD 选择 AF\_UNIX、TCP/IP 或 Hyper-V Socket 等 provider；
* Hybrid 模式由调用者给出与参数兼容的 TCP、UDP、Raw IP 设备路径；
* TDI 模式允许提供更自由的传输路径，例如 RFCOMM 或 PGM 设备。

AFD endpoint 中至少有三组字段直接参与后续安全决策：状态、`TdiServiceFlags`、`AddressFileObject/AddressHandle`，以及 `TransportInfo->TransportDeviceName`。可用简化结构表示：

c

```
typedefstruct _AFD_ENDPOINT_VIEW {     ULONG State;     ULONG TdiServiceFlags;     PFILE_OBJECT AddressFileObject;     HANDLE AddressHandle;     PTRANSPORT_INFO TransportInfo; } AFD_ENDPOINT_VIEW;  typedefstruct _TRANSPORT_INFO_VIEW {     UNICODE_STRING TransportDeviceName;     ULONG AddressFamily;     ULONG SocketType;     ULONG Protocol; } TRANSPORT_INFO_VIEW;
```

这些字段不是普通元数据。`TransportDeviceName` 决定请求交给谁，`TdiServiceFlags` 可能影响访问检查模式，`AddressFileObject` 又能在后续被转换成用户句柄。也就是说，AFD 同时承担路由、状态和授权语义；如果三者没有绑定在一个不可变对象上，攻击面就不再局限于公开的 AFD IOCTL。

## 3、只审计 AFD\_IOCTL，会漏掉真正的跨层入口

传统 AFD 审计通常从 `AfdIrpCallDispatch`、`AfdImmediateCallDispatch` 开始，逐个检查 `AfdBind`、`AfdConnect`、`AfdPoll`、`AfdQueryHandles` 等处理函数。这当然必要，但它默认了一个前提：漏洞一定在 AFD 消费用户缓冲区的地方。

![传统 AFD 攻击面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850aMd0EEjK8EFKbjpcYk35eJuN7Ks3KopqYicVHd8Lsfvp59pqlAwd1tWXbPfEIX7IP9Puazib7OlSno5NRnBNK5iakL0jiaIOKof8/640?from=appmsg)

*图 7：已知审计面集中在 AFD 的 IOCTL 分发函数，容易把下游驱动视为实现细节*

课件给出的反例是：低层传输驱动经常假设输入已经由 AFD 验证。对于内部 IOCTL，这种假设并非完全不合理——调用者通常确实是另一个内核驱动。但“请求来自内核组件”和“请求中的每个字段都可信”不是一回事。

![低层驱动信任上游](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850siaQwhH7mUHZwAiaXt7eIn8B5KQia6IQn6UMgKib0Fry2aJbwCoyEy6LzU526wthic1PR4aX7kAs2eqpT1ymNZe1PQxDRicVofDEibI/640?from=appmsg)

*图 8：`tdx.sys`、`tcpip.sys`、`rfcomm.sys` 等下层组件往往把 AFD 当作可信 producer*

研究者沿着这条边界发现多组漏洞：`tdx.sys` 的 CVE-2025-49658、CVE-2025-49659，`tcpip.sys` 的 CVE-2025-54093，以及 `rfcomm.sys` 的 CVE-2025-59513。CVE-2025-49659 的调用链从 `afd!AfdFastDatagramSend` 到 `tdx!TdxSendDatagramTransportAddress`，下层存在固定尺寸假设。

![低层传输驱动漏洞清单](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853hfYc4cORlFgdW0Ea84sevUW9usxa5Jepjy9U8TBmZyq7BwMyQyv4d8tcRia1LgxYIaOVjPGaW0znLYQtEEvEnPcKkKwaeFoiao/640?from=appmsg)

*图 9：同一上游验证假设在多个 transport provider 中产生了独立漏洞*

![固定尺寸假设](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850TBWDxHwFT4NIPwbc0zDz5LUhwtVaD9icXLDxDC5G2dMttia3bibiadjMnYTK9zBxrZEzhhCxubWq6rKL4t6z43rkZF8rn83N4ePU/640?from=appmsg)

*图 10：当变长地址结构进入固定尺寸消费逻辑，问题已不在 AFD 的公开 handler 内*

驱动接口应把“内核调用者”与“可信输入”分开。即使是 `IRP_MJ_INTERNAL_DEVICE_CONTROL`，消费端也要验证长度、类型、枚举范围、嵌套偏移和对象归属：

c

```
NTSTATUS ValidateTransportAddress(     _In_reads_bytes_(InputLength) constvoid *Input,     _In_ size_t InputLength,     _Out_ const TRANSPORT_ADDRESS **Address) {     if (Input == NULL || Address == NULL ||         InputLength < sizeof(TRANSPORT_ADDRESS)) {         return STATUS_INVALID_PARAMETER;     }      const TRANSPORT_ADDRESS *ta = Input;     if (ta->TAAddressCount == 0 || ta->TAAddressCount > MAX_TA_COUNT) {         return STATUS_INVALID_PARAMETER;     }      if (!AllVariableEntriesFit(ta, InputLength)) {         return STATUS_INFO_LENGTH_MISMATCH;     }      *Address = ta;     return STATUS_SUCCESS; }
```

关键不是这段样例是否覆盖全部 TDI 结构，而是消费驱动不能把“AFD 调过我”当成类型证明。所有跨驱动缓冲区都要按 hostile-but-well-formed 的输入处理。

## 4、把 transport 换成意外设备，攻击面就从函数变成组合

接下来问题发生了变化：如果 socket 所选的 transport 不是设计者预期的 TCP、UDP 或 RFCOMM，而是另一个恰好接受相同内部请求的设备，会怎样？

![意外的传输设备](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853QicteOg4tHNwAicWKdDD3clG3ULPicJynQHU8iaicTdOGLBuVOGCUOG57tu9E2YT4m7K1bGtt8Hvliaqu7xLNUfN6ibia7B0zj3SKhtc/640?from=appmsg)

*图 11：AFD 的可达面不只由自身 IOCTL 决定，还由可被选中并接受请求的设备对象决定*

这不是简单的“任意设备可打开”。组合成立至少需要四个条件：

1. 用户可影响 AFD 保存的传输名称或其解析结果；
2. 目标设备允许在当前命名空间和令牌条件下被解析；
3. AFD 在 bind/connect 阶段用足够高的权限打开该对象；
4. 后续操作把目标对象按原传输协议继续使用，或把它转换成用户可用句柄。

因此，攻击面清单不应只列 IOCTL，而应列“状态 × provider × 阶段 × 对象类型”的笛卡尔积：

yaml

```
afd_composition_matrix:states: [created, bound, connected, listening]   transport_modes: [tli, hybrid, tdi]   phases:-create_transport-create_address-create_connection-relay_internal_ioctl-export_handlesecurity_properties:-canonical_object_identity-requestor_mode-desired_access-force_access_check-object_type-creator_token
```

对每一个组合，审计者要核对对象类型是否符合预期、名称解析是否只发生一次、权限是否来自原始用户令牌，以及低层收到的结构是否由当前 provider 定义。课件在 NetBT 与 NDIS 的组合上给出了具体结果，包括 CVE-2025-55230、CVE-2025-47996、CVE-2025-55679 和 CVE-2025-55339。

![跨驱动组合发现的漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP851G5DiaDpGN2vzz8QV7ffMBia6pyo5iaAUlibb2R5mIpfr4bibbMufgFfNbkQSfGRbGdAvMpPLicTT9y16kpXIVAAE0EK5bhAfA8te54/640?from=appmsg)

*图 12：NetBT 和 NDIS 不是传统 AFD handler，但能通过 transport composition 进入同一攻击面*

## 5、RequestorMode 丢失后，内核代理替用户获得了权限

NDIS 组合暴露了 Windows 驱动审计中一个经典问题：access mode mismatch。创建特定 socket 时，endpoint 的 `TdiServiceFlags` 可以为 0；绑定阶段，AFD 调用 `IoCreateFileEx` 打开下层对象，却没有带 `IO_FORCE_ACCESS_CHECK`。

![缺少强制访问检查](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853360UFbTdEC0J1uYZV9VNLXmwia...