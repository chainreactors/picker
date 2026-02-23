---
title: 深入理解 Windows 进程属性：从 PPID 欺骗到句柄继承
url: https://mp.weixin.qq.com/s/-0MbfIWFnpUD2P4IZRBrkQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:44.741842
---

# 深入理解 Windows 进程属性：从 PPID 欺骗到句柄继承

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K162YP0p9ZKW1ZRibjE9hs7AZicRa9csO59rTX7iaB05Q2pdMVl0mGAq8MZFAjypsbRZia1Sz9ZDicUXFFHu3mJOicY5jW0veEdoK0XQ/0?wx_fmt=jpeg)

# 深入理解 Windows 进程属性：从 PPID 欺骗到句柄继承

ZyOrca
ZyOrca

看雪学苑

![]()

在小说阅读器中沉浸阅读

在 Windows 恶意软件开发和红队行动中，如何让恶意进程在系统中看起来“人畜无害”是一项重要技能。本文将探讨STARTUPINFOEX 结构体，揭示如何通过它来实现父进程 ID (PPID) 欺骗、Early Bird 注入以及精确的句柄继承控制。

#

**1.基础介绍**

## 1.1 结构体 STARTUPINFO

STARTUPINFO  主要用于在创建新进程（调用 CreateProcess 函数）时，指定新进程的主窗口应当如何显示以及标准输入输出句柄的处理方式等信息。

```
typedef struct _STARTUPINFO {
  DWORD  cb;                // 结构体的大小 (以字节为单位)
  LPTSTR lpReserved;        // 保留，必须为 NULL
  LPTSTR lpDesktop;         // 指定桌面名称 (通常为 NULL)
  LPTSTR lpTitle;           // 控制台窗口的标题
  DWORD  dwX;               // 窗口左上角 X 坐标
  DWORD  dwY;               // 窗口左上角 Y 坐标
  DWORD  dwXSize;           // 窗口宽度 (像素)
  DWORD  dwYSize;           // 窗口高度 (像素)
  DWORD  dwXCountChars;     // 控制台窗口缓冲区宽度 (字符数)
  DWORD  dwYCountChars;     // 控制台窗口缓冲区高度 (字符数)
  DWORD  dwFillAttribute;   // 控制台文本和背景颜色
  DWORD  dwFlags;           // 标志位：决定哪些成员是有效的
  WORD   wShowWindow;       // 窗口显示状态 (如 SW_HIDE, SW_MAXIMIZE)
  WORD   cbReserved2;       // 保留，必须为 0
  LPBYTE lpReserved2;       // 保留，必须为 NULL
  HANDLE hStdInput;         // 标准输入句柄
  HANDLE hStdOutput;        // 标准输出句柄
  HANDLE hStdError;         // 标准错误句柄
} STARTUPINFO, *LPSTARTUPINFO;
```

在使调用 CreateProcess 创建进程前，必须初始化 STARTUPINFO。

```
STARTUPINFOsi = { 0 };
PROCESS_INFORMATIONpi = { 0 };
si.cb = sizeof(si);
```

## 1.2 结构体 STARTUPINFOEX

Windows 在 Vista / Windows Server 2008 引入了一个增强版的启动结构体：STARTUPINFOEX。这个结构体比普通的 STARTUPINFO 多了一个成员：lpAttributeList（属性列表）。

```
typedef struct _STARTUPINFOEXA {
  STARTUPINFOA                 StartupInfo;
  LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList; //属性列表
} STARTUPINFOEXA, *LPSTARTUPINFOEXA;
```

STARTUPINFOEX 引入属性列表lpAttributeList，目的在于更有针对性地设置进程的各种属性，包括子进程应该继承父进程的哪些句柄、是否可以加载非微软签名的 DLL ，以及支持 AppContainer（应用容器）和 UWP 应用的进程归属等等。

## 1.3  函数 InitializeProcThreadAttributeList()

InitializeProcThreadAttributeList() 用于初始化创建进程或线程时所需的属性列表。

