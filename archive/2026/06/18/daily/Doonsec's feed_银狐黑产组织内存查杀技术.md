---
title: 银狐黑产组织内存查杀技术
url: https://mp.weixin.qq.com/s/2U6ifEEHte86Tar6FlhQEg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:00:39.839418
---

# 银狐黑产组织内存查杀技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/M5H82XuSHY4L3J6WSIMhCFXWFHSZ4yI5Io6ux1YjS0BrncIbNHiaWYISYs43jbmiav2kVX1LzzyT7ibrYXxx1zdiaFD0eVSRegMxibNs0PTclAcQ/0?wx_fmt=jpeg)

# 银狐黑产组织内存查杀技术

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

深度剖析银狐黑产组织16大内存加载技术原理、实现细节与内存特征扫描检测方法

---

## 目录

* 一、银狐内存加载技术全景
* 二、DLL内存加载
* 三、远程线程注入
* 四、进程创建加载（Process Hollowing）
* 五、线程创建加载
* 六、白+黑加载（DLL侧载）
* 七、内存映射加载
* 八、反射DLL注入
* 九、APC内存注入
* 十、线程上下文设置（Thread Hijacking）
* 十一、Callback内存执行
* 十二、Module Stomping与DLL Phantom
* 十三、ETW/AMSI内存Patch后执行
* 十四、异常处理链注入（VEH/SEH）
* 十五、纤程（Fiber）内存执行
* 十六、DLL通知回调注入
* 十七、NtCreateSection双进程注入
* 十八、内存特征扫描检测技术
* 十九、内存查杀实战工具与流程

---

## 一、银狐内存加载技术全景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/M5H82XuSHY482ic10dic26PsV3icw2sM08TDAibZoPdVFNautW9GUAibehvZbypkDgEuj2GBib31fgWtgzNZ9OCqjQftcs4KYoqUNoepsqIvO7y18/640?wx_fmt=png&from=appmsg)

银狐黑产组织在内存加载方面具备**APT级全栈能力**，从文件落地到纯内存驻留，覆盖**16大技术路径**：

| 技术 | 文件落地 | PEB可见 | 调用栈外观 | 银狐使用频率 | 检测难度 |
| --- | --- | --- | --- | --- | --- |
| DLL内存加载 | 有 | 是 | 正常 | ★★★★★ | 中 |
| 远程线程注入 | 无 | 否 | 异常(新线程) | ★★★★★ | 中 |
| 进程创建加载 | 无 | 伪装合法 | 合法进程外观 | ★★★★ | 高 |
| 线程创建加载 | 无 | 否 | 异常(新线程) | ★★★★ | 中 |
| 白+黑加载 | 有(白+黑) | 是 | 正常(白程序) | ★★★★★ | 中高 |
| 内存映射 | 无 | 否 | 取决于执行方式 | ★★★★ | 高 |
| 反射DLL注入 | 无 | **否** | 无模块记录 | ★★★★★ | 极高 |
| APC注入 | 无 | 否 | 回调栈外观 | ★★★★ | 高 |
| 线程上下文设置 | 无 | 否 | 劫持合法线程 | ★★★ | 极高 |
| **Callback内存执行** | 无 | 否 | 合法回调栈 | ★★★★ | 极高 |
| **Module Stomping** | 无 | 伪装合法 | 合法模块外观 | ★★★ | 极高 |
| **ETW/AMSI Patch** | 无 | 否 | 正常(检测已禁用) | ★★★★★ | 极高 |
| **异常处理链注入** | 无 | 否 | 异常处理栈 | ★★★ | 极高 |
| **纤程执行** | 无 | 否 | 纤程切换栈 | ★★★ | 极高 |
| **DLL通知回调注入** | 无 | 否 | Ldr通知栈 | ★★★ | 高 |
| **NtCreateSection双进程注入** | 无 | 否 | Section映射栈 | ★★★ | 极高 |

---

## 二、DLL内存加载

### 2.1 技术原理

DLL内存加载是银狐木马**最基础也最常用**的内存加载方式，通过`LoadLibrary`/`LoadLibraryEx`将DLL加载到进程地址空间，DLL的`DllMain`函数在加载时自动执行。

```
DLL内存加载流程:
  ① 调用LoadLibraryA("malicious.dll")
     → 操作系统执行:
       a) 映射DLL到进程地址空间(NtMapViewOfSection)
       b) 处理导入表(解析依赖DLL+API地址)
       c) 处理重定位表(修正地址引用)
       d) 调用DllMain(hModule, DLL_PROCESS_ATTACH, NULL)
  ② DllMain中执行恶意逻辑:
     → 创建线程执行核心功能(避免阻塞加载者)
     → 反沙箱检测 → 地域限制 → 解密Shellcode → C2回连
  ③ DLL加载后:
     → PEB.Ldr模块列表中新增条目
     → LDR_DATA_TABLE_ENTRY记录DLL路径/基址/大小
     → 可通过Module32First/Next枚举到
```

### 2.2 银狐实现细节

```
// 银狐木马DLL加载 - 通过白程序侧载触发
// 白程序(wps.exe)同目录放置恶意version.dll
// Windows DLL搜索顺序: 当前目录 → System32 → Path

// 恶意DLL DllMain入口
BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID lpReserved) {
    if (reason == DLL_PROCESS_ATTACH) {
        // 1. 加载原始DLL(保证白程序正常功能)
        hOrigDll = LoadLibraryA("original_version.dll");
        // 2. 新线程执行恶意逻辑(不阻塞白程序启动)
        CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)MaliciousEntry, NULL, 0, NULL);
    }
    return TRUE;
}
```

