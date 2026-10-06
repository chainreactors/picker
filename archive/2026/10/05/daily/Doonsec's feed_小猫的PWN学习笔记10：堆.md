---
title: 小猫的PWN学习笔记10：堆
url: https://mp.weixin.qq.com/s/CmF52OXToJRbcHqjn8MbzA
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:19:43.976979
---

# 小猫的PWN学习笔记10：堆

# 小猫的PWN学习笔记10：堆

原创

小猫信安
小猫信安

小猫信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYI4mQl7kfYnfJEc1ZvTicn9dpfmicicrfsC0Ivp0uz4I8OB7eUtY60xmPuK6MwU5VJwTp4vdnGw7QG0xLQCdAdgaaJUnqSc4kqIOM/640?wx_fmt=png&from=appmsg)

前面我们学过了栈溢出相关的pwn手法，

都是利用栈帧的溢出，进行操纵内存。

![](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYLzqiak8OY2YUvU8SK1PnET7tPjLeLPUYToXl513XVwribOjvnISvJGD1ibTibLybVFWS2lLL9BiaDlLZbtMgKfFSEGL0e23xINJjZs/640?wx_fmt=png&from=appmsg)

实际上

在我们系统中同样也有一个内存结构,叫做堆

堆可以理解为操作系统内的一块内存，每次程序要用到一块内存存东西，就可以向操作系统申请一块内存，这块内存叫做堆。

堆与栈的区别

|  |  |  |
| --- | --- | --- |
|  | 堆 | 栈 |
| 申请 | 程序运行中分配，由程序语句控制申请释放（人工操作） | 程序运行前自动分配，不需要人工操作 |
| 释放 | 人工释放 | 自动 |
| 地址 | 低地址向高地址写入 | 高地址向低地址写入 |
| 内存分配 | 非线性。无序 | 线性。有序 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYLic1kRlId4hNwdSiatXKbibhPentaF5Ak9Gj4oYOk2SX7JnOLAvMY5iazj96MG8rhJREsBp2p7KsbsKN4v3z7Gk8mkl4de4V3iccQE/640?wx_fmt=png&from=appmsg)

简单解释下为什么非线性无序：

例如上面那张图代表一块专门用来存堆块的内存，各个颜色代表不同的堆块，从上到下依次是红，蓝，黄，绿，橙等等

我们的操作系统会切割这块内存为不同长度小区块最为堆，可能相邻也可能不相邻，中间是会存在间隔。

因此，这不同于我们的栈，栈中的元素的地址是连续的，堆中的元素只是在堆块内连续，各个堆块之间无序。

这个过程就堆的管理方式（ptmalloc）

堆管理

我们都学过c语言，当初学习malloc() 和 free() 函数老师只会告诉你这是进行动态内存分配，

但是实际上malloc() 和 free() 分配的就是堆空间，malloc() 和 free() 的底层实现就是ptmalloc进行分配和管理堆空间

ptmalloc采用边界标记法将内存划分成很多块，从而对内存的分配与回收进行管理。为了内存分配函数malloc的高效性，ptmalloc会预先向操作系统申请一块大的内存供用户使用当我们申请和释放内存的时候，ptmalloc会将这些内存管理起来，并通过一些策略来判断是否将其回收给操作系统。

堆储存在哪里呢？

以32位 4gb内存为例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYILH35G1LqjB20OkQAB3JhpZEhdOBB0HPlc7oKneEKdXIJbrgS81mQYPGS9R5telSicQxVqrMZ08aIS1ohekd7vf7Eovn67h5Kk/640?wx_fmt=png&from=appmsg)

这里看到了我们熟悉的bss段，text段，data段等等，这些存在程序最底地址部分，上面的heap就是我们所有堆块存储的地方（对应上图专门用来存堆块的内存，从上到下依次是红，蓝，黄，绿，橙等等），在stack栈存储的地方下面，在bss段，text段，data段上面。

上面的箭头也直观展示了堆向上增长，栈向下增长。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYK4VcFvGXV5NbotvdAhVW7XTwlpnvpJkcsXZdRYdSnccS96V8E5LavSIZHvDeh5cIpu6BibOxEJUoL0BoIsC1hp5Jua0sm2E5W4/640?wx_fmt=png&from=appmsg)

这里中间可以注意到有一个Memory Mapping Segment，这个叫程序的内存映射空间MMAP，由程序自行进行分配，我们熟悉的libc就是加载到这个位置然后和我们的程序进行拼接。

