---
title: Relocation overflow and code models
url: https://buaq.net/go-163327.html
source: unSafe.sh - 不安全
date: 2023-05-15
fetch_date: 2025-10-04T11:36:49.986011
---

# Relocation overflow and code models

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

Relocation overflow and code models

When linking an oversized executable, it is possible to encountererrors such asrel
*2023-5-14 15:0:0
Author: [maskray.me(查看原文)](/jump-163327.htm)
阅读量:71
收藏*

---

When linking an oversized executable, it is possible to encounter
errors such as
`` relocation truncated to fit: R_X86_64_PC32 against `.text' ``
(GNU ld) or `relocation R_X86_64_PC32 out of range` (ld.lld).
These diagnostics are a result of the relocation overflow check, a
feature in the linker.

This article aims to explain why such issues can occur and provides
insights on how to mitigate them.

Certain groups prefer static linking or mostly static linking for the
sake of deployment convenience and performance. In scenarios where the
distributed program contains a significant amount of code (related:
software bloat), employing full or mostly static linking can result in
very large executable files. Consequently, certain relocations may be
close to the distance limit, and even a minor disruption can trigger
relocation overflow linker errors.

## Static linking

In this section, we will deviate slightly from the main topic to
discuss static linking. Static linking involves copying dependencies
directly into the final executable and is often preferred in certain
scenarios due to its advantages in deployment convenience and
performance.

By including all dependencies within the executable itself, it can
run without relying on external shared objects. This eliminates the
potential risks associated with updating dependencies separately.

Static linking also offers performance benefits in several
aspects:

* Link-time optimization is more effective when all dependencies are
  known. Providing shared object information during executable
  optimization is possible, but it may not be a worthwhile engineering
  effort.
* Profiling techniques are more efficient dealing with one single
  executable.
* The traditional ELF dynamic linking approach incurs overhead to
  support [symbol
  interposition](https://maskray.me/blog/2021-05-16-elf-interposition-and-bsymbolic).
* Dynamic linking involves PLT and GOT, which can introduce additional
  overhead. Static linking eliminates the overhead.
* Loading libraries in the dynamic loader has a time complexity
  `O(|libs|^2*|libname|)`. The existing implementations are
  designed to handle tens of shared objects, rather than a thousand or
  more.

Furthermore, the current lack of techniques to partition an
executable into a few larger shared objects, as opposed to numerous
smaller shared objects, exacerbates the overhead issue.

These performance benefits make static linking an attractive option
in certain scenarios, where the convenience and performance gains
outweigh the potential drawbacks.

## Relocation overflow

We will use the following C program to illustrate the concepts.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` int var; int callee(); int caller() { return callee() + var; } ``` |

The generated x86-64 assembly may appear as follows, with comments
indicating the relocation types associated with each instruction:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` .globl caller caller:   call [email protected]                  # R_X86_64_PLT32   add  eax, dword ptr [rip + var]  # R_X86_64_PC32  .bss .globl var var: .long 0 ``` |

Both `R_X86_64_PLT32` and `R_X86_64_PC32` have
a value range of `[-2**31,2**31)`. If the referenced symbol
is too far away from the relocated location, we may get a relocation
overflow.

In practice, relocation overflows due to code referencing code are
not common. The more frequent occurrences of overflows involve the
following categories (where we use `.text` to represent code
sections, `.rodata` for read-only data, and so on):

* `.text <-> .rodata`
* `.text <-> .eh_frame`: `.eh_frame` has
  32-bit offsets. 64-bit code offsets are possible, but I don't know if an
  implementation exists.
* `.text <-> .bss`
* `.rodata <-> .bss`

In many programs, `.text <-> .data/.bss` relocations
have the stringent constraints. Overflows due to
`.text <-> .rodata` relocations are possible but rare
(although I have encountered such issues in the past). Typically,
`.rodata` tends to be larger than the combined
`.data` and `.bss`.

`.rodata <-> .bss` overflows are generally
infrequent. However, caution must be exercised when working with
metadata `.quad label-.` instead of
`.long label-.`. Such issues can be easily addressed on the
compiler side.

The current section layout of ld.lld is as follows:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` .rodata .text .data .bss ``` |

One notable distinction from GNU ld is that `.rodata`
precedes `.text`. This ordering decreases the distance
between `.text` and `.data`/`.bss`,
thereby alleviating relocation overflow pressure for references from
`.text` to `.data`/`.bss`.

For handling `.eh_frame`, I suggest compiling with the [`-fno-asynchronous-unwind-tables`](https://maskray.me/blog/2020-11-08-stack-unwinding)
option. `.eh_frame` is used by runtime support for C++
exceptions. Many programs don't utilitize exceptions, making
`.eh_frame` non-mandatory. For profiling purposes, the
limitations of the `.eh_frame` format have become apparent,
and it is not the most suitable unwinding format.

## x86-64

The x86-64 psABI defines multiple code models. The small code model
is the one we are most familiar with. In the small code model, symbols
are required to be located within the range
`[0, 2**31 - 2**24)`.

The medium code model introduces large data sections such as
`.lrodata`, `.ldata`, `.lbss`, and uses
`movabs` instructions to access them. GCC providess several
variants for `.ldata`, including `.ldata.rel`,
`.ldata.rel.local`, `.ldata.rel.ro`, and
`.ldata.rel.ro.local`.

Linkers are expected to recognize these large data sections and place
them in appropriate locations. GNU ld uses the following section layout
in its internal linker scripts:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` .text .rodata   # if -z separate-code, MAXPAGESIZE alignment RELRO     # DATA_SEGMENT_ALIGN .data     # DATA_SEGMENT_RELRO_END .bss .lbss .lrodata  # MAXPAGESIZE alignment .ldata    # MAXPAGESIZE alignment ``` |

GNU ld places `.lbss`, `.lrodata`,
`.ldata` after `.bss` and inserts 2 MAXPAGESIZE
alignments for `.lrodata` and `.ldata`.

`.lbss` is placed immediately after `.bss`,
creating a single BSS, i.e. a read-write `PT_LOAD` program
header with `p_filesz<p_memsz`. The file image in the
segment is smaller than the memory image. When the dynamic loader
creates the memory image for the `PT_LOAD` segment, it will
set the byte range `[p_filesz,p_memsz)` to zeros. However,
there is a missing optimization that the `[p_filesz,p_memsz)`
portion occupies zero bytes in the object file, preventing overlap
between `.lrodata` and BSS in the file image.

For ld.lld, I am contemplating the following section layout:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` .lrodata .rodata .text     # if --ro-segment, MAXPAGESIZE alignment RELRO     # MAXPAGESIZE alignment .data     # MAXPAGESIZE alignment .bss .ldata    # MAXPAGESIZE alignment .lbss ``` |

GCC generates both regular and large data sections with
`-mcmodel=medium`. This is decided by a section size
threshold (`-mlarge-data-threshold`). In practice, programs
always mix object files built from small and medium/large code models
(just think of prebuilt object files including libc). The large data
sections built with `-mcmodel=large` do not exert relocation
pressure on sections in object files with
`-mcmodel=small`

However, GCC only generates regular data sections with
`-mcmo...