---
title: Navigating the Vast Ocean of Sandbox Evasions
url: https://buaq.net/go-141605.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:44.155904
---

# Navigating the Vast Ocean of Sandbox Evasions

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

![](https://8aqnet.cdn.bcebos.com/2baa616787ba1dbe62c3dc44971f8267.jpg)

Navigating the Vast Ocean of Sandbox Evasions

This post is also available i
*2022-12-27 22:0:5
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-141605.htm)
阅读量:34
收藏*

---

![A pictorial depiction of a sandbox evasion](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Vulnerability-r3d3-1.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/sandbox-evasion-memory-detection/)

## Executive Summary

When malware authors go to great lengths to avoid behaving maliciously if they detect they’re running in a sandbox, sometimes the best answer for security defenders is to write their own sandbox that can’t easily be detected. There are a lot of sandboxing approaches out there with pros and cons to each. We’ll talk about why we chose to go the bespoke route, and we’ll discuss many of the evasion types we had to cover in that effort as well as strategies that can be used to counter them.

There are many variations on how malware authors specifically detect sandboxes, but the general theme is that they will check the characteristics of the environment to see whether it looks like a targeted host rather than an automated system.

Palo Alto Networks customers receive improved detection for the evasions discussed in this blog through Advanced WildFire.

## Table of Contents

[How We Became Evasion Connoisseurs](#post-126138-_fh99rab46dpn)

## How We Became Evasion Connoisseurs

You could say that our day to day in the world of malware analysis has made the WildFire malware team sandbox evasion connoisseurs. Our team’s Slack channel has had its share of “look at this one!” over the years, sharing the joy of finding new evasion techniques. Getting to the bottom of these has been a big part of our team mission to help improve detection.

There’s a vast number of techniques malware authors use to check if they are running on a “real” targeted host, such as counting the number of cookies in browser caches, or checking whether video memory appears too small. Given that sandbox evasions are legion and there are far too many to cover in a single article, we will first examine some of the major categories we typically encounter and then cover what we can do about them.

## Checks for Instrumentation or “Hooks”

The first broad category of evasions involves the detection of any sandbox instrumentation. This is definitely one of the most popular techniques. The most common example is checking for API hooks, as this is a common method for sandboxes and antivirus vendors alike to instrument and log all of the API calls made by an executable under analysis. This can be as simple as checking the function prologues of common functions to see if they are hooked.

In Figure 1, we see what the disassembly looks like for the prologue of CreateFileA in Windows 10 as well as what it might look like if it’s been instrumented in a sandbox.

![Image 1 demonstrates disassembly of CreateFileA’s prologue in Windows 10. There are three separate boxes. Box 1 on the left represents the normal CreateFileA prologue in kernel base.dll. Box 2 in the middle shows a hooked version of the same CreateFileA, and arrows going to and from this box to Box 3, which shows the Sandbox Hook Handler.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/VO-Figure1.png)

Figure 1. A typical sandbox hook on a function in the system API.

As you can see, this is pretty easy for attackers to detect, which is why it’s one of the most prevalent evasions we’ve seen out there.

A fun variation on this technique is when malware detects and unhooks existing hooks in order to stealthily execute without having its activity logged. This happens when malware authors want to slide past endpoint protections without being detected on a targeted host.

Figure 2 shows an example of how [GuLoader](https://unit42.paloaltonetworks.com/guloader-variant-anti-analysis/) unpatches the bytes of the ZwProtectVirtualMemory function prologue to restore the original functionality.

![Image 2 is a screenshot of a before and after of GuLoader unhooking instrumentation in a system API function. It has unpatched the bytes of ZwProtectVirtualMemory function prologue.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Figure2-1.png)

Figure 2. GuLoader unhooking instrumentation in a system API function.

### Mitigating Instrumentation Evasions

The gold standard for preventing malware authors from detecting instrumentation is simply not to have anything out of the ordinary that’s visible to the program you’re analyzing. A growing number of sandboxes are making this idea the focus of their detection strategy. It’s easier to be evasion resistant when you don’t change a single byte anywhere in the OS.

Instead of instrumenting APIs by changing code, it’s a better strategy to use virtualization to invisibly instrument programs under analysis. There are a lot of advantages to instrumenting malware from outside of the guest VM, as shown in Figure 3.

![Image 3 shows two side-by-side diagrams. The left diagram shows a guest virtual machine’s program analysis components with the addition of the malware sample it executes. The diagram on the right shows the host operating system outside of the same virtual machine.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/VO-Figure3.png)

Figure 3. In-guest versus a hypervisor based hooking engine. Left: Program analysis components exist in the guest VM along with the malware sample it executes. Right: Analysis components exist entirely outside of the guest VM and are thus invisible to the program under analysis.

## Detecting Virtual Environments

Another common evasion category involves detecting that a file is executing in a virtual machine (VM). This can involve fingerprinting resources like low CPU core count, system or video memory, or screen resolution. It can also involve fingerprinting artifacts of the specific VM.

When building a sandbox, vendors have a large number of VM solutions to choose from, such as KVM, VirtualBox and Xen. Each one has various artifacts and idiosyncrasies that are detectable by software running in VMs underneath them.

Some of these idiosyncrasies are particular to a specific system, like checking for the backdoor interface of VMware, or checking whether the hardware presented to the OS matches the virtual hardware provided by QEMU. Other approaches can simply detect hypervisors in general. For example, Mark Lim discussed a [general evasion for hypervisors](https://unit42.paloaltonetworks.com/single-bit-trap-flag-intel-cpu/) in an article, which capitalizes on the fact that many hypervisors incorrectly emulate the behavior of the trap flag.

One of the earliest and most widely used mechanisms for malware to determine whether it’s running inside a VMware virtual machine is to use the backdoor interface of VMware to see whether there is any valid response from the VMware hypervisor. An example of such a check is shown in Figure 4.

![Image 4 is a screenshot of many line of code where malware checks if it’s running inside a VMware virtual machine to see if there will be a valid response. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Figure4.png)

Figure 4. Malware checking if it’s running inside a VMware virtual machine.

Malware families can also query the computer manufacturer or model information using Windows Management Instrumentation (WMI) queries. This allows them to get information about the system and compare it with known sandbox and/or hypervisor...