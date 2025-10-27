---
title: BugChecker - SoftICE-like Kernel Debugger For Windows 11
url: https://buaq.net/go-171294.html
source: unSafe.sh - 不安全
date: 2023-07-06
fetch_date: 2025-10-04T11:51:25.222144
---

# BugChecker - SoftICE-like Kernel Debugger For Windows 11

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

![](https://8aqnet.cdn.bcebos.com/17209ab0db1bd242e19d1a180d0631ee.jpg)

BugChecker - SoftICE-like Kernel Debugger For Windows 11

Introduction BugChecker is a SoftICE-like kernel and user debugger for Windows 11 (and Wi
*2023-7-5 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171294.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiiIADjrRs_TLCBefDgik1GdLQBAklt0r9ebRvY1ZNZ0WA2l-JWEaG3A2AD1KxAnV13lQGSha1CQULbvt6RcTe-553H_zXXpwhqwhJJcWyT83UKSpFGU3f2NCuIB8s5lAao21eAafgsCvnREGQ9dBYaodaogfs24EBn1-iBWpwSuW36frVwTH0mPV2qZA=w640-h480)](https://blogger.googleusercontent.com/img/a/AVvXsEiiIADjrRs_TLCBefDgik1GdLQBAklt0r9ebRvY1ZNZ0WA2l-JWEaG3A2AD1KxAnV13lQGSha1CQULbvt6RcTe-553H_zXXpwhqwhJJcWyT83UKSpFGU3f2NCuIB8s5lAao21eAafgsCvnREGQ9dBYaodaogfs24EBn1-iBWpwSuW36frVwTH0mPV2qZA)

## Introduction

BugChecker is a [SoftICE](https://en.wikipedia.org/wiki/SoftICE "SoftICE")-like kernel and user debugger for Windows 11 (and Windows XP as well: it supports Windows versions from XP to 11, both x86 and x64). BugChecker doesn't require a second machine to be connected to the system being debugged, like in the case of WinDbg and KD. This version of BugChecker (unlike the [original version](https://github.com/vitoplantamura/BugChecker2002 "original version") developed 20 years ago) leverages the internal and undocumented KD API in NTOSKRNL. KD API allows WinDbg/KD to do calls like read/write virtual memory, read/write registers, place a breakpoint at an address etc.

By contrast, the original BugChecker, like SoftICE as well, used to "take over" the system, by hooking several kernel APIs (both exported and private), taking control of the APIC, sending IPIs etc. This approach increases complexity exponentially (and lowers system stability), since the implementation must be compatible with all the supported versions and sub-version of Windows (at the function signature level) as well as all the possible supported hardware configurations. Moreover, 20 years later, PatchGuard makes this solution impossible.

By contrast, this version of BugChecker, by intercepting calls to KdSendPacket and KdReceivePacket in the kernel, presents itself to the machine being debugged as a second system running an external kernel debugger, but, in reality, everything happens on the same machine. Typically this is achieved by [replacing KDCOM.DLL](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/kdserial-extensibility-code-samples "replacing KDCOM.DLL") (which is the module that implements serial cable communication for the KD API in Windows) and by starting the system in kernel debugging mode. This approach (inspired by [VirtualKD](https://github.com/4d61726b/VirtualKD-Redux "VirtualKD")) lowers complexity and increases stability and compatibility (and portability, for example, to ARM - and modularity, since the lower level debugger capabilities are implemented behind KdXxxPacket and could be replaced with a custom implementation). Moreover, the presence of a kernel debugger at boot time (although "fake") makes Windows disable PatchGuard.

At the moment, BugChecker requires a PS/2 keyboard for input and a linear framebuffer to write its output.

## Features

* Support for Windows XP up to Windows 11, x86 and x64, and SMP kernels. Support for WOW64 processes on x64.
* Integration of [QuickJSPP](https://github.com/c-smile/quickjspp "QuickJSPP"), which is a port of [QuickJS](https://bellard.org/quickjs/ "QuickJS") to MSVC++. Before calling QuickJS, BugChecker saves the FPU state (on x86) and switches to an expanded stack of 128KB.
* Commands accept JS expressions. For example, "U rip+rax\*4" and "U MyJsFn(rax+2)" are valid commands. Custom functions can be defined in the Script Window. CPU registers are declared as global scope variables automatically by BugChecker.
* Support for PDB symbol files. PDB files can be specified manually or Symbol Loader can download them from a symbol server.
* JavaScript code can call the following [asynchronous](https://www.kitploit.com/search/label/Asynchronous "asynchronous") functions: WriteReg, ReadMem, WriteMem.
* Breakpoints can have a JS condition: if condition evaluates to 0, no "breakin" happens. This allows to set "Logpoints" and breakpoints that can change the flow of execution.
* Log window shows the messages sent to the kernel debugger (for example DbgPrint messages).
* JavaScript window with syntax highlighting.
* The tab key allows, given few digits, to cycle through all the hex numbers on the screen or, given few characters, to cycle through all the symbols containing those characters.
* EASTL and C++20 coroutines make creating new commands a breeze. **Feel free to send your pull requests!**

## Videos (Youtube)

Demonstration of BugChecker on Windows 11 22H2, inside VirtualBox 7.0.4. A JavaScript breakpoint condition is written that changes the flow of execution in an user mode thread.

BugChecker running in a very constrained environment: a [Raspberry Pi](https://www.kitploit.com/search/label/Raspberry%20Pi "Raspberry Pi") 4 (4GB RAM), via QEMU on Windows XP (512MB RAM). A breakpoint is used to log all the SYSENTER calls from user mode to the kernel. The service index is stored in a JavaScript array.

Running BugChecker directly on bare metal, on an HP Pavilion Dv2000, which is an old PC with a PS/2 keyboard. The OS is Windows 7 Home 32bit.

## Installation Instructions

### Introduction

Make sure that [Secure Boot](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot "Secure Boot") is disabled when installing and using BugChecker. Typically you can re-enable it later. If you are using VMware or VirtualBox, Secure Boot can be disabled in the [virtual machine](https://www.kitploit.com/search/label/Virtual%20Machine "virtual machine") settings.

Consider also enabling legacy boot menu, if using Windows 8, 10 or 11, by using the command: **bcdedit /set "{current}" bootmenupolicy legacy**. It allows a smoother experience during boot, by allowing to select the BugChecker boot option and then to disable Driver Signature Enforcement at the same time.

### Instructions

The first step is to start Symbol Loader:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjzURfL6RBd2TFIgKu8YC6S6nAjN2qRzWBHFFYfoGYcgdY5q2kixPlS-MGmjmOPZH1SZ8xaOEz8tPfLuDN-ORA0xbmmLnkJ62BdaSmpJpYV1gH19Lenx4ZSNcjxA8H7gk52Hs-ekhvamw1ZVg9pzUURqmb3JiHNZnKdp2mNDQbtdPtzeULHuuFHbOxV-w=w626-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEjzURfL6RBd2TFIgKu8YC6S6nAjN2qRzWBHFFYfoGYcgdY5q2kixPlS-MGmjmOPZH1SZ8xaOEz8tPfLuDN-ORA0xbmmLnkJ62BdaSmpJpYV1gH19Lenx4ZSNcjxA8H7gk52Hs-ekhvamw1ZVg9pzUURqmb3JiHNZnKdp2mNDQbtdPtzeULHuuFHbOxV-w)

If necessary, disable the display drivers, by clicking on the "Disable Display Drvs" button. The same thing can be accomplished in Windows Device Manager. After the display drivers have been disabled, they remain disabled even after a system reboot. They can be re-enabled at any time later when not using BugChecker.

The point here is that BugChecker needs a linear framebuffer with a format of 32 bits-per-pixel, to draw its interface. When disabling the display drivers, Windows dismisses hardware acceleration for drawing its UI and falls back to VGA compatibility mode. If running on bare metal or VMware, you should disable display drivers. If running on VirtualBox, you should disable display drivers or set the vm\_screen setting in BugChecker.dat, as described below. If running on QEMU, you don't need to disable display drivers but make sure to specify the "-vga std" display device.

Note that VGA compatibility mode could limit the ...