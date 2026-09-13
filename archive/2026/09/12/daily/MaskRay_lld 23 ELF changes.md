---
title: lld 23 ELF changes
url: https://maskray.me/blog/lld-23-elf-changes
source: MaskRay
date: 2026-09-12
fetch_date: 2026-09-13T07:01:26.870010
---

# lld 23 ELF changes

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-09-12](/blog/lld-23-elf-changes)

# lld 23 ELF changes

LLVM 23.1 has been released. As usual, I maintain lld/ELF and as
volunteer work have added some notes to <https://github.com/llvm/llvm-project/blob/release/23.x/lld/docs/ReleaseNotes.rst>.

Like last time, I used Claude Code to summarize
`git log llvmorg-23-init..origin/release/23.x -- lld/ELF`,
excluding changes cherry-picked into 22.x
(`git rev-list llvmorg-23-init..llvmorg-22.1.8 -- lld`), and
then edited the draft.

This was a busy cycle: 141 commits landed in lld/ELF between the
branch point (2026-01-13) and 23.1.0-rc1 (2026-07-16), compared with 72
in the 22 cycle. Much of the increase is performance work, which I
described in [Recent
lld/ELF performance improvements](/blog/2026-04-12-recent-lld-elf-performance-improvements). lld 23 is the first release that
ships all of it.

