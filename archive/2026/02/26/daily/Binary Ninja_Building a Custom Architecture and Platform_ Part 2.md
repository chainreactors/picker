---
title: Building a Custom Architecture and Platform: Part 2
url: https://binary.ninja/2026/02/26/quark-platform-part-2.html
source: Binary Ninja
date: 2026-02-26
fetch_date: 2026-02-27T04:07:05.010617
---

# Building a Custom Architecture and Platform: Part 2

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

## Building a Custom Architecture and Platform: Part 2

* [Glenn Smith](https://github.com/CouleeApps)
* 2026-02-26
* [reversing](/tag/reversing), [decompiler](/tag/decompiler), [architecture](/tag/architecture)

![Quark](/blog/images/quark/robot-surgery.png)

Lifting is the critical step to unlocking Binary Ninjaâs powerful analysis and decompilation. Often the âleft as an exercise to the readerâ of Binary Ninja custom architecture tutorials, it is both a lengthy process and one with a lot of subtlety. From simple instructions to flags and intrinsics, the lifting process describes the behavior of every instruction. Letâs write a lifter for [Quark](/2026/02/20/quark-platform-part-1.html#target)!

## Contents

This is Part 2 of a three-part series. When the other posts are live, weâll link them from here:

* [Target](/2026/02/20/quark-platform-part-1.html#target)
* [Setup](/2026/02/20/quark-platform-part-1.html#setup)
* [Part 1: Disassembly](/2026/02/20/quark-platform-part-1.html#disassembly)
  + [Decoding](/2026/02/20/quark-platform-part-1.html#decoding)
  + [Disassembly Text](/2026/02/20/quark-platform-part-1.html#disassembly-text)
  + [Control Flow](/2026/02/20/quark-platform-part-1.html#control-flow)
  + [Addendum](/2026/02/20/quark-platform-part-1.html#addendum)
  + [Patching](/2026/02/20/quark-platform-part-1.html#patching)
  + [Assembling](/2026/02/20/quark-platform-part-1.html#assembling)
* [Part 2: Lifting](#lifting)
  + [Basics](#basics)
  + [Loads and Stores](#loads-and-stores)
  + [Calls](#calls)
  + [Arithmetic](#arithmetic)
  + [System Calls](#system-calls)
  + [Intrinsics](#intrinsics)
  + [Flags](#flags)
  + [Conditionals](#conditionals)
  + [Other](#other)
* Part 3: Platform Support

# Recap

In [Part 1](/2026/02/20/quark-platform-part-1.html), we covered the basics of disassembly. We implemented trivial control flow recovery, patching, and even added an assembler. Thanks to Binary Ninjaâs built-in ELF loader, we were able to skip writing a file format loader and spent the entire time turning instructions into tokens.

![State of the disassembly at the end of Part 1](/blog/images/quark/control-flow-branches.png)
*State of the disassembly at the end of Part 1*

# Lifting

To write a lifter, we need to implement `get_instruction_low_level_il`. The lifter needs the same information as the disassembler, so the scaffolding is very similar:

```
    def get_instruction_low_level_il(self, data: bytes, addr: int, il: LowLevelILFunction) -> Optional[int]:
        info = QuarkInstruction(int.from_bytes(data, 'little'))
        op = QuarkOpcode(info.op)

        match op:
            # Regular ops here
            case QuarkOpcode.integer_group:
                int_op = QuarkIntegerOpcode(info.b)
                match int_op:
                    # Integer ops have their own group
                    case _:
                        il.append(il.unimplemented())
            case QuarkOpcode.cmp:
                cmp_op = QuarkCompareOpcode(info.b & 7)
                match cmp_op:
                    # Comparison ops have their own group
                    case _:
                        il.append(il.unimplemented())
            case QuarkOpcode.icmp:
                cmp_op = QuarkCompareOpcode(info.b & 7)
                match cmp_op:
                    case _:
                        il.append(il.unimplemented())
            case _:
                il.append(il.unimplemented())
        return 4
```

From here, implementing the lifter involves going through every instruction in the disassembly and translating it into IL expressions, trying to keep it simple. Most operations in Quark translate cleanly into Low Level IL, though there are some weird outliers. Below we documented the cases we ran into while writing this, which hopefully covers anything you might run into.

## Basics

It is easier to understand lifters when there are helper functions that reduce the size of the code in each case. Given that, we will write a few helpers for looking up registers based on how the instructions usually operate.

```
        # Get name of register in `a` component of instruction
        def ra():
            # sanity: make sure we don't lift anything that references ip directly
            assert info.a != self.ip_reg_index, "Can't handle ip"
            return il.arch.get_reg_name(info.a)

        # Get expression to get the register in `a` component of instruction
        def ra_expr():
            # Special case ip register by emitting a constant with its value
            if info.a == self.ip_reg_index:  # ip
                return il.const(4, addr + 4)
            return il.reg(4, il.arch.get_reg_name(info.a))

        # Same exists for `b`, `c`, and `d` components of the instruction
```

We will also implement a helper for `cval`, the Quark equivalent of more complicated constant value and addressing mode encodings found in other architectures.

```
        def cval():
            if info.largeimm:
                return il.const(4, info.imm11)
            elif info.smallimm:
                return il.const(4, rol(info.imm5, info.d))
            else:
                if info.d == 0:
                    return rc_expr()
                il.append(il.set_reg(4, LLIL_TEMP(0), il.shift_left(4, rc_expr(), il.const(4, info.d))))
                return il.reg(4, LLIL_TEMP(0))
```

Having these helper functions available made the rest of lifting significantly more terse and easy to understand. *The power of being able to fit an entire instructionâs IL in one line cannot be understated.*

With all of this scaffolding in place, itâs time to start implementing instructions. We do this by grouping instructions into similar behaviors and writing lifter code for them, one at a time. Since every instruction is currently lifted as `unimplemented`, we can use the Tags sidebar to see which instructions we have yet to implement.

![Tags sidebar showing unimplemented instructions](/blog/images/quark/unimplemented-tags.png)
*Tags sidebar showing unimplemented instructions*

## Loads and Stores

Load and store instructions are the main way stack variables are used, and Quark has a decent number of them. Their general format is pretty simple, though you should be careful to insert `zx` and `low_part` instructions to extend and shrink value sizes to match memory/register sizes. There are a couple of details here:

* Check the semantics on loads smaller than the register width, and whether they zero or ignore the upper bits in the existing register
* Quark has âload and updateâ instructions that increment the source register. Weâve chosen to lift these using a temporary register, as the VM does the update prior to the load.
* Loads into registers should check for loads to `ip`, as lifting those as with direct register access will not have any effect on control flow. They need to instead be lifted as jumps. To make this blog easier to read, weâve left these as calls to `il.set_reg` here. See [the section at the end](#other) for how we handled this in practice.
* Complicated addressing modes may be better to lift with temporary registers. While itâ...