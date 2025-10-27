---
title: MalVirt  | .NET Virtualization Thrives in Malvertising Attacks
url: https://buaq.net/go-147714.html
source: unSafe.sh - 不安全
date: 2023-02-03
fetch_date: 2025-10-04T05:34:03.509878
---

# MalVirt  | .NET Virtualization Thrives in Malvertising Attacks

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

![](https://8aqnet.cdn.bcebos.com/36d8fd93c67c6999b2d3921d8383ca83.jpg)

MalVirt | .NET Virtualization Thrives in Malvertising Attacks

By Aleksandar Milenkoski and Tom HegelExecutive SummarySentinelLabs observed a cluster of virtua
*2023-2-2 18:55:59
Author: [www.sentinelone.com(查看原文)](/jump-147714.htm)
阅读量:68
收藏*

---

**By Aleksandar Milenkoski and Tom Hegel**

## Executive Summary

* SentinelLabs observed a cluster of virtualized .NET malware loaders distributed through malvertising attacks.
* The loaders, dubbed MalVirt, use obfuscated virtualization for anti-analysis and evasion along with the Windows Process Explorer driver for terminating processes.
* MalVirt loaders are currently distributing malware of the Formbook family as part of an ongoing campaign.
* To disguise real C2 traffic and evade network detections, the malware beacons to random decoy C2 servers hosted at different hosting providers, including Azure, Tucows, Choopa, and Namecheap.

## Overview

While [investigating](https://www.sentinelone.com/blog/breaking-down-the-seo-poisoning-attack-how-attackers-are-hijacking-search-results/) recent malvertising (malicious advertising) attacks, SentinelLabs spotted a cluster of virtualized malware loaders that has joined the trend. The loaders are implemented in .NET and use virtualization, based on the [KoiVM](https://github.com/Loksie/KoiVM-Virtualization) virtualizing protector of .NET applications, in order to obfuscate their implementation and execution. We refer to these loaders as MalVirt (a recently [observed](https://labs.k7computing.com/index.php/koivm-loader-resurfaces-with-a-bang/) and likely related implementation is referred to as KoiVM Loader). Although popular for hacking tools and cracks, the use of KoiVM virtualization is [not often seen](https://blogs.blackberry.com/en/2022/03/lokilocker-ransomware) as an obfuscation method utilized by cybercrime threat actors.

Among the payloads that MalVirt loaders distribute, we spotted infostealer malware of the [Formbook family](https://malpedia.caad.fkie.fraunhofer.de/details/win.formbook) as part of an ongoing campaign at the time of writing. The distribution of this malware through the MalVirt loaders is characterized by an unusual amount of applied anti-analysis and anti-detection techniques.

The current spikes in threat actors using alternative malware distribution methods to Office macros, such as malvertising, [Windows Shortcuts](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) (LNK files), and ISO [files](https://www.darkreading.com/endpoint/post-macro-world-container-files-distribute-malware-replacement), comes as a response to Microsoft [blocking by default](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked) Office macros in documents from the Internet. Malvertising is a malware delivery method that is currently very popular among threat actors, marked by a significant increase in malicious search engine advertisements in recent weeks.

The Formbook family – [Formbook](https://www.fortinet.com/blog/threat-research/deep-analysis-new-formbook-variant-delivered-phishing-campaign-part-I) and its newer version XLoader –  is a feature-rich infostealer malware that implements a wide range of functionalities, such as keylogging, screenshot theft, theft of web and other credentials, and staging of additional malware. For example, one of the hallmarks of XLoader is its [intricate](https://research.checkpoint.com/2021/stealth-is-never-enough-or-revealing-formbook-successors-cc-infrastructure/) [disguising](https://research.checkpoint.com/2022/xloader-botnet-find-me-if-you-can/) of C2 [traffic](https://www.zscaler.com/blogs/security-research/analysis-xloaders-c2-network-encryption).

This malware is sold on the dark web and is traditionally delivered as an attachment to phishing emails. While it is typically used by threat actors with cybercrime motivations, its use has also been recently observed as part of attacks with potentially political motivations – in September 2022,  Ukraine’s CERT [reported](https://cert.gov.ua/article/37688) a Formbook/XLoader campaign [targeting](https://www.theregister.com/2022/03/16/ukraine_cobalt_caddywipe/) Ukrainian state organizations through war-themed phishing emails. In the case of an intricate loader, this could suggest an attempt to co-opt cybercriminal distribution methods to load more targeted second-stage malware onto specific victims after initial validation.

We focus on the MalVirt loaders and the infostealer malware subsequently distributed by them in order to highlight the effort the threat actors have invested in evading detection and thwarting analysis.

## The MalVirt Loaders

We first spotted a MalVirt sample when [performing](https://www.sentinelone.com/blog/breaking-down-the-seo-poisoning-attack-how-attackers-are-hijacking-search-results/) a routine Google search for “Blender 3D” and [examining](https://twitter.com/TomHegel/status/1616540242949070848) the Ad results.

![Malicious advertisements (“Blender 3D” Google search)](https://www.sentinelone.com/wp-content/uploads/2023/01/MalVirt_15.jpg)

The MalVirt samples we analyzed have the PDB path

```
C:\Users\Administrator\source\repos\DVS-Calculator-Windows-App-main\Calculator\obj\x86\Debug\Calculator.pdb
```

They can be further characterized by obfuscated namespace, class, and function names composed of alphanumeric characters, such as `Birthd1y` or `Tota2`, in the same manner as previously [observed](https://www.fortinet.com/blog/threat-research/deep-analysis-new-formbook-variant-delivered-phishing-campaign-part-I) Formbook loaders.

![MalVirt namespace, class, and function names](https://www.sentinelone.com/wp-content/uploads/2023/01/MalVirt_6.jpg)

MalVirt namespace, class, and function names

The loaders pretend to be digitally signed using signatures and countersignatures from companies such as Microsoft, Acer, DigiCert, Sectigo, and AVG Technologies USA. However, in each case the signatures are invalid, created using invalid certificates or are certificates untrusted by the system (i.e., not stored in the Trusted Root Certification Authorities certificate store). For example, the following certificate appears to be from Microsoft but doesn’t pass signature validation.

* Name: Microsoft Corporation
* Thumbprint: 8c2136e83f9526d3c44c0bb0bccc6cf242702b16
* Serial Number: 00b6bce5a3c0e0111b78adf33d9fdc3793

![A digital signature of a MalVirt sample](https://www.sentinelone.com/wp-content/uploads/2023/01/MalVirt_16.jpg)

A digital signature of a MalVirt sample

The MalVirt loaders we analyzed, especially those distributing malware of the Formbook family, implement a range of anti-analysis and anti-detection techniques, with some variations across MalVirt samples. For example, some samples patch the `AmsiScanBuffer` function implemented in `amsi.dll` to bypass the Anti Malware Scan Interface (AMSI) that detects malicious PowerShell commands.

Further, in an attempt to evade static detection mechanisms, some strings (such as `amsi.dll` and `AmsiScanBuffer`) are Base-64 encoded and AES-encrypted. The MalVirt loaders decode and decrypt such strings using hardcoded, Base64-encoded AES encryption keys.

![String decryption](https://www.sentinelone.com/wp-content/uploads/2023/01/MalVirt_1.jpg)

String decryption

We also observed MalVirt samples evaluating whether they are executing within a virtual machine or an application sandbox environment. For example, detecting the VirtualBox and VMWare environments involves querying t...