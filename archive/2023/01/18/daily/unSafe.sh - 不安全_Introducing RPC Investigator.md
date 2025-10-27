---
title: Introducing RPC Investigator
url: https://buaq.net/go-145958.html
source: unSafe.sh - 不安全
date: 2023-01-18
fetch_date: 2025-10-04T04:07:29.684538
---

# Introducing RPC Investigator

* [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh)
* [жҲ‘зҡ„ж”¶и—Ҹ](/user/collects)
* [д»Ҡж—ҘзғӯжҰң](/?hot=true)
* [е…¬дј—еҸ·ж–Үз«](/?gzh=true)
* [еҜјиҲӘ](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [зј–з Ғ/и§Јз Ғ](/encode)
* [ж–Үд»¶дј иҫ“](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
й»‘еӨңжЁЎејҸ

![](https://8aqnet.cdn.bcebos.com/b54456dd82b071ea4c9587d36e1201b3.jpg)

Introducing RPC Investigator

A new tool for Windows RPC researchBy Aaron LeMastersTrail of Bits is releasing
*2023-1-17 21:0:6
Author: [blog.trailofbits.com(жҹҘзңӢеҺҹж–Ү)](/jump-145958.htm)
йҳ…иҜ»йҮҸ:42
ж”¶и—Ҹ*

---

*A new tool for Windows RPC research*

***By Aaron LeMasters***

Trail of Bits is releasing a new tool for exploring RPC clients and servers on Windows. RPC Investigator is a .NET application that builds on the [NtApiDotNet](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet) platform for enumerating, decompiling/parsing and communicating with arbitrary RPC servers. WeвҖҷve added visualization and additional features that offer a new way to explore RPC.

RPC is an important communication mechanism in Windows, not only because of the flexibility and convenience it provides software developers but also because of the renowned attack surface its implementers afford to exploit developers. While there has been extensive research published related to RPC servers, interfaces, and protocols, we feel thereвҖҷs always room for additional tooling to make it easier for security practitioners to explore and understand this prolific communication technology.

Below, weвҖҷll cover some of the background research in this space, describe the features of RPC Investigator in more detail, and discuss future tool development.

If you prefer to go straight to the code, check out [RPC Investigator on Github](https://github.com/trailofbits/RpcInvestigator).

## Background

Microsoft Remote Procedure Call (MSRPC) is a prevalent communication mechanism that provides an extensible framework for defining server/client interfaces. MSRPC is involved on some level in nearly every activity that you can take on a Windows system, from logging in to your laptop to opening a file. For this reason alone, it has been a popular research target in both the defensive and offensive infosec communities for decades.

A few years ago, the developer of the open source .NET library [NtApiDotNet](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet), James Foreshaw, updated his library with functionality for decompiling, constructing clients for, and interacting with arbitrary RPC servers. In an excellent [blog post](https://googleprojectzero.blogspot.com/2019/12/calling-local-windows-rpc-servers-from.html)вҖ”focusing on using the new `NtApiDotNet` functionality via powershell scripts and cmdlets in his [`NtObjectManager`](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtObjectManager) packageвҖ”he included a small section on how to use the powershell scripts to generate C# code for an RPC client that would work with a given RPC server and then compile that code into a C# application.

We built on this concept in developing RPC Investigator (RPCI), a .NET/C# Windows Forms UI application that provides a visual interface into the existing core RPC capabilities of the `NtApiDotNet` platform:

* Enumerating all active ALPC RPC servers
* Parsing RPC servers from any PE file
* Parsing RPC servers from processes and their loaded modules, including services
* Integration of symbol servers
* Exporting server definitions as serialized .NET objects for your own scripting

Beyond visualizing these core features, RPCI provides additional capabilities:

* The Client Workbench allows you to create and execute an RPC client binary on the fly by right-clicking on an RPC server of interest. The workbench has a C# code editor pane that allows you to edit the client in real time and observe results from RPC procedures executed in your code.
* Discovered RPC servers are organized into a library with a customizable search interface, allowing you to pivot RPC server data in useful ways, such as by searching through all RPC procedures for all servers for interesting routines.
* The RPC Sniffer tool adds visibility into RPC-related Event Tracing for Windows (ETW) data to provide a near real-time view of active RPC calls. By combining ETW data with RPC server data from `NtApiDotNet`, we can build a more complete picture of ongoing RPC activity.

## Features

**Disclaimer:** Please exercise caution whenever interacting with system services. It is possible to corrupt the system state or cause a system crash if RPCI is not used correctly.

### Prerequisites and System Requirements

Currently, RPCI requires the following:

* The Windows operating system
* [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) or newer
* The [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/) with the [Debugging Tools for Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) component installed
* Administrator access

By default, RPCI will automatically discover the Debugging Tools for Windows installation directory and configure itself to use the public Windows symbol server. You can modify these settings by clicking `Edit -> Settings`. In the Settings dialog, you can specify the path to the debugging tools DLL (dbghelp.dll) and customize the symbol server and local symbol directory if needed (for example, you can specify the path `srv*c:\symbols*https://msdl.microsoft.com/download/symbols`).

If you want to observe the debug output that is written to the RPCI log, set the appropriate trace level in the Settings window. The RPCI log and all other related files are written to the current userвҖҷs application data folder, which is typically `C:\Users\(user)\AppData\Roaming\RpcInvestigator`. To view this folder, simply navigate to `View -> Logs`. However, we recommend disabling tracing to improve performance.

ItвҖҷs important to note that the bitness of RPCI must match that of the system: if you run 32-bit RPCI on a 64-bit system, only RPC servers hosted in 32-bit processes or binaries will be accessible (which is most likely none).

### Searching for RPC servers

The first thing youвҖҷll want to do is find the RPC servers that are running on your system. The most straightforward way to do this is to query the RPC endpoint mapper, a persistent service provided by the operating system. Because most local RPC servers are actually ALPC servers, this query is exposed via the `File -> All RPC ALPC ServersвҖҰ` menu item.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/01/Screenshot-2023-01-11-at-6.25.29-PM.png?resize=690%2C465&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/01/Screenshot-2023-01-11-at-6.25.29-PM.png?ssl=1)

The discovered servers are listed in a table view according to the hosting process, as shown in the screenshot above. This table view is one starting point for navigating RPC servers in RPCI. Double-clicking a particular server will open another tab that lists all endpoints and their corresponding interface IDs. Double-clicking an endpoint will open another tab that lists all procedures that can be invoked on that endpointвҖҷs interface. Right-clicking on an endpoint will open a context menu that presents other useful shortcuts, one of which is to create a new client to connect to this endpointвҖҷs interface. WeвҖҷll describe that feature in a later section.

You can locate other RPC servers that are not running (or are not ALPC) by parsing the serverвҖҷs image by selecting `File -> Load from binaryвҖҰ` and locating the image on disk, or by selecting `File->Load from serviceвҖҰ` and sel...