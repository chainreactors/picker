---
title: lld 21 ELF changes
url: https://maskray.me/blog/2025-09-07-lld-21-elf-changes
source: MaskRay
date: 2025-09-08
fetch_date: 2025-10-02T19:48:25.092779
---

# lld 21 ELF changes

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-09-07](/blog/2025-09-07-lld-21-elf-changes)

# lld 21 ELF changes

LLVM 21.1 have been released. As usual, I maintain lld/ELF and have
added some notes to <https://github.com/llvm/llvm-project/blob/release/21.x/lld/docs/ReleaseNotes.rst>.
I've meticulously reviewed nearly all the patches that are not authored
by me. I'll delve into some of the key changes.

* Added `-z dynamic-undefined-weak` to make undefined weak
  symbols dynamic when the dynamic symbol table is present. ([#143831](https://github.com/llvm/llvm-project/pull/143831))
* For `-z undefs` (default for `-shared`),
  relocations referencing undefined strong symbols now behave like
  relocations referencing undefined weak symbols.
* `--why-live=<glob>` prints for each symbol matching
  `<glob>` a chain of items that kept it live during
  garbage collection. This is inspired by the Mach-O LLD feature of the
  same name.
* `--thinlto-distributor=` and
  `--thinlto-remote-compiler=` options are added to support
  Integrated Distributed ThinLTO. ([#142757](https://github.com/llvm/llvm-project/pull/142757))
* Linker script `OVERLAY` descriptions now support virtual
  memory regions (e.g. `>region`) and
  `NOCROSSREFS`.
* When the last `PT_LOAD` segment is executable and
  includes BSS sections, its `p_memsz` member is now correct.
  ([#139207](https://github.com/llvm/llvm-project/pull/139207))
* Spurious `ASSERT` errors before the layout converges are
  now fixed.
* For ARM and AArch64, `--xosegment` and
  `--no-xosegment` control whether to place executable-only and
  readable-executable sections in the same segment. The default option is
  `--no-xosegment`. ([#132412](https://github.com/llvm/llvm-project/pull/132412))
* For AArch64, added support for the `SHF_AARCH64_PURECODE`
  section flag, which indicates that the section only contains program
  code and no data. An output section will only have this flag set if all
  input sections also have it set. ([#125689](https://github.com/llvm/llvm-project/pull/125689), [#134798](https://github.com/llvm/llvm-project/pull/134798))
* For AArch64 and ARM, added `-zexecute-only-report`, which
  checks for missing `SHF_AARCH64_PURECODE` and
  `SHF_ARM_PURECODE` section flags on executable sections. ([#128883](https://github.com/llvm/llvm-project/pull/128883))
* For AArch64, `-z nopac-plt` has been added.
* For AArch64 and X86\_64, added `--branch-to-branch`, which
  rewrites branches that point to another branch instruction to instead
  branch directly to the target of the second instruction. Enabled by
  default at `-O2`.
* For AArch64, added support for `-zgcs-report-dynamic`,
  enabling checks for GNU GCS Attribute Flags in Dynamic Objects when GCS
  is enabled. Inherits value from `-zgcs-report` (capped at
  `warning` level) unless user-defined, ensuring compatibility
  with GNU ld linker.
* The default Hexagon architecture version in ELF object files
  produced by lld is changed to v68. This change is only effective when
  the version is not provided in the command line by the user and cannot
  be inferred from inputs.
* For LoongArch, the initial-exec to local-exec TLS optimization has
  been implemented.
* For LoongArch, several relaxation optimizations are supported,
  including relaxation for `R_LARCH_PCALA_HI20/LO12` and
  `R_LARCH_GOT_PC_HI20/LO12` relocations, instruction
  relaxation for `R_LARCH_CALL36`, TLS local-exec
  (`LE`)/global dynamic (`GD`)/ local dynamic
  (`LD`) model relaxation, and TLSDESC code sequence
  relaxation.
* For RISCV, an oscillation bug due to call relaxation is now fixed.
  ([#142899](https://github.com/llvm/llvm-project/pull/142899))
* For x86-64, the `.ltext` section is now placed before
  `.rodata`.

---

Link: [lld 20 ELF
changes](/blog/2025-02-02-lld-20-elf-changes)

Share

* [linker](/blog/tags/linker/)
* [llvm](/blog/tags/llvm/)

[**Newer**

Remarks on SFrame](/blog/2025-09-28-remarks-on-sframe)
[**Older**

Benchmarking compression programs](/blog/2025-08-31-benchmarking-compression-programs)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/) [hpc](/blog/tags/hpc/) [image](/blog/tags/image/) [inotify](/blog/tags/inotify/) [ipsec](/blog/tags/ipsec/) [irc](/blog/tags/irc/) [isc](/blog/tags/isc/) [j](/blog/tags/j/) [javascript](/blog/tags/javascript/) [josephus problem](/blog/tags/josephus-problem/) [jq](/blog/tags/jq/) [kernel](/blog/tags/kernel/) [kythe](/blog/tags/kythe/) [ld](/blog/tags/ld/) [leetcode](/blog/tags/leetcode/) [libunwind](/blog/tags/libunwind/) [linker](/blog/tags/linker/) [linux](/blog/tags/linux/) [lld](/blog/tags/lld/) [lldb](/blog/tags/lldb/) [llvm](/blog/tags/llvm/) [lsp](/blog/tags/lsp/) [m68k](/blog/tags/m68k/) [makefile](/blog/tags/makefile/) [math](/blog/tags/math/) [maze](/blog/tags/maze/) [mirror](/blog/tags/mirror/) [ml](/blog/tags/ml/) [musl](/blog/tags/musl/) [mutt](/blog/tags/mutt/) [n-body](/blog/tags/n-body/) [neovim](/blog/tags/neovim/) [network](/blog/tags/network/) [nginx](/blog/tags/nginx/) [nim](/blog/tags/nim/) [nlp](/blog/tags/nlp/) [node.js](/blog/tags/node-js/) [noip](/blog/tags/noip/) [notmuch](/blog/tags/notmuch/) [npm](/blog/tags/npm/) [ocaml](/blog/tags/ocaml/) [offlineimap](/blog/tags/offlineimap/) [oi](/blog/tags/oi/) [oj](/blog/tags/oj/) [openwrt](/blog/tags/openwrt/) [parallel](/blog/tags/parallel/) [parser generator](/blog/tags/parser-generator/) [perl](/blog/tags/perl/) [powerpc](/blog/tags/powerpc/) [presentation](/blog/tags/presentation/) [puzzle](/blog/tags/puzzle/) [python](/blog/tags/python/) [qq](/blog/tags/qq/) [radare2](/blog/tags/radare2/) [regex](/blog/tags/regex/) [regular expression](/blog/tags/regular-expression/) [reverse engineering](/blog/tags/reverse-engineering/) [review](/blog/tags/review/) [riscv](/blog/tags/riscv/) [router](/blog/tags/router/) [rtld](/blog/tags/rtld/) [ruby](/blog/tags/ruby/) [ructfe](/blog/tags/ructfe...