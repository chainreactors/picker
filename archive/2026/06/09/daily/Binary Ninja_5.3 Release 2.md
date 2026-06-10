---
title: 5.3 Release 2
url: https://binary.ninja/2026/06/09/5.3-release-2.html
source: Binary Ninja
date: 2026-06-09
fetch_date: 2026-06-10T06:15:33.743576
---

# 5.3 Release 2

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

## 5.3 Release 2

* [Jordan Wiens](https://github.com/psifertex)
* 2026-06-09
* [announcements](/tag/announcements), [stable](/tag/stable), [debugger](/tag/debugger)

![Binjas, assemble! >](/blog/images/5.3-release/jotunheim.jpg)

Today weâre releasing a new âR2â for [Jotunheim](https://binary.ninja/2026/04/13/binary-ninja-5.3-jotunheim.html). This second stable release of 5.3 primarily contains stability fixes with a heavy emphasis on crashes and hangs (in part thanks to our new [Sentry](https://binary.ninja/2026/04/13/binary-ninja-5.3-jotunheim.html#crash-reporting) infrastructure). This release should result in a much more stable reverse engineering experience.

As always, customers with [active support](https://binary.ninja/purchase/) on the [development branch](https://docs.binary.ninja/guide/index.html#development-branch) have access to these changes and more.

## BinaryView Fixes

* Multiple fixes for crashes loading malformed Mach-O binaries and binaries with malformed Objective-C metadata
* Fixed a hang when loading an ELF MIPS binary containing a corrupt symbol table
* Fixed long analysis stalls on malformed size claims in C++ RTTI data
* Fixed malformed PE exception directory causing large allocations / hangs
* Fixed a memory leak from VxWorks view loading (Ultimate only) ([#8075](https://github.com/Vector35/binaryninja-api/issues/8075))

## Analysis and Architectures

* Multiple Thumb-2 lifting fixes including an out-of-bounds read during lifting, and incorrect handling of IT (conditional) instructions
* Fixed an out-of-bounds read when lifting certain Rust binaries ([#8155](https://github.com/Vector35/binaryninja-api/issues/8155))
* Fixed a crash from unbounded recursion when two functions that call each other are both marked âinline during analysisâ
* Fixed crashes when no default calling convention is registered for a platform (resulted in both PDB and WARP crashes) ([#8196](https://github.com/Vector35/binaryninja-api/issues/8196), [#8181](https://github.com/Vector35/binaryninja-api/issues/8181))

## Stability: Races and Lifetimes

* Multiple fixes for crashes when a binary view is closed or removed while still in use
* Fixed a race condition on Windows x64 binaries during view initialization
* Fixed a WARP crash when its sidebar was deleted just as analysis completed

## UI and Platform

* Fixed a crash rendering very long symbol names when the maximum symbol width setting is smaller than the symbol being truncated
* Fixed an abort when checking file paths the OS denies access to (e.g. permission errors while reading the keybindings file)
* Fixed a UI crash when a structureâs base type or a member type canât be resolved from a named type reference
* Fixed keybindings not saving in the free version on macOS ([#7253](https://github.com/Vector35/binaryninja-api/issues/7253))

## Debugger

The debugger received its own batch of 20 stabilization commits in this release. Apologies to those impacted by these issues:

* Multiple crash fixes in debug adapters when a connection is unavailable or drops mid-operation ([#1073](https://github.com/Vector35/debugger/issues/1073), [#1076](https://github.com/Vector35/debugger/issues/1076), [#1077](https://github.com/Vector35/debugger/issues/1077), [#1078](https://github.com/Vector35/debugger/issues/1078))
* Multiple object-lifetime and threading fixes ([#1047](https://github.com/Vector35/debugger/issues/1047), [#1048](https://github.com/Vector35/debugger/issues/1048), [#1058](https://github.com/Vector35/debugger/issues/1058), [#1062](https://github.com/Vector35/debugger/issues/1062), [#1080](https://github.com/Vector35/debugger/issues/1080), [#1086](https://github.com/Vector35/debugger/issues/1086))
* Fixed a deadlock and repeated resume-event spam with conditional breakpoints ([#1051](https://github.com/Vector35/debugger/issues/1051))
* Fixed the native Windows adapter being unusable after detaching from a target ([#1050](https://github.com/Vector35/debugger/issues/1050))
* Multiple error-handling improvements so failures while reading debuggee memory or communicating with remote targets are logged instead of crashing or being silently dropped ([#1046](https://github.com/Vector35/debugger/issues/1046), [#1079](https://github.com/Vector35/debugger/issues/1079), [#1081](https://github.com/Vector35/debugger/issues/1081))
* UI fixes: time-travel debugging widgets no longer appear for targets that donât support it, and the debugger sidebar no longer steals focus every time the target stops ([#1033](https://github.com/Vector35/debugger/issues/1033), [#1055](https://github.com/Vector35/debugger/issues/1055))

These builds are now live on both our website and update servers. If youâre a Binary Ninja Free user, you can download a
new installer [here](https://binary.ninja/free). If youâre a Personal, Commercial, or Enterprise user, the new build is
available from the [portal](https://portal.binary.ninja/) or via a [license recovery
email](https://binary.ninja/recover). And as always, you can
[update](https://docs.binary.ninja/guide/index.html#updates) your existing client.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2026 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#67050e0906151e090e090d062711020413081554524904080a)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)

[Service Status](https://status.binary.ninja/)