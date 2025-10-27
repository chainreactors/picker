---
title: My involvement with LLVM 18
url: https://maskray.me/blog/2024-02-25-my-involvement-with-llvm-18
source: MaskRay
date: 2024-02-26
fetch_date: 2025-10-04T12:05:48.735063
---

# My involvement with LLVM 18

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-02-25](/blog/2024-02-25-my-involvement-with-llvm-18)

# My involvement with LLVM 18

LLVM 18 will soon be relased. This post provides a summary of my
contributions in this release cycle to record my learning progress.

* LLVM binary utility maintenance, e.g.
  + [adopted llvm-readobj
    style ObjectFile specific dumpers](https://reviews.llvm.org/D155045)
  + [`[llvm-objdump][X86] Add @plt symbols for .plt.got`](https://reviews.llvm.org/D149817)
  + [`[llvm-readobj] Print <null> for relocation target with an empty name`](https://reviews.llvm.org/D155353)
  + Support `--decompress`/`-z` ([#82594](https://github.com/llvm/llvm-project/pull/82594))
* sanitizer maintenance, e.g.
  + [[asan]
    Enable StackSafetyAnalysis by default](https://github.com/llvm/llvm-project/pull/77210)
  + asan\_static x86-64: Support 64-bit
    `ASAN_SHADOW_OFFSET_CONST` ([#75748](https://github.com/llvm/llvm-project/pull/75748))
  + [asan] Report executable/DSO name for report\_globals=2 and
    odr-violation checking ([#71879](https://github.com/llvm/llvm-project/pull/71879))
  + changed lsan to work with high-entropy ASLR for x86-64 Linux
  + [removed crypt and crypt\_r
    interceptors](https://reviews.llvm.org/D149403) to work with glibc
  + [implemented
    interceptors](https://reviews.llvm.org/D158943) for glibc 2.38 `__isoc23_strtol` and
    `__isoc23_scanf` family functions
  + tsan: Respect !nosanitize metadata and remove gcov special case
  + [dfsan] Wrap glibc 2.38 `__isoc23_*` functions ([#79958](https://github.com/llvm/llvm-project/pull/79958))
  + `-fsanitize=alignment`: check memcpy/memmove arguments
    (#67766)
* gcov maintenance
  + Ignore blocks from another file to fix a crash
* LTO maintenance
  + Improve diagnostics handling when parsing module-level inline
    assembly ([#75726](https://github.com/llvm/llvm-project/pull/75726))
* MC maintenance
  + [[MC,AArch64] Suppress
    local symbol to STT\_SECTION conversion for GOT relocations](https://reviews.llvm.org/D158577)
  + [MC](#mc) Make `.pseudo_probe` created
    sections deterministic after D91878
  + Change `.reloc` to register used symbols
  + Change `SHF_LINK_ORDER` and section group parsing order
    to match GNU assembler
* AArch32
  + [ARM,ELF] Fix access to dso\_preemptable \_\_stack\_chk\_guard with
    static relocation model ([#70014](https://github.com/llvm/llvm-project/pull/70014))
* AArch64
  + [Suppress local symbol to
    STT\_SECTION conversion for GOT relocations](https://reviews.llvm.org/D158577)
  + Restrict MOVZ/MOVK to non-PIC large code model ([#70178](https://github.com/llvm/llvm-project/pull/70178))
  + clang: Define `__GCC_HAVE_SYNC_COMPARE_AND_SWAP_16` for
    AArch64 ([#74954](https://github.com/llvm/llvm-project/pull/74954))
* MIPS
  + Use generic isBlockOnlyReachableByFallthrough ([#80799](https://github.com/llvm/llvm-project/pull/80799))
* RISC-V
  + Clean up code after improved assembler support for linker
    relaxation
  + [Support
    R\_RISCV\_SET\_ULEB128/R\_RISCV\_SUB\_ULEB128 for .uleb128 directives](https://reviews.llvm.org/D157657)
  + Parse SHF\_LINK\_ORDER argument before section group name ([#77407](https://github.com/llvm/llvm-project/pull/77407))
  + `R_RISCV_CALL`/`R_RISCV_CALL_PLT` assembler
    and assembly parser cleanup
  + Force relocations if initial MCSubtargetInfo contains FeatureRelax
    ([#77436](https://github.com/llvm/llvm-project/pull/77436))
* x86
  + Support inline assembly constraint "Ws"
  + Change displacement overflow when parsing assembly code ([#75747](https://github.com/llvm/llvm-project/pull/75747))
  + Fix MSVC-style inline assembly `call fptr` and
    `jmp fptr` ([#73207](https://github.com/llvm/llvm-project/pull/73207))
  + In 32-bit mode, fix FastISel `-fno-pic` for intrinsics to
    emit `R_386_PC32` instead of `R_386_PLT32` ([#51078](https://github.com/llvm/llvm-project/pull/51078))
  + clang: Support `arch=x86-64{,-v2,-v3,-v4}` for
    `target_clones` attribute
  + clang: `__builtin_cpu_supports`: support
    `x86-64{,-v2,-v3,-v4}`
* libunwind
  + Bump to `CXX_STANDARD 17` ([#75986](https://github.com/llvm/llvm-project/pull/75986))

## lld

See [lld 18 ELF
changes](/blog/2024-02-18-lld-18-elf-changes)

## MC

* Removed many obsoleted workarounds from the integrated
  assembler
* Fixed placement of function entry comments
* Re-architectured a substantial part of the integrated assembler that
  is used by RISC-V linker relaxation, fixing some longstanding bugs. See
  [The
  dark side of RISC-V linker relaxation](/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation) for detail.

## Clang

Driver maintenance

* [[Driver] -###: exit with
  code 1 if hasErrorOccurred](https://reviews.llvm.org/D156363)
* [Report errors for
  target-specific options on unsupported targets](https://reviews.llvm.org/D158329)
* Remove RequiresPIE and msan's NeedPIE setting (#77689)
* Add -fandroid-pad-segment/-fno-android-pad-segment (#77244)
* Support `-mtls-dialect=desc`

Others:

* Function multi-versioning: don't set comdat for internal linkage
  resolvers

## Code review

Reviewed many patches, including ADT/Support, binary utilities, MC,
lld (sometimes non-ELF ports even if my primary expertise is in ELF),
clangDriver, LTO, sanitizers, LoongArch, RISC-V, x86-64 medium/large
code models, etc.

TODO
`is:pr is:closed sort:updated-desc review-requested:@me`
lists pull requests that requested a review from me, but it's unclear
how to list pull requests that I've made a comment.

Link: [My
involvement with LLVM 17](/blog/2023-08-20-my-involvement-with-llvm-17)

Share

* [llvm](/blog/tags/llvm/)

[**Newer**

A compact relocation format for ELF](/blog/2024-03-09-a-compact-relocation-format-for-elf)
[**Older**

MMU-less systems and FDPIC](/blog/2024-02-20-mmu-less-systems-and-fdpic)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/...