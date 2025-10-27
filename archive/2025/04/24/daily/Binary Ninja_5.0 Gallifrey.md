---
title: 5.0 Gallifrey
url: https://binary.ninja/2025/04/23/5.0-gallifrey.html
source: Binary Ninja
date: 2025-04-24
fetch_date: 2025-10-06T22:05:15.709254
---

# 5.0 Gallifrey

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

## 5.0 Gallifrey

* [Jordan Wiens](https://github.com/psifertex)
* 2025-04-23
* [announcements](/tag/announcements), [stable](/tag/stable)

![Council of Time Lords style drawing with the Binary Ninja team instead of Doctor Who characters >](/blog/images/5.0-release/gallifrey.png)

Not enough time to reverse engineer everything you want? The Time Lords are here to help in Binary Ninja 5.0 Gallifrey! With major features across the board from huge analysis improvements, fantastic iOS support, many new firmware-specific features, and more, this major version has something for everyone.

* [iOS](/2025/04/23/5.0-gallifrey.html#ios)
  + [DYLD Shared Cache](/2025/04/23/5.0-gallifrey.html#dyld-shared-cache)
  + [Kernel Cache](/2025/04/23/5.0-gallifrey.html#kernel-cache)
* [Firmware](/2025/04/23/5.0-gallifrey.html#firmware)
  + [Firmware Ninja (Ultimate Only)](/2025/04/23/5.0-gallifrey.html#firmware-ninja-ultimate-only)
  + [IHEX/TI-TXT/SREC Loader](/2025/04/23/5.0-gallifrey.html#ihextitxtsrec-loader-all-paid-editions)
  + [SVD Loader](/2025/04/23/5.0-gallifrey.html#svd-loader-all-editions)
* [Analysis](/2025/04/23/5.0-gallifrey.html#analysis)
  + [Array and Structure Detection and Propagation](/2025/04/23/5.0-gallifrey.html#array-and-structure-detection-and-propagation)
  + [Union Type Support](/2025/04/23/5.0-gallifrey.html#union-type-support)
  + [Itanium RTTI](/2025/04/23/5.0-gallifrey.html#itanium-rtti)
* [Debugger](/2025/04/23/5.0-gallifrey.html#debugger)
* [Shellcode Compiler Open Sourced](/2025/04/23/5.0-gallifrey.html#shellcode-compiler-open-sourced)
* [New Architectures](/2025/04/23/5.0-gallifrey.html#new-architectures)
* [Enterprise Browser Improvements](/2025/04/23/5.0-gallifrey.html#enterprise-browser-improvements)
* [Other Notables](/2025/04/23/5.0-gallifrey.html#other-notables)
  + [Updated URL Handler](/2025/04/23/5.0-gallifrey.html#updated-url-handler)
  + [Line Wrapping](/2025/04/23/5.0-gallifrey.html#line-wrapping)
  + [Render Layers](/2025/04/23/5.0-gallifrey.html#render-layer)
  + [Customer Portal](/2025/04/23/5.0-gallifrey.html#customer-portal)
* [Open Source Contributions](/2025/04/23/5.0-gallifrey.html#open-source-contributions)
* [Everything Else](/2025/04/23/5.0-gallifrey.html#everything-else)

With all these improvements, 5.0 is our most effective release yet. If youâve been waiting for the right time to upgrade your reversing toolkit, this is it. Try it for [free](https://binary.ninja/free/) or [get your license](https://binary.ninja/purchase/) today!

## iOS

Better support for reverse engineering iOS has been a major focus of the 5.0 release. Between major improvements to DYLD Shared Cache integration, architecture/lifting fixes, and the new Kernel Shared Cache support, Binary Ninja 5.0 is a great choice for all your iOS reverse engineering needs.

### DYLD Shared Cache

Thanks to the efforts of both the team at Vector 35 and a number of [incredibly helpful](https://github.com/Vector35/binaryninja-api/issues?q=is%3Apr%20state%3Aclosed%20%5BSharedCache%5D) community members, the DYLD Shared Cache integration has seen some major improvements. Weâre pleased that, after all this work, DYLD Shared Cache support is no longer considered in an alpha state, but is now a first-class feature!

The most noticeable improvement is the performance. On hardware that previously took four and a half minutes to do initial analysis in Binary Ninja 4.2, it now only takes fifteen seconds in 5.0!

* The UI has been improved
  + The image and symbols lists can be sorted
  + You can select âLoad Selected Image and Dependenciesâ from the context menu in the Images tab, and skip manually walking dependency trees
  + DYLD Shared Caches can now be loaded from a Project
* Analysis has been improved
  + iOS 16 Symbol Cache files are now processed and many more symbol names are now displayed
  + Objective-C support is better, with more `objc_msgSend` calls being processed
  + Symbol names are demangled with LLVM
  + Pointers to not-yet-loaded regions are resolved automatically now
* Stability has been improved with a substantial rewrite of the model logic
* [The documentation](https://docs.binary.ninja/guide/sharedcache.html?h=dyld#opening-a-shared-cache) was given a refresh.

* Images
* Symbols
* Mappings and Regions

![Dyld Shared Cache Triage Images](/blog/images/5.0-release/dsc-images.png)

![Dyld Shared Cache Triage Symbols](/blog/images/5.0-release/dsc-symbols.png)

![Dyld Shared Cache Mappings and Regions](/blog/images/5.0-release/dsc-mappings-and-regions.png)

### Kernel Cache

New to Binary Ninja 5.0 is support for the Kernel Cache from iOS and macOS. While newer than the DYLD Shared Cache support, this capability is also [open source](https://github.com/Vector35/binaryninja-api/tree/dev/view/kernelcache) and quickly improving. [Similar features](https://docs.binary.ninja/guide/kernelcache.html) enable you to choose images to load into a shared virtual memory space for cross-image analysis. Named `KSCView` in the UI, the Kernel Cache view supports both image loading and symbol lookup.

* Images
* Symbols

![Dyld Shared Cache Triage Images](/blog/images/5.0-release/ksc-images.png)

![Dyld Shared Cache Triage Symbols](/blog/images/5.0-release/ksc-symbols.png)

## Firmware

There are many improvements in this release for those doing firmware analysis. These include Firmware Ninja (available only in the Ultimate edition), the text format loaders (available in all paid editions), and SVD file loading (available in all editions).

### Firmware Ninja (Ultimate Only)

[![Firmware Ninja](/blog/images/firmwareninja/firmwareninja-overview.png)](/blog/images/firmwareninja/firmwareninja-overview.png)

Firmware Ninja includes a number of features designed specifically to enhance analysis of firmware. We recently wrote up a [detailed blog post](https://binary.ninja/2025/04/02/firmware-ninja.html) covering these features, but here is a quick summary:

* Entropy based analysis for segments/sections
* Memory insights for identifying patterns unique to firmware, such as loads/stores to external memory, MMIO usage, and others
* A board description database with built-in support for over 1000 microprocessor memory maps, including automatic detection/matching based on memory accesses from memory insights
* Relationship mapping that uses the Project API to automatically associate related endpoints between different binaries (for example, an I2C bus send function in one binary and the receive function in another)

### IHEX/TI-TXT/SREC Loader (All paid editions)

[![Hex File Loader](/blog/images/5.0-release/dothex.png)](/blog/images/5.0-release/dothex.png)

Previously a plugin, weâve re-implemented and integrated support for these various text-encodings commonly seen when dealing with firmware. You should be able to automatically open them and analyze their contents just like any other binary.

In the above screenshot, you can see how loading a `.hex` file is not only handled, but Binary Ninja also correctly identified the architecture using its automatic architecture prediction!

### SVD Loader (All editions)

Yet another open source ð¦ plugin, a [loader for SVD files](http...