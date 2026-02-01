---
title: lld 22 ELF changes
url: https://maskray.me/blog/2026-01-31-lld-22-elf-changes
source: MaskRay
date: 2026-01-31
fetch_date: 2026-02-01T04:26:32.691178
---

# lld 22 ELF changes

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-01-31](/blog/2026-01-31-lld-22-elf-changes)

# lld 22 ELF changes

LLVM 22 will be released. As usual, I maintain lld/ELF and have added
some notes to <https://github.com/llvm/llvm-project/blob/release/22.x/lld/docs/ReleaseNotes.rst>.
I've meticulously reviewed nearly all the patches that are not authored
by me. I'll delve into some of the key changes.

* `--print-gc-sections=<file>` has been added to
  redirect garbage collection section listing to a file, avoiding
  contamination of stdout with other linker output. ([#159706](https://github.com/llvm/llvm-project/pull/159706))
* A `VersionNode` lexer state has been added for better
  version script parsing. This brings the lexer behavior closer to GNU ld.
  ([#174530](https://github.com/llvm/llvm-project/pull/174530))
* Unversioned undefined symbols now use version index 0, aligning with
  GNU ld 2.46 behavior. ([#168189](https://github.com/llvm/llvm-project/pull/168189))
* `.data.rel.ro.hot` and `.data.rel.ro.unlikely`
  are now recognized as RELRO sections, allowing profile-guided static
  data partitioning. ([#148920](https://github.com/llvm/llvm-project/pull/148920))
* DTLTO now supports archive members and bitcode members of thin
  archives. ([#157043](https://github.com/llvm/llvm-project/pull/157043))
* For DTLTO,
  `--thinlto-remote-compiler-prepend-arg=<arg>` has been
  added to prepend an argument to the remote compiler's command line. ([#162456](https://github.com/llvm/llvm-project/pull/162456))
* Balanced Partitioning (BP) section ordering now skips input sections
  with null data, and filters out section symbols. ([#149265](https://github.com/llvm/llvm-project/pull/149265)) ([#151685](https://github.com/llvm/llvm-project/pull/151685))
* For AArch64, fixed a crash when using
  `--fix-cortex-a53-843419` with synthetic sections and
  improved handling when patched code is far from the short jump. ([#170495](https://github.com/llvm/llvm-project/pull/170495))
* For AArch64, added support for the `R_AARCH64_FUNCINIT64`
  dynamic relocation type for relocating word-sized data using the return
  value of a function. ([#156564](https://github.com/llvm/llvm-project/pull/156564))
* For AArch64, added support for the `R_AARCH64_PATCHINST`
  relocation type to support deactivation symbols. ([#133534](https://github.com/llvm/llvm-project/pull/133534))
* For AArch64, added support for reading AArch64 Build Attributes and
  converting them into GNU Properties. ([#147970](https://github.com/llvm/llvm-project/pull/147970))
* For ARM, fixed incorrect veneer generation for wraparound branches
  at the high end of the 32-bit address space branching to the low end.
  ([#165263](https://github.com/llvm/llvm-project/pull/165263))
* For LoongArch, `-r` now synthesizes
  `R_LARCH_ALIGN` at input section start to preserve alignment
  information. ([#153935](https://github.com/llvm/llvm-project/pull/153935))
* For LoongArch, added relocation types for LA32R/LA32S. ([#172618](https://github.com/llvm/llvm-project/pull/172618)) ([#176312](https://github.com/llvm/llvm-project/pull/176312))
* For RISC-V, added infrastructure for handling vendor-specific
  relocations. ([#159987](https://github.com/llvm/llvm-project/pull/159987))
* For RISC-V, added support for statically resolved vendor-specific
  relocations. ([#169273](https://github.com/llvm/llvm-project/pull/169273))
* For RISC-V, `-r` now synthesizes
  `R_RISCV_ALIGN` at input section start to preserve alignment
  information during two-stage linking. ([#151639](https://github.com/llvm/llvm-project/pull/151639))

---

Link: [lld 21 ELF
changes](/blog/2025-09-07-lld-21-elf-changes)

Share

* [linker](/blog/tags/linker/)
* [llvm](/blog/tags/llvm/)

[**Older**

Long branches in compilers, assemblers, and linkers](/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [git](/blog/tags/git/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/) [hpc](/blog/tags/hpc/) [image](/blog/tags/image/) [inotify](/blog/tags/inotify/) [ipsec](/blog/tags/ipsec/) [irc](/blog/tags/irc/) [isc](/blog/tags/isc/) [j](/blog/tags/j/) [javascript](/blog/tags/javascript/) [josephus problem](/blog/tags/josephus-problem/) [jq](/blog/tags/jq/) [kernel](/blog/tags/kernel/) [kythe](/blog/tags/kythe/) [ld](/blog/tags/ld/) [leetcode](/blog/tags/leetcode/) [libunwind](/blog/tags/libunwind/) [linker](/blog/tags/linker/) [linux](/blog/tags/linux/) [lld](/blog/tags/lld/) [lldb](/blog/tags/lldb/) [llvm](/blog/tags/llvm/) [lsp](/blog/tags/lsp/) [m68k](/blog/tags/m68k/) [makefile](/blog/tags/makefile/) [math](/blog/tags/math/) [maze](/blog/tags/maze/) [mirror](/blog/tags/mirror/) [ml](/blog/tags/ml/) [musl](/blog/tags/musl/) [mutt](/blog/tags/mutt/) [n-body](/blog/tags/n-body/) [neovim](/blog/tags/neovim/) [network](/blog/tags/network/) [nginx](/blog/tags/nginx/) [nim](/blog/tags/nim/) [nlp](/blog/tags/nlp/) [node.js](/blog/tags/node-js/) [noip](/blog/tags/noip/) [notmuch](/blog/tags/notmuch/) [npm](/blog/tags/npm/) [ocaml](/blog/tags/ocaml/) [offlineimap](/blog/tags/offlineimap/) [oi](/blog/tags/oi/) [oj](/blog/tags/oj/) [openwrt](/blog/tags/openwrt/) [parallel](/blog/tags/parallel/) [parser generator](/blog/tags/parser-generator/) [perl](/blog/tags/perl/) [powerpc](/blog/tags/powerpc/) [presentation](/blog/tags/presentation/) [puzzle](/blog/tags/puzzle/) [python](/blog/tags/python/) [qq](/blog/tags/qq/) [radare2](/blog/tags/radare2/) [regex](/blog/tags/regex/) [regular expression](/blog/tags/regular-expression/) [reverse engineering](/blog/tags/reverse-engineering/) [review](/blog/tags/review/) [riscv](/blog/tags/riscv/) [router](/blog/tags/router/) [rtld](/blog/tags/rtld/) [ruby](/blog/tags/ruby/) [ructfe](/blog/tags/ructfe/) [s390x](/blog/tags/s390x/) [sanitizer](/blog/tags/sanitizer/) [scheme](/blog/tags/scheme/) [search](/blog/tags/search/) [security](/blog/tags/security/...