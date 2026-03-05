---
title: Building a Custom Architecture and Platform: Part 3
url: https://binary.ninja/2026/03/04/quark-platform-part-3.html
source: Binary Ninja
date: 2026-03-04
fetch_date: 2026-03-05T04:06:05.602525
---

# Building a Custom Architecture and Platform: Part 3

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

## Building a Custom Architecture and Platform: Part 3

* [Glenn Smith](https://github.com/CouleeApps)
* 2026-03-04
* [reversing](/tag/reversing), [decompiler](/tag/decompiler), [architecture](/tag/architecture)

![Quark](/blog/images/quark/arm-upgrade.png)

Adding platform support to an architecture plugin is one of the best ways to improve decompilation. While disassembling and lifting give us good results, they are limited in scope and cannot fill in details about the operating system. With platform support, we can add rich annotations to the analysis and get better results. Letâs look through the many systems Binary Ninja includes for implementing platform support in a plugin of your own.

## Contents

This is Part 3 of a three-part series. Here is the full list of contents:

* [Target](/2026/02/20/quark-platform-part-1.html#target)
* [Setup](/2026/02/20/quark-platform-part-1.html#setup)
* [Part 1: Disassembly](/2026/02/20/quark-platform-part-1.html#disassembly)
  + [Decoding](/2026/02/20/quark-platform-part-1.html#decoding)
  + [Disassembly Text](/2026/02/20/quark-platform-part-1.html#disassembly-text)
  + [Control Flow](/2026/02/20/quark-platform-part-1.html#control-flow)
  + [Addendum](/2026/02/20/quark-platform-part-1.html#addendum)
  + [Patching](/2026/02/20/quark-platform-part-1.html#patching)
  + [Assembling](/2026/02/20/quark-platform-part-1.html#assembling)
* [Part 2: Lifting](/2026/02/26/quark-platform-part-2.html#lifting)
  + [Basics](/2026/02/26/quark-platform-part-2.html#basics)
  + [Loads and Stores](/2026/02/26/quark-platform-part-2.html#loads-and-stores)
  + [Calls](/2026/02/26/quark-platform-part-2.html#calls)
  + [Arithmetic](/2026/02/26/quark-platform-part-2.html#arithmetic)
  + [System Calls](/2026/02/26/quark-platform-part-2.html#system-calls)
  + [Intrinsics](/2026/02/26/quark-platform-part-2.html#intrinsics)
  + [Flags](/2026/02/26/quark-platform-part-2.html#flags)
  + [Conditionals](/2026/02/26/quark-platform-part-2.html#conditionals)
  + [Other](/2026/02/26/quark-platform-part-2.html#other)
* [Part 3: Platform Support](#platform-support)
  + [Calling Convention](#calling-convention)
  + [System Calls](#system-calls-1)
  + [Platform Types](#platform-types)
  + [Type Libraries](#type-libraries)
  + [Function Signatures](#function-signatures)
  + [Other](#other)
* [Conclusion](#conclusion)

# Recap

In [Part 1](/2026/02/20/quark-platform-part-1.html) we implemented a disassembler. In [Part 2](/2026/02/26/quark-platform-part-2.html) we implemented a lifter. Together, that got us a working decompiler for Quark, with stack resolution, variable creation, and high-level control flow structures. What we have now is pretty good, though its output needs the user to annotate every part of every binary.

![State of the decompilation results at the end of Part 2](/blog/images/quark/hlil-initial-results.png)
*State of the decompilation results at the end of Part 2*

# Platform Support

Up until now, weâve implemented all the functionality with a custom architecture, but we havenât gotten to more specific details like calling conventions, system calls, and library signatures yet. For those, we need to implement a Platform subclass. Binary Ninja distinguishes between the concept of an architecture and a platform to allow for details to be defined at generic and specific places. Architectures describe processor behavior, like instructions, and platforms describe operating system behavior, like register selection and types. To make further platform-specific improvements to our decompilation results, we need to implement a platform.

You can register a Platform with the Binary View Type in a very similar manner to registering an Architecture. In the case of Quark on Linux, this is pretty straightforward:

```
class LinuxQuarkPlatform(Platform):
    name = "linux-quark"

qlinuxplatform = LinuxQuarkPlatform(qarch)
qlinuxplatform.register("linux")

# Linux uses ELF platforms 0 and 3, so register for both
BinaryViewType['ELF'].register_platform(0, qarch, qlinuxplatform)
BinaryViewType['ELF'].register_platform(3, qarch, qlinuxplatform)
```

Specifying the platform wonât have any visible changes immediately, but by implementing the next few sections we can improve decompilation significantly.

## Calling Convention

The first thing to notice when looking at the decompilation results is that the control flow looks good, but the arguments to every function call are wrong. This is because, to get proper function call arguments detected, you need to specify them via a Calling Convention. These are relatively straightforward to declareâ you just need to fill out a few fields:

```
class QuarkCallingConvention(CallingConvention):
    name = "qcall"
    caller_saved_regs = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
    callee_saved_regs = ['r16', 'r17', 'r18', 'r19', 'r20', 'r21', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28']
    int_arg_regs = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8']
    int_return_reg = 'r1'
    high_int_return_reg = 'r2'
    arg_regs_for_varargs = False
```

* `caller_saved_regs` - Registers that the caller assumes can be modified by the callee, so the caller must save them itself
* `callee_saved_regs` - Registers that the caller assumes are not modified by the callee, so the callee needs to save them if it modifies them
* `int_arg_regs` - Arguments passed to integer parameters at call sites, in order. Arguments passed after this are assumed to be on the stack
* `int_return_reg` - Register that return value is passed in
* `high_int_return_arg` - For double-width size return values, the high bits are passed in this register
* `arg_regs_for_varargs` - Some compilers have variadic functions put all the variable arguments on the stack, instead of using the remaining register slots. If that is the case (and it is with SCC/Quark), then set this to False.

Other fields that Quark did not need, but you can specify:

* `float_arg_regs` - If your architecture supports separate floating-point registers used for arguments, you can specify those as well
* `float_return_reg` - If your architecture has a separate floating-point register used for return values, you can specify that
* `arg_regs_share_index` - When passing mixed integer and floating point arguments to functions, some platforms use shared slot indices and some use split indices. With shared slot indices, each argument uses either the integer or floating point register for its index, and the other is reserved but unused. For a function with the signature `void foo(int, int, float, int, float)`, this leads to an argument list of `void foo(int @ i0, int @ i1, float @ f2, int @ i3, float @ i4)` where `f0`, `f1`, `i2`, and `f3` registers are unused. In contrast, split slot indices cause each integer and floating point argument to pull the next free register from their list, regardless of how many arguments of the other type are present. In these cases, the order of integer and floating point arguments does not affect one another, and each use registers from their set in order. This leads to argument lists like `...