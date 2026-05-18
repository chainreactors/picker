---
title: EDR终端对抗技术深度剖析
url: https://mp.weixin.qq.com/s/rzZYoAdzmjWGHlYp_FVWDQ
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:07:22.047494
---

# EDR终端对抗技术深度剖析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M5H82XuSHY5o8cicvJUBOibBm9t8OMw46wAIeO47fEAvEgtU7zn6HYSJzMsQevvwiaZ0icHPTnoTS03uE3ssaKNfy2IQF17uGffGS4IqibmEZqjI/0?wx_fmt=jpeg)

# EDR终端对抗技术深度剖析

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文从应用层、内核层、静态、动态四大维度，系统剖析 EDR 终端对抗技术的原理、实现与检测策略，为红蓝双方提供全面的技术参考。

---

## 目录

* 一、EDR 监控体系全景
* 二、应用层对抗技术
* 三、内核层对抗技术
* 四、静态对抗技术
* 五、动态对抗技术
* 六、对抗技术全景矩阵
* 七、组合对抗战术与实战链路
* 八、蓝队检测与防御策略
* 九、实战工具与资源
* 十、技术演进趋势与展望
* 附录

---

## 一、EDR 监控体系全景

### 1.1 EDR 监控架构总览

现代 EDR 产品采用多层次、全维度的监控体系，从用户态到内核态形成完整的检测闭环：

![](https://mmbiz.qpic.cn/mmbiz_png/M5H82XuSHY6eOj2QDDn2wpjhUawHIDqIorCfRia76pB4Pp5ZDNFPcOgC3hUthu4OnKGOG30VXtWYFt39rxpEvkKIoN6mRVrKjMtqH5EJX7rw/640?wx_fmt=png&from=appmsg)

### 1.2 内核回调机制

EDR 通过注册 Windows 内核回调来获取系统事件通知，这是 EDR 最基础也最关键的监控手段：

| 回调类型 | 注册函数 | 监控内容 | 数据结构 | 对应 SSRM |
| --- | --- | --- | --- | --- |
| 进程创建 | `PsSetCreateProcessNotifyRoutineEx` | 新进程启动/退出 | `PS_CREATE_NOTIFY_INFO` | `PsCreateProcess` |
| 线程创建 | `PsSetCreateThreadNotifyRoutine` | 新线程创建 | Thread ID + Process ID | `PsCreateThread` |
| 镜像加载 | `PsSetLoadImageNotifyRoutine` | DLL/EXE 映像加载 | `IMAGE_INFO_EX` | `PsLoadImage` |
| 文件操作 | `FltRegisterCallback` | 文件读写删除重命名 | `FLT_CALLBACK_DATA` | Mini-filter |
| 注册表操作 | `CmRegisterCallback` | 注册表键值增删改查 | `REG_CALLBACK_CONTEXT` | `CmRegister` |
| 对象管理 | `ObRegisterCallbacks` | 句柄操作(打开/复制) | `OB_CALLBACK_CONTEXT` | `ObRegister` |

**回调函数存储结构：** 回调以指针数组形式存储在内核中（如 `PspCreateProcessNotifyRoutine[]`），每个元素编码了回调函数地址和启用状态（最低2位为标志位：bit0=启用，bit1=是否Ex版本），实际地址 = `entry & ~3`。

**对抗思路**：这些回调函数地址存储在内核内存中，理论上可以被定位并修改。但现代 EDR 会保护这些回调表，直接修改会触发 PatchGuard (KPP)。

### 1.3 ETW（Event Tracing for Windows）

ETW 是 Windows 内置的事件追踪系统，EDR 通过订阅特定 Provider 获取细粒度事件：

| Provider GUID | Provider 名称 | 监控内容 | 事件级别 |
| --- | --- | --- | --- |
| `{F4A2C69D-12A7-4D73-B8F1-8F2B5E3F8D3A}` | Microsoft-Windows-Threat-Intelligence | 内核行为（进程/线程/镜像加载） | Critical |
| `{22FB2CD6-0E7B-422B-A0C7-2F8DF4794EE0}` | Microsoft-Windows-Kernel-Process | 进程生命周期事件 | Information |
| `{7B921740-4380-44E6-9DE6-3F4E62D1E3A0}` | Microsoft-Windows-Kernel-ImageLoad | 模块加载事件 | Information |
| `{E7EF15BE-2D2B-419B-9E4A-5ED9C3E08D3A}` | Microsoft-Windows-DotNETRuntime | .NET 运行时事件 | Information |
| `{647B8910-39A0-4CA7-8570-2E04D2B32E7A}` | Microsoft-Antimalware-Scan-Interface | AMSI 扫描结果 | Verbose |

**ETW 数据流架构：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/M5H82XuSHY5prnkwiaPfawK7XxxMOGYiaias3ib34n5P2YGjPF0vrbNyiaA0yXFib96gXibySIVz436JA75s2oGdha5JEFG4L9Dgo9ZSOfWEozj7U8/640?wx_fmt=png&from=appmsg)

