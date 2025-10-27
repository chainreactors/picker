---
title: 3.2 Release
url: https://binary.ninja/2022/10/28/3.2-released.html
source: Binary Ninja
date: 2022-10-29
fetch_date: 2025-10-03T21:13:44.298904
---

# 3.2 Release

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

## 3.2 Release

* [Alexander Taylor](https://github.com/fuzyll)
* 2022-10-28
* [announcements](/tag/announcements), [stable](/tag/stable)

After 4 long months of development, Binary Ninja 3.2 is finally here with a huge list of major changes and an even bigger list of minor ones:

* [Enhanced Windows Experience](/2022/10/28/3.2-released.html#enhanced-windows-experience)
  + [Improved Enumeration Support](/2022/10/28/3.2-released.html#improved-enumerations)
  + [Next-Generation PDB Support](/2022/10/28/3.2-released.html#next-generation-pdb-support)
  + [CFG Call Handling](/2022/10/28/3.2-released.html#cfg-call-handling)
  + [MS Demangler Improvements](/2022/10/28/3.2-released.html#ms-demangler-improvements)
* [Decompiler Improvements](/2022/10/28/3.2-released.html#decompiler-improvements)
  + [Variable Merging/Splitting](/2022/10/28/3.2-released.html#variable-mergingsplitting)
  + [Offset Pointers](/2022/10/28/3.2-released.html#offset-pointers)
  + [Split Loads and Stores](/2022/10/28/3.2-released.html#split-loads-and-stores)
* [Objective-C Support](/2022/10/28/3.2-released.html#objective-c-support)
* [Segments and Sections Editing UI](/2022/10/28/3.2-released.html#segments-and-sections-editing-ui)
* [Default to Clang Type Parser](/2022/10/28/3.2-released.html#default-to-clang-type-parser)
* [Named and Computer Licenses for Enterprise](/2022/10/28/3.2-released.html#named-and-computer-licenses-for-enterprise)
* [Many More](/2022/10/28/3.2-released.html#other-updates)

While we have some additional Windows improvements coming in future releases, the majority of our short-term Windows roadmap has been completed for this release and should represent a major improvement for all Binary Ninja users working with PE binaries.

## Price Change

As a reminder: The price of Commercial license purchases and support renewals will be increasing to $1499 and $749 respectively on **November 1, 2022**. If youâd like to get a copy (or renew your support) of Binary Ninja Commercial at its current price, act fast! And, if you *really* like the product, remember that you can purchase multiple years of support at once to lock in the current price.

## Major Changes

### Enhanced Windows Experience

For a long time, we labelled this release as the âWindowsâ release. While itâs a bit presumptuous to think any single release could contain everything to solve all Windows binary analysis, our goal was to have this release represent a major step forward for PE support. And, of course, not *all* the features are headliners or Windows-specific, but will still show important improvements. For example, the improved enumeration support below isnât explicitly for Windows, but PE files definitely benefit, especially with improved type library information.

#### Improved Enumerations

![Enum Example >](/blog/images/3.2-release/enum-example.png)

The most commonly up-voted issue still open is about [specifying enumeration values](https://github.com/Vector35/binaryninja-api/issues/1216). While that specific issue has unfortunately been moved to the next release, it turns out that changes made on this release render it unnecessary for most situations! With this release, enums are rendered appropriately in most places in IL once the appropriate type has been set. Even better, this is often handled for you automatically with the [improved Windows type libraries](https://binary.ninja/2022/05/31/3.1-the-performance-release.html#added-types) from 3.1.

Consider the following simple example (to the right) showing how comparisons, math operations, and switch operations using an enum all properly render. Note that this is in addition to existing support for enumerations when typed as a function argument (shown below). That leaves a UI picker to let you choose appropriately matching enums for a given constant as the only remaining feature to be completed.

![Enum Example Arguments](/blog/images/3.2-release/enum-example-arg.png)

#### Next-Generation PDB Support

Binary Ninjaâs PDB support has been rewritten from the ground up. Our previous PDB support was written in-house before any [public specification releases](https://github.com/microsoft/microsoft-pdb) and, while weâre proud to have had one of the first cross-platform solutions to loading PDB files in a reverse engineering tool (weâve never required a particular OS to load debug information, all our features are fully cross-platform), our previous solution for loading PDBs was not without downsides. To improve PDB support, weâve rewritten it entirely to leverage [pdb-rs](https://github.com/willglynn/pdb), which weâre happy to be committing improvements to [upstream](https://github.com/willglynn/pdb/pull/141). Thereâs also [more fixes](https://github.com/Vector35/pdb-rs/branches) planned once that PR is accepted.

This rewrite resulted in [a ton](https://github.com/Vector35/binaryninja-api/issues?q=is%3Aclosed+is%3Aissue+milestone%3A%223.2+%28Windows%29%22+pdb+) of improvements to Binary Ninjaâs PDB support. From leveraging the [DebugInfo APIs](https://api.binary.ninja/binaryninja.debuginfo-module.html) for automatically applying PDB information when available to much better support for loading types, our ability to ingest PDB information has dramatically improved. Itâs also been helpful to have a first-class solution to test the new `DebugInfo` APIs so that we could work on the workflows and UI associated with loading debug information in a way that will benefit other types of debug information in the future.

But, donât just take the number of closed issues as proof, hereâs a great before/after showing how much better the new PDB support is for one particular binary. Note that significantly more types are being properly extracted:

![](/blog/images/3.2-release/pdbng-after.png)
![](/blog/images/3.2-release/pdbng-before.png)

The experience for loading files with associated PDBs is also vastly improved. Instead of having to manually trigger a PDB load as you did on 3.1 (with the Tools -> Plugins -> PDB -> Load menu option), the default behavior is to simply open a PDB (if one exists) *or* download one from public PDB servers (if one is available). Additionally, loading a PDB is both faster and results in more accurate analysis. The old default behavior did a full linear sweep and complete analysis before applying any information gleaned from the PDB, which often resulted in redoing a significant amount of analysis. The new behavior is to load and use the PDB before other analysis begins. We also support significantly more search/discovery of PDB files such as following [`ptr`](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/symbol-storage-format) files and [environment variables](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/environment-variables). You can, of course, modify this default behavior using [Open With Options](https://docs.binary.ninja/guide/index.html#loading-files) or by changing settings in the PDB category.

#### CFG Call Handling

Two important issues for Control Flow Guard (CFG) call handling were fixed that can really improve the reversing experience for PE files. ...