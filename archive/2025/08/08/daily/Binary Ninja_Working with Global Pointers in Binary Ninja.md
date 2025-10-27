---
title: Working with Global Pointers in Binary Ninja
url: https://binary.ninja/2025/08/07/working-with-global-pointers.html
source: Binary Ninja
date: 2025-08-08
fetch_date: 2025-10-07T00:17:15.065216
---

# Working with Global Pointers in Binary Ninja

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

## Working with Global Pointers in Binary Ninja

* [Xusheng Li](https://github.com/xusheng6)
* 2025-08-07
* [reversing](/tag/reversing)

Global pointer usage is an important yet often overlooked concept in reverse engineering. This article explains what it
is, how it interacts with Binary Ninjaâs analysis and the relevant APIs and settings. This can hopefully help you master
it in your day-to-day reverse engineering!

![Overview](/blog/images/global-pointer-value/3.png)

## A primer on global pointer

*(Feel free to skip this introduction if youâre already familiar with the concepts discussed.)*

Let us start with a Linux x86 example. On Linux-x86 platform, usually the compiler will use the `ebx` register as the
global pointer register and point it to the GOT (Global Offset Table). References to global variables or external
functions can be made relative to GOT. This way, the code can be position-independent and the instruction
encoding can use a smaller relative offset value.

In the following screenshot, you can see that soon after the entry of the `main` function, it calls a function called
`__x86.get_pc_thunk.bx`.

![main function](/blog/images/global-pointer-value/1.png)

And the `__x86.get_pc_thunk.bx` function only has two instructions:

```
000110f0  __x86.get_pc_thunk.bx:
000110f0  mov     ebx, dword [esp {__return_addr}]
000110f3  retn     {__return_addr}
```

It simply loads the dword at the stack pointer into `ebx` and then returns. Remember the return address is on the stack,
so this loads the return address into `ebx`. Since the call is made at `0x11204` and the next instruction is at
`0x11209`, `ebx` ends up being `0x11209`.

Back in the `main` function, the next instruction is `add ebx, 0x2dcb`, and `0x11209 + 0x2dcb = 0x13fd4`, so it turns
`ebx` into `0x13fd4`, and the GOT is at that address:

![GOT](/blog/images/global-pointer-value/2.png)

In short, the code uses the above combination to load the address of the GOT into the `ebx` register. We call `ebx` the
global pointer register, and its value, `0x13fd4`, the global pointer value. To examine them, we can use the Python API:

```
>>> current_function.calling_convention.global_pointer_reg
'ebx'
>>> bv.global_pointer_value
<const ptr 0x13fd4>
```

Or see it in the Triage View:

![Global pointer in triage view](/blog/images/global-pointer-value/3.png)

A few instructions down, we can see that it loads a global string using `ebx` relative addressing:

```
00011214  lea     eax, [ebx-0x1fcc]  {"Hello, world!"}
0001121a  push    eax
0001121b  call    puts
```

If you have dealt with MIPS binaries, you probably know that the `$gp` register is used similarly. However, not every
architecture/calling convention uses the global pointer. For example, for x86\_64 sysv calling convention (the default
calling convention on Linux x86\_64) along with the convenience of RIP-based addressing mode enables compilers to
generate code like `lea rdi, [rip + offset]` instead of designating a dedicated register.

You might not have noticed this though, since Binary Ninja does the calculation (next instruction address + offset) for
you and shows the actual offset being referenced in the form of `lea rdi, [0xXXXXX]`. In this case, the calling
convention doesnât specify a global pointer register at all, and the global pointer value in the triage view shows
`N/A`:

![No global pointer](/blog/images/global-pointer-value/4.png)

## The Global Pointer in Binary Ninja

A common misconception is that tracking the value of `ebx` is unrelated to global pointer analysis. Our state-of-the-art
dataflow engine understands the process in the above sequence and can track the value of `ebx` properly, as evidenced by
the correct resolution of the âHello, world!â string. From a program analysis point of view, this is intra-procedural
dataflow, i.e., the dataflow within a function. Binary Ninja already handles it quite well. In other words, if every
function initiates the global pointer in the same way at its entry, then we wouldnât need to do anything to support it.

What can cause issues is inter-procedural usage of the global pointer value. For example, after the main function sets
the `ebx` register to the GOT, the compiler ensures it does not change, so in a callee of the `main` function, the code
will use the value of `ebx` directly without initializing it again.

In the above example, the call to the `puts` function is indeed performed through a small thunk function:

```
00011090  puts:
00011090  endbr32
00011094  jmp     dword [ebx+0x10]  {puts}
```

You can see that it uses the `ebx` value without first setting it. If the analysis does not know that `ebx` is pointing
to the GOT, it wouldnât be able to know this is jumping the `puts` function which significantly degrades the analysis.

Given that, we modeled the behavior of the global pointer in our core analysis. After all functions have been analyzed
individually, a module-level workflow will calculate the global pointer value based on information from individual
functions, and the calculated global pointer value is then used to update functions that use the global pointer register
without initializing it, and the process repeats until the analysis converges (no more changes are made). This process
can correctly determine the value in most cases. That said, binary analysis is
[*hard*](https://en.wikipedia.org/wiki/Rice%27s_theorem) and there is no guarantee of correctness, so we also provided the
necessary API and settings to customize the behavior of global pointer value analysis or specify a custom global pointer
value.

### Global Pointer Value Calculation

To start with, when the calling convention specifies a global pointer, it will override the `GetGlobalPointerRegister()`
method to specify it. See, for example, our
[x86](https://github.com/Vector35/binaryninja-api/blob/9eba1bb003e65a664367c9bf2b6ed03d418aa3c2/arch/x86/arch_x86.cpp#L3715)
and
[MIPS](https://github.com/Vector35/binaryninja-api/blob/71af6853ae407d70dc0783d5682b80563d045a90/arch/mips/arch_mips.cpp#L2519)
open-source architectures.

If a functionâs calling convention specifies a global register, then the analysis will look for an assignment of a
constant value to the global register and record its value which is then a candidate global pointer value. If you wish to
see the value suggested by a function, you can open the âEdit Function Propertiesâ dialog and look for something like
`GP (reg) = value`:

![Global pointer value suggested by a function](/blog/images/global-pointer-value/6.png)

Note that this merely means this function suggested a global pointer value, it does not mean it is using this value for
analysis. To check that out that, run `bv.global_pointer_value` in the Python console or view it in the [Triage
view](https://docs.binary.ninja/guide/index.html?h=triage#triage-summary). We might make the presentation clearer as it
is causing some confusion in [#6675](https://github.com/Vector35/binaryninja-api/issues/6675).

After all the functions are analyzed, there could be many that have suggested a candidate global pointer value. To
find the correct one, a majority vote is done...