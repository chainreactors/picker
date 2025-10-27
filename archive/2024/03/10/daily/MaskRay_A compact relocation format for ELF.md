---
title: A compact relocation format for ELF
url: https://maskray.me/blog/2024-03-09-a-compact-relocation-format-for-elf
source: MaskRay
date: 2024-03-10
fetch_date: 2025-10-04T12:08:19.834634
---

# A compact relocation format for ELF

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-03-09](/blog/2024-03-09-a-compact-relocation-format-for-elf)

# A compact relocation format for ELF

This article introduces CREL (previously known as RELLEB), a new
relocation format offering incredible size reduction ([LLVM
implementation in my fork](https://github.com/MaskRay/llvm-project/tree/demo-crel)).

ELF's design emphasizes natural size and alignment guidelines for its
control structures. This principle, outlined in Proceedings of the
Summer 1990 USENIX Conference, *ELF: An Object File to Mitigate
Mischievous Misoneism*, promotes ease of random access for
structures like program headers, section headers, and symbols.

> All data structures that the object file format defines follow the
> "natural" size and alignment guidelines for the relevant class. If
> necessary, data structures contain explicit padding to ensure 4-byte
> alignment for 4-byte objects, to force structure sizes to a multiple of
> four, etc. Data also have suitable alignment from the beginning of the
> file. Thus, for example, a structure containing an Elf32\_Addr member
> will be aligned on a 4-byte boundary within the file. Other classes
> would have appropriately scaled definitions. To illustrate, the 64-bit
> class would define Elf64 Addr as an 8-byte object, aligned on an 8-byte
> boundary. Following the strictest alignment for each object allows the
> format to work on any machine in a class. That is, all ELF structures on
> all 32-bit machines have congruent templates. For portability, ELF uses
> neither bit-fields nor floating-point values, because their
> representations vary, even among pro- cessors with the same byte order.
> Of course the programs in an ELF file may use these types, but the
> format itself does not.

While beneficial for many control structures, the natural size
guideline presents significant drawbacks for relocations. Since
relocations are typically processed sequentially, they don't gain the
same random-access advantages. The large 24-byte `Elf64_Rela`
structure highlights the drawback. For a detailed comparison of
relocation formats, see [Exploring
object file formats#Relocations](https://maskray.me/blog/2024-01-14-exploring-object-file-formats#relocations).

Furthermore, `Elf32_Rel` and `Elf32_Rela`
sacrifice flexibility to maintain a smaller size, limiting relocation
types to a maximum of 255. This constraint has become noticeable for
AArch32 and RISC-V, and especially when platform-specific relocations
are needed. While the 24-bit symbol index field is less elegant, it
hasn't posed significant issues in real-world use cases.

In contrast, the [WebAssembly
object file format](https://github.com/WebAssembly/tool-conventions/blob/main/Linking.md#relocation-sections) uses LEB128 encoding for relocations and other
constrol structures, offering a significant size advantage over ELF.

Inspired by WebAssembly, I will start discussion with a generic
compression algorithm and then propose an alternative format (CREL) that
addresses ELF's limitations.

## Compressed relocations

While the standard `SHF_COMPRESSED` feature is commonly
used for debug sections, its application can easily extend to relocation
sections. I have developed a Clang/lld prototype that demonstrates this
by compressing `SHT_RELA` sections.

The compressed `SHT_RELA` section occupies
`sizeof(Elf64_Chdr) + size(compressed)` bytes. The
implementation retains uncompressed content if compression would result
in a larger size.

In scenarios with numerous smaller relocation sections (such as when
using `-ffunction-sections -fdata-sections`), the 24-byte
`Elf64_Chdr` header can introduce significant overhead. This
observation raises the question of whether encoding
`Elf64_Chdr` fields using ULEB128 could further optimize file
sizes. With larger monolithic sections (`.text`,
`.data`, `.eh_frame`), compression ratio would be
higher as well.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # configure-llvm is my wrapper of cmake that specifies some useful options. configure-llvm s2-custom0 -DLLVM_TARGETS_TO_BUILD=host -DLLVM_ENABLE_PROJECTS='clang;lld' configure-llvm s2-custom1 -DLLVM_TARGETS_TO_BUILD=host -DLLVM_ENABLE_PROJECTS='clang;lld' -DCMAKE_{C,CXX}_FLAGS=-Xclang=--compress-relocations=zstd ninja -C /tmp/out/s2-custom0 lld ninja -C /tmp/out/s2-custom1 lld  ruby -e 'p Dir.glob("/tmp/out/s2-custom0/**/*.o").sum{|f| File.size(f)}'  # 135996752 ruby -e 'p Dir.glob("/tmp/out/s2-custom1/**/*.o").sum{|f| File.size(f)}'  # 116424688 ``` |

Relocations consume a significant portion (approximately 20.9%) of
the file size. Despite the overhead of
`-ffunction-sections -fdata-sections`, the compression
technique yields a significant reduction of 14.5%!

However, dropping in-place relocation processing is a downside.

## CREL relocation format

The 1990 ELF paper *ELF: An Object File to Mitigate Mischievous
Misoneism* says "ELF allows extension and redefinition for other
control structures." Let's explore CREL, a new and more compact
relocation format designed to replace REL and RELA. Our emphasis is on
simplicity over absolute minimal encoding. This is achieved by using a
byte-oriented encoding that avoids complex compression techniques (e.g.,
dictionary-based compression, entropy encoder). As a byte-oriented
format, CREL relocations can be further compressed by other codecs, if
desired. Using CREL as relocatable files can decrease memory usage.

See the end of the article for a detailed format description.

A `SHT_CREL` section (preferred name:
`.crel<name>`) holds compact relocation entries that
decode to `Elf32_Rela` or `Elf64_Rela` depending
on the object file class (32-bit or 64-bit). Its content begins with a
ULEB128-encoded relocation count, followed by entries encoding
`r_offset`, `r_type`, `r_symidx`, and
`r_addend`. The entries use ULEB128 and SLEB128 exclusively
and there is no endianness difference.

Here are key design choices:

*Relocation count (ULEB128)*:

This allows for efficient retrieval of the relocation count without
decoding the entire section. While a `uint32_t` (like [`SHT_HASH`](https://www.sco.com/developers/gabi/latest/ch5.dynamic.html#hash))
could be used, ULEB128 aligns with subsequent entries, removes
endianness differences, and offers a slight size advantage in most cases
when the number of symbols can be encoded in one to three bytes.

*Shifted offset*:

64-bit data sections frequently have absolute relocations spaced 8
bytes apart. Additionally, in RISC architectures, offsets are often
multiples of 2 or 4. A shift value of 2 allows delta offsets within the
[0, 64) range to be encoded in a single byte, often avoiding the need
for two-byte encoding. In an AArch64 `-O3` build, the shifted
offset technique reduces `size(.crel*)` by 12.8%.

Many C++ virtual tables have the first relocation at offset 0x10. In
the absence of the shifted offset technique, the relocation at offset
0x10 cannot be encoded in one byte.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` Relocation section '.crel.data.rel.ro._ZTVN12_GLOBAL__N_113InlineSpillerE' at offset 0x116fe contains 5 entries:     Offset             Info             Type               Symbol's Value  Symbol's Name + Addend 0000000000000010  0000007e00000001 R_X86_64_64            0000000000000000 _ZN4llvm7Spiller6anchorEv + 0 0000000000000018  0000000c00000001 R_X86_64_64            0000000000000000 .text._ZN12_GLOBAL__N_113InlineSpillerD2Ev + 0 0000000000000020  0000000f00000001 R_X86_64_64            0000000000000000 .text._ZN12_GLOBAL__N_113InlineSpillerD0Ev + 0 0000000000000028  0000001100000001 R_X86_64_64            0000000000000000 .text._ZN12_GLOBAL__N_113InlineSpiller5spillERN4llvm13LiveRangeEditE + 0 0000000000000030  0...