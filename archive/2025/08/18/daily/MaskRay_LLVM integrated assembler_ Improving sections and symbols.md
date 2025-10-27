---
title: LLVM integrated assembler: Improving sections and symbols
url: https://maskray.me/blog/2025-08-17-llvm-integrated-assembler-improving-sections-and-symbols
source: MaskRay
date: 2025-08-18
fetch_date: 2025-10-07T00:17:11.502070
---

# LLVM integrated assembler: Improving sections and symbols

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-08-17](/blog/2025-08-17-llvm-integrated-assembler-improving-sections-and-symbols)

# LLVM integrated assembler: Improving sections and symbols

In my previous post, [LLVM
integrated assembler: Improving expressions and relocations](/blog/2025-05-26-llvm-integrated-assembler-improving-expressions-and-relocations) delved
into enhancements made to LLVM's expression resolving and relocation
generation. This post covers recent refinements to MC, focusing on
sections and symbols.

## Sections

Sections are named, contiguous blocks of code or data within an
object file. They allow you to logically group related parts of your
program. The assembler places code and data into these sections as it
processes the source file.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` class MCSection { ...   enum SectionVariant {     SV_COFF = 0,     SV_ELF,     SV_GOFF,     SV_MachO,     SV_Wasm,     SV_XCOFF,     SV_SPIRV,     SV_DXContainer,   }; ``` |

In LLVM 20, the [`MCSection`
class](https://github.com/llvm/llvm-project/blob/release/20.x/llvm/include/llvm/MC/MCSection.h) used an enum called `SectionVariant` to
differentiate between various object file formats, such as ELF, Mach-O,
and COFF. These subclasses are used in contexts where the section type
is known at compile-time, such as in `MCStreamer` and [`MCObjectTargetWriter`](https://github.com/llvm/llvm-project/blob/release/21.x/llvm/include/llvm/MC/MCObjectWriter.h).
This change eliminates the need for runtime type information (RTTI)
checks, simplifying the codebase and improving efficiency.

Additionally, the storage for fragments' fixups (adjustments to
addresses and offsets) has been moved into the `MCSection`
class.

## Symbols

Symbols are names that represent memory addresses or values.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` class MCSymbol { protected:   /// The kind of the symbol.  If it is any value other than unset then this   /// class is actually one of the appropriate subclasses of MCSymbol.   enum SymbolKind {     SymbolKindUnset,     SymbolKindCOFF,     SymbolKindELF,     SymbolKindGOFF,     SymbolKindMachO,     SymbolKindWasm,     SymbolKindXCOFF,   };    /// A symbol can contain an Offset, or Value, or be Common, but never more   /// than one of these.   enum Contents : uint8_t {     SymContentsUnset,     SymContentsOffset,     SymContentsVariable,     SymContentsCommon,     SymContentsTargetCommon, // Index stores the section index   }; ``` |

Similar to sections, the [`MCSymbol`
class](https://github.com/llvm/llvm-project/blob/release/20.x/llvm/include/llvm/MC/MCSymbol.h) also used a discriminator enum, SymbolKind, to distinguish
between object file formats. This enum has also been removed.

Furthermore, the `MCSymbol` class had an
`enum Contents` to specify the kind of symbol. This name was
a bit confusing, so it has been [renamed
to `enum Kind`](https://github.com/llvm/llvm-project/commit/190778a8ba6d30995b7e1b4b4a556ab6444bdf3a) for clarity.

* regular symbol
* [equated
  symbol](/blog/2023-05-08-assemblers#symbol-equating-directives)
* [common
  symbol](/blog/2022-02-06-all-about-common-symbols)

A special enumerator, `SymContentsTargetCommon`, which was
used by AMDGPU for a specific type of common symbol, has also been [removed](https://github.com/llvm/llvm-project/commit/aa96e20dcefa7d73229c98a7d2727696ff949459).
The functionality it provided is now handled by updating
`ELFObjectWriter` to respect the symbol's section index
(`SHN_AMDGPU_LDS` for this special AMDGPU symbol).

`sizeof(MCSymbol)` has been reduced to 24 bytes on 64-bit
systems.

The previous blog post [LLVM
integrated assembler: Improving expressions and relocations](/blog/2025-05-26-llvm-integrated-assembler-improving-expressions-and-relocations)
describes other changes:

* The `MCSymbol::IsUsed` flag was a workaround for
  detecting a subset of invalid reassignments and is [removed](https://github.com/llvm/llvm-project/commit/e015626f189dc76f8df9fdc25a47638c6a2f3feb).
* The `MCSymbol::IsResolving` flag is added to detect
  cyclic dependencies of equated symbols.

Share

* [assembler](/blog/tags/assembler/)
* [llvm](/blog/tags/llvm/)

[**Newer**

Understanding alignment - from source to object file](/blog/2025-08-24-understanding-alignment-from-source-to-object-file)
[**Older**

LLVM integrated assembler: Engineering better fragments](/blog/2025-07-27-llvm-integrated-assembler-engineering-better-fragments)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/) [hpc](/blog/tags/hpc/) [image](/blog/tags/image/) [inotify](/blog/tags/inotify/) [ipsec](/blog/tags/ipsec/) [irc](/blog/tags/irc/) [isc](/blog/tags/isc/) [j](/blog/tags/j/) [javascript](/blog/tags/javascript/) [josephus problem](/blog/tags/josephus-problem/) [jq](/blog/tags/jq/) [kernel](/blog/tags/kernel/) [kythe](/blog/tags/kythe/) [ld](/blog/tags/ld/) [leetcode](/blog/tags/leetcode/) [libunwind](/blog/tags/libunwind/) [linker](/blog/tags/linker/) [linux](/blog/tags/linux/) [lld](/blog/tags/lld/) [lldb](/blog/tags/lldb/) [llvm](/blog/tags/llvm/) [lsp](/blog/tags/lsp/) [m68k](/blog/tags/m68k/) [makefile](/blog/tags/makefile/) [math](/blog/tags/math/) [maze](/blog/tags/maze/) [mirror](/blog/tags/mirror/) [ml](/blog/tags/ml/) [musl](/blog/tags/musl/) [mutt](/blog/tags/mutt/) [n-body](/blog/tags/n-body/) [neovim](/blog/tags/neovim/) [network](/blog/tags/network/) [nginx](/blog/tags/nginx/) [nim](/blog/tags/nim/) [nlp](/blog/tags/nlp/) [node.js](/blog/tags/node-js/) [noip](/blog/tags/noip/) [notmuch](/blog/tags/notmuch/) [npm](/blog/tags/npm/) [ocaml](/blog/tags/ocaml/) [offlineimap](/blog/tags/offlineimap/) [oi](/blog/tags/oi/) [oj](/blog/tags/oj/) [openwrt](/blog/tags/openwrt/) [parallel](/blog/tags/parallel/) [parser generator](/blog/tags/parser-generator/) [perl](/blog/tags/perl...