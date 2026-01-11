---
title: windows下利用进程克隆实现 EDR 规避
url: https://mp.weixin.qq.com/s/wtLbF61I4hJ-SJgvXyYx6w
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:38:39.284182
---

# windows下利用进程克隆实现 EDR 规避

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2ltn6J2FPhqa9HGS1oT0Nb80ZZ9NxrANxbUUeRSLxLL76RibHMY8ibpbfhT47tJKz1Ur0gncbwv5TNw/0?wx_fmt=jpeg)

# windows下利用进程克隆实现 EDR 规避

星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

# Windows 下利用进程克隆实现 EDR 规避

## 摘要 (Abstract)

“Dirty Vanity” 是一种基于 Windows 操作系统中尚不广为人知的进程分支（Process Forking）机制实现的代码注入技术。该技术的关键在于，它将传统“分配-写入-执行”（Allocate-Write-Execute）攻击链条中的写入和执行阶段拆分到两个不同的进程里。通过滥用如 `RtlCreateProcessReflection` 这类进程反射 API，攻击者得以在一个新生成的子进程（即克隆进程）内运行恶意代码。由于 EDR（端点检测与响应）系统通常专注于监视并关联发生在同一进程内的操作，Dirty Vanity 使得克隆进程在 EDR 的视角下从未经过写入或修改，因此能够有效绕过当前主流的注入检测逻辑，对传统的安全防御模型构成了新的挑战。

---

## 1. 技术背景：Windows 进程分支 (Process Forking)

### 1.1 分支机制的起源与在 Windows 中的存在

进程分支（Forking）指的是从调用者进程创建出一个新进程的行为。这一概念最早源于 Unix 系统中用于进程创建的 `fork` 和 `exec` 系统调用。分支产生的结果（子进程）是分支调用者（父进程）的一个**完全相同的副本**，唯一的区别在于 `fork` 系统调用的返回值不同。

尽管 Windows 默认的进程创建机制（例如 `CreateProcess`）并不采用 `fork` 与 `exec` 模型，但它确实通过遗留的 POSIX 子系统（其中包含 `psxdll.dll`）提供了对该机制的支持。

在现代 Windows 系统中，进程分支或克隆能力主要通过以下几种机制来实现：

1. **进程反射 (Process Reflection)：** 该机制旨在支持对需要持续提供服务的进程进行分析。Windows 诊断基础设施（WDI）就运用了反射进程，其核心实现函数是 `RtlCreateProcessReflection`。
2. **进程快照 (Process Snapshotting)：** 通过调用 `PssCaptureSnapshot` 来实现。
3. **凭证窃取：** 反射和快照技术使得攻击者能够在逃避 EDR 检测的同时执行凭证窃取操作。

### 1.2 进程分支 API 概览

Windows 提供了一系列用于进程克隆的底层 Native API：

| API 类型 | 核心函数 | 描述 |
| --- | --- | --- |
| **自克隆 (Self Fork)** | `RtlCloneUserProcess` | 用于克隆调用者自身的进程，子进程中的线程会返回 `STATUS_PROCESS_CLONED` (0x00000129)。 |
| **远程克隆 (Remote Fork)** | `NtCreateProcess[Ex]` | 用于创建新进程，同时也是进程快照（`PssCaptureSnapshot`）功能所依赖的底层机制。 |
| **远程执行克隆** | `RtlCreateProcessReflection` | 允许通过远程线程在目标进程内部触发克隆操作，并且可以指定起始的执行例程。 |

需要注意的是，如果直接尝试使用 `NtCreateUserProcess` 进行远程克隆，操作将会失败，系统会返回 `STATUS_INVALID_PARAMETER` (0xC000000D) 错误。例如，`Forker.exe` 在尝试克隆 `lsass.exe` 时就遇到了这个错误。因此，实现远程代码执行需要依赖于 `RtlCreateProcessReflection`。

---

## 2. 内部机制：地址空间克隆的奥秘

Dirty Vanity 攻击之所以有效，其根源在于 Windows 内核管理进程地址空间克隆的特定方式。

### 2.1 地址空间复制与写时复制 (Copy-on-Write)

克隆机制的核心是 `MiCloneProcessAddressSpace` 函数，它负责将父进程的内存内容复制给分支出来的子进程。这种复制是以**写时复制 (Copy-on-Write)** 视图的形式进行的，这大大提升了效率。这意味着，只有在子进程或父进程试图对某个页面进行写入时，才会发生实际的数据复制操作。克隆过程会复制父进程的私有内存页面以及大部分已被映射的内存区域。

### 2.2 内存继承的筛选机制

虽然进程克隆听起来像是一次完美的内存复制，但并非所有的内存区域都会被克隆。操作系统通过一个名为 `_MMVAD`（用于描述进程中内存分配情况的内核对象）的内核对象来管理每个进程的虚拟地址描述符。在克隆过程中，内核函数 `MiAllocateChildVads` 会遍历父进程的 VADs，并通过 `MiVadShouldBeForked` 函数对这些 VADs 进行筛选。

