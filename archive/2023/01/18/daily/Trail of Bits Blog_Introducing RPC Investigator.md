---
title: Introducing RPC Investigator
url: https://blog.trailofbits.com/2023/01/17/rpc-investigator-microsoft-windows-remote-procedure-call/
source: Trail of Bits Blog
date: 2023-01-18
fetch_date: 2025-10-04T04:08:07.141270
---

# Introducing RPC Investigator

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Introducing RPC Investigator

Aaron LeMasters

January 17, 2023

[engineering-practice](/categories/engineering-practice/), [research-practice](/categories/research-practice/)

*A new tool for Windows RPC research*

Trail of Bits is releasing a new tool for exploring RPC clients and servers on Windows. RPC Investigator is a .NET application that builds on the [NtApiDotNet](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet) platform for enumerating, decompiling/parsing and communicating with arbitrary RPC servers. We’ve added visualization and additional features that offer a new way to explore RPC.

RPC is an important communication mechanism in Windows, not only because of the flexibility and convenience it provides software developers but also because of the renowned attack surface its implementers afford to exploit developers. While there has been extensive research published related to RPC servers, interfaces, and protocols, we feel there’s always room for additional tooling to make it easier for security practitioners to explore and understand this prolific communication technology.

Below, we’ll cover some of the background research in this space, describe the features of RPC Investigator in more detail, and discuss future tool development.

If you prefer to go straight to the code, check out [RPC Investigator on Github](https://github.com/trailofbits/RpcInvestigator).

## Background

Microsoft Remote Procedure Call (MSRPC) is a prevalent communication mechanism that provides an extensible framework for defining server/client interfaces. MSRPC is involved on some level in nearly every activity that you can take on a Windows system, from logging in to your laptop to opening a file. For this reason alone, it has been a popular research target in both the defensive and offensive infosec communities for decades.

A few years ago, the developer of the open source .NET library [NtApiDotNet](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtApiDotNet), James Foreshaw, updated his library with functionality for decompiling, constructing clients for, and interacting with arbitrary RPC servers. In an excellent [blog post](https://googleprojectzero.blogspot.com/2019/12/calling-local-windows-rpc-servers-from.html)—focusing on using the new `NtApiDotNet` functionality via powershell scripts and cmdlets in his [`NtObjectManager`](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtObjectManager) package—he included a small section on how to use the powershell scripts to generate C# code for an RPC client that would work with a given RPC server and then compile that code into a C# application.

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

If you want to observe the debug output that is written to the RPCI log, set the appropriate trace level in the Settings window. The RPCI log and all other related files are written to the current user’s application data folder, which is typically `C:\Users\(user)\AppData\Roaming\RpcInvestigator`. To view this folder, simply navigate to `View -> Logs`. However, we recommend disabling tracing to improve performance.

It’s important to note that the bitness of RPCI must match that of the system: if you run 32-bit RPCI on a 64-bit system, only RPC servers hosted in 32-bit processes or binaries will be accessible (which is most likely none).

### Searching for RPC servers

The first thing you’ll want to do is find the RPC servers that are running on your system. The most straightforward way to do this is to query the RPC endpoint mapper, a persistent service provided by the operating system. Because most local RPC servers are actually ALPC servers, this query is exposed via the `File -> All RPC ALPC Servers…` menu item.

[![](/img/wpdump/0ca19dae570072f9953d7e68bff22ab1.png)](/img/wpdump/0ca19dae570072f9953d7e68bff22ab1.png)

The discovered servers are listed in a table view according to the hosting process, as shown in the screenshot above. This table view is one starting point for navigating RPC servers in RPCI. Double-clicking a particular server will open another tab that lists all endpoints and their corresponding interface IDs. Double-clicking an endpoint will open another tab that lists all procedures that can be invoked on that endpoint’s interface. Right-clicking on an endpoint will open a context menu that presents other useful shortcuts, one of which is to create a new client to connect to this endpoint’s interface. We’ll describe that feature in a later section.

You can locate other RPC servers that are not running (or are not ALPC) by parsing the server’s image by selecting `File -> Load from binary…` and locating the image on disk, or by selecting `File->Load from service…` and selecting the service of interest (this will parse all servers in all modules loaded in the service process).

### Exploring the Library

The other starting point for navigating RPC servers is to load the library view. The library is a file containing serialized .NET objects for every RPC server you have discovered while using RPCI. Simply select the menu item `Library -> Servers` to view all discovered RPC servers and `Library -> Procedures` to view all discovered procedures for all server interfaces. Both menu items will open in new tabs. To perform a quick keyword search in either ...