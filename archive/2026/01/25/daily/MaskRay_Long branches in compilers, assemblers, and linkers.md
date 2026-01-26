---
title: Long branches in compilers, assemblers, and linkers
url: https://maskray.me/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers
source: MaskRay
date: 2026-01-25
fetch_date: 2026-01-26T03:52:16.041826
---

# Long branches in compilers, assemblers, and linkers

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-01-25](/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers)

# Long branches in compilers, assemblers, and linkers

Branch instructions on most architectures use PC-relative addressing
with a limited range. When the target is too far away, the branch
becomes "out of range" and requires special handling.

Consider a large binary where `main()` at address 0x10000
calls `foo()` at address 0x8010000-over 128MiB away. On
AArch64, the `bl` instruction can only reach Â±128MiB, so this
call cannot be encoded directly. Without proper handling, the linker
would fail with an error like "relocation out of range." The toolchain
must handle this transparently to produce correct executables.

This article explores how compilers, assemblers, and linkers work
together to solve the long branch problem.

* Compiler (IR to assembly): Handles branches within a function that
  exceed the range of conditional branch instructions
* Assembler (assembly to relocatable file): Handles branches within a
  section where the distance is known at assembly time
* Linker: Handles cross-section and cross-object branches discovered
  during final layout

## Branch range limitations

Different architectures have different branch range limitations.
Here's a quick comparison of unconditional branch/call ranges:

| Architecture | Unconditional Branch | Conditional Branch | Notes |
| --- | --- | --- | --- |
| AArch64 | Â±128MiB | Â±1MiB | Range extension thunks |
| AArch32 (A32) | Â±32MiB | Â±32MiB | Range extension and interworking veneers |
| AArch32 (T32) | Â±16MiB | Â±1MiB | Thumb has shorter ranges |
| LoongArch | Â±128MiB | Â±128KiB | Linker relaxation |
| PowerPC64 | Â±32MiB | Â±32KiB | Range extension and TOC/NOTOC interworking thunks |
| RISC-V | Â±1MiB (`jal`) | Â±4KiB | Linker relaxation |
| x86-64 | Â±2GiB | Â±2GiB | Code models or thunk extension |

The following subsections provide detailed per-architecture
information, including relocation types relevant for linker
implementation.

### AArch32

In A32 state:

* Branch (`b`/`b<cond>`), conditional
  branch and link (`bl<cond>`)
  (`R_ARM_JUMP24`): Â±32MiB
* Unconditional branch and link (`bl`/`blx`,
  `R_ARM_CALL`): Â±32MiB

Note: `R_ARM_CALL` is for unconditional
`bl`/`blx` which can be relaxed to BLX inline;
`R_ARM_JUMP24` is for branches which require a veneer for
interworking.

In T32 state (Thumb state pre-ARMv8):

* Conditional branch (`b<cond>`,
  `R_ARM_THM_JUMP8`): Â±256 bytes
* Short unconditional branch (`b`,
  `R_ARM_THM_JUMP11`): Â±2KiB
* ARMv5T branch and link (`bl`/`blx`,
  `R_ARM_THM_CALL`): Â±4MiB
* ARMv6T2 wide conditional branch (`b<cond>.w`,
  `R_ARM_THM_JUMP19`): Â±1MiB
* ARMv6T2 wide branch (`b.w`,
  `R_ARM_THM_JUMP24`): Â±16MiB
* ARMv6T2 wide branch and link (`bl`/`blx`,
  `R_ARM_THM_CALL`): Â±16MiB. `R_ARM_THM_CALL` can be
  relaxed to BLX.

### AArch64

* Test bit and branch (`tbz`/`tbnz`,
  `R_AARCH64_TSTBR14`): Â±32KiB
* Compare and branch (`cbz`/`cbnz`,
  `R_AARCH64_CONDBR19`): Â±1MiB
* Conditional branches (`b.<cond>`,
  `R_AARCH64_CONDBR19`): Â±1MiB
* Unconditional branches (`b`/`bl`,
  `R_AARCH64_JUMP26`/`R_AARCH64_CALL26`):
  Â±128MiB

The compiler's `BranchRelaxation` pass handles
out-of-range conditional branches by inverting the condition and
inserting an unconditional branch. The AArch64 assembler does not
perform branch relaxation; out-of-range branches produce linker errors
if not handled by the compiler.

### LoongArch

* Conditional branches
  (`beq`/`bne`/`blt`/`bge`/`bltu`/`bgeu`,
  `R_LARCH_B16`): Â±128KiB (18-bit signed)
* Compare-to-zero branches (`beqz`/`bnez`,
  `R_LARCH_B21`): Â±4MiB (23-bit signed)
* Unconditional branch/call (`b`/`bl`,
  `R_LARCH_B26`): Â±128MiB (28-bit signed)
* Medium range call (`pcaddu12i`+`jirl`,
  `R_LARCH_CALL30`): Â±2GiB
* Long range call (`pcaddu18i`+`jirl`,
  `R_LARCH_CALL36`): Â±128GiB

### MIPS

* Conditional branches
  (`beq`/`bne`/`bgez`/`bltz`/etc,
  `R_MIPS_PC16`): Â±128KiB
