---
title: Stack walking: space and time trade-offs
url: https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs
source: MaskRay
date: 2025-10-26
fetch_date: 2025-10-27T16:50:31.929049
---

# Stack walking: space and time trade-offs

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-10-26](/blog/2025-10-26-stack-walking-space-and-time-trade-offs)

# Stack walking: space and time trade-offs

On most Linux platforms (except AArch32, which uses
`.ARM.exidx`), DWARF `.eh_frame` is required for
[C++ exception
handling](/blog/2020-12-12-c%2B%2B-exception-handling-abi) and [stack
unwinding](/blog/2020-11-08-stack-unwinding) to restore callee-saved registers. While
`.eh_frame` can be used for call trace recording, it is often
criticized for its runtime overhead. As an alternative, developers can
enable frame pointers, or adopt SFrame, a newer format designed
specifically for profiling. This article examines the size overhead of
enabling non-DWARF stack walking mechanisms when building several LLVM
executables.

Runtime performance analysis will be added in a future update.

## Stack walking mechanisms

Here is a survey of mechanisms available for x86-64:

* Frame pointers: fast but costs a register
* DWARF `.eh_frame`: comprehensive but slower, supports
  additional features like C++ exception handling
* SFrame: a new format being developed, profiling only.
  `.eh_frame` is still needed for debugging and C++ exception
  handling. Check out [Remarks
  on SFrame](/blog/2025-09-28-remarks-on-sframe) for details.