**筛选的关键点：**

决定内存是否被克隆，主要取决于 `_MMVAD_FLAGS2` 中的第 26 位，即 `Inherit` 标志（其值为 `0x4000000`）。

`MiVadShouldBeForked` 函数的伪代码逻辑如下所示：

```
PSEUDO bool MiVadShouldBeForked(_MMVAD *CurrentVadNode)
{
    // 对于大多数 MEM_PRIVATE VADs (私有内存)
    return 1;

    // 对于 MEM_MAPPED VADs (映射内存)
    if ( _bittest(CurrentVadNode.u2.LongFlags2 , 0x1A)) // 26th bit
        return 1; // 继承标志位已设置，进行克隆
    else
        return 0; // 继承标志位未设置，不进行克隆
}
```

内存映射是通过 `NtMapViewOfSection` API 来完成的，其中的 `InheritDisposition` 参数控制着视图如何与子进程共享：

* **ViewShare (1)：** 该视图将被映射到未来创建的任何子进程中（会设置 `Inherit` 标志）。
* **ViewUnmap (2)：** 该视图将**不会**被映射到子进程中（不会设置 `Inherit` 标志）。

### 2.3 `MessageBoxA` 失败的启示：DLL 调用的兼容性问题

当尝试在克隆进程中执行涉及高级 DLL（例如 `user32.dll`）的 Shellcode 时，例如调用 `MessageBoxA` 函数，会导致访问冲突（Access violation - code c0000005）。

失败的原因在于，`MessageBoxA` 所调用的内部函数（例如 `USER32!GetDpiForCurrentProcess`）需要访问 `USER32!gpsi`。`USER32!gpsi` 指向一个名为 `win32k!tagSHAREDINFO` 的核心对象，该对象持有会话特定的 GUI 信息。这个对象位于一个共享的只读区段内，在 `user32.dll` 初始化期间被映射到每个进程中。

通过逆向分析可以得知，`win32k!InitMapSharedSection` 在映射这个共享区段时，使用了 `ViewUnmap` 作为继承属性：

```
result = NtMapViewOfSection(ghSectionShared,[snip], ViewUnmap, [snip]);
```

因此，由于使用了 `ViewUnmap` 属性，进程分支过程**不会复制**这些共享区段。这导致克隆进程缺少 `USER32!gpsi` 所需的内存映射，从而使依赖于这些高层 DLL 状态的 Shellcode 执行失败。

**结论：** Dirty Vanity 的攻击者在构建 Shellcode 时，应当避免依赖这些不会被继承的内存映射，或者选择使用纯 Ntdll API 来执行操作，例如通过调用 `NtCreateUserProcess` 来启动一个新进程。

---

## 3. Dirty Vanity 攻击原理与实现

### 3.1 核心原理：分离攻击链

传统的代码注入检测依赖于 EDR 系统对同一进程内发生的以下三个步骤进行关联：

1. **分配 (Allocate)：** 在目标进程中分配具有可执行权限的内存。
2. **写入 (Write)：** 将恶意的 Shellcode 写入到该内存区域。
3. **执行 (Execute)：** 通过创建远程线程等方式来执行该 Shellcode。

**Dirty Vanity** 技术利用进程分支机制，引入了两个新的操作原语：**分支 (Fork)** 和 **分支与执行 (Fork & Execute)**。

**攻击链分离流程 (拟人化架构图描述):**

| 步骤 | 原始进程（父进程，例如 `explorer.exe`） | 克隆进程（子进程，例如 `explorer.2.exe`） | EDR 视角 |
| --- | --- | --- | --- |
| **1. 分配 (Allocate Primitive)** | 使用 `VirtualAllocEx` 在父进程中分配内存。 | N/A | EDR 记录：**分配** |
| **2. 初始写入 (Initial Write Primitive)** | 使用 `WriteProcessMemory` 将 Shellcode 写入父进程的内存。 | N/A | EDR 记录：**写入** |
| **3. 分支与执行 (Fork & Execute Primitive)** | 调用 `RtlCreateProcessReflection`。 | 克隆父进程的地址空间，继承已写入的 Shellcode。 | EDR 记录：**克隆创建** |
| **4. 执行 (Execution)** | N/A | 在克隆进程中，从克隆得到的 Shellcode 起始地址开始执行。 | EDR 发现：克隆进程上只有**执行**操作，没有写入记录。 |

**EDR 规避点：** EDR 观察到 Allocate 和 Write 操作发生在父进程，但 Execute 操作却发生在子进程。由于子进程是父进程内存的克隆体，EDR 会错误地认为子进程从未被写入过，因此不会被标记为存在注入行为。Dirty Vanity 通过改变操作系统监控的固有规则，颠覆了人们对注入防御的传统认知。### 3.2 攻击步骤与代码示例

#### 3.2.1 初始写入步骤

