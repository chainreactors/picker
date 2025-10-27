---
title: 2024年总结
url: https://maskray.me/blog/2024-12-31-summary
source: MaskRay
date: 2025-01-01
fetch_date: 2025-10-06T20:06:42.954282
---

# 2024年总结

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-12-31](/blog/2024-12-31-summary)

# 2024å¹´æ»ç»

ä¸å¦æ¢å¾ï¼ä¸»è¦å¨å·¥å·é¾é¢åèèã

## Blogging

I have been busy creating posts, authoring a total of 31 blog posts
(including this one). 7 posts resonated on Hacker News, garnering over
50 points. (<https://news.ycombinator.com/from?site=maskray.me>).

I have also revised many posts initially written between 2020 and
2024.

Mastodon: [https://hachyderm.io/@meowray](https://hachyderm.io/%40meowray)

## GCC

I made 5 commits to the project, including the addition of the x86
inline asm constraint "Ws". you can read more about that in my earlier
post [Raw
symbol names in inline assembly](/blog/2024-01-30-raw-symbol-names-in-inline-assembly).

I believe that modernizing code review and test infrastructure will
enhance the contributor experience and attract more contributors.

## llvm-project

* [Reviewed
  numerous patches](https://github.com/llvm/llvm-project/pulls?q=sort%3Aupdated-desc+is%3Apr+created%3A%3E2024-01-01+reviewed-by%3AMaskRay). query
  `is:pr created:>2024-01-01 reviewed-by:MaskRay` => "989
  Closed"
* Official maintainer status on the MC layer and binary utilities
* My involvement with LLVM [18](/blog/2024-02-25-my-involvement-with-llvm-18) and [19](/blog/2024-08-18-my-involvement-with-llvm-19)

Key Points:

* TODO
* Added a script [update\_test\_body.py](https://llvm.org/docs/TestingGuide.html#elaborated-tests)
  to generate elaborated IR and assembly tests ([#89026](https://github.com/llvm/llvm-project/pull/89026))
* MC
  + Made some [MC
    and assembler improvements](/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19) in LLVM 19
  + Fixed some intrusive changes to the generic code due to AIX and
    z/OS.
  + Made llvm-mc better as an [assembler
    and disassembler](/blog/2024-12-22-simplifying-disassembly-with-llvm-tools)
* Light ELF
  + [Implemented
    a compact relocation format for ELF](/blog/2024-03-09-a-compact-relocation-format-for-elf)
* [AArch64
  mapping symbol size optimization](/blog/2024-07-21-mapping-symbols-rethinking-for-efficiency)
* Enabled StackSafetyAnalysis for AddressSanitizer to remove
  instrumentations on stack-allocated variables that are guaranteed to be
  safe from memory access bugs
  + Bail out if MemIntrinsic length is -1
  + Bail out when calling [ifunc](/blog/2021-01-18-gnu-indirect-function)
* Added the [Clang cc1 option
  `--output-asm-variant=`](https://github.com/llvm/llvm-project/pull/109360) and cleaned up internals of its
  friends (`x86-asm-syntax`).
* [`llvm/ADT/Hashing.h`
  stability](/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19#hashing)

### llvm/ADT/Hashing.h stability

To facilitate improvements, `llvm/ADT/Hashing.h` promised
to be non-deteriministic so that users could not depend on exact hash
values. However, the values were actually deterministic unless
`set_fixed_execution_hash_seed` was called. A lot of internal
code incorrectly relied on the stability of
`hash_value/hash_combine/hash_combine_range`. I have fixed
them and landed <https://github.com/llvm/llvm-project/pull/96282> to make
the hash value non-deteriministic in
`LLVM_ENABLE_ABI_BREAKING_CHECKS` builds.

### lld/ELF

lld/ELF is quite stable. I have made some maintenance changes. As
usual, I wrote the ELF port's release notes for the two releases. See [lld 18 ELF changes](/blog/2024-02-18-lld-18-elf-changes) and [lld 19 ELF changes](/blog/2024-08-04-lld-19-elf-changes) for
detail.

## Linux kernel

Contributed 4 commits.

## ccls

I finally removed support for LLVM 7, 8, and 9. The latest release <https://github.com/MaskRay/ccls/releases/tag/0.20241108>
has some nice features.

* didOpen: sort index requests. When you open A/B/foo.cc, files under
  "A/B/" and "A/" will be prioritized during the initial indexing process,
  leading to a quicker response time.
* Support for older these LLVM versions 7, 8, and 9 has been
  dropped.
* LSP semantic tokens are now supported. See usage guide
  https://maskray.me/blog/2024-10-20-ccls-and-lsp-semantic-tokens usage
  (including rainbow semantic highlighting)
* textDocument/switchSourceHeader (LSP extension) is now
  supported.

## Misc

Reported 12 feature requests or bugs to binutils.

* [`objdump -R: dump SHT_RELR relocations?`](https://sourceware.org/bugzilla/show_bug.cgi?id=32459)
* [`gas arm aarch64: missing mapping symbols $d in the absence of alignment directives`](https://sourceware.org/bugzilla/show_bug.cgi?id=32082)
* [`gas: Extend .loc directive to emit a label`](https://sourceware.org/bugzilla/show_bug.cgi?id=31955)
* [`Compressed .strtab and .symtab`](https://sourceware.org/bugzilla/show_bug.cgi?id=31884)
* [`gas: Support \+ in .rept/.irp/.irpc directives`](https://sourceware.org/bugzilla/show_bug.cgi?id=31752)
* [`ld: Add CLASS to allow separate section matching and referring`](https://sourceware.org/bugzilla/show_bug.cgi?id=31688)
* [`gas/ld: Implicit addends for non-code sections`](https://sourceware.org/bugzilla/show_bug.cgi?id=31567)
* [`binutils: Support CREL relocation format`](https://sourceware.org/bugzilla/show_bug.cgi?id=31475)
* [`ld arm: global/weak non-hidden symbols referenced by R_ARM_FUNCDESC are unnecessarily exported`](https://sourceware.org/bugzilla/show_bug.cgi?id=31409)
* [`ld arm: fdpic link segfaults on R_ARM_GOTOFFFUNCDESC referencing a hidden symbol`](https://sourceware.org/bugzilla/show_bug.cgi?id=31408)
* [`ld arm: fdpic link may have null pointer dereference in allocate_dynrelocs_for_symbol`](https://sourceware.org/bugzilla/show_bug.cgi?id=31407)
* [`objcopy: add --prefix-symbols-remove`](https://sourceware.org/bugzilla/show_bug.cgi?id=31292)

Reported 2 feature requests to glibc

* [`Feature request: special static-pie capable of loading the interpreter from a relative path`](https://sourceware.org/bugzilla/show_bug.cgi?id=31959)
* [`rtld: Support DT_CREL relocation format`](https://sourceware.org/bugzilla/show_bug.cgi?id=31541)

Share

* [summary](/blog/tags/summary/)

[**Newer**

Understanding and improving Clang -ftime-report](/blog/2025-01-12-understanding-and-improving-clang-ftime-report)
[**Older**

Skipping boring functions in debuggers](/blog/2024-12-30-skipping-boring-functions-in-debuggers)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tag...