我们的存堆的heap区域离mmap很近？

如果我们的堆很多，需要很大的heap，能不能瓜分一部分mmap区域呢？

当然可以！

此外我们还可以瓜分bss部分区域，也就是heap向下扩展，这种操作叫brk

![image-20210808212344994](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYIINs9njHXkMnfNLrngRTYt2ZIEJ0CaqC8Q2C5Lf0zB1DwJJyPHkymCJf3FaFIPPGWCaqeCYg5Vv4OSgicibY8yhJQvucbGPpVv0/640?wx_fmt=png&from=appmsg)

![image-20210808211341106](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYJ2NWFMEbbppjd6LicoyKh8dv7pevP5tEmQLfCUwvwWficWicTdDNSwPEX6SKdlxmFlwZic3tn58hproBgpOt0NFvbfXqSQoHUS594/640?wx_fmt=png&from=appmsg)

因此，我们想要得到heap区，

有两种申请内存的系统调用：

brk

mmap

第一种brk，是将heap下方的data段（bss属于data段），向上扩展申请的内存。

第二种mmap，瓜分mmap区域，也就是内存映射。如果使用这种方式申请内存，那么就在mmap区域内开辟新的内存空间给heap。

堆结构

那么我们每个堆块长什么样呢？

堆不同于我们的栈，堆块种类分为正在使用堆块和空闲堆块。

正在使用堆块：alloced\_chunk

![](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYLAzkFedGCaYlNUGWmytdscR0CTWkJDJv8GEP5KXTwrTtPib9kQ8ZZjYn2UuvTjsN4x7ng2gyF8ClYlrLA3cibCL0XkTjBUMZf2g/640?wx_fmt=png&from=appmsg)

黄色区域代表一个完整堆块

先看堆块内部储存的数据：

第一部分叫pre size：记录上一个堆块大小

> 为什么要记录上一个堆块大小？
>
> 因为我们操作系统堆块是通过链表结构进行管理

第二部分：

size记录当前堆块大小，

size字段的最低三位A,M,P是标志位:

M=1 为mmap映射区域分配；M=0为heap区域分配
A=0 为主分配区分配；A=1 为非主分配区分配。

> （内存分配器中，为了解决多线程锁争夺问题，分为主分配区main\_area，非主分配区no\_main\_area。分配区的本质就是内存池，管理着chunk，一般用英文area表示，了解即可）

P代表前一个堆块是否在被使用  1是0否

第三部分：user data数据区，堆真正存数据的地方，我们想存的数据储存在这里

第一部分和第二部分叫做堆头，设置的目的是方便堆管理器进行管理，不存储数据。

左侧的两个指针分别是堆管理器的指针，chunk指向堆的头部，mem指向数据区头部，我们c语言里每次malloc就是返回一个mem指针。

空闲堆块：free\_chunk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYItbhYqlEE76GmbPR5aibuYQ343HIVKbesviceFDH0PCdxGzD5hf1o6qHCmwRlsPuz4RweelUl6agPXLm1ljYoMsB4AQ4Cia5JO7E/640?wx_fmt=png&from=appmsg)

free\_chunk本质上就是相比alloced\_chunk多了两个指针fd和bk，和两个储存前后两个堆块大小的值

指针fd指向后一个空闲的chunk,而bk指向前一个空闲的chunk，malloc通过这两个指针将大小相近的chunk连成一个双向链表。

堆的真实内存形态

当然理论很枯燥，接下来看看堆在我们真实内存空间究竟长什么样

新建heap.c

