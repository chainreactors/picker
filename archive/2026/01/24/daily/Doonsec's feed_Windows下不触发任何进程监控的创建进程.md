---
title: Windows下不触发任何进程监控的创建进程
url: https://mp.weixin.qq.com/s/i7qJCI1az3qZB-o1d7WYTQ
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:50.748849
---

# Windows下不触发任何进程监控的创建进程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ejibWMxI7nWLGKcY4e7q0ANGY1jt6sG6MM5rWyS7kMa8O0y2pac1CMwu95GEeZuXahuv57ey9yhsiafXlCkpmngw/0?wx_fmt=jpeg)

# Windows下不触发任何进程监控的创建进程

原创

为了安全鸭
为了安全鸭

冲鸭安全

![]()

在小说阅读器中沉浸阅读

## 前言

这几年AI用多了,脑子坏了,比如之前写代码很容易进入心流解决问题,这个过程很爽,但是现在只会开五六个ai的console让他帮我打工。
一开始是很急的让AI写功能，
但是到后来恨不得遇到bug，编译不通过，甚至是思考都托管给AI。
我把它叫做脑腐现象.所以为了避免这种现象,我准备用纯手工打造的方式搞点项目做。锻炼一下大脑。正巧，操作系统内核目前还是AI无法触及的领域。所以，here we go。

## 内核创建进程

所以，让我们来复习一下内核创建进程，这里不会说太多的基础，因为chatgpt都能回答了。我们直接说简单一点的。我们先实现一个简单的调用ntcreateuserprocess创建进程的例子，在内核里面这需要三步:

1. 定位ntcreateuserprocess
2. 填好参数
3. call

### 定位ntcreateuserprocess

定位方式有很多，比如经典款祖传找SSDT table,但是
我是懒得定位了，直接特征码写死了:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ejibWMxI7nWLGKcY4e7q0ANGY1jt6sG6McmIoGvS1oYTXtg29g4joF2GjicicUibc86ib9yUKRJkzGzbOwyY7BkH1bw/640?wx_fmt=png&from=appmsg)

### 填好参数

ntcreateuserpcoess在R3的执行的时候需要用到RtlCreateProcessParametersEx和RtlDestroyProcessParameters去填\_RTL\_USER\_PROCESS\_PARAMETERS
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ejibWMxI7nWLGKcY4e7q0ANGY1jt6sG6MAiacUg5Nym2svYicPm1xz6uk5YRQk1WdLPpLQCkucUptsE9IILYTgnHg/640?wx_fmt=png&from=appmsg)
我们R0是没有这个两个参数的，所以要自己填.填完直接call就行:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ejibWMxI7nWLGKcY4e7q0ANGY1jt6sG6MTibmXfwsQBRtpicNuQ4RWJB5RFW4ZgyE1FlnjXL0R9r14VvIfUplMGAg/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ejibWMxI7nWLGKcY4e7q0ANGY1jt6sG6M7X4xQXBkd3hN43kC5NIibxF4ZtmZaL1PCBEmkVPJbbcibxRxzeSCou9g/640?wx_fmt=png&from=appmsg)

但是坑来了,
而这个RTL\_USER\_PROCESS\_PARAMETERS 微软故意隐藏了东西，导致如果你按照微软的来写是没有办法跑起来的，跑起来会直接segment fault.这是因为没有正确的填参数,CRT初始化的时候就崩溃了。因此我写了一个R3程序，打印一下里面需要什么东西:

```
// ConsoleApplication1.cpp
// Dumps the raw payload produced by RtlCreateProcessParametersEx (user-mode).

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <winternl.h>

#include <cstdint>
#include <cstdio>
#include <string>
//0x18 bytes (sizeof)
struct _CURDIR
{
    struct _UNICODE_STRING DosPath;                                         //0x0
    VOID* Handle;                                                           //0x10
};
//0x18 bytes (sizeof)
struct _RTL_DRIVE_LETTER_CURDIR
{
    USHORT Flags;                                                           //0x0
    USHORT Length;                                                          //0x2
    ULONG TimeStamp;                                                        //0x4
    struct _STRING DosPath;                                                 //0x8
};
//0x410 bytes (sizeof)
struct _RTL_USER_PROCESS_PARAMETERSEX
{
    ULONG MaximumLength;                                                    //0x0
    ULONG Length;                                                           //0x4
    ULONG Flags;                                                            //0x8
    ULONG DebugFlags;                                                       //0xc
    VOID* ConsoleHandle;                                                    //0x10
    ULONG ConsoleFlags;                                                     //0x18
    VOID* StandardInput;                                                    //0x20
    VOID* StandardOutput;                                                   //0x28
    VOID* StandardError;                                                    //0x30
    struct _CURDIR CurrentDirectory;                                        //0x38
    struct _UNICODE_STRING DllPath;                                         //0x50
    struct _UNICODE_STRING ImagePathName;                                   //0x60
    struct _UNICODE_STRING CommandLine;                                     //0x70
    VOID* Environment;                                                      //0x80
    ULONG StartingX;                                                        //0x88
    ULONG StartingY;                                                        //0x8c
    ULONG CountX;                                                           //0x90
    ULONG CountY;                                                           //0x94
    ULONG CountCharsX;                                                      //0x98
    ULONG CountCharsY;                                                      //0x9c
    ULONG FillAttribute;                                                    //0xa0
    ULONG WindowFlags;                                                      //0xa4
    ULONG ShowWindowFlags;                                                  //0xa8
    struct _UNICODE_STRING WindowTitle;                                     //0xb0
    struct _UNICODE_STRING DesktopInfo;                                     //0xc0
    struct _UNICODE_STRING ShellInfo;                                       //0xd0
    struct _UNICODE_STRING RuntimeData;                                     //0xe0
    struct _RTL_DRIVE_LETTER_CURDIR CurrentDirectores[32];                  //0xf0
    ULONGLONG EnvironmentSize;                                              //0x3f0
    ULONGLONG EnvironmentVersion;                                           //0x3f8
    VOID* PackageDependencyData;                                            //0x400
    ULONG ProcessGroupId;                                                   //0x408
    ULONG LoaderThreads;                                                    //0x40c
};
// Some SDKs do not declare this prototype in user-mode headers.
using fnRtlCreateProcessParametersEx = NTSTATUS(NTAPI*)(
    _RTL_USER_PROCESS_PARAMETERSEX* pProcessParameters,
    PUNICODE_STRING ImagePathName,
    PUNICODE_STRING DllPath,
    PUNICODE_STRING CurrentDirectory,
    PUNICODE_STRING CommandLine,
    PVOID Environment,
    PUNICODE_STRING WindowTitle,
    PUNICODE_STRING DesktopInfo,
    PUNICODE_STRING ShellInfo,
    PUNICODE_STRING RuntimeData,
    ULONG Flags
);

using fnRtlDestroyProcessParameters = NTSTATUS(NTAPI*)(_RTL_USER_PROCESS_PARAMETERSEX ProcessParameters);

static UNICODE_STRING MakeUnicodeString(const std::wstring& s)
{
    UNICODE_STRING us{};
    us.Buffer = const_cast<PWSTR>(s.c_str());
    us.Length = static_cast<USHORT>(s.size() * sizeof(wchar_t));
    us.MaximumLength = us.Length + sizeof(wchar_t);
    return us;
}

static void HexDump(const void* data, size_t size)
{
    const auto* p = static_cast<const unsigned char*>(data);
    for (size_t i = 0; i < size; i += 16) {
        std::printf("%08zx  ", i);
        for (size_t j = 0; j < 16; ++j) {
            if (i + j < size) std::printf("%02X ", p[i + j]);
            else std::printf("   ");
        }
        std::printf(" ");
        for (size_t j = 0; j < 16 && i + j < size; ++j) {
            unsigned char c = p[i + j];
            std::printf("%c", (c >= 32 && c <= 126) ? c : '.');
        }
        std::printf("\n");
    }
}

static void PrintUs(const char* name, const UNICODE_STRING& us, const void* base)
{
    const auto baseAddr = reinterpret_cast<uintptr_t>(base);
    const auto bufAddr = reinterpret_cast<uintptr_t>(us.Buffer);
    std::wprintf(L"%hs: Len=%u Max=%u Buf=%p (off=0x%Ix)  \"%.*s\"\n",
        name,
        us.Length,
        us.MaximumLength,
        us.Buffer,
        (bufAddr >= baseAddr) ? (bufAddr - baseAddr) : 0,
        us.Length / 2,
        us.Buffer ? us.Buffer : L"");
}

int wmain()
{
    // Example payload: create cmd.exe parameters (NOT actually launching here).
    std::wstring imagePath = L"\\??\\C:\\Windows\\System32\\cmd.exe";
    std::wstring cmdLine = L"\"C:\\Windows\\System32\\cmd.exe\"";

    UNICODE_STRING usImage = MakeUnicodeString(imagePath);
    UNICODE_STRING usCmd = MakeUnicodeString(cmdLine);

    HMODULE ntdll = ::GetModuleHandleW(L"ntdll.dll");
    if (!ntdll) {
        std::printf("GetModuleHandleW(ntdll) failed: %lu\n", ::GetLastError());
        return 1;
    }

    auto pRtlCreate = reinterpret_cast<fnRtlCreateProcessParametersEx>(
        ::GetProcAddress(ntdll, "RtlCreateProcessParametersEx"));
    auto pRtlDestroy = reinterpret_cast<fnRtlDestroyProcessParameters>(
        ::GetProcAddress(ntdll, "RtlDestroyProcessParameters"));
    if (!pRtlCreate || !pRtl...