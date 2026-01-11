---
title: PatchGuard Peekaboo：在启用 PatchGuard 的系统上隐藏进程 (2026)
url: https://mp.weixin.qq.com/s/U66LwrTqhwSy4ptibZ8qwQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:19.499042
---

# PatchGuard Peekaboo：在启用 PatchGuard 的系统上隐藏进程 (2026)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3icyjBbsTVkqfvQKCdqMHRcUvhjseOd9Jq65vib9y8ibTVns2QaUf3sOhA/0?wx_fmt=jpeg)

# PatchGuard Peekaboo：在启用 PatchGuard 的系统上隐藏进程 (2026)

Ksawery

securitainment

![]()

在小说阅读器中沉浸阅读

## 引言

我花了几周时间 (而且完全可能花得更久)，试图在 HVCI“盯着我喘气”的情况下，找到一种可靠的方法来拦截内核活动。我几乎尝试过的每一种方案，结局都一样：要么是干脆利落的“access denied”，要么就是瞬间黑屏，把大家最熟悉的蓝屏给替换掉。

Windows 已经不再手下留情；那些巧妙的 inline hook 和富有创意的 PatchGuard 绕过手法，基本已经结束。Microsoft 把“强制执行层”推到了普通内核驱动根本碰不到的地方。我们说的是硬件强制、hypervisor 加持的保护：“你甚至没有权限去请求权限。”

这项研究聚焦于一个明确目标：**通过操纵内核结构来让用户态枚举看不见某些进程——具体来说，是修改 Windows 用来跟踪活动进程的进程链表**。为什么要做这件事？隐藏进程仍然是 rootkit、反作弊规避与安全研究中的基石技术。让一个进程对任务管理器、系统监控工具，甚至某些安全产品不可见，可以提供强大的持久化与隐蔽能力。

问题在于，现代 Windows 并不会只检查一次这些结构——它会通过多层机制持续验证。传统 **PatchGuard**会对关键内核结构执行周期性完整性检查，但它的响应并不固定：有些违规会触发即时 bugcheck (立刻蓝屏)，而另一些会被排队，延迟并随机触发，可能在几分钟甚至几小时后才发生。这种不可预测性，让测试阶段几乎无法尽早发现违规。更麻烦的是，**Secure Kernel PatchGuard (SKPG) 运行在 VTL1，并以特权 hypervisor 视角监控普通内核**，再加上一层从 VTL0 难以检测或干预的看门狗。

本文聚焦于一个窄但可复现的问题：**被篡改的 LIST\_ENTRY 结构会在进程终止时触发 0x139 KERNEL\_SECURITY\_CHECK\_FAILURE**。目标非常简单且受限：在 VTL0 中、仅凭一个内核态驱动找到可行的绕过思路。不搞 bootkit，不搞 pre-OS 花活，只做纯粹的内核内实验。

先打个预防针：如果你期待的是一发入魂、能打穿 Windows 所有防线的“magic bullet”，那这里没有。我呈现的是一个看起来有希望的绕过方向，以及一份尚未完全展开的思路清单。这是一张快照：当你试图在 hypervisor-backed 完整性监控之下操作内核时，究竟什么是可能的，什么是不可能的。

## 第一部分：认识敌人——HVCI 与 VTL

在尝试任何内核拦截之前，我们必须理解 Windows 的 virtualization-based security 架构——它让传统 hooking 变得几乎不可能。这里的解释建立在两份深入技术资料之上：Rayanfam 的 hypervisor 系列 与 Connor McGarr 的 HVCI 深入解析。

传统的内核安全主要依赖 PatchGuard 这类软件检查；只要手法足够巧妙或技巧足够到位，理论上就能把它绕过去甚至关闭。因为 PatchGuard 的保护与攻击者的技巧，常常运行在同一特权层级——内核本身。这就形成了典型的猫鼠游戏：攻击者只要摸清实现细节就可能绕过，而 Microsoft 则以更复杂的检查、更强的反调试、更复杂的代码回应。

