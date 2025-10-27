---
title: 玄 - 利用DLL通知回调函数注入shellcode（上） - zha0gongz1
url: https://www.cnblogs.com/zha0gongz1/p/17633377.html
source: 博客园 - zha0gongz1
date: 2023-08-18
fetch_date: 2025-10-04T11:58:43.944815
---

# 玄 - 利用DLL通知回调函数注入shellcode（上） - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [玄 - 利用DLL通知回调函数注入shellcode（上）](https://www.cnblogs.com/zha0gongz1/p/17633377.html "发布于 2023-08-18 01:01")

区别传统进程注入执行恶意代码，新技术学习记录 - 在远程目标进程中利用DLL通知回调机制执行shellcode

## 序

偶然看到某国外大佬发布新技术-“Threadless”进程注入技术，据说可过EDR（确实可），总结该技术原理 - 在远程目标进程中利用DLL通知回调机制执行shellcode，项目地址[在这里](https://github.com/ShorSec/DllNotificationInjection)。

传统进程注入四步法：

* 获取远程进程句柄（OpenProcess函数）
* 在远程进程中分配内存（VirtualAllocEx函数）
* 将shellcode复制到远程进程中新分配的内存页中（WriteProcessMemory函数）
* 在远程进程中创建线程执行shellcode（CreateRemoteThread函数）

杀毒软件和EDR产品已经学会通过快速查找这四步操作来概括并检测进程注入。

针对第四步执行shellcode方式，[@CCob](https://github.com/CCob/ThreadlessInject)与[@Kudaes](https://github.com/Kudaes/EPI)相继提出新加载技术 - ThreadlessInject。原理上基本一致，**Hook并修改远程进程中线程创建与销毁过程中DLL加载的入口点，进而加载我们的shellcode**。下面我们逐步剖析学习一下该技术手段。

## 什么是DLL Notification Callbacks？

在 Windows 操作系统中，当一个 DLL（动态链接库）被加载或卸载时，系统会调用一个预先注册的回调函数来通知应用程序。在Windows用户态下，通常使用`LdrRegisterDllNotification`函数来注册回调函数。

*ps:Windows中除了通过上述API函数注册回调函数，还有`PsSetLoadImageNotifyRoutine`函数，该函数允许驱动程序注册一个回调函数，当驱动程序映像或用户映像（DLL、EXE）被映射到虚拟内存中时，系统会调用此回调函数。注意，`PsSetLoadImageNotifyRoutine`函数只能在内核态下使用*

很遗憾，在[微软官方文档](https://learn.microsoft.com/en-us/windows/win32/devnotes/ldrdllnotification)中没有关于`LdrDllNotification`函数的详细资料，只有大致介绍

![](https://img2023.cnblogs.com/blog/1449167/202308/1449167-20230816122027493-83752420.png)

LdrDllNotification函数简介

*ps:通常，一些EDR产品也是使用此函数在用户态下从加载DLL事件中获取监测数据。在@onlymalware截取的[这段代码](https://github.com/rad9800/misc/blob/main/bypasses/UnregisterAllLdrRegisterDllNotification.c)中，可以看到作为攻击方，应如何在自己的进程中取消注册所有`LdrDllNotification`回调函数，从而限制EDR从我们的进程中收集样本数据。*

回归正题，`LdrRegisterDllNotification`函数方法没有相关联的头文件，但是可以通过`LoadLibrary`和`GetProcAddress`进行导入。

![](https://img2023.cnblogs.com/blog/1449167/202308/1449167-20230816130808028-449184252.png)

另外，通过查阅[@modexp文章](https://modexp.wordpress.com/2020/08/06/windows-data-structures-and-callbacks-part-1/#dll)了解到，还需要自己实现函数及其所有相关数据结构，以下是构造的简单示例代码：

```
#include <Windows.h>
#include <stdio.h>

typedef struct _UNICODE_STR
{
    USHORT Length;
    USHORT MaximumLength;
    PWSTR pBuffer;
} UNICODE_STR, * PUNICODE_STR;

typedef struct _LDR_DLL_LOADED_NOTIFICATION_DATA {
    ULONG           Flags;             // Reserved.
    PUNICODE_STR FullDllName;       // The full path name of the DLL module.
    PUNICODE_STR BaseDllName;       // The base file name of the DLL module.
    PVOID           DllBase;           // A pointer to the base address for the DLL in memory.
    ULONG           SizeOfImage;       // The size of the DLL image, in bytes.
} LDR_DLL_LOADED_NOTIFICATION_DATA, * PLDR_DLL_LOADED_NOTIFICATION_DATA;

typedef struct _LDR_DLL_UNLOADED_NOTIFICATION_DATA {
    ULONG           Flags;             // Reserved.
    PUNICODE_STR FullDllName;       // The full path name of the DLL module.
    PUNICODE_STR BaseDllName;       // The base file name of the DLL module.
    PVOID           DllBase;           // A pointer to the base address for the DLL in memory.
    ULONG           SizeOfImage;       // The size of the DLL image, in bytes.
} LDR_DLL_UNLOADED_NOTIFICATION_DATA, * PLDR_DLL_UNLOADED_NOTIFICATION_DATA;

typedef union _LDR_DLL_NOTIFICATION_DATA {
    LDR_DLL_LOADED_NOTIFICATION_DATA   Loaded;
    LDR_DLL_UNLOADED_NOTIFICATION_DATA Unloaded;
} LDR_DLL_NOTIFICATION_DATA, * PLDR_DLL_NOTIFICATION_DATA;

typedef VOID(CALLBACK* PLDR_DLL_NOTIFICATION_FUNCTION)(
    ULONG                       NotificationReason,
    PLDR_DLL_NOTIFICATION_DATA  NotificationData,
    PVOID                       Context);

typedef struct _LDR_DLL_NOTIFICATION_ENTRY {
    LIST_ENTRY                     List;
    PLDR_DLL_NOTIFICATION_FUNCTION Callback;
    PVOID                          Context;
} LDR_DLL_NOTIFICATION_ENTRY, * PLDR_DLL_NOTIFICATION_ENTRY;

typedef NTSTATUS(NTAPI* _LdrRegisterDllNotification) (
    ULONG                          Flags,
    PLDR_DLL_NOTIFICATION_FUNCTION NotificationFunction,
    PVOID                          Context,
    PVOID* Cookie);

typedef NTSTATUS(NTAPI* _LdrUnregisterDllNotification)(PVOID Cookie);

// 回调函数
VOID MyCallback(ULONG NotificationReason, const PLDR_DLL_NOTIFICATION_DATA NotificationData, PVOID Context)
{
    printf("[MyCallback] dll loaded: %Z\n", NotificationData->Loaded.BaseDllName);
}

int main()
{
    // 获取NTDLL句柄
    HMODULE hNtdll = GetModuleHandleA("NTDLL.dll");

    if (hNtdll != NULL) {

        // 找到 LdrUnregisterDllNotification函数地址
        _LdrRegisterDllNotification pLdrRegisterDllNotification = (_LdrRegisterDllNotification)GetProcAddress(hNtdll, "LdrRegisterDllNotification");

        // 将MyCallback函数注册为 DLL 通知回调
        PVOID cookie;
        NTSTATUS status = pLdrRegisterDllNotification(0, (PLDR_DLL_NOTIFICATION_FUNCTION)MyCallback, NULL, &cookie);
        if (status == 0) {
            printf("[+] Successfully registered callback\n");
        }

        //字符中断
        printf("[+] Press enter to continue\n");
        getchar();

        // 加载其他dll来触发回调函数
        printf("[+] Loading USER32 DLL now\n");
        LoadLibraryA("USER32.dll");
    }
}
```

*ps：普及下基础知识，为什么要获取ntdll.dll的句柄？是为了找到 LdrRegisterDllNotification 函数的地址，有且只有 ntdll.dll 库中有 LdrRegisterDllNotification 函数。*

运行截图：
![](https://img2023.cnblogs.com/blog/1449167/202308/1449167-20230816181400454-2131134417.jpg)

上述代码作用大致解释为利用LoadLibraryA("USER32.dll") 加载 USER32.dll 库，触发 DLL 通知回调函数，也就是上面注册的 MyCallback 函数。MyCallback函数将打印出 DLL 的基本名称。

注意：图中出现多个dll加载回调结果是因为 USER32.dll 库依赖于其他 DLL 库，所以在加载 USER32.dll 库时，也会同时加载它所依赖的其他 DLL 库。这些 DLL 库也会触发 DLL 通知回调函数，并打印出它们的基本名称到控制台，所以除了 USER32.dll 的基本名称之外，还打印出了其他 DLL 库的基本名称。

## 注册自定义回调函数

在当前进程中操纵注册自己的DLL通知回调函数，首先要找到它在内存中的位置。 查阅函数定义，获取的唯一返回值（除了 NTSTATUS）是一个指向`Cookie`的指针，与`LdrUnregisterDllNotification`的`Cookie`一样（`LdrUnregisterDllNotification`函数是帮助我们删除特定的回调函数）。

关于Cookie指针的解释：**Cookie指针实际上是一个指向`LDR_DLL_NOTIFICATION_ENTRY`的指针，它保存了与我们注册的回调函数相关的所有数据，包括指向回调函数本身的指针和指向回调函数上下文的指针（在本例中未使用）**。 `_LDR_DLL_NOTIFICATION_ENTRY`还包含一个`LIST_ENTRY`结构，该结构指向进程中注册的其余回调函数。

```
     LdrpDllNotificationList                                         Cookie
     │                                                               │
     ▼                                                               ▼
    ┌─────┐  ┌────────────────────┐  ┌────────────────────┐  ┌───┐  ┌────────────────────┐
┌──►│Flink├─►│Flink               ├─►│Flink               ├─►│   ├─►│Flink               ├───┐
│   ├─────┤  ├────────────────────┤  ├────────...