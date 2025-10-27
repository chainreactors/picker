---
title: 2022年总结
url: https://maskray.me/blog/2022-12-31-summary
source: MaskRay
date: 2023-01-01
fetch_date: 2025-10-04T02:50:37.824420
---

# 2022年总结

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2022-12-31](/blog/2022-12-31-summary)

# 2022氓鹿麓忙聙禄莽禄聯

盲赂聙氓娄聜忙聴垄氓戮聙茂录聦盲赂禄猫娄聛氓聹篓氓路楼氓聟路茅聯戮茅垄聠氓聼聼猫聙聲猫聙聵茫聙聜莽禄聶猫驴聶盲潞聸high-profile
OSS猫麓隆莽聦庐莽職聞忙聴露氓聙聶茂录聦氓赂聦忙聹聸茅聙聫猫驴聡猫驴聶盲赂陋氓戮庐氓掳聫莽職聞猫搂聮氓潞娄忙聰鹿氓聫聵盲赂聳莽聲聦茫聙聜

## Highlights

* RELR relative relocation format (glibc, musl, DynamoRIO)
* zstd compressed debug sections (binutils, gdb, clang, lld/ELF,
  lldb)
* lld/ELF (huge performance improvement, RISC-V linker relaxation,
  `SHT_RISCV_ATTRIBUTES`)
* Clang built glibc (get the ball rolling)
* Make protected symbols work in binutils/glibc
* Involved in sanitizers, ThinLTO, AArch64/x86 hardening features,
  AArch64 Memtag ABI, RISC-V psABI, etc

### RELR relative relocation format

* (In 2021-10, upstreamed `DT_RELR` patch to FreeBSD
  rtld-elf)
* In April, upstreamed `DT_RELR` patch to glibc
  (highlighted feature for the 2.36 release)
* In August, upstreamed `DT_RELR` patch to musl (milestone:
  1.2.4)
* Upstreamed `DT_RELR` patch to DynamoRIO
* Contributed an unmerged gold patch

