---
title: RISC-Y Business: Raging against the reduced machine
url: https://secret.club/2023/12/24/riscy-business.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:21.060495
---

# RISC-Y Business: Raging against the reduced machine

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# RISC-Y Business: Raging against the reduced machine

![main authors image](/assets/author_img/mrexodia.jpg)  [mrexodia](/author/mrexodia), [oopsmishap](/author/oopsmishap)

 Dec 24, 2023

---

## [Abstract](#abstract)

In recent years the interest in obfuscation has increased, mainly because people want to protect their intellectual property. Unfortunately, most of what’s been written is focused on the theoretical aspects. In this article, we will discuss the practical engineering challenges of developing a low-footprint virtual machine interpreter. The VM is easily embeddable, built on open-source technology and has various hardening features that were achieved with minimal effort.

## [Introduction](#introduction)

In addition to protecting intellectual property, a minimal virtual machine can be useful for other reasons. You might want to have an embeddable interpreter to execute business logic (shellcode), without having to deal with RWX memory. It can also be useful as an educational tool, or just for fun.

Creating a custom VM architecture (similar to [VMProtect](https://secret.club/2021/09/08/vmprotect-llvm-lifting-1.html)/[Themida](https://github.com/67-6f-64/AntiOreans-CodeDevirtualizer)) means that we would have to deal with binary rewriting/lifting or write our own compiler. Instead, we decided to use a preexisting architecture, which would be supported by LLVM: **RISC-V**. This architecture is already widely used for educational purposes and has the advantage of being very simple to understand and implement.

Initially, the main contender was WebAssembly. However, existing interpreters were very bloated and would also require dealing with a binary format. Additionally, it looks like WASM64 is very underdeveloped and our memory model requires 64-bit pointer support. SPARC and PowerPC were also considered, but RISC-V seems to be more popular and there are a lot more resources available for it.

WebAssembly was designed for sandboxing and therefore strictly separates guest and host memory. Because we will be writing our own RISC-V interpreter, we chose to instead share memory between the guest and the host. This means that pointers in the RISC-V execution context (the guest) are valid in the host process and vice-versa.

As a result, the instructions responsible for reading/writing memory can be implemented as a simple `memcpy` call and we do not need additional code to translate/validate memory accesses (which helps with our goal of small code size). With this property, we need to implement only two system calls to perform arbitrary operations in the host process:

```
uintptr_t riscvm_get_peb();
uintptr_t riscvm_host_call(uintptr_t rip, uintptr_t args[13]);
```

The `riscvm_get_peb` is Windows-specific and it allows us to resolve exports, which we can then pass to the `riscvm_host_call` function to execute arbitrary code. Additionally, an optional `host_syscall` stub could be implemented, but this is not strictly necessary since we can just call the functions in `ntdll.dll` instead.

## [Toolchain and CRT](#toolchain-and-crt)

To keep the interpreter footprint as low as possible, we decided to develop a toolchain that outputs a freestanding binary. The goal is to copy this binary into memory and point the VM’s program counter there to start execution. Because we are in freestanding mode, there is no C runtime available to us, this requires us to handle initialization ourselves.

As an example, we will use the following `hello.c` file:

```
int _start() {
    int result = 0;
    for(int i = 0; i < 52; i++) {
        result += *(volatile int*)&i;
    }
    return result + 11;
}
```

We compile the program with the following incantation:

```
clang -target riscv64 -march=rv64im -mcmodel=medany -Os -c hello.c -o hello.o
```

And then verify by disassembling the object:

```
$ llvm-objdump --disassemble hello.o

hello.o:        file format elf64-littleriscv

0000000000000000 <_start>:
       0: 13 01 01 ff   addi    sp, sp, -16
       4: 13 05 00 00   li      a0, 0
       8: 23 26 01 00   sw      zero, 12(sp)
       c: 93 05 30 03   li      a1, 51

0000000000000010 <.LBB0_1>:
      10: 03 26 c1 00   lw      a2, 12(sp)
      14: 33 05 a6 00   add     a0, a2, a0
      18: 9b 06 16 00   addiw   a3, a2, 1
      1c: 23 26 d1 00   sw      a3, 12(sp)
      20: 63 40 b6 00   blt     a2, a1, 0x20 <.LBB0_1+0x10>
      24: 1b 05 b5 00   addiw   a0, a0, 11
      28: 13 01 01 01   addi    sp, sp, 16
      2c: 67 80 00 00   ret
```

The `hello.o` is a regular ELF object file. To get a freestanding binary we need to invoke the linker with a linker script:

```
ENTRY(_start)

LINK_BASE = 0x8000000;

SECTIONS
{
    . = LINK_BASE;
    __base = .;

    .text : ALIGN(16) {
        . = LINK_BASE;
        *(.text)
        *(.text.*)
    }

    .data : {
        *(.rodata)
        *(.rodata.*)
        *(.data)
        *(.data.*)
        *(.eh_frame)
    }

    .init : {
        __init_array_start = .;
        *(.init_array)
        __init_array_end = .;
    }

    .bss : {
        *(.bss)
        *(.bss.*)
        *(.sbss)
        *(.sbss.*)
    }

    .relocs : {
        . = . + SIZEOF(.bss);
        __relocs_start = .;
    }
}
```

This script is the result of an excessive amount of swearing and experimentation. The format is `.name : { ... }` where `.name` is the destination section and the stuff in the brackets is the content to paste in there. The special `.` operator is used to refer to the current position in the binary and we define a few special symbols for use by the runtime:

| Symbol | Meaning |
| --- | --- |
| `__base` | Base of the executable. |
| `__init_array_start` | Start of the C++ init arrays. |
| `__init_array_end` | End of the C++ init arrays. |
| `__relocs_start` | Start of the relocations (end of the binary). |

These symbols are declared as `extern` in the C code and they will be resolved at link-time. While it may seem confusing at first that we have a destination section, it starts to make sense once you realize the linker has to output a regular ELF executable. That ELF executable is then passed to `llvm-objcopy` to create the freestanding binary blob. This makes debugging a whole lot easier (because we get DWARF symbols) and since we will not implement an ELF loader, it also allows us to extract the relocations for embedding into the final binary.

To link the intermediate ELF executable and then create the freestanding `hello.pre.bin`:

```
ld.lld.exe -o hello.elf --oformat=elf -emit-relocs -T ..\lib\linker.ld --Map=hello.map hello.o
llvm-objcopy -O binary hello.elf hello.pre.bin
```

For debugging purposes we also output `hello.map`, which tells us exactly where the linker put the code/data:

```
             VMA              LMA     Size Align Out     In      Symbol
               0                0        0     1 LINK_BASE = 0x8000000
               0                0  8000000     1 . = LINK_BASE
         8000000                0        0     1 __base = .
         8000000          8000000       30    16 .text
         8000000          8000000        0     1         . = LINK_BASE
         8000000          8000000       30     4         hello.o:(.text)
         8000000          8000000       30     1                 _start
         8000010          8000010        0     1                 .LBB0_1
         8000030          8000030        0     1 .init
         8000030          8000030        0     1         __init_array_start = .
         8000030          8000030        0     1         __init_array_end = .
         8000030          8000030        0     1 .relocs
         8000030          8000030        0     1         . = . + SIZEOF ( .bss )
         8000030          8000030        0     1         __relocs_start = .
               0                0       18     8 .rela.text
               0                0       18     8         hello.o:(.rela.text)
               0                0       3b...