**对抗思路**：ETW 事件在用户态通过 `EtwEventWrite` 发出，可以在此函数上下钩子或打补丁阻止事件上报；在内核态则可修改 ETW Provider 的启用标志位。

### 1.4 用户态 API 钩子（User-land Hooking）

EDR 在关键 API 入口处插入跳转指令（通常为 `JMP` 或 `CALL`），将执行流重定向到检测代码：

```
正常调用链:
┌─────────────────┐    ┌───────────────────────┐    ┌──────────┐
│ kernel32.dll    │───▶│ ntdll.dll             │───▶│ 内核     │
│ CreateProcessA │    │ NtCreateUserProcess   │    │ (syscall)│
└─────────────────┘    └───────────────────────┘    └──────────┘

被 Hook 后:
┌─────────────────┐    ┌──────────┐    ┌───────────────────────┐    ┌──────────┐
│ kernel32.dll    │───▶│ EDR 检测 │───▶│ ntdll.dll             │───▶│ 内核     │
│ CreateProcessA │    │  代码    │    │ NtCreateUserProcess   │    │ (syscall)│
└─────────────────┘    └──────────┘    └───────────────────────┘    └──────────┘
```

**Hook 实现原理（Inline Hook / Trampoline Hook）：**

```
// EDR Hook 典型实现 - 修改ntdll函数入口
// 原始字节: 4C 8B D1 B8 XX 00 00 00  (mov r10, rcx; mov eax, syscall_num)
// Hook后:   JMP [EDR_Handler]         (5字节跳转或14字节绝对跳转)

// 32位相对跳转 (5字节, 覆盖mov r10,rcx + mov eax,SSN前5字节)
E9 XX XX XX XX    // JMP rel32

// 64位绝对跳转 (14字节, 避免跳转范围限制, 覆盖前14字节)
FF 2500000000    // JMP [rip+0]
XX XX XX XX XX XX XX XX  // 绝对地址(8字节)

// EDR Hook后的ntdll!NtWriteVirtualMemory内存布局示例:
// 偏移  字节                    含义
// 0x00  E9 3A 12 00 00         JMP rel32 → EDR Handler (被Hook)
// 0x05  90 90 90 90 90         NOP填充 (原字节被覆盖)
// 0x0A  ...                    函数剩余部分
```

**主流 EDR Hook 覆盖范围：**

| EDR 产品 | Hook 层级 | Hook 范围 | 自保护机制 | Unhook难度 |
| --- | --- | --- | --- | --- |
| CrowdStrike Falcon | ntdll + kernel32 | 进程/线程/内存/文件/注册表 | 驱动保护+回调校验+ETW TI | ★★★★★ |
| Microsoft Defender | ntdll | 进程/内存/文件/AMSI | ELAM+云协同+MPMinDriver | ★★★☆☆ |
| SentinelOne | ntdll + win32k | 进程/线程/内存/注册表 | 内核回调+ETW+行为模型 | ★★★★☆ |
| Carbon Black | ntdll | 进程/文件/网络 | 驱动保护+云分析 | ★★★☆☆ |
| Elastic EDR | ntdll | 进程/文件/网络 | eBPF(Linux)/ETW(Windows) | ★★☆☆☆ |
| Cortex XDR | ntdll + kernel32 | 进程/线程/内存/文件/注册表 | 内核回调+cyvrmtck驱动 | ★★★★★ |
| Trellix (McAfee) | ntdll | 进程/内存/文件 | mfefirek驱动+AMSI | ★★★☆☆ |

---

## 二、应用层对抗技术

应用层对抗技术主要针对 EDR 在用户态部署的监控机制（API Hook、ETW 用户态上报、AMSI 扫描等），通过绕过、移除或欺骗这些监控点来规避检测。

### 2.1 直接系统调用（Direct Syscall）

**原理**：不经过被 Hook 的 ntdll.dll 导出函数，直接在代码中内联 syscall 指令进入内核，完全绕过用户态 Hook。

**实现方式一：内联汇编（硬编码 SSN）**

```
; NtAllocateVirtualMemory (SSN = 0x18 on Win10 21H2)
NtAllocateVirtualMemory:
    mov r10, rcx          ; x64调用约定: syscall需r10
    mov eax, 18h          ; 系统调用号
    syscall               ; 进入内核
    ret
```

> **局限**：SSN 随 Windows 版本更新而变化，硬编码导致跨版本兼容性问题。

**实现方式二：Hell's Gate — 动态 SSN 提取**

从内存中被 Hook 的 ntdll 中提取 syscall 号（Hook 通常保留 `mov eax, SSN` 指令）：

