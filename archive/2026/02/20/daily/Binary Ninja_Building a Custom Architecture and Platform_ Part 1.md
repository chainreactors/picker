---
title: Building a Custom Architecture and Platform: Part 1
url: https://binary.ninja/2026/02/20/quark-platform-part-1.html
source: Binary Ninja
date: 2026-02-20
fetch_date: 2026-02-21T04:00:27.201633
---

# Building a Custom Architecture and Platform: Part 1

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

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## Building a Custom Architecture and Platform: Part 1

* [Glenn Smith](https://github.com/CouleeApps)
* 2026-02-20
* [reversing](/tag/reversing), [decompiler](/tag/decompiler), [architecture](/tag/architecture)

![Quark](/blog/images/quark/solder-good.png)

From the beginning, the most important feature of Binary Ninja has been our API. The goal is simple: your plugins should be capable of producing the same high-quality decompilation as our official architectures. In this three-part series, we will implement a complete architecture and platform using some lesser-known features in Binary Ninja. From disassembly and lifting, to calling conventions, Type Libraries, and function signatures, we will explore the many steps involved in getting and refining decompilation results. The series is intended to be used both as a roadmap for how to build your own architecture plugin and as ideas for how to improve an existing one you might already have.

## Contents

This is Part 1 of a three-part series. When the other posts are live, weâll link them from here:

* [Target](#target)
* [Setup](#setup)
* [Part 1: Disassembly](#disassembly)
  + [Decoding](#decoding)
  + [Disassembly Text](#disassembly-text)
  + [Control Flow](#control-flow)
  + [Addendum](#addendum)
  + [Patching](#patching)
  + [Assembling](#assembling)
* Part 2: Lifting
* Part 3: Platform Support

# Target

The target of these new tools is the custom VM-based architecture Quark, available as a compilation backend in Binary Ninjaâs [Shellcode Compiler](https://github.com/Vector35/scc) (SCC). It comes complete with an interpreter, a standard library, and a full compiler suite for creating test programs. Having a toolchain available to produce objects for the target was quite helpful during implementation, as assumptions we make about how the target works can be tested relatively easily, and getting sample binaries was not an issue.

The architecture is a 32-bit register-based VM with 68 instructions, including a full set of load/store, arithmetic, and control flow operations. All instructions are packed into 4 bytes, and execution is a simple switch-based loop with each instruction acting independently. Conditional branches are handled by every instruction having the option to be conditionally executed, which is only used for jumps in compiled executables but could theoretically apply to any instruction. It has 32 4-byte registers, including a stack pointer, addressable instruction pointer, a link register, and four flags that can be used with any operation. A standard library of functions is [included](https://github.com/Vector35/scc/tree/master/runtime), with a decent amount of the C standard implemented. Library functions are always statically linked (no dynamic linking), and it uses system calls based on the operating system executing the VM. Overall, while the architecture is pretty simple, the full compiler and standard library make it good for demonstrating Binary Ninjaâs extensive set of features available for you to use.

# Setup

The first step in creating a plugin for a custom architecture is defining an Architecture subclass. We need to fill out a bunch of metadata about the architecture, most of which will not be used until much later.

```
class QuarkArch(Architecture):
    name = "Quark"
    endianness = Endianness.LittleEndian
    address_size = 4
    default_int_size = 4
    instr_alignment = 1
    max_instr_length = 4
    regs = {
        'sp': RegisterInfo('sp', 4),
        # ...
        'lr': RegisterInfo('lr', 4),
        # ...
        # Note: IP register can be defined here, but we will not use it (explained later)
    }
    stack_pointer = 'sp'
    link_reg = 'lr'

QuarkArch.register()
```

SCC conveniently [gives us](https://scc.binary.ninja/scc.html) the option to produce object files as ELFs, so we will not need to write a BinaryView file format parser for this project. We can register our new architecture with the existing ELF loader, and Binary Ninja will automatically pick up the custom machine type and start using our new architecture without needing to click anything in the UI:

```
# Later, we will see this is not a complete solution
# But for now, we can register with the appropriate machine type (4242),
# and then loading a Quark ELF will automatically create a start function
# at the entry point using the Quark architecture.
BinaryViewType['ELF'].register_arch(4242, Endianness.LittleEndian, Architecture['Quark'])
```

![No decoding yet, but we now have a Quark function created at the entry point.](/blog/images/quark/setup-entry-point.png)
*No decoding yet, but we now have a Quark function created at the entry point.*

It might not look like much yet, but thanks to Binary Ninjaâs [existing ELF parser](https://github.com/Vector35/binaryninja-api/tree/dev/view/elf), we get to skip a significant amount of work parsing binary files, and we can skip directly to decoding bytes.

# Disassembly

## Decoding

Before we can disassemble the instructions, we need to decode them. In the case of Quark, instructions are always 4 bytes, in a single stream, and there are no segments to differentiate between code and data ([a Von Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)). Binary Ninja will feed instructions to our subclassâs implementations of [`get_instruction_info`](https://api.binary.ninja/binaryninja.architecture-module.html#binaryninja.architecture.Architecture.get_instruction_info) and [`get_instruction_text`](https://api.binary.ninja/binaryninja.architecture-module.html#binaryninja.architecture.Architecture.get_instruction_text) to determine instruction size and text. We can make a trivial implementation of both and see instructions start lining up:

```
    def get_instruction_info(self, data: bytes, addr: int) -> Optional[InstructionInfo]:
        result = InstructionInfo()
        result.length = 4
        return result

    def get_instruction_text(self, data: bytes, addr: int) -> Optional[Tuple[List['function.InstructionTextToken'], int]]:
        tokens = []
        # We will fill out tokens in the next section
        return tokens, 4
```

![Our instructions, ready to be decoded](/blog/images/quark/instructions-raw.png)
*Our instructions, ready to be decoded*

Quark packs a number of different fields into each 4-byte instruction using bit-shifts and masks to read out opcode, operands, and conditions. We can look at [the interpreter source](https://github.com/Vector35/scc/blob/master/runtime/quark_vm.c) to see precisely how this is done:

```
uint32_t instr = *(uint32_t*)(r[IP]);
uint32_t cond = instr >> 28;
uint32_t op = (instr >> 22) & 0x3f;
uint32_t a = (instr >> 17) & 31;
uint32_t b = (instr >> 12) & 31;
uint32_t c = (instr >> 5) & 31;
uint32_t d = instr & 31;
// ...
```

We can model this in Python with a bit of structure unpacking and integer math:

```
class QuarkInstruction:
    def __init__(self, instr: int):
        self.instr = instr

    @property
    def cond(self):
        return self.instr >> 28

    @property
    def op(self):
        return (self.instr >> 22) & 0x3f

    @property
    def a(self):
    ...