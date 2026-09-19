---
title: Auditing in the age of (good enough) AI
url: https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
source: The Trail of Bits Blog
date: 2026-09-18
fetch_date: 2026-09-19T07:01:09.168891
---

# Auditing in the age of (good enough) AI

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Auditing in the age of (good enough) AI

[Fredrik Dahlgren](/authors/fredrik-dahlgren/)

September 18, 2026

[cryptography](/categories/cryptography/), [zero-knowledge](/categories/zero-knowledge/), [static-analysis](/categories/static-analysis/), [ai](/categories/ai/)

Page content

* [Auditing the Miden zkVM](#auditing-the-miden-zkvm)
* [Building all the tools!](#building-all-the-tools)
* [Finding all the bugs!](#finding-all-the-bugs)
* [But what if there are no bugs?](#but-what-if-there-are-no-bugs)
* [Why we couldn’t have done this two years ago](#why-we-couldnt-have-done-this-two-years-ago)

Security firms have published numerous blog posts describing how they pointed their agent harness at a codebase and found dozens of bugs ([we’re one of them](/tags/patch-the-planet/)). However, these posts tend to focus on agentic code review, which is just one aspect of how we use AI in our security reviews. We want to give a different perspective: before code review even starts, agents now allow us to build custom tooling and formal models that improve the quality and depth of our reviews.

We recently reviewed the Miden VM, a new zero-knowledge VM with its own custom assembly language and almost no developer tooling. To prepare, we spent six months having our agents build an [LSP server](https://github.com/trailofbits/masm-lsp), a [decompiler](https://github.com/trailofbits/masm-decompiler), a [static analysis engine](https://github.com/trailofbits/masm-lsp/tree/main/crates/masm-analysis), and a [Lean model of the VM executor](https://github.com/trailofbits/masm-lean) from scratch. These tools found real security issues, like an unvalidated prover-supplied input that would let a malicious prover forge Falcon signatures and steal funds from Miden account holders. Additionally, the Lean work produced 95 machine-checked correctness proofs, covering a large component of the Miden core library.

## Auditing the Miden zkVM

In late 2025, the Miden team came to us to have parts of their [zero-knowledge VM](https://docs.miden.xyz/reference/miden-vm/) reviewed before launch. Part of the review was scoped to cover the Miden core library, which contains a small set of cryptographic primitives written in a custom assembly language called [Miden assembly](https://docs.miden.xyz/reference/miden-vm/user_docs/assembly/) (MASM). This made us genuinely excited, as it was right up our alley: a high-assurance project writing complex cryptographic code in a low-level custom assembly language that we had never seen before. At the same time, it also presented some unique challenges.

![“Two code listings side by side: a MASM procedure computing the XOR of two 128-bit values, and the same procedure implemented in 32-bit x86 assembly”](/2026/09/18/auditing-in-the-age-of-good-enough-ai/auditing-ai-figure-1_hu_e9e13470729ab3cb.webp)

Figure 1: The left image shows a MASM procedure computing the XOR of two 128-bit values (represented as 32-bit limbs). The right image shows the same procedure implemented using 32-bit x86 assembly code.

To start, the Miden VM implements a [stack-machine architecture](https://en.wikipedia.org/wiki/Stack_machine). This means that each instruction operates on values read from the stack, and the result of the instruction is then written back to the top of the stack. While conceptually simple, this makes code written in MASM challenging to review, since instruction inputs and outputs are read from the stack and are always implicit. Additionally, since the Miden VM is a completely new architecture, very little existed in terms of developer tooling like IDE support, Language Server Protocol (LSP) servers, and linters.

We knew that we had six months to prepare for the review, since the implementation was not yet feature complete, so we asked ourselves: *“What could we spend our time and tokens on to make sure that the review would root out as many bugs as possible in the codebase?”*

## Building all the tools!

Since MASM lacked developer tooling, we started out by asking ourselves what kind of tools we would like to have available when the project started. We typically use VS Code to review code, and syntax highlighting and code navigation are essential for readability and being able to follow data flow throughout a codebase. We needed an LSP server and a corresponding VS Code extension for this, and within a few days we had Claude build a [working prototype](https://github.com/trailofbits/masm-lsp) that provided most of the functionality we wanted: features like syntax highlighting, goto definition, finding code references, and displaying procedure docstrings on hover. With these fundamental features in place, we also decided to add more language-specific features like displaying inline instruction documentation, and stack effects for individual instructions.

![“Figure showing code annotated with inline stack effects and instruction documentation helps prevent the context switch required to look up instruction semantics elsewhere”](/2026/09/18/auditing-in-the-age-of-good-enough-ai/auditing-ai-figure-2_hu_a8d3f4dbce9cf99f.webp)

Figure 2: Annotating the code with inline stack effects and instruction documentation helps prevent the context switch required to look up instruction semantics elsewhere.

Having built the LSP server, we started thinking about other ways to provide high-level semantic information to support manual and agent-driven review. We thought it would be interesting to see if we could provide faithful decompilation for MASM procedures inside the VS Code UI, to help the reviewer quickly understand the high-level control flow and data flow of the procedures they were looking at. For MASM, this is a harder problem than it first appears. Stack machine lifting and decompilation is a well-studied problem, but decompiling hand-written MASM is still difficult for a number of reasons.

1. Most procedures in the core library do not have declared signatures, which means that the number of inputs and outputs must be inferred from context.
2. MASM procedures do not conform to a well-defined calling convention, and the net stack effect of such calls is generally impossible to determine statically. This means that all analysis failures propagate up the call chain.
3. While-loops do not need to be stack neutral, which means that the while-loop condition may occupy a different stack slot in each iteration. This also makes it impossible to map instruction inputs to stack slots for subsequent instructions.
4. Different branches in conditional statements may have different stack effects, which similarly makes stack tracking and signature inference challenging.

This meant that we could not expect to be able to decompile all MASM procedures if we also wanted the decompiled output to be correct. We therefore focused on decompiling a well-defined subset of MASM correctly. During the development of the decompiler, we alternated between using Claude for planning and development and Codex for code review. Whenever we had implemented a new feature, we had agents decompile a randomized set of procedures from the core library and compare the result to the original MASM to look for regressions. Any issues found were added as regression tests to be fixed by the model.

![“The eqz MASM procedure shown above its decompiled pseudocode”](/2026/09/18/auditing-in-the-age-of-good-enough-ai/auditing-ai-figure-3_hu_c721639b7435d1e3.webp)

Figure 3: The `eqz` procedure, which tests if a 256-bit integer (represented as eight 32-bit limbs) is equal to zero, together with the corresponding decompiled pseudocode

[The decompiler](https://github.com/trailofbits/masm-decompiler) represented the single largest effort of the tooling development for this project, with over 100 AI-generated commits over multiple months. The main benefit of this wor...