```
BOOL ExtractSyscallNumber(PVOID pFunctionAddress, UINT32* pSyscallNumber) {
    BYTE* pBytes = (BYTE*)pFunctionAddress;
    // 被Hook的ntdll入口: mov r10,rcx (4C 8B D1) + mov eax,SSN (B8 XX XX XX XX)
    if (pBytes[0] == 0x4C && pBytes[1] == 0x8B && pBytes[2] == 0xD1 && pBytes[3] == 0xB8) {
        *pSyscallNumber = *(UINT32*)(pBytes + 4);
        return TRUE;
    }
    return FALSE;
}
```

**实现方式三：Tartarus' Gate** — 从磁盘映射干净的 ntdll.dll 解析 SSN，解决 Hell's Gate 在 Hook 覆盖了 `mov eax` 指令时失败的问题。

**实现方式四：SysWhispers3** — 自动化 Syscall 代码生成（`python syswhispers3.py -f NtAllocateVirtualMemory -o output`），自动适配不同 Windows 版本，支持 Direct/Indirect 两种模式。

**对抗效果对比：**

| 技术方案 | SSN获取方式 | 绕过Hook | 跨版本兼容 | 实现复杂度 | 调用栈合法性 | EDR检测风险 |
| --- | --- | --- | --- | --- | --- | --- |
| 硬编码SSN | 静态写死 | ✅ | ❌ | ★☆☆☆☆ | ❌ (RIP在未知内存) | ETW TI+栈回溯 |
| Hell's Gate | 内存解析被Hook的ntdll | ✅ | ✅ | ★★★☆☆ | ❌ (RIP在未知内存) | ETW TI+栈回溯 |
| Tartarus' Gate | 磁盘映射干净ntdll | ✅ | ✅ | ★★★★☆ | ❌ (RIP在未知内存) | ETW TI+栈回溯 |
| SysWhispers3 | 编译时生成 | ✅ | ✅ | ★★☆☆☆ | ❌ (RIP在未知内存) | ETW TI+栈回溯 |
| Halo's Gate | 跳过Hook扫描相邻SSN | ✅ | ✅ | ★★★☆☆ | ❌ (RIP在未知内存) | ETW TI+栈回溯 |

### 2.2 间接系统调用（Indirect Syscall）

**原理**：跳转到 ntdll.dll 中原始 `syscall; ret` 指令的位置执行系统调用，返回地址指向 ntdll.dll 内部而非未知内存区域，使调用栈看起来合法。

```
Direct Syscall 调用栈:
  攻击代码区域 ◄── 返回地址指向未知内存 (EDR可检测)

Indirect Syscall 调用栈:
  攻击代码区域 ──▶ ntdll.dll!syscall;ret ◄── 返回地址指向ntdll (看起来合法)
```

**代码实现：**

```
// 1. 在ntdll中定位原始syscall指令地址 (扫描0F 05 C3序列)
PVOID FindSyscallInstruction(PVOID pNtFunction) {
    BYTE* ptr = (BYTE*)pNtFunction;
    for (int i = 0; i < 0x20; i++) {
        if (ptr[i] == 0x0F && ptr[i+1] == 0x05 && ptr[i+2] == 0xC3)
            return (PVOID)(ptr + i);
    }
    return NULL;
}
// 2. 设置SSN后JMP到ntdll!syscall;ret (非直接执行syscall)
```

**Direct vs Indirect Syscall 对比：**

| 对比维度 | Direct Syscall | Indirect Syscall |
| --- | --- | --- |
| syscall执行位置 | 攻击代码自身（未知内存区域） | ntdll.dll 内部（合法地址范围） |
| 返回地址(RIP) | 指向未知内存 → EDR栈回溯可标记 | 指向ntdll.dll → 调用栈看起来合法 |
| ETW TI Provider | 可检测syscall来源不在ntdll | syscall来源在ntdll范围内 |
| 调用栈回溯 | 立即暴露（RIP ∉ 已知模块） | 需深度分析才能识别 |
| 实现复杂度 | 较低（仅需SSN+syscall指令） | 中等（需定位ntdll中syscall指令地址） |
| 兼容性 | 高（任何Windows版本） | 中（需扫描ntdll找到syscall;ret序列） |
| 绕过Hook能力 | ✅ 完全绕过用户态Hook | ✅ 完全绕过用户态Hook |
| 代表工具 | SysWhispers3, Hell's Gate | SysWhispers2/3 (indirect模式) |

### 2.3 ETW 补丁技术

#### 2.3.1 用户态 ETW 补丁

定位 ntdll.dll 中的 `EtwEventWrite` 函数，修改其开头字节使其直接返回：

```
// 将EtwEventWrite修改为 xor eax,eax; ret (返回STATUS_SUCCESS)
// 比直接写ret(0xC3)更隐蔽, 调用者不会因返回值异常而报错
BOOL PatchEtwReturnSuccess() {
    FARPROC pFunc = GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWrite");
    DWORD oldProtect;
    VirtualProtect(pFunc, 3, PAGE_EXECUTE_READWRITE, &oldProtect);
    BYTE patch[] = { 0x31, 0xC0, 0xC3 };  // xor eax,eax; ret
    memcpy(pFunc, patch, sizeof(patch));
    Vir...