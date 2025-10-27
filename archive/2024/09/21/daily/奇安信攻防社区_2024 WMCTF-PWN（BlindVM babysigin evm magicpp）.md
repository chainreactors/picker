---
title: 2024 WMCTF-PWN（BlindVM babysigin evm magicpp）
url: https://forum.butian.net/share/3812
source: 奇安信攻防社区
date: 2024-09-21
fetch_date: 2025-10-06T18:21:22.934572
---

# 2024 WMCTF-PWN（BlindVM babysigin evm magicpp）

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

### 2024 WMCTF-PWN（BlindVM babysigin evm magicpp）

* [CTF](https://forum.butian.net/topic/52)

2024 WMCTF PWN方向 做题人视角详细版

> 衷心感谢tplus师傅耐心的帮助
BlindVM
=======
[Linux进程虚拟内存空间布局/ Linux 下虚拟内存的分布](https://blog.csdn.net/vincent3678/article/details/117458127)
```bash
hint: https://sourceware.org/git/?p=glibc.git;a=blob;f=malloc/arena.c;hb=09fb06d3d60291af6cdb20357dbec2fbb32514de#l596
hint2: Useheap spraying to make the heap space contiguous with the LIBC space.
Task content：The expected solution does not require any brute force.
47.104.193.231:9999
```
```bash
da1bb0f99/bin$ checksec BlindVM
[\*] '/home/llk/Desktop/pwn/2024 WMCTF/BlindVM\_3952e413eaca0e8ede93af1da1bb0f99/bin/BlindVM'
Arch: amd64-64-little
RELRO: Partial RELRO
Stack: No canary found
NX: NX enabled
PIE: PIE enabled
```
[linux系统编程之进程（四）：进程退出exit，\\_exit区别即atexit函数](https://www.cnblogs.com/mickole/p/3186606.html)
可以尝试比topchunk大的不同size来尝试
线程堆栈
----
一开始`\_\_pthread\_create\_2\_1`会通过mmap分配`0x801000`大小的线程栈，然后被分割成`800000`和`1000`
```c
#0 \_\_GI\_\_\_mmap64 (addr=addr@entry=0x0, len=len@entry=8392704, prot=prot@entry=0, flags=flags@entry=131106, fd=fd@entry=-1, offset=offset@entry=0) at ../sysdeps/unix/sysv/linux/mmap64.c:47
#1 0x000070fc02095707 in allocate\_stack (stacksize=<synthetic pointer>, stack=<synthetic pointer>, pdp=<synthetic pointer>, attr=0x7ffca70c5d30) at ./nptl/allocatestack.c:370
#2 \_\_pthread\_create\_2\_1 (newthread=0x7ffca70c5e60, attr=0x0, start\_routine=0x6223aad872c0, arg=0x0) at ./nptl/pthread\_create.c:647
0x6223ac771000 0x6223ac792000 rw-p 21000 0 [heap]
0x70fc01600000 0x70fc01601000 ---p 1000 0 [anon\_70fc01600]
0x70fc01601000 0x70fc01e01000 rw-p 800000 0 [anon\_70fc01601]
0x70fc02000000 0x70fc02028000 r--p 28000 0 /usr/lib/x86\_64-linux-gnu/libc.so.6
```
线程堆的初始化和mmap相关分配
----------------
新线程heap\\_info和mstate和topchunk的初始化流程
```c
\_\_GI\_\_\_libc\_malloc->tcache\_init->arena\_get->arena\_lock->arena\_get2->\_int\_new\_arena->new\_heap->alloc\_new\_heap (size, top\_pad, GLRO (dl\_pagesize), MAP\_NORESERVE);->MMAP (0, max\_size << 1, PROT\_NONE, mmap\_flags) max\_size << 1=8000000 和\_\_munmap (p1, ul);和 \_\_munmap (p2 + max\_size, max\_size - ul);
0x6223ac771000 0x6223ac792000 rw-p 21000 0 [heap]
0x70fbf9600000 0x70fc01600000 ---p 8000000 0 [anon\_70fbf9600]
0x70fc01600000 0x70fc01601000 ---p 1000 0 [anon\_70fc01600]
0x70fc01601000 0x70fc01e01000 rw-p 800000 0 [anon\_70fc01601]
\_\_munmap (p1, ul);和 \_\_munmap (p2 + max\_size, max\_size - ul);后
0x6223ac771000 0x6223ac792000 rw-p 21000 0 [heap]
0x70fbfc000000 0x70fc00000000 ---p 4000000 0 [anon\_70fbfc000]
0x70fc01600000 0x70fc01601000 ---p 1000 0 [anon\_70fc01600]
0x70fc01601000 0x70fc01e01000 rw-p 800000 0 [anon\_70fc01601]
```
当分配堆的大小超过线程堆中的topchunk，但没有大于等于`0x20000 mp\_.mmap\_threshold`时会进入如下流程，相当于将heap\\_info的size增加，然后topchunk的size自然变大，（size是自己申请的字节数，然后和页面大小对齐）然后topchunk分割
```c
sysmalloc (nb, av);
{
……
if ((long) (MINSIZE + nb - old\_size) > 0
&& grow\_heap (old\_heap, MINSIZE + nb - old\_size) == 0)
{
av->system\_mem += old\_heap->size - old\_heap\_size;
set\_head (old\_top, (((char \*) old\_heap + old\_heap->size) - (char \*) old\_top)
| PREV\_INUSE );
}
}
grow\_heap {
……
diff = ALIGN\_UP (diff, pagesize);
new\_size = (long) h->size + diff;
if ((unsigned long) new\_size > (unsigned long) max\_size)
return -1;
……
}
保证在0x4000000范围内
0x6223ac771000 0x6223ac792000 rw-p 21000 0 [heap]
0x70fbfc000000 0x70fbfc021000 rw-p 21000 0 [anon\_70fbfc000]
0x70fbfc021000 0x70fc00000000 ---p 3fdf000 0 [anon\_70fbfc021]
```
但如果大于等于`0x20000 mp\_.mmap\_threshold`直接通过mmap分配
```c
mm = sysmalloc\_mmap (nb, pagesize, 0, av);
->
MMAP (0, size,
mtag\_mmap\_flags | PROT\_READ | PROT\_WRITE,
extra\_flags);
```
但growheap中如果`h->size + diff;`大小已经超过0x4000000范围了，会进入如下处理流程
```c
else if ((heap = new\_heap (nb + (MINSIZE + sizeof (\*heap)), mp\_.top\_pad)))
->
alloc\_new\_heap (size就是nb + (MINSIZE + sizeof (\*heap)), top\_pad, GLRO (dl\_pagesize), MAP\_NORESERVE);
->
MMAP (0, max\_size << 1, PROT\_NONE, mmap\_flags);
else
aligned\_heap\_area = p2 + max\_size;
\_\_munmap (p2 + max\_size, max\_size - ul);
newheap后的处理流程（av还是之前那个，但把av的top改成了当前新heap的topchunk），大小就是heap->size - sizeof (\*heap)) | PREV\_INUSE，然后会设置一些间隔堆
{
/\* Use a newly allocated heap. \*/
heap->ar\_ptr = av;
heap->prev = old\_heap;
av->system\_mem += heap->size;
/\* Set up the new top. \*/
top (av) = chunk\_at\_offset (heap, sizeof (\*heap));
set\_head (top (av), (heap->size - sizeof (\*heap)) | PREV\_INUSE);
/\* Setup fencepost and free the old top chunk with a multiple of
MALLOC\_ALIGNMENT in size. \*/
/\* The fencepost takes at least MINSIZE bytes, because it might
become the top chunk again later. Note that a footer is set
up, too, although the chunk is marked in use. \*/
old\_size = (old\_size - MINSIZE) & ~MALLOC\_ALIGN\_MASK;
set\_head (chunk\_at\_offset (old\_top, old\_size + CHUNK\_HDR\_SZ),
0 | PREV\_INUSE);
if (old\_size >= MINSIZE)
{
set\_head (chunk\_at\_offset (old\_top, old\_size),
CHUNK\_HDR\_SZ | PREV\_INUSE);
set\_foot (chunk\_at\_offset (old\_top, old\_size), CHUNK\_HDR\_SZ);
set\_head (old\_top, old\_size | PREV\_INUSE | NON\_MAIN\_ARENA);
\_int\_free (av, old\_top, 1);
00:0000│ 0x72b087ffffe0 ◂— 0xf60 是原来的topchunk的size
01:0008│ 0x72b087ffffe8 ◂— 0x10
02:0010│ 0x72b087fffff0 ◂— 0x10
03:0018│ 0x72b087fffff8 ◂— 1
}
else
{
set\_head (old\_top, (old\_size + CHUNK\_HDR\_SZ) | PREV\_INUSE);
set\_foot (old\_top, (old\_size + CHUNK\_HDR\_SZ));
}
}
然后再新的topchunk分割
p = av->top;
size = chunksize (p);
/\* check that one of the above allocation paths succeeded \*/
if ((unsigned long) (size) >= (unsigned long) (nb + MINSIZE))
{
remainder\_size = size - nb;
remainder = chunk\_at\_offset (p, nb);
av->top = remainder;
set\_head (p, nb | PREV\_INUSE | (av != &main\_arena ? NON\_MAIN\_ARENA : 0));
set\_head (remainder, remainder\_size | PREV\_INUSE);
check\_malloced\_chunk (av, p, nb);
return chunk2mem (p);
}
```
注意新的heap是没有mstate的，就heap\\_info，剩余的就是topchunk了
思路
--
由于mmap分配的区间在主线程heap到栈的某个偏移，这中间有mmap匿名映射分配的和libc和ld库的文件映射。
- 先分配当前heap\\_info的空间（残留topchunk，但大小使得topchunk不满足也不能扩充了，就申请新的heap\\_info），然后申请的和当前heap-&gt;size大于max\\_size使得原来的topchunk被free掉，然后得到新的heap\\_info
- 分配大于`0x20000`的使得mmap分配填充heap到libc的部分
- 将之前的进入unsortedbin的chunk分配一部分，然后溢出改size，然后能分割到unsortedbin 的fd正好在新页面的前八个字节（即libc对应的heap\\_info的ar\\_ptr 因为每个拿到chunk都会检查arena是否和ar\\_ptr 一样 而此时的fd指向就在ar\\_ptr 对应的mstate里 ），然后分配出来，部分写，就能得到`ar\_ptr`
```c
assert (!victim || chunk\_is\_mmapped (mem2chunk (victim)) ||
ar\_ptr == arena\_for\_chunk (mem2chunk (victim)));
```
- 然后分配掉当前新的heap\\_info的空间（残留topchunk，但大小使得topchunk不满足也不能扩充了，就申请新的heap\\_info），然后改topchunk的size,改大
- 然后使得分配到该heap\\_info只剩0x10(但对应的topchunk还有很多，因为改了size)，然后分配size=`0x4000010`使得第一次分配在第二个heap\\_info，而第二次分配在第一个heap\\_info
-
```c
0x76becc000000 0x76bed0000000 rw-p 4000000 0 [anon\_76becc00] 第二个
0x76bed0000000 0x76bed4000000 rw-p 4000000 0 [anon\_76bed0000]
0x76bed4000000 0x76bed8000000 rw-p 4000000 0 [anon\_76bed4000] 第一个
第一个下面总是不连续，并且小于0x20000，可以每次喷的时候多个小于0x20000的部分，来把不足0x20000的部分填满
```
- 此时topchunk在heap\\_info以下，而之前伪造的heap\\_info就是在heap\\_info以下的开始处，就是第一个分配完之后topchunk到fakeheapinfo那里去了，这个把\\_heap\\_info当作topchunk嘛，然后再申请，正好可以通过ar\\_ptr检查，然后也能写size后面的了，进而控制heap\\_info
- 后面的grow\\_heap和topchunk扩容然后分割覆盖libc就顺理成章了
> libc加载地址的过程大概是这样的
> 在dl\\_fixup中根据字符串找到这个函数对应的结构体
> 这个结构体存储一个偏移量
> 最终这个函数的真实地址是l\\_addr(库加载地址)...