---
title: Striga: Lifting x86 to LLVM IR with Python
url: https://secret.club/2026/05/21/striga.html
source: Over Security
date: 2026-05-21
fetch_date: 2026-05-22T06:08:16.497003
---

# Striga: Lifting x86 to LLVM IR with Python

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Striga: Lifting x86 to LLVM IR with Python

![main authors image](/assets/author_img/mrexodia.jpg)  [mrexodia](/author/mrexodia)

 May 21, 2026

---

## [Background](#background)

While discussing with [eversinc33](https://x.com/eversinc33) about lifting [BinaryShield](https://connorjaydunn.github.io/blog/posts/binaryshield-a-bin2bin-x86-64-code-virtualizer/) to LLVM IR I decided it would be useful to write a basic lifter in Python that can lift x86\_64 instructions to LLVM IR. He has since released his blog post: [Writing a Naive LLVM-based Devirtualizer](https://eversinc33.com/2026/05/07/llvm-devirtualizer), which I highly recommend you check out! This post assumes familiarity with the basics of LLVM IR. You can find some references at the end of this post.

Over the years I noticed that a lot of people get stuck exploring lifters, because existing tooling is too difficult to compile. In October 2025 I spent around a month redoing Remill’s build system ([remill#723](https://github.com/lifting-bits/remill/pull/723)) and earlier this month I did the same for the Dna project ([Dna#9](https://github.com/Colton1skees/Dna/pull/9)). Last year I also started working on [Python bindings for LLVM](https://github.com/LLVMParty/llvm-nanobind), which I wanted to use for a real project. You can find the lifter at [LLVMParty/striga](https://github.com/LLVMParty/striga).

The goal of this post is to lower the barrier of entry and let you experiment with lifting to LLVM IR. For inspiration you can look at the [Static Devirtualization of Themida](https://back.engineering/blog/09/05/2026/) post that was just released by Back Engineering Labs, as well as the [Pushan: Trace-Free Deobfuscation of Virtualization-Obfuscated Binaries](https://arxiv.org/html/2603.18355v1) paper by ASU researchers published in March.

**If you enjoy this article and would like to learn more, see [my website](https://labs.ogilvie.pl/) for information about my in-person trainings.**

## [Lifting](#lifting)

Lifting is the process of translating assembly instructions to some kind of intermediate representation (IR). The motivation is usually that directly analyzing and manipulating (x86) assembly instructions is complex and error prone. The lifter translates the underlying instruction semantics directly to an IR that is easier to reason about (and therefore to manipulate as well).

A few popular IRs:

* SMT-LIB, used by [Triton](https://github.com/JonathanSalwan/Triton) (symbolic execution)
* [VEX](https://github.com/angr/pyvex), used by [angr](https://github.com/angr/angr)
* [Miasm](https://github.com/cea-sec/miasm) IR
* [Sleigh](https://github.com/lifting-bits/sleigh), used by [Ghidra](https://github.com/nationalsecurityagency/ghidra), [Remill](https://github.com/lifting-bits/remill) and [Icicle](https://github.com/icicle-emu/icicle-python)
* LLVM IR, used by [Rellume](https://github.com/aengelke/rellume), [revng](https://github.com/revng/revng) and Remill
* Microcode, used by [IDA](https://hex-rays.com/decompiler) (proprietary)
* BNIL, used by [Binary Ninja](https://binary.ninja) (proprietary)

For this project I picked LLVM IR, because I am the most familiar with it and it has a well-established ecosystem. LLVM already has all of the common compiler optimizations and it is used and maintained by teams at large corporations.

## [Architecture](#architecture)

The architecture of the lifter is very much inspired by [remill](https://github.com/lifting-bits/remill), but I simplified some things to make it easier to follow. In LLVM a *register* is actually an [SSA *value*](https://mapping-high-level-constructs-to-llvm-ir.readthedocs.io/en/latest/control-structures/ssa-phi.html), which means we can only assign to it once. CPU registers are *variables* that can be assigned to multiple times. We model this by creating a `State` structure in memory that represents the x86 CPU state:

```
struct State {
  uint64_t rax;
  uint64_t rbx;
  uint64_t rcx;
  uint64_t rdx;
  // ... GPRs
  uint8_t cf;
  uint8_t zf;
  uint8_t of;
  // ... Flags
  // ... XMM
};
```

Instructions that read or write to RAX will load/store to `State->rax`. If we play our cards right, the optimizer will use the [mem2reg](https://haqr.eu/tinyoptimizer/mem2reg/) pass to translate this into SSA form for us and enable further optimizations.

An important difference to an actual CPU is that flags are modelled as independent 8-bit registers. This makes it easier to reason about compared to a packed bitfield. For instance, it helps the optimizer to perform dead store elimination and propagation.

In addition to the `State`, we need an opaque `memory` pointer that helps us differentiate a `load/store` in the `State` from memory accesses by the x86 CPU. In short: the `State` pointer is used to model the CPU and the `memory` pointer is used to model the RAM. While lifting, the prototype of the lifted function is `void lifted(State* state, void* memory)`. Later on we will perform *brightening*, to turn this into something we can recompile.

Below is the LLVM IR for the instruction `mov rax, rcx`, with comments in pseudo-C:

```
define internal void @lifted_0x140001000(ptr %state, ptr %memory) {
initialize:
  ; uint64_t* rcx = &state->rcx;
  %rcx = getelementptr inbounds nuw %State, ptr %state, i32 0, i32 2

  ; uint64_t* rax = &state->rax;
  %rax = getelementptr inbounds nuw %State, ptr %state, i32 0, i32 0

  ; Jump to the first instruction
  br label %insn_0x140001000

insn_0x140001000:                                 ; preds = %initialize
  ; uint64_t v0 = *rcx;
  %0 = load i64, ptr %rcx, align 4

  ; *rax = v0;
  store i64 %0, ptr %rax, align 4

  ; Jump to the next instruction
  br label %insn_0x140001003

insn_0x140001003:                                 ; preds = %insn_0x140001000
  ; Block terminator to keep the IR valid
  ret void
}
```

We start out with the `initialize` block, which is used to get pointers to the relevant `State` members. Then every instruction gets its own basic block named `insn_<addr>`. Every instruction is responsible for emitting an unconditional branch to its successors. The basic block for the successor is created with just a `ret` [terminator](https://llvm.org/docs/LangRef.html#terminator-instructions), to keep the module verifier happy.

To illustrate memory accesses, here is the LLVM IR for `mov rax, qword [rbx+42]`:

```
define internal void @lifted_0x140001000(ptr %state, ptr %memory) {
initialize:
  %rbx = getelementptr inbounds nuw %State, ptr %state, i32 0, i32 1
  %rax = getelementptr inbounds nuw %State, ptr %state, i32 0, i32 0
  br label %insn_0x140001000

insn_0x140001000:                                 ; preds = %initialize
  ; uint64_t v0 = *rbx;
  %0 = load i64, ptr %rbx, align 4

  ; uint64_t v1 = v0 + 42;
  %1 = add i64 %0, 42

  ; uint8_t* v2 = &memory[v1];
  %2 = getelementptr i8, ptr %memory, i64 %1

  ; uint64_t v3 = *(uint64_t*)v2;
  %3 = load i64, ptr %2, align 1

  ; *rax = v3;
  store i64 %3, ptr %rax, align 4

  br label %insn_0x140001004

insn_0x140001004:                                 ; preds = %insn_0x140001000
  ret void
}
```

Here you can see the `getelementptr i8, ptr %memory, i64 %1` instruction which uses `memory` as a base, signaling that this is a read from the x86 memory (we will clean this up later).

The lifter itself is contained in a ~500 line `Semantics` class with these main functions (some are omitted for brevity):

```
# src/striga/semantics.py

class Semantics:
    def __init__(self, module: Module): ...

    # Lifting
    def begin(self, address: int) -> Function: ...
    def get_or_create_block(self, address: int) -> BasicBlock: ...
    def lift_bytes(self, address: int, code: bytes) -> list[Successor]: ...

    # Semantic helpers
    def reg_read(self, name: str) -> Value: ...
    def reg_write(self, name: str, value: Value): ...
    def mem_read(self, addr: Value, ty: Type) -> Value: ...
    def mem_write(...