* x86 Last Branch Record (LBR): Skylake increased the LBR stack size
  to 32. Supported by AMD Zen 4 as [Last
  Branch Record Extension Version 2 (LbrExtV2)](https://lkml.kernel.org/lkml/b6bb0abaa8a54c0b6d716344700ee11a1793d709.1660211399.git.sandipan.das%40amd.com/T/)
* [Apple's
  Compact Unwinding Format](https://faultlore.com/blah/compact-unwinding/): This has llvm, lld/MachO, and libunwind
  implementation. Supports x86-64 and AArch64. This can mostly replace
  DWARF CFI, but some entries need DWARF escape.
* OpenVMS's Compact Unwinding Format: This modifies Apple's Compact
  Unwinding Format.

## Space overhead analysis

### Frame pointer size impact

For most architectures, GCC defaults to
`-fomit-frame-pointer` in `-O` compilation to free
up a register for general use. To enable frame pointers, specify
`-fno-omit-frame-pointer`, which reserves the frame pointer
register (e.g., `rbp` on x86-64) and emits push/pop
instructions in function prologues/epilogues.

For leaf functions (those that don't call other functions), while the
frame pointer register should still be reserved for consistency, the
push/pop operations are often unnecessary. Compilers provide
`-momit-leaf-frame-pointer` (with target-specific defaults)
to reduce code size.

The viability of this optimization depends on the target
architecture:

* On AArch64, the return address is available in the link register
  (X30). The immediate caller can be retrieved by inspecting X30, so
  `-momit-leaf-frame-pointer` does not compromise
  unwinding.
* On x86-64, after the prologue instructions execute, the return
  address is stored at RSP plus an offset. An unwinder needs to know the
  stack frame size to retrieve the return address, or it must utilize
  DWARF information for the leaf frame and then switch to the FP chain for
  parent frames.

Beyond this architectural consideration, there are additional
practical reasons to use `-momit-leaf-frame-pointer` on
x86-64:

* Many hand-written assembly implementations (including numerous glibc
  functions) don't establish frame pointers, creating gaps in the frame
  pointer chain anyway.
* In the prologue sequence `push rbp; mov rbp, rsp`, after
  the first instruction executes, RBP does not yet reference the current
  stack frame. When shrink-wrapping optimizations are enabled, the
  instruction region where RBP still holds the old value becomes larger,
  increasing the window where the frame pointer is unreliable.

Given these trade-offs, three common configurations have emerged:

* omitting FP:
  `-fomit-frame-pointer -momit-leaf-frame-pointer` (smallest
  overhead)
* reserving FP, but removing FP push/pop for leaf functions:
  `-fno-omit-frame-pointer -momit-leaf-frame-pointer` (frame
  pointer chain omitting the leaf frame)
* reserving FP:
  `-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer`
  (complete frame pointer chain, largest overhead)

The size impact varies significantly by program. Here's a [Ruby
script `section_size.rb`](https://github.com/MaskRay/unwind-info-size-analyzer/blob/master/section_size.rb) that compares section sizes:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` % ~/Dev/unwind-info-size-analyzer/section_size.rb /tmp/out/custom-{none,nonleaf,all}/bin/{llvm-mc,opt} Filename                            |       .text size |        EH size |  VM size | VM increase ------------------------------------+------------------+----------------+----------+------------ /tmp/out/custom-none/bin/llvm-mc    |  2114687 (23.7%) |  367992 (4.1%) |  8914057 |           - /tmp/out/custom-nonleaf/bin/llvm-mc |  2124143 (24.0%) |  301688 (3.4%) |  8856713 |       -0.6% /tmp/out/custom-all/bin/llvm-mc     |  2149535 (24.0%) |  362408 (4.1%) |  8942729 |       +0.3% /tmp/out/custom-none/bin/opt        | 39018511 (70.2%) | 4561112 (8.2%) | 55583965 |           - /tmp/out/custom-nonleaf/bin/opt     | 38879897 (71.4%) | 3542288 (6.5%) | 54424789 |       -2.1% /tmp/out/custom-all/bin/opt         | 38980905 (71.0%) | 3888624 (7.1%) | 54871285 |       -1.3% ``` |

For instance, `llvm-mc` is dominated by read-only data,
making the relative `.text` percentage quite small, so frame
pointer impact on the VM size is minimal. ("VM size" is a metric used by
bloaty, representing the total `p_memsz` size of
`PT_LOAD` segments, excluding [alignment
padding](/blog/2023-12-17-exploring-the-section-layout-in-linker-output).) As expected, `llvm-mc` grows larger as more
functions set up the frame pointer chain. However, `opt`
actually becomes smaller when `-fno-omit-frame-pointer` is
enabledâa counterintuitive result that warrants explanation.

Without frame pointer, the compiler uses RSP-relative addressing to
access stack objects. When using the register-indirect + disp8/disp32
addresing mode, RSP needs an extra SIB byte while RBP doesn't. For
larger functions accessing many local variables, the savings from
shorter RBP-relative encodings can outweigh the additional
`push rbp; mov rbp, rsp; pop rbp` instructions in the
prologues/epilogues.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % echo 'mov rax, [rsp+8]; mov rax, [rbp-8]' | /tmp/Rel/bin/llvm-mc -x86-asm-syntax=intel -output-asm-variant=1 -show-encoding         mov     rax, qword ptr [rsp + 8]        # encoding: [0x48,0x8b,0x44,0x24,0x08]         mov     rax, qword ptr [rbp - 8]        # encoding: [0x48,0x8b,0x45,0xf8]  # ModR/M byte 0x44: Mod=01 (register-indirect addressing + disp8), Reg=0 (dest reg RAX), R/M=100 (SIB byte follows) # ModR/M byte 0x45: Mod=01 (register-indirect addressing + disp8), Reg=0 (dest reg RAX), R/M=101 (RBP) ``` |

### SFrame vs .eh\_frame

Oracle is advocating for SFrame adoption in Linux distributions. The
SFrame implementation is handled by the assembler and linker rather than
the compiler. Let's build the latest binutils-gdb to test it.

**Building test program**

We'll use the clang compiler from <https://github.com/llvm/llvm-project/tree/release/21.x>
as our test program.

There are still issues related to garbage collection ([object file
format design issue](/blog/2025-09-28-remarks-on-sframe#:~:text=garbage)), so I'll just disable
`-Wl,--gc-sections`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` --- i/llvm/cmake/modules/AddLLVM.cmake +++ w/llvm/cmake/modules/AddLLVM.cmake @@ -331,4 +331,4 @@ function(add_link_opts target_name)          # TODO Revisit this later on z/OS. -        set_property(TARGET ${target_name} APPEND_STRING PROPERTY -    ...