**Hypervisor-protected Code Integrity (HVCI)**从根本上改变了规则。它不再是“软件保护 vs. 软件攻击”的对抗，而是把整套保护机制搬到了 **一个与正常 Windows OS 并行运行的、不同的操作系统**中。这个并行 OS 与普通内核隔离，只有经过加密签名、受信任的二进制才能执行。

但 HVCI 并不是单打独斗。**它是一个更大防御生态的一部分**：

**PatchGuard (Kernel Patch Protection)**—— 原始的守门员，仍然存在于 VTL0 (普通 Windows)。PatchGuard 在运行时对内核结构做完整性检查。虽然在拥有内核权限时仍存在被绕过的可能，但它作为第一道防线，会迫使攻击者更复杂、更谨慎。

**HVCI (Hypervisor-protected Code Integrity)**—— 硬件级执行者。HVCI 使用 Extended Page Tables (EPT)，在 hypervisor 层把所有内核代码页强制设为只读可执行 (R-X)。即使你绕过了 PatchGuard 的检查并修改页表项 (PTE)，把页面标记为可写，EPT 仍会拦下写入。这不是你能用软件手段绕过的“检查”。

**HyperGuard (Secure Kernel PatchGuard / SKPG)**—— hypervisor 的看门狗，运行在 VTL1。HyperGuard 持续监控关键的 hypervisor 与 VTL1 结构是否被篡改：包括 hypervisor 完整性、EPT 结构、VMCS (Virtual Machine Control Structure)、VTL1 内存区域、Secure Kernel (securekernel.exe) 本体、VTL1 关键数据结构、函数指针，以及安全策略的强制执行机制。你可以把它理解为“守护守护者的守护者”：即便攻击者以某种方式触达 VTL1，也很难关掉这些安全检查。

### 1.1 虚拟信任级别 (VTL) —— 基础

启用 HVCI 的 Windows 运行在由 Microsoft Hyper-V 强制执行的多层安全模型之上。这不只是一个“安全开关”，它几乎重构了 Windows 的底层运行方式：在启用 HVCI 后，整个 Windows 安装以虚拟机 guest 的形式运行，即便你感觉它像是在裸机上跑。

这套架构利用 Virtual Trust Levels (VTL) 来构建隔离边界。你可以把它理解为“环中环”。传统 x86 处理器有保护环 (Ring 0 是内核，Ring 3 是用户态)。启用 VTL 后又多了一维：由 hypervisor 强制的垂直隔离。

**VTL 架构：一台机器上的两个世界**

把 VTL 想成在同一套硬件上运行的平行宇宙：VTL0 是 Windows 生活的正常世界，VTL1 是在旁边盯着它的安全世界。它们共享同一颗物理 CPU 与内存，但 hypervisor 会确保它们永远不能直接“碰到”对方。

VTL0 中的进程无法访问，甚至无法看到 VTL1 中发生了什么。这种隔离是绝对的。一个现实世界的例子是 Credential Guard 对 LSASS 的保护实现：

* **VTL0**

  ：普通的 `lsass.exe`在这里运行，照常处理认证请求
* **VTL1**

  ：`LsaIso.exe`(LSA Isolated) 在这里运行，存放真实凭据 (密码哈希、Kerberos ticket)
* **通信**

  ：VTL0 的 `lsass.exe`通过由 hypervisor 验证的安全 RPC 通道，把请求发送到 VTL1 的 `LsaIso.exe`

即使恶意代码拿下了内核，在 VTL0 获得完整 Ring-0 权限，它仍然无法从 `LsaIso`转储凭据，因为这些凭据物理上存在于 VTL1 的隔离内存空间中。hypervisor 根本不会允许 VTL0 读取 VTL1 的内存。

下面是你试图从 VTL0 调试 VTL1 进程时会发生的事：

![securekernel.exe process information](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3ic8J3L5WcthNHMRU8JfRMphnDB7iat509mV4NubhB5pWDF55KPUguk6w/640?wx_fmt=png&from=appmsg)

图 1 WinDBG 调试 VTL1 进程

![HVCI Layout](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3FS5DnLOFGqZC0Y2LpSZ6icu5VmqiaSec4NbPbgJCpsrhbGyvOWhcmW0w/640?wx_fmt=png&from=appmsg)

