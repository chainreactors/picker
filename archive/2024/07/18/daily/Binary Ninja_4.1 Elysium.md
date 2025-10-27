---
title: 4.1 Elysium
url: https://binary.ninja/2024/07/17/4.1-elysium.html
source: Binary Ninja
date: 2024-07-18
fetch_date: 2025-10-06T17:43:18.869637
---

# 4.1 Elysium

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
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

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## 4.1 Elysium

* [Jordan Wiens](https://github.com/psifertex)
* 2024-07-17
* [announcements](/tag/announcements), [stable](/tag/stable)

![Binja character wearing sci-fi exoskeleton in the style of the movie Elysium >](/blog/images/4.1-release/elysium.png)

What a release! Even we were surprised when we started tallying up all the major improvements since 4.0. Even though this is a minor version increment, the list of improvements is huge. Itâs hard to pick favorites as weâve seen major improvements in decompilation quality, multiple new architectures, type library improvements across most of the supported platforms and so many other important new features.

* [Decompiler Improvements](/2024/07/17/4.1-elysium.html#decompiler-improvements)
* [Linux ARM Builds](/2024/07/17/4.1-elysium.html#linux-arm-builds)
* [UEFI Enhancements](/2024/07/17/4.1-elysium.html#uefi-enhancements)
* [BASE](/2024/07/17/4.1-elysium.html#binary-ninja-base-address-scan-engine-base)
* [UI Improvements](/2024/07/17/4.1-elysium.html#ui-improvements)
  + [History Widget](/2024/07/17/4.1-elysium.html#history-widget)
  + [Address Display / Stack View](/2024/07/17/4.1-elysium.html#address-display--stack-view)
* [macOS/iOS/Objective-C Improvements](/2024/07/17/4.1-elysium.html#macosiosobjective-c-improvements)
* [Fallback Libc](/2024/07/17/4.1-elysium.html#fallback-libc)
* [Debugger](/2024/07/17/4.1-elysium.html#debugger)
  + [Debugger Annotations and Memory Map API](/2024/07/17/4.1-elysium.html#debugger-annotations-and-memory-map-api)
  + [Time-Travel Debugging](/2024/07/17/4.1-elysium.html#ttd-made-easy)
* [Architecture/Platform Changes](/2024/07/17/4.1-elysium.html#architecture--platform-changes)
  + [Platform Changes](/2024/07/17/4.1-elysium.html#platform-changes)
  + [Octeon Support](/2024/07/17/4.1-elysium.html#octeon-support)
  + [TriCore](/2024/07/17/4.1-elysium.html#tricore)
* [Open-Source Contributions](/2024/07/17/4.1-elysium.html#open-source-contributions)
* [Many More](/2024/07/17/4.1-elysium.html#other-updates)

# Major Features

## Decompiler Improvements

With Binary Ninja 4.1, our out of the box decompilation quality has dramatically improved. Of course, many of the features later in this blog all contribute to this improvement, but the most impactful change has been our [control flow recovery](https://binary.ninja/2024/06/19/restructuring-the-decompiler.html) changes. Along with dedicated verification by emulating IL to validate transformations, weâve been able to not only improve the accuracy of our decompilation, but the readability as well.

Hereâs one small example showing a C runtime function before and after this change:

![Control Flow Before After](/blog/images/4.1-release/graph-transform.png)

While itâs impossible to convey the improvements exactly for any given binary, we ran a quick [script](https://gist.github.com/psifertex/284a115762c5b461a4ed87a237152b8f) across a recent `ntoskrnl.exe` and saw show fantastic improvements: we observed 8% less `if` statements, and 34% more `for` loops. This was in addition to a decrease in 28% of total conditional instructions. Combined with the higher accuracy of our transformations, this again shows that not only is the decompilation better, it should be far more readable too.

Weâve also added many new boolean simplifications. While the higher level restructuring means they are needed far less frequently, when they do show up this will also result in far easier to read decompilation. See the detailed list of changes at the bottom of the blog for examples of the many types of boolean simplification added.

Of course many other changes also improved decompilation quality as well. In addition to the many type library improvements described below, we also improved lifting across multiple architectures. How much of a difference can that make? Check out this before/after from [improved lifting](https://github.com/Vector35/binaryninja-api/commit/c3040ecfc43983af6f05da13cf2242d085b1e230):

![](/blog/images/4.1-release/checkpw-after.png)
![](/blog/images/4.1-release/checkpw-before.png)

Also, if you want to understand more about the internals of our decompilation, make sure to check out our recent blog post on [Debug Visualizations](https://binary.ninja/2024/07/15/debug-visualizations.html) built right into the product. They show in great detail how every step of analysis happens.

## Linux ARM Builds

![Phido chasing a penguin >](/blog/images/4.1-release/phido-penguin.png)

Whether youâre an Apple Silicon user missing your x86 virtual machines, or one of the few running ARM Linux on a native platform, either way weâve got you covered. Elysium now has official support for ARM Linux on our [officially supported](https://binary.ninja/faq/#supported-platforms) Linux platforms. Weâd show screenshots of the UI, but itâs justâ¦ the same UI as always. Except on ARM. So instead, enjoy this image of Phido chasing a penguin.

Note that the [free version](https://binary.ninja/free/) of Binary Ninja is not being released on ARM Linux in 4.1 due to ARMv8 not being included in free.

## UEFI Enhancements

While [we announced](https://binary.ninja/2023/09/15/3.5-expanded-universe.html#uefi-support) UEFI support with a plugin and core changes in Binary Ninja 3.5, this release brings a host of improvements to that support. First, we now have a [Terse Executable (TE) view](https://github.com/Vector35/binaryninja-api/blob/dev/view/pe/teview.cpp). Additionally, we added new platform types for System Management Mode (SMM), Pre-EFI Initialization (PEI), and PEIM-to-PEIM Interfaces (PPI). New functionality has been added to [EFI Resolver](https://github.com/Vector35/efi-resolver) to make use of these new types to identify SMM protocol interfaces and PPIs and to provide enhanced supplemental analysis for PEI and SMM modules. Some of the new types even take advantage of Binary Ninjaâs [offset pointers](https://binary.ninja/2022/10/28/3.2-released.html#offset-pointers) to allow EFI Resolver to identify accesses to PEI services relative to the x86 Interrupt Descriptor Table (IDT)!

![UEFI](/blog/images/4.1-release/uefi.png)

## Binary Ninja Base Address Scan Engine (BASE)

Announced a few months ago in a previous [blog post](https://Binary Ninja Base Address Scan Engine (BASE)), our new BASE feature is now live on version 4.1. Itâs designed to automatically identify the correct load address when reverse engineering embedded firmware. True to our philosophy of âdo the right thing by defaultâ we have an intelligent set of default settings to automatically identify a binary blobâs default load address, but we also expose a large number of [advanced settings](https://docs.binary.ninja/guide/index.html#4-base-address-detection-base) to let you tune the search to your needs.

![BASE](/blog/images/4.1-release/base.png)

## UI Improvements

### History Widget

A brand new UI feature was added for 4.1: a history widget! Accessible from the bottom-right sidebar panel by default, this view even lets you see changes in databases that were created prior to the UI existing as our database format has supported this information since the first rel...