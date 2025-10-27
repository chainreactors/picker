---
title: 浅析libc2.38版本及以前tcache安全机制演进过程与绕过手法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585913&idx=2&sn=5c4eaeec34a6b48ede70a3c2a1b22aca&chksm=b18c3bb386fbb2a5b84abb22974b6f91c8711ceeb39d4e104587d643b540c8e3b7e04acff1c6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-13
fetch_date: 2025-10-06T19:38:43.050472
---

# 浅析libc2.38版本及以前tcache安全机制演进过程与绕过手法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsFia4tZQHPqbHQGPNNIQEKLFvTgDOx476Ao1xyeicULnjHsqUUO4CpB9w/0?wx_fmt=jpeg)

# 浅析libc2.38版本及以前tcache安全机制演进过程与绕过手法

是气球呀

看雪学苑

本文重点关注tcache本身的结构、取用放入的原子操作，以及其free安全机制的演变过程，大概分水岭在于：

2.26(tcache出现)

2.28(\_int\_free引入key防止双重释放)

2.32(PROTECT\_PTR的引入波及tcache利用)

2.34(使得key随机生成，而非tcache\_perthread\_struct的地址)

在这个过程中，可以看到ptmalloc力保tcache的性能，导致没有做到对堆利用的完全封堵。本文对于tcache针对各sizebin的具体操作，将不会表现太多细节，因为如果要关注安全性，其实关注它们的底层一点的安全机制即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsw6VUG8LMFZGVnn7vmtSTwgSvfxo19LPNROYS9aF6YuyORiaJ0pDOVDQ/640?wx_fmt=gif&from=appmsg)

**01**

**tcache安全机制演变与对应绕过手法**

## tcache核心思想

首先不得不提的是，“快”，贯穿整个tcache机制之中——这决定了它的一些安全特性。

这使得刚开始2.26版本下突然引入的tcache没有任何安全检查，在后面的补丁中，也只是做了必要的、不太影响性能的安全检查。

tcache适用于非large bin大小的堆内存的管理，使用单链表，fd指针，每当有新的内存大小被申请，其会创造一个新的入口点(entry)与其大小关联起来，以后申请和释放no large大小的块都会首先经过tcache内部指定大小的入口点的堆块遍历，查找有无合适的块，其中，这个大小通过以下方式来计算。

下面根据glibc版本的演变过程作为时间轴来看看tcache安全机制的变化。

## 早期型tcache（glibc 2.26-2.27）

*https://github.com/bminor/glibc/blob/release/2.26/master/malloc/malloc.c*

所有需要了解的部分都在malloc.c

### 早期tcache结构

画了一下图片来纵观就非常清晰了，这里可以看清tcache的内部结构是怎么样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIs3J9P5FZ824X6mlwD3fEXW0bl1Ap6yBDUcxJZaDENJlyaVNVZVXAHVw/640?wx_fmt=jpeg&from=appmsg)

其中，一些限制值已经在代码上有预先的定义，当然这些个值也可以在编译阶段进行修改。

#### tcache\_perthread\_struct（2.26-2.27)

tcache\_perthread\_struct，顾名思义，是每个线程都维护一个的tcache结构体，可以说其就是整个tcache的主干结构体。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsz0HAK1Orl5ibQVMjqDibslMtDvz9LnicuqfY3RY3JudKg5ryQ76GcOq1g/640?wx_fmt=jpeg&from=appmsg)

其维护了两个数组，实际上，这两个数组的每个位置，是一一对应的关系：一个负责计数，另一个负责管理tcache,一般使用tc\_idx(tcache\_index)这一名称作为数组索引。

而每个索引tc\_idx，其实对应的是不同大小的tcache bins，比如16字节大小的各个tcaches，32字节大小的各个tcaches，64字节大小的各个tcaches，会被分门别类地摆放到各自的entries[tc\_idx]之下。

其分门别类的方式也比较特别，实际上tc\_idx是由csize2tidx()方法生成的，其参数tbytes其实就是用户请求内存的大小。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIs3RDa32TDC1cva9pBe4yqWxBJ5rhKY4jXkXDfRJibYSbRib8iaibTfEkP9Q/640?wx_fmt=jpeg&from=appmsg)

其算法只有一句话：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsF44dicyN04zv3hzEGwOR5FqPSLrJ0VkwC5R8PQOdIvfReMRWW5Ju6Hw/640?wx_fmt=jpeg&from=appmsg)

式中，x指代需要分配的大小。

MALLOC\_ALIGNMENT为各chunk的大小单位，MALLOC\_ALIGNMENT在64位下是16字节，在32位下是8字节。

而MINSIZE在64位下是8字节，32位下是4字节。

