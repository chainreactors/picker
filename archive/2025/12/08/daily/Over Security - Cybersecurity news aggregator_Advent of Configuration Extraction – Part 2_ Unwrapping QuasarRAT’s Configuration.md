---
title: Advent of Configuration Extraction – Part 2: Unwrapping QuasarRAT’s Configuration
url: https://blog.sekoia.io/advent-of-configuration-extraction-part-2-unwrapping-quasarrats-configuration/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-08
fetch_date: 2025-12-09T03:18:16.094120
---

# Advent of Configuration Extraction – Part 2: Unwrapping QuasarRAT’s Configuration

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# Advent of Configuration Extraction – Part 2: Unwrapping QuasarRAT’s Configuration

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Pierre Le Bourhis, Sekoia TDR and Jeremy Scion](#molongui-disabled-link)
December 8 2025

0

22 minutes reading

In the second part of our “Advent of Configuration Extraction” series, we unwrap QuasarRAT, a popular .NET remote access trojan (RAT), and show how to extract its encrypted configuration out of the binary. The article begins by detailing the environment: Jupyter Notebook, [pythonnet](https://github.com/pythonnet/pythonnet), [dnSpy](https://github.com/dnSpy/dnSpy) and friends—so every step is reproducible. Next, it presents the construction of a Python-based extractor for a clean QuasarRAT sample, then extends the approach to handle an obfuscated build.

# RAT in the Chimney: Introducing QuasarRAT

[QuasarRAT](https://github.com/quasar/Quasar) is an open-source RAT that first appeared in 2014, under the name xRAT. Originally published on GitHub as a legitimate Windows remote administration tool. Over time, however, its accessibility, small size, and ease of modification have led to it being frequently abused by cybercriminals and threat actors for malicious purposes. For more information about the RAT itself, the JPCERT made a presentation at the [Botconf 2020](https://github.com/JPCERTCC/QuasarRAT-Analysis/blob/main/slides) which details the origins, variants and capabilities.

Implemented in **C#** on the **.NET Framework**, QuasarRAT lends itself readily to extension, recompilation and customisation. Its open-source codebase has been thoroughly analysed and adapted by threat actors seeking bespoke functionality.

Functionally, QuasarRAT supports a **broad set of remote administration functions**, including features such as system information collection, file management, remote desktop viewing, keylogging, and command execution. While these capabilities can be used for legitimate administrative tasks, they are also commonly leveraged in cyber espionage, unauthorized surveillance, and other forms of intrusion.

It has been observed in multiple attacks orchestrated by both [independent threat actors](https://securelist.com/gitvenom-campaign/115694/) and [state-aligned groups](https://www.botconf.eu/wp-content/uploads/formidable/2/Botconf2022-19-FaouCoteCyr.pdf). Its popularity stems from being lightweight, configurable, and freely available, making it a recurring tool in Windows-targeted malware campaigns.

# Elf’s Workshop Tour: Sleighing the Basics of IL

DnSpy and [ILSpy](https://github.com/icsharpcode/ILSpy) are widely adopted for .NET sample analysis. A [Jupyter Notebook](https://gist.github.com/lbpierre/15e6f3100ab88bf4fc80b5e51ff6dafb) environment has been configured to support configuration extraction development, incorporating libraries for PE/ELF manipulation, decompilation frameworks, and related tasks. To facilitate the environment portability, the configuration has been containerised with Docker.

This installment of “Advent Of Configuration Extraction” focuses exclusively on the .NET decompiler component. The extractor for .NET malware configuration which must interact with the Intermediate Language (*a.k.a IL*) relies on a combination of pythonnet and [dnlib](https://github.com/0xd4d/dnlib). In this arrangement, dnlib serves as the core engine for reading, rewriting, and inspecting .NET assemblies, while pythonnet acts as a bridge that allows Python code to invoke dnlib’s APIs.

*Dnlib is an open-source .NET library designed for deep inspection and modification of .NET assemblies (EXE and DLL files). It exposes metadata, types, methods, attributes, and IL instructions in a programmatic fashion, making it a powerful tool for reverse engineering and malware analysis.*

```
import clr
clr.AddReference("System.Memory")
from System.Reflection import Assembly, MethodInfo, BindingFlags
from System import Type

DNLIB_PATH = 'https://t7f4e9n3.delivery.rocketcdn.me/workspace/utils/dnlib.dll'   # path in docker to dnlib.dll
clr.AddReference(DNLIB_PATH)

import dnlib
from dnlib.DotNet import *
from dnlib.DotNet.Emit import OpCodes

module = dnlib.DotNet.ModuleDefMD.Load(MALWARE_PE_PATH)
```

*Code 1. Python prelude to load a .NET sample to interact with its namespaces, classes and methods*

The preceding Python snippet uses pythonnet’s clr module to load and interact with .NET assemblies. Invoking `AddReference(“System.Memory”)` grants access to low-level memory handling-types. These preliminary calls are required to import the dnlib framework for the next and most required step that will load to pythonnet the dnlib framework. Once dnlib is loaded, the script can open and analyse a .NET PE or DLL, enabling it to:

* Decompile individual function.
* Traverse the assembly structure: namespace, classes, methods, and variables.
* Extract custom types, metadata entries, and embedded strings.

At this stage, the most “critical” portion of the lab setup is complete. The module variable provides programmatic access to the bulk of the decompiled .NET content.

Before proceeding with QuasarRAT configuration extraction, a brief overview of the .NET Intermediate Language is necessary.

Within the .NET decompilation context, Intermediate Language (IL) is also referred to as MicroSoft IL (MSIL) or Common IL (CIL).

IL is a **stack‑based intermediate bytecode** used by .NET. High-level source (C#, VB.NET, *etc.*) compiles into IL, which the Common Language Runtime(CLR) then **JIT-compiles** into native machine code.

IL is a **stack machine**, meaning:

* Instructions **push** values onto a stack.
* Other instructions **pop** values from the stack.
* Operations work on the stack (not registers).

Eac...