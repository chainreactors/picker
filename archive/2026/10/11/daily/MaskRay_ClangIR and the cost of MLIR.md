---
title: ClangIR and the cost of MLIR
url: https://maskray.me/blog/clangir-and-the-cost-of-mlir
source: MaskRay
date: 2026-10-11
fetch_date: 2026-10-12T08:13:30.155706
---

# ClangIR and the cost of MLIR

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-10-11](/blog/clangir-and-the-cost-of-mlir)

# ClangIR and the cost of MLIR

ClangIR (CIR) is an MLIR dialect between the AST and LLVM IR, and in
October 2026 the clang area team [accepted
building it by default](https://discourse.llvm.org/t/rfc-enable-clangir-build-by-default/91730/100). CIR is built on MLIR because each step along
the way was locally reasonable, and together the steps locked MLIR in.
The costs (build time, binary size, MLIR API churn) land largely on
Clang contributors who neither chose MLIR nor use CIR.

This post traces how CIR came to depend on MLIR, collects what the
dependency costs, and uses an MLIR-free CIR as a thought experiment to
separate the costs inherent to MLIR from those that can be reduced.

This post relies heavily on an LLM agent (Claude Code). It read the
Discourse threads, GitHub PRs, slides, and the source tree, computed the
build-closure and contributor numbers, and drafted the text, which I
then edited. My part was steering, and some of what I added to its
context:

* the build-by-default and premerge-testing RFCs, and a discussion on
  Discord #llvm;
* the opportunity-cost framing: contributors without fast machines pay
  for MLIR (and Flang) on every llvm/ change, though most of them never
  use either.

Treat the numbers as checked but not peer-reviewed.

## What ClangIR replaces

Classic Clang lowers the AST to LLVM IR in
`clang/lib/CodeGen`. With `-fclangir`,
`clang/lib/CIR/CodeGen` (CIRGen) emits CIR instead, a set of
CIR passes runs, CIR is converted to MLIR's `llvm` dialect,
and MLIR translates that to LLVM IR.

* CIRGen mirrors the AST-to-IR half of `clang/lib/CodeGen`
  file by file: `CodeGenFunction` becomes
  `CIRGenFunction`, `CGExprScalar.cpp` becomes
  `CIRGenExprScalar.cpp`, and so on. It is 66K lines against
  CodeGen's 214K, with 786 `errorNYI` calls marking what is
  missing.
* Work that classic CodeGen does while emitting IR becomes separate
  CIR passes: C++ ABI lowering (`CXXABILowering`), calling
  conventions (`CallConvLowering`), exception handling
  (`EHABILowering`), and structured control flow to a CFG
  (`FlattenCFG`).
* The optimizer and backend are not replaced. CIR's frontend action
  calls `emitBackendOutput` from
  `clang/lib/CodeGen/BackendUtil.cpp`, so
  `clangCIRFrontendAction` links
  `clangCodeGen`.
* Some code is shared rather than duplicated:
  `clang/lib/CodeGenUtils` ([#221001](https://github.com/llvm/llvm-project/pull/221001),
  September 2026) holds AST-only helpers used by both, and
  `llvm/lib/ABI` (LLVMABI) does ABI classification for CIR's
  calling-convention lowering and, under
  `-fexperimental-abi-lowering`, for classic CodeGen.
* Nothing in `clang/lib/Analysis` is replaced yet. The CFG,
  the analyses behind Sema's analysis-based warnings, the dataflow
  framework, lifetime safety, and the Static Analyzer all still work on
  the AST and the CFG. Upstream CIR's only analysis is an alias analysis
  used by ABI lowering. Replacing CFG-based analysis is an aspiration
  rather than a plan: the 2022 RFC argued that the CFG is "discarded after
  analysis" and "has lots of known problems", and the area team expects
  CIR to replace "the current CodeGen and CFG analysis", but no ClangIR
  document schedules it.

The in-tree roadmap, [`clang/docs/CIR/CodeDuplication.md`](https://github.com/llvm/llvm-project/blob/main/clang/docs/CIR/CodeDuplication.md),
is about CodeGen. It plans to raise CIR to a higher level, move ABI
details into later lowering passes, and "replace relevant parts of the
existing implementation, piece by piece" with implementations shared by
both code generators. Calling conventions are the first case (LLVMABI,
plus an MLIR adapter that FIR can also use). The roadmap lists the next
candidates: constant expression evaluation, complex multiplication and
division, builtins, exception handling and C++ cleanups, inline
assembly, and C++ ABI handling (vtables, virtual calls, constructor and
destructor arguments, dynamic casts, base class addresses, type
descriptors, array new and delete). Linkage, alignment, debug info,
TBAA, sanitizers, and lifetime markers are spread through CodeGen and
listed as harder to share. It also aims to run all classic CodeGen tests
through the CIR path.

## Where things stand

The area team's decision says "ClangIR is likely to reach the point
where it becomes the replacement for the current CodeGen and CFG
analysis." The same post promises that
`-DCLANG_ENABLE_CIR=Off` "will still be a supported
configuration for the forseeable future", and `-fclangir`
stays off by default. On main, `clang/CMakeLists.txt` tests
`CLANG_ENABLE_CIR` but declares no `option()` for
it, so the flip is still pending.

A separate RFC, [Add
CIR testing to clang and MLIR CI](https://discourse.llvm.org/t/rfc-add-cir-testing-to-clang-and-mlir-ci/92452) ([#227834](https://github.com/llvm/llvm-project/pull/227834)),
would build and test CIR in premerge for clang/ and mlir/ changes. nikic
is [weakly
-1](https://discourse.llvm.org/t/rfc-add-cir-testing-to-clang-and-mlir-ci/92452/9): if contributors have to fix CIR failures, "they also need to
build and test CIR locally", so premerge testing and build-by-default
"should go hand in hand". rengolin [calls](https://discourse.llvm.org/t/rfc-add-cir-testing-to-clang-and-mlir-ci/92452/10)
asking non-CIR developers to stub out CIR breakage "an unreasonable
request" and suggests a different CI setup.

As for the compiler itself, the [ClangIR
progress report for September 2026](https://discourse.llvm.org/t/clangir-progress-report-september-2026/91947) measures `-fclangir`
against classic CodeGen: 1.32x the wall time on a typical file, 1.57x
across the tree, 1.17x the memory, and 3% more code.

## Why MLIR

### Meta, 2022: framework reuse for a lifetime checker

ClangIR started at Meta in October 2021. Bruno Cardoso Lopes and
Nathan Lanza proposed it in [RFC:
An MLIR based Clang IR (CIR)](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319) in June 2022, and it moved to an LLVM
incubator in August 2022 (timeline from the [2025
keynote](https://llvm.org/devmtg/2025-10/slides/keynotes/kaylor_lopes.pdf)). The primary goal was "improved diagnostics for modern
C++"; the design had "grown out of implementing a lifetime
analysis/checker pass"; optimization and lowering were "a secondary goal
for now". Clang lacked a suitable IR: the AST is awkward for dataflow,
LLVM IR is too low level, and the Clang CFG is discarded after analysis.
The RFC's entire "Why MLIR?" section reads:

> MLIR provides a solid and tested framework to build custom IR and run
> passes. Among several other capabilities, it's also in already in tree
> and used by Flang to build FIR.

Nobody in the thread argued for a bespoke IR; the closest was John
McCall's [aside](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319/31)
that if MLIR needed in-tree dialects to be useful, "it would be better
to just not use MLIR" and write the IR "from scratch on top of
llvm::ilist". efriedma [wrote](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319/2)
"using MLIR to build it seems like the right approach" and objected to
structured control flow instead. GÃ¡bor HorvÃ¡th [argued](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319/4)
that the CFG suffices for lifetime analysis, and John McCall [wanted](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319/15)
a two-stage lowering like Swift's. Reid Kleckner [asked](https://discourse.llvm.org/t/rfc-an-mlir-based-clang-ir-cir/63319/12)
for an agreed compile-time ceiling, "like +15-25%, before making this
part of the default pipeline". `-fclangir` is still opt-in,
and 1.32x/...