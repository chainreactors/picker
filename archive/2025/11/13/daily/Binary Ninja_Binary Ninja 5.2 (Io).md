---
title: Binary Ninja 5.2 (Io)
url: https://binary.ninja/2025/11/13/binary-ninja-5.2-io.html
source: Binary Ninja
date: 2025-11-13
fetch_date: 2025-11-14T03:12:40.353152
---

# Binary Ninja 5.2 (Io)

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

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## Binary Ninja 5.2 (Io)

* [Jordan Wiens](https://github.com/psifertex)
* 2025-11-13
* [announcements](/tag/announcements), [stable](/tag/stable)

![The release codename Io is inspired by the Expanse, though of course it's a real moon in many other sci-fi stories as well. >](/blog/images/5.2-release/io.png)

For the last few months, weâve been hard at work on todayâs release, Binary Ninja 5.2 (Io)! This release delivers some of our most impactful and highly requested features yet, including bitwise data-structure support (second most requested), container support (fifth most requested), full Hexagon architecture support for disassembly and decompilation, and much more. Under-the-hood, 5.2 also contains some other improvements that will help us chart a course toward even bigger improvements in the future.

Letâs dig in!

* [Free Candy](/2025/11/13/binary-ninja-5.2-io.html#free-candy)
* [Initial Bitfield Support](/2025/11/13/binary-ninja-5.2-io.html#initial-bitfield-support)
* [Container Support](/2025/11/13/binary-ninja-5.2-io.html#container-support)
* [Custom Strings / Constants](/2025/11/13/binary-ninja-5.2-io.html#custom-strings--constants)
* [Ghidra Import](/2025/11/13/binary-ninja-5.2-io.html#ghidra-import)
* [WARP Server](/2025/11/13/binary-ninja-5.2-io.html#warp-server)
  + [Downloading Signatures](/2025/11/13/binary-ninja-5.2-io.html#downloading-signatures)
  + [Pushing Signatures](/2025/11/13/binary-ninja-5.2-io.html#pushing-signatures)
  + [Enterprise](/2025/11/13/binary-ninja-5.2-io.html#enterprise)
  + [More](/2025/11/13/binary-ninja-5.2-io.html#more)
* [Hexagon](/2025/11/13/binary-ninja-5.2-io.html#hexagon)
* [Cross References](/2025/11/13/binary-ninja-5.2-io.html#cross-references)
* [TTD Queries and Analysis](/2025/11/13/binary-ninja-5.2-io.html#ttd-queries-and-analysis)
  + [TTD Calls Widget](/2025/11/13/binary-ninja-5.2-io.html#ttd-calls-widget)
  + [TTD Memory Widget](/2025/11/13/binary-ninja-5.2-io.html#ttd-memory-widget)
  + [TTD Events Widget](/2025/11/13/binary-ninja-5.2-io.html#ttd-events-widget)
  + [TTD Analysis](/2025/11/13/binary-ninja-5.2-io.html#ttd-analysis)
  + [Python API for TTD](/2025/11/13/binary-ninja-5.2-io.html#python-api-for-ttd)
* [Objective-C](/2025/11/13/binary-ninja-5.2-io.html#objective-c)
* [Open-Source Contributions](/2025/11/13/binary-ninja-5.2-io.html#open-source-contributions)
* [Everything Else](/2025/11/13/binary-ninja-5.2-io.html#everything-else)

# Major Features

[![Free Candy >](/blog/images/5.2-release/free-candy.png)](/blog/images/5.2-release/free-candy.png)

## Free Candy

Well, not *quite* free candy, but it might seem like it if youâre a user of the [Free edition](https://binary.ninja/free/) of Binary Ninja! In 5.2, weâre adding many new features from the paid versions to Free:

* [Objective-C workflow](https://github.com/Vector35/binaryninja-api/tree/dev/plugins/workflow_objc)
* [WARP plugin](https://binary.ninja/2025/08/22/warp.html)
* [DWARF Import](https://github.com/Vector35/binaryninja-api/tree/dev/plugins/dwarf/dwarf_import)
* and [TTD support](https://docs.binary.ninja/guide/debugger/dbgeng-ttd.html)!

## Initial Bitfield Support

New in Binary Ninja 5.2, there is [support for bitwise structure members](https://github.com/Vector35/binaryninja-api/issues/694), commonly referred to as bitfields. Structure members can now be represented with a given bit position and bit width, and Linear View will render the fields properly:

[![Bitfield Support](/blog/images/5.2-release/bitfield.png)](/blog/images/5.2-release/bitfield.png)

Currently, we use bitfield information when rendering structures in the data renderer, as shown above. The included [debug info plugins](https://docs.binary.ninja/guide/types/debuginfo.html) (e.g. DWARF, PDB) have been updated to express bitfields alongside other plugins like the built-in [SVD import](https://github.com/Vector35/binaryninja-api/tree/dev/plugins/svd), where MMIO peripherals make heavy use of bitfields.

In a future release, we will [extend our analysis](https://github.com/Vector35/binaryninja-api/issues/7533) to resolve common access patterns for bitfields in Medium and High Level IL.

## Container Support

One of our most-requested features is finally here: full container support. With the introduction of [Container Transforms](https://docs.binary.ninja/dev/containertransforms.html), Binary Ninja can now seamlessly handle nested formats like ZIP, IMG4, or CaRT directly in-memory â no manual extraction required.

At its core, container support lets you browse inside archives and automatically follow transformation layers to reach the data you care about. When a container resolves to a single target, Binary Ninja can transparently open it for analysis. Combined with the [files.container.defaultPasswords](https://docs.binary.ninja/guide/settings.html#files.container.defaultPasswords) setting, this makes it effortless to open password-protected samples or malware archives safely â everything happens in memory, so nothing ever touches disk, and you can create an analysis database immediately.

When there are multiple payloads, the new Container Browser lets you explore and choose exactly which one to load:

[![Container Browser](/blog/images/5.2-release/container-browser.png)](/blog/images/5.2-release/container-browser.png)

You can easily extend this functionality since it leverages the [Transform API](https://api.binary.ninja/binaryninja.transform-module.html). A complete [ZipInfo example](https://github.com/Vector35/binaryninja-api/blob/36d99ad88aed9889c741f34bddd045405a68369b/python/transform.py#L822) is included with the API, so you can add support for whatever container formats you need.

## Custom Strings / Constants

Want to add your own custom string deobfuscator that can be automatically applied merely by adding a type? How about support for custom string formats for a new language? Hereâs some of the changes we made in this release to support it:

* Custom String Rendering: These new APIs allow for custom callbacks, enabling strings to be rendered with different logic than just standard C-style strings.
* Type Attributes: These are useful for annotating which strings to use a custom renderer on in a file that has a mix of obfuscated strings and regular C-style strings.
* Better type-propagation: For the example plugin below, we had to add some additional type propagation features that would automatically propagate the types (including attributes).
* Custom Constant Rendering: The constant renderer system makes similar changes to strings as the custom string rendering but applied to constants. For example, consider automatically converting constants passed to a library hashing function into their string representations.

Weâll show off more details in an upcoming blog post, but here are a few examples to whet your appetite. First, we asked one of our favorite YouTubers and malware analysis trainers, Josh Reynolds from [InvokeRE](https://invokere.com/), for a good sample that uses a custom string obfuscation implementation. He suggested a recent Amadey variant([1](https://www.virustotal.com/gui/file/4cfd8b1592254d745d8f654...