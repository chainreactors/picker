---
title: lld linked musl on PowerPC64
url: https://buaq.net/go-134301.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:31.436301
---

# lld linked musl on PowerPC64

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

lld linked musl on PowerPC64

I was asked about a cra
*2022-11-5 15:0:0
Author: [maskray.me(查看原文)](/jump-134301.htm)
阅读量:23
收藏*

---

I was asked about a crash related to lld linked musl libc.so on PowerPC64. An executable using the built libc.so as the interpreter segfaulted while invoking libc.so to load the executable did not.

The section and program header dump from readelf looked like the following.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` There are 36 section headers, starting at offset 0x2e4890:  Section Headers:   [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al   [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0   [ 1] .note.gnu.build-id NOTE           0000000000000270 000270 000018 00   A  0   0  4   [ 2] .dynsym           DYNSYM          0000000000000288 000288 009fc0 18   A  5   1  8   [ 3] .gnu.hash         GNU_HASH        000000000000a248 00a248 003150 00   A  2   0  8   [ 4] .hash             HASH            000000000000d398 00d398 003548 04   A  2   0  4   [ 5] .dynstr           STRTAB          00000000000108e0 0108e0 004564 00   A  0   0  1   [ 6] .rela.dyn         RELA            0000000000014e48 014e48 000e28 18   A  2   0  8   [ 7] .rela.plt         RELA            0000000000015c70 015c70 000090 18  AI  2  17  8   [ 8] .rodata           PROGBITS        0000000000015d00 015d00 0336fd 00 AMS  0   0 16   [ 9] .eh_frame_hdr     PROGBITS        0000000000049400 049400 00001c 00   A  0   0  4   [10] .eh_frame         PROGBITS        0000000000049420 049420 00004c 00   A  0   0  8   [11] .text             PROGBITS        0000000000059480 049480 089308 00  AX  0   0 32   [12] .glink            PROGBITS        00000000000e2788 0d2788 000054 00  AX  0   0  4   [13] .data.rel.ro      PROGBITS        00000000000f27e0 0d27e0 000408 00  WA  0   0  8   [14] .dynamic          DYNAMIC         00000000000f2be8 0d2be8 000140 10  WA  5   0  8   [15] .got              PROGBITS        00000000000f2d28 0d2d28 000008 00  WA  0   0  8   [16] .toc              PROGBITS        00000000000f2d30 0d2d30 0002a0 00  WA  0   0  8   [17] .plt              NOBITS          00000000000f2fd0 0d2fd0 000040 00  WA  0   0  8   [18] .data             PROGBITS        0000000000103010 0d3010 0003c0 00  WA  0   0  8   [19] .bss              NOBITS          00000000001033d0 0d33d0 002ac8 00  WA  0   0 16   [20] .branch_lt        NOBITS          0000000000105e98 0d33d0 000000 00  WA  0   0  8   [21] .debug_loclists   PROGBITS        0000000000000000 0d33d0 046be2 00      0   0  1   [22] .debug_abbrev     PROGBITS        0000000000000000 119fb2 0466c3 00      0   0  1   [23] .debug_info       PROGBITS        0000000000000000 160675 089b79 00      0   0  1   [24] .debug_rnglists   PROGBITS        0000000000000000 1ea1ee 006693 00      0   0  1   [25] .debug_str_offsets PROGBITS       0000000000000000 1f0881 02783c 00      0   0  1   [26] .debug_str        PROGBITS        0000000000000000 2180bd 013f8b 01  MS  0   0  1   [27] .debug_addr       PROGBITS        0000000000000000 22c048 011780 00      0   0  1   [28] .comment          PROGBITS        0000000000000000 23d7c8 000029 01  MS  0   0  1   [29] .debug_frame      PROGBITS        0000000000000000 23d7f8 0176f0 00      0   0  8   [30] .debug_line       PROGBITS        0000000000000000 254ee8 0657e4 00      0   0  1   [31] .debug_line_str   PROGBITS        0000000000000000 2ba6cc 0089ee 01  MS  0   0  1   [32] .debug_aranges    PROGBITS        0000000000000000 2c30ba 0001b0 00      0   0  1   [33] .symtab           SYMTAB          0000000000000000 2c3270 016b90 18     35 2175  8   [34] .shstrtab         STRTAB          0000000000000000 2d9e00 00016f 00      0   0  1   [35] .strtab           STRTAB          0000000000000000 2d9f6f 00a91f 00      0   0  1 Key to Flags:   W (write), A (alloc), X (execute), M (merge), S (strings), I (info),   L (link order), O (extra OS processing required), G (group), T (TLS),   C (compressed), x (unknown), o (OS specific), E (exclude),   p (processor specific)  Elf file type is DYN (Shared object file) Entry point 0xdb8bc There are 10 program headers, starting at offset 64  Program Headers:   Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align   PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x000230 0x000230 R   0x8   LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x04946c 0x04946c R   0x10000   LOAD           0x049480 0x0000000000059480 0x0000000000059480 0x08935c 0x08935c R E 0x10000   LOAD           0x0d27e0 0x00000000000f27e0 0x00000000000f27e0 0x0007f0 0x000830 RW  0x10000   LOAD           0x0d3010 0x0000000000103010 0x0000000000103010 0x0003c0 0x002e88 RW  0x10000   DYNAMIC        0x0d2be8 0x00000000000f2be8 0x00000000000f2be8 0x000140 0x000140 RW  0x8   GNU_RELRO      0x0d27e0 0x00000000000f27e0 0x00000000000f27e0 0x0007f0 0x001820 R   0x1   GNU_EH_FRAME   0x049400 0x0000000000049400 0x0000000000049400 0x00001c 0x00001c R   0x4   GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x0   NOTE           0x000270 0x0000000000000270 0x0000000000000270 0x000018 0x000018 R   0x4   Section to Segment mapping:   Segment Sections...    00    01     .note.gnu.build-id .dynsym .gnu.hash .hash .dynstr .rela.dyn .rela.plt .rodata .eh_frame_hdr .eh_frame    02     .text .glink    03     .data.rel.ro .dynamic .got .toc .plt    04     .data .bss    05     .dynamic    06     .data.rel.ro .dynamic .got .toc .plt    07     .eh_frame_hdr    08    09     .note.gnu.build-id    None   .branch_lt .debug_loclists .debug_abbrev .debug_info .debug_rnglists .debug_str_offsets .debug_str .debug_addr .comment .debug_frame .debug_line .debug_line_str .debug_aranges .symtab .shstrtab .strtab ``` |

