---
title: The Mystery of Metador | Unpicking Mafalda’s Anti-Analysis Techniques
url: https://buaq.net/go-138111.html
source: unSafe.sh - 不安全
date: 2022-12-02
fetch_date: 2025-10-04T00:15:47.249174
---

# The Mystery of Metador | Unpicking Mafalda’s Anti-Analysis Techniques

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

![](https://8aqnet.cdn.bcebos.com/c4ae32c89f4a212e6bdc5ccbfceb2544.jpg)

The Mystery of Metador | Unpicking Mafalda’s Anti-Analysis Techniques

OverviewAt the inaugural LabsCon, we unveiled Metador,  a previously unreported threat actor that
*2022-12-1 22:19:42
Author: [www.sentinelone.com(查看原文)](/jump-138111.htm)
阅读量:31
收藏*

---

## Overview

At the inaugural [LabsCon](https://www.labscon.io/), we unveiled [Metador](https://www.sentinelone.com/labs/the-mystery-of-metador-an-unattributed-threat-hiding-in-telcos-isps-and-universities/),  a previously unreported threat actor that targets telecommunications, internet service providers, and universities in the Middle East and Africa. We observed Metador using two versions of a feature-rich backdoor, dubbed ‘Mafalda’, one of which features anti-analysis techniques to make analysis challenging.

In this article, we provide a deep dive into the anti-analysis techniques that Mafalda implements. This article complements our previous [report](https://assets.sentinelone.com/sentinellabs22/metador) on Metador and offers a deeper understanding of how Mafalda tries to hinder analysis and make detection and attribution more challenging for analysts.

The implementation of Mafalda suggests that the malware is maintained and developed by a dedicated team. Mafalda includes comprehensive backdoor command documentation with comments for a separate group of operators. In addition, Mafalda implements an execution log that the malware maintains when it runs on an infected system. The log provides detailed information about the execution of the malware on the system and therefore is a rich resource to analysts. Our previous [report](https://assets.sentinelone.com/sentinellabs22/metador) discusses the functionalities of Mafalda in greater detail.

Throughout our analysis, we retrieved and analyzed two variants of Mafalda, which we refer to as  ‘Mafalda clear build 144’ (compiled with a timestamp of April 2021) and its successor,  ‘obfuscated Mafalda variant’ (compiled with a timestamp of December 2021). The newer,  obfuscated Mafalda variant extends the backdoor functionalities that the older variant provides and implements the anti-analysis techniques that we cover in this article.

## String Obfuscation

Mafalda uses obfuscated strings for different purposes, for example, to dynamically resolve library function addresses through library and library export names, or to store content in the execution log that Mafalda maintains. Mafalda obfuscates strings by:

* Splitting the strings into multiple portions, with a maximum portion length of 9 characters.
* Encrypting and encoding each string portion. Mafalda encodes a portion of an obfuscated string using the bitmask 0x7F and XOR-encrypts the portion using a portion-specific XOR key of one byte.

Therefore, to restore an obfuscated string into a valid string, Mafalda first decodes and decrypts each of the string’s portions, and then concatenates the string portions together.

The figure below depicts a snippet of the function that Mafalda executes to decode and decrypt a portion of an obfuscated string (a2 is a portion of an obfuscated string, v2 is an XOR key).

![Mafalda’s function for decoding and decrypting string portions](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_9.jpg)

## String Encryption

In addition to the string obfuscation approach, Mafalda works with encrypted versions of strings that may represent an information source to malware analysts. Such strings include segments of the execution log and debugger messages that Mafalda generates.

We noted that Mafalda prints encrypted debugger messages if the name of the computer where it executes is `WIN-K4C3EKBSMMI`, possibly indicating the name of the computer used by the developers.

![Encrypted debugger messages](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_3.jpg)

Encrypted debugger messages

In contrast to the Mafalda clear build 144, the obfuscated Mafalda variant writes encrypted strings to its execution log. Given that this log provides extensive information about the operation of the malware, encrypting the execution log serves to hinder analysis.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_7.jpg)

![Encrypted (top) and plain text (bottom) Mafalda execution log](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_13.jpg)

Encrypted (top) and plain text (bottom) Mafalda execution log

We did not discover evidence of functionality within Mafalda for decrypting the strings it encrypts. This suggests that string decryption takes place at Metador’s  command-and-control servers – a simple yet effective technique for hindering analysis.

## Function Parameter Obfuscation

Mafalda often obfuscates numerical function parameters by calculating parameter values prior to function execution using arithmetics and bitwise operations. It may also first calculate a value using arithmetics and bitwise operations. If the computed value does or does not match a predefined value, Mafalda assigns the correct values to the obfuscated parameters. The alternative branch assigns wrong values to the obfuscated parameters.

Mafalda applies this obfuscation approach when it executes the function that the implant uses to decode and decrypt portions of obfuscated strings (labeled `j_str_resolve_sub_18014FE4D` in the figure below).

![Function parameter obfuscation; v53 is a portion of an obfuscated string](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_10.jpg)

Function parameter obfuscation; *v53* is a portion of an obfuscated string

This obfuscation technique may direct emulation tools to wrong execution branches and function parameter values – analysts may use emulation to automate the decryption and decoding of portions of obfuscated strings across the whole implementation of Mafalda. For example, the `iterateAllPaths` feature of the [flare-emu](https://github.com/mandiant/flare-emu) tool attempts to emulate all execution paths to a given function and the function itself. For automated deobfuscation, malware analysts typically use this feature to emulate functions that deobfuscate strings at runtime. When we used the  `iterateAllPaths` function to emulate `j_str_resolve_sub_18014FE4D`, Mafalda often directed the tool to the wrong values of the function’s obfuscated parameters. This resulted in incorrect string decoding and decryption. In the figure below, `rn` and `9` are incorrectly decoded and decrypted strings.

![Incorrect string decoding and decryption](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_11.jpg)

Incorrect string decoding and decryption

However, when we used the flare-emu `emulateRange` functionality for emulating only specific implementation regions in which Mafalda invokes `j_str_resolve_sub_18014FE4D`, the tool was more accurate in assigning correct function parameter values. This resulted in correct string decoding and decryption. In the figure below, `Sleep` and `kernel32` are correctly decoded and decrypted strings – Mafalda uses these strings to invoke the [Sleep](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-sleep) function that is implemented in the `kernel32.dll` library file.

![Correct string decoding and decryption](https://www.sentinelone.com/wp-content/uploads/2022/11/Mafalda_6.jpg)

Correct string decoding and decryption

## Execution Flow Obfuscation

Mafalda is obfuscated at implementation-level such that the compiled code of the implant consists mainly of obfuscated and non-obfuscated code segments. The majority of the non-...