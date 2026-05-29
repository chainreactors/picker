---
title: Backflip into the stack
url: https://armoredcode.com/blog/backflip-into-the-stack/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:06.074164
---

# Backflip into the stack

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# Backflip into the stack

March 2019

During my OSCE journey I came across an interesting technique to jump backwards
into the very beginning of the buffer injected on the vulnerable process.

The more reliable technique to jump back is to use an egghunter. You split
your shellcode into stages: in the first stage you write an [egghunter
shellcode](https://codiceinsicuro.it/slae/assignment-3-an-egg-hunter-journey)
that searches into the memory for the second stage payload, that it is the code
you want to executed prepended by your egg.

However, under some circumstances, you may want to execute a jump back into
your shellcode.

This [old but gold phrack article](http://phrack.org/issues/62/7.html)
describes some very handy assembly code snippets when writing shellcode for
Microsoft Windows.

Here you can find the idea about using FPU state saving instructions to have
the EIP value to be written on the stack.

```
fldz
fnstenv [esp-12]
pop ecx
add cl, 10
nop
```

[FLDZ](https://c9x.me/x86/html/file_module_x86_id_101.html) instruction pushes
a 0 on the FPU register stack and the
[FNSTENV](https://www.felixcloutier.com/x86/fstenv%3Afnstenv) stores the FPU
environment to the address given as parameter,

Executing a “fnstenv [esp]” instruction, the result on the stack is the
following.

```
gdb-peda$ x/30x $esp
0xffffd600:	0x7f	0x03	0xff	0xff	0x00	0x38	0xff	0xff
0xffffd608:	0xff	0x7f	0xff	0xff	0x82	0x80	0x04	0x08
0xffffd610:	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
0xffffd618:	0x00	0x00	0xff	0xff	0xe9	0xd7
```

If we want to align the information about the EIP (0x08048082 in my case) to be
found at the very beginning of the stack, we kindly ask FNSTENV to start
writing 12 bytes before the $ESP value, that’s the reason of “fnstenv
[esp-12]”.

We than pop the stack word into ECX storing the value the EIP register has when
fnstenv it was called. Then, I choose to add 9 bytes to move ECX value to the
instruction right after the NOP.

In order to execute a jump, we decrement CH register (the most significant 8
bits of the CX register, [the 16 bits representation of
ECX](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm).
This will subtract 256 on the whole ECX value, that means this technique allow
us to jump backwards in steps of 256 bytes.

```
fldz
fnstenv [esp-12]
pop ecx
add cl, 10
nop
dec ch
dec ch
jmp ecx
```

See the code in action on gdb.

Today I added those two shellcodes in [shellerate
project](https://github.com/thesp0nge/shellerate/blob/master/shellerate/utils/asm_x86.py).

```
def get_where_am_i_in_ecx():
    # fldz
    # fnstenv [esp-12]
    # pop ecx
    # add cl, 9
    return "\xd9\xee\xd9\x74\x24\xf4\x59\x80\xc1\x09"

# jumps is how many 256 bytes backword jump you want to take
def jmp_backwards_ecx(jumps=1):
    return get_where_am_i_in_ecx() + "\xfe\xcd" * jumps + "\xff\xe1"
```

Please note again that using egghunter is more reliable but it can take some
time in order to loop into victim memory searching for the payload. Anyway,
this technique can be used if you’re pretty sure about the fixed amount of
space you can backward skip, e.g. it can be safetly used in a SEH overwrite
exploitation.

Enjoy it!

© 2012 - 2026 Armored Code. All rights
reserved.