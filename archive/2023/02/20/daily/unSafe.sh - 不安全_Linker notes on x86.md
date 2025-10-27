---
title: Linker notes on x86
url: https://buaq.net/go-150082.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:09.611684
---

# Linker notes on x86

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

Linker notes on x86

This article describes
*2023-2-19 16:0:0
Author: [maskray.me(查看原文)](/jump-150082.htm)
阅读量:28
收藏*

---

This article describes target-specific things about x86 in ELF
linkers. I will use "x86" to refer to both x86-32 and x86-64.

## Global Offset Table

`_GLOBAL_OFFSET_TABLE_` is defined at the start of the
section `.got.plt`. `.got.plt` has 3 reserved
entries.

`_GLOBAL_OFFSET_TABLE_[0]` stores the link-time address of
`_DYNAMIC` for a legacy reason. It's unused now. See [All
about Global Offset Table](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0).

`_GLOBAL_OFFSET_TABLE_[1]` and
`_GLOBAL_OFFSET_TABLE_[2]` are for lazy binding PLT.

### GOT optimization

See [All
about Global Offset Table#GOT optimization](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization).

## Procedure Linkage Table

### Retpoline and Indirect Branch Tracking

ld.lld supports `-z retpolineplt` for Spectre v2
mitigation.

See `.note.gnu.property` below for Indirect Branch
Tracking.

See [All about
Procedure Linkage Table#x86](https://maskray.me/blog/2021-09-19-all-about-procedure-linkage-table#x86) for detail.

## Thread Local Storage

x86 uses TLS Variant II: the static TLS blocks are placed below the
thread pointer.

Beside the traditional general dynamic and local dynamic TLS models,
there are TLSDESC ABIs for x86-32 and x86-64.

The linker performs TLS optimization.

See [All
about thread-local storage](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage).

## `.note.gnu.property`

The linker parses input `.note.gnu.property` sections and
recognize `-z force-ibt` and `-z shstk` to compute
the output `.note.gnu.property` (type is
`SHT_NOTE`) section.

The following code (extracted from ld.lld) describes the behavior.
Basically, without extra options, the output has the
`GNU_PROPERTY_X86_FEATURE_1_IBT` bit if all input
`.note.gnu.property` sections have the bit (logical AND).
`-z force-ibt` forces setting the bit with a warning.

The output has the `GNU_PROPERTY_X86_FEATURE_1_SHSK` bit
if all input `.note.gnu.property` sections have the bit
(logical AND). `-z shstk` forces setting the bit without a
warning.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` for (ELFFileBase *f : ctx.objectFiles) {   uint32_t features = f->andFeatures;   if (!(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {     if (config->zCetReport == "error")       error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");     else if config->zCetReport == "warning")       warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");   }   if (!(features & GNU_PROPERTY_X86_FEATURE_1_SHSTK)) {     if (config->zCetReport == "error")       error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");     else if config->zCetReport == "warning")       warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");   }    if (config->zForceIbt && !(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {     if (config->zCetReport == "none")       warn(toString(f) + ": -z force-ibt: file does not have "                          "GNU_PROPERTY_X86_FEATURE_1_IBT property");     features |= GNU_PROPERTY_X86_FEATURE_1_IBT;   }   ret &= features; }   if (config->zShstk)   ret |= GNU_PROPERTY_X86_FEATURE_1_SHSTK; ``` |

See [Control flow
integrity](https://maskray.me/blog/2022-12-18-control-flow-integrity) for an overview of Intel CET.

## `.eh_frame`

Clang since rL252300 emits `.eh_frame` sections of type
`SHT_X86_64_UNWIND`. It is unfortunate that
`.eh_frame` does not use a dedicated section type but
nowadays

## `.gnu.linkonce.t.__x86.get_pc_thunk.bx`

The magic symbol prefix `.gnu.linkonce` was used before
COMDAT was introduced into ELF. `.gnu.linkonce` was very
obsoleted now, but unfortunately
`.gnu.linkonce.t.__x86.get_pc_thunk.bx` remained relevant in
glibc x86-32 until glibc 2.32 (2020-08).

[**Older**

All about LeakSanitizer](https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer)

文章来源: https://maskray.me/blog/2023-02-19-linker-notes-on-x86
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)