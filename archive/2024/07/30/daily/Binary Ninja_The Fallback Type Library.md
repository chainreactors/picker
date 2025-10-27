---
title: The Fallback Type Library
url: https://binary.ninja/2024/07/29/fallback-typelib.html
source: Binary Ninja
date: 2024-07-30
fetch_date: 2025-10-06T17:42:29.792060
---

# The Fallback Type Library

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

## The Fallback Type Library

* [Zichuan Li](https://github.com/river-li)
* 2024-07-29
* [reversing](/tag/reversing), [meta](/tag/meta)

New in version 4.1, Binary Ninja now has a fallback type library for libc-like libraries. We showed it briefly in the [Binary Ninja 4.1 Feature Stream](https://www.youtube.com/watch?v=IdNFMIQ9roQ&t=3537s) and also showed one screenshot in our [4.1 announcement blog](https://binary.ninja/2024/07/17/4.1-elysium.html#fallback-libc) post.

This post will go into more detail as to what it is, how it works, and how it makes your reverse engineering experience better.

## Type Library Recap

Before looking into the fallback type library, letâs do a quick summary of how types are applied in Binary Ninja.

Binary Ninja provides [type libraries](https://docs.binary.ninja/guide/types/typelibraries.html) and [type archives](https://docs.binary.ninja/guide/types/typearchives.html). Type libraries are intended to help analyze imported functions, which will be introduced to the binary view when the target binary depends on a library that matches the type libraryâs name (or `alternate_name`).

Letâs create a simple type library.

```
tl = TypeLibrary.new(Architecture['x86_64'], "libc-test.so")
tl.add_alternate_name('libc.so')
tl.add_alternate_name('libc.so.6')
```

Note that using the Python console to do the above isnât available in the [free](https://binary.ninja/free) versions, but all of our [paid](https://binary.ninja/purchase) licenses support the interactive repl.

The type library above will match on `libc.so`, `libc.so.6`, and `libc-test.so`.

To learn how to create a type library see the [documentation](https://docs.binary.ninja/guide/types/typelibraries.html) and check our [example](https://github.com/Vector35/binaryninja-api/blob/dev/python/examples/typelib_create.py).

Included with the program download, we provide several type libraries for different architectures and platforms. They will be applied automatically and you can also put your own type libraries into your [user folder](https://docs.binary.ninja/guide/index.html#user-folder).

## Why Fallback?

So whatâs a fallback type library and why does it exist?

Honestly, there are still some platforms/architectures where our existing type libraries do not exist or may not be correctly applied. Although in most cases our heuristic analysis is good enough to identify parameters and some types, it is always better to have types for function signatures even if theyâre generic compared to an exact type library for a specific architecture.

Here are two cases where our previous type system fails:

### Libc Doesnât Match the alternate name

You may have noticed that the typelib must have a matched alternate name. What if the binary depends on a libc with an unusual name?

Unfortunately, it happens. For example, our `armv7` libc typelib matches `libc.so` or `libc.so.6`, which are commonly used. But in the following case, the binary depends on `libc.so.0`, which is a uClibc library. As a result, the existing type library wonât be loaded into the binary view, and functions like `scanf` and `malloc` wonât have types.

```
>>> bv.platform.type_libraries[-2]
<typelib 'libc_armv7.so.6':armv7>
>>> bv.platform.type_libraries[-2].alternate_names
['libc.so', 'libc.so.6']
>>> bv.libraries
['libdl.so.0', 'libpthread.so.0', 'libcrypto.so.1.0.0', 'libc.so.0']
```

### New Platforms

Recently, we added several new architectures: [RISC-V](https://binary.ninja/2024/02/28/4.0-dorsai.html#new-architecture-risc-v), [nanoMIPS](https://binary.ninja/2024/04/24/introducing-nanomips.html#nanomips-and-the-architecture-plugin), and [Tricore](https://www.youtube.com/watch?v=IdNFMIQ9roQ&t=3920s).

Platforms on these architectures donât yet have libc type libraries. The fallback type library can be used as a temporary solution in that situation.

Similarly, the fallback type library should be helpful when you are working on a custom platform/architecture and donât want to make your own type libraries.

## How Fallback Types Work

To solve such cases, starting in version 4.1, we have added a fallback type library. This fallback type library is created at runtime (during platform initialization) and will be introduced into the binary view when:

1. The binary depends on a *âlibc-likeâ* library.
2. We donât find a matching type library for this platform.
3. The platform enables the fallback type library.

Examples are always better than an explanation. Check the following examples:

On a RISC-V ELF:

![](/blog/images/fallback/riscv_4.1.png)
![](/blog/images/fallback/riscv_stable.png)

On a binary depending on `libc.so.0`:

![](/blog/images/fallback/armv7_4.1.png)
![](/blog/images/fallback/armv7_stable.png)

## Try it now!

The fallback type library is available on both dev and the 4.1 stable. Enjoy your reverse engineering with Binary Ninja!

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#73111a1d12010a1d1a1d191233051610071c0140465d101c1e)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)