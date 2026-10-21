---
title: 6.0 Release 2
url: https://binary.ninja/2026/10/20/6.0-release-2.html
source: Binary Ninja
date: 2026-10-20
fetch_date: 2026-10-21T06:49:25.855803
---

# 6.0 Release 2

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

# 6.0 Release 2

By [Jordan Wiens](https://github.com/psifertex)
 2026-10-20

![Caped Binja flying over the city. >](/blog/images/6.0-release/krypton.jpg)

Weâre back with a small R2 update for those who only use our stable branch. This R2 improves on our [Krypton 6.0
release](https://binary.ninja/2026/09/03/binary-ninja-6.0-krypton.html) with crash fixes, hardening of the PE and ELF
loaders, Linux compatibility improvements, as well as bug-fixes for the MSP430 architecture, DWARF, Mach-O, Ghidra
Export, and the debugger.

As always, customers with [active support](https://binary.ninja/purchase/) on the [development
branch](https://docs.binary.ninja/guide/index.html#development-branch) have access to these changes and more.

## Core/Analysis

* **Fix**: Analysis getting stuck with endlessly increasing progress during phase 1 when processing RTTI ([#8017](https://github.com/Vector35/binaryninja-api/issues/8017))
* **Fix**: Crash in the GNU3 demangler on names containing non-ASCII characters, which could occur when loading kernel caches ([#8582](https://github.com/Vector35/binaryninja-api/issues/8582))

## File Formats

* **Fix**: Harden PE loader against malformed files
* **Fix**: Reject out-of-bounds ELF sections and header tables
* **Fix**: Skip malformed ELF section metadata instead of rejecting the entire file
* **Fix**: Multiple privately reported crashes when loading malformed files
* **Fix**: arm64e.x1 and other new Mach-O slice variants being mislabeled as arm64 ([#8571](https://github.com/Vector35/binaryninja-api/issues/8571))

## Architectures

* **Fix**: MSP430 `sub` lifting operands in reverse order ([#8503](https://github.com/Vector35/binaryninja-api/issues/8503))
* **Fix**: MSP430 conditional jumps emitting a spurious jump ([#8516](https://github.com/Vector35/binaryninja-api/issues/8516))
* **Fix**: MSP430 byte operations sign-extending into registers instead of zero-extending ([#8517](https://github.com/Vector35/binaryninja-api/issues/8517))

## DWARF

* **Fix**: DWARF import not loading all types ([#8552](https://github.com/Vector35/binaryninja-api/issues/8552))

## Ghidra Export

* **Fix**: Exporting functions with typedef return types fixed
* **Fix**: Certain user types not being included when exporting to Ghidra ([#8449](https://github.com/Vector35/binaryninja-api/issues/8449))

## Debugger

* **Fix**: Crash when recording a TTD trace by attaching to or launching a process in Binary Ninja Free ([#796](https://github.com/Vector35/debugger/issues/796))
* **Fix**: Crash when shutting down a Corellium session before the connection was established ([#1197](https://github.com/Vector35/debugger/issues/1197))

## UI/UX

* **Fix**: âReset window layoutâ always crashing ([#8527](https://github.com/Vector35/binaryninja-api/issues/8527))

## Platform Support

* **Fix**: Startup failures on Ubuntu 26.04 due to missing `libopengl0`/`libxcb`; Qt now uses libGL on Linux

## Documentation

* **Improvement**: Clarified Ultimate, Commercial, and Non-Commercial edition requirements ([#8574](https://github.com/Vector35/binaryninja-api/issues/8574))

These builds are now live on both our website and update servers. If youâre a Binary Ninja Free user, you can download a
new installer [here](https://binary.ninja/free). If youâre a Personal, Commercial, or Enterprise user, the new build is
available from the [portal](https://portal.binary.ninja/) or via a [license recovery
email](https://binary.ninja/recover). And as always, you can
[update](https://docs.binary.ninja/guide/index.html#updates) your existing client.

Tagged

* [announcements](/tag/announcements)
* [stable](/tag/stable)
* [debugger](/tag/debugger)

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

## Contact

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#90f2f9fef1e2e9fef9fefaf1d0e6f5f3e4ffe2a3a5bef3fffd)

+1-321-306-5535

[Join us on Slack](https://slack.binary.ninja/)

[Mailing List Sign-Up](https://41aup4.share-na2.hsforms.com/29wZPDRsySp-r6qz2-yAhQg)

## Resources

* [User Documentation](https://docs.binary.ninja/)
* [API Reference](https://api.binary.ninja/)
* [Support](/support/)
* [FAQ](/faq/)
* [Changelog](/changelog/)
* [Manage Licenses & Downloads](https://portal.binary.ninja/)

Â© 2015-2026 Vector 35. All rights reserved. Binary NinjaÂ® is a registered trademark of Vector 35.

[Software EULA](https://docs.binary.ninja/about/license.html)
[Privacy Policy](/privacy/)
[Service Status](https://status.binary.ninja/)