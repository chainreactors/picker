---
title: A compact section header table for ELF
url: https://maskray.me/blog/2024-03-31-a-compact-section-header-table-for-elf
source: MaskRay
date: 2024-04-01
fetch_date: 2025-10-04T12:14:59.744666
---

# A compact section header table for ELF

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-03-31](/blog/2024-03-31-a-compact-section-header-table-for-elf)

# A compact section header table for ELF

ELF's design emphasizes [natural size
and alignment guidelines for its control structures](/blog/2024-03-09-a-compact-relocation-format-for-elf). However, this
approach has substantial size drawbacks.

In a release build of llvm-project
(`-O3 -ffunction-sections -fdata-sections`, the section
header tables occupy 13.4% of the `.o` file size.

I propose an alternative section header table format that is signaled
by `e_shentsize == 0` in the ELF header.
`e_shentsize == sizeof(Elf64_Shdr)` (or the 32-bit
counterpart) selects the traditional section header table format.

The content bgins with a ULEB128-encoded value `nshdr`:
the number of sections (including `SHN_UNDEF`).
`nshdr` section headers follow `nshdr`.

Each header begins with a `presence` byte indicating which
subsequent `Elf_Shdr` members use explicit values vs.
defaults:

* `sh_name`, ULEB128 encoded
* `sh_type`, ULEB128 encoded (if
  `presence & 1`), defaults to
  `SHT_PROGBITS`
* `sh_flags`, ULEB128 encoded (if
  `presence & 2`), defaults to 0
* `sh_addr`, ULEB128 encoded (if
  `presence & 4`), defaults to 0
* `sh_offset`, ULEB128 encoded
* `sh_size`, ULEB128 encoded (if
  `presence & 8`), defaults to 0
* `sh_link`, ULEB128 encoded (if
  `presence & 16`), defaults to 0
* `sh_info`, ULEB128 encoded (if
  `presence & 32`), defaults to 0
* `sh_addralign`, ULEB128 encoded as log2 value (if
  `presence & 64`), defaults to 1
* `sh_entsize`, ULEB128 encoded (if
  `presence & 128`), defaults to 0

In traditional ELF, `sh_addralign` can be 0 or a positive
integral power of two, where 0 and 1 mean the section has no alignment
constraints. While the compact encoding cannot encode
`sh_addralign` value of 0, there is no loss of
generality.

Example C++ code that decodes a section header:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` // readULEB128(const uint8_t *&p);  const uint8_t *sht = base + ehdr->e_shoff; const uint8_t *p = sht + offsets[i]; uint8_t presence = *p++; Elf_Shdr shdr = {}; shdr.sh_name = readULEB128(p); shdr.sh_type = presence & 1 ? readULEB128(p) : ELF::SHT_PROGBITS; shdr.sh_flags = presence & 2 ? readULEB128(p) : 0; shdr.sh_addr = presence & 4 ? readULEB128(p) : 0; shdr.sh_offset = readULEB128(p); shdr.sh_size = presence & 8 ? readULEB128(p) : 0; shdr.sh_link = presence & 16 ? readULEB128(p) : 0; shdr.sh_info = presence & 32 ? readULEB128(p) : 0; shdr.sh_addralign = presence & 64 ? 1UL << readULEB128(p) : 1; shdr.sh_entsize = presence & 128 ? readULEB128(p) : 0; ``` |

While O(1) random access isn't supported, this is often addressed by
applications building their own data representations. Alternatively, for
simpler applications, a prescan can be performed to determine the
starting offset of each header beforehand.

In a release build of llvm-project
(`-O3 -ffunction-sections -fdata-sections -Wa,--crel`, the
traditional section header tables occupy 16.4% of the `.o`
file size while the compact section header table drastically reduces the
ratio to 4.7%.

## Experiments

I have developed a Clang/lld prototype that implements compact
section header table and CREL. <https://github.com/MaskRay/llvm-project/tree/demo-cshdr>

| `.o size` | sht size | build |
| --- | --- | --- |
| 136599656 | 18429824 | -O3 |
| 112088088 | 18431616 | -O3 -Wa,--crel |
| 97517175 | 3860703 | -O3 -Wa,--crel,--cshdr |
| 2166435360 | 260303360 | -g |
| 1755222784 | 260305152 | -g -Wa,--crel |
| 1557420523 | 62502891 | -g -Wa,--crel,--chsdr |

## Alternatives

The WebAssembly object file format implemented by LLVM adopts the
following design that does not use section headers. Consumders need to
perform a few random accesses to collect all section information.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` # start section foo section_id size content # end section  # start_section bar section_id size content # end section ``` |

We could adopt a similar design by adding metadata beside the size
field. We would be able to remove the `sh_offset` member.

We could take inspirations from DWARF `.debug_abbrev`:
define a few shapes with fixed fields (e.g.
`sh_type==SHT_PROGBITS`) and make a section header fill in
the rest fields.

We could also adopt a scheme similar to
`.subsections_via_symbols`, but using metadata instead of
symbols to describe subsection boundaries.

## More ideas

Like other sections, [symbol
table](/blog/2024-01-14-exploring-object-file-formats#symbols) and string table sections (`SHT_SYMTAB` and
`SHT_STRTAB`) can be compressed through
`SHF_COMPRESSED`. However, compressing the dynamic symbol
table (`.dynsym`) and its associated string table
(`.dynstr`) is not recommended.

Symbol table sections have a non-zero `sh_entsize`, which
remains unchanged after compression.

The string table, which stores symbol names (also section names in
LLVM output), is typically much larger than the symbol table itself. To
reduce its size, we can utilize a text compression algorithm. While
compressing the string table, compressing the symbol table along with it
might make sense, but using a compact encoding for the symbol table
itself won't provide significant benefits.

Share

* [elf](/blog/tags/elf/)
* [linker](/blog/tags/linker/)

[**Newer**

Light ELF: exploring potential size reduction](/blog/2024-04-01-light-elf-exploring-potential-size-reduction)
[**Older**

C++ exit-time destructors](/blog/2024-03-17-c%2B%2B-exit-time-destructors)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/) [hpc](/blog/tags/hpc/) [image](/blog/tags/image/) [inotify](/blog/tags/inotify/) [ipsec](/blog/tags/ipsec/) [irc](/blog/tags/irc/) [isc](/blog/tags/isc/) [j](/blog/tags/j/) [javascript](/blog/tags/javascript/) [josephus problem](/blog/tags/josephus-problem/) [jq](/...