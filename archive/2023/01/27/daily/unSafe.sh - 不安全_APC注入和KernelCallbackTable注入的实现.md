---
title: APC注入和KernelCallbackTable注入的实现
url: https://buaq.net/go-146776.html
source: unSafe.sh - 不安全
date: 2023-01-27
fetch_date: 2025-10-04T04:56:39.277606
---

# APC注入和KernelCallbackTable注入的实现

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

![](https://8aqnet.cdn.bcebos.com/f364b68b781570b9d131babb065668a8.jpg)

APC注入和KernelCallbackTable注入的实现

Windows下关于进程的注入方法有很多有几种通用性较强像APC注入和KernelCallbackTable注入。这里结合了实际参考了github代码和一些优化的项
*2023-1-26 21:24:0
Author: [xz.aliyun.com(查看原文)](/jump-146776.htm)
阅读量:36
收藏*

---

Windows下关于进程的注入方法有很多

**APC Code Injection**
首先来介绍一下APC APC注入 和实现的过程中一些细节的地方，比如枚举线程，用户态内核态APC的区别等这样方便更好的理解APC 注入的实现原理和后续改进等。
Windows内核态使用APC来完成异步启动的I/O操作，线程挂起等行为
APC是（Asynchronous Procedure Call）指异步过程调用
APC是允许用户程序和系统组件在特定线程的上下文中执行代码，因此会在特定进程的地址空间内执行代码,与APC注入有关的DLL主要有两个：Kernel32.dll和Ntdll.dll
有关的函数主要有如下这几个

```
CreateToolhelp32Snapshot，Process32First，Process32Next，Thread32First，Thread32Next，OpenProcess，OpenThread，DuplicateHandle，GetCurrentProcess，WriteProcessMemory，VirtualProtectEx，QueueUserAPC，ResumeThread，NtAllocateVirtualMemory
```

以上的函数，在APC注入过程中都会使用到其中有几个在其他注入方法中可能不常见的函数，需要了解一下函数的作用。比如QueueUserAPC --将用户模式 异步过程调用 (APC) 对象添加到指定线程的 APC 队列，ResumeThread --递减线程的挂起计数。 当暂停计数递减为零时，将恢复线程的执行

---

文章来源: https://xz.aliyun.com/t/12070
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)