---
title: Simplifying disassembly with LLVM tools
url: https://maskray.me/blog/2024-12-22-simplifying-disassembly-with-llvm-tools
source: MaskRay
date: 2024-12-23
fetch_date: 2025-10-06T19:36:08.408377
---

# Simplifying disassembly with LLVM tools

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-12-22](/blog/2024-12-22-simplifying-disassembly-with-llvm-tools)

# Simplifying disassembly with LLVM tools

Both compiler developers and security researchers have built
disassemblers. They often prioritize different aspects. Compiler
toolchains, benefiting from direct contributions from CPU vendors, tend
to offer more accurate and robust decoding. Security-focused tools, on
the other hand, often excel in user interface design.

For quick disassembly tasks, [rizin](https://rizin.re/)
provides a convenient command-line interface.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % rz-asm -a x86 -b 64 -d 4829c390 sub rbx, rax nop ``` |

`-a x86` can be omitted.

## llvm-mc

Within the LLVM ecosystem, llvm-objdump serves as a drop-in
replacement for the traditional GNU objdump, leveraging instruction
information from LLVM's TableGen files
(`llvm/lib/Target/*/*.td`). Another LLVM tool, llvm-mc, was
originally designed for internal testing of the Machine Code (MC) layer,
particularly the assembler and disassembler components. There are
numerous `RUN: llvm-mc ...` tests within
`llvm/test/MC`. Despite its internal origins, llvm-mc is
often distributed as part of the LLVM toolset, making it accessible to
users.

However, using llvm-mc for simple disassembly tasks can be
cumbersome. It requires explicitly prefixing hexadecimal byte values
with 0x:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` % echo 0x48 0x29 0xc3 0x90 | llvm-mc --triple=x86_64 --cdis --output-asm-variant=1         .text         sub     rbx, rax         nop ``` |

Let's break down the options used in this command:

* `--triple=x86_64`: This specifies the target
  architecture. If your LLVM build's default target triple is already
  `x86_64-*-*`, this option can be omitted.
* [`--output-asm-variant=1`](/blog/2023-05-08-assemblers#x86):
  LLVM, like GCC, defaults to AT&T syntax for x86 assembly. This
  option switches to the Intel syntax. See [lhmouse/mcfgthread/wiki/Intel-syntax](https://github.com/lhmouse/mcfgthread/wiki/Intel-syntax)
  if you prefer the Intel syntax in compiler toolchains.
* `--cdis`: Introduced in LLVM 18, this option enables
  colored disassembly. In older LLVM versions, you have to use
  `--disassemble`.

---

I have contributed patches to [remove
`.text`](https://github.com/llvm/llvm-project/pull/120185) and allow [disassembling
raw bytes without the 0x prefix](https://github.com/llvm/llvm-project/pull/120185). You can now use the
`--hex` option:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % echo 4829c390 | llvm-mc --cdis --hex --output-asm-variant=1         sub     rbx, rax         nop ``` |

You can further simplify this by creating a bash/zsh function. bash
and zsh's "here string" feature provides a clean way to specify
stdin.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` disasm() {   llvm-mc --cdis --hex --output-asm-variant=1 <<< $@ } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % disasm 4829c390         sub     rbx, rax         nop % disasm $'4829 c3\n# comment\n90'         sub     rbx, rax         nop ``` |

The `--hex` option conveniently ignores whitespace and
`#`-style comments within the input.

### Atomic blocks

llvm-mc handles decoding failures by skipping a number of bytes, as
determined by the target-specific
`llvm::MCDisassembler::getInstruction`. To treat a sequence
of bytes as a single unit during disassembly, enclose them within
`[]`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` % echo 'f995ab99f995 ab99' | fllvm-mc --triple=riscv64 --cdis --hex <stdin>:1:1: warning: invalid instruction encoding f995ab99f995 ab99 ^ <stdin>:1:5: warning: invalid instruction encoding f995ab99f995 ab99     ^ <stdin>:1:14: warning: invalid instruction encoding f995ab99f995 ab99              ^ <stdin>:1:16: warning: invalid instruction encoding f995ab99f995 ab99                ^ % echo '[f995ab99][f995 ab99]' | fllvm-mc --triple=riscv64 --cdis --hex <stdin>:1:2: warning: invalid instruction encoding [f995ab99][f995 ab99]  ^ <stdin>:1:12: warning: invalid instruction encoding [f995ab99][f995 ab99]            ^ ``` |

---

llvm-mc can also function as an assembler:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % echo 'li t3, 42' | llvm-mc -show-encoding --triple=riscv64         li      t3, 42                          # encoding: [0x13,0x0e,0xa0,0x02] ``` |

(I've contributed a change to LLVM 20 that [removes
the previously printed `.text` directive](https://github.com/llvm/llvm-project/commit/7b23f413d1f76532825e470b523e971818d453ca).)

## llvm-objdump

For address information, llvm-mc falls short. We need to turn to
llvm-objdump to get that detail. Here is a little fish script that takes
raw hex bytes as input, converts them to a binary format
(`xxd -r -p`), and then creates an ELF relocatable file
(`llvm-objcopy -I binary`) targeting the x86-64 architecture.
Finally, llvm-objdump with the `-D` flag disassembles the
data section (`.data`) containing the converted binary.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` #!/usr/bin/env fish llvm-objdump -D -j .data (echo $argv | xxd -r -p | llvm-objcopy -I binary -O elf64-x86-64 - - | psub) | sed '1,/<_binary__stdin__start>:/d' ``` |

Here is a more feature-rich script that supports multiple
architectures:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` #!/usr/bin/env fish argparse a/arch= att r -- $argv; or return 1 if test -z "$_flag_arch"; set _flag_arch x86_64; end set opt --triple=$_flag_arch if test -z "$_flag_att" && string match -rq 'i.86|x86_64' $_flag_arch; set -a opt -M intel; end if test -n "$_flag_r"; set -a opt --no-leading-addr; set -a opt --no-show-raw-insn; end  switch $_flag_arch   case arm; set bfdname elf32-littlearm   case aarch64; set bfdname elf64-littleaarch64   case ppc32; set bfdname elf32-powerpc   case ppc32le; set bfdname elf32-powerpcle   case ppc64; set bfdname elf64-powerpc   case ppc64le; set bfdname elf64-powerpcle   case riscv32; set bfdname elf32-littleriscv   case riscv64; set bfdname elf64-littleriscv   case 'i?86'; set bfdname elf32-i386   case x86_64; set bfdname elf64-x86-64   case '*'; echo unknown arch >&2; return 1 end llvm-objdump -D -j .data $opt (echo $argv | xxd -r -p | llvm-objcopy -I binary -O $bfdname - - | psub) | sed '1,/<_binary__stdin__start>:/d' ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` % ./disasm e8 00000000c3 e800000000 c3        0: e8 00 00 00 00                call    0x5 <_binary__stdin__start+0x5>        5: c3                            ret        6: e8 00 00 00 00                call    0xb <_binary__stdin__start+0xb>        b: c3                            ret % ./disasm -r e8 00000000c3 e800000000 c3                 call    0x5 <_binary__stdin__start+0x5>                 ret                 call    0xb <_binary__stdin__start+0xb>                 ret % ./disasm -a riscv64 1300 0000        0: 00000013      nop ``` |

## Summary

* Assembler: `llvm-mc --show-encoding`
* Disassembler: `llvm-mc --cdis --hex`
* Disassembler with address information: `xxd -r -p`,
  `llvm-objcopy`, and
  `llvm-objdump -D -j .data`

Share

* [assembler](/blog/tags/assembler/)
* [llvm](/blog/tags/llvm/)
* [x86](/blog/tags/x86/)

[**Newer**

Exporting Tweets](/blog/2024-12-25-exporting-tweets)
[**Older**

clang-format and single-line statements](/blog/2024-12-01-clang-format-and-single-line-statements)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [b...