```
#include<stdio.h>#include<stdlib.h>int main(){  char *p=(char *)malloc(0x10);  free(p);}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYLGZGXGV4Id1hS55vVtppJtOzORichvMM3zVPTWIzxjhYhMnPmLUnC7fGD8tTAI1KaeBKF7k29NA4vwLVqdPcbCPuN5IkVeTJEs/640?wx_fmt=png&from=appmsg)

我们在这个程序分配了0x10大小的空间

用gdb进行编译

```
gcc heap.cgdb a.out
```

在main函数打断点

![](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYLpeoPnkFlcPzMGiblibmaZRLqXybptRIEJZbiaNF8DFviaE0NrHKChPL3kpwJEicvTDObDrTZGFK3qiacnIxTrdPya7CMqtOaPoE6oE/640?wx_fmt=png&from=appmsg)

运行

```
r
```

然后输入

```
vmmap
```

查看内存映射

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYJibqkdibkyPzlxwxkAb9RuDVTKZjR5zFrqytJb0bGXhA2KgP38UCK85L9HqV4MsbiccibR1DPUl7k7mgb22eKvGQgcvsKEEiaPyMd4/640?wx_fmt=png&from=appmsg)

可以看到没有关于蓝色heap的标识，因为堆是经过程序主动申请malloc才有的，我们现在还没运行到malloc语句

输入n继续运行下一条语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYLxRFbBtlYaTkJxhwsE0Fo5RLu6kVf7q8EpfmpbqpqBMnWGX7MKicqthYOgdDpEmib6kPcFXO8aYqnexHhicPV4cstDjkyIaPjMYs/640?wx_fmt=png&from=appmsg)

可以看到出现heap了，左边0x555555559000就是堆起始地址，0x55555557a000就是结束地址，总大小0x21000

但是我们是

```
char *p=(char *)malloc(0x10);
```

只申请了0x10大小啊？

这也就是我们刚才说的，每次申请prmalloc会先申请一块大的内存，然后再切分为小块供我们使用。这个0x21000 就是最开始的一大块内存

查看堆内部

这里说一下x/20这个gdb命令

```
x / <数量><单位大小><显示格式>  起始地址
```

这个命令作用是直接查看内存，也就是从xxx地址开始,直接看内存里储存了什么

```
x/<n><u><f>
```

* **单位大小 u**：

+ `b` = byte（1 字节）
+ `h` = halfword（2 字节）
+ `w` = word（4 字节）
+ `g` = giant word（8 字节）

* **显示格式 f**：

+ `x` = 十六进制
+ `d` = 有符号十进制
+ `u` = 无符号十进制
+ `t` = 二进制
+ `c` = 字符
+ `s` = 以 NUL 结尾的字符串
+ `i` = 指令（反汇编）

## 常用例子

```
x/20gx 0x555555559300     # 20 个 8 字节，十六进制（看堆块头、指针数组）x/32wx 0x555555559300     # 32 个 4 字节，十六进制（看 int 数组、字符串）x/s 0x555555559320        # 看作字符串（地址处存 "hello" 之类）x/10i $rip                # 从当前指令开始反汇编 10 条x/4gx $rsp                # 看栈顶 4 个值x/8bx 0x555555559310      # 逐字节看（检查字节序、padding）
```

```
我们现在的指针p是储存再rax寄存器里面，值为0x555555559310
```

```

```

![](https://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYKkUkFmn7kChiaaTMicNUfeYOWniaZPWCj1lrWI5gNYxO9IJ6VdAowrhdz9zs6JDzm1gLicWYQvWnZ5QXLI9aTib5QcKbOEqK66M8W8/640?wx_fmt=png&from=appmsg)

```
指针p指向的就是堆块，因此我们用x/20gx $rax代表从$rax当前存的地址打印后面0x20的内存内容。
```

```

```

但是gdb的x/20gx返回的指针是数据区指针，也就是我们上文堆结构讲的mem指针，因此不包括堆头，我们看完整堆起始位置参数减去堆头固定大小（0x10）

```
x/20gx $rax-0x10
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a4nfIUib3hYKDNPnB9y1DFkUpkjQhaDqc6Al1uNPlUlxS38IPRQnUc7Qd4UW4RfgVuicCqjUYiakEjGj2jONfO8B9JmLxkQK5JvqysOgazZT2g/640?wx_fmt=png&from=appmsg)

现在可以看到了，第一行最后的1是上文说的p标识位，代表我们程序现在上一个堆块正在被使用，倒数第二个数字2代表size大小，表示此堆块大小为0x20，第二行就是我们数据区了，我们没有写数据，因此全是零。

```
我们申请的是0x10大小,为什么size是0x20?malloc这个函数传入数值是申请user data数据区大小，真实堆块大小要加上堆头0x10
```

这就是堆的基本结构了。下一期我们将介绍空堆块如何进行管理，也就是各种bin机制，并且如何通过这些堆管理机制，进行攻击

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a4nfIUib3hYIUErCU8AW4XdY96w7xw1gy9wC5tMBjoDq9zlOBFoibv6W3TNBw263cXBq60qC4tic8TsEM2pQjUf2bjHh6c3lzBdLia2nLMu0QHQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过