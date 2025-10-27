---
title: Control-flow integrity
url: https://maskray.me/blog/2022-12-18-control-flow-integrity
source: MaskRay
date: 2022-12-19
fetch_date: 2025-10-04T01:53:45.025479
---

# Control-flow integrity

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2022-12-18](/blog/2022-12-18-control-flow-integrity)

# Control-flow integrity

Updated in 2025-05.

A control-flow graph (CFG) is a graph representation of all paths
that might be traversed through a program during its execution.
Control-flow integrity (CFI) refers to security policy dictating that
program execution must follow a control-flow graph. This article
describes some features that compilers and hardware can use to enforce
CFI, with a focus on llvm-project implementations.

CFI schemes are typically divided into forward-edge (e.g. indirect
calls) and backward-edge (mainly function returns). It should be noted
that exception handling and symbol interposition are not included in
these categories, as far as my understanding goes.

Let's start with backward-edge CFI. Fine-grained schemes check
whether a return address refers to a possible caller in the control-flow
graph. However, this is a very difficult problem, and the additional
guarantee may not be that useful.

Coarse-grained schemes, on the other hand, simply just check that
return addresses have not been tampered with. Return addresses are
typically stored in a memory region called the "stack" along with
function arguments, local variables, and register save areas. Stack
smashing is an attack that overwrites the return address to hijack the
control flow. The name was made popular by Aleph One (Elias Levy)'s
paper *Smashing The Stack For Fun And Profit*.

## StackGuard/Stack Smashing Protector

*StackGuard: Automatic Adaptive Detection and Prevention of
Buffer-Overflow Attacks* (1998) introduced an approach to detect
tampered return addresses on the stack.

GCC 4.1 [implemented](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=7d69de618e732d343228a07d797a30e39a6363f4)
`-fstack-protector` and `-fstack-protector-all`.
Additional variants have been added over the years, such as [`-fstack-protector-strong`](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=f6bc1c4a12af78d96c951547d9693e6e805162da)
for GCC 4.9 and [`-fstack-protector-explicit`](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=5434dc0730795cf6a2ef8a9fe20e4dcc9cd077be)
in 2015-01.

* In the prologue, the canary is loaded from a secret location and
  placed before the return address on the stack.
* In the epilogue, the canary is loaded again and compared with the
  entry before the return address.

The idea is that an attack overwriting the return address will likely
overwrite the canary value as well. If the attacker doesn't know the
canary value, returning from the function will crash.

The canary is stored either in a libc global variable
(`__stack_chk_guard`) or a field in the thread control block
(e.g. `%fs:40` on x86-64). Every architecture may have a
preference on the location. In a glibc port, only one of
`-mstack-protector-guard=global` and
`-mstack-protector-guard=tls` is supported ([BZ
#26817](https://sourceware.org/bugzilla/show_bug.cgi?id=26817)). (Changing this requires symbol versioning wrestling and may
not be [necessary](https://sourceware.org/pipermail/libc-alpha/2021-January/121618.html)
as we can move to a more fine-grained scheme.) Under the current thread
stack allocation scheme, the thread control block is allocated next to
the thread stack. This means that a large out-of-bounds stack write can
potentially overwrite the canary.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` void foo(const char *a) {   char s[10];   strcpy(s, a);   puts(s); } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` # x86-64 assembly   movq    %fs:40, %rax                      # load the canary from the thread control block   movq    %rax, 24(%rsp)                    # place the value before the return address   ...   movq    %fs:40, %rax                      # load the canary again   cmpq    24(%rsp), %rax                    # compare it with the entry before the return address   jne     .LBB0_2                           # fail if mismatching   <epilogue> .LBB0_2:   callq   __stack_chk_fail@PLT  # AArch64 assembly   adrp    x8, __stack_chk_guard   ldr     x8, [x8, :lo12:__stack_chk_guard] # load the canary from a global variable   stur    x8, [x29, #-8]                    # place the value before the saved frame pointer/return address   ...   adrp    x8, __stack_chk_guard   ldur    x9, [x29, #-8]                    # load the entry before the saved frame pointer/return address   ldr     x8, [x8, :lo12:__stack_chk_guard] # load the canary again   cmp     x8, x9   b.ne    .LBB0_2                           # fail if mismatching   <epilogue> .LBB0_2:   bl      __stack_chk_fail ``` |

GCC source code lets either libssp or libc provide
`__stack_chk_guard` (see
`TARGET_LIBC_PROVIDES_SSP`). It seems that libssp is
obsoleted for modern systems.

musl [sets](74a28a8af21977ebbc2945beb879f1b9b6ff13ba)
`((char *)&__stack_chk_guard)[1] = 0;`:

* The NUL byte serves as a terminator to sabotage string reads as
  information leak.
* A string overflow which attempts to preserve the canary while
  overwriting bytes after the canary (implementation detail of
  `struct pthread`) will fail.
* One byte overwrite is still detectable.
* The set of possible values is decreased, but this seems acceptable
  for 64-bit systems.

There are two related function attributes: `stack_protect`
and `no_stack_protector`. Strangely
`stack_protect` is not named
`stack_protector`.

`-mstack-protector-guard-symbol=` can change the global
variable name from `__stack_chk_guard` to something else. The
option was introduced for the Linux kernel. See
`arch/*/include/asm/stackprotector.h` for how the canary is
initialized in the Linux kernel. It is at least per-cpu. Some ports
support [per-task
stack canary](https://git.kernel.org/linus/0a1213fa7432778b71a1c0166bf56660a3aab030) (search
`config STACKPROTECTOR_PER_TASK`).

## Retguard

OpenBSD introduced Retguard in 2017 to improve security. Details can
be found in [RETGUARD and stack
canaries](https://isopenbsdsecu.re/mitigations/retguard/). Retguard is more fine-grained than StackGuard, but it has
more expensive function prologues and epilogues.

For each instrumented function, a cookie is allocated from a pool of
4000 entries. In the prologue, `return_address ^ cookie` is
pushed next to the return address (similar to the [XOR Random Canary](http://phrack.org/issues/56/5.html)). The
epilogue pops the XOR value and the return address and verifies that
they match (`(value ^ cookie) == return_address`).

Not encrypting the return address directly is important to preserve
return address prediction for the CPU. However, if a static branch
predictor exists (likely not-taken for a forward branch) the initial
prediction is likely wrong. The two `int3` instructions are
used to disrupt ROP gadgets that may form from `je ...; retq`
(`02 cc cc c3` is `addb %ah, %cl; int3; retq`),
but they don't remove the `pop+ret` gadget. ([ROP gadgets
removal](https://isopenbsdsecu.re/mitigations/rop_removal/) notes that gadget removal may not be useful.)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` // From https://www.openbsd.org/papers/eurobsdcon2018-rop.pdf // prologue ffffffff819ff700: 4c 8b 1d 61 21 24 00 mov 2367841(%rip),%r11 # <__retguard_2759> ffffffff819ff707: 4c 33 1c 24          xor (%rsp),%r11 ffffffff819ff70b: 55                   push %rbp ffffffff819ff70c: 48 89 e5             mov %rsp,%rbp ffffffff819ff70f: 41 53                push %r11  // epilogue ffffffff8115a457: 41 5b                pop %r11 ffffffff8115a459: 5d                   pop %rbp ffffffff8115a45a: 4c 33 1c 24          xor (%rsp),%r11 ffffffff8115a45e: 4c 3b 1d 03 74 ae 00 cmp 11432963(%rip),%r11 # <__retguard_...