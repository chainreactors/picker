---
title: DragonSpark | Attacks Evade Detection with SparkRAT and Golang Source Code Interpretation
url: https://buaq.net/go-146614.html
source: unSafe.sh - 不安全
date: 2023-01-25
fetch_date: 2025-10-04T04:43:04.987541
---

# DragonSpark | Attacks Evade Detection with SparkRAT and Golang Source Code Interpretation

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

![](https://8aqnet.cdn.bcebos.com/37df390e3b935a612a83448f5d1e13dd.jpg)

DragonSpark | Attacks Evade Detection with SparkRAT and Golang Source Code Interpretation

By  Aleksandar Milenkoski, Joey Chen, and Amitai Ben Shushan EhrlichExecutive SummarySentinelLab
*2023-1-24 18:55:22
Author: [www.sentinelone.com(查看原文)](/jump-146614.htm)
阅读量:60
收藏*

---

**By  Aleksandar Milenkoski, Joey Chen, and Amitai Ben Shushan Ehrlich**

## Executive Summary

* SentinelLabs tracks a cluster of recent opportunistic attacks against organizations in East Asia as DragonSpark.
* SentinelLabs assesses it is highly likely that a Chinese-speaking actor is behind the DragonSpark attacks.
* The attacks provide evidence that Chinese-speaking threat actors are adopting the little known open source tool SparkRAT.
* The threat actors use Golang malware that implements an uncommon technique for hindering static analysis and evading detection: Golang source code interpretation.
* The DragonSpark attacks leverage compromised infrastructure located in China and Taiwan to stage SparkRAT along with other tools and malware.

## Overview

SentinelLabs has been monitoring recent attacks against East Asian organizations we track as ‘DragonSpark’. The attacks are characterized by the use of the little known open source SparkRAT and malware that attempts to evade detection through Golang source code interpretation.

The DragonSpark attacks represent the first concrete malicious activity where we observe the consistent use of the open source [SparkRAT](https://github.com/XZB-1248/Spark), a relatively new occurrence on the threat landscape. SparkRAT is multi-platform, feature-rich, and frequently updated with new features, making the RAT attractive to threat actors.

The Microsoft Security Threat Intelligence team [reported](https://www.microsoft.com/en-us/security/blog/2022/12/21/microsoft-research-uncovers-new-zerobot-capabilities/) in late December 2022 on indications of threat actors using SparkRAT. However, we have not observed concrete evidence linking DragonSpark to the activity documented in the report by Microsoft.

We observed that the threat actor behind the DragonSpark attacks uses Golang malware that interprets embedded Golang source code at runtime as a technique for hindering static analysis and evading detection by static analysis mechanisms. This uncommon technique provides threat actors with yet another means to evade detection mechanisms by obfuscating malware implementations.

## Intrusion Vector

We observed compromises of web servers and MySQL database servers exposed to the Internet as initial indicators of the DragonSpark attacks. Exposing [MySQL servers to the Internet](https://www.shadowserver.org/news/over-3-6m-exposed-mysql-servers-on-ipv4-and-ipv6/) is an infrastructure posture flaw that often leads to severe incidents that involve data breaches, credential theft, or lateral movement across networks. At compromised web servers, we observed use of the China Chopper webshell, [recognizable](https://blog.talosintelligence.com/china-chopper-still-active-9-years-later/) by the `&echo [S]&cd&echo [E]` sequence in virtual terminal requests. [China Chopper](https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/china-chopper) is commonly used by Chinese threat actors, which are known to deploy the webshell through different vectors, such as exploiting web server vulnerabilities, cross-site scripting, or SQL injections.

After gaining access to environments, the threat actor conducted a variety of malicious activities, such as lateral movement, privilege escalation, and deployment of malware and tools hosted at attacker-controlled infrastructure. We observed that the threat actor relies heavily on open source tools that are developed by Chinese-speaking developers or Chinese vendors. This includes SparkRAT as well as other tools, such as:

* [SharpToken](https://github.com/BeichenDream/SharpToken): a privilege escalation tool that enables the execution of Windows commands with SYSTEM privileges. The tool also features enumerating user and process information, and adding, deleting, or changing the passwords of system users.
* [BadPotato](https://github.com/BeichenDream/BadPotato): a tool similar to SharpToken that elevates user privileges to SYSTEM for command execution. The tool has been observed in an [attack campaign](https://www.trellix.com/en-us/about/newsroom/stories/research/operation-harvest-a-deep-dive-into-a-long-term-campaign.html) conducted by a Chinese threat actor with the goal of acquiring intelligence.
* [GotoHTTP](https://gotohttp.com/): a cross-platform remote access tool that implements a wide array of features, such as establishing persistence, file transfer, and screen view.

In addition to the tools above, the threat actor used two custom-built malware for executing malicious code: ShellCode\_Loader, implemented in Python and delivered as a PyInstaller package, and m6699.exe, implemented in Golang.

## SparkRAT

SparkRAT is a RAT developed in Golang and released as [open source](https://github.com/XZB-1248/Spark) software by the Chinese-speaking developer [XZB-1248](https://github.com/XZB-1248). SparkRAT is a feature-rich and multi-platform tool that supports the Windows, Linux, and macOS operating systems.

SparkRAT uses the WebSocket protocol to communicate with the C2 server and features an upgrade system. This enables the RAT to automatically upgrade itself to the latest version available on the C2 server upon startup by issuing an upgrade request. This is an HTTP POST request, with the commit query parameter storing the current version of the tool.

![A SparkRAT upgrade request](https://www.sentinelone.com/wp-content/uploads/2023/01/SaprkRAT_6.jpg)

In the attacks we observed, the version of SparkRAT was `6920f726d74efb7836a03d3acfc0f23af196765e`, built on 1 November 2022 UTC. This version supports 26 commands that implement a wide range of functionalities:

* Command execution: including execution of arbitrary Windows system and PowerShell commands.
* System manipulation: including system shutdown, restart, hibernation, and suspension.
* File and process manipulation: including process termination as well as file upload, download, and deletion.
* Information theft: including exfiltration of platform information (CPU, network, memory, disk, and system uptime information), screenshot theft, and process and file enumeration.

![SparkRAT version](https://www.sentinelone.com/wp-content/uploads/2023/01/SaprkRAT_5.jpg)

SparkRAT version

## Golang Source Code Interpretation For Evading Detection

The Golang malware m6699.exe uses the [Yaegi](https://github.com/traefik/yaegi) framework to interpret at runtime encoded Golang source code stored within the compiled binary, executing the code as if compiled. This is a technique for hindering static analysis and evading detection by static analysis mechanisms.

The main purpose of m6699.exe is to execute a first-stage shellcode that implements a loader for a second-stage shellcode.

m6699.exe first decodes a Base-64 encoded string. This string is Golang source code that conducts the following activities:

* Declares a `Main` function as part of a `Run` package. The `run.Main` function takes as a parameter a byte array – the first-stage shellcode.
* The `run.Main` function invokes the [HeapCreate](https://learn.microsoft.com/en-us/windows/win32/api/heapapi/nf-heapapi-heapcreate) function to allocate executable and growable heap memory (`HEAP_CREATE_ENABLE_EXECUTE`).
* The `run.Main` function places the first-stage shellcode, supplied to it as a par...