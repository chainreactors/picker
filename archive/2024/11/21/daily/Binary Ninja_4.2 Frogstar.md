---
title: 4.2 Frogstar
url: https://binary.ninja/2024/11/20/4.2-frogstar.html
source: Binary Ninja
date: 2024-11-21
fetch_date: 2025-10-06T19:15:25.284001
---

# 4.2 Frogstar

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

## 4.2 Frogstar

* [Jordan Wiens](https://github.com/psifertex)
* 2024-11-20
* [announcements](/tag/announcements), [stable](/tag/stable)

![Dont Panic Text With Binary Ninja Mascot Holding a Towel >](/blog/images/4.2-release/frogstar.png)

Donât panic! Binary Ninja version 4.2 Frogstar is here. It is, after all, [the answer](https://en.wikipedia.org/wiki/42_%28number%29#The_Hitchhiker's_Guide_to_the_Galaxy) to everything. Much like a trusty towel, youâll find that the improvements in 4.2 are applicable to many situations. This major release (despite the number increment being minor since we couldnât skip version 4.2) includes an industry-first multiple-language decompilation, DYLD Shared Cache analysis, MSVC RTTI support, a new signature system fittingly called WARP, and so many more features.

* [Language Representations](/2024/11/20/4.2-frogstar.html#language-representations)
* [MSVC RTTI](/2024/11/20/4.2-frogstar.html#msvc-run-time-type-information-rtti-extraction)
* [WARP Signature Matching](/2024/11/20/4.2-frogstar.html#warp-advanced-function-matching-algorithm-alpha)
* [DYLD Shared Cache Alpha](/2024/11/20/4.2-frogstar.html#dyld-shared-cache-alpha)
* [Workflows Feature Update](/2024/11/20/4.2-frogstar.html#workflows-feature-update)
* [Ultimate Edition](/2024/11/20/4.2-frogstar.html#ultimate-edition)
* [New Architecture](/2024/11/20/4.2-frogstar.html#new-architecture)
* [Smaller But Notable](/2024/11/20/4.2-frogstar.html#smaller-but-notable)
  + [Code Folding](/2024/11/20/4.2-frogstar.html#code-folding)
  + [Forward Type Propagation](/2024/11/20/4.2-frogstar.html#forward-type-propagation)
  + [Smart Undefine](/2024/11/20/4.2-frogstar.html#smart-undefine)
  + [Plugin Status](/2024/11/20/4.2-frogstar.html#plugin-status)
* [Open Source Contributions](/2024/11/20/4.2-frogstar.html#open-source-contributions)
* [Other Updates](/2024/11/20/4.2-frogstar.html#other-updates)

# Major Features

## Language Representations

One of Vector 35âs long-standing goals has been to break people away from the assumption that âCâ is the ultimate output of a decompiler. That is one reason why [HLIL](https://docs.binary.ninja/dev/bnil-hlil.html) is our default view, even though we offer Pseudo C output. Now, in Binary Ninja 4.2, we are taking this one step further. We are adding a brand new, unique capability to Binary Ninja: the ability to decompile to other target languages.

This new Language Representation system is designed to allow custom renderings of HLIL that are language-specific. Using this system, we are adding [Pseudo Rust](https://github.com/Vector35/binaryninja-api/tree/dev/lang/rust), which displays decompiled code in a style similar to the popular language Rust. The best part of this feature is that it is fully pluggable and user-customizable, with both a comprehensive API available and fully-featured example plugins for you to explore. In addition to both the [Pseudo C](https://github.com/Vector35/binaryninja-api/tree/dev/lang/c) and [Pseudo Rust](https://github.com/Vector35/binaryninja-api/tree/dev/lang/rust) representations being released as open source C++ plugins, we are also releasing a [Pseudo Python](https://github.com/Vector35/binaryninja-api/blob/dev/python/examples/pseudo_python.py) example, written in Python, to demonstrate how to use this new system in Python plugins.

Not only does this add to the groundwork for new language-specific decompilation, but it also is a dramatic improvement in the quality of our Pseudo C output. Instead of a one-off implementation, itâs now much more robust so users who prefer Pseudo C as their default should see a noticeable increase in quality.

* Pseudo C
* Pseudo Rust
* Pseudo Python

![Pseudo C](/blog/images/4.2-release/pseudo-c.png)

![Pseudo Rust](/blog/images/4.2-release/pseudo-rust.png)

![Pseudo Python](/blog/images/4.2-release/pseudo-python.png)

Note that (for now) the Pseudo Rust is only available in paid editions of Binary Ninja by default. Pseudo Python is a [separate example plugin](https://github.com/Vector35/binaryninja-api/blob/dev/python/examples/pseudo_python.py) that can be installed by copying it to your [user plugin folder](https://docs.binary.ninja/guide/index.html#user-folder). You can however check out <https://cloud.binary.ninja/> which does have the Pseudo Rust view as well!

## MSVC Run-Time Type Information (RTTI) Extraction

Most C++ binaries contain a significant amount of information about their types, as it is necessary when using the object-oriented features of the language. Now, in C++ binaries compiled using MSVC, Binary Ninja will automatically extract this type information and apply it for you. It will discover Virtual Function Tables, creating structures for them in your analysis, and making data variables with those structures where they are found. For classes with multiple inheritance, multiple Virtual Function Tables are supported and will be created accordingly. This update specifically adds support for extracting RTTI from x86 and x64 PE files compiled with MSVC. In future updates, we plan to expand this functionality to include [Itanium RTTI](https://github.com/Vector35/binaryninja-api/issues/3857) support.

[![RTTI](/blog/images/4.2-release/rtti.png)](/blog/images/4.2-release/rtti.png)

## WARP: Advanced Function Matching Algorithm Alpha

This release features a new way to transfer function information between binaries. Unlike our existing SigKit tool, WARP is meant for whole function matching. This means fewer false positives and more opportunities to match on smaller functions, thanks to WARPâs function constraints. WARP integration is *currently in alpha,* and is disabled by default. If you would like to try it, you can **enable** `analysis.warp` in your settings. For more information about WARP, visit the documentation [here](https://docs.binary.ninja/dev/annotation.html?h=warp#warp-signature-libraries)!

[![WARP applying calling convention and type info](/blog/images/4.2-release/warp.png)](/blog/images/4.2-release/warp.png)

![](/blog/images/4.2-release/warp-after.png)
![](/blog/images/4.2-release/warp-before.png)

## DYLD Shared Cache Alpha

For those iOS researchers who have been waiting for our new dyld shared cache (DSC) support, thanks for your patience! Weâre extremely happy to announce that Binary Ninja 4.2 contains an alpha preview of our DSC support. The current release contains full support for iOS 11-17 shared cache bundles and partial support for iOS 18 and all macOS caches. Like many of our custom views, the implementation is [open source](https://github.com/Vector35/binaryninja-api/tree/dev/view/sharedcache) and feedback is welcome.

Our DSC loader lets you select images from the shared cache to load into the analysis space and will automatically link loaded images. You can search either by image in the `Images` tab or you can search by a symbol to cause the image that contains it to be loaded.

[![Dyld Shared Cache Triage View](/blog/images/4.2-release/dsc.png)](/blog/images/4.2-release/dsc.png)

## Workflows Feature Update

Weâre excited to announce major updates to the **Workflows Feature** in version 4.2. These enhancements brin...