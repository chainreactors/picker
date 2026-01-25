---
title: 逆向分析微软签名的 Rootkit：Netfilter.sys 与 WFP 流量重定向
url: https://mp.weixin.qq.com/s/HSoOtspTl_tjQBAEk4keWg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:15.445207
---

# 逆向分析微软签名的 Rootkit：Netfilter.sys 与 WFP 流量重定向

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtGRgThK11nUfcSZxczPqbvAb0OnTibBTKrXQOcgBnP4IhSxGmhqhOC9w/0?wx_fmt=jpeg)

# 逆向分析微软签名的 Rootkit：Netfilter.sys 与 WFP 流量重定向

splintersfury
splintersfury

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://threatunpacked.com/2025/10/07/reversing-a-microsoft-signed-rootkit-the-netfilter-driver/ | splintersfury |

对 Netfilter.sys 的一篇详细技术剖析：这是一个恶意内核驱动，却通过 Attestation Signing 获得了 Microsoft 的合法签名。本文将拆解该 rootkit 如何利用 Windows Filtering Platform (WFP) 进行隐蔽的 IP 重定向、其 C2 通信机制，以及事后 Microsoft 如何强化了驱动签名流程。

## 为什么我要拆解这个驱动

在研究攻击者如何在现代 Windows 上绕过 Driver Signing Enforcement (DSE) 的过程中，我碰到了一起 2021 年的案例：一个名为 Netfilter 的恶意驱动，竟然被 Microsoft 合法签名。签名流水线在现实世界里“翻车”的例子非常有意思。我们来把它逆向一遍，看看威胁行为者是如何混过去的，并总结 Microsoft 之后又收紧了哪些环节。

## 一个恶意驱动如何获得 Microsoft 的背书

### Attestation Signing 入门 (过去的“快车道”)

Windows 要求内核驱动必须带有 Microsoft 签名，才能在开启 DSE 的情况下加载。厂商通常通过 Windows Hardware Compatibility Program (WHCP) 提交，并运行全面的 HLK 测试。2015 年，Microsoft 引入了 Attestation Signing：这是一条更快、更自动化的通道，针对非 PnP 或小众驱动可以跳过 HLK。厂商上传一个 CAB，自动化扫描器会查找明显的恶意行为，然后 Microsoft 返回已签名的 CAT + 重新签名过的二进制文件。

### 2021 年 6 月出了什么问题

威胁行为者创建了一个看起来“合法”的 Hardware Developer Program 账号 (EV 证书 + 公司身份)，并通过 attestation 门户提交了 Netfilter.sys。该驱动的恶意逻辑非常隐蔽 (它注册为 Windows Filtering Platform 的 callout 并重定向 IP；没有明显的 shellcode)。自动化检查没有命中任何问题，于是门户为其签名并盖章。随后，这个“已签名的恶意软件”在中国游戏圈被观察到，G DATA 发出警报。Microsoft 确认这是一次误签，并吊销了合作伙伴账号与相关哈希。

### Microsoft 的清理动作与新规则

2021 年 6 月 — Microsoft 通过 Defender 封禁该驱动、暂停 dev-center 账号，并表示后续将“完善合作伙伴访问、验证与签名”流程。

2023 年 3 月 — Microsoft 宣布：Attestation Signing 签名的驱动不再允许面向零售用户发布到 Windows Update。想要大范围分发的厂商必须走完整的 WHCP release-sign 路径 (通过 HLK 测试)。

2024–2025 年 — 进一步调整：预生产签名被拆分到单独的 CA；合作伙伴必须重新关联 EV 证书；任何可能触达零售受众的内核驱动会引入额外的人工审查。

结论是：Netfilter 事件基本关闭了大多数公开驱动的“快车道”，attestation 如今更多只能用于测试；而面向零售发布的版本将接受更严格的人工与自动化审查。

## 逐步拆解 Netfilter

名称：`netfilter.sys`

MD5: `916ba55fc004b85939ee0cc86a5191c5`

SHA-1: `8788f4b39cbf037270904bdb8118c8b037ee6562`

SHA-256: `115034373fc0ec8f75fb075b7a7011b603259ecc0aca271445e559b5404a1406`

类型：`Driver64`

### DriverEntry: 标准初始化，但暗藏变化

**(这一部分从表面看基本无害，非常符合许多 WFP 驱动的典型套路。)**

在 IDA 里打开驱动 ➜ 直接跳到 `DriverEntry`。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtaP1K0tT2gIbgicrf0zuZuVbhibknlvxRAlQxE9j4gmkbYicVgoXYNsKOg/640?wx_fmt=png&from=appmsg)