```
BOOL InitializeProcThreadAttributeList(
  [out, optional] LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList,   //属性列表
  [in]            DWORD                        dwAttributeCount,  //要添加到列表的属性计数
                  DWORD                        dwFlags,           //此参数是保留的，必须为零。
  [in, out]       PSIZE_T                      lpSize             //如果 lpAttributeList 不为 NULL，则此参数指定输入时 lpAttributeList 缓冲区的大小（以字节为单位）。 输出时，此参数接收初始化的属性列表的大小（以字节为单位）。如果 lpAttributeList 为 NULL，则此参数接收所需的缓冲区大小（以字节为单位）。
);
```

属性列表的初始化比较特殊，需要调用两次：第一次确定需要多大的内存，第二次才真正填充数据。

```
STARTUPINFOEXA siex = { 0 };
// 第一次调用：获取属性列表所需的内存大小
InitializeProcThreadAttributeList(NULL, 1, 0, &attributeSize);
siex.lpAttributeList = (PPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 0, attributeSize);
// 第二次调用：正式初始化属性列表
InitializeProcThreadAttributeList(siex.lpAttributeList, 1, 0, &attributeSize);
```

lpAttributeList 指向的内存必须持续有效，直到 DeleteProcThreadAttributeList 被调用，如果在 CreateProcess 之前释放了该内存，进程的属性设置就不会奏效。

## 1.4 函数 UpdateProcThreadAttribute ()

UpdateProcThreadAttribute() 用于在创建进程或线程之前，精确设置其属性（如父进程分配、句柄继承、缓解策略等）。

```
BOOL UpdateProcThreadAttribute(
  [in, out]       LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList,  //指向属性列表的指针
  [in]            DWORD                        dwFlags,          //保留，必须为 0
  [in]            DWORD_PTR                    Attribute,        //指定要修改的进程属性
  [in]            PVOID                        lpValue,          //指向属性值 (Value) 的指针
  [in]            SIZE_T                       cbSize,           //lpValue 数据的大小
  [out, optional] PVOID                        lpPreviousValue,  //保留，通常为 NULL
  [in, optional]  PSIZE_T                      lpReturnSize      //保留，通常为 NULL
);
```

lpAttributeList 指向的内存是“不透明的”，在设置进程属性列表时，需要按照以下步骤操作：

* InitializeProcThreadAttributeList(第一次调用获取所需大小)
* 分配内存
* InitializeProcThreadAttributeList(第二次调用初始化)
* UpdateProcThreadAttribute(添加属性)
* 调用 CreateProcess
* DeleteProcThreadAttributeList(清理)

#

**2.父进程欺骗**

## 2.1 技术介绍（PPID Spoofing）

父进程欺骗（Parent Process Spoofing），也被称为 PPID Spoofing，是一种通过篡改进程创建参数，使新进程看起来是由另一个合法的系统进程（而非实际的创建者）启动的技术。

EDR（端点检测与响应系统）和杀毒软件通常会监控异常的父子进程关系。

* 异常行为：Word.exe -> PowerShell.exe (高度可疑，通常是宏病毒)。
* 欺骗后：Word.exe 启动了 PowerShell，但指认 Explorer.exe 为父进程。安全软件看到的是 Explorer.exe -> PowerShell.exe (这是用户正常打开终端的行为，可能会被放行)。

例如，正常点击 cmd 程序后，可以看出 cmd.exe 是由资源管理器进程 explorer.exe 创建的， explorer.exe 就是 cmd.exe 的父进程
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K29rNliaQIgZbTKA8UC9ZcxXNg0hkdMEsT4tRX3JIZ3JEar28iaicK8iaVV15j9Ky8blmEQe91fPWw7Kjglhm95TdfBfUtQf0tmkia8/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3KvUGcqRsdzFKMLrOjXzVpXSX5RWcpIjiaafEics1wIuT4EiagjukGVv6vDwLpbUhjPfcW2NiaHKNyhRvDfbqnLicW7R6iacdMAuianY/640?wx_fmt=png&from=appmsg)![]()

通过伪造 cmd.exe 的父进程后，上面正常的进程树就会被改变。

## 2.2 代码实现

### 2.2.1 正常情况的进程关系

正常情况下，在 Visual Studio 编译的程序 testcmd.exe 调用CreateProcess 创建 cmd.exe 进程，