* Jump/call (`j`/`jal`, `R_MIPS_26`):
  pseudo-absolute branch within the current 256MiB region, only suitable
  for `-fno-pic` code. Deprecated in R6 in favor of
  `bc`/`balc`

16-bit instructions removed in Release 6:

* Conditional branch (`beqz16`,
  `R_MICROMIPS_PC7_S1`): Â±128 bytes
* Unconditional branch (`b16`,
  `R_MICROMIPS_PC10_S1`): Â±1KiB

MIPS Release 6:

* Unconditional branch, compact (`bc16`, unclear toolchain
  implementation): Â±1KiB
* Compare and branch, compact
  (`beqc`/`bnec`/`bltc`/`bgec`/etc,
  `R_MIPS_PC16`): Â±128KiB
* Compare register to zero and branch, compact
  (`beqzc`/`bnezc`/etc,
  `R_MIPS_PC21_S2`): Â±4MiB
* Branch (and link), compact (`bc`/`balc`,
  `R_MIPS_PC26_S2`): Â±128MiB

LLVM's `MipsBranchExpansion` pass handles out-of-range
branches.

lld implements LA25 thunks for MIPS PIC/non-PIC interoperability, but
not range extension thunks.

### PowerPC

* Conditional branch (`bc`/`bcl`,
  `R_PPC64_REL14`): Â±32KiB
* Unconditional branch (`b`/`bl`,
  `R_PPC64_REL24`/`R_PPC64_REL24_NOTOC`):
  Â±32MiB

GCC-generated code relies on linker thunks. However, the legacy
`-mlongcall` can be used to generate long code sequences.

### RISC-V

* Compressed `c.beqz`: Â±256 bytes
* Compressed `c.jal`: Â±2KiB
* `jalr` (I-type immediate): Â±2KiB
* Conditional branches
  (`beq`/`bne`/`blt`/`bge`/`bltu`/`bgeu`,
  B-type immediate): Â±4KiB
* `jal` (J-type immediate, `PseudoBR`): Â±1MiB
  (notably smaller than other RISC architectures: AArch64 Â±128MiB,
  PowerPC64 Â±32MiB, LoongArch Â±128MiB)
* `PseudoJump` (using `auipc` +
  `jalr`): Â±2GiB
* `beqi`/`bnei` (Zibi extension, 5-bit compare
  immediate (1 to 31 and -1)): Â±4KiB

Qualcomm uC Branch Immediate extension (Xqcibi):

* `qc.beqi`/`qc.bnei`/`qc.blti`/`qc.bgei`/`qc.bltui`/`qc.bgeui`
  (32-bit, 5-bit compare immediate): Â±4KiB
* `qc.e.beqi`/`qc.e.bnei`/`qc.e.blti`/`qc.e.bgei`/`qc.e.bltui`/`qc.e.bgeui`
  (48-bit, 16-bit compare immediate): Â±4KiB

Qualcomm uC Long Branch extension (Xqcilb):

* `qc.e.j`/`qc.e.jal` (48-bit,
  `R_RISCV_VENDOR(QUALCOMM)+R_RISCV_QC_E_CALL_PLT`): Â±2GiB

For function calls:

* The [Go
  compiler](https://go-review.googlesource.com/c/go/%2B/345051) emits a single `jal` for calls and relies on its
  linker to generate trampolines when the target is out of range.
* In contrast, GCC and Clang emit `auipc`+`jalr`
  and rely on linker relaxation to shrink the sequence when possible.

The `jal` range (Â±1MiB) is notably smaller than other RISC
architectures (AArch64 Â±128MiB, PowerPC64 Â±32MiB, LoongArch Â±128MiB).
This limits the effectiveness of linker relaxation ("start large and
shrink"), and leads to frequent trampolines when the compiler
optimistically emits `jal` ("start small and grow").

### SPARC

* Compare and branch (`cxbe`, `R_SPARC_5`): Â±64
  bytes
* Conditional branch (`bcc`, `R_SPARC_WDISP19`):
  Â±1MiB
* Unconditional branch (`b`, `R_SPARC_WDISP22`):
  Â±8MiB
* `call`
  (`R_SPARC_WDISP30`/`R_SPARC_WPLT30`): Â±2GiB

With Â±2GiB range for `call`, SPARC doesn't need range
extension thunks in practice.

### SuperH

* Conditional branch (`bf`/`bt`): Â±256
  bytes
* Unconditional branch (`bra`): Â±4KiB
* Branch to subroutine (`bsr`): Â±4KiB

The very short range for conditional branches (Â±256 bytes) requires
the compiler to invert the condition and generate register-indirect
`braf`/`bsrf` for longer distances. SuperH is not
supported by LLVM.

### Xtensa

* Narrow conditional branch (`beqz.n`/`bnez.n`):
  -28 to +35 bytes (6-bit signed + 4)
* Conditional branch (compare two registers)
  (`beq`/`bne`/`blt`/`bge`/etc):
  Â±256 bytes
* Conditional branch (compare with zero)
  (`beqz`/`bnez`/`bltz`/`bgez`):
  Â±2KiB
* Unconditional jump (`j`): Â±128KiB
* Call
  (`call0`/`call4`/`...