* **导入与框架绑定：**
* **组件初始化：**
* `InitializeDriverComponents(&driverConfigObject)`

  会遍历每个组件，并为每个组件调用 `WdfVersionBindClass`。
* 如果初始化 (`InitializeDriverComponents`、`FinalizeInitialization`或 fallback init) 失败，`CleanupComponents`会调用 `WdfVersionUnbind`/`WdfVersionUnbindClass`来干净地回滚。这个错误处理也很常见。
* **Driver Unload 挂钩：**
* `DriverUnloadHook`

  确保会调用自己的 `CleanupComponents`函数 (以及任何原始的卸载例程)。这是确保资源释放的标准做法。
* **提示网络活动的初始导入：**

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtjibsTXgWiaMyIJm3AjogpQ54kn6sORzOBzZeQaqXlUIEDrWOmtb1o40w/640?wx_fmt=png&from=appmsg)

* `FwpsCalloutRegister1`

  、`FwpmEngineOpen0`等 `Fwpm*`/`Fwps*`函数 (Windows Filtering Platform) 的出现，清楚表明该驱动打算与网络栈交互。许多合法的安全产品与网络工具都会使用 WFP。
* `IoCreateDevice`

  与 `IoCreateSymbolicLink`之类的调用 (出现在 `SetupNetworkFilter`调用的 `InitializeDriverResources`中) 对需要从用户态访问的驱动来说也很标准。

截至 `DriverEntry`的这一阶段，它的行为都符合“要做网络过滤”的驱动：逻辑主要围绕初始化、框架绑定，以及保证正确清理。

### 回退路径：InitializeFallback

即便在 `DriverEntry`中已经尝试了标准的 WDF 绑定与组件初始化，这个驱动仍然总会落到这条回退例程：

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtFx4coCsdSMfR1l07hcLYI5ylTChu0zKcPC9wUfNGCPJ3DwCcgFaLvw/640?wx_fmt=png&from=appmsg)

* **什么时候调用 `InitializeFallback`?**

  在 `DriverEntry`中 `InitializeDriverComponents`与 `FinalizeInitialization`之后无条件调用——不管前面的步骤成功还是失败。在极少数 `DriverObject`为 null 的情况下，它会被直接调用。
* **为什么这很重要：**

  无论其它环节失败与否，驱动都要尽量拉起它的 **网络过滤核心**。这种“最后一道防线”的执念说明 **拦截网络流量是它的最高优先级**——即使处于降级状态也一样。

### 网络过滤初始化：SetupNetworkFilter

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtLB1YbaUTSjFw2kzJ2zaIoIyiadvKjtRXDBMdPrd0bWNu1oddNibXm5UQ/640?wx_fmt=png&from=appmsg)

在 `SetupNetworkFilter`内，驱动为其网络操控能力打地基：

* **全局配置：**

  ```
  ConfigureFilterGlobals(0, (__int64)"NET_FILTER", 1, 1);
  // Sets g_FilterName = "NET_FILTER", g_CreateDevObj = 0, g_FilterFlagA = 1, g_FilterFlagB = 1
  ```
* 该函数设置了一些全局名称与标志位。`L"NET_FILTER"`变成了一个全局标识符。
* **条件启动：**

  ```
  if ( ShouldStartFilter() )
  // ShouldStartFilter() calls QueryServiceControl(), which likely checks a registry value or external trigger.
  // The result is cached in g_ShouldStartCached.
  ```
* 驱动会检查它 *是否应该*启用过滤。这提供了一个控制机制，可能由 C2 或注册表配置触发。
* **设备对象创建：**

  ```
  SetDeviceAndSymbolicNames(L"\\Device\\netfilter", L"\\??\\netfilter");
  ```