以下注释解释了MALLOC\_ALIGNMENT的计算结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIs6qTnPMr64bRzSFvqVG9Go2jjF8n0P6baN2PYmq9MWCMDLF3wkptZaQ/640?wx_fmt=jpeg&from=appmsg)

counts负责计数，计算的数目是每个索引之下的tcache bins数目。而entryies负责保存"入口"，其指向某大小的首个tcache bins。

值得一提的是，这所有的内容其实都是在堆上的，tcache\_perthread\_struct则更是在top\_chunk附近的首个位置。

#### tcache\_entry（2.26-2.27)

早期tcache的tcache\_entry结构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsCFtvZOHrAEewvra6PzibrpLHs7Lcqbk6wxW6wjawciaRtZRpAuydZ0lA/640?wx_fmt=jpeg&from=appmsg)

tcache\_entry实际上指向tcache堆空闲块的fd位置，所以next其实跟fd是一个位置，作用相同，指向该大小tcache下的下一空闲块。

### 早期tcache原子行为

首先了解一下tcache的最基础的行为，取用tcache和放入tcache，这两个行为的定义直接决定了tcache的安全机制是否足够安全。

#### tcache\_put（2.26-2.27)

这是tcache的原子行为之一：放入tcache

仅仅检查了所操作的tc\_idx是否比限制值TCACHE\_MAX\_BINS更大，然后使用了头插法（O(1)）来加入新的tcache\_entry节点，这样比尾插法（O(n)）更快。

然后更新对应count[tc\_idx]：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsjdkCWV1xyKqccwB4Y3JdHTHImBEckD61PSYaGumZxFax2yQicj5qstQ/640?wx_fmt=jpeg&from=appmsg)

####

#### tcache\_get（2.26-2.27)

这是tcache的原子行为之二：取用tcache。

同样，仅仅检查了所操作的tc\_idx是否比限制值TCACHE\_MAX\_BINS更大。

然后更新对应count[tc\_idx]：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsVgDrgSVuQL6vpqVfO0ffrWiarRAhAJxGFvEyTWAM4pibMzRf1aUpHkFg/640?wx_fmt=jpeg&from=appmsg)

这里两个原子行为的问题就是，tcache太追求速度了，舍弃了一切的安全机制，不做任何检查，导致极易进行double free，或者poisoning（其实就是溢出）等攻击实际上后期正是在这里做了一点文章，加入了安全机制。

## 中期tcache（2.28<=glibc <=2.33）

读罢早期tcache，其实最大的问题就是没有任何检查给攻击者造成麻烦，但是矛盾就是，这本身是一种强调速度的结构，如果加入安全机制比较消耗性能，那就失去了这个结构的存在意义。所以，现今tcache引入了一种key检验的机制，目的是在尽可能低的性能开销情况下，给没有获得信息泄露能力的攻击者造成一定麻烦。

https://github.com/bminor/glibc/blob/release/2.28/master/malloc/malloc.c

总的来说，中期直到现今的结构大体上是差不多的，示意图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsO7SYCgZCjJUXkMFdwWQ1pEjiatEx1d0OMA6Sh8DvsSIqL4y3y1Wia4Pg/640?wx_fmt=jpeg&from=appmsg)

###

### 中期tcache结构（2.28<=glibc <=2.33）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsVXcqOMztic702EDLDPHq5hcgJCTm4bP0pnf22UITv1C1FqYYFzCIT3A/640?wx_fmt=jpeg&from=appmsg)

####

#### tcache\_perthread\_struct（2.28<=glibc <=2.33）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsT2Z7JEU8Cgy8b7R88P09gXEEnthSFDEnslASwTJMtkgPCGATm5ZPMg/640?wx_fmt=jpeg&from=appmsg)

更换了counts的类型，从char数组变为无符号整形，也许是预防了一手类型混淆，而且本来就应该这样写吧。

#### tcache\_entry（2.28<=glibc <=2.33）

可以看到，原本对应于堆块的位置，放置了一个key值，这个key值就是2.28新增的安全机制的安全性保证所在。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsLxeZwntibAA4ko93EHyh2tDUibI9Gh2cZUeJ1BvxGs17Pv5cY8vCYPmg/640?wx_fmt=jpeg&from=appmsg)

key实际上就是tcache\_perthread\_struct的地址，换言之，其在不同的tcache bin上是一样的值，一旦tcache\_perthread\_struct泄露就等于全部key的安全机制失效
而且，实际上next并没有做任何的校验。

#### 中期tcache原子行为(tcache bin的取用和放入)

重点关注key的相关操作：

#### tcache\_put（2.28<=glibc <=2.33)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsrAiaMWT3wIM4FebBNOave34ehwgh6Y4cDiaeIVAyFY3ZqX8OaYZSYZLw/640?wx_fmt=jpeg&from=appmsg)

