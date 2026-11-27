---
title: A direct -O0 code generator for LLVM
url: https://maskray.me/blog/llvm-direct-o0-code-generator
source: MaskRay
date: 2026-11-26
fetch_date: 2026-11-27T10:16:05.183269
---

# A direct -O0 code generator for LLVM

[Skip to content](#main-content)

[MaskRay](https://maskray.me/blog/)

* [Archives](https://maskray.me/blog/archives)
* [tags](https://maskray.me/blog/tags)
* [Feeds](https://maskray.me/feeds/)
* [TIL](https://maskray.me/til/)
* [Presentations](https://maskray.me/presentations/)

# A direct -O0 code generator for LLVM

[MaskRay](https://maskray.me/blog "MaskRay")
* 26th Nov 2026
* â¢15 min read
* â¢Tags:
* [llvm](https://maskray.me/blog/tags/llvm/)

### Table of Contents

* [Where -O0 back-end time goes](#where-o0-back-end-time-goes)
* [Prior art](#prior-art)
* [What "direct" means](#what-direct-means)
* [The value model](#the-value-model)
* [Two targets](#two-targets)
* [What a skipped pipeline owes](#what-a-skipped-pipeline-owes)
* [-S must print what -c encodes](#s-must-print-what-c-encodes)
* [Debug info without a MachineFunction](#debug-info-without-a-machinefunction)
* [Exceptions](#exceptions)
* [MC became the bottleneck](#mc-became-the-bottleneck)
* [Compile time](#compile-time)
* [Code size and quality](#code-size-and-quality)
* [How it was tested](#how-it-was-tested)
* [Compared with FastISel and GlobalISel](#compared-with-fastisel-and-globalisel)
* [Open questions](#open-questions)
* [Status](#status)

This post describes an experiment that compiles a function directly from LLVM IR to machine code bytes, without building a `MachineFunction`, and falls back to the regular pipeline one function at a time.
On the compile-time tracker, `clang -O0 -g` builds take 14% fewer instructions on x86-64 and 21% fewer on AArch64.
The generated code is 10% larger on x86-64 and about the same size on AArch64, and `clang -S` output assembles to the same code that `clang -c` emits.
Skipping the pipeline creates an obligation, and most of this post is about that obligation.

This post relies heavily on an LLM agent (Claude Code).
It wrote most of the code and drafted this post, which I then edited.
My part was steering.

## Where `-O0` back-end time goes

Within the back end, the cost is spread out: FastISel with its SelectionDAG fallback, RegAllocFast, prologue/epilogue insertion, the remaining machine IR passes, legacy pass manager overhead, and MC lowering.
Shares of back-end cycles from a profile (`llc -O0 -relocation-model=pic` on x86-64, no assertions, bitcode parsing excluded, tramp3d built with `-fno-exceptions`), good to a few points:

| Layer | sqlite3 | tramp3d | sqlite3 -g | tramp3d -g |
| --- | --- | --- | --- | --- |
| ISel (FastISel, SelectionDAG, driver) | 43% | 28% | 30% | 19% |
| RegAllocFast | 10% | 8% | 7% | 6% |
| Prologue/epilogue insertion | 6% | 7% | 4% | 5% |
| IR preparation passes | 7% | 9% | 6% | 6% |
| Legacy pass manager | 5% | 10% | 3% | 7% |
| MachineFunction allocation, other MIR passes, CFI | 9% | 8% | 7% | 6% |
| LiveDebugValues | 0% | 1% | 9% | 9% |
| AsmPrinter (MI to MCInst) | 7% | 6% | 6% | 5% |
| MC encoding, streamer, object writer | 11% | 22% | 10% | 17% |
| DWARF and `.eh_frame` emission | 1% | 2% | 19% | 22% |

`llc -O0 -mtriple=x86_64 -debug-pass=Structure` on `define void @f() { ret void }` prints 72 entries under the function pass manager, counting repeated analyses, the printer and `Free MachineFunction`.
An excerpt:

```
    FunctionPass Manager
      Expand IR instructions
      Expand Atomic instructions
      ...
      Exception handling preparation
      Prepare inline asm insts
      Safe Stack instrumentation pass
      Insert stack protectors
      Module Verifier
      Assignment Tracking Analysis
      X86 DAG->DAG Instruction Selection
      ...
      Eliminate PHI nodes for register allocation
      Machine Register Class Info Analysis
      Fast Register Allocator
      ...
      Prologue/Epilogue Insertion & Frame Finalization
      Post-RA pseudo instruction expansion pass
      X86 pseudo instruction expansion pass
      Insert KCFI indirect call checks
      Analyze Machine Code For Garbage Collection
      Insert fentry calls
      Insert XRay ops
      Implement the 'patchable-function' attribute
      X86 Indirect Branch Tracking
      ...
      Live DEBUG_VALUE analysis
      ...
      X86 Indirect Thunks
      X86 Return Thunks
      Check CFA info and insert CFI instructions if needed
      X86 Load Value Injection (LVI) Ret-Hardening
      ...
      X86 Assembly Printer
      Free MachineFunction
```

## Prior art

FastISel (2008) selects most instructions itself, hands the rest of a block to SelectionDAG when it cannot, and then runs the full MIR pipeline.
GlobalISel is the AArch64 `-O0` default.

TPDE is a single-pass back end with per-module fallback, no DWARF, and its own ELF writer.

What this experiment adds is fallback per function into the same object file, debug info, respect for function attributes, hardening, and text output.

The advantages worth claiming are structural: a small delta inside LLVM, the regular pipeline as a differential oracle for every function, per-function fallback, and reused DWARF and object writing.

## What "direct" means

IR goes to encoded bytes with no MIR in between.
It is not "one pass": the bytes are patched afterwards, and emission still goes through AsmPrinter and MC.

`DirectCodeGen` is a function pass, first in the `-O0` codegen function pass manager, enabled by `-direct-codegen`.
It compiles a function into a private buffer: bytes, fixups, CFI points, line rows, variable slots, and a call-site table.
Nothing shared is touched until the function succeeds, and the IR is never modified.
On success, `AsmPrinter::emitCompiledFunction` emits the function header, the bytes and the tables, and the pass tells the pass manager to skip the remaining passes for this function.
On failure, the function takes the regular pipeline into the same object file.

```
IR function
    |
DirectCodeGen pass ---- any failure ----> regular pipeline
    |                                    (ISel, MIR passes, AsmPrinter)
    | success                                  |
AsmPrinter::emitCompiledFunction               |
    |                                          |
MCStreamer: the same .o or .s  <---------------+
```

Section selection, linkage, alignment, DWARF and the object writer are reused, because they are not where the time goes.
`-direct-codegen-report` prints the reason for each fallback, and `-direct-codegen-abort` turns a fallback into an error.

## The value model

* Static allocas live in fixed frame slots.
* A value with one use in its own block lives only in a register.
* Any other value is stored to its own slot at the definition. Its register stays as a clean copy that can be dropped without emitting code.
* Only caller-saved registers are used, so calls need no save and restore. The frame pointer is always set up.
* PHI moves happen on edges, with a temporary when PHIs of one block read each other.

A compare used only by its branch, a load used only by the next instruction, and a constant-offset address are folded into their user.

Here is a small function with a local, a branch and a call:

```
struct S { int n, count; };
int g(int);
int f(struct S *p, int d) {
  int t = d * 2;
  if (t > 0)
    p->count += g(t);
  return p->count;
}
```

`clang -O0 -emit-llvm` gives, trimmed to the instructions:

```
entry:
  %p.addr = alloca ptr, align 8
  %d.addr = alloca i32, align 4
  %t = alloca i32, align 4
  store ptr %p, ptr %p.addr, align 8
  store i32 %d, ptr %d.addr, align 4
  %0 = load i32, ptr %d.addr, align 4
  %mul = mul nsw i32 %0, 2
  store i32 %mul, ptr %t, align 4
  %1 = load i32, ptr %t, align 4
  %cmp = icmp sgt i32 %1, 0
  br i1 %cmp, label %if.then, label %if.end
if.then:
  %2 = load i32, ptr %t, align 4
  %call = call i32 @g(i32 noundef %2)
  %3 = load ptr, ptr %p.addr, align 8
  %count = getelementptr inbounds nuw %struct.S, ptr %3, i32 0, i32 1
  %4 = load i32, ptr %count, align 4
  %add = add nsw i32 %4, %call
  store i32 %add, ptr %count, align 4
  br label %if.end
if.end:
  %5 = load ptr, ptr %p.addr, align 8
  %count1 = getelementptr ...