[Relative
relocations and RELR](https://maskray.me/blog/2021-10-31-relative-relocations-and-relr)

Carlos O'Donell [said](https://twitter.com/CarlosODonell/status/1554523273085566982):

> It's exactly that, .rela.dyn is 30x larger than .rela.plt in glibc. I
> applaud Fangrui Song's efforts here to move DT\_RELR forward. If you're
> going to do one thing that has high impact and move *multiple*
> communities forward then picking .rela.dyn is the section to pick.

### zstd compressed debug sections

* Added zstd support to gas, ld.bfd, gold, gdb, objcopy, readelf,
  objdump, addr2line, etc
* Added zstd support to clang, ld.lld, lldb, llvm-objcopy,
  llvm-symbolizer, llvm-dwarfdump, etc

[zstd
compressed debug sections](https://maskray.me/blog/2022-09-09-zstd-compressed-debug-sections)

### lld/ELF

#### RISC-V

茅聶聢忙聻聺忙聡聥 added initial RISC-V support for non-PIC in 2018. I added PIC
and TLS support in 2019 ([acknowledgements
by lowRISC](https://lowrisc.org/blog/2019/07/risc-v-llvm-backend-in-clang-llvm-9.0/)). The port was mature but linker relaxation was the last
main piece to bring feature parity with GNU ld. This year I

* Implemented RISC-V linker relaxation ([acknowledgement](https://muxup.com/2022q3/whats-new-for-risc-v-in-llvm-15))
* Implemented `SHT_RISCV_ATTRIBUTES` merge support which
  has a niche value
* Implemented `DT_RISCV_VARIANT_CC`

[RISC-V
linker relaxation in lld](https://maskray.me/blog/2022-07-10-riscv-linker-relaxation-in-lld)

#### Performance

I spent some weekends improving the performance of lld/ELF this year.
Let's compare an lld 13 built with latest Clang
(`/tmp/out/custom0/bin/lld`) with latest lld built with
latest Clang (`/tmp/out/custom2/bin/lld`).

Link a
`-DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=on`
build of clang 16:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` lld 13:     Time (mean 脗卤 脧聝):     687.1 ms 脗卤   7.1 ms    [User: 642.6 ms, System: 431.7 ms] latest lld: Time (mean 脗卤 脧聝):     422.9 ms 脗卤   5.3 ms    [User: 579.8 ms, System: 470.7 ms]  Summary   'numactl -C 32-39 /tmp/out/custom2/bin/lld -flavor gnu @response.txt --threads=8' ran     1.62 脗卤 0.03 times faster than 'numactl -C 32-39 /tmp/out/custom0/bin/lld -flavor gnu @response.txt --threads=8' ``` |

Link a `-DCMAKE_BUILD_TYPE=Debug` build of clang 16:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` lld 13:     Time (mean 脗卤 脧聝):      4.494 s 脗卤  0.039 s    [User: 7.516 s, System: 2.909 s] latest lld: Time (mean 脗卤 脧聝):      3.174 s 脗卤  0.037 s    [User: 7.361 s, System: 3.202 s]  Summary   'numactl -C 32-39 /tmp/out/custom2/bin/lld -flavor gnu @response.txt --threads=8' ran     1.42 脗卤 0.02 times faster than 'numactl -C 32-39 /tmp/out/custom0/bin/lld -flavor gnu @response.txt --threads=8' ``` |

This great speedup is achieved by

* Improve internal representation and optimize passes
* Parallelize [section](https://reviews.llvm.org/D120626)
  and [local symbol](https://reviews.llvm.org/D119909)
  initialization
* [Parallelize relocation
  scanning](https://reviews.llvm.org/D133003)
* [Parallelize writes of
  different output sections](https://reviews.llvm.org/D131247)
* [Process archives as
  flattened `--start-lib` relocatable files](https://reviews.llvm.org/D119074) (avoid memory
  accesses to archive symbol tables)
* Parallelize `--compress-debug-sections=zlib`

See [lld 14 ELF
changes](https://maskray.me/blog/2022-02-20-lld-14-elf-changes) and [lld 15 ELF
changes](https://maskray.me/blog/2022-09-05-lld-15-elf-changes) for detail. As usual, I wrote the ELF port's release notes
for the two releases.

### Clang built glibc (get the ball rolling)

glibc is probably the most prominent OSS which cannot be built with
Clang yet. I sent some patches last year and made a few this year. See
my notes from the last year: [When
can glibc be built with Clang?](https://maskray.me/blog/2021-10-10-when-can-glibc-be-built-with-clang#asm-label-after-first-use)

This year Adhemerval Zanella from Linaro maintained a local branch to
fix aarch64/i386/x86\_64 builds. I reviewed some of his patches.

It seems that such work will benefit some research projects. For
example, Intel FineIBT used a GRTE branch of glibc.

## llvm-project

* C++/ObjC++: switch to gnu++17 as the default standard (fixed many
  tests)
* `--gcc-install-dir=`: use
  `clang++ --gcc-install-dir=/usr/lib/gcc/x86_64-linux-gnu/12`
  to use the selected GCC installation directory. Gentoo uses this
  (`/etc/clang/gentoo-gcc-install.cfg`) to select the
  configured GCC installation
* Defaulted to `-fsanitize-address-use-odr-indicator`
* Fixed a long-term bug related to local linkage
  `GlobalValue` in non-prevailing COMDAT, exposed in
  (Thin)LTO+PGO
* Fixed some `-fdebug-prefix-map=` issues for debug
  information for assembly sources
* [Supported](https://reviews.llvm.org/D135045)
  `SOURCE_DATE_EPOCH` in Clang
* Helped some opaque pointers migration
* Helped legacy pass manager deprecation

Reviewed many commits. A lot of people don't add a
`Reviewed By:` tag. Anyway, counting commits with the tag can
give an underestimate.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % git shortlog -sn bfc8f76e60a8efd920dbd6efc4467ffb6de15919.. --grep 'Reviewed .*MaskRay' | awk '{s+=$1}END{print s}' 386 ``` |

My number of commits exceeded 4000 this year. Many are clean-up
commits or fixup for others' work. I hope that I can do more useful work
next year.

## binutils

Reported many bugs and feature requests:

* [`ar: Add --thin to avoid 'T' conflict with X/Open System Interface`](https://sourceware.org/PR28759)
* [`ld: Make --compress-debug-sections=zlib parallel`](https://sourceware.org/PR28812)
* [`ld: Customize output section type`](https://sourceware.org/PR28841)
* [`ar: add 'L' modifier as a shortcut for ADDLIB`](https://sourceware.org/PR28851)
* [`gold: --no-define-common is incompatible with GNU ld`](https://sourceware.org/PR28871)
* [`` ld: `not found for insert` error has a weird ordering ``](https://sourceware.org/PR28902)
* [`objcopy --weaken-symbol does not weaken STB_GNU_UNIQUE symbols`](https://sourceware.org/PR28926)
* [`gas: .set should copy st_size only if src's st_size is unset`](https://sourceware.org/PR29012)
* [`gas: -gsomething-not-already-a-long-option does not get a diagnostic`](https://sourceware.org/PR29067)
* [`nm: add --no-weak`](https://sourceware.org/PR29135)
* [`ld: ENTRY(no_such_symbol) in -shared mode does not report a warning`](https://sourceware.org/PR29136)
* [`build failures with make --shuffle -j N`](https://sourceware.org/PR29167)
* [`binutils: support zstd for SHF_COMPRESSED debug sections`](https://sourceware.org/PR29397)
* [`ld ppc64: unneeded R_PPC64_NONE in .rela.dyn when linking Linux vdso`](https://sourceware.org/PR29540)
*...