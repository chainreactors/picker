---
title: Binary Ninja 6.0 (Krypton)
url: https://binary.ninja/2026/09/03/binary-ninja-6.0-krypton.html
source: Binary Ninja
date: 2026-09-03
fetch_date: 2026-09-04T06:42:42.073701
---

# Binary Ninja 6.0 (Krypton)

[Skip to main content](#main-content)

[![Binary Ninja](/images/binary-ninja-wordmark-light-2tone.svg)](/)

Features

[Features Overview](/features/)
[Enterprise](/enterprise/)

[Sidekick](https://sidekick.binary.ninja)
[Portal](https://portal.binary.ninja/dashboard)
[Training](/training/)

Support

[Support Overview](/support/)
[Extended Support](/support/extended.html)
[Documentation](/support/#documentation)
[License/Installer Recovery](/recover/)
[Renew Current License](/renew/)
[Slack Signup](https://slack.binary.ninja/)
[FAQ](/faq/)
[Sponsorship Information](/sponsorship/)
[Contact Us](/support/)

[Blog](/blog/)
[Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Not a bird, a plane, it's [Binary Ninja 6.0](/2026/09/03/binary-ninja-6.0-krypton.html)! A
super-powered release with more improvements than ever. Massive performance gains, binary similarity, TMS320C6x, MCP, and much more.

[Binary Ninja Blog](/blog/)

# Binary Ninja 6.0 (Krypton)

By [Jordan Wiens](https://github.com/psifertex)
 2026-09-03

![Caped Binja flying over the city. >](/blog/images/6.0-release/krypton.jpg)

Binary Ninja 6.0 (Krypton) is here! This is a major version bump and itâs worth the wait. Weâve shipped a brand new [MCP server](/2026/09/03/binary-ninja-6.0-krypton.html#mcp), a new [Binary Similarity](/2026/09/03/binary-ninja-6.0-krypton.html#binary-similarity) feature, and a complete overhaul of the Plugin Manager as the new [Extension Manager](/2026/09/03/binary-ninja-6.0-krypton.html#extension-manager). Under the hood, youâll find major improvements to [performance and memory usage](/2026/09/03/binary-ninja-6.0-krypton.html#performance-and-memory), a refactored [calling convention](/2026/09/03/binary-ninja-6.0-krypton.html#calling-convention-refactor) to properly represent structure parameters and return values, and added [HLIL structure initializers](/2026/09/03/binary-ninja-6.0-krypton.html#hlil_struct_initialize). On the scripting side, weâve upgraded the bundled Python to [3.13](/2026/09/03/binary-ninja-6.0-krypton.html#python-313-and-linux) and included it on Linux. Weâve also added a new [TMS320C6x](/2026/09/03/binary-ninja-6.0-krypton.html#tms320c6x) architecture, a [new user wizard](/2026/09/03/binary-ninja-6.0-krypton.html#new-user-wizard) to ease migration, and a long list of [debugger](/2026/09/03/binary-ninja-6.0-krypton.html#debugger) improvements. And those are still only some of the new features detailed below.

Weâre also improving the [free edition](/2026/09/03/binary-ninja-6.0-krypton.html#new-features-in-free). Weâve added the highly requested `armv8` (AArch64) architecture as well as the above mentioned MCP server. Additionally, weâre also shipping a new Linux ARM64 build of the free version. Next, as previously [announced](/2026/07/28/pricing-changes.html), with this release weâre putting our new [pricing and packaging](/2026/09/03/binary-ninja-6.0-krypton.html#pricing-and-packaging) into effect. Finally, thanks to everyone who participated in our [10 year celebration](/2026/07/22/10-years-of-binary-ninja.html), weâre looking forward to another decade!

* [Performance and Memory](/2026/09/03/binary-ninja-6.0-krypton.html#performance-and-memory)
  + [Analysis Cache](/2026/09/03/binary-ninja-6.0-krypton.html#analysis-cache)
  + [Database Saving](/2026/09/03/binary-ninja-6.0-krypton.html#database-saving)
* [MCP](/2026/09/03/binary-ninja-6.0-krypton.html#mcp)
* [Binary Similarity](/2026/09/03/binary-ninja-6.0-krypton.html#binary-similarity)
* [Architectures and Platforms](/2026/09/03/binary-ninja-6.0-krypton.html#architectures-and-platforms)
  + [TMS320C6x](/2026/09/03/binary-ninja-6.0-krypton.html#tms320c6x)
  + [Multiple Global Pointers](/2026/09/03/binary-ninja-6.0-krypton.html#multiple-global-pointers)
* [Analysis](/2026/09/03/binary-ninja-6.0-krypton.html#analysis)
  + [Improved BASE (Fast Analysis Mode)](/2026/09/03/binary-ninja-6.0-krypton.html#improved-base-fast-analysis-mode)
  + [Calling Convention Refactor](/2026/09/03/binary-ninja-6.0-krypton.html#calling-convention-refactor)
  + [HLIL\_STRUCT\_INITIALIZE](/2026/09/03/binary-ninja-6.0-krypton.html#hlil_struct_initialize)
  + [Type Fragments](/2026/09/03/binary-ninja-6.0-krypton.html#type-fragments)
* [Scripting and Extensions](/2026/09/03/binary-ninja-6.0-krypton.html#scripting-and-extensions)
  + [Python 3.13 and Linux](/2026/09/03/binary-ninja-6.0-krypton.html#python-313-and-linux)
  + [Scripting Console](/2026/09/03/binary-ninja-6.0-krypton.html#scripting-console)
  + [Extension Manager](/2026/09/03/binary-ninja-6.0-krypton.html#extension-manager)
* [New User Wizard](/2026/09/03/binary-ninja-6.0-krypton.html#new-user-wizard)
* [Debugger](/2026/09/03/binary-ninja-6.0-krypton.html#debugger)
* [Packaging and Licensing](/2026/09/03/binary-ninja-6.0-krypton.html#packaging-and-licensing)
  + [New Features in Free](/2026/09/03/binary-ninja-6.0-krypton.html#new-features-in-free)
  + [Pricing and Packaging](/2026/09/03/binary-ninja-6.0-krypton.html#pricing-and-packaging)
  + [Server Deployments](/2026/09/03/binary-ninja-6.0-krypton.html#server-deployments)
* [Open-Source Contributions](/2026/09/03/binary-ninja-6.0-krypton.html#open-source-contributions)
* [Everything Else](/2026/09/03/binary-ninja-6.0-krypton.html#everything-else)

# Major Features

## Performance and Memory

Letâs get some universally applicable improvements out of the way first. No matter how you use Binary Ninja, youâll see some fantastic speedups in 6.0 while also seeing decreases in memory usage. Exact improvements depend on the workload and hardware so we picked some representative sample binaries and ran a gamut of testing including multiple runs (for all samples but Chrome) to ensure reliability. The results speak for themselves.

5.3 stable
6.0 stable

syspolicyd

Mach-O universal, x86-64 slice

4,215 functions2.6 MB

Analysis time

13.8s7.0s

1.97× faster

Peak memory

2.81 GB2.30 GB

18% less

CPU instructions

0.51T0.41T

19% fewer

chrome\_crashpad\_handler

ELF x86-64

6,092 functions1.9 MB

Analysis time

32.8s30.9s

1.06× faster

Peak memory

3.00 GB2.03 GB

32% less

CPU instructions

0.96T0.76T

21% fewer

locationd

Mach-O universal, x86-64 slice

28,372 functions19.0 MB

Analysis time

63.9s41.4s

1.54× faster

Peak memory

6.06 GB3.62 GB

40% less

CPU instructions

3.33T2.79T

16% fewer

ntoskrnl.exe

PE32+ x86-64

34,146 functions12.8 MB

Analysis time

257s128s

2.02× faster

Peak memory

8.78 GB3.96 GB

55% less

CPU instructions

18.3T8.57T

53% fewer

libbinaryninjaui.so.1

ELF x86-64 shared object

43,957 functions136.1 MB

Analysis time

76.4s55.6s

1.37× faster

Peak memory

8.48 GB7.90 GB

7% less

CPU instructions

3.26T2.94T

10% fewer

vmlinux 6.14

ELF AArch64, with DWARF

92,961 functions511.8 MB

Analysis time

761s352s

2.16× faster

Peak memory

17.29 GB12.25 GB

29% less

CPU instructions

46.7T22.6T

52% fewer

chrome

ELF x86-64, with DWARF

950,042 functions1.47 GB

Analysis time

1186s584s

2.03× faster

Peak memory

43.85 GB32.82 GB

25% less

CPU instructions

59.3T38.3T

35% fewer

How this was measured

Machine
:   AMD Ryzen 9 9950X (16 cores, 32 threads), 96 GB RAM, Ubuntu 26.04. Measurements made while idle.

Procedure
:   Default headless analysis to completion including full decompilation, three runs per binary (one for Chrome, which takes ten minutes a run), reporting the mean. Time is wall-clock analysis time; memory is peak resident set size.

As you can see, across a representative corpus, 6.0 analyzes up to 2.16 times faster than 5.3 while using as much as 55% less peak memory.

These gains come from many changes rather than any single optimization. There were dozens of smaller fixes, hundreds of hours of profiling, new tools developed to analyze memory usage, and Brian, Mark, Ryan, and others working to optimize the system. Nothing was sacred: many long-standing data structures and sections of code were critically ex...