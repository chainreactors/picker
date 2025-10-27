---
title: EDR: The Great Escape - RomHack Training Review
url: https://dfir.ch/posts/romhack_edr/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-01
fetch_date: 2025-10-06T18:57:28.105945
---

# EDR: The Great Escape - RomHack Training Review

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# EDR: The Great Escape - RomHack Training Review

30 Sep 2024

**Table of Contents**

* [Overview of Module 1](#overview-of-module-1)
  + [Filesystem Minifilter Driver](#filesystem-minifilter-driver)
  + [Hooking](#hooking)
* [Module 2](#module-2)
  + [ELAM and PPLs](#elam-and-ppls)
  + [Event Tracing for Windows](#event-tracing-for-windows)
  + [Return Oriented Programming](#return-oriented-programming)
* [Module 3](#module-3)
  + [Callbacks and Notify Routines](#callbacks-and-notify-routines)
  + [Vulnerable Drivers](#vulnerable-drivers)
  + [Stack Spoofing](#stack-spoofing)
  + [Local Privilege Escalation](#local-privilege-escalation)
  + [Windows Filtering Platform](#windows-filtering-platform)
  + [Memory Scanners](#memory-scanners)
* [Module 4](#module-4)
  + [.NET Internals](#net-internals)
* [Conclusion](#conclusion)

![Romhack Logo](/images/romhack_edr/logo.png "Romhack Logo")

> This course aims to provide a comprehensive understanding of the architecture of modern EDRs and their underlying Antivirus (AV) systems. It delves deeply into the complexity of modern EDRs, their structure, including the components responsible for real-time monitoring, data collection, and threat analysis.
>
> [..]
>
> 50% of the course will be dedicated to hands-on labs showing how to translate the theory principles into practice. Labs are designed to provide flexibility in terms of complexity and include bonus tracks to ensure that you always feel engaged and have something interesting to explore and learn. This course is valuable not only for red team operators but also for blue team professionals. Blue team members can gain insights into how their detection systems may be bypassed, helping them enhance their security measures and stay one step ahead of potential threats. This course equips security professionals with a deep understanding of modern EDRs and their AV systems, enabling them to better simulate advanced threat scenarios, improve their evasion detection skills, and contribute to the overall enhancement of security within enterprise networks.

Throughout my years as a security analyst and consultant, I have attended numerous training courses and earned several certifications along the way. These trainings included both defensive (blue team) and offensive (red team) perspectives. Some of these training were labeled âAdvancedâ, but last week, I attended [EDR: The Great Escape](https://romhack.io/training/2024/edr-the-great-escape/) training by the two *Crazy Italiene Doctors*, and it was the first time in a long period that I felt that the course really deserved the label âAdvancedâ (this is of course very subjective, and for other participants, it might have been less demanding as it was for me). Silvio and Antonio are the founders of RETooling. You can find their latest research here ([An unexpected journey into Microsoft Defender’s signature World](https://retooling.io/blog/an-unexpected-journey-into-microsoft-defenders-signature-world)), as we spoke several times about this research during the training.

In this post, I’ll review the training, discuss labs we worked on, and highlight key learning moments. As Silvio, one of the two teachers said a lot during the labs: *Come on, it’s just a few lines of code and some printf statements!* :)

## Overview of Module 1

### Filesystem Minifilter Driver

On the first day, we discussed the specific components of newer EDR systems which we will cover over the next four days, to find gaps in the implementations, and how to attack them. Within the course, we utilized the open-source EDR [openedr](https://github.com/ComodoSecurity/openedr) as a reference architecture.

The first major block of the course was dedicated to minifilter drivers, where we were shown how to hunt for whitelists for paths or filenames that we could use to hide our implant or how the altitude of the filter manager could play tricks on the returned results. For me, the biggest âahaâ experience in this module was the example of *altitude sickness*, a term coined by James Forshaw of Project Zero and explained in [Hunting for Bugs in Windows Mini-Filter Drivers](https://googleprojectzero.blogspot.com/2021/01/hunting-for-bugs-in-windows-mini-filter.html).

*This is a bug class that is caused by the ordering of filter operations based on the assigned altitudes of the driver. For example, if you look at the list of filters from the fltmc command shown earlier in this blog post youâll notice that WdFilter which is the real-time scanner for Windows Defender is at a much higher altitude than LUAFV which is the UAC file virtualization driver.*

Leading, as you can imagine, to some really impressive bugs and exploits. In the lab, we were tasked to find a way to write a file to a folder protected by `openedr`, where we were able to put our newly acquired skills to the test.

### Hooking

Nomen est omen. Every EDR monitors the API calls executed by a process in one way or another in order to detect suspicious and malicious behavior. In order to better understand unhooking, we first looked at various types of hooking techniques and then learned about unhooking and bypass techniques. In this module, the most significant learning for me was that syscalls can also be explicitly triggered via the `VectoredExceptionHandler` in order to bypass the hooking of EDR systems through this mechanism.

In the lab, we were tasked to remove a hook installed by the EDR through the APC injection technique. An amazing learning experience for me because we used WinDGB to analyze the hooks, and equipped with this knowledge we gained from the analysis, we wrote some C code which will first check if a hook is present and, if present, remove it. A clever way to put what we have learned into practice.

## Module 2

### ELAM and PPLs

ELAM stands for `Early Launch Anti Malware`, and although I knew the term and the technology in general, we were shown how to analyze the WdBoot driver with the Windows Kernel Debugger and how ELAM checks the information in the certificates for integrity since the file system is not yet available at boot time.

I taught about PPL, the `Protected Process Light`, in my FIRSTCON training this year, but even with some background in this topic, the level of presented details of the internals of PPLs was amazing.

### Event Tracing for Windows

Certainly, one of the topics I was most looking forward to, as ETW (`Event Tracing for Windows`) is becoming increasingly important. Quote from the course: *It was mainly introduced for capacity and performance analysis (and internal use!), but in the last few years, it has been adopted as a powerful tracing source for a wide range of AV/EDR solutions (e.g., Symantec, McAfee, Sophos etc.) and tools (Sysmon, wtrace etc.)*

![ETW](/images/romhack_edr/ETW-4.png "ETW")

Figure 1: EtwSiloState (Source: blog.trailofbits.com)

The picture above is from the Trail of Bits blog, [ETW internals for security research and forensics](https://blog.trailofbits.com/2023/11/22/etw-internals-for-security-research-and-forensics/). In the lab, we then to mute ETW via the `EtwUnregister` API. The content was also great in this module - several times, I looked at the slides and thought - *Wait, is this really possible?*

### Return Oriented Programming

I didn’t expect to find ROP techniques in this course, and I wasn’t aware that these techniques could be used for EDR evasions. This part of the course was all the more exciting, as was the accompanying lab:

*In this lab, you must use ONLY ROP to allocate and copy a payload to a specified process.Â And from the provided solution:Â Instead of using a standard, well-known pattern of APIs from the injector code, we are using ROP to force the execution of our instructions directly inside the target process, making the whole process stealthier and much...