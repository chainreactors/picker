---
title: Blowing Cobalt Strike Out of the Water With Memory Analysis
url: https://buaq.net/go-138315.html
source: unSafe.sh - 不安全
date: 2022-12-03
fetch_date: 2025-10-04T00:22:59.349602
---

# Blowing Cobalt Strike Out of the Water With Memory Analysis

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

![](https://8aqnet.cdn.bcebos.com/1a99b16a6d91af164a41bafeb1dbc1d2.jpg)

Blowing Cobalt Strike Out of the Water With Memory Analysis

Executive SummaryUnit 42 res
*2022-12-2 22:0:0
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-138315.htm)
阅读量:50
收藏*

---

![Conceptual image representing evasive malware such as Cobalt Strike](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Malware-r3d3.png)

## Executive Summary

Unit 42 researchers examine several malware samples that incorporate Cobalt Strike components, and discuss some of the ways that we catch these samples by analyzing artifacts from the deltas in process memory at key points of execution. We will also discuss the evasion tactics used by these threats, and other issues that make their analysis problematic.

[Cobalt Strike](https://www.cobaltstrike.com/) is a clear example of the type of evasive malware that has been a thorn in the side of detection engines for many years. It is one of the most well-known adversary simulation frameworks for red team operations. However, it’s not only popular among red teams, but it is also abused by many threat actors for malicious purposes.

Although the toolkit is only sold to trusted entities to conduct realistic security tests, due to source code leaks, its various components have inevitably found their way into the arsenal of malicious actors ranging from ransomware groups to state actors. Malware authors abusing Cobalt Strike even played a role in the infamous [SolarWinds incident](https://unit42.paloaltonetworks.com/solarstorm-supply-chain-attack-timeline/) in 2020.

## Table of Contents

[Overview of Cobalt Strike](#post-125875-_e2rkiblq96ad)

## Overview of Cobalt Strike

The main driver for the proliferation of Cobalt Strike is that it is very good at what it does. It was designed from the ground up to help red teams armor their payloads to stay ahead of security vendors, and it regularly introduces new evasion techniques to try to maintain this edge.

One of the main advantages of Cobalt Strike is that it mainly operates in memory once the initial loader is executed. This situation poses a problem for detection when the payload is statically armored, exists only in memory and refuses to execute. This is a challenge to many security software products, as scanning memory is anything but easy.

In many cases, Cobalt Strike is a natural choice for gaining an initial footprint in a targeted network. A threat actor can use a builder with numerous deployment and obfuscation options to create the final payload based on a customizable template.

This payload is typically embedded into a file loader in encrypted or encoded form. When the file loader is executed by a victim, it decrypts/decodes the payload into memory and runs it. As the payload is present in memory in its original form, it can be detected easily due to some specific characteristics.

As malware researchers, we often see potentially interesting malicious samples that turn out to just be loaders for Cobalt Strike. It’s also often unclear if a loader was created by a red team or a real malicious actor, thus making attribution even more challenging.

In the next few sections, we’re going to take a closer look into three different Cobalt Strike loaders that were detected out of the box by a new hypervisor based sandbox we designed to allow us to analyze artifacts in memory. Each sample loads a different implant type, namely an SMB, HTTPS and stager beacon. We dubbed these Cobalt Strike loaders KoboldLoader, MagnetLoader and LithiumLoader. We will also discuss some of the methods we can use to detect these payloads.

## KoboldLoader SMB Beacon

The sample we’re looking at was detected during a customer incident.

SHA256: 7ccf0bbd0350e7dbe91706279d1a7704fe72dcec74257d4dc35852fcc65ba292

This 64-bit KoboldLoader executable uses various known tricks to try to bypass sandboxes and to make the analysis process more time consuming.

To bypass sandboxes that hook only high-level user mode functions, it solely calls built-in API functions. To make the analyst's life harder, it dynamically resolves the functions by hash instead of using plain text strings. The malware contains code to call the following functions:

* NtCreateSection
* NtMapViewOfSection
* NtCreateFile (unused)
* NtAllocateVirtualMemory (unused)
* RtlCreateProcessParameters
* RtlCreateUserProcess
* RtlCreateUserThread
* RtlExitUserProcess

The malware creates two separate tables of function hash/address pairs. One table contains one pair for all built-in functions, while the second table only pairs for Nt\* functions.

For the Rtl\* functions that were used, it loops through the first table and searches for the function hash to get the function address. For the Nt\* functions that were used, it loops through the second table and simultaneously increases a counter variable.

When the hash is found, it takes the counter value that is the system call number of the corresponding built-in function, and it enters a custom syscall stub. This effectively bypasses many sandboxes, even if the lower level built-in functions are hooked instead of the high-level ones.

The overall loader functionality is relatively simple and uses mapping injection to run the payload. It spawns a child process of the Windows tool sethc.exe, creates a new section and maps the decrypted Cobalt Strike beacon loader into it. The final execution of the Cobalt Strike loader that in turn loads an SMB beacon happens by calling RtlCreateUserThread.

You can find the decrypted beacon configuration data in the [Appendix](#post-125875-_o9a7sz67lxwt) section.

### In-Memory Evasion

With our new hypervisor-based sandbox, we were able to detect the decrypted Cobalt Strike SMB beacon in memory. This beacon loader even uses some [in-memory evasion](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/malleable-c2-extend_pe-memory-indicators.htm#_Toc65482856) features that create a strange sort of chimeric file. While it’s actually a DLL, the “MZ'' magic PE bytes and subsequent DOS header are overwritten with a small loader shellcode as shown in Figure 1.

![Image of shellcode showing disassembled Cobalt Strike beacon loader.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image.png)

Figure 1. Disassembled Cobalt Strike beacon loader shellcode.

The shellcode loader jumps to the exported function DllCanUnloadNow, which prepares the SMB beacon module in memory. To do this, it first loads the Windows pla.dll library and zeroes out a chunk of bytes inside its code section (.text). It then writes the beacon file into this blob and fixes the import address table, thus creating an executable memory module.

During the analysis of the file, we could figure out some of the in-memory evasion features that were used, as shown in Table 1.

| **Evasion feature** | **Description** | **Used in our sample** |
| --- | --- | --- |
| allocator | Set how beacon's ReflectiveLoader allocates memory for the agent. Options are: HeapAlloc, MapViewOfFile and VirtualAlloc. | No |
| cleanup | Ask beacon to attempt to free memory associated with the reflective DLL package that initialized it. | Yes |
| magic\_mz\_x64 | Override the first bytes (MZ header included) of beacon's reflective DLL. Valid x86 instructions are required. Follow instructions that change CPU state with instructions that undo the change. | Yes |
| magic\_pe | Override the PE character marker used by beacon's ReflectiveLoader with another value. | No |
| module\_x64 | Ask the x86 reflective loader to load the specified librar...