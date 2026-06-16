---
title: Inside iOS 27's Reworked Stub Islands
url: https://codecolor.ist/posts/2026-06-15-ios27-reworked-stub-islands/
source: CodeColorist
date: 2026-06-15
fetch_date: 2026-06-16T07:15:00.142266
---

# Inside iOS 27's Reworked Stub Islands

[CodeColorist](/)[Blog](/blog/)[Talks](/talks/)[About](/about/)

![Inside iOS 27's Reworked Stub Islands](/img/2026-06-15-ios27-reworked-stub-islands/ios27.webp)

June 15, 2026

# Inside iOS 27's Reworked Stub Islands

At WWDC 2026, Apple announced iOS 27 with performance improvements, but of course the keynote didn't cover much of the implementation details.
Below are a few observations from the disassembly — some may relate to those performance boosts, some may not.
*This article only focuses on aarch64 implementations.*

## How Stubs Worked Before iOS 27

In the dyld\_shared\_cache, external symbols—whether functions or data references from other libraries—are pre-bound
during cache optimization. Pointers to other libraries become rebase operations (or relative offsets)
because the precise distances between libraries are known and fixed.

A typical example of how dyld resolves dynamic symbol references in standalone binaries outside of the dyld\_shared\_cache:

```
__text:

BL              _os_unfair_lock_unlock ; __auth_stubs
```

```
__auth_stubs: _os_unfair_lock_unlock

ADRL            X17, _os_unfair_lock_unlock_ptr
LDR             X16, [X17] ; load from GOT entry
BRAA            X16, X17 ; jump to the resolved function
```

Where `_os_unfair_lock_unlock_ptr` is an entry in `__auth_got`. The linker (dyld) will bind (and sign) the pointer to the actual implementation (`__imp__os_unfair_lock_unlock`) and store it in `__auth_got`.

```
_os_unfair_lock_unlock_ptr DCQ __imp__os_unfair_lock_unlock
```

In dyld\_shared\_cache, most of `__auth_stubs` and `__auth_got` are aggregated into stub island pages, which don't belong to any specific binary.

There is still a per-binary `__auth_stubs` section in the dyld\_shared\_cache, however most of the time you won't find the actual cross-references to them, because the branch instructions are replaced to point to the stub island pages.

iOS still makes heavy use of Objective-C, so there is first-class support for method calls (message dispatch).

Most Objective-C method calls are compiled into a branch instruction that points to stubs in a dedicated section `__objc_stubs`:

```
__objc_stubs: _objc_msgSend$URLByAppendingPathComponent_
ADRP            X1, #selRef_URLByAppendingPathComponent_@PAGE ; load from __objc_selrefs
LDR             X1, [X1,#selRef_URLByAppendingPathComponent_@PAGEOFF] ; load selector
ADRL            X17, _objc_msgSend_ptr ; GOT entry
LDR             X16, [X17] ; load _objc_msgSend
BRAA            X16, X17 ; dispatch message
```

## What iOS 27 Changes

### Redundant sections are gone

As mentioned, after dyld cache optimization, branch instructions to `__objc_stubs` are updated to jump to stub island pages, while the unused sections remain in each binary.

On iOS 27 beta, those sections are removed; only the stub island pages in the dyld\_shared\_cache remain.

Some other sections related to Objective-C are also removed from source binaries, such as `__objc_methname`, `__objc_methtype` and `__objc_classname`. Now the data references (selectors, method types, class names) point to the `__OBJC_RO` region.

It's worth noting that a while ago, the schema of `__objc2_meth_list` changed.

`__objc2_meth_list` contains a list of method information for Objective-C methods, including each method's selector, type encoding, and implementation pointer. The selector field used to be an offset from the field itself. Then the dyld\_shared\_cache optimizer changed the semantics to use a global base address for selector offsets, which can be found through the cache header:

```
struct dyld_cache_header {
    // other fields omitted
    uint64_t    objcOptsOffset;         // VM offset from cache_header* to ObjC optimizations header
    uint64_t    objcOptsSize;           // size of ObjC optimizations header
};
```

This pair points to the `ObjCOptimizationHeader` struct:

[dyld/common
/DyldSharedCache.h#L89](https://github.com/apple-oss-distributions/dyld/blob/e9da5ae571b4191dcdbcfd827363f19847c84561/common/DyldSharedCache.h#L89)

```
struct VIS_HIDDEN ObjCOptimizationHeader
{
    uint32_t version;
    uint32_t flags;
    uint64_t headerInfoROCacheOffset;
    uint64_t headerInfoRWCacheOffset;
    uint64_t selectorHashTableCacheOffset;
    uint64_t classHashTableCacheOffset;
    uint64_t protocolHashTableCacheOffset;
    uint64_t relativeMethodSelectorBaseAddressOffset;

    // Added in version 2
    uint64_t relativeMethodSelectorBufferSize;
    uint64_t relativeMethodTypesBufferSize; // this buffer starts at the end of the selectors buffer
};
```

So on iOS 26, to get the selector string, you need to add the selector offset
to `relativeMethodSelectorBaseAddressOffset`, instead of to the address of that field itself. 🤯

In version 2 of the Objective-C optimizations, dyld also applies this same offset
schema to method type encoding strings.

### Rethinking the stub trampolines

We've mentioned two types of stubs: one for cross-module symbols and one for Objective-C method calls.

On iOS 27, the old `__auth_stubs` style — `ADRL` and `LDR` to load a function pointer
from the GOT, then `BRAA` to branch with pointer authentication — still exists. But there are two new variants.

The first has no memory load nor pointer authentication:

```
_stubs: _open
ADRL            X16, _open
BR              X16
```

Then here comes an interesting pattern:

```
ADR             X16, 0x188060060
MOV             X17, #0x9B7
ADD             X16, X16, X17, LSL #21
BR              X16
```

If you have no clue what it is supposed to do, try simulating the arithmetic instructions.

```
> X16 = 0x188060060 + (0x9B7 << 21)
      = 0x188060060 + 0x136E00000
      = 0x2BEE60060
```

In this example, `0x2BEE60060` is the address of `libsystem_m.dylib!_acosl`.

So the first one can reach ±4 GiB from the stub: the `ADRP` gives a page-granular displacement of ±4 GiB,
and then `ADD` fills in the byte offset within that 4 KiB page.

The second variant exists for things that live further than that. Notice that our example target,
`0x2BEE60060`, sits `0x136E00000` ≈ 4.857 GiB away from the stub — already past what a single `ADRL` can encode.

In the instruction `ADD X16, X16, X17, LSL #21`, `imm16 << 21` is a multiple of 2 MiB, ranging up to `0xFFFF << 21` ≈ 128 GiB.
Note that this displacement is unsigned, so the range is forward-biased, unlike `ADRL`, which can also reach backward.

The motivation behind this pattern is easy to guess: performance.

This new arithmetic way to encode large offsets eliminates the memory load and pointer authentication overhead.

### Objective-C trampolines

The Objective-C trampolines now look like this:

```
ADRL            X1, sel_length
B               _objc_msgSend ; /usr/lib/objc/libobjcMsgSend.dylib
```

It's shorter than the previous load-and-branch pair. But wait a second.
This branch instruction can only reach ±128 MB from the current PC.
The dyld\_shared\_cache is several gigabytes — how can it handle all frameworks?

Write a parser to dump the image list from the cache, and we'll see the answer:

* /usr/lib/objc/libobjcMsgSend.dylib
* /usr/lib/objc/libobjcMsgSend1.dylib
* /usr/lib/objc/libobjcMsgSend2.dylib
* ...
* /usr/lib/objc/libobjcMsgSend33.dylib

The optimizer makes dozens of copies of the same `objc_msgSend` code and distributes them across the cache.
Every binary then branches to whichever copy sits within the range.

[![Abusing tclsh to Load (Remote) Shellcode on macOS](/img/2025-10-31-macos-abuse-tcl-lol/cover.webp)

Previous

### Abusing tclsh to Load (Remote) Shellcode on macOS](/posts/2025-10-31-macos-abuse-tcl-lol/)

© 2026

[GitHub](https://github.com/chichou)[Mastodon](https://infosec.exchange/%40codecolorist)[RSS](/feed.xml)