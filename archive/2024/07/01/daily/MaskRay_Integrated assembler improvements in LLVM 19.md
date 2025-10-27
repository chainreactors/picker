---
title: Integrated assembler improvements in LLVM 19
url: https://maskray.me/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19
source: MaskRay
date: 2024-07-01
fetch_date: 2025-10-06T17:41:04.430176
---

# Integrated assembler improvements in LLVM 19

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-06-30](/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19)

# Integrated assembler improvements in LLVM 19

Within the LLVM project, MC is a library responsible for handling
assembly, disassembly, and object file formats. [Intro
to the LLVM MC Project](https://blog.llvm.org/2010/04/intro-to-llvm-mc-project.html), which was written back in 2010, remains a
good source to understand the high-level structures.

In the latest release cycle, substantial effort has been dedicated to
refining MC's internal representation for improved performance and
readability. These changes have [decreased compile
time significantly](#summary). This blog post will delve into the details,
providing insights into the specific changes.

## Merged `MCAsmLayout` into `MCAssembler`

`MCAssembler` manages assembler states (including
sections, symbols) and implements post-parsing passes (computing a
layout and writing an object file). `MCAsmLayout`, tightly
coupled with `MCAssembler`, was in charge of symbol and
fragment offsets during `MCAssembler::Finish`.
`MCAsmLayout` was a wrapper of `MCAssembler` and a
section order vector (actually Mach-O specific). Many
`MCAssembler` and `MCExpr` member functions have a
`const MCAsmLayout &` parameter, contributing to slight
overhead. Here are some functions that are called frequently:

* `MCAssembler::computeFragmentSize` is called a lot in the
  layout process.
* `MCAsmBackend::handleFixup` and
  `MCAsmBackend::applyFixup` evaluate each fixup and produce
  relocations.
* `MCAssembler::fixupNeedsRelaxation` determines whether a
  `MCRelaxableFragment` needs relaxation due to a
  `MCFixup`.
* `MCAssembler::relaxFragment` and
  `MCAssembler::relaxInstruction` relax a fragment.

I [started
to merge](https://github.com/llvm/llvm-project/commit/67957a45ee1ec42ae1671cdbfa0d73127346cc95) `MCAsmLayout` into `MCAssembler` and
simplify MC code, and eventually removed [`llvm/include/llvm/MC/MCAsmLayout.h`](https://github.com/llvm/llvm-project/commit/122db8b2cb7fa43ce1d6dc17148080579fcfb55a).

## Fragments

Fragments, representing sequences of non-relaxable instructions,
relaxable instruction, alignment directives, and other elements.
`MCDataFragment` and `MCRelaxableFragment`, whose
sizes are crucial for memory consumption, have undergone several
optimizations:

* [MCInst:
  decrease inline element count to 6](https://github.com/llvm/llvm-project/pull/94913)
* [[MC]
  Reduce size of MCDataFragment by 8 bytes](https://github.com/llvm/llvm-project/pull/95293) by @aengelke
* [[MC] Move
  MCFragment::Atom to MCSectionMachO::Atoms](https://github.com/llvm/llvm-project/pull/95341)

The fragment management system has also been streamlined by
transitioning from a doubly-linked list (`llvm::iplist`) to a
[singly-linked
list](https://github.com/llvm/llvm-project/pull/95077), eliminating unnecessary overhead. A few prerequisite commits
removed backward iterator requirements.

Furthermore, I [introduced
the "current fragment" concept](https://github.com/llvm/llvm-project/commit/e48c4011ca80385573f1b92793c75dc98abb228f) (`MCSteamer::CurFrag`)
allowing for faster appending of new fragments.

I have also simplified and optimized fragment offset computation:

* [`[MC] Relax fragments eagerly`](https://github.com/llvm/llvm-project/commit/9d0754ada5dbbc0c009bcc2f7824488419cc5530)
* [`[MC] Relax MCFillFragment and compute fragment offsets eagerly`](https://github.com/llvm/llvm-project/commit/742ecfc13e8aa34cfff2900e31838f657fcafe30),
  a June 2025 reland of a July 2024 patch.

Previously, fragment offset computation was lazily performed by
`getFragmentOffset`. The section that converged the slowest
determined other sections' iteration steps, leading to some unneeded
computation.

The new layout algorithm assigns fragment offsets and iteratively
refines them for each section until it's optimized. Then, it moves on to
the next section. If relaxation doesn't change anything, fragment offset
assignment will be skipped. This way, sections that converge quickly
don't have to wait for the slowest ones, resulting in [a
significant decrease in compile time for full LTO](https://llvm-compile-time-tracker.com/compare.php?from=0387cd052b081d6bc9856ef756942a5df1a2a301&to=1a47f3f3db66589c11f8ddacfeaecc03fb80c510&stat=instructions%3Au&linkStats=on).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` bool MCAssembler::relaxOnce() {   bool ChangedAny = false;   for (MCSection &Sec : *this) {     auto MaxIter = NumFrags + 1;     uint64_t OldSize = getSectionAddressSize(Sec);     do {       uint64_t Offset = 0;       Changed = false;       for (MCFragment &F : Sec) {         if (F.Offset != Offset) {           F.Offset = Offset;           Changed = true;         }         relaxFragment(F);         Offset += computeFragmentSize(F);       }        Changed |= OldSize != Offset;       ChangedAny |= Changed;       OldSize = Offset;     } while (Changed && --MaxIter);     if (MaxIter == 0)       return false;   }   return ChangedAny; } ``` |

## Symbols

@aengelke made
two noticeable performance improvements:

* [[MC] Don't
  evaluate name of unnamed symbols](https://github.com/llvm/llvm-project/pull/95021)
* [[MC]
  Eliminate two symbol-related hash maps](https://github.com/llvm/llvm-project/pull/95464)

In `MCObjectStreamer`, newly defined labels were put into
a "pending label" list and initially assigned to a
`MCDummyFragment` associated with the current section. The
symbols will be reassigned to a new fragment when the next instruction
or directive is parsed. This pending label system, while necessary for
aligned bundling, introduced complexity and potential for subtle
bugs.

To streamline this, I [revamped
the implementation](https://github.com/llvm/llvm-project/commit/75006466296ed4b0f845cbbec4bf77c21de43b40) by directly adjusting offsets of existing
fragments, eliminating over 100 lines of code and reducing the potential
for errors.

Details: In 2014, [[MC]
Attach labels to existing fragments instead of using a separate
fragment](https://reviews.llvm.org/D5915) introduced `flushPendingLabels` aligned bundling
assembler extension for Native Client. [[MC] Match labels to existing
fragments even when switching sections.](https://reviews.llvm.org/D71368), built on top of
`flushPendingLabels`, added further complication.

In `MCObjectStreamer`, a newly defined label was
temporarily assigned to a `MCDummyFragment`. The symbol would
be reassigned to a new fragment when the next instruction or directive
was parsed. The `MCDummyFragment` was not in the section's
fragment list. However, during expression evaluation, it should be
considered as the temporary end of the section.

For the following code, aligned bundling requires that
`.Ltmp` is defined at `addl`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` $ clang var.c -S -o - -fPIC -m32 ... .bundle_lock align_to_end   calll   .L0$pb .bundle_unlock .L0$pb:   popl    %eax .Ltmp0:   addl    $_GLOBAL_OFFSET_TABLE_+(.Ltmp0-.L0$pb), %eax ``` |

Worse, a lot of directive handling code had to add
`flushPendingLabels` and a missing
`flushPendingLabels` could lead to subtle bugs related to
incorrect symbol values.

( `MCAsmStreamer` doesn't call
`flushPendingLabels` in its handlers. This is the reason that
we cannot change `MCAsmStreamer::getAssemblerPtr` to use a
`MCAssembler` and change
`AsmParser::parseExpression`. )

## Sections

Section handling was also refined. MCStreamer maintains a a section
stack for features like
`.push_section`/`.pop_section`/`.previous`
directives. Many functions relied on the section stack for loading the
current section, which introduced overhead due to the addi...