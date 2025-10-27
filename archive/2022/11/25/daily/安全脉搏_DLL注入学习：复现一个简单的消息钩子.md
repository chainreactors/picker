---
title: DLL注入学习：复现一个简单的消息钩子
url: https://www.secpulse.com/archives/192067.html
source: 安全脉搏
date: 2022-11-25
fetch_date: 2025-10-03T23:43:04.060598
---

# DLL注入学习：复现一个简单的消息钩子

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# DLL注入学习：复现一个简单的消息钩子

[漏洞复现](https://www.secpulse.com/archives/category/articles/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-24

10,790

# 文章转载自先知社区：

# https://xz.aliyun.com/t/11863

# 作者：Youngmith

#

# 概述：

这篇文章开始进入DLL注入和API钩取的部分，首先来看一下什么叫做DLL注入：

顾名思义，DLL注入是将某些DLL（动态链接库）强行加载到某个程序的进程中，从而完成某些特定的功能，。DLL注入与普通的DLL 加载的区别在于，加载的目标是其自身或者其他特定程序，而注入的目标是强制在某个进程中插入自定义的DLL。

在DLL注入的过程中，会频繁地接触到钩子这个概念，也就是Hook这个操作。

钩子的主要作用就是将消息和进程钩取过来，对于被钩取到的消息和进程，我们可以自己写程序对其进行一些修改或者查看，这样就完成了对于程序原本功能的修改。

# 消息钩子：

本文要实现的功能主要依托于Windows中的消息钩子。Windows为用于提供了相当完备的GUI（图形化操作界面），而用户通过鼠标，键盘，光驱等外设与系统进行交互。在Windows中，每一次鼠标点击和键盘输入都可以被叫做是一个事件，Windows就是基于这些事件驱动的系统。

当按下键盘上的某个键时，这个键被按下的消息传递到Windows的事件队列中等待处理，这时的键盘事件还没有进入到应用程序加以处理，而在系统消息队列和应用之间就是架设消息钩子的空间，在这里可以通过钩子钩取即将被传入应用的事件并加以处理，大概流程如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192067-1669276654.png)

# 钩取键盘消息：

下面就对钩取键盘消息进行实际操作，开始之前先要准备一个进程查看器：Process Explorer，这个进程查看器功能相当强大，可以看到进程都加载了哪些DLL，以及某个DLL被哪些进程加载过。本次操作是基于notepad.exe（也就是记事本软件）的DLL注入

（下载链接放在文末）

## KeyHook.cpp：

首先来看一下完成主要功能的动态链接库，也就是后面将注入notepad.exe的DLL文件。下面先给出源码，然后在分析源码中用到的API：

```
#include "stdio.h"#include "windows.h"
#define PROCESS_NAME "notepad.exe"
HINSTANCE g_hInstance = NULL; HHOOK g_Hook = NULL; HWND g_hWnd = NULL;
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {    switch (fdwReason)    {    case DLL_PROCESS_ATTACH:        g_hInstance = hinstDLL;        break;    case DLL_PROCESS_DETACH:        break;    default:        break;    }    return TRUE;}
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam){    char szPath[MAX_PATH] = { 0, };    char* p = NULL;    if (nCode >= 0)    {        if (!(lParam & 0x80000000))        {            GetModuleFileNameA(NULL, szPath, MAX_PATH);            p = strrchr(szPath, '\\');
            if (!_stricmp(p + 1, PROCESS_NAME))            {                return 1;            }        }    }    return CallNextHookEx(g_Hook, nCode, wParam, lParam);}#ifdef __cplusplusextern "C" {#endif // __cplusplus    __declspec(dllexport) void HookStart(){        g_Hook = SetWindowsHookEx(WH_KEYBOARD, KeyboardProc, g_hInstance, 0);    }    __declspec(dllexport) void HookStop(){        if (g_Hook)        {            UnhookWindowsHookEx(g_Hook);            g_Hook = NULL;        }    }#ifdef __cplusplus}#endif // __cplusplus
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
BOOL WINAPI DllMain(    HINSTANCE hinstDLL,  // handle to DLL module    DWORD fdwReason,     // reason for calling function    LPVOID lpvReserved )  // reserved{    // Perform actions based on the reason for calling.    switch( fdwReason )     {         case DLL_PROCESS_ATTACH:         // Initialize once for each new process.         // Return FALSE to fail DLL load.            break;
        case DLL_THREAD_ATTACH:         // Do thread-specific initialization.            break;
        case DLL_THREAD_DETACH:         // Do thread-specific cleanup.            break;
        case DLL_PROCESS_DETACH:
            if (lpvReserved != nullptr)            {                break; // do not do cleanup if process termination scenario            }
         // Perform any necessary cleanup.            break;    }    return TRUE;  // Successful DLL_PROCESS_ATTACH.}
```