### 2.3 内存特征与检测

| 内存特征 | 检测方法 | 检测工具 | 银狐绕过方式 |
| --- | --- | --- | --- |
| PEB模块列表新增DLL | Module32First/Next枚举 | Process Explorer | 正常加载无法绕过 |
| LDR\_DATA\_TABLE\_ENTRY | 遍历InLoadOrderModuleList | 自定义扫描器 | 正常加载无法绕过 |
| DLL路径异常 | 检查非标准路径DLL | Sysmon Event 7 | 选择冷门但合法路径 |
| 导出表转发特征 | 检测export指向original\_xxx.dll | PE分析工具 | 转发命名随机化 |
| 数字签名缺失 | 白程序有签名但DLL无签名 | sigcheck | 窃取合法签名 |

---

## 三、远程线程注入

### 3.1 技术原理

远程线程注入是银狐木马**最经典的跨进程内存加载方式**，在目标进程中分配内存、写入Shellcode、创建远程线程执行。

```
远程线程注入流程:
  ① OpenProcess → 获取目标进程句柄
     → 常见目标: explorer.exe / svchost.exe / 浏览器进程

  ② NtAllocateVirtualMemory(Indirect Syscall)
     → 在目标进程分配PAGE_EXECUTE_READWRITE内存
     → 基址由系统决定(baseAddr=NULL)

  ③ NtWriteVirtualMemory(Indirect Syscall)
     → 将Shellcode写入分配的内存区域
     → 写入大小=Shellcode长度

  ④ NtProtectVirtualMemory(Indirect Syscall)
     → 将内存属性从RWX改为PAGE_EXECUTE(不可读)
     → 防止内存扫描读取Shellcode明文

  ⑤ NtCreateThreadEx(Indirect Syscall)
     → 在目标进程创建远程线程
     → 线程起始地址=Shellcode基址
     → 线程立即开始执行
```

### 3.2 银狐实现细节（Indirect Syscall全链路）

```
// 银狐木马远程线程注入 - 全部使用Indirect Syscall绕过EDR Hook
NTSTATUS InjectShellcode(HANDLE hProcess, BYTE* shellcode, SIZE_T size) {
    PVOID baseAddr = NULL;
    SIZE_T regionSize = size;

    // Step 1: NtAllocateVirtualMemory (Indirect Syscall)
    // mov r10, rcx; mov eax, 0x18; jmp [ntdll!syscall;ret]
    IndirectSyscall(ssn_alloc, g_syscallRetAddr,
        hProcess, &baseAddr, 0, &regionSize,
        MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    // Step 2: NtWriteVirtualMemory (Indirect Syscall)
    IndirectSyscall(ssn_write, g_syscallRetAddr,
        hProcess, baseAddr, shellcode, size, NULL);

    // Step 3: NtProtectVirtualMemory → PAGE_EXECUTE
    IndirectSyscall(ssn_protect, g_syscallRetAddr,
        hProcess, &protectBase, &protectSize,
        PAGE_EXECUTE, &oldProtect);

    // Step 4: NtCreateThreadEx (Indirect Syscall)
    IndirectSyscall(ssn_thread, g_syscallRetAddr,
        &hThread, THREAD_ALL_ACCESS, NULL,
        hProcess, baseAddr, NULL, FALSE, 0, 0, 0, NULL);

    return STATUS_SUCCESS;
}
```

### 3.3 内存特征与检测

| 内存特征 | 检测方法 | 检测工具 | 银狐绕过方式 |
| --- | --- | --- | --- |
| 跨进程内存分配 | 监控NtAllocateVirtualMemory跨进程调用 | EDR内核回调 | Indirect Syscall绕过用户态Hook |
| 远程线程创建 | Sysmon Event 8检测 | Sysmon | NtCreateThreadEx Syscall |
| 线程起始地址异常 | 检查线程StartAddress不在任何模块范围内 | Process Explorer | Shellcode基址不在模块范围 |
| PAGE\_EXECUTE内存 | 扫描仅有EXECUTE权限的内存区域 | PE-sieve/Volatility | 执行后擦除或改为RWX再执行 |
| Unbacked可执行内存 | 可执行内存无对应磁盘文件 | HollowsHunter | 内存映射方式可部分绕过 |

---

## 四、进程创建加载（Process Hollowing）

### 4.1 技术原理

进程镂空（Process Hollowing）以挂起方式创建合法进程，替换其主模块内存为恶意PE，实现**合法进程外观+恶意代码执行**。

```
Process Hollowing流程:
  ① CreateProcess(CREATE_SUSPENDED)
     → 以挂起状态创建合法进程(如svchost.exe)
     → 进程主模块已映射但未执行

  ② GetThreadContext → 获取挂起线程上下文
     → 从上下文中提取PEB地址
     → 从PEB中读取ImageBaseAddress(主模块基址)

  ③ NtUnmapViewOfSection(Indirect Syscall)
     → 取消映射原进程主模块内存
     → 释放原合法PE占用的地址空间

  ④ NtAllocateVirtualMemory + NtWriteVirtualMemory
     → 在原ImageBase处分配内存
     → 写入恶意PE头+各节区数据
     → 处理重定位表(修正地址引用)
     → 修复导入表(解析依赖DLL+API)

  ⑤ SetThreadContext → 修改线程上下文
     → 将RIP/EIP指向恶意PE的入口点

  ⑥ ResumeThread → 恢复线程执行
     → 线程从恶意PE入口点开始执行
     → 进程外观仍为合法svchost.exe
```

### 4.2 银狐实现细节

```
// 银狐木马Process Hollowing
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过