* 创建一个 `\Device\netfilter`设备和一个 `\??\netfilter`符号链接，使用户态应用能与其通信 (例如发送配置或接收数据)。这对很多驱动来说是标准操作。
* **Windows Filtering Platform (WFP) 注册 (“隐蔽”恶意逻辑的核心):**

  Windows Filtering Platform (WFP) 是 Windows 中一套强大的 API 与系统服务，为应用与驱动提供拦截、修改网络流量的基础设施。它是许多网络安全特性的骨干 (包括 Windows Firewall)，也被大量第三方防火墙、入侵检测/防御系统、VPN 客户端与网络监控工具使用。

  **WFP 如何工作 (简化版):**

  WFP 很重要，因为它为内核态组件提供了一条有文档、受支持、相对稳定的路径来与网络栈交互，避免使用直接 NDIS hooking 这类不受支持且可能导致系统不稳定的技术。

  *(如果想深入了解 WFP 架构与开发，可以阅读 zeronetworks 的这篇文章*https://zeronetworks.com/blog/wtf-is-going-on-with-wfp)

  下面我们看看 Netfilter.sys 如何利用这个“合法”的平台：

1. **Filtering Engine:**

   WFP 的核心组件，用于将网络 packet 与已注册规则进行匹配与处理。
2. **Layers:**

   WFP 在 TCP/IP 栈的不同位置定义了特定“层”(例如 IP packet layer、transport layer、用于连接建立的 Application Layer Enforcement (ALE))，过滤可发生在任意层。
3. **Callouts:**

   由第三方驱动 (如 Netfilter.sys) 实现的函数。当 WFP engine 处理到匹配某条与 callout 关联的 filter rule 的流量时，就会调用该 callout 函数。
4. **ClassifyFn:**

   callout 内的主函数。它接收 packet/connection metadata，并决定返回 `PERMIT`、`BLOCK`或 `CALLOUT_ACTION_CONTINUE`(交给权重更低的 filter)。关键点在于，它还可以请求对 packet data 的可写访问，以便修改数据。
5. **Filters:**

   规则本体。filter 会指定条件 (如 IP 地址、端口、协议、方向)，并把自己关联到某个 layer 与 sub-layer 上的特定 callout；同时定义 action (例如调用 callout、permit、block)。
6. **Sub-Layers:**

   用于在同一 WFP layer 上对多个 filter 做排序与仲裁，保证处理顺序可预测。

* `EnsureFrameworkInitialized()`

  : 很可能用于确保基本的 WDF 结构已经就绪。
* `RegisterFilterContext()`

  : 通过 WDF 提供的回调获取并保存驱动的 WDF device context。
* `InitializeContextFromHandle()`

  : 一次性完成 WFP engine handle、transaction、callout 与 filter 的初始化：

  ```
  1. OpenWfpEngine() 调用 `FwpmEngineOpen0` 获取 Windows Filtering Platform 的 handle。

  2. BeginWfpTransaction() 调用 `FwpmTransactionBegin0`，使随后的 WFP 变更作为一个可回滚的整体进行。

  3. RegisterCalloutFunctions()

      填充一个 `FWPM_CALLOUT` 结构体：

      - `classifyFn = (FWPS_CALLOUT_CLASSIFY_FN1)ClassifyCallback`

      - `notifyFn = (FWPS_CALLOUT_NOTIFY_FN1)NotifyCallback`

      - `flowDeleteFn = (FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0)FlowDeleteNoOp`

      - `calloutKey = {GUID}` 用于标识该驱动的 callout。

          通过 `FwpmCalloutAdd0` 提交。

  4. **AddCalloutAndFilters()**

      - **FwpmSubLayerAdd0**: 创建一个自定义 sub-layer (GUID `{2921234954u,50698u,…}`)，用于对 filters 做排序。
      - **FwpmFilterAdd0**: 插入一个 terminating callout filter:

      ```c
      filter.layerKey     = {IP_PACKET-or-ALE_AUTH_CONNECT GUID};
      filter.subLayerKey  = customSubLayerKey;
      filter.action.type  = FWP_ACTION_CALLOUT_TERMINATING | FWP_ACTION_FLAG_CALLOUT;
      filter.action.calloutKey = calloutKey;
      ```

      这会强制把匹配的流量送进 callout 例程，并让它的裁决成为最终结果。

  5. CommitWfpTransaction()

      调用 `FwpmTransactionCommit0` 应用全部变更；如出错则回滚。
  ```
* **g\_ContextInitSucceeded**

  仅当上述每一步都返回成功时，这个全局标志才会被置为 true。
  > **WFP 的良性用法：**注册 callout 与 filter 正是防火墙、网络监控工具 hook 网络 I/O 的方式。**恶意之处：**这里不是用于防护，而是用于“无形地”重定向流量并支撑 C2 通道，利用标准 OS API 来尽量躲在雷达之下。
* **工作线程创建：**

  ```
  if ( regStatus >= 0 && StartFilterDevice(DriverObject) ) // StartFilterDevice likely finalizes WDF device operations
  {
  AllocateWorkItem(&g_WorkItem); // Initializes a KEVENT for synchronization
  return (unsigned __int8)CreateSystemThread(&g_WorkerThreadHandle, FilterWorkerThread) != 0;
  }
  ```
* 如果 WFP 初始化全部成功，就会创建一个内核工作线程 (`FilterWorkerThread`)。这个线程将负责 C2 活动。

## `FilterWorkerThread`中的隐蔽 Beaconing 与 C2 功能

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtFtWBSkK8HM4covQhnvR1yibIbu9a3QvauFDAQTwTZTibAE8XdbS1YbicQ/640?wx_fmt=png&from=appmsg)

...