当主程序在调用LoadLibrary和FreeLibrary时，BOOL WINAPI DllMain就是DLL程序开始的地方。

在DllMain函数中有三个参数，分别是：

* hinstDLL：DLL模块的实例化句柄，也就是DLL加载时的基址
* fdwReason：标识调用DLL入口点函数的原因，有0、1、2、3这个四个值，对应四种不同情况。本次复现主要接触到的是值为0和1时的两种情况（2和3的情况在后面学习线程注入时会接触到）：

+ 值为1：对应**DLL\_PROCESS\_ATTACH**，进程使用LoadLibrary加载DLL时（也就是DLL模块被加载入虚拟地址空间时），系统会接收到这个消息
+ 值为0：对应**DLL\_PROCESS\_DETACH**，当进程使用FreeLibrary卸载掉DLL时（也就是DLL模块被从虚拟空间中卸载时），系统会受到这个消息

* lpvReserved：用于指示DLL是静态加载还是动态加载

在函数内部是一个Switch选择结构，根据fdwReason（也就是DLL的加载情况）执行相应操作，本次的复现中采用的是最简单的一种：也就是当DLL模块加载成功时将DLL的实例化句柄赋值给全局变量hInstance。这部分的代码及注释如下：

据fdwReason（也就是DLL的加载情况）执行相应操作，本次的复现中采用的是最简单的一种：也就是当DLL模块加载成功时将DLL的实例化句柄赋值给全局变量hInstance。这部分的代码及注释如下：

```
HINSTANCE g_hInstance = NULL; //实例化句柄类型，简单理解为内存分配了的资源IDHHOOK g_Hook = NULL; //钩子的句柄HWND g_hWnd = NULL; //窗口句柄
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) //DLL入口点函数{    switch (fdwReason)    {    case DLL_PROCESS_ATTACH: //当系统事件为DLL被初次映射到内存中时        g_hInstance = hinstDLL; //前面的实例化句柄被赋值为DLLMain的模块句柄        break;    case DLL_PROCESS_DETACH:        break;    default:        break;    }    return TRUE;}
```

### KeyboardProc回调函数：

KeyboardProc，也就是键盘消息进程的函数，它是一个回调函数，它作为参数在SetWindowsHookEx这个API中使用，这个回调函数也有一个比较固定的模板，在MSDN上可以查到：

```
LRESULT CALLBACK KeyboardProc(
  _In_ int    code,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

有三个参数：

* code：这个参数的值决定如何处理消息，分为0、3和小于0两种情况

+ 小于0：必须调用CallNextHookEx函数传递消息（也就是传递给钩链中的下一个钩子），且不能做过多操作
+ 0：表示参数wParam和lParam 包含关于虚拟键值相关信息（正常输入的情况下就是这个值）
+ 3：在值为0的基础上，表示这个消息被某个进程用PeekMessage查看过

* wParam：按下键盘的按键后生成的虚拟键值，用于判断按下了哪个键
* lParam：这是一个组合值，它的每个不同的bit位代表不同的情况，具体可以在官方文档中查看，本次复现主要关注它的第31位bit位：

| 31 | 转换状态。如果按下键，则值为 0;如果正在释放键，则值为 1。 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

这一部分的代码和注释如下：

```
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam)//nCode:确定如何处理消息的代码 wParam：获取键盘输入的虚拟键值，lParam：扩展键值，比较复杂，这里不多解释{    char szPath[MAX_PATH] = { 0, };    //TCHAR szPath[MAX_PATH] = { 0, };    char* p = NULL;    if (nCode >= 0) //nCode大于0时表明接收到键盘消息是正常的    {        if (!(lParam & 0x80000000)) //lParam的第31位bit位的值代表按键是按下还是释放，0->press 1->release        {            GetModuleFileNameA(NULL, szPath, MAX_PAT...