---
title: PWN堆unlink
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458583680&idx=1&sn=330011e107fbb9f5b1088c9fcde49a8e&chksm=b18c320a86fbbb1c7c7a4282ba526bf61f9b0ff7cfd5c77357c08d3af1df689c3a4be2353afb&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-24
fetch_date: 2025-10-06T19:15:22.980226
---

# PWN堆unlink

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqERrM3TrxnWbVgKuM47PnhsVlQwQ6YicIUZWOkBHzOYzAibrEn5QBRgIA/0?wx_fmt=jpeg)

# PWN堆unlink

iyheart

看雪学苑

介绍

◆unlink，俗称链，将`unsorted_bin`中的处于free状态的堆块脱离出来，然后和物理地址相邻的新free的堆块合并成大堆块（可以是向前合并或者向后合并），合并完之后再放入`unsorted_bin`中。

◆漏洞产生的原因：`offbynull`、`offbyone`、`堆溢出`，修改了堆块的p标志位

◆在这里，建议先了解`unlink`的原理，和如何利用，再学习`off_by_null`和`off_by_one`

◆在本篇文章中会标注堆的高低地址，以便会更清晰的展现unlink的过程。

# 堆再介绍

◆为了更快的获取堆内存空间，程序员设计了`bins`这个数据结构，这个数据结构就是用来更好的，更快速的管理堆、获得堆内存。

◆`bins`只是为了管理`free`之后的堆块

◆`bins`一共有136个`bins`:

* `unsorted bins`
* `small bins`
* `largebins`
* `他们的分布如下`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqTd7JK69pm7bP1C51tMCxOYL96HRF3uLrKD7mdibo74u2JWrcJ4IiaH0A/640?wx_fmt=png&from=appmsg)

◆`prev_size`：记录前一个堆块的大小

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqLiaUNjfM8CdGc8Hdu5FBRicRnnI8jRibxBlYdgp66UK7r1Xhrtpf1BrVg/640?wx_fmt=png&from=appmsg)

◆下图是`size`所表示的堆块大小范围

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqs6eqQzo29LiaYpODKus0e2bJJBQaxggyWcJv4rKN065u5OXfNTibTFiaQ/640?wx_fmt=png&from=appmsg)

◆知道了`size`所表示堆块大小的范围后，接下来就可以解释为什么会有`N`、`M`、`P`标志位了

◆由于一个堆块至少包含了`prev_size`、`size`、`fd`、`bk`。

◆而`user_data`可能会为0，当我们`malloc(0x1)`时，堆管理器会判断申请的堆块会不会满足`fd`、`bk`、后一个`prev_size`内存空间能不能存放下去，如果能存放下去，则`user_data`是为`0`的。

◆而`prev_size`、`size`是`size_t`类型（无符号整数），在32位是4字节，64位8字节，fd、bk指针都一样32位4字节、64位8字节。这样32位的堆块`size`至少要`0x10`,64位堆块至少要`0x20`。并且堆块最后还会和`8字节`或`32字节`对齐。

◆从下图可以看到，size的最小3位都是0，都是空闲着不会改变，所以就将这3位合理利用起来，即将他们做为标志位

```
0x10--->0001 0000
0x18--->0001 1000
0x20--->0010 0000
```

◆而这边的`P`位表示的是与当前堆块物理地址相邻的前一个堆块是否空闲还是在使用，这里`p`等于1就表示物理地址相邻的前一个堆块正在被使用（这里chunk1简单画了就没把user\_data画出来）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzq25LG4q6KRfvTPvQmH3u0qn222BqDYjzLiaIeBBcH25koRibtC1v18FPg/640?wx_fmt=png&from=appmsg)

◆当这物理地址相邻的俩个堆块`P`标志位都为0的情况下，这俩个堆块就会发生合并，俩个堆块合并成一个大堆块，并放在unsorted\_bin这个链表里面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzq6hBA9HxWJg0oPdRXjiabzyfMgBHILkgic0mKbOOS6A9xcolv7pgvGiauA/640?wx_fmt=png&from=appmsg)

