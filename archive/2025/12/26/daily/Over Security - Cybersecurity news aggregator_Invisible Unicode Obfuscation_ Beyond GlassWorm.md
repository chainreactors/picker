---
title: Invisible Unicode Obfuscation: Beyond GlassWorm
url: https://reggia.xyz/posts/invisible-unicode-obfuscation-beyond-glassworm.html
source: Over Security - Cybersecurity news aggregator
date: 2025-12-26
fetch_date: 2025-12-27T03:24:01.001394
---

# Invisible Unicode Obfuscation: Beyond GlassWorm

*Reading time: 8 minutes*

# Invisible Unicode Obfuscation: Beyond GlassWorm

## Table of Contents

* [Introduction](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#introduction)
* [Research](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#research)
  + [Encoding logic](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#encoding-logic)
  + [POC](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#poc)
* [Simulation](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#simulation)
  + [Windows](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#windows)
  + [Linux](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#linux)
* [Detection](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#detection)
* [References](/posts/invisible-unicode-obfuscation-beyond-glassworm.html#references)

## Introduction

While analyzing several malware samples, I recently observed the use of *mock directories* (folders crafted to closely resemble default Windows directories but containing embedded spaces) to mislead analysts. A documented example of this technique can be found here: <https://security.googlecloudcommunity.com/community-blog-42/finding-malware-dirtybulk-and-friends-usb-infections-to-fuel-cybercriminal-coinmining-operations-5552>

![â0.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/0.png)

Mock directories abusing embedded spaces to visually mimic legitimate Windows folders

Shortly after, John Hammond released a video on **GlassWorm**
([https://www.youtube.com/watch?v=0XumkGQFEEk)](https://www.youtube.com/watch?v=0XumkGQFEEk%29), a malware that infects VS Code extensions by embedding obfuscated payloads made of *invisible Unicode characters* directly into the source code. These characters are visually similar to whitespace, making the malicious logic extremely hard to notice.

![â1.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/1.png)

GlassWorm payload hidden inside a source code file using invisible Unicode characters. Source: <https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace>

This heavy reliance on whitespace-like characters sparked my curiosity. I wanted to understand how this technique works in practice, how it can be detected, and whether it could be applied in contexts beyond source code files. In many XDR products I use daily, file content inspection is limited or unavailable, which makes detecting this class of payload particularly challenging.

This led me to a broader question: **can invisible Unicode obfuscation be abused in other execution contexts**, such as command lines (PowerShell, Linux shells, etc.), to achieve *Defense Evasion* via *Obfuscation* (MITRE ATT&CK T1027.010 â Obfuscated Files or Information: Command Obfuscation)?

Since I found very little public material on this topic, I decided to conduct my own research.

The analysis was conducted through the following steps:

* Threat Intelligence research to identify attacker techniques and trends
* Study and research of undocumented malware variants
* Proof of Concept development
* Threat Hunting activities on generated events
* Detection rule creation

## Research

The first step was collecting information on Unicode characters that are rendered as invisible or near-invisible. I quickly realized that the set is **far larger** than the one documented in GlassWorm analysis.

To understand their behavior in real telemetry, I printed these characters using a simple PowerShell script on a host monitored by Windows Defender. I then inspected how they appeared in Defender logs. Below are screenshots of the script and the resulting events. It is immediately evident that:

* some characters are rendered as visible symbols in logs
* others are completely invisible
* the classic Windows console correctly renders a smaller subset compared to Defender

![â2.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/2.png)

PowerShell script printing invisible and near-invisible Unicode characters for telemetry analysis

![â3.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/3.png)

Windows Defender logs showing mixed rendering of invisible Unicode characters

Using Defender logs, I extracted all characters that appeared fully invisible and used them to build a proof of concept capable of obfuscating a payload.

### Encoding logic

The encoder follows this logic:

* it takes two main inputs: the **payload** and **two Unicode characters** (X and Y) chosen from the previously identified invisible character set
* each character of the payload is converted into its 8-bit binary representation
* for each bit:
  + `0` is represented by Unicode character X
  + `1` is represented by Unicode character Y
* the result is a long sequence of invisible Unicode characters whose length is 8Ã the original payload length

The malicious code responsible for deobfuscation performs the inverse operation. Once the payload is reconstructed, it is executed using a cmdlet such as `Invoke-Expression` (`IEX`).

Below is the encoder using the characters `\uFEFF` and `\u0020`:

![â4.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/4.png)

Unicode encoder transforming a clear-text payload into invisible characters

And here is the POC that decodes and executes the payload:

![â5.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/5.png)

PowerShell decoder reconstructing and executing the invisible Unicode payload

The result was interesting: **no alert was triggered, and the Defender event appeared empty**. The only visual clue was an unusually small horizontal scrollbar in the browser, indicating a very long command line. Scrolling far to the right reveals the PowerShell decoder logic, which seems to operate on an empty variable.

In reality, although the characters are invisible, they are composed of different bytes. This makes it possible to store information covertly. Additionally, if the analystâs text editor does not fully support the Unicode characters used, copy-paste operations may corrupt the payload by replacing or normalizing characters, making analysis impossible. In such cases, the safest approach is to download the raw log and inspect it using a hex editor or a Unicode-aware text editor.

![â6.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/6.png)

Defender event appearing empty despite containing a long invisible command line

Apparently, an alternative variant consists of invoking powershell.exe from within an existing PowerShell session and passing the payload via `-Args` using a ScriptBlock. In this scenario, the PowerShell host may repackage the invocation for the spawned process using `-EncodedCommand` and `-EncodedArguments`, with arguments being internally serialized as XML before Base64 encoding. This approach can be particularly effective when an attacker has interactive access to the host, such as via RDP or direct console access.

![â7.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/7.png)

Decoder variant using ScriptBlock in an existing Powershell session to make the command automatically Base64 encoded

![â8.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/8.png)

Automatically generated -EncodedCommand and -EncodedArguments after process spawning

Even in this scenario, attempts to parse the command line reveal valid but *apparently empty* XML, potentially misleading analysts into assuming the event is benign or irrelevant.

![â9.pngâ](/posts/invisible-unicode-obfuscation-beyond-glassworm/9.png)

Seemingly empty but valid XML generated from serialized invisible Unicode arguments

### POC

Below is the POC code.

ENCODER:

```
$PAYLOAD = "Write-host paddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpaddingpadding mal...