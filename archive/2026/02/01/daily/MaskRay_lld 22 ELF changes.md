---
title: lld 22 ELF changes
url: https://maskray.me/blog/2026-02-01-lld-22-elf-changes
source: MaskRay
date: 2026-02-01
fetch_date: 2026-02-02T04:15:47.907190
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

[2026-02-01](/blog/2026-02-01-lld-22-elf-changes)

# lld 22 ELF changes

For those unfamiliar, [lld](https://lld.llvm.org/) is the
LLVM linker, supporting PE/COFF, ELF, Mach-O, and WebAssembly ports.
These object file formats differ significantly, and each port must
follow the conventions of the platform's system linker. As a result, the
ports share limited code (diagnostics, memory allocation, etc) and have
largely separate reviewer groups.

With LLVM 22.1 releasing soon, I've added some notes to the <https://github.com/llvm/llvm-project/blob/release/22.x/lld/docs/ReleaseNotes.rst>
as an lld/ELF maintainer. As usual, I've reviewed almost all the patches
not authored by me.

For the first time, I used an LLM agent (Claude Code) to help look
through commits
(`git log release/21.x..release/22.x -- lld/ELF`) and draft
the release notes. Despite my request to only read lld/ELF changes,
Claude Code also crafted notes for other ports, which I retained since
their release notes had been quite sparse for several releases. Changes
back ported to the 21.x release are removed
(`git log --oneline llvmorg-22-init..llvmorg-21.1.8 -- lld`).

I'll delve into some of the key changes.

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
  This is an interesting [relocatable
  linking challenge](/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation#:~:text=relocatable%20linking%20challenge) for linker relaxation.

Besides me, Peter Smith (smithp35) and Jessica Clarke (jrtc27) have
done a lot of reviews.

jrtc27 has done great work simplifying the dynamic relocation system,
which is highly appreciated.

I should call out <https://github.com/llvm/llvm-project/pull/172618>: for
this relatively large addition, the author and approver are from the
same company and contributing to their architecture, and neither the
author nor the approver is a regular lld contributor/reviewer. The
author did not request review from regular reviewers and landed the
patch just 3 minutes after their colleague's approval. I left a comment
asking to keep the PR open for other maintainers to review.

## Distributed ThinLTO

[Distributed ThinLTO
(DTLTO)](https://llvm.org/docs/DTLTO.html) enables distributing ThinLTO backend compilations to
external systems (e.g., Incredibuild, distcc-like tools) during the link
step. This feature was contributed by PlayStation, who had offered it as
a proprietary technology before upstreaming.

The traditional distributed ThinLTO is implemented in Bazel in buck2.
**Bazel-style distribution** (build system orchestrated)
uses a multi-step workflow:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # Compile to bitcode (made parallel by build system) clang -c -O2 -flto=thin a.c b.c # Thin link clang -flto=thin -fuse-ld=lld -Wl,--thinlto-index-only=a.rsp,--thinlto-emit-imports-files -Wl,--thinlto-prefix-replace=';lto/' a.o b.o # Backend compilation (distributed by build system) with dynamic dependencies clang -c -O2 -fthinlto-index=lto/a.o.thinlto.bc a.o -o lto/a.o clang -c -O2 -fthinlto-index=lto/b.o.thinlto.bc b.o -o lto/b.o # Final native link clang -fuse-ld=lld @a.rsp   # a.rsp contains lto/a.o and lto/b.o ``` |

The build system sees the index files from step 2 as outputs and
schedules step 3 jobs across the build cluster. This requires a build
system that handles **dynamic dependencies**âoutputs of
step 2 determine inputs to step 3.

**DTLTO** (linker orchestrated) integrates steps 2-4
into a single link invocation:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` clang -flto=thin -c a.c b.c clang -flto=thin -fuse-ld=lld -fthinlto-distributor=<distributor> *.o ``` |

LLD performs the thin-link internally, generates a JSON job
description for each backend compilation, invokes the distributor
process, waits for native objects, and links them. The distributor is
responsible for farming out the compilations to remote machines.

DTLTO works with any build system but requires a separate distributor
process that speaks its JSON protocol. DTLTO is essentially "ThinLTO
distribution for projects that don't use Bazel".

## Pointer Field Protection

`R_AARCH64_PATCHINST` is a static relocation type used
with Pointer Field Protection (PFP), which leverages Armv8.3-A Pointer
Authentication (PAC) to protect pointer fields in structs.

Consider the following C++ code:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` struct cls {   ~cls();   long *ptr; private:   long *ptr2; };  long *load(cls *c) { return c->ptr; } void store(cls *c, long *ptr) { c->ptr = ptr; } ``` |

With Pointer Field Prot...