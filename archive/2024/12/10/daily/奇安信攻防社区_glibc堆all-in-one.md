---
title: glibc堆all-in-one
url: https://forum.butian.net/share/3919
source: 奇安信攻防社区
date: 2024-12-10
fetch_date: 2025-10-06T19:33:41.562848
---

# glibc堆all-in-one

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

### glibc堆all-in-one

本篇文章篇幅很长，记录了笔者学习glibc堆的全部心得，从入门的堆分配的学习，一些经典打法的总结，以及个人的技巧，保护机制的变动。再到io basic knowledge，glibc的IO-FILE攻击部分，常见的house系列总结，最后到magic\_gadgets，以及打libc got,stdout,stderr这些比较边角的内容，希望对入门学堆的你有所帮助，也希望帮助更多学习glibc堆的师傅建立知识体系，也欢迎更多大佬进行补充指点

堆分配（自己复现）
=========
[一篇讲的比较清楚的博客](https://blog.csdn.net/qq\_41453285/article/details/99005759)
malloc函数
--------
说明：first chunk是指bin中链表头部的chunk,last chunk是指bin中链表尾部的chunk。fastbin是LIFO，其他bin是FIFO
1. 判断是否在fastbin大小范围内，如果在则根据malloc的size求出idx；如果fastbin\[idx\]不为空则取first chunk；如果为空，进入unsorted bins大循环
2. 如果不在fastbin大小范围内，判断是否在smallbin大小范围内。如果在则根据malloc的size求出idx；如果smallbin\[idx\]不为空则取last chunk；如果为空,判断smallbin是否初始化。如果已经初始化，那么就进入unsorted bins大循环；如果没有初始化，调用malloc consolidate函数再进入unsorted bins大循环
3. 如果既不在fastbin大小范围内，也不在smallbin大小范围内，判断有无fastchunks。如果没有，进入unsorted bins大循环；如果有，调用malloc consolidate函数再进入unsorted bins大循环
- 在后面有了tcache之后，填满tcache再考虑fastbin
malloc consolidate函数
--------------------
- 穷尽合并fastbin里面的chunk并放入unsorted bin中，与top chunk合并的chunk除外
1. 遍历整个fastbinY(这是个指针数组,每个元素是一个单向链表的头部),只要整个fastbinY有chunk就遍历。先看prev inuse，如果为0,则unlink prev chunk；如果为1，看next chunk。如果next chunk为top chunk，那就和top chunk合并(和top合并后就直接遍历下一个fastchunk了);如果不是，看next inuse。如果为0，则unlink next chunk；为1就什么都不做。不管next inuse为0还是1，最终都将合并后的chunk插入unsorted bins中
2. 一直遍历fastbinY直到fastbinY为空，进入unsorted bins大循环
unsorted bins大循环
----------------
- 遍历unsorted bin判断是否有满足条件的unsorted chunk，如果不满足条件就consolidate（将其放入合适的bin中）
1. 取last unsorted chunk
2. 1.如果大小刚好合适，返回这个chunk 2.如果在small bin的大小，chunk进入small bin 3.如果large bin为空，放入large bin中（因为在之前已经判断是否是small bin的大小了）4.前面条件都不满足，从large bin的最后开始寻找这个chunk合适的位置。
3. 一直遍历unsorted bin直到unsorted bin为空
\*\*malloc的时候，不论malloc的大小，首先会去检查每个bins链是否有与malloc相等大小的freechunk。如果没有就去检查bins链中是否有大的freechunk可以切割（除去fastbins链），如果切割，那么就切割大的freechunk，那么切割之后的chunk成为last remainder，并且last remainder会被放入到unsortedbin中（这里往往可以泄露libcbase）\*\*
free函数
------
- 先看能不能放入fastbin，再看能不能进行后向合并与unlink prev chunk，再看能不能和top chunk合并，最后看能不能前向合并与unlink next chunk，不论进不进行前向合并与unlink next chunk，都要放入unsorted bin的头部，之后还有一些检查
1. 做一系列检查
2. 判断chunk大小是否小于max fast，做检查后get fastbin index for the chunksize,然后判断fastbin的first chunk是否是这个chunk（这里应该防止fastbin double free，但是很好绕过），放入fast bin中
3. 判断chunk是否是mmaped，如果是（目前先不了解）。如果不是，做一系列检查，最重要的就是检查当前的chunk是否是inuse（这也是为什么只有fastbin double free）
4. 检查通过后，检查prev chunk inuse，如果为0，unlink prev chunk;否则看next chunk：如果next chunk为top chunk，与top chunk合并；否则就看next chunk是否inuse,如果inuse为1，什么都不做；否则进行unlink next chunk,除了和top chunk合并的，都要将new chunk放入unsorted bin头部
概念明晰
----
- bins的链表用的是头插法
fd和bk只在bins才有
在堆中prev chunk就是比它地址低的，next chunk就是比它地址高的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9872fbeb8e38d5aa53fc75b354c4c717f0e05258.png)
- fd,bk指向的chunk的头而不是mem区域
- fastbinsY和bins要区分开来
- 高版本的glibc，如果某个大小的tcache bin满了后再free这个大小的chunk，那么就会尝试进行unlink，如果没满那么是直接放入相应的tcache bin中的
- malloc\\_consolidate和unsorted bin大循环不是绑在一起的，而是在malloc的过程中，大部分的malloc\\_consolidate后也会进行unsorted bin大循环
- unsorted bin里面的chunk大小&gt;想要分配的大小，并且在其他bin中都没有合适大小的chunk，那么一定会从unsorted bin进行切割分配
- malloc的时候，不论malloc的大小，首先会去检查每个bins链是否有与malloc相等大小的freechunk。如果没有就去检查bins链中是否有大的freechunk可以切割（除去fastbins链），如果切割，那么就切割大的freechunk，那么切割之后的chunk成为last remainder，并且last remainder会被放入到unsortedbin中（这里往往可以泄露libcbase）。 [这篇博客讲的很清楚](https://blog.csdn.net/qq\_41453285/article/details/97803141)
basic\\_skills
=============
各个bin的大小
--------
以下皆为chunk的大小：
fastbin:0x20-0x80
smallbin:&lt;=0x3f0
largebin:&gt;=0x400
tcache:0x20-0x410
unlink
------
- unlink 的目的是把一个双向链表中的空闲块拿出来（例如 free 时和目前物理相邻的 free chunk 进行合并）比如当前Q是使用中的一个chunk，P是Q的prev chunk或者next chunk，如果free(Q),那么在堆空间上P,Q相邻且都被free，要合并这两个chunk,首先要先把P从bin中取出来，因此进行了unlink,unlink是对P进行的操作。
- unlink要绕过的检查,检查有个缺陷，就是 fd/bk 指针都是通过与 chunk 头部的相对地址来查找的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6027342a667a9a3cb63eb9a6ff675936090d7c69.png)
off-by-one/off-by-null
----------------------
- 当chunk大小&lt;0x80的时候会直接进入tcache，不会参与unlink
- unlink之后的overlapping chunk都会进入unsorted bin，不论其大小
uaf
---
- 条件：在free掉一块内存后，没有将其置为NULL，紧接着申请大小相同的内存，操作系统会将刚刚free掉的内存再次分配。(为了更高的分配效率)
- glibc 堆分配的策略为first-fit。在分配内存时，malloc 会先到 unsorted bin（或者fastbins） 中查找适合的被 free 的 chunk，如果没有，就会把 unsorted bin 中的所有 chunk 分别放入到所属的 bins 中，然后再去这些 bins 里去找合适的 chunk。
chunk extend and overlapping
----------------------------
- chunk extend 就是通过控制 size 和 prev\\_size 域来实现跨越块操作从而导致 overlapping 的
- 漏洞利用条件：漏洞可以控制 chunk header 中的数据（所以经常会结合off-by-one一起用）
- 漏洞作用：一般来说，这种技术并不能直接控制程序的执行流程，但是可以控制 chunk 中的内容。
- 利用方法：后向overlapping:一般都是通过修改该chunk的size字段，再将其free，free的时候就对next chunk进行了overlapping。如果再malloc合适大小，就可以得到extend后的chunk，通过edit函数进行控制。而且如果extend后是small bin的大小，会放入unsorted bin中，这时候chunk会有一些有用信息
personal skills
===============
- 注意二级指针，\\*的作用是解引用，把它想成访问地址又形象又好理解
- 学会画图很重要
- 注意malloc的大小和实际开辟的chunk的大小
- 传给free的指针应当是指向mem的指针
- tcache中next指针指向的是mem;fastbin的fd指针指向的是chunk header
- 一个指针值为多少它就指向哪里
- 各种bin,tcache都是有一个结构体指针数组，充当着链表头
- 区分&amp;p,p,\\*p
- 注意add,edit,show,delete函数的判断条件，这很重要，特别是delete有时候没有任何判断
- 基本上要打hook的情况下，最后都是要通过tcache构造:chunk-&gt;hook，再申请两次向hook里面写入东西
- 要有防止与top chunk合并的意识，每次多分配一个chunk防止与top chunk合并
- 当a是指针变量时，a-&gt;b等价为（&amp;a）.b
- 从 tcache bin 中申请堆块出来需要保证 counts &gt; 0，一般情况下打hook时tcache结构都是1-&gt;0变成1-&gt;hook，counts&gt;0是满足的，当特殊情况是需要留意counts &gt; 0
- 注意到底有没有uaf可以利用,下面这个看似置0了，但是注意是栈上的置0，不影响bss段中的notes
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c7f646d575c1a94f7bd53d37e1325aadce67078c.png)
- 注意fastbin是0x20-0x80,留意打tcache时chunk大小是fastbin
- 一般没有uaf的时候，就必须有off-by-one，不然就无法泄露，除非partial overwrite申请出stdout
- largebin attack最好用之前申请过的，反正总有奇奇怪怪的问题
- 学会伪造fake chunk泄露libcbase这个技巧，想一想free的一些检查，很容易就得到了libcbase
- \*\*当没有edit的时候一定会打chunk overlapping，只有得到一个大的overlapping chunk之后，将其free后再add就可以实现等同于edit的功能，这是一种很常见的技巧\*\*
tricks
======
\*\*1. 泄露libcbase，heapbase\*\*
\*\*2. 打free\\_hook或IO\\_FILE\*\*
[保护机制](https://jkilopu.github.io/2021/05/12/glibc%E5%90%84%E7%89%88%E6%9C%AC%E7%9A%84%E5%A0%86%E4%BF%9D%E6%8A%A4/)
泄露heapbase
----------
- 一般想要泄露heapbase的情况比较少见，都是想要修改tcache\\_perthread\\_struct才泄露。方法也很简单，有show函数直接让tcache结构变成：1-&gt;0,那么show(1)然后再dbg一看算一下相对偏移就行了(或者直接heapbase = heap &amp; 0xFFFFFFFFFFFFF000)
泄露libcbase
----------
- 一般都是通过unsortedbin的特点来泄露libcbase，因此如何绕过题目限制得到一个unsortedbin chunk是核心问题。show出来的是main\\_arena附近，直接手动算个偏移就行了
- largebin可以同时泄露libcbase和heapbase，但是要注意泄露后修复largebin
- 有时候也会遇到没有show函数的情况，此时可以打\\_\\_IO\\_2\\_1\\_stdout
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d6ea75555ec1bf900945816755b8b8d4a821bfc3.png)
- 有时候会没有uaf，这样进入unsorted bin也不是很好泄露。但是可以利用chunk进入unsorted bin或者largebin会向其fd或者bk写入libc地址的特性，再add出来进行泄露就可以了
free\\_hook
----------
[可以看看这篇文章](https://seanachao.github.io/2020/07/13/hook%E5%8A%AB%E6%8C%81/#free-hook)
tcache\\_perthread\\_struct
-------------------------
- 这个还是很好用的
- 有时候可以add的次数有限或者可以申请的chunk数量有限，所以不能直接用一个循环填满tcache，这时候可以通过修改tcache\\_perthread\\_struct中的counts数组，也可以达到填满tcache的效果
- 这个是libc2.30以下的tcache\\_perthread\\_struct结构，counts类型为char
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ad2e4a614e652bf5e8003cecdb80567a8f6680b1.png)
- libc2.30及以上counts的类型变为unit16\\_t，总大小为0x10+2\\*0x40+8\\*0x40=0x10+0x80+0x200=0x290
- \*\*很显然这个时候要泄露出heapbase\*\*
mp\\_结构体
-------
不能使用tcache -&gt; 通过large\*bin attack修改mp\*.tcache\\_bins -&gt; free相应chunk（满足tcache-&gt;counts\[tc\\_idx\] &gt; 0） -&gt; 修改tcache的相应entries -&...