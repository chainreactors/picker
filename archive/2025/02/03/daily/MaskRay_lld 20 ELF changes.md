---
title: lld 20 ELF changes
url: https://maskray.me/blog/2025-02-02-lld-20-elf-changes
source: MaskRay
date: 2025-02-03
fetch_date: 2025-10-06T20:35:22.639635
---

# lld 20 ELF changes

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-02-02](/blog/2025-02-02-lld-20-elf-changes)

# lld 20 ELF changes

LLVM 20 will be released. As usual, I maintain lld/ELF and have added
some notes to <https://github.com/llvm/llvm-project/blob/release/20.x/lld/docs/ReleaseNotes.rst>.
I've meticulously reviewed nearly all the patches that are not authored
by me. I'll delve into some of the key changes.

* `-z nosectionheader` has been implemented to omit the
  section header table. The operation is similar to
  `llvm-objcopy --strip-sections`. ([#101286](https://github.com/llvm/llvm-project/pull/101286))
* `--randomize-section-padding=<seed>` is introduced
  to insert random padding between input sections and at the start of each
  segment. This can be used to control measurement bias in A/B
  experiments. ([#117653](https://github.com/llvm/llvm-project/pull/117653))
* The reproduce tarball created with `--reproduce=` now
  excludes directories specified in the `--dependency-file`
  argument (used by Ninja). This resolves an error where non-existent
  directories could cause issues when invoking
  `ld.lld @response.txt`.
* `--symbol-ordering-file=` and call graph profile can now
  be used together.
* When `--call-graph-ordering-file=` is specified,
  `.llvm.call-graph-profile` sections in relocatable files are
  no longer used.
* `--lto-basic-block-sections=labels` is deprecated in
  favor of `--lto-basic-block-address-map`. ([#110697](https://github.com/llvm/llvm-project/pull/110697))
* In non-relocatable links, a `.note.GNU-stack` section
  with the `SHF_EXECINSTR` flag is now rejected unless
  `-z execstack` is specified. ([#124068](https://github.com/llvm/llvm-project/pull/124068))
* In relocatable links, the `sh_entsize` member of a
  `SHF_MERGE` section with relocations is now respected in the
  output.
* Quoted names can now be used in output section phdr, memory region
  names, `OVERLAY`, the LHS of `--defsym`, and
  `INSERT AFTER`.
* Section `CLASS` linker script syntax binds input sections
  to named classes, which are referenced later one or more times. This
  provides access to the automatic spilling mechanism of
  `--enable-non-contiguous-regions` without globally changing
  the semantics of section matching. It also independently increases the
  expressive power of linker scripts. ([#95323](https://github.com/llvm/llvm-project/pull/95323))
* `INCLUDE` cycle detection has been fixed. A linker script
  can now be included twice.
* The `archivename:` syntax when matching input sections is
  now supported. ([#119293](https://github.com/llvm/llvm-project/pull/119293))
* To support Arm v6-M, short thunks using B.w are no longer generated.
  ([#118111](https://github.com/llvm/llvm-project/pull/118111))
* For AArch64, BTI-aware long branch thunks can now be created to a
  destination function without a BTI instruction. ([#108989](https://github.com/llvm/llvm-project/pull/108989)) ([#116402](https://github.com/llvm/llvm-project/pull/116402))
* Relocations related to GOT and TLSDESC for the AArch64 Pointer
  Authentication ABI are now supported.
* Supported relocation types for x86-64 target:
  + `R_X86_64_CODE_4_GOTPCRELX` ([#109783](https://github.com/llvm/llvm-project/pull/109783)) ([#116737](https://github.com/llvm/llvm-project/pull/116737))
  + `R_X86_64_CODE_4_GOTTPOFF` ([#116634](https://github.com/llvm/llvm-project/pull/116634))
  + `R_X86_64_CODE_4_GOTPC32_TLSDESC` ([#116909](https://github.com/llvm/llvm-project/pull/116909))
  + `R_X86_64_CODE_6_GOTTPOFF` ([#117675](https://github.com/llvm/llvm-project/pull/117675))
* Supported relocation types for LoongArch target:
  `R_LARCH_TLS_{LD,GD,DESC}_PCREL20_S2`. ([#100105](https://github.com/llvm/llvm-project/pull/100105))

## Linker scripts

The `CLASS` keyword, which separates section matching and
referring, is a noteworthy new feature to the linker script support.
Here is the GNU ld [feature
request](https://sourceware.org/bugzilla/show_bug.cgi?id=31688).

## Section layout

If `--symbol-ordering-file=` is specified,
`--symbol-ordering-file=` specified sections are placed
first. In LLD 20, `SHT_LLVM_CALL_GRAPH_PROFILE` sections in
relocatable files are still used for other sections.

The next release will support options
`--bp-compression-sort=both` and
`--bp-startup-sort=function --irpgo-profile=a.profdata` that
improves Lempel-Ziv compression and reduces page faults during program
startup for mobile applications.

## `.dynsym` computation

The purpose of `Symbol::includeInDynsym` was somewhat
ambiguous, as it was used both to determine if a symbol should be
exported to `.dynsym` and to conservatively suppress
transformations in other contexts like MarkLive and ICF. LLD 20
clarifies this by introducing `Symbol::isExported`
specifically for indicating whether a defined symbol should be exported.
All previous uses of `Symbol::includeInDynsym` have been
updated to use `Symbol::isExported` instead. The old
confusing `Symbol::exportDynamic` has been removed.

A special case within `Symbol::includeInDynsym` checked
for `isUndefWeak() && ctx.arg.noDynamicLinker`. (This
could be generalized to
`isUndefined() && ctx.arg.noDynamicLinker`, as
non-weak undefined symbols led to errors. Nonetheless,
`noDynamicLinker` has been removed to improve consistency.)
This condition ensures that undefined symbols are not included in
`.dynsym` for statically linked `ET_DYN`
executables (created with `clang -static-pie`).

This condition has been generalized in LLD 20 to
`(ctx.arg.shared || !ctx.sharedFiles.empty()) && (sym->isUndefined() || sym->isExported)`.
This means undefined symbols are excluded from `.dynsym` in
both `ld.lld -pie a.o` and
`ld.lld -pie --no-dynamic-linker a.o`, but not
`ld.lld -pie a.o b.so`. This change brings LLD's behavior
more in line with GNU ld.

`Symbol::isPreemptible`, indicating whether a symbol could
be bound to another component, was calculated before relocation scanning
and, in LLD 19, also during Identical Code Folding (ICF). In LLD 20, the
ICF-related calculation has been moved to the symbol versioning parsing
stage.

In LLD 20, `isExported` and `isPreemptible` are
computed in the following passes.

* Scan input files, interleaved with symbol resolution: set
  `isExported` when defined or referenced by shared
  objects
* Clear `isExported` if influenced by
  `--exclude-libs`
* `parseVersionAndComputeIsPreemptible`
  + Clear `isExported` if localized due to hidden
    visibility.
  + For undefined symbols, compute `isPreemptible`
  + For defined symbols in relocatable files, or bitcode files when
    `!ltoCanOmit`, set `isExported` and compute
    `isPreemptible`
* `compileBitcodeFiles`
* Scan LTO compiled relocatable files
* Clear `isExported` if influenced by
  `--exclude-libs`
* `finalizeSections`: recompute
  `isPreemptible`
* `isPreemptible` and `isExported` determine
  whether a symbol should be exported to `.dynsym`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` for (Symbol *sym : ctx.symtab->getSymbols()) {   if (!sym->isUsedInRegularObj || !includeInSymtab(ctx, *sym))     continue;   if (!ctx.arg.relocatable)     sym->binding = sym->computeBinding(ctx);   if (ctx.in.symTab)     ctx.in.symTab->addSymbol(sym);    // computeBinding might localize a linker-synthesized hidden symbol   // that was considered exported.   if ((sym->isExported || sym->isPreemptible) && !sym->isLocal()) {     ctx.partitions[sym->partition - 1].dynSymTab->addSymbol(sym);     if (auto *file = dyn_cast<SharedFile>(sym->file))       if (file->isNeeded && !sym->isUndefined())         addVerneed(ctx, *sym);   } } ``` |

---

Link: [lld 19 ELF
changes](/blog/2024-08-04-lld-19-elf-changes)

Share

* [linker](/blog/tags/linker/)
* [llvm]...