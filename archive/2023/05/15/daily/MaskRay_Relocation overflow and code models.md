---
title: Relocation overflow and code models
url: https://maskray.me/blog/2023-05-14-relocation-overflow-and-code-models
source: MaskRay
date: 2023-05-15
fetch_date: 2025-10-04T11:37:10.271533
---

# Relocation overflow and code models

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-05-14](/blog/2023-05-14-relocation-overflow-and-code-models)

# Relocation overflow and code models

Updated in 2025-05.

When linking an oversized executable, it is possible to encounter
errors such as
`` relocation truncated to fit: R_X86_64_PC32 against `.text' ``
(GNU ld) or `relocation R_X86_64_PC32 out of range` (ld.lld).
These diagnostics are a result of the relocation overflow check, a
feature in the linker.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % gcc -fuse-ld=bfd @response.txt ... a.o: in function `_start': (.text+0x0): relocation truncated to fit: R_X86_64_PC32 against `.text' % gcc -fuse-ld=lld @response.txt ld.lld: error: a.o:(.text+0x0): relocation R_X86_64_PC32 out of range: -2147483649 is not in [-2147483648, 2147483647]; references section '.text' ``` |

This article aims to explain why such issues can occur and provides
insights on how to mitigate them.

## Static linking

In this section, we will deviate slightly from the main topic to
discuss static linking. By including all dependencies within the
executable itself, it can run without relying on external shared
objects. This eliminates the potential risks associated with updating
dependencies separately.

Certain users prefer static linking or mostly static linking for the
sake of deployment convenience and performance aspects:

* Link-time optimization is more effective when all dependencies are
  known. Providing shared object information during executable
  optimization is possible, but it may not be a worthwhile engineering
  effort.
* Profiling techniques are more efficient dealing with one single
  executable.
* The traditional ELF dynamic linking approach incurs overhead to
  support [symbol
  interposition](/blog/2021-05-16-elf-interposition-and-bsymbolic).
* Dynamic linking involves PLT and GOT, which can introduce additional
  overhead. Static linking eliminates the overhead.
* Loading libraries in the dynamic loader has a time complexity
  `O(|libs|^2*|libname|)`. The existing implementations are
  designed to handle tens of shared objects, rather than a thousand or
  more.

Furthermore, the current lack of techniques to partition an
executable into a few larger shared objects, as opposed to numerous
smaller shared objects, exacerbates the overhead issue.

In scenarios where the distributed program contains a significant
amount of code (related: software bloat), employing full or mostly
static linking can result in very large executable files. Consequently,
certain relocations may be close to the distance limit, and even a minor
disruption (e.g. add a function or introduce a dependency) can trigger
relocation overflow linker errors.

## Relocation overflow

We will use the following C program to illustrate the concepts.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` int var0; // known non-preemptible if -fno-pic or -fpie extern int var1; // possibly-preemptible int callee(); int caller() { return callee() + var0 + var1; } ``` |

The generated x86-64 assembly may appear as follows, with comments
indicating the relocation types associated with each instruction:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` # gcc -S -O1 -fpie -mno-direct-extern-access -masm=intel a.c .globl caller caller:   call callee@PLT                          # R_X86_64_PLT32   add  eax, DWORD PTR [rip + var0]         # R_X86_64_PC32; load from &var0   mov  rdx, QWORD PTR var1@GOTPCREL[rip]   # R_X86_64_REX_GOTPCRELX; rdx = .got[n] = &var1   add  eax, DWORD PTR [rdx]                # load from &var1  .bss .globl var0 var0: .long 0 ``` |

You see that I specify `-mno-direct-extern-access` for
some assembly output. The option is to prefer GOT-generating code
sequences for possibly-preemptible data symbols. See
`-fdirect-access-external-data` on [Copy
relocations, canonical PLT entries and protected visibility](/blog/2021-01-09-copy-relocations-canonical-plt-entries-and-protected).

All of `R_X86_64_PLT32`, `R_X86_64_PC32`,
`R_X86_64_REX_GOTPCRELX`, and
`R_X86_64_CODE_4_GOTPCRELX` have a value range of
`[-2**31,2**31)`. If the referenced symbol is too far away
from the relocated location, we may get a relocation overflow.

In practice, relocation overflows due to code referencing code are
not common. The more frequent occurrences of overflows involve the
following categories (where we use `.text` to represent code
sections, `.rodata` for read-only data, and so on):

* `.text <-> .rodata`
* `.text <-> .eh_frame`: `.eh_frame` has
  32-bit offsets. 64-bit code offsets are possible, but I don't know if an
  implementation exists.
* `.text <-> .data/.bss`
* `.rodata <-> .data/.bss`

In many programs, `.text <-> .data/.bss` relocations
have the most stringent constraints. Overflows due to
`.text <-> .rodata` relocations are possible but rare
(although I have encountered such issues in the past).

`.rodata <-> .data/.bss` overflows are generally
infrequent. However, caution must be exercised when working with
metadata `.quad label-.` instead of
`.long label-.`. Such issues can be easily addressed on the
compiler side.

On x86-64, linkers optimize some GOT-indirect instructions
(`R_X86_64_REX_GOTPCRELX`; e.g.
`movq var@GOTPCREL(%rip), %rax`) to PC-relative instructions.
The distance between a code section and `.got` is usually
smaller than the distance between a code section and
`.data`/`.bss`. ld.lld's one-pass relocation
scanning scheme has a limitation: if it decides to suppress a GOT entry
and it turns out that optimizing the instruction will lead to relocation
overflow, the decision cannot be reverted. It should be easy to work
around the issue with `-Wl,--no-relax`.

The current section layout of ld.lld is as follows:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` .rodata .text .plt .data.rel.ro .got .data .bss ``` |

One notable distinction from GNU ld is that `.rodata`
precedes `.text`. This ordering decreases the distance
between `.text` and `.data`/`.bss`,
thereby alleviating relocation overflow pressure for references from
`.text` to `.data`/`.bss`.

For handling `.eh_frame`, I suggest compiling with the [`-fno-asynchronous-unwind-tables`](/blog/2020-11-08-stack-unwinding)
option. `.eh_frame` is used by runtime support for C++
exceptions. Many programs don't utilitize exceptions, making
`.eh_frame` non-mandatory. For profiling purposes, the
limitations of the `.eh_frame` format have become apparent,
and it is not the most suitable unwinding format.

## x86-64 code models

The x86-64 psABI defines multiple code models. Here is a summary:

* Small: symbols are required to be located within the range
  `[0, 2**31 - 2**24)`. Use 32-bit PC-relative or absolute
  addressing
* Kernel: similar to the small code model, but symbols are within the
  high end range
* Medium: keep using 32-bit offsets for code and GOT, but split data
  sections into 2 parts: regular and large. Large data can be more than
  2GiB away
* Large: all of code, GOT, and data can be more than 2GiB away

### x86-64 medium code model

The medium code model maintains the assumption that code and the GOT
is within the Â±2GiB range from the program counter, while allowing data
to be located outside of that range. Data that resides outside the range
is placed in large data sections such as `.lrodata`,
`.ldata`, and `.lbss`, as well as
`.ldata`'s variants like `.ldata.rel`,
`.ldata.rel.local`, `.ldata.rel.ro`, and
`.ldata.rel.ro.local`.

These sections may have the `SHF_X86_64_LARGE` flag.

`-mlarge-data-threshold=` decides whether a data section
should be treated as large.

Accessing code and GOT-indirect data has the same code sequence as
the small code model.

To access data without GOT indirection (usually a known
non-pree...