◆然后就会变成这样，合并还分为前向合并（堆块从前向后合并）和后向合并（堆块从后向前合并）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqvGBxPRz8ueu07PnT55ib9Hd2s9X8I4OU86PNxtcbJ7icTN71YeibzlVDg/640?wx_fmt=png&from=appmsg)

◆main\_arena：是结构体`malloc_state`的一个实例，下面是`malloc_state`结构体中内部具体的结构

```
struct malloc_state
{
  /* Serialize access.  */
  mutex_t mutex;

  /* Flags (formerly in max_fast).  */
  int flags;

  /* Fastbins */
  mfastbinptr fastbinsY[NFASTBINS];

  /* Base of the topmost chunk -- not otherwise kept in a bin */
  mchunkptr top;

  /* The remainder from the most recent split of a small request */
  mchunkptr last_remainder;

  /* Normal bins packed as described above */
  mchunkptr bins[NBINS * 2 - 2];

  /* Bitmap of bins */
  unsigned int binmap[BINMAPSIZE];

  /* Linked list */
  struct malloc_state *next;

  /* Linked list for free arenas.  Access to this field is serialized
     by free_list_lock in arena.c.  */
  struct malloc_state *next_free;

  /* Number of threads attached to this arena.  0 if the arena is on
     the free list.  Access to this field is serialized by
     free_list_lock in arena.c.  */
  INTERNAL_SIZE_T attached_threads;

  /* Memory allocated from the system in this arena.  */
  INTERNAL_SIZE_T system_mem;
  INTERNAL_SIZE_T max_system_mem;
};
```

◆下面的代码就是定义并初始化`main_arena`

```
static struct malloc_state main_arena =
{
  .mutex = _LIBC_LOCK_INITIALIZER,
  .next = &main_arena,
  .attached_threads = 1
};
```

◆这里面先使用gdb动态调试查看`main_arena`的结构
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqplXH8Vt8WnbCc6WkuW6CVtmz5BKsKjq4BvzwGibsZUsDJstVgYibMPkQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqnE45iaHD0jgibNcha85gTw17icZMUJ3wqxDqzVcGj1W3SDIqic6NhGxtZw/640?wx_fmt=png&from=appmsg)

◆下面用图介绍一下`main_arena`并给出一些在本题中比较重要的一些东西：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqUYrof8uHMicbaECnXPIJ5nLJgojwomre7naDfjy2osFOag6KBoRoCIA/640?wx_fmt=png&from=appmsg)

# 示例程序

◆注：以下程序都是在64位环境下进行的

## 实验1

◆对下面程序进行动态调试，思考以下问题

* 申请的堆块释放后会被哪个`bins`管理？
* p1和p2会发生合并吗？
* p2和p3会发生合并吗？

```
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>

long long int a[100];

int main() {
    long long int *p1 = malloc(0x100);
    long long int *pp = malloc(0x100);
    long long int *p2 = malloc(0x100);
    long long int *p3 = malloc(0x100);
    free(p1);
    free(p2);
    free(p3);
    return 0;
}
# gcc -o unlink_64 unlink_64.c -fno-stack-protector -z execstack
```

### 分析1.1

◆将可执行程序编译后，使用`gdb`动态调试，输入`ni`指令将程序执行到该语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqV14ZEfRnU9qbJJhRT8UrvAicBPVjkpjcxKoBqicsBccZnIBNbTARgicDw/640?wx_fmt=png&from=appmsg)

◆然后使用`heap`指令查看堆块，发现申请了四个堆块，四个堆块都在使用中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqzGfZZjZsWufibkWoicwricF1aFj7qp60JKjyuUiaKhSop1ftKAvZGDlntA/640?wx_fmt=png&from=appmsg)

◆然后再使用`ni`指令，将程序运行到该处（第一个free之后，第二个free之前）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqx2Z2s2nibsF6sKiaa7Nwz1U49JW6L1GTeZBWHgHJPywtP4nduDF5ia2jQ/640?wx_fmt=png&from=appmsg)

