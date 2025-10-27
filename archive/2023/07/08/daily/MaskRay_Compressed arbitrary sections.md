---
title: Compressed arbitrary sections
url: https://maskray.me/blog/2023-07-07-compressed-arbitrary-sections
source: MaskRay
date: 2023-07-08
fetch_date: 2025-10-04T11:53:16.691536
---

# Compressed arbitrary sections

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-07-07](/blog/2023-07-07-compressed-arbitrary-sections)

# Compressed arbitrary sections

This article describes `SHF_ALLOC|SHF_COMPRESSED` sections
in ELF and lld's linker option `--compress-sections` to
compress arbitrary sections.

## .symtab and .strtab

In ELF executables and DSOs, `.symtab` and
`.strtab` sections can consume a significant portion of the
file size (10+% or even 20+%). In many scenarios, we cannot remove them
due to symbolizers (crash reporters, Linux perf, etc) and other analysis
tools. `.symtab` and `.strtab` might be present in
the executable/DSO or a debug file (see [`.gnu_debuglink`](/blog/2022-10-30-distribution-of-debug-information#gnu_debuglink)).

It's natural to compress the two sections using the standard
`SHF_COMPRESSED` feature.

* [binutils
  feature request](https://sourceware.org/bugzilla/show_bug.cgi?id=31884)
* [LLVM
  Discourse post](https://discourse.llvm.org/t/rfc-compressed-sht-symtab-sht-strtab-for-elf/77608)

## Metadata sections

In recent years, metadata sections have gained more uses. Some users
may find compression attractive if they weigh file sizes over
decompression overhead.

Some metadata sections are non-`SHF_ALLOC`, like DWARF
debug sections. They may be unused by a runtime library but provide
additional information for an analysis tool to inspect the content.

Other metadata sections have the `SHF_ALLOC` flag and
therefore are part of a `PT_LOAD` segment. When the program
is executed, we will have both the compressed and uncompressed copies in
memory. This may appear inefficient if the runtime library needs to
allocate a buffer for the decompressed content. Why do some people
accept this tradeoff? Well, they may prioritize file size or they simply
accept this inefficiency.

Some factors may lean more toward compression.

* Some metadata sections are optional and may be used infrequently
  (think of debug sections).
* Some use cases allow for streaming decompression. They may build an
  in-memory data structure from the decompressed section content and can
  then discard the decompressed section.

Anyhow, compression is sometimes useful and designers may want to
implement compression within the format. However, this would lead to
duplicated code, considering that we have a generic feature at the
object file format level: ELF `SHF_COMPRESSED`.

## `SHF_COMPRESSED` sections

[Compressed debug
sections](/blog/2022-01-23-compressed-debug-sections) I wrote last year describes `SHF_COMPRESSED`.
Currently, its use cases are limited to debug sections.

Many ELF linkers provide
`--compress-debug-sections=[zlib|zstd]` to compress
`.debug_*` sections. This functionality can be extended to
arbitrary sections. I filed a [GNU ld
feature request](https://sourceware.org/bugzilla/show_bug.cgi?id=27452) in 2021, and recently decided to push forward with
the effort. I have implemented [[ELF] Add
--compress-sections](https://reviews.llvm.org/D154641) in ld.lld.

My proposed syntax is
`--compress-sections <section-glob>={none,zlib,zstd}[:level]`.
If an output section matches the glob pattern, it will be compressed
using the specified format: zlib or zstd. The compression level is
`level` (if specified) or a default speed-focused level.

A natural question arises: if a `SHF_ALLOC` section is
matched, should the linker compress the section?

## `SHF_ALLOC|SHF_COMPRESSED` sections

I believe the answer is yes. However, I have concerns regarding
non-compliance with the ELF standard, as stated in the current generic
ABI documentation:

> `SHF_COMPRESSED` - This flag identifies a section
> containing compressed data. `SHF_COMPRESSED` applies only to
> non-allocable sections, and cannot be used in conjunction with
> `SHF_ALLOC`. In addition, `SHF_COMPRESSED` cannot
> be applied to sections of type `SHT_NOBITS`.

I believe this restriction is unnecessary for all of relocatable
object files, executables, and shared objects. Therefore, I have [proposed a
change](https://groups.google.com/g/generic-abi/c/HUVhliUrTG0) in the generic-abi group to remove the incompatibility
between `SHF_COMPRESSED` and `SHF_ALLOC` in the
wording.

For `SHF_ALLOC|SHF_COMPRESSED` sections in relocatable
object files, they are fine as long as the linker is capable of
decompressing the content. It is also important to ensure that
non-linker consumers are compatible with the section, which is
relatively easy to confirm.

For linker output (executable or shared object), having both the
`SHF_ALLOC` and `SHF_COMPRESSED` flags should be
permissible. For example, we can use PC-relative relocations in a
metadata section to reference text sections. These relocations will be
resolved at link time.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ```   ...   leaq __start_foo0(%rip), %rdi   leaq __stop_foo0(%rip), %rsi   call runtime  .section .text.foo,"ax" nop .section .text.bar,"ax" nop  .section foo,"a" .p2align 3 .quad .text.foo-. .quad .text.bar-. ``` |

Section headers are optional in executables and shared objects and
are ignored by runtime loaders. The runtime loader does not require any
special handling for the `SHF_COMPRESSED` flag.

When the program is executed, the runtime library responsible for the
metadata section will allocate memory and decompress the section's
content. Let's say `foo` has the address 0x201000 in memory.
If we allocate the decompressed buffer at address 0x202000, we need to
add the offset 0x201000-0x202000 = -0x1000 to the label differences in
`foo`.

Section decompression imposes certain limitations on use cases.

First, the sections cannot have dynamic sections. Relocation offsets
are relative to the decompressed section instead of the compressed
section. However, the runtime loader doesn't know there are compressed
sections, so it would blindly apply the relocation. In the common case
that the compressed section is smaller, the runtime loader will modify
bytes in a subsequent section or an unmapped address, leading to runtime
crashes or corruption of writable data sections.

In general, absolute references should be replaced with label
differences.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` .section foo.wrong,"a" .p2align 3 .quad .text.foo  # wrong .quad .text.bar  # wrong ``` |

Second, a symbol defined relative to an input section designate an
offset relative to the compressed content. If the program tries to read
the content at the symbol, it will load a random location from the
compressed content or another section. Similar to the arithmetic example
above (0x201000-0x202000 = -0x1000), the runtime library may adjust the
symbol value by `addr(compressed)-addr(decompressed)` to
obtain an offset relative to the decompressed content. If there are two
symbols defined relative to one or two input sections, taking the
difference can be more convenient.

Third, there is a circular dependency between the compressed section
content and the section layout.

* The uncompressed section content decides the compressed section
  size.
* The compressed section size affects addresses of subsequent sections
  and symbol assignments. The affected sections include text sections that
  use range extension thunks.
* Subsequent sections and symbol assignments may affect the
  uncompressed section content.
  + PC-relative references to text sections (e.g.,
    `.quad .text.foo-.`) change values when the text section
    address changes.
  + data commands in an output section description may change.
  + location counter increments (e.g., `. += expr;`) in an
    output section description may change.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` SECTIONS {   ...   foo : { *(foo*) QUAD(expr1) . += expr2; } } ``` |

If the linker compresses t...