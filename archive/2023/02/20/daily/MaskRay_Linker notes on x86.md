---
title: Linker notes on x86
url: https://maskray.me/blog/2023-02-19-linker-notes-on-x86
source: MaskRay
date: 2023-02-20
fetch_date: 2025-10-04T07:32:33.037337
---

# Linker notes on x86

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-02-19](/blog/2023-02-19-linker-notes-on-x86)

# Linker notes on x86

Updated in 2024-01.

This article describes target-specific details about x86 in ELF
linkers. I will use "x86" to refer to both x86-32 and x86-64.

## Global Offset Table

The Global Offset Table consists of two sections:

* `.got.plt` holds code addresses for PLT.
* `.got` holds other addresses and offsets.

The symbol `_GLOBAL_OFFSET_TABLE_` is defined at the
beginning of the `.got.plt` section. If `.got.plt`
is absent, GNU ld defines `_GLOBAL_OFFSET_TABLE_` at the
beginning of the `.got` section.

`.got.plt` has 3 reserved entries.

`.got.plt[0]` holds the link-time address of
`_DYNAMIC` for a legacy reason. Versions of glibc prior to
2.35 have the `_DYNAMIC` requirement. See [All
about Global Offset Table](/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0).

`.got.plt[1]` and `.got.plt[2]` are for lazy
binding PLT. Linkers communicate the address of `.got.plt` to
rtld with the dynamic tag `DT_PLTGOT`.

### GOT optimization

