---
title: OysterLoader Unmasked: The Multi-Stage Evasion Loader
url: https://blog.sekoia.io/oysterloader-unmasked-the-multi-stage-evasion-loader/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-12
fetch_date: 2026-02-13T04:18:39.682318
---

# OysterLoader Unmasked: The Multi-Stage Evasion Loader

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# OysterLoader Unmasked: The Multi-Stage Evasion Loader

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Pierre Le Bourhis](#molongui-disabled-link)
February 12 2026

0

19 minutes reading

## Introduction

**OysterLoader,** also known as **Broomstick** and **CleanUp,** is a malware developed in C++, composed of multiple stages, belonging to the loader (*A.k.a.: downloader*) malware family. First reported in June 2024 by [Rapid7](https://www.rapid7.com/blog/post/2024/06/17/malvertising-campaign-leads-to-execution-of-oyster-backdoor/), it is mainly distributed via web sites impersonating legitimate software which are often IT software for instance: PuTTy, WinSCP, Google Authenticator and Ai software. The loader is primarily employed in campaigns leading to Rhysida ransomware.

According to [Expel reports](https://expel.com/blog/certified-oysterloader-tracking-rhysida-ransomware-gang-activity-via-code-signing-certificates/), OysterLoader is used by the Rhysida ransomware group which is closely associated with the [WIZARD SPIDER nebula](https://www.recordedfuture.com/research/outmaneuvering-rhysida-advanced-threat-intelligence-shields-critical-infrastructure-ransomware). Besides, the loader is also used to distribute commodity malware such as **Vidar**, the most widespread infostealer by January 2026. According to Huntress, OysterLoader is also distributed via **[Gootloader](https://www.huntress.com/blog/gootloader-threat-detection-woff2-obfuscation)**. Based on our observations and other reports on this threat, it is unclear whether the malware is proprietary to Rhydida ransomware group and friends or sold as **MaaS** on private marketplaces.

Since its apparition, the malware’s code has evolved, and analysis by various security vendors highlighted some regressions between its first and current versions, particularly in Command-and-Control (C2) content and in code obfuscation.

## Malware Analysis

The malware is distributed mainly through fake websites that copy legitimate software. It is disguised as a software installer and serves as a **MicroSoft Installer** (MSI). The MSI is often signed to appear benign. The infection chain is composed of **four stages**:

1. Stage 1 – Packer [*TextShell*]
2. Stage 2 – Custom shellcode [*TextShell*]
3. Stage 3 – Intermediate DLL acting as a downloader
4. Stage 4 – OysterLoader core

### Stage 1 – Obfuscator

The main function of the packer is to load in memory the next stage that is stored “shuffled”. According to [Huntress](https://www.huntress.com/blog/gootloader-threat-detection-woff2-obfuscation)‘ report on Gootlader that mentions OysterLoader, the packer (also called obfuscator in the report) is another malware named **TextShell**.

To load it, it allocates a memory area with necessary permissions (Read, Write, Execute) and makes a raw copy of the data in the newly allocated memory. The copy is made in a bunch of eight bytes. Besides, the code of the initial stage is full of useless API calls to legitimate DLL, the objectives being to avoid execution in particular environments. The packer also embedded a simple anti-debug trap that is present multiple times in the packer.

Besides, the first stage employs common techniques such API hammering and dynamic API resolution.

#### Legitimate API calls flooding-hammering

In order to hide its malicious code, the loader attempts to make hundreds of calls to legitimate DLLs.  In malware, these calls often serve **no operational purpose**. They don’t meaningfully change the environment. They look legitimate, though, and that’s the point. Their purposes are various:

* Break heuristic detectors “lots of GDI calls – mimikate graphics tool).

* Distract reverse-engineers during static analysis.
* Mislead sandboxes (some sandboxes don’t fully emulate GDI calls).
* Introduce chaotic paths in decompiled code.

The malware code is encapsulated with legitimate calls, sometimes, only the prologue of the function is filled with DLLs calls, sometimes the epilogue also contains these patterns.

```
RevokeDragDrop(0);
DC = GetDC(0);
SolidBrush = CreateSolidBrush(0x75051u);
UnrealizeObject(SolidBrush);
SetMapMode(DC, 2);
v2 = CreateSolidBrush(0xFACB9Fu);
UnrealizeObject(v2);
SetCommBreak(0);
ptr_buff_struct_mem = allocate_mem;
*(_DWORD *)&allocate_mem->blob0[0x1AD5B] = 0xE539234E;
OaBuildVersion();
OaBuildVersion();
*(_DWORD *)&ptr_buff_struct_mem->blob0[0x1A0D8] = 0x2AD4A690;
SetBkColor(DC, 0x6C072Au);
SetMapMode(DC, 4);
if ( IsDebuggerPresent() )
{
while ( 1 );
}
v4 = CreateSolidBrush(0x202417u);
UnrealizeObject(v4);
*(_QWORD *)&ptr_buff_struct_mem->blob0[0x1A6B9] = 0x475717F412B7ABBCLL;
*(_QWORD *)&ptr_buff_struct_mem->blob0[0x1A6C1] = 0xBA8581BA8183F21BuLL;
*(_QWORD *)&ptr_buff_struct_mem->blob0[0x1A6C9] = 0x3A48C871C86971C8LL;
...
```

*Code 1. Extract of decompiled code employing API flooding*

In the above example, the only relevant code are (highlighted in blue):

1. Accessing a global variable (here allocate\_mem)
2. Copying data at specifics offset (`DWORD` and `QWORD` value)

A more intentional anti-analysis mechanism is the **IsDebuggerPresent() check**; if a debugger is detected, the malware enters an infinite loop (`while(1);`), effectively freezing execution and preventing dynamic analysis. This kind of anti-debugging trick is **far from being advanced**—analysts can easily bypass it by patching the `IsDebuggerPresent` function in *kernel32.dll*, for example by replacing its epilogue with `xor eax, eax; ret`, forcing it to always report that no debugger is attached. Together, these techniques illustrate how malware authors pad their binaries with noise and simple anti-debugging traps to slow down analysts and automated detection systems.

*To ease the analysis of this stage, the following* [*script*](https://gist.github....