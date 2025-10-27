---
title: Defeating Guloader Anti-Analysis Technique
url: https://buaq.net/go-133137.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:22.513837
---

# Defeating Guloader Anti-Analysis Technique

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

![](https://8aqnet.cdn.bcebos.com/5b38d7f4fc97004a1879f7449b490133.jpg)

Defeating Guloader Anti-Analysis Technique

This post is also available i
*2022-10-28 21:0:39
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-133137.htm)
阅读量:32
收藏*

---

![Malware conceptual image, including types of malware such as the Guloader variant covered here.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/Malware-r3d3.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/guloader-variant-anti-analysis/)

## **Executive Summary**

Unit 42 researchers recently discovered a Guloader variant that contains a shellcode payload protected by anti-analysis techniques, which are meant to slow human analysts and sandboxes processing this sample. To help speed analysis for this sample and others like it, we are providing a complete [Python script](https://github.com/pan-unit42/public_tools/blob/master/idapython-guloader-anti-analysis/guloader_veh_anti_analysis_.py) to deobfuscate the Guloader sample that is available on GitHub.

In early September 2022, we discovered a Guloader variant with low VirusTotal detection. Guloader (also known as CloudEye) is a malware downloader first discovered in December 2019.

We analyzed the control flow obfuscation technique used by this Guloader sample to create the [IDA Processor module extension](https://hex-rays.com/blog/extending-ida-processor-modules-for-gdb-debugging/) script so researchers can deobfuscate the sample automatically. The script can be applied to other malware families like [Dridex](https://unit42.paloaltonetworks.com/excel-add-ins-dridex-infection-chain/), which utilize similar anti-analysis techniques.

Palo Alto Networks customers receive protections from malware families using similar anti-analysis techniques with [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) or the [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions), including [WildFire](https://www.paloaltonetworks.com/network-security/wildfire) and [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention).

## Table of Contents

[Guloader Control Flow Obfuscation Technique](#guloader-control-flow-obfuscation-technique)

## **Guloader Control Flow Obfuscation Technique**

The Guloader sample in question uses the control flow obfuscation technique to hide its functionalities and evade detection. This technique impedes both static and dynamic analysis.

First, let’s look at how this threat hampers static analysis. In short, it uses CPU instructions that trigger exceptions, resulting in unintelligible code during static analysis.

After peeling away the packer layer of our Guloader sample, we see that its code is obfuscated. Using static analysis tools such as [IDA Pro](https://hex-rays.com/ida-pro/), we observe many 0xCC bytes (or int3 instructions) littered throughout the sample, as shown in Figure 1.

Following the 0xCC bytes are junk instructions. These added bytes disrupt the static analysis tool’s disassembly process, resulting in the wrong disassembly listing.

![Scrolling through obfuscated code to show 0xCC bytes throughout.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image.gif)

Figure 1. Obfuscated code blocks.

0xCC bytes are CPU instructions that trigger an exception *EXCEPTION\_BREAKPOINT* (0x80000003), which pauses the execution of a process. The CPU will pass the code flow to the handler function before the execution continues. The handler function is responsible for moving the instruction pointer to the correct address.

The presence of these same 0xCC bytes make it so that using a debugger during dynamic analysis would crash the Guloader sample. Debuggers insert 0xCC bytes as software breakpoints to halt the execution of the sample. The debugger handles the exception instead of the handler function.

Before understanding what happens in the handler function, we first have to locate its address.

Guloader uses the AddVectoredExceptionHandler function to register the handler function, as shown in Figure 2. The second argument of the AddVectoredExceptionHandler function points to the address of the handler function.

![Function prototype of AddVectoredExceptionHandler used to register the handler function.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-41.png)

Figure 2. Function prototype of AddVectoredExceptionHandler.

Using a debugger as shown in Figure 3, we locate the address of the handler function registered by the Guloader sample. With the address information, we can examine its code. Notably, this ExceptionHandler is registered with the order of 1, meaning it is the first handler to be invoked.

![Using a debugger to locate the address of the AddVectoredExceptionHandler function registered by the Guloader sample.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-42.png)

Figure 3. Debugging the call to AddVectoredExceptionHandler in Guloader sample.

## **Analyzing the Vectored Exception Handler Function**

The first step of analyzing the handler function is to apply its type information, as shown in Figure 4.

![Showing the type information for the handler function.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-43.png)

Figure 4. Type information for the handler function.

Next, we apply the type information for three Windows data structures (shown in Figure 5) used by the handler function.

![Showing the type information of three Windows data structures to be applied on the handler function.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-44.png)

Figure 5. Type information of three Windows data structures to be applied on the handler function.

With the type information applied, we can examine how the function handled the exceptions caused by the 0xCC bytes. Figure 6 shows the decompiled handler function (Func\_VectoredExceptionHandler) annotated with comments.

![Decompiled handler function (Func_VectoredExceptionHandler) annotated with the following comments: "Check type of exception raised," "Check for hardware breakpoint," "CC byte raising exception," "Decode offset byte," "Loop to check for software breakpoint," "Exit handler function if software breakpoint is found," and "Update EIP with offset."](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-45.png)

Figure 6. Decompiled handler function.

The handler function begins with anti-debugging checks. It will terminate execution when hardware or software breakpoints are found. Next, the offset value is computed by XOR decoding the byte after the 0xCC byte with 0xA9. Finally, the offset value is added to the instruction pointer before the code execution resumes. Code execution continues at the address pointed to by the updated instruction pointer.

After understanding how the obfuscation is carried out, we can identify the legitimate instructions and discard the unwanted ones, as shown in Figure 7.

![Labeled code block so we can identify the legitimate instructions and discard the unwanted ones](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-46.png)

Figure 7. Labeled code block.

To completely deobfuscate the Guloader sample, we need to replace all the 0xCC bytes with a JMP short instruction (0xEB) and the following byte with the decoded offset value.

Because doing all this manua...