---
title: 手把手教会你白加黑无敌免杀（附工具和源码）
url: https://mp.weixin.qq.com/s/C9EyxOLYamhh145rvViJBw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:36:34.507673
---

# 手把手教会你白加黑无敌免杀（附工具和源码）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxPDo2LOsdDiaPtuZuzrdqdkt0dOSyFHKhrHicH3QgrsfkpL4b2Zzh2jSA/0?wx_fmt=jpeg)

# 手把手教会你白加黑无敌免杀（附工具和源码）

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg)

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

### **前言**

最近看到微步的一篇文章，里面提到“白文件+黑 DLL”组合的利用思路，引发了我的兴趣。起初我以为实现并不复杂，但真正动手尝试后，才发现过程中有不少坑点：

* 关于 DLL 编写的资料零散且不够系统；
* 在 `DllMain` 中直接执行代码时容易出现死锁；
* 如何正确挂接主线程逻辑也需要反复调试。

经过一番研究，我逐步解决了这些问题，并成功完成了实验。在过程中也发现，虽然“白+黑”方式在设计上较为简单高效，但要想稳定运行仍然需要不少细节打磨。

接下来的文章将会从 **DLL 开发基础** 开始讲起，结合实践经验，介绍：

* 如何着手开发和调试 DLL；
* 在不同入口点执行逻辑的差异；
* `DllMain` 与导出函数中加载逻辑的不同方式；
* 以及常见问题与对应的解决思路。

希望这份总结能为刚接触 DLL 技术的朋友提供一些思路，避免在入门阶段踩过多的坑。

### **一、dll 开发前置知识**

动态链接库（Dynamic Link Library，简称 **DLL**）是 Windows 操作系统中的一种共享组件文件，它内部包含了可供多个程序调用的函数、数据和资源。与可执行文件（EXE）一样，DLL 也是一种 **PE（Portable Executable）文件格式**。

当应用程序需要使用某个功能时，并不需要一开始就把所有代码加载进内存，而是会在需要时才加载对应的 DLL，并获取其中目标函数的入口地址，再进行调用。通过这种方式，程序可以更高效地运行，同时也便于多个程序共享相同的功能模块，减少重复开发和资源占用。

#### **1. VS目录结构**

首先我们打开vs2022新建一个动态链接库：

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxqglWxDiaWIvlR8hDyn18tibUHEXf3QYkxEHWiaw35v2TSWyzZxJhmMyDA/640?wx_fmt=png&from=appmsg)

可以看到有如下目录结构，可以看到有framework.h、pch.h、dllmain.cpp、pch.cpp四个文件：

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxcYBb5ibauFkGPlkeXhDdNJ44jlEmtJh6DD2BlWz0TjjiaULc2jQtu36Q/640?wx_fmt=png&from=appmsg)

##### **（1）framework.h 文件**

framework.h 文件用于包含项目中需要使用的头文件，可以看到已经默认包含了windows头文件：

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxKkjN85gF5ds0TqNzrWuydb1cubYlib0daicD4d7cq9SZCn9Q9XtclyDQ/640?wx_fmt=png&from=appmsg)

##### **（2）pch.h 文件**

pch.h 是预编译标头文件，dll的导出函数应该在此处定义：

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxucpwCV0kmmeFVr0popoZvGBIx6R0A2szbr9OOmjS8MUZI8RtzdmSbA/640?wx_fmt=png&from=appmsg)

##### **（3）dllmain.cpp 文件**

dllmain.cpp 文件包含程序的入口点，在 dllmain.cpp 中实现的在 pch.h 中定义函数，当然也可以在其他 cpp 文件中实现，如 pch.cpp 等。

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwx5Nib56sQrvg7q13AjeSiaqH24aRicTXHEefia4InV9R8MVtdwNm9KWqa4w/640?wx_fmt=png&from=appmsg)

#### **2. 入口函数（DllMain）**

DllMain是动态链接库的可选入口点。当系统启动或终止进程或线程时，它会使用进程的第一个线程为每个加载的 dll 调用入口点函数。当 dll 使用 LoadLibrary(Ex) 加载和使用 FreeLibrary 函数卸载 dll 时，系统还会调用该函数的入口点函数。

##### **（1）DllMain 示例**

DllMain函数结构如下：

运行

```
/*
* hModule：DLL模块句柄
* ul_reason_for_call：调用函数的原因
* lpReserved：保留参数
*/
BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
      case DLL_PROCESS_ATTACH: // 当DLL被进程加载时执行，每个新进程只初始化一次。
      case DLL_THREAD_ATTACH: // 当线程被创建时调用
      case DLL_THREAD_DETACH: // 当线程结束时执行
      case DLL_PROCESS_DETACH: // 当DLL被进程卸载时执行
            if (lpvReserved != nullptr)
            {
                break; // lpvReserved为非空时，表示进程被终止，不做任何清理
            }
            // 执行必要的清理
          break;
    }
    return TRUE; // DLL_PROCESS_ATTACH成功
}
```

##### **（2）DLL\_PROCESS\_ATTACH**

当一个 dll 文件被映射到进程的地址空间时，系统调用该 dll 的 DllMain 函数，传递的 fdwReason 参数为DLL\_PROCESS\_ATTACH，该值只会被传递一次。

一个程序要调用DLL里的函数，首先要先把DLL文件映射到进程的地址空间。要把一个 dll 文件映射到进程的地址空间，有两种方法：静态链接（.lib）和使用 LoadLibrary(Ex) 方法加载的动态链接。

##### **（3）DLL\_PROCESS\_DETACH**

当 dll 被从进程的地址空间解除映射时调用。

以下情况 dll 会被从进程的地址空间中解除映射：

* 调用 FreeLibrary
* 进程结束
* 传入 DLL\_PROCESS\_ATTACH 的 DllMain 返回 FALSE

如果调用了 TerminateProcess() 终结进程，则不会传入 DLL\_PROCESS\_DETACH 做任何清理工作。

##### **（4）DLL\_THREAD\_ATTACH**

当进程创建一线程时调用，与 DLL\_PROCESS\_ATTACH 不同，该值可被多次调用。

当进程创建一线程时，系统查看当前映射到进程地址空间中的所有 dll 文件映像，并用值 DLL\_THREAD\_ATTACH 调用 dll 的 DllMain 函数。新创建的线程负责执行这次的 dll 的 DllMain 函数，只有当所有的 dll 都处理完这一通知后，系统才允许进程开始执行它的线程函数。

##### **（5）DLL\_THREAD\_DETACH**

当线程调用了 ExitThread 来结束线程（线程函数返回）时调用。如果调用了 TerminateThread() 终结线程，则不会传入 DLL\_THREAD\_DETACH 做任何清理工作。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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