HVCI Layout

**硬件层**：这里是 **Intel VT-x**或 **AMD-V**所在的位置。这些是直接集成在 CPU 里的硬件虚拟化扩展。在 BIOS 中启用虚拟化，相当于给 CPU“许可”去创建隔离的执行环境。与软件虚拟化的关键差异在于：CPU 可以在硬件层面进行隔离分区。CPU 能维护多套页表、多套处理器状态，并以硬件速度在它们之间切换。

**Extended Page Tables (EPT)**或 **Nested Page Tables (NPT)**尤其关键。它们提供了第二层内存地址转换，位于操作系统页表之下。OS 可以说“这个页可写”，但 EPT 可以回答“不，它不可写”，而 OS 没有任何办法推翻这个决定。

**hypervisor 层 (Hyper-V)**：Microsoft 的 Hyper-V hypervisor 运行在所谓的 VMX root mode。这个层级比内核更高权。hypervisor 拥有硬件——它决定内核可以做什么、不可以做什么。启用 HVCI 后，Hyper-V 不只是为了跑虚拟机；它在这里的核心职责是控制并保护内核本身。每当内核试图执行带特权的操作 (修改页表、执行某些指令、访问某些内存)，CPU 都会先与 hypervisor 协商；如果 hypervisor 说不，这个操作就失败。hypervisor 的响应是法律，因为它由 CPU 硬件强制执行。

hypervisor 维护着控制内存权限的 EPT 结构。当我们说 HVCI 之下代码“只读”，意思是它在 EPT 里是只读。即使我们强行把常规页表项 (PTE) 改成可写，EPT 仍然可以拒绝写入。

![MMPTR\_HARDWARE stracture](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3AnhFUqkq43nN69gpj4k5YrmEYFUsweAWVaEGM3s2T22ss88P7qRvlg/640?wx_fmt=png&from=appmsg)

图 3 MMPTE\_HARDWARE 结构

![Setting nt!KeBugCheckEx PTE to writable. If the driver had tried to perform write operation, for e.g. to perform inline code hooking on KeBugCheckEx function, system would have crashed because EPT still marks the page as read-execute only.](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt33eZQCftqQSQKicnwQdrdS5t0A7NSm12gOjUbU1Rgfca2cdktg6fNg4g/640?wx_fmt=png&from=appmsg)

*图 4 将 `nt!KeBugCheckEx`的 PTE 设为可写。如果驱动此时尝试写入 (例如对 `KeBugCheckEx`做 inline code hooking)，系统会崩溃，因为 EPT 仍把该页面标记为只读可执行。*

CPU 的地址转换分两阶段进行：先走 guest 页表 (Windows 的页表)，再走 EPT (hypervisor 的页表)。写操作必须在两阶段都通过；只要任意一层回应“无写权限”，那就没有写权限。取决于你用什么方式去写，结果通常只有两种——access denied 或蓝屏。

**VTL1 (Secure Kernel)**：魔法发生在这里。VTL1 运行 `securekernel.exe`，本质上是一个专注安全的极简 OS 内核。它很小，只有几 MB，目标只有一个：强制执行代码完整性策略。Code Integrity 模块 (`ci.dll`) 在这里运行，连同 Secure Kernel Code Integrity (`skci.dll`)。这些组件会在驱动加载前验证签名，检查内核代码是否被修改，并强制执行“什么可以执行 / 什么不可以执行”的策略。

VTL1 在 hypervisor 层与 VTL0 隔离。虽然从 CPU 视角它们看起来处于同一层级，但从 hypervisor 视角它们是完全不同的虚拟机。VTL1 更受信任，并且可以单向访问 VTL0 的内存；反过来，VTL0 不能读取 VTL1 的内存，不能调试 VTL1，甚至无法知道 VTL1 正在做什么。VTL0 唯一能与 VTL1 通信的方式是通过受控 hypercall：本质上是请 hypervisor 把一条被严格校验的消息送到 VTL1；而 VTL1 仍然可以选择是否回应。