```
#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <tlhelp32.h>
#include <stdio.h>

intmain() {
    STARTUPINFO si = { 0 };
    PROCESS_INFORMATION pi = { 0 };
    si.cb = sizeof(si);

    BOOL success = CreateProcess(
"C:\\Windows\\System32\\cmd.exe",   // 模块名
NULL,        // 命令行
NULL,        // 进程安全属性
NULL,        // 线程安全属性
        FALSE,       // 是否继承句柄
        CREATE_NEW_CONSOLE,   // 创建标志，CREATE_NEW_CONSOLE确保弹出新窗口
NULL,        // 环境变量
NULL,        // 当前目录
        &si,         // 指向 STARTUPINFO 或者 STARTUPINFOEX 指针
        &pi          // PROCESS_INFORMATION 指针
    );

if (success) {
printf("cmd 已启动，PID: %d\n", pi.dwProcessId);
CloseHandle(pi.hProcess);
CloseHandle(pi.hThread);
    }
else {
printf("创建进程失败，错误代码: %d\n", GetLastError());
    }

return 0;
}
```

进程树应该如下图所示， testcmd.exe 是 cmd.exe 的父进程
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2CgrGkxlg67PD3DY7dC9Tqw63ic59VJkCibJctPwKH7Aic2icVmkyH5ic0gfQhUoHj4K7uZuW0jCic7iatSqTvpvYib21l3yv4cHRzwaA/640?wx_fmt=png&from=appmsg)![]()

### 2.2.2 父进程欺骗后的进程关系

根据上面所介绍的关于进程属性列表的内容，函数 InitializeProcThreadAttributeList() 和 UpdateProcThreadAttribute() 可以用于设置进程属性，包括改变进程的父进程，具体代码实现如下：

```
#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <tlhelp32.h>
#include <stdio.h>

// 根据进程名获取 PID 的函数
DWORD GetPidByName(const char* processName) {
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    PROCESSENTRY32 entry = { sizeof(PROCESSENTRY32) };
if (Process32First(snapshot, &entry)) {
do {
if (_stricmp(entry.szExeFile, processName) == 0) {
                CloseHandle(snapshot);
return entry.th32ProcessID;
            }
        } while (Process32Next(snapshot, &entry));
    }
    CloseHandle(snapshot);
return 0;
}

int main() {
// 1. 目标：找到notepad++.exe 的 PID
    DWORD parentPid = GetPidByName("notepad++.exe");
if (parentPid == 0) {
        printf("请先运行notepad++程序！\n");
return 1;
    }

// 2. 打开父进程，获取句柄，需要 PROCESS_CREATE_PROCESS 权限
    HANDLE hParent = OpenProcess(PROCESS_CREATE_PROCESS, FALSE, parentPid);
if (hParent == NULL) return 1;

// 3. 初始化扩展启动信息结构体
    STARTUPINFOEXA siex = { 0 };
    PROCESS_INFORMATION pi = { 0 };
    SIZE_T attributeSize;

// 第一次调用：获取属性列表所需的内存大小
    InitializeProcThreadAttributeList(NULL, 1, 0, &attributeSize);
    siex.lpAttributeList = (PPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 0, attributeSize);

// 第二次调用：正式初始化属性列表
    InitializeProcThreadAttributeList(siex.lpAttributeList, 1, 0, &attributeSize);

// 4. 更新属性列表：设置父进程属性
    UpdateProcThreadAttribute(
        siex.lpAttributeList,
0,
        PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,
        &hParent,
sizeof(HANDLE),
NULL,
NULL
    );

    siex.StartupInfo.cb = sizeof(STARTUPINFOEXA);

// 5. 创建进程
// 使用 EXTENDED_STARTUPINFO_PRESENT 标志告诉系统我们使用了扩展启动信息
BOOL success = CreateProcessA(
"C:\\Windows\\System32\\cmd.exe", // 要启动的程序
NULL,
NULL,
NULL,
FALSE,
        EXTENDED_STARTUPINFO_PRESENT | CREATE_NEW_CONSOLE,
NULL,
NULL,
        &siex.StartupInfo,
        &pi
    );

if (success) {
        printf("cmd 已启动，PID: %d，伪造父进程 PID: %d\n", pi.dwProcessId, parentPid);...