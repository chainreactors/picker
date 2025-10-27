---
title: Mapping symbols: rethinking for efficiency
url: https://maskray.me/blog/2024-07-21-mapping-symbols-rethinking-for-efficiency
source: MaskRay
date: 2024-07-22
fetch_date: 2025-10-06T17:40:25.006002
---

# Mapping symbols: rethinking for efficiency

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-07-21](/blog/2024-07-21-mapping-symbols-rethinking-for-efficiency)

# Mapping symbols: rethinking for efficiency

In object files, certain code patterns embed data within instructions
or transitions occur between instruction sets. This can create hurdles
for disassemblers, which might misinterpret data as code, resulting in
inaccurate output. Furthermore, code written for one instruction set
could be incorrectly disassembled as another. To address these issues,
some architectures (Arm, C-SKY, NDS32, RISC-V, etc) define mapping
symbols to explicitly denote state transition. Let's explore this
concept using an AArch32 code example:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` .text   adr     r0, .LJTI0_0   vldr    d0, .LCPI0_0   bl thumb_callee .LBB0_1:   nop .LBB0_2:   nop  .LCPI0_0:   .long   3367254360                      @ double 1.234   .long   1072938614    nop  .LJTI0_0:   .long   .LBB0_1   .long   .LBB0_2  .thumb .type thumb_callee, %function thumb_callee:   bx lr ``` |

**Jump tables** (`.LJTI0_0`): Jump tables can
reside in either data or text sections, each with its trade-offs. Here
we see a jump table in the text section
(`MachineJumpTableInfo::EK_Inline` in LLVM), allowing a
single instruction to take its address. Other architectures generally
prefer to place jump tables in data sections. While avoiding data in
code, RISC architectures typically require two instructions to
materialize the address, since text/data distance can be pretty
large.

**Constant pool (`.LCPI0_0`)**: The
`vldr` instruction loads a 16-byte floating-point literal to
the SIMD&FP register.

**ISA transition**: This code blends A32 and T32
instructions (the latter used in `thumb_callee`).

In these cases, a dumb disassembler might treat data as code and try
disassembling them as instructions. Assemblers create mapping symbols to
assist disassemblers. For this example, the assembled object file looks
like the following:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $a:   ...  $d:   .long   3367254360                      @ double 1.234   .long   1072938614  $a:   nop  $d:   .long   .LBB0_1   .long   .LBB0_2   .long   .LBB0_3  $t: thumb_callee:   bx lr ``` |

## Toolchain

Now, let's delve into how mapping symbols are managed within the
toolchain.

### Disassemblers

llvm-objdump sorts symbols, including mapping symbols, relative to
the current section, presenting interleaved labels and instructions.
Mapping symbols act as signals for the disassembler to switch
states.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` % llvm-objdump -d --triple=armv7 --show-all-symbols a.o  a.o:    file format elf32-littlearm  Disassembly of section .text:  00000000 <$a.0>:        0: e28f0018      add     r0, pc, #24        4: ed9f0b02      vldr    d0, [pc, #8]            @ 0x14        8: ebfffffe      bl      0x8                     @ imm = #-0x8        c: e320f000      hint    #0x0       10: e320f000      hint    #0x0  00000014 <$d.1>:       14: 58 39 b4 c8   .word   0xc8b43958       18: 76 be f3 3f   .word   0x3ff3be76  0000001c <$a.2>:       1c: e320f000      nop  00000020 <$d.3>:       20: 0c 00 00 00   .word   0x0000000c       24: 10 00 00 00   .word   0x00000010  00000028 <$t.4>: 00000028 <thumb_callee>:       28: 4770          bx      lr ``` |