**VTL0 (Normal Kernel)**：这就是你熟悉的 Windows 所在之处。完整的 Windows 内核 (`ntoskrnl.exe`)、硬件抽象层 (`hal.dll`) 以及所有驱动都在这里运行。尽管这些组件知道自己运行在虚拟化之下，但 hypervisor 的存在对正常操作基本透明，使得现有 Windows 软件无需修改也能工作。

一句话总结，VTL0 像一只被关在笼子里的、完全不受信任的野兽。VTL0 对某些页面只有严格受控的访问：它可以执行内核代码，但不能修改正在执行的代码。任何写入代码页的尝试都会触发 EPT violation，导致 VM-exit 到 hypervisor，然后把违规转交给 VTL1，最终立刻 bugcheck。这个链路简单且无情：**尝试写代码 → EPT violation → VM-exit → bugcheck**。

![VTL0 locked in the cage](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3BWDYWzEVfVE1qbUemLot98Mib5GHMc92MSVWaldAX9dXdiciagqibibCEjA/640?wx_fmt=png&from=appmsg)

VTL0 locked in the cage

但所有进程的数据段在 EPT 上通常是 RW- 权限。**HVCI 不会对数据段做完整性检查**，因此在合适的位置，攻击者可以覆盖数据段中的函数 / 变量指针，从而打开一些“HVCI-safe hook”的可能性。

### 1.2 Extended Page Tables (EPT) —— 强制执行机制

EPT 是理论落地的地方，也是 HVCI 能真正生效的“执行层”。理解 EPT 至关重要，因为这就是为什么你每一次试图修改内核代码都会失败。

在传统的、非虚拟化系统中，地址转换大致是这样：

1. 程序给 CPU 一个 VA (Virtual Address)
2. CPU 在页表里查找并返回物理地址
3. 页表项包含权限位：

* 是否可读？
* 是否可写？
* 是否可执行？

4. 如果权限位与操作不匹配，就会触发 page fault

但在虚拟化场景里会出现一个问题：页表由 VTL0 控制，而 VTL0 是不受信任的。一个被攻破的内核完全可以改自己的页表，让自己拥有对代码页的写权限。为了解决这个问题，hypervisor 引入第二层转换：Extended Page Tables。

![GVA to HPA structure](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3VLheeytXj4CA27JKNTHUsB8DXUVfw7tLtee9xJSpyjG9S1Sd5VSZbg/640?wx_fmt=png&from=appmsg)

GVA to HPA structure

**把它落到具体问题上**：Windows 通过嵌入在 EPROCESS 结构中的双向链表来跟踪活动进程。当进程终止时，**内核必须把它从这些链表中解链——这项工作由 PspProcessDelete 负责**。`PspProcessDelete`是一个内部内核函数，负责清理进程对象，并把它从 `ActiveProcessLinks`链中移除。它会对 LIST\_ENTRY 做关键的完整性检查，确认它没有被破坏或篡改。如果你的驱动为了隐藏进程而操纵过这些链接，**`PspProcessDelete`会在终止阶段检测到不一致，并触发 0x139 bugcheck**。

理解 Windows 如何保护 `PspProcessDelete`这类代码非常关键。假设你的驱动尝试访问地址 `0xFFFFF80274EE1310`的内存 (假设 `PspProcessDelete`就在这里)，CPU 会先用 Windows 的页表把这个虚拟地址转换为 Guest Physical Address (GPA)。比如得到 `0x274EE1000`。但这还没完：CPU 接着会用 EPT 再把这个 GPA 转换一次，得到真正的 host 物理地址。

因此，即便 VTL0 在自己的页表里把页面标记为可写，EPT 仍然可以强制只读策略。

**VTL0 页表 (Windows 视角)**

Windows 看着自己的页表，会“以为”自己完全掌控。对内核代码页，Windows 通常会这样设置：

![\_MMPTE\_HARDWARE structure](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3pctUHs4Ex4hzkfm4QjiaWsFicd99mSPgTrUy1uGZ9sxwgrxsanvd0BZg/640?wx_fmt=png&from=appmsg)

\_MMP...