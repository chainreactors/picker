---
title: Linker notes on AArch64
url: https://buaq.net/go-152092.html
source: unSafe.sh - 不安全
date: 2023-03-06
fetch_date: 2025-10-04T08:44:52.135167
---

# Linker notes on AArch64

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Linker notes on AArch64

This article describes
*2023-3-5 16:0:0
Author: [maskray.me(查看原文)](/jump-152092.htm)
阅读量:34
收藏*

---

This article describes target-specific details about AArch64 in ELF
linkers. AArch64 is the 64-bit execution environment for the Arm
architecture.

## ABI documents

* [ELF
  for the Arm® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst)
* [System
  V ABI for the Arm® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/sysvabi64/sysvabi64.rst)

## Global Offset Table

The Global Offset Table consists of two sections:

* `.got.plt` holds code addresses for PLT.
* `.got` holds other addresses and offsets.

`_GLOBAL_OFFSET_TABLE_` is defined at the start of the
section `.got`. GNU ld reserves one entry for
`.got` and `.got[0]` holds the link-time address
of `_DYNAMIC` for a legacy reason glibc versions before 2.35
have the `_DYNAMIC` requirement. See [All
about Global Offset Table](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0).

`.got.plt[1]` and `.got.plt[2]` are for lazy
binding PLT. Linkers communicate the address of `.got.plt` to
rtld with the dynamic tag `DT_PLTGOT`.

### GOT optimization

See [All
about Global Offset Table#GOT optimization](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization).

## Procedure Linkage Table

`x16` (IP0) and `x17` (IP1) are the first and
second intra-procedure-call temporary registers. They may be used by PLT
entries and veneers.

The PLT header looks like:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` bti  c       // If BTI stp  x16, x30, [sp,#-16]! adrp x16, :page: &.got.plt[2] ldr  x17, [x16, :lo12: &.got.plt[2]] add  x16, x16, :lo12: &.got.plt[2] br   x17 ``` |

The Nth PLT entry looks like:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` bti  c       // If BTI adrp x16, :page: &.got.plt[N + 3] ldr  x17, [x16, :lo12: &.got.plt[N + 3]] add  x16, x16, :lo12: &.got.plt[N + 3] autia1716    // If PAC-PLT br   x17 ``` |

When BTI is enabled for the output file, the code sequence starts
with `bti c`. When PAC-PLT is enabled, the code sequence has
a `autia1716` before `br x17`.

## Relocation optimization

There are a few optimization schemes beside GOT optimization,
e.g.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` add  x2, x2, 0  // R_<CLS>_ADD_ABS_LO12_NC  =>  nop ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` adrp x0, :page: symbol add  x0, x0, :lo12: symbol  =>  nop adr  x0, symbol ``` |

See [ELF
for the Arm® 64-bit Architecture (AArch64)#Relocation
optimization](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst#relocation-optimization).

## Program Property

A `.note.gnu.property` section contains program property
notes which describe special handling requirements for the linker and
the dynamic loader.

The linker parses input `.note.gnu.property` sections and
recognizes command line options `-z force-bti` and
`-z pac-plt` to compute the output
`.note.gnu.property` (type is `SHT_NOTE`) section.
Without the options linkers set the feature bit in the output file only
if all the input relocatable object files have the corresponding feature
set.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` for (ELFFileBase *f : ctx.objectFiles) {   uint32_t features = f->andFeatures;   if (!(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {     if (config->zBtiReport == "error")       error(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");     else if (config->zBtiReport == "warning")       warn(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");   }    if (config->zForceBti && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {     if (config->zBtiReport == "none")       warn(toString(f) + ": -z force-bti: file does not have "                          "GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");     features |= GNU_PROPERTY_AARCH64_FEATURE_1_BTI;   }   if (config->zPacPlt && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_PAC)) {     warn(toString(f) + ": -z pac-plt: file does not have "                        "GNU_PROPERTY_AARCH64_FEATURE_1_PAC property");     features |= GNU_PROPERTY_AARCH64_FEATURE_1_PAC;   }   ret &= features; } ``` |

## Range extension thunks

Function calls typically use `B` and `BL`
instructions. The twoinstructions have a range of +/-128MiB and may use
2 relocation types: `R_AARCH64_CALL26` and
`R_AARCH64_JUMP26`. Linkers may insert a veneer (range
extension thunk) to a destination not reachable by a single
`B`/`BL`.

`-no-pie` links may use a thunk with absolute addressing
targeting any location in the 64-bit address space.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` <caller>:   bl      __AArch64AbsLongThunk_nonpreemptible   b       __AArch64AbsLongThunk_nonpreemptible  <__AArch64AbsLongThunk_nonpreemptible>:   ldr     x16, .+8   br      x16  <$d>:   .word   0x00000000   .word   0x00000010  <.plt>: ``` |

`-pie` and `-shared` links need to use a thunk
with PC-relative addressing targeting a range of +/-4GiB.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` <caller>:   bl      __AArch64ADRPThunk_nonpreemptible   b       __AArch64ADRPThunk_nonpreemptible  <__AArch64ADRPThunk_nonpreemptible>:   adrp    x16, :page: nonpreemptible   add     x16, x16, :lo12: nonpreemptible   br      x16 ``` |

The branch target of a thunk may be a PLT entry:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` <caller>:   bl      __AArch64ADRPThunk_preemptible  <__AArch64ADRPThunk_preemptible>:   adrp    x16, :page: [email protected]   add     x16, x16, :lo12: [email protected]   br      x16  ...  <[email protected]>:   adrp    x16, :page: &.got.plt[N + 3]   ldr     x17, [x16, :lo12: &.got.plt[N + 3]]   add     x16, x16, :lo12: &.got.plt[N + 3]   br      x17 ``` |

[**Older**

Linker notes on Power ISA](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)

文章来源: https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)