There were two `PT_LOAD` program headers with the `PF_R|PF_W` flags and the unusual property `p_filesz < p_memsz`. It turns out that when the Linux kernel loads an interpreter (`PT_INTERP`; see `fs/binfmt_elf.c:load_elf_interp`), it only supports one `PT_LOAD` with `p_filesz < p_memsz`.

Note: it is typical for lld output to have two RW `PT_LOAD` program headers, one for RELRO sections (`PT_GNU_RELRO`) and the other for non-RELRO sections. This may look unusual at the first glance but it avoids an alignment padding as used in GNU ld's single RW `PT_LOAD` layout. See [Explain GNU style linker options#-z relro](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options#z-relro).

In the PowerPC ELFv2 ABI, `.plt` is like GOTPLT on other architectures (it holds resolved addresses for PLT entries) and has the `SHT_NOBITS` type. With `-z now`, `.plt` can be eagerly resolved and become read-only after relocation resolving, therefore it is part of `PT_GNU_RELRO`. When lld layouts sections, it is part of the first RW `PT_LOAD`.

Clang as of 15.0 passes `-z now` to ld for Alpine Linux. Chimera Linux has patched Clang Driver to pass `-z now` for all musl target triples. To override `-z now`, just build musl with `LDFLAGS=-Wl,-z,lazy`.

I made the suggestion and verified with a local cross-compilation build.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` mkdir out/ppc64le && cd out/ppc64le ../../configure --target=powerpc64le-linux-gnu CC=clang CFLAGS='--target=powerpc64le-linux-gnu -mlong-double-64' LDFLAGS=-fuse-ld=lld make -j$(nproc) ``` |

(If you use GCC's powerpc64 port, avoid `-Os`. lld has not implemented `_savefpr*` and `_restfpr*` functions.)

An alternative workaround I suggested was linking `libc.so` with a linker script:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` SECTIONS { .plt : {} } INSERT AFTER ...