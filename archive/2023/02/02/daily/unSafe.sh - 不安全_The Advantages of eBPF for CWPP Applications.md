---
title: The Advantages of eBPF for CWPP Applications
url: https://buaq.net/go-147566.html
source: unSafe.sh - 不安全
date: 2023-02-02
fetch_date: 2025-10-04T05:27:58.399490
---

# The Advantages of eBPF for CWPP Applications

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

![](https://8aqnet.cdn.bcebos.com/1169193bb81373b3cc07e332cfd04230.jpg)

The Advantages of eBPF for CWPP Applications

Extended Berkeley Packet Filter (eBPF) is a framework for loading and running user-defined programs
*2023-2-1 21:58:59
Author: [www.sentinelone.com(查看原文)](/jump-147566.htm)
阅读量:30
收藏*

---

Extended Berkeley Packet Filter (eBPF) is a framework for loading and running user-defined programs within the Linux OS kernel, to observe, change, and respond to kernel behavior without the destabilizing impact of kernel modules. eBPF provides kernel-level visibility directly from user space. This combination of visibility and stability makes the eBPF framework particularly attractive for security applications.

In this blog post, we describe how eBPF works, its significance to cloud workload protection platforms (CWPP) for machine-speed detection of OS-level runtime threats, and the benefits of such an architectural approach, namely stability, scalability, and performance. We will then summarize how SentinelOne has over the last 3 years, in close cooperation with leaders across a wide variety of verticals, crafted the most high-performing, resource-efficient, and DevOps-friendly CWPP solution on the market.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/The-Advantages-of-eBPF-for-CWPP-Application-5.jpg)

## eBPF Architectural Overview

eBPF programs allow us to observe and respond to application (workload) behavior within the kernel without modifying the application code itself. This is useful for many applications, especially security applications such as cloud workload protection.

Consider the following diagram in Figure 1, modified for simplicity from the original found at [ebpf.io](http://ebpf.io/).

![eBPF Simple Architectural Overview](https://www.sentinelone.com/wp-content/uploads/2023/02/eBPF_CWPP_9.jpg)

Figure 1: Simple Architectural Overview

Here, we have an application (for example, a CWPP agent) running in user space and which includes an eBPF program for process-level visibility within the Linux kernel. The eBPF program itself is in bytecode, though developers usually use a higher level programming language whose compiler supports eBPF bytecode. This eBPF program is loaded into the Linux kernel, where the program is immediately verified by the eBPF Verification Engine. Then, the program is compiled and attached to a targeted-by-design kernel event; this is what is meant when one says that eBPF programs are “event-driven.” Whenever this event occurs, the program is attached to this event, runs its observation and analysis tasks to completion, and presents results back to the application.

The mechanism by which information is transferred between the eBPF program and the user space application/workload is called “eBPF Maps” or simply “maps”. Now that we have a high-level overview, let’s dig in a little deeper for more complete understanding.

## eBPF Safety

The eBPF Verification Engine and Just-in-Time Compiler are the means by which the eBPF framework ensures that, first and foremost, the eBPF program to be loaded and run within the kernel does not destabilize the kernel. This is Rule No. 1: Do No Harm.

> #### Kernel Modules: The Inferior Alternative
>
> Consider the alternative to eBPF: writing kernel modules. Kernel modules raise concerns about operational stability and complexity. While writing a kernel module does indeed allow a developer to change kernel behavior, it is a highly specialized skill, which therefore makes staffing and retention an issue.  More pointedly, using kernel modules raises the specter of two critical risk questions: (1) *will my kernel module crash the machine?*, and (2) *will it introduce a security vulnerability?*
>
> In addition to stability and security concerns, there is the matter of operational overhead: a kernel module only works for a specific Linux kernel version and distribution. Maintaining the kernel module consumes precious developer cycles and complicates operational management unnecessarily. The eBPF framework addresses each of these pain points, making kernel modules far less desirable.

Before any eBPF program is loaded into the kernel, it passes through the Verification Engine and JIT Compiler. The Verifier ensures that the program is safe to run, will not crash the system, and will not compromise data. It validates that several conditions are met:

1. The process loading the eBPF program has the necessary privileges to do so.
2. The eBPF program does not crash the system.
3. The eBPF program runs to completion. That is, it does not loop indefinitely.

Once verified, the JIT Compiler translates the program from bytecode into machine instructions, optimizing for speed of execution.

Now that the eBPF program is verified and compiled, it is attached to a kernel-level event, such that when the event occurs, the program is triggered, run to completion, and information presented to the user space application. This brings us to eBPF Maps, or simply “maps”.

## eBPF Maps

eBPF maps are the mechanism by which information transfers between the eBPF program and the user space application. Bidirectional information flow is supported. A map is a data structure that the eBPF program and user space application can read or write.

For example, the program might be triggered on an event such as gzip of a file. The eBPF program will write some information about that event, such as the file name, filesize, and gzip timestamp, to the map. It might also increment the number of times a gzip operation occurs within a given period of time. If that number exceeds a certain threshold, the eBPF program can write a judgment of “MALICIOUS” to the data structure. Stated simply, the eBPF program observed behavior indicative of a ransomware attack and flagged this behavior as malicious. The user space program – in our example, a cloud workload protection (CWPP) agent – can read that map, see the malicious judgment, and take appropriate action. Basic information processing occurred within the eBPF program, minimizing the amount of information passed to the user space application and thereby optimizing performance.

## Advantages of eBPF within CWPP

A cloud workload protection platform agent does what other security controls do not: detect and respond to runtime threats, like ransomware or zero days, in real time. This makes CWPP a vital component of a [cloud defense in depth strategy](https://assets.sentinelone.com/abm-cloud/practical-guidance-for-cloud-defense-in-depth#page=1). An organization can, and quite often should, have other cloud security measures in place, such as AppSec, CSPM, and more. Each plays a role in a robust cloud security strategy. A CWPP agent works alongside these other controls, to (1) provide runtime protection and (2) record workload telemetry.

![Linux Ransomware Attack Shown in the SentinelOne Console](https://www.sentinelone.com/wp-content/uploads/2023/02/eBPF_CWPP_10v2.jpg)

Figure 2: Linux Ransomware Attack Shown in the SentinelOne Console

As shown in Figure 2, a ransomware attack on a cloud compute instance (VM) can [lock-up a cloud workload in milliseconds](https://assets.sentinelone.com/cloud-security/sentinelone-singularity-cloud-detects). Note that the CWPP agent in this 1-minute video detected and stopped the ransomware attack mere moments (less than a second) after it was launched.

Try getting this real-time response from a side-scanning solution. You cannot. Side-scanning is typically run only once a day, because taking snapshots of a cloud compute instances’ storage volumes for inspection is cost-prohibitive. Mo...