I [changed llvm-objdump
18](https://reviews.llvm.org/D156190) to not display mapping symbols as labels unless
`--show-all-symbols` is specified.

### nm

Both llvm-nm and GNU nm typically conceal mapping symbols alongside
`STT_FILE` and `STT_SECTION` symbols. However, you
can reveal these special symbols using the `--special-syms`
option.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` % cat a.s foo:   bl thumb_callee .long 42 .thumb thumb_callee:   bx lr % clang --target=arm-linux-gnueabi -c a.s % llvm-nm a.o 00000000 t foo 00000008 t thumb_callee % llvm-nm --special-syms a.o 00000000 t $a.0 00000004 t $d.1 00000008 t $t.2 00000000 t foo 00000008 t thumb_callee ``` |

GNU nm behaves similarly, but with a slight quirk. If the default BFD
target isn't AArch32, mapping symbols are displayed even without
`--special-syms`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` % arm-linux-gnueabi-nm a.o 00000000 t foo 00000008 t thumb_callee % nm a.o 00000000 t $a.0 00000004 t $d.1 00000008 t $t.2 00000000 t foo 00000008 t thumb_callee ``` |

### Symbolizers

Mapping symbols, being non-unique and lacking descriptive names, are
intentionally omitted by symbolizers like addr2line and llvm-symbolizer.
Their primary role lies in guiding the disassembly process rather than
providing human-readable context.

## Size problem: symbol table bloat

While mapping symbols are useful, they can significantly inflate the
symbol table, particularly in 64-bit architectures
(`sizeof(Elf64_Sym) == 24`) with larger programs. This issue
becomes more pronounced when using
`-ffunction-sections -fdata-sections`, which generates
numerous small sections.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` | ``` % cat a.c void f0() {} void f1() {} void f2() {} int d1 = 1; int d2 = 2; % clang -c --target=aarch64 -ffunction-sections -fdata-sections a.c % llvm-objdump -d --show-all-symbols a.o  # GNU objdump --show-all-symbols does no display mapping symbols  a.o:    file format elf64-littleaarch64  Disassembly of section .text.f0:  0000000000000000 <$x>: 0000000000000000 <f0>:        0: d65f03c0      ret  Disassembly of section .text.f1:  0000000000000000 <$x>: 0000000000000000 <f1>:        0: d65f03c0      ret  Disassembly of section .text.f2:  0000000000000000 <$x>: 0000000000000000 <f2>:        0: d65f03c0      ret % llvm-readelf -sX a.o  Symbol table '.symtab' contains 16 entries:    Num:    Value          Size Type    Bind   Vis+Other Ndx(SecName) Name [+ Version Info]      0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT   UND      1: 0000000000000000     0 FILE    LOCAL  DEFAULT   ABS          a.c      2: 0000000000000000     0 SECTION LOCAL  DEFAULT     3 (.text.f0) .text.f0      3: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     3 (.text.f0) $x      4: 0000000000000000     0 SECTION LOCAL  DEFAULT     4 (.text.f1) .text.f1      5: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     4 (.text.f1) $x      6: 0000000000000000     0 SECTION LOCAL  DEFAULT     5 (.text.f2) .text.f2      7: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     5 (.text.f2) $x      8: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     6 (.data)  $d      9: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     7 (.comment) $d     10: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT     9 (.eh_frame) $d     11: 0000000000000000     4 FUNC    GLOBAL DEFAULT     3 (.text.f0) f0     12: 0000000000000000     4 FUNC    GLOBAL DEFAULT     4 (.text.f1) f1     13: 0000000000000000     4 FUNC    GLOBAL DEFAULT     5 (.text.f2) f2     14: 0000000000000000     4 OBJECT  GLOBAL DEFAULT     6 (.data)  d1     15: 0000000000000004     4 OBJECT  GLOBAL DEFAULT     6 (.data)  d2 ``` |

Except the trivial cases (e.g. empty section), in both GNU assembler
and LLVM integrated assemble's AArch64 ports:

* A non-text section (data, debug, etc) almost always starts with an
  initial `$d`.
* A text section almost always starts with an initial `$x`.
  ABI requires a mapping symbol at offset 0.

The behaviors ensure that each function or data symbol has a
corresponding mapping symbol, while extra mapping symbols might occur in
rare cases. Thereo...