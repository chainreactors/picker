---
title: lld 19 ELF changes
url: https://maskray.me/blog/2024-08-04-lld-19-elf-changes
source: MaskRay
date: 2024-08-05
fetch_date: 2025-10-06T18:00:33.498623
---

# lld 19 ELF changes

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-08-04](/blog/2024-08-04-lld-19-elf-changes)

# lld 19 ELF changes

LLVM 19 will be released. As usual, I maintain lld/ELF and have added
some notes to <https://github.com/llvm/llvm-project/blob/release/19.x/lld/docs/ReleaseNotes.rst>.
I've meticulously reviewed nearly all the patches that are not authored
by me. I'll delve into some of the key changes.

* Experimental CREL relocations with explicit addends are now
  supported using the temporary section type code 0x40000020
  (`clang -c -Wa,--crel,--allow-experimental-crel`). LLVM will
  change the code and break compatibility (Clang and lld of different
  versions are not guaranteed to cooperate, unlike other features). CREL
  with implicit addends are not supported. ([#98115](https://github.com/llvm/llvm-project/pull/98115))
* `EI_OSABI` in the output is now inferred from input
  object files. ([#97144](https://github.com/llvm/llvm-project/pull/97144))
* `--compress-sections <section-glib>={none,zlib,zstd}[:level]`
  is added to compress matched output sections without the
  `SHF_ALLOC` flag. ([#84855](https://github.com/llvm/llvm-project/pull/84855)) ([#90567](https://github.com/llvm/llvm-project/pull/90567))
* The default compression level for zlib is now independent of linker
  optimization level (`Z_BEST_SPEED`).
* zstd compression parallelism no longer requires
  `ZSTD_MULITHREAD` build.
* `GNU_PROPERTY_AARCH64_FEATURE_PAUTH` notes,
  `R_AARCH64_AUTH_ABS64` and
  `R_AARCH64_AUTH_RELATIVE` relocations are now supported. ([#72714](https://github.com/llvm/llvm-project/pull/72714))
* `--no-allow-shlib-undefined` now rejects non-exported
  definitions in the `def-hidden.so ref.so` case. ([#86777](https://github.com/llvm/llvm-project/issues/86777))
* `--debug-names` is added to create a merged
  `.debug_names` index from input `.debug_names`
  sections. Type units are not handled yet. ([#86508](https://github.com/llvm/llvm-project/pull/86508))
* `--enable-non-contiguous-regions` option allows
  automatically packing input sections into memory regions by
  automatically spilling to later matches if a region would overflow. This
  reduces the toil of manually packing regions (typical for embedded). It
  also makes full LTO feasible in such cases, since IR merging currently
  prevents the linker script from referring to input files. ([#90007](https://github.com/llvm/llvm-project/pull/90007))
* `--default-script`/`-dT` is implemented to
  specify a default script that is processed if
  `--script`/`-T` is not specified. ([#89327](https://github.com/llvm/llvm-project/pull/89327))
* `--force-group-allocation` is implemented to discard
  `SHT_GROUP` sections and combine relocation sections if their
  relocated section group members are placed to the same output section.
  ([#94704](https://github.com/llvm/llvm-project/pull/94704))
* `--build-id` now defaults to generating a 20-byte digest
  ("sha1") instead of 8-byte ("fast"). This improves compatibility with
  RPM packaging tools. ([#93943](https://github.com/llvm/llvm-project/pull/93943))
* `-z lrodata-after-bss` is implemented to place
  `.lrodata` after `.bss`. ([#81224](https://github.com/llvm/llvm-project/pull/81224))
* `--export-dynamic` no longer creates dynamic sections for
  `-no-pie` static linking.
* `--lto-emit-asm` is now added as the canonical spelling
  of `--plugin-opt=emit-llvm`.
* `--lto-emit-llvm` now uses the pre-codegen module. ([#97480](https://github.com/llvm/llvm-project/pull/97480))
* When AArch64 PAuth is enabled, `-z pack-relative-relocs`
  now encodes `R_AARCH64_AUTH_RELATIVE` relocations in
  `.rela.auth.dyn`. ([#96496](https://github.com/llvm/llvm-project/pull/96496))
* `-z gcs` and `-z gcs-report` are now supported
  for AArch64 Guarded Control Stack extension.
* `-r` now forces `-Bstatic`.
* Thumb2 PLT is now supported for Cortex-M processors. ([#93644](https://github.com/llvm/llvm-project/pull/93644))
* `DW_EH_sdata4` of addresses larger than 0x80000000 is now
  supported for MIPS32. ([#92438](https://github.com/llvm/llvm-project/pull/92438))
* Certain unknown section types are rejected. ([#85173](https://github.com/llvm/llvm-project/pull/85173))
* `PROVIDE(lhs = rhs) PROVIDE(rhs = ...)`, `lhs`
  is now defined only if `rhs` is needed. ([#74771](https://github.com/llvm/llvm-project/issues/74771)) ([#87530](https://github.com/llvm/llvm-project/pull/87530))
* `OUTPUT_FORMAT(binary)` is now supported. ([#98837](https://github.com/llvm/llvm-project/pull/98837))
* `NOCROSSREFS` and `NOCRFOSSREFS_TO` commands
  now supported to prohibit cross references between certain output
  sections. ([#98773](https://github.com/llvm/llvm-project/pull/98773))
* Orphan placement is refined to prefer the last similar section when
  its rank <= orphan's rank. ([#94099](https://github.com/llvm/llvm-project/pull/94099))
  Non-alloc orphan sections are now placed at the end. ([#94519](https://github.com/llvm/llvm-project/pull/94519))
* `R_X86_64_REX_GOTPCRELX` of the addq form is no longer
  incorrectly optimized when the address is larger than 0x80000000.

## CREL

I've developed CREL (compact relocations) to reduce relocatable file
tremendously for LLVM 19. LLD now supports CREL with explicit addends.
Clang and lld of different versions are not guaranteed to cooperate,
unlike other features.

See [Integrated
assembler improvements in LLVM 19](/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19) for details.

## `--compress-sections`

The `--compress-sections` option has been enhanced. You
can choose between zlib and zstd for compression, along with specifying
the desired compression level. Looking ahead, zlib is deprecated in
favor of zstd. While zstd offers additional tuning options, we only
provide the compression level.

My [Compressed
arbitrary sections](https://maskray.me/blog/2023-07-07-compressed-arbitrary-sections) has analyzed potential use cases.

## Orphan sections

My [Understanding
orphan sections](/blog/2024-06-02-understanding-orphan-sections) explains the changes in detail.

## Linker scripts

There are quite a few enhancements to the linker script support.
`NOCROSSREFS` and
`--enable-non-contiguous-regions` are noteworthy new
features. There is now an increasing demand of features for embedded
programming.

The world of embedded programming is a fascinating mix of open and
closed ecosystems. Developers of proprietary hardware and closed-source
software are increasingly interested in migrating their toolchains to
the LLVM Linker (LLD). The allure of faster link speeds, a clean
codebase, and seamless LTO integration is undeniable. However, as LLD's
maintainer, I must tread carefully. While accommodating these users is
nice for LLD's growth, incorporating custom linker extensions risks
compromising the project's code quality and maintainability. Striking
the right balance between flexibility and code integrity is essential to
ensure LLD remains a robust and efficient linker for a wide range of
users.

GNU ld also supports extensions for embedded programming. I
categorize these extensions into two groups: mature and experimental.
Many of the established extensions exhibit well-defined semantics and
have been incorporated into LLD. However, some newer extensions in GNU
ld appear less thoughtfully designed and inflexible.

When considering a specific extension, we should prioritize practical
needs over arbitrary adherence to GNU ld's implementation. If compelling
reasons justify a particular feature and GNU ld's approach proves
restrictive, we should feel empowered to innovate within LLD.

Conversely, when developing new extensions, it's essential to engage
with the broader community. I often submit feature requests to GNU ld to
inform decisi...