攻击者首先在目标父进程中分配内存并写入 Shellcode。以下为几种常见的初始写入方法：

* `VirtualAllocEx` 与 `WriteProcessMemory`
* `NtCreateSection` 与 `NtMapViewOfSection`
* `NtSetContextThread`（幽灵写入）

#### 3.2.2 分支与执行步骤

随后，攻击者利用 `RtlCreateProcessReflection` API 触发进程克隆与代码执行。

**先决条件：** 调用 `RtlCreateProcessReflection` 前，需以特定的访问权限打开目标进程：

* `PROCESS_VM_OPERATION`
* `PROCESS_CREATE_THREAD`
* `PROCESS_DUP_HANDLE`

**代码示例：基于 `RtlCreateProcessReflection` 实现 Dirty Vanity** 以下代码演示了如何打开目标进程、分配并写入 Shellcode，最终借助反射机制在克隆进程中执行该代码：

```
// 1. 定义 Shellcode 数组（此处为示意，假设是 ntdll API shellcode）
unsigned char shellcode[] = {0x40, 0x55, 0x57, ...};

// 2. 以适当权限打开目标进程
HANDLE victimHandle = OpenProcess(
    PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_CREATE_THREAD | PROCESS_DUP_HANDLE,
    TRUE,
    victimPid
);

// 3. 在目标进程内分配内存以容纳 Shellcode
DWORD_PTR shellcodeSize = sizeof(shellcode);
LPVOID baseAddress = VirtualAllocEx(
    victimHandle,
    nullptr,
    shellcodeSize,
    MEM_COMMIT | MEM_RESERVE,
    PAGE_EXECUTE_READWRITE
);

// 4. 将 Shellcode 写入分配的内存
BOOL status = WriteProcessMemory(
    victimHandle,
    baseAddress,
    shellcode,
    shellcodeSize,
    &bytesWritten
);

// 5. 加载 ntdll.dll 并获取 RtlCreateProcessReflection 的函数指针
#define RTL_CLONE_PROCESS_FLAGS_INHERIT_HANDLES 0x00000002
HMODULE ntlib = LoadLibraryA("ntdll.dll");
Rtl_CreateProcessReflection RtlCreateProcessReflection =
    (Rtl_CreateProcessReflection)GetProcAddress(ntlib, "RtlCreateProcessReflection");

// 6. 分支目标进程，并在克隆进程中执行 Shellcode
T_RTLP_PROCESS_REFLECTION_REFLECTION_INFORMATION info = { 0 };
NTSTATUS ret = RtlCreateProcessReflection(
    victimHandle,
    RTL_CLONE_PROCESS_FLAGS_INHERIT_HANDLES,
    baseAddress, // 将 Shellcode 的基地址作为 StartRoutine 传入
    NULL,
    NULL,
    &info
);
// 克隆进程（clone）将从 baseAddress 处开始执行
```

**反射流程描述：**`RtlCreateProcessReflection` 涉及三个进程的协作：

1. **调用者：** 准备共享内存，创建同步事件，并将事件句柄复制到**父进程**。
2. **父进程：** 在其中创建远程线程以执行 `RtlpProcessReflectionStartup`。该线程随后调用 `RtlCloneUserProcess` 完成克隆，并将事件句柄复制到**克隆进程**。
3. **克隆进程：** 启动后，等待用户提供的事件（如存在），然后调用 `StartRoutine`（即传入的 Shellcode 地址）执行代码，执行完毕后终止。

通过将 Shellcode 的起始地址 (`baseAddress`) 作为 `StartRoutine` 参数传递给 `RtlCreateProcessReflection`，克隆进程便会在其地址空间中直接执行这段预先写入的代码。

---

## 4. EDR 规避、挑战与防御对策

### 4.1 EDR 规避机制

Dirty Vanity 的主要规避能力源于它打破了传统的分配/写入/执行（Allocate/Write/Execute）单进程关联模型：

* **分配与写入阶段：** 发生在父进程中。这些内存操作本身可能表现为合法的进程行为，或与其他操作相混淆。
* **执行阶段：** 发生在克隆的子进程中。由于内存是作为父进程副本通过写时复制（Copy-on-Write）继承的，子进程的内存页在 EDR 视角下是“干净”的，**从未显示被写入的痕迹**。

### 4.2 攻击的可见性与局限性

尽管 Dirty Vanity 能绕过传统的注入模式检测，但其实现远程代码注入所需的底层操作仍具有较高的可观测性。特别是通过 `RtlCreateProcessReflection` 进行的远程注入，与经典注入技术共享许多可检测的向量：

1. **进程句柄获取：** 打开目标父进程时会触发 Ob- 回调，而请求的访问权限掩码（`PROCESS_VM_OPERATION | PROCESS_CREATE_THREAD | PROCESS_DUP_HANDLE`）与 Shellcode 或 DLL 注入所需的权限高度相似，通常受到严格监控。
2. **跨进程内存映射：** 在父...