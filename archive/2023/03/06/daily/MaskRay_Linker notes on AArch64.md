---
title: Linker notes on AArch64
url: https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64
source: MaskRay
date: 2023-03-06
fetch_date: 2025-10-04T08:45:16.231734
---

# Linker notes on AArch64

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-03-05](/blog/2023-03-05-linker-notes-on-aarch64)

# Linker notes on AArch64

This article describes target-specific details about AArch64 in ELF
linkers. AArch64 is the 64-bit execution state for the Arm architecture.
The AArch64 execution state runs the A64 instruction set. The AArch32
and AArch64 execution states use very different instruction sets, so
many pieces of software use two ports for the two execution states of
the Arm architecture.

There were the "ARM architecture" and the "ARM instruction set",
leading to many software projects using "ARM" or "arm" as their port
names. In 2011, ARMv8 introduced two execution states, AArch32 and
AArch64. The previous instruction sets "ARM" and "Thumb" were renamed to
"A32" and "T32", respectively. In 2017, the architecture was renamed to
the "Arm architecture" to reflect the rebranding of the company name.
So, the "ARMv8-A" architecture profile is now named "Armv8-A".

For the AArch64 execution state, while many projects use "AArch64" as
their port name, for legacy reasons, macOS, Windows, the Linux kernel,
and some BSD operating systems unfortunately use "arm64". (Support for
AArch64 was added to the Linux kernel in version 3.7. Initially, the
patch set was named "aarch64", but it was later changed at the [request](https://lkml.org/lkml/2012/7/6/624) of kernel
developers.)

## ABI documents

* [ELF
  for the ArmÂ® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst)
* [System
  V ABI for the ArmÂ® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/sysvabi64/sysvabi64.rst)

## Global Offset Table

The Global Offset Table consists of two sections:

* `.got.plt` holds code addresses for PLT.
* `.got` holds other addresses and offsets.

The symbol `_GLOBAL_OFFSET_TABLE_` is defined at the
beginning of the `.got` section. GNU ld reserves a single
entry for `.got` and `.got[0]` holds the link-time
address of `_DYNAMIC` for a legacy reason Versions of glibc
prior to 2.35 have the `_DYNAMIC` requirement. See [All
about Global Offset Table](/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0).

`.got.plt[1]` and `.got.plt[2]` are for lazy
binding PLT. Linkers communicate the address of `.got.plt` to
rtld with the dynamic tag `DT_PLTGOT`.

## Procedure Linkage Table

The registers `x16` (IP0) and `x17` (IP1) are
the first and second intra-procedure-call temporary registers. They may
be used by PLT entries and veneers.

The PLT header looks like:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` bti  c       // If BTI stp  x16, x30, [sp,#-16]! adrp x16, &.got.plt[2] ldr  x17, [x16, :lo12: &.got.plt[2]] add  x16, x16, :lo12: &.got.plt[2] br   x17 ``` |

The Nth PLT entry looks like:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` bti  c       // If BTI adrp x16, &.got.plt[N + 3] ldr  x17, [x16, :lo12: &.got.plt[N + 3]] add  x16, x16, :lo12: &.got.plt[N + 3] autia1716    // If PAC-PLT br   x17 ``` |

When BTI is enabled for the output file, the code sequence starts
with `bti c`. When PAC-PLT is enabled, the code sequence
includes `autia1716` before `br x17`.

`x16` is used by the lazy PLT resolver. For
`ld -z now`, setting `x16` is unneeded. <https://github.com/ARM-software/abi-aa/issues/202>
discusses making `x16` setting optional.

## Relocation optimization

See [All
about Global Offset Table#GOT optimization](/blog/2021-08-29-all-about-global-offset-table#got-optimization) for GOT optimization.

There are a few optimization schemes beside GOT optimization,
e.g.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` add  x2, x2, 0  // R_<CLS>_ADD_ABS_LO12_NC  =>  nop ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` adrp x0, symbol add  x0, x0, :lo12: symbol  =>  nop adr  x0, symbol ``` |

`--no-relax` disables the optimization.

See [ELF
for the ArmÂ® 64-bit Architecture (AArch64)#Relocation
optimization](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst#relocation-optimization).

## Thread Local Storage

AArch64 uses a variant of TLS Variant I: the static TLS blocks are
placed above the thread pointer. The thread pointer points to the end of
the thread control block.

The linker performs TLS optimization.

The traditional general dynamic and local dynamic TLS models are
obsoleted and not supported by ld.lld

See [All
about thread-local storage](/blog/2021-02-14-all-about-thread-local-storage).

## Program Property

A `.note.gnu.property` section contains program property
notes that describe special handling requirements for the linker and the
dynamic loader.

The linker parses input `.note.gnu.property` sections and
recognizes command line options `-z force-bti` and
`-z pac-plt` to compute the output
`.note.gnu.property` (type is `SHT_NOTE`) section.
Without these options, linkers only set the feature bit in the output
file if all the input relocatable object files have the corresponding
feature set.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` for (ELFFileBase *f : ctx.objectFiles) {   uint32_t features = f->andFeatures;   if (!(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {     if (config->zBtiReport == "error")       error(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");     else if (config->zBtiReport == "warning")       warn(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");   }    if (config->zForceBti && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {     if (config->zBtiReport == "none")       warn(toString(f) + ": -z force-bti: file does not have "                          "GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");     features |= GNU_PROPERTY_AARCH64_FEATURE_1_BTI;   }   if (config->zPacPlt && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_PAC)) {     warn(toString(f) + ": -z pac-plt: file does not have "                        "GNU_PROPERTY_AARCH64_FEATURE_1_PAC property");     features |= GNU_PROPERTY_AARCH64_FEATURE_1_PAC;   }   ret &= features; } ``` |

## Range extension thunks

Function calls typically use `B` and `BL`
instructions. The two instructions have a range of +/-128MiB and may use
2 relocation types: `R_AARCH64_CALL26` and
`R_AARCH64_JUMP26`. The range is larger than the branch range
for many other instruction sets. If the destination is not reachable by
a single `B`/`BL`, linkers may insert a veneer
(range extension thunk).

`-no-pie` links may use a thunk with absolute addressing
targeting any location in the 64-bit address space.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` <caller>:   bl      __AArch64AbsLongThunk_nonpreemptible   b       __AArch64AbsLongThunk_nonpreemptible  <__AArch64AbsLongThunk_nonpreemptible>:   ldr     x16, .+8   br      x16  <$d>:   .word   0x00000000   .word   0x00000010  <.plt>: ``` |

`-pie` and `-shared` links need to use a thunk
with PC-relative addressing targeting a range of +/-4GiB.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` <caller>:   bl      __AArch64ADRPThunk_nonpreemptible   b       __AArch64ADRPThunk_nonpreemptible  <__AArch64ADRPThunk_nonpreemptible>:   adrp    x16, nonpreemptible   add     x16, x16, :lo12: nonpreemptible   br      x16 ``` |

The branch target of a thunk may be a PLT entry:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` <caller>:   bl      __AArch64ADRPThunk_preemptible  <__AArch64ADRPThunk_preemptible>:   adrp    x16, preemptible@plt   add     x16, x16, :lo12: preemptible@plt   br      x16  ...  <preemptible@plt>:   adrp    x16, &.got.plt[N + 3]   ldr     x17, [x16, :lo12: &.got.plt[N + 3]]   add     x16, x1...