---
title: Binary Ninja 5.3 (Jotunheim)
url: https://binary.ninja/2026/04/13/binary-ninja-5.3-jotunheim.html
source: Binary Ninja
date: 2026-04-13
fetch_date: 2026-04-14T04:44:23.759609
---

# Binary Ninja 5.3 (Jotunheim)

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Portal](https://portal.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Binary Ninja [5.3 (Jotunheim) is out](/2026/04/13/binary-ninja-5.3-jotunheim.html) and includes better interoperability with both Ghidra and IDA, NDS32 decompilation, and more.

# Binary Ninja Blog

## Binary Ninja 5.3 (Jotunheim)

* [Jordan Wiens](https://github.com/psifertex)
* 2026-04-13
* [announcements](/tag/announcements), [stable](/tag/stable)

![Binjas, assemble! This release is code-named Jotunheim in honor of Norse mythology though of course the modern Marvel re-telling is perhaps the most well-known. >](/blog/images/5.3-release/jotunheim.jpg)

For Binary Ninja 5.3, weâre bringing features and fixes across a number of areas. For improved interoperability, weâve added [Ghidra Export](/2026/04/13/binary-ninja-5.3-jotunheim.html#ghidra-export) to the existing [Ghidra Import](/2025/11/13/binary-ninja-5.2-io.html#ghidra-import) code and have improved our [IDB Import](/2026/04/13/binary-ninja-5.3-jotunheim.html#idb-import-improvements) capability. For new architectures and platforms, weâve added [NDS32](/2026/04/13/binary-ninja-5.3-jotunheim.html#nds32) to Ultimate, a new [ILP32 ABI](/2026/04/13/binary-ninja-5.3-jotunheim.html#aarch64-ilp32-abi) for AArch64, and a new set of APIs for [âweirdâ architectures](/2026/04/13/binary-ninja-5.3-jotunheim.html#new-architecture-apis). And of course, weâve made a number of improvements to the UI including a new [Universal Mach-O loader UI](/2026/04/13/binary-ninja-5.3-jotunheim.html#mach-o-architecture-picker), usability improvements to the [container browser](/2026/04/13/binary-ninja-5.3-jotunheim.html#container-browser-improvements), and a new [âsuperâ command palette](/2026/04/13/binary-ninja-5.3-jotunheim.html#command-palette-refresh)! Plus, changes to the [debugger](/2026/04/13/binary-ninja-5.3-jotunheim.html#debugger), [enterprise features](/2026/04/13/binary-ninja-5.3-jotunheim.html#enterprise), new opt-in [crash reporting](/2026/04/13/binary-ninja-5.3-jotunheim.html#crash-reporting) to help us squash bugs faster, and so much more!

* [Architecture / Platform](/2026/04/13/binary-ninja-5.3-jotunheim.html#architecture--platform)
  + [New Architecture APIs](/2026/04/13/binary-ninja-5.3-jotunheim.html#new-architecture-apis)
  + [NDS32](/2026/04/13/binary-ninja-5.3-jotunheim.html#nds32)
  + [AArch64 ILP32 ABI](/2026/04/13/binary-ninja-5.3-jotunheim.html#aarch64-ilp32-abi)
* [UI](/2026/04/13/binary-ninja-5.3-jotunheim.html#ui)
  + [Mach-O Architecture Picker](/2026/04/13/binary-ninja-5.3-jotunheim.html#mach-o-architecture-picker)
  + [Container Browser Improvements](/2026/04/13/binary-ninja-5.3-jotunheim.html#container-browser-improvements)
  + [Command Palette Refresh](/2026/04/13/binary-ninja-5.3-jotunheim.html#command-palette-refresh)
* [Types & Signatures](/2026/04/13/binary-ninja-5.3-jotunheim.html#types--signatures)
  + [Type Library Utilities](/2026/04/13/binary-ninja-5.3-jotunheim.html#type-library-utilities)
  + [WARP Improvements](/2026/04/13/binary-ninja-5.3-jotunheim.html#warp-improvements)
* [Interoperability](/2026/04/13/binary-ninja-5.3-jotunheim.html#interoperability)
  + [Ghidra Export](/2026/04/13/binary-ninja-5.3-jotunheim.html#ghidra-export)
  + [IDB Import Improvements](/2026/04/13/binary-ninja-5.3-jotunheim.html#idb-import-improvements)
* [Enterprise](/2026/04/13/binary-ninja-5.3-jotunheim.html#enterprise)
* [Debugger](/2026/04/13/binary-ninja-5.3-jotunheim.html#debugger)
  + [Hardware and Conditional Breakpoints](/2026/04/13/binary-ninja-5.3-jotunheim.html#hardware-and-conditional-breakpoints)
  + [New Debug Adapters](/2026/04/13/binary-ninja-5.3-jotunheim.html#new-debug-adapters)
* [Crash Reporting](/2026/04/13/binary-ninja-5.3-jotunheim.html#crash-reporting)
* [Open-Source Contributions](/2026/04/13/binary-ninja-5.3-jotunheim.html#open-source-contributions)
* [Everything Else](/2026/04/13/binary-ninja-5.3-jotunheim.html#everything-else)

# Major Features

## Architecture / Platform

### New Architecture APIs

Building on the new [architecture APIs added in 5.1](https://binary.ninja/2025/07/24/5.1-helion.html#custom-basic-block-analysis), weâve added a new set of APIs to support standalone function-level lifting. Our initial design for Binary Ninja was optimized for multithreaded analysis with as little state as possible so that each basic block could potentially be analyzed in its own thread. However, for plenty of architectures (including a lot of VM-based ones such as Java, Python bytecode, .NET, etc.), there is far too much state or even metadata at the top of each function. The only way to handle such architectures is to enable a single thread to analyze the entire function. While the ABB feature in 5.1 added support for basic block recovery and analysis in a single thread, in 5.3 we now support full function-level lifting.

Internally, weâre using [these APIs](https://api.binary.ninja/binaryninja.architecture-module.html#binaryninja.architecture.Architecture.get_instruction_text_with_context) to work on our upcoming TMS320C6x support, but because we use the same APIs available to third parties, this also means other projects like [banjo](https://github.com/ivision-research/banjo) or some of the WASM plugins weâve heard about could be updated for much better decompilation results using these new APIs.

Keep an eye out for an upcoming blog post explaining more about how you can leverage these APIs yourself!

### NDS32

Ultimate customers will appreciate the brand new NDS32 support. We now have 18 officially supported architectures including full decompilation in our Ultimate/Enterprise edition!

[![nds32-libstdc++.so decompilation](/blog/images/5.3-release/nds32-decompilation.png)](/blog/images/5.3-release/nds32-decompilation.png)

### AArch64 ILP32 ABI

Itâs not enough to just have support for the instructions in a CPU architecture since there are lots of platforms or variants that need to be supported. For example, ILP32 adds a mode for AArch64 that has 32-bit pointers despite still using 64-bit mode. In 5.3, weâve not only [added the platform](https://github.com/Vector35/binaryninja-api/commit/d634a5d6527f7ec203907f17cde8d0d807028fe3), but also [updated our function recognizer](https://github.com/Vector35/binaryninja-api/commit/6be9a1fce3d750613d2605c57f0c911d5dc569d0) for ILP32 PLT entries and [fixed a bug](https://github.com/Vector35/binaryninja-api/commit/c762640d97a6302e9e2a8a5afcc62a6b1a100e7b) related to the address size calculation.

![](/blog/images/5.3-release/ilp32-new.png)
![](/blog/images/5.3-release/ilp32-old.png)

## UI

[![Mach-O Picker >](/blog/images/5.3-release/macho-picker.png)](/blog/images/5.3-release/macho-picker.png)

### Mach-O Architecture Picker

While itâs long been possible to open a specific slice in a fat Mach-O or even adjust your settings to default to a particular slice, the UI around it was fairly painful, reusing our âOpen With Optionsâ dialog in a way that led to a lot of confusion.

In 5.3, you now get a much more streamlined dialog that lets you pick the architecture and, more importantly, makes it easy to set the default for future opens without having to dig through the [settings](https://docs.binary.ninja/guide/settings.html)! The dialog also shows the size of each slice, so you can quickly identify the one you need.

### Container Browser Improvements
...