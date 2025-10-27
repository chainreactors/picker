---
title: 3.3: The Bytes Must Flow
url: https://binary.ninja/2023/01/18/3.3-the-bytes-must-flow.html
source: Binary Ninja
date: 2023-01-19
fetch_date: 2025-10-04T04:16:51.837618
---

# 3.3: The Bytes Must Flow

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

## 3.3: The Bytes Must Flow

* [Jordan Wiens](https://github.com/psifertex)
* 2023-01-18
* [announcements](/tag/announcements), [stable](/tag/stable)

The future is now; Binary Ninja 3.3 (Arrakis) is available. You may have noticed that weâve renamed our [milestones](https://github.com/Vector35/binaryninja-api/milestones) based on an alphabetical list of famous Sci-Fi/Fantasy planets, and the first release in this theme is named after the famous desert planet from [Dune](https://en.wikipedia.org/wiki/Dune_%28novel%29) - [Arrakis](https://en.wikipedia.org/wiki/Arrakis). The bytes must flow!

So what spicy goodies are in this release?

* [Decompiler Improvements](/2023/01/18/3.3-the-bytes-must-flow.html#decompiler-improvements)
  + [Parameter Rejection](/2023/01/18/3.3-the-bytes-must-flow.html#parameter-rejection)
  + [Improved Objective-C](/2023/01/18/3.3-the-bytes-must-flow.html#improved-objective-c)
  + [Automatic Outlining](/2023/01/18/3.3-the-bytes-must-flow.html#automatic-outlining)
* [Debugger](/2023/01/18/3.3-the-bytes-must-flow.html#debugger)
* [Type Interactions](/2023/01/18/3.3-the-bytes-must-flow.html#type-interactions)
  + [Create Array Dialog](/2023/01/18/3.3-the-bytes-must-flow.html#create-array-dialog)
  + [Import / Export Header Files](/2023/01/18/3.3-the-bytes-must-flow.html#import--export-header-files)
  + [Enumeration Dialog](/2023/01/18/3.3-the-bytes-must-flow.html#enumeration-dialog)
* [More Windows Improvements](/2023/01/18/3.3-the-bytes-must-flow.html#more-windows-improvements)
  + [SEH Prolog/Epilog Inlining](/2023/01/18/3.3-the-bytes-must-flow.html#seh-prologepilog-inlining)
  + [Type Libraries and Signatures](/2023/01/18/3.3-the-bytes-must-flow.html#type-libraries-and-signatures)
* [Enterprise Improvements](/2023/01/18/3.3-the-bytes-must-flow.html#enterprise-improvements)
  + [Named Snapshots](/2023/01/18/3.3-the-bytes-must-flow.html#named-snapshots)
  + [SAML Support](/2023/01/18/3.3-the-bytes-must-flow.html#saml-support)
* [Many More](/2023/01/18/3.3-the-bytes-must-flow.html#other-updates)

## Major Changes

Even though this was a shorter release timeline with a big holiday break in the middle, we still managed a huge list of features for this release. In only 2.5 months we have (we dare-say) released a bigger set of new features and  fixes than other tools might get in a year! Itâs quite the mix of fixes, usability improvements, and new features.

### Decompiler Improvements

Our first three major improvements all serve to improve our decompilation output.

#### Parameter Rejection

If youâve ever noticed an incorrect number of arguments or return values from a function call in Binary Ninja, the root cause is that the heuristic that tried to guess them wasnât correct. Of course, if you have accurate type information you can always improve the result by specifying the proper parameters and their types, but with this new improvement, that often wonât be required. Consider the following two examples.

In the first, you can see how previously on some arm/thumb PE API calls, the function itself was erroneously showing up as an argument but no longer does in 3.3.

![](/blog/images/3.3-release/pe_thumb-after.png)
![](/blog/images/3.3-release/pe_thumb-before.png)

In the second example we can see on this x64 Linux ELF that the locations where free is called now show the correct arguments, and no longer show erroneous return values (for a void function!). One of the important features in this improvement is that in instances where the heuristic analysis has to guess parameters it is far less likely to override an existing function type.

![](/blog/images/3.3-release/onewrite-after.png)
![](/blog/images/3.3-release/onewrite-before.png)

#### Improved Objective-C

Our first-class Objective-C support might have [landed](/2022/10/28/3.2-released.html#objective-c-support) in the last release, but weâve seen a number of major improvements since then.

Apple loves to constantly iterate on the Mach-O format since they implement all of the CPU, compiler, and tool-chain, so maintaining support for the latest platform requires us to keep chasing an ever-moving target. Two important features have been added for 3.3: support for chained fixups and proper handling of instance variables (ivars). First, âchained fixupsâ allow dynamically linked libraries to have chains of fixups that encode an offset plus an offset to the next fixup. The difference made by adding support is obvious on binaries that use this format:

![](/blog/images/3.3-release/chainedfixups-after.png)
![](/blog/images/3.3-release/chainedfixups-before.png)

The second addition to our Objective-C support is the [proper handling](https://github.com/Vector35/workflow_objc/commit/c86cf56a89fdab9ce88076f7211ba94693fc256d) of instance variables (ivars). This is mostly noticed when extracting type information for extracted structures:

![](/blog/images/3.3-release/ivars-after.png)
![](/blog/images/3.3-release/ivars-before.png)

And of course these arenât the only changes! Check out the full [commit history](https://github.com/Vector35/workflow_objc/commits/master) on the open-source Objective-C plugin for even more details about what else has improved.

#### Automatic Outlining

The actual full title for this feature is: [Automatic Un-inlining/Outlining of Compiler Builtin Functions](https://github.com/Vector35/binaryninja-api/issues/3742) â and even that was hotly contested internally! Whatever the name though, the feature is a major improvement to our overall decompilation and rendering of functions where common functions like memset, memcpy, and strcpy are frequently inlined by a compiler. But to really understand it, letâs turn it on and show what it does.

As it is an experimental feature, outlining needs to be enabled via a setting:

![Outlining Setting](/blog/images/3.3-release/outlining-setting.png)

Once enabled, youâll notice a new section called âsynthetic built-insâ at the very bottom of linear view:

![Synthetic Built-Ins](/blog/images/3.3-release/synthetic-builtins.png)

From there, just look for cross-references to those functions and you can see all the instances where the new feature was able to identify patterns that were replaced with these new synthetic functions for improved readability:

![Synthetic Xrefs](/blog/images/3.3-release/synthetic-xrefs.png)

Hereâs a quick comparison showing one of those regions of code before/after the setting was applied:

![](/blog/images/3.3-release/outlining-after.png)
![](/blog/images/3.3-release/outlining-before.png)

### Debugger

The new debugger is now out of beta!

![Native Debugger](/images/screenshots/debugger.png)

One of the biggest changes for this release is that weâre finally bringing our native debugger out of beta and into the stable product. This is a full replacement of the [legacy debugger plugin](https://binary.ninja/2020/05/06/debugger-showcase.html) we released over two and a half years ago. That older version was written in Python and had some significant limitations. Our *new* debugger has been entirely re-written in C++ and supports local and remote debugging on our three major platforms...