See [All
about Global Offset Table#GOT optimization](/blog/2021-08-29-all-about-global-offset-table#got-optimization).

## Procedure Linkage Table

### Indirect Branch Tracking

See `.note.gnu.property` below for Indirect Branch
Tracking. See [All about
Procedure Linkage Table#x86](/blog/2021-09-19-all-about-procedure-linkage-table#x86) for detail.

The scheme used in GNU ld unnecessarily uses two sections
`.plt` and `.plt.sec`. ld.lld follows suit to
avoid adding complexity to tools like objdump (PLT recognition). mold
adopts an alternative scheme (what Indirect Branch Tracking should have
used in the first place). Unfortunately, this is a scenario that the
ship has sailed and adding an alternative would not simplify the world.
I think this just adds implementation complexity for other tools which
want to support its scheme.

### Retpoline

Retpoline is for Spectre v2 mitigation. PLT entries are synthesized
by the linker and need adaptation as well. This can be enabled in ld.lld
with `-z retpolineplt`.

### mark-plt

See x86 PLT rewriting on [All
about Procedure Linkage Table](/blog/2021-09-19-all-about-procedure-linkage-table#x86-plt-rewriting).

## Thread Local Storage

x86 uses TLS Variant II: the static TLS blocks are placed below the
thread pointer.

Beside the traditional general dynamic and local dynamic TLS models,
there are TLSDESC ABIs for x86-32 and x86-64.

The linker performs TLS optimization.

See [All
about thread-local storage](/blog/2021-02-14-all-about-thread-local-storage).

## Program Property

A `.note.gnu.property` section contains program property
notes which describe special handling requirements for the linker and
the dynamic loader.

x86 psABIs define many property notes but many don't seem
particularly useful.

* `GNU_PROPERTY_X86_ISA_1_BASELINE`,
  `GNU_PROPERTY_X86_ISA_1_V2`,
  `GNU_PROPERTY_X86_ISA_1_V2`,
  `GNU_PROPERTY_X86_ISA_1_V3`: these properties describe the
  x86 ISA level
* `GNU_PROPERTY_X86_ISA_1_USED`,
  `GNU_PROPERTY_X86_ISA_1_NEEDED`: deprecated when the x86 ISA
  level was introduced
* `GNU_PROPERTY_X86_FEATURE_1_IBT`,
  `GNU_PROPERTY_X86_FEATURE_1_SHSTK`: used by Intel CET (see [Control flow
  integrity](/blog/2022-12-18-control-flow-integrity)). See below

For x86, the linker parses input `.note.gnu.property`
sections and recognize `-z force-ibt` and
`-z shstk` to compute the output
`.note.gnu.property` (type is `SHT_NOTE`)
section.

The following code (extracted from ld.lld) describes the behavior.
Basically, without extra options, the output has the
`GNU_PROPERTY_X86_FEATURE_1_IBT` bit if all input
`.note.gnu.property` sections have the bit (logical AND).
`-z force-ibt` forces setting the bit with a warning.

The output has the `GNU_PROPERTY_X86_FEATURE_1_SHSK` bit
if all input `.note.gnu.property` sections have the bit
(logical AND). `-z shstk` forces setting the bit without a
warning.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` for (ELFFileBase *f : ctx.objectFiles) {   uint32_t features = f->andFeatures;   if (!(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {     if (config->zCetReport == "error")       error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");     else if config->zCetReport == "warning")       warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");   }   if (!(features & GNU_PROPERTY_X86_FEATURE_1_SHSTK)) {     if (config->zCetReport == "error")       error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");     else if config->zCetReport == "warning")       warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");   }    if (config->zForceIbt && !(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {     if (config->zCetReport == "none")       warn(toString(f) + ": -z force-ibt: file does not have "                          "GNU_PROPERTY_X86_FEATURE_1_IBT property");     features |= GNU_PROPERTY_X86_FEATURE_1_IBT;   }   ret &= features; }  // Force enable Shadow Stack. if (config->zShstk)   ret |= GNU_PROPERTY_X86_FEATURE_1_SHSTK; ``` |

## `.eh_frame`

`.eh_frame` sections are usually of type
`SHT_PROGBITS`. It is regarded as a mistake that a
special-purpose section does not have a dedicated type. The x86-64 psABI
says that `SHT_X86_64_UNWIND` should be used. For future
architectures, it would be good not to reserve 0x70000001 for other
purposes.

Clang since rL252300 emits `.eh_frame` sections of type
`SHT_X86_64_UNWIND` to conform to the psABI. Linkers need to
allow mixed `SHT_PROGBITS` and `SHT_X86_64_UNWIND`
`.eh_frame` sections.

## `.gnu.linkonce.t.__x86.get_pc_thunk.bx`

The magic symbol prefix `.gnu.linkonce` was used before
COMDAT was introduced into ELF. `.gnu.linkonce` was very
obsoleted now, but unfortunately
`.gnu.linkonce.t.__x86.get_pc_thunk.bx` remained relevant in
glibc x86-32 until glibc 2.32 (2020-08).

## Split stack

gccgo uses a segmented stack scheme called "split stack". Split stack
permits a discontiguous stack which is grown automatically as needed.
(The gc Go compiler now uses stack copying rather than stack splitting.
Using stack copying in gccgo is difficult as the compiler needs to have
accurate stack maps for all frames on the stack, knowing absolutely
every pointer.)

The scheme calls runtime functions (`__morestack*`)
defined in libgcc and requires the linker to rewrite some code
sequences.

Each relocatable object file using split stack has a marker section
named `.note.GNU-split-stack`. The linker uses this section
to recognize relocatable object files compiled with split stack
support.

For a function call from a split-stack relocatable object file to a
non-split-stack relocatable object file, the linker rewrites the
function prologue. The prologue can be of either of the following two
schemes.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ```   cmp   rsp, qword ptr fs:[0x70]   jae   1f   call  __morestack   ret 1:   ...  =>    stc   nop   dword ptr [rax + rax]   jae   1f   call  __morestack_non_split   ret 1:   ... ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ```   lea   r10, [rsp-0x100]     # The register is r10 or r11   cmp   r10, qword ptr fs:[0x70]   jae   1f   call  __morestack   ret 1:   ...  =>    lea   r10, [rsp-0x4100]    # The displacement is changed   cmp   r10, qword ptr fs:[0x70]   jae   1f   call  __morestack_non_split   ret 1:   ... ``` |

Share

* [linker](/blog/tags/linker/)

[**Newer**

Linker notes on Power ISA](/blog/2023-02-26-linker-notes-o...