可以看到tcache的放入时会增添key：

#### tcache\_get（2.28<=glibc <=2.33)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsMOrh7BHpV6apWdjgMA1HKG5csF6INialzsQTIksI0ec1Su9KFO1WicjA/640?wx_fmt=jpeg&from=appmsg)

可以看到tcache的取出，置空了key，以免在tcache堆重叠的情况下造成key泄露。

### key如何于free过程进行操作验证

如果一个chunk不是由mmap（申请128KB或更大的块）分配得到，就会调用\_int\_free进行释放。

其实就是说，fastbin,tcache bin，small large bin,unsorted bin这些都是归\_int\_free管的。

话不多说，跟进到\_int\_free()：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsiciaeNx0oYF8Y4JALVgDfibBBiaRKaNkprFy1hLE6uIviaickAJszrS5gy8g/640?wx_fmt=jpeg&from=appmsg)

省略部分代码，然后，代码经过一个关于 USE\_TCACHE 的if判断，就会进入这里
请先默读一句话：“在tcache这里，答错key有奖励，答对key有惩罚”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIskv2YHMopC5QZjQZtCMUQZS4VEianJ6W8RLk4ZIk6kVBHNXgGFJgwicLQ/640?wx_fmt=jpeg&from=appmsg)

\_int\_free把tcache bin跟一般bins混在一起，且使用操作块的key是否正确，来判断要不要跳入验证逻辑，所以其double free防御机制只会在key正确时启动。

可以看到作者使用了unlikely来引导了glibc的分支预测来提高性能，这是因为很多情况下确实是 USE\_TCACHE=1跳进来这里，但很多时候都不是tcache下的那些操作，所以要给它们更侧重的性能优化，实际上这被认为是一种剪枝算法，其确实在性能近乎不受影响的代价下，最大可能地给攻击者造成麻烦。

但值得一提的是，其e->key有极低概率被其它chunk的bk值刚好相等，导致进入该检查并触发double free的检查，这样的话会造成性能上的缓慢，但毕竟概率极低，可以接受。

有好些文章里说这个e->key条件下的绕过double free很难，但是ta们全都错了，只要e->key不正确，就等于不需要进行那些判断了，而且这也并不会影响tcache\_put的执行。

这里有个逻辑问题，只要我们的改写再稍微溢出一点点，改到tcache bin结构内比fd稍高地址的bk部分，即存放key的部分。

改成不一样的key，就能轻松绕过判断逻辑继续double free。（这里让我一度怀疑是不是看漏了什么，事实如此）

## Double free检测绕过（适用至今！）

能直接改key，就等于绕过double free检测了，这种方法就不细说啦。

当然，如果没有对key的直接改写能力（比如，受限的溢出长度？），还可以考虑以下两种方法：

### 通过覆盖free chunk的size误导tc\_idx生成

（更少的溢出长度）改变被 free 的堆块的大小，于是在以上遍历时可以误导tc\_idx的计算，从而使tchache进入另一entry入口，这样就能避开double free检查。

回顾tc\_idx的计算方法：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIs3RDa32TDC1cva9pBe4yqWxBJ5rhKY4jXkXDfRJibYSbRib8iaibTfEkP9Q/640?wx_fmt=jpeg&from=appmsg)

其算法只有一句话：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FOSrZ2X5sAkEPTza7QFRIsF44dicyN04zv3hzEGwOR5FqPSLrJ0VkwC5R8PQOdIvfReMRWW5Ju6Hw/640?wx_fmt=jpeg&from=appmsg)

式中，x指代需要分配的大小。

MALLOC\_ALIGNMENT为各chunk的大小单位，MALLOC\_ALIGNMENT在64位下是16字节，在32位下是8字节。

而MINSIZE在64位下是8字节，32位下是4字节。

实际上我们可以通过对请求大小的伪造，从而误导tc\_idx的指向，以让double free检测检查不到任何重复的块（因为在别的chunk大小的entry处进行遍历）

### House of botcake:free#1 unsortedbin(无key)->#2 tcache(有key)

House of botcake，简单来说就是抓住了tcache的一个特点：它只管tcache本身的double free安全，对于unsorted bin的块，因为其bk字段与key对不上，所以不会被检查。

据此可以创造堆重叠的时机：

> 通常的利用思路就是，填充完 tcache bin 链表后，然后把一个chunkA free到 unsorted bin 中，然后把这一个chunkA 上面紧邻的chunkB free掉，这样A、B就会合并，unsorted bin中的fd指针就从chunkA 的fd指针，变成了chunkB 的fd指针。
>
> 之后我们先申请一个chunk 在tcache bin中给chunk A 留下空间，利用 House of Botcake 的原理（指u...