◆再使用`heap -v`指令查看，发现第一个被释放的`chunk0`被归入了`unsortedbin`里面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqbs5COrgqxRI22HTaM0uIDjtfNtCszcjGZyBSnPTWsiaCx7WdFBRn3VA/640?wx_fmt=png&from=appmsg)

◆再使用`ni`指令运行到第二个`free`后，第三个`free`前

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqJfFdDzFibNuE17jYuoSsgNjQMhichlnz6N68YtWXe42EjLKwh8avxBUg/640?wx_fmt=png&from=appmsg)

◆再使用`heap -v`查看堆块，发现第二个被释放的堆块也被放入了`unsortedbin`，此时我们还发现第二个堆块（即Addr:0x1200110这个地址的堆块）的`P`位变成了`0`，表示了前一个堆块处于空闲

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqibabwibcWMZIEGUetIEU5mzeWj3fBoWUneJPzibSxG2qApj3mibRNLycqw/640?wx_fmt=png&from=appmsg)

◆这时我们使用`unsortedbin`指令，查看`unsortedbin`，发现`unsortedbin`这个bin上有俩条链子，但是他们并没有合并，这里还要注意一点是unsortedbin是后进先出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqibJAZ26Om488uqRE2V9vS8f1qJkRDR8iayyvRAymh6BTCVI8Xn5gPbpQ/640?wx_fmt=png&from=appmsg)

◆接下来`ni`将程序执行到第三次`free`之后，再使用`heap -v`命令查看堆的状态，发现后俩个堆块被合并了，都合并到了`Top chunk`中，`top chunk`的`Addr`也发生了改变

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzq3ajLJUwsvNeCwQwTdXiarrmzW2LRZcT07pDgydnuGE6e4xSruMSaMxQ/640?wx_fmt=png&from=appmsg)

◆回答：

* 这些堆块被释放后都会被`unsortedbin`管理
* `p1`与`p2`这俩个指针指向的堆块是不会合并的，只有物理地址相邻且空闲的堆块会被合并
* `p2`与`p3`这俩个指针指向的堆块是会合并的

### 补充1

◆编译并调试该段代码

```
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<string.h>
#include<unistd.h>
long long int a[100];
int main(){
        long long int *p1 = malloc(0x100);
        long long int *pp = malloc(0x100);
        long long int *p2 = malloc(0x100);
        long long int *p3 = malloc(0x100);
        long long int *p4 = malloc(0x100);
        free(p1);
        free(p2);
        free(p3);
        free(p4);
        return 0;
}
// gcc -o lab_3 lab_3.c -fno-stack-protector -z execstack
```

◆使用gdb动态调试，使用`ni`指令将程序运行到第二个`free`之后，第三个`free`之前，使用`heap -v`查看堆块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqUaY9dJgGLLBeROlK61yYGD5iaWlVgVyej3UoZhs15rtIDEt7deBVZEg/640?wx_fmt=png&from=appmsg)

◆再使用`ni`指令将程序运行到第三个`free`之后，第四个`free`之前，再使用`heap -v`查看堆块，发现第三个申请的堆块和第四个申请的堆块在释放后被合并了，合并后也会被放入`unsortedbin`里面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqbv8IEz2qyXhWqQm9b6zMGoYKOlWqpYI4ORRUfbRfic0Hfkar6OwTrAA/640?wx_fmt=png&from=appmsg)

##

## 实验2

◆查看分析glibc源码，并使用图描述unlink的过程，然后具体了解unlink的检查过程

◆Index of /gnu/glibc在该网站上找到glibc2.23，下载解压后在该目录`glibc-2.23\malloc`下找到`malloc.c`，搜索到`unlink`，查找到unlink这个宏定义，这段代码就是unlink的具体过程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HvKo7aEEmfwG8NxWDCiamzqclkJgqV3KY3eTIhywlv4xXHgKOzAHgADZUeWe59Z6a3S8Svr8IEWHA/640?wx_fmt=png&from=appmsg)

◆这段代码是unlink的具体代码，也是unlink的具体逻辑，源码看不习惯，我稍微调整了一下位置（没有修改代码）

#...