---
title: Function-level Basic Block Analysis
url: https://binary.ninja/2025/08/12/function-level-basic-block-analysis.html
source: Binary Ninja
date: 2025-08-14
fetch_date: 2025-10-07T00:47:44.220793
---

# Function-level Basic Block Analysis

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Function-level Basic Block Analysis

* [Brandon Miller](https://github.com/zznop)
* 2025-08-12
* [reversing](/tag/reversing)

With the [5.1 Helion release](https://binary.ninja/2025/07/24/5.1-helion.html), we introduced a new capability for
architecture plugins that enables function-level basic block analysis by overriding the default implementation. This
feature provides powerful new flexibility for performing control-flow recovery on architectures where instruction-level
or even basic block-level analysis alone is inadequate for building an accurate control flow graph (CFG). In this post,
we demonstrate how this mechanism can be leveraged to resolve zero-overhead hardware loops and accurately identify
branch targets in parallel instruction pipelines.

## Motivation

Digital Signal Processor (DSP) architectures often feature complex control flow mechanisms that present unique
challenges for static analysis. For example, many DSPs implement zero-overhead loops where the loop control is managed
by special hardware features rather than explicit branch instructions. This can lead to situations where the control
flow graph (CFG) does not accurately reflect the intended execution path, especially when relying solely on
instruction-level analysis. Likewise parallel instruction pipelines can complicate the identification of branch targets,
as multiple instructions can execute simultaneously, leading to potential misinterpretation of control flow.

Consider this code example for Microchip PIC32, which features zero-overhead loops:

```
0x0039C   do #16383,0x03a2
0x0039E   nop
0x003A0   inc.w 0x000c
0x003A2   nop
```

The `do` instruction repeats a set of instructions *n*+1 times, where *n* is specified as a 14-bit constant or the lower
14 bits of any `W` register. In the code above, the `do` instruction stores the loop start address (the address of the
next instruction - `0x39e`) in the `DOSTART` register and the loop end address (`0x3a2`) in the `DOEND` register. It
also sets the `DOCOUNT` register to `16383`. Instructions from `0x39e` through `0x3a2` are repeated until the `DOCOUNT`
register reaches zero.

By default, Binary Ninjaâs core analysis engine invokes the architecture pluginâs `get_instruction_info` callback on
each instruction to determine its properties, such as whether the instruction includes branches. In the case of the
`do` assembly code above, `get_instruction_info` would be invoked on the `nop` instruction at `0x3a2`, which is not a
branch instruction. As a result, the core analysis engine would not recognize the loop structure, leading to an
incomplete or incorrect CFG.

Parallel instruction pipelines can also complicate control flow analysis. For example, consider the following assembly
code snippet from Qualcomm Hexagon architecture:

```
{
  if (p0) jump:nt 0x5b08;
  jump 0x5b7c;
  p0 = cmp.eq(r9,#9);
  r9 = add(r9, #1);
}
```

Hexagon packets can contain up to four instructions that execute in parallel. Hexagon also supports
[dot-new](https://docs.qualcomm.com/bundle/publicresource/topics/80-N2040-60/conditional-execution.html#v79-prm-dot-new-predicates) predicates,
where the processor can generate and use a scalar predicate in the same instruction packet. In the example
above, the instruction packet contains a conditional branch that depends on the value of `p0.new`, which is set by the
`cmp.eq` instruction. If the `p0.new` predicate is true, the processor will jump to `0x5b08`; otherwise, it will branch
to `0x5b7c`. `r9` is incremented by `1` prior to the branch. Processing this packet an instruction at a time would lead
to an incorrect interpretation of the control flow. It would result in the block ending at the first branch
instruction. A new block would be created on the next instruction, which jumps past the `cmp.eq` and `add`
instructions, causing code to be missed. In Hexagon, only one branch is taken per packet. If more than one branch is
eligible, the branch in the lowest execution slot number is taken.

## Function-level Basic Block Analysis

In Binary Ninja 5.1, we introduced a new callback in the architecture class
([`analyze_basic_blocks`](https://api.binary.ninja/binaryninja.architecture-module.html#binaryninja.architecture.Architecture.analyze_basic_blocks))
that allows plugins to implement a custom algorithm for performing function basic block analysis. This callback can be
used in lieu of
[`get_instruction_info`](https://api.binary.ninja/binaryninja.architecture-module.html#binaryninja.architecture.Architecture.get_instruction_info)
(or alongside it) to perform basic block analysis at the function level, rather than the instruction level.

To demonstrate this capability, I have updated my personal [Brain\*\*\*k](https://github.com/zznop/bn-brainfuck) architecture
plugin to use the new `analyze_basic_blocks` API to build an accurate control flow graph, eliminating a hack that was
previously required to handle loop structures.

### Brain\*\*\*k Overview

Brain\*\*\*k ([BF](https://esolangs.org/wiki/Brainfuck)) is one of the most famous (infamous, even?) esoteric programming
languages of all time. TL;DR - hereâs a simple Hello World program:

```
>+++++++++[<++++++++>-]<.>++++++[<+++++>-]<-.+++++++..+++.>>
+++++++[<++++++>-]<++.------------.<++++++++.--------.+++.------.--------.
>+.>++++++++++.
```

Each character in the program is an instruction that operates on a memory tape, which is an array of memory cells, each
initially set to zero. The pointer starts at the first cell and can be moved left or right. The description for each
instruction is listed in the table below.

| Instruction | Description |
| --- | --- |
| > | Move the pointer to the right |
| < | Move the pointer to the left |
| + | Increment the memory cell at the pointer |
| - | Decrement the memory cell at the pointer |
| . | Output the character signified by the cell at the pointer |
| , | Input a character and store it in the cell at the pointer |
| [ | Jump past the matching ] if the cell at the pointer is 0 |
| ] | Jump back to the matching [ if the cell at the pointer is nonzero |

## Brain\*\*\*k Basic Block Analysis

The BF `[` and `]` instructions are used to represent the start and end of loops. Conceptually, BF loops are similar to
zero-overhead loops in DSPs, where the loop control is managed by the interpreter (or hardware) rather than explicit
branch instructions. A `[` instruction caches the loop start address. When the `]` instruction is encountered, the
interpreter checks the value of the current memory cell. If it is zero, the interpreter jumps to the instruction after
the matching `]`. If it is nonzero, the interpreter jumps back to the matching `[`. To resolve the matching `[` and
build an accurate control flow graph, instruction-level analysis is insufficient. We need contextual information about
the entire function to connect the outgoing edge of the block that ends with a `[` instruction to the incoming edge of
the block with the matching `]`.

To implement this, Iâve overridden Binjaâs default basic block analysis algorithm by implementing the
`analyze_basic_blocks` callback in the BF architecture plugin. [The implementatio...