* Input file loading is now parallelized, meaningfully reducing link
  time for large links. ([#191690](https://github.com/llvm/llvm-project/pull/191690))
* `--gc-sections` mark phase is now parallelized. ([#189321](https://github.com/llvm/llvm-project/pull/189321))
* Relocation scanning was rewritten as target-specific scanners for
  all targets with shared library support, devirtualizing the hot
  relocation-classification path.
* Added
  `--bp-compression-sort-section=<glob>[=<layout_priority>[=<match_priority>]]`,
  replacing the old coarse `--bp-compression-sort` modes with a
  way to split input sections into multiple compression groups, run
  balanced partitioning independently per group, and leave out sections
  that are poor candidates for BP. ([#185661](https://github.com/llvm/llvm-project/pull/185661))
* Added `-z memtag-{mode,heap,stack}` as generic
  replacements for the Android-specific `--android-memtag-*`
  flags; `--android-memtag-note` keeps the Android-specific
  memtag note opt-in. ([#188205](https://github.com/llvm/llvm-project/pull/188205))
* Unused space in executable output sections is now filled with trap
  instructions, primarily for `-z separate-code` mode. ([#176845](https://github.com/llvm/llvm-project/pull/176845))
* `.eh_frame_hdr` now supports the
  `DW_EH_PE_sdata8` encoding, auto-upgrading from
  `sdata4` when a table entry or the frame pointer exceeds the
  32-bit range, instead of erroring out for large executables. ([#179089](https://github.com/llvm/llvm-project/pull/179089))
* `vna_flags` is now set to `VER_FLG_WEAK` when
  all undefined references to a version are weak, allowing glibc's dynamic
  loader to warn instead of error when the version is missing at runtime.
  ([#176673](https://github.com/llvm/llvm-project/pull/176673))
* `.ltext.*` input sections are now merged into a single
  `.ltext` output section, matching the existing
  `.ldata.*`/`.lrodata.*`/`.lbss.*`
  handling for the large code model with `-ffunction-sections`.
  ([#190305](https://github.com/llvm/llvm-project/pull/190305))
* `.gnu.build.attributes.*` input sections are now
  concatenated into one output section, matching GNU ld. ([#208737](https://github.com/llvm/llvm-project/pull/208737))
* `.tbss` output sections may now use an explicit address
  expression; previously it was silently overridden to follow the
  preceding `.tbss`. ([#196447](https://github.com/llvm/llvm-project/pull/196447))
* `--discard-locals`/`--discard-all` combined
  with `-r`/`--emit-relocs` no longer discard local
  symbols that are referenced only from retained
  non-`SHF_ALLOC` sections (e.g. `.L` symbols
  referenced by `.debug_info`), fixing DWARF corruption in the
  output. ([#209035](https://github.com/llvm/llvm-project/pull/209035)) ([#209042](https://github.com/llvm/llvm-project/pull/209042))
* `--retain-symbols-file` now filters `.symtab`
  instead of `.dynsym`, matching GNU ld. ([#209063](https://github.com/llvm/llvm-project/pull/209063))
* When `-o` is `-`, the output is written to the
  `lld::outs()` stream instead of the process's stdout, so that
  library users can capture it. ([#209064](https://github.com/llvm/llvm-project/pull/209064))
* `INCLUDE` in linker scripts now fully parses its own
  content instead of sharing a lexer buffer stack with the includer,
  fixing spurious acceptance of malformed scripts. ([#193427](https://github.com/llvm/llvm-project/pull/193427))
* The `OVERLAY` linker script command now accepts any
  output-section-command (e.g. symbol assignments), not just input section
  descriptions. ([#203524](https://github.com/llvm/llvm-project/pull/203524))
* Thunks are no longer reused across an `OVERLAY` boundary
  unless the target output section is guaranteed to be resident at the
  same time. ([#200415](https://github.com/llvm/llvm-project/pull/200415))
* When a `SECTIONS` command interleaves relro and non-relro
  sections, lld now emits one `PT_GNU_RELRO` segment per
  contiguous run of relro sections instead of reporting a
  `not contiguous with other relro sections` error. ([#203675](https://github.com/llvm/llvm-project/pull/203675))
* `SHT_NOBITS` sections are now excluded from LMA overlap
  checks, matching GNU ld and allowing e.g. a startup section to share an
  LMA with `.bss` in embedded linker scripts. ([#196423](https://github.com/llvm/llvm-project/pull/196423))
* LTO: the middle-end no longer emits new references to, or
  internalizes, symbols defined in bitcode after the extracted-bitcode set
  has been fixed, preventing undefined symbol references from transforms
  that run after linking has determined which bitcode files to extract.
  ([#164916](https://github.com/llvm/llvm-project/pull/164916))
* DTLTO: significantly improved the performance of adding backend
  output files to the link, especially on Windows. ([#186366](https://github.com/llvm/llvm-project/pull/186366))
* For AArch64, fixed `.relr.auth.dyn` ->
  `.rela.dyn` movement to properly adjust
  `__rela_iplt_start`/`__rela_iplt_end` and size the
  `.dynamic` section for both tags. ([#195649](https://github.com/llvm/llvm-project/pull/195649))
* For AArch64, handle Memtag globals for
  `R_AARCH64_AUTH_ABS64`. ([#173291](https://github.com/llvm/llvm-project/pull/173291))
* For AArch64, fixed TLS GD against non-preemptible dynamic symbols
  (e.g. `protected` or `-Bsymbolic`) in DSOs, which
  previously produced an inconsistent GOT entry and spurious preemption.
  ([#207881](https://github.com/llvm/llvm-project/pull/207881))
* For AArch64, `adrp`+`ldr` GOT relaxation is
  now decided per-symbol, all-or-nothing, avoiding invalid relaxation when
  a branch target sits between the `adrp` and `ldr`
  of a pair. ([#208396](https://github.com/llvm/llvm-project/pull/208396))
* For AArch64, a redundant local-exec TLS `add` with a zero
  high-12-bits immediate is now relaxed to a `nop`. ([#204286](https://github.com/llvm/llvm-project/pull/204286))
* For AArch64, `-z bti-report=none` and
  `-z gcs-report=none` now silence the warnings implied by
  `-z force-bti` and `-z gcs=always`. ([#186343](https://github.com/llvm/llvm-project/pull/186343))
* For Hexagon, fixed out-of-range PLT branch thunks and TLS GD PLT
  entry creation. ([#186545](https://github.com/llvm/llvm-project/pull/186545)) ([#180297](https://github.com/llvm/llvm-project/pull/180297))
* For LoongArch, fixed range checking of
  `R_LARCH_*_PCADD_HI20` relocations on 64-bit and DTPREL
  relocations in debug sections. ([#183233](https://github.com/llvm/llvm-project/pull/183233)) ([#199327](https://github.com/llvm/llvm-project/pull/199327))
* For MIPS, fixed the addend for preemptible static TLS. ([#150729](https://github.com/llvm/llvm-project/pull/150729))
* For x86-64, CFI jump table relaxation reduces the runtime overhead
  of indirect calls under Control Flow Integrity by opportunistically
  mov...