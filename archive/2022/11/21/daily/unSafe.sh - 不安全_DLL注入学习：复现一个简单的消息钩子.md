---
title: DLL注入学习：复现一个简单的消息钩子
url: https://buaq.net/go-136474.html
source: unSafe.sh - 不安全
date: 2022-11-21
fetch_date: 2025-10-03T23:18:58.995640
---

# DLL注入学习：复现一个简单的消息钩子

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9086bcc13a192d66c37061edf9aa47de.jpg)

DLL注入学习：复现一个简单的消息钩子

这篇文章开始进入DLL注入和API钩取的部分，首先来看一下什么叫做DLL注入：顾名思义，DLL注入是将某些DLL（动态链接库）强行加载到某个程序的进程中，从而完成
*2022-11-20 11:54:35
Author: [xz.aliyun.com(查看原文)](/jump-136474.htm)
阅读量:28
收藏*

---

这篇文章开始进入DLL注入和API钩取的部分，首先来看一下什么叫做DLL注入：

顾名思义，DLL注入是将某些DLL（动态链接库）强行加载到某个程序的进程中，从而完成某些特定的功能，。DLL注入与普通的DLL 加载的区别在于，加载的目标是其自身或者其他特定程序，而注入的目标是强制在某个进程中插入自定义的DLL。

在DLL注入的过程中，会频繁地接触到钩子这个概念，也就是Hook这个操作。

钩子的主要作用就是将消息和进程钩取过来，对于被钩取到的消息和进程，我们可以自己写程序对其进行一些修改或者查看，这样就完成了对于程序原本功能的修改。

本文要实现的功能主要依托于Windows中的消息钩子。Windows为用于提供了相当完备的GUI（图形化操作界面），而用户通过鼠标，键盘，光驱等外设与系统进行交互。在Windows中，每一次鼠标点击和键盘输入都可以被叫做是一个事件，Windows就是基于这些事件驱动的系统。

当按下键盘上的某个键时，这个键被按下的消息传递到Windows的事件队列中等待处理，这时的键盘事件还没有进入到应用程序加以处理，而在系统消息队列和应用之间就是架设消息钩子的空间，在这里可以通过钩子钩取即将被传入应用的事件并加以处理，大概流程如下图：

![](https://xzfile.aliyuncs.com/media/upload/picture/20221120114937-5a92b278-6886-1.png)

下面就对钩取键盘消息进行实际操作，开始之前先要准备一个进程查看器：Process Explorer，这个进程查看器功能相当强大，可以看到进程都加载了哪些DLL，以及某个DLL被哪些进程加载过。本次操作是基于notepad.exe（也就是记事本软件）的DLL注入

（下载链接放在文末）

## KeyHook.cpp：

首先来看一下完成主要功能的动态链接库，也就是后面将注入notepad.exe的DLL文件。下面先给出源码，然后在分析源码中用到的API：

```
#include "stdio.h"
#include "windows.h"

#define PROCESS_NAME "notepad.exe"

HINSTANCE g_hInstance = NULL;
HHOOK g_Hook = NULL;
HWND g_hWnd = NULL;

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    switch (fdwReason)
    {
    case DLL_PROCESS_ATTACH:
        g_hInstance = hinstDLL;
        break;
    case DLL_PROCESS_DETACH:
        break;
    default:
        break;
    }
    return TRUE;
}

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam)
{
    char szPath[MAX_PATH] = { 0, };
    char* p = NULL;
    if (nCode >= 0)
    {
        if (!(lParam & 0x80000000))
        {
            GetModuleFileNameA(NULL, szPath, MAX_PATH);
            p = strrchr(szPath, '\\');

            if (!_stricmp(p + 1, PROCESS_NAME))
            {
                return 1;
            }
        }
    }
    return CallNextHookEx(g_Hook, nCode, wParam, lParam);
}
#ifdef __cplusplus
extern "C" {
#endif // __cplusplus
    __declspec(dllexport) void HookStart()
    {
        g_Hook = SetWindowsHookEx(WH_KEYBOARD, KeyboardProc, g_hInstance, 0);
    }
    __declspec(dllexport) void HookStop()
    {
        if (g_Hook)
        {
            UnhookWindowsHookEx(g_Hook);
            g_Hook = NULL;
        }
    }
#ifdef __cplusplus
}
#endif // __cplusplus
```

其实程序的逻辑非常简单，大概如下：

1. 创建DLL入口点，当遇到DLL\_PROCESS\_ATTACH事件时获取DLL进程的实例化句柄
2. 构造一个KeyboardProc回调函数，根据获取到的消息进行操作
3. 使用前面获得的实例化句柄和回调函数创建钩子进程
4. 程序结束时卸载钩子进程

下面来具体分析每个部分

### DLL入口点函数：

在自己编写DLL的过程中，要注意程序的入口点函数是一个固定的模式，这个模式可以在MSDN（Windows的官方帮助文档）上查到，如下：

```
BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,  // handle to DLL module
    DWORD fdwReason,     // reason for calling function
    LPVOID lpvReserved )  // reserved
{
    // Perform actions based on the reason for calling.
    switch( fdwReason )
    {
        case DLL_PROCESS_ATTACH:
         // Initialize once for each new process.
         // Return FALSE to fail DLL load.
            break;

        case DLL_THREAD_ATTACH:
         // Do thread-specific initialization.
            break;

        case DLL_THREAD_DETACH:
         // Do thread-specific cleanup.
            break;

        case DLL_PROCESS_DETACH:

            if (lpvReserved != nullptr)
            {
                break; // do not do cleanup if process termination scenario
            }

         // Perform any necessary cleanup.
            break;
    }
    return TRUE;  // Successful DLL_PROCESS_ATTACH.
}
```

当主程序在调用LoadLibrary和FreeLibrary时，BOOL WINAPI DllMain就是DLL程序开始的地方。

在DllMain函数中有三个参数，分别是：

* hinstDLL：DLL模块的实例化句柄，也就是DLL加载时的基址
* fdwReason：标识调用DLL入口点函数的原因，有0、1、2、3这个四个值，对应四种不同情况。本次复现主要接触到的是值为0和1时的两种情况（2和3的情况在后面学习线程注入时会接触到）：
  + 值为1：对应**DLL\_PROCESS\_ATTACH**，进程使用LoadLibrary加载DLL时（也就是DLL模块被加载入虚拟地址空间时），系统会接收到这个消息
  + 值为0：对应**DLL\_PROCESS\_DETACH**，当进程使用FreeLibrary卸载掉DLL时（也就是DLL模块被从虚拟空间中卸载时），系统会受到这个消息
* lpvReserved：用于指示DLL是静态加载还是动态加载

在函数内部是一个Switch选择结构，根据fdwReason（也就是DLL的加载情况）执行相应操作，本次的复现中采用的是最简单的一种：也就是当DLL模块加载成功时将DLL的实例化句柄赋值给全局变量hInstance。这部分的代码及注释如下：

```
HINSTANCE g_hInstance = NULL; //实例化句柄类型，简单理解为内存分配了的资源ID
HHOOK g_Hook = NULL; //钩子的句柄
HWND g_hWnd = NULL; //窗口句柄

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) //DLL入口点函数
{
    switch (fdwReason)
    {
    case DLL_PROCESS_ATTACH: //当系统事件为DLL被初次映射到内存中时
        g_hInstance = hinstDLL; //前面的实例化句柄被赋值为DLLMain的模块句柄
        break;
    case DLL_PROCESS_DETACH:
        break;
    default:
        break;
    }
    return TRUE;
}
```

### KeyboardProc回调函数：

KeyboardProc，也就是键盘消息进程的函数，它是一个回调函数，它作为参数在SetWindowsHookEx这个API中使用，这个回调函数也有一个比较固定的模板，在MSDN上可以查到：

```
LRESULT CALLBACK KeyboardProc(
  _In_ int    code,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

有三个参数：

* code：这个参数的值决定如何处理消息，分为0、3和小于0两种情况

  + 小于0：必须调用CallNextHookEx函数传递消息（也就是传递给钩链中的下一个钩子），且不能做过多操作
  + 0：表示参数wParam和lParam 包含关于虚拟键值相关信息（正常输入的情况下就是这个值）
  + 3：在值为0的基础上，表示这个消息被某个进程用PeekMessage查看过
* wParam：按下键盘的按键后生成的虚拟键值，用于判断按下了哪个键
* lParam：这是一个组合值，它的每个不同的bit位代表不同的情况，具体可以在官方文档中查看，本次复现主要关注它的第31位bit位：

| 31 | 转换状态。 如果按下键，则值为 0;如果正在释放键，则值为 1。 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |

这一部分的代码和注释如下：

```
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam)
//nCode:确定如何处理消息的代码 wParam：获取键盘输入的虚拟键值，lParam：扩展键值，比较复杂，这里不多解释
{
    char szPath[MAX_PATH] = { 0, };
    //TCHAR szPath[MAX_PATH] = { 0, };
    char* p = NULL;
    if (nCode >= 0) //nCode大于0时表明接收到键盘消息是正常的
    {
        if (!(lParam & 0x80000000)) //lParam的第31位bit位的值代表按键是按下还是释放，0->press 1->release
        {
            GetModuleFileNameA(NULL, szPath, MAX_PATH);
            p = strrchr(szPath, '\\'); //如果使用TCHAR的字符数组要把项目使用的字符集改为多字节字符集
            //strrchr函数：在一个字符串中查找目标字符串末次出现的位置
            if (!_stricmp(p + 1, PROCESS_NAME)) //判断当前进程是否为notepad
            //stricmp函数：比较两个字符串，比较过程不区分大小写
             {
                return 1;
            }
        }
    }
    return CallNextHookEx(g_Hook, nCode, wParam, lParam); //如果当前进程是notepad就将消息传递给下一个程序
}
```

### 导出函数HookStart()与HookStop()：

这两个函数就是后面将被导出到主程序中使用的开启Hook和卸载Hook的函数，本次的复现中写的很简单，就是调用了一个建立钩子进程的API，但是还有些地方需要注意

在我们使用VS编写DLL时，生成的源文件后缀是.cpp，也就是C++文件，但是有些函数是只能在C语言下解析，所以我们使用C++中解析C语言的一个模式：

```
#ifdef __cplusplus
extern "C" {
#endif // __cplusplus
.
.
.
#ifdef __cplusplus
}
#endif // __cplusplus
```

当我们需要在DLL中导出函数时，要用一个前缀标识这个函数为导出函数，如下：

```
__declspec(dllexport)
```

这个前缀标识后面的函数为DLL的导出函数，默认的调用约定是\_srdcall

在HookStart创建钩子进程时会调用一个API：SetWindowsHookEx，它在MSDN中可以查询到：

```
HHOOK SetWindowsHookExA(
  [in] int       idHook,
  [in] HOOKPROC  lpfn,
  [in] HINSTANCE hmod,
  [in] DWORD     dwThreadId
);
```

拥有四个参数：

* idHook：表示需要安装的挂钩进程的类型，有很多，具体可以在MSDN上查，这次主要使用**WH\_KEYBOARD**这个类型（安装监视击键消息的挂钩过程）
* lpfn：指向钩子过程的指针
* hmod：关于钩子进程的实例化句柄
* dwThreadId：指向一个线程标识符，如果当前的钩子进程与现存的线程相关，那么它的值就是0

这一部分的代码及注释如下：

```
#ifdef __cplusplus
extern "C" { //后面的导出函数将使用C语言进行解析
#endif // __cplusplus
    __declspec(dllexport) void HookStart() //创建钩子进程
    {
        g_Hook = SetWindowsHookEx(WH_KEYBOARD, KeyboardProc, g_hInstance, 0); //创建钩子进程
    }
    __declspec(dllexport) void HookStop() //卸载钩子进程
    {
        if (g_Hook)
        {
            UnhookWindowsHookEx(g_Hook); //卸载钩子进程
            g_Hook = NULL;
        }
    }
#ifdef __cplusplus
}
#endif // __cplusplus
```

## WindowsMessageHook：

还是先看总的源码：

```
#include"stdio.h"
#include"Windows.h"
#include"conio.h"

#define DLL_NAME "KeyHook.dll"
#define HOOKSTART "HookStart"
#define HOOKSTOP "HookStop"

typedef void(*FN_HOOKSTART)();
typedef void(*FN_HOOKSTOP)();

void main()
{
    HMODULE hDll = NULL;
    FN_HOOKSTART HookStart = NULL...