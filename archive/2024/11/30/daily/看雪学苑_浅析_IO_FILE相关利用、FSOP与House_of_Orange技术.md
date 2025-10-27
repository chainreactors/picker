---
title: 浅析_IO_FILE相关利用、FSOP与House_of_Orange技术
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458584586&idx=1&sn=c14c9df12deb9d8b04c597dae49adfc8&chksm=b18c368086fbbf96bf460715768ed2947c21eb3e8dad19e7d1bdacf5ef63d2f9ece67215d9e4&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-30
fetch_date: 2025-10-06T19:16:15.089909
---

# 浅析_IO_FILE相关利用、FSOP与House_of_Orange技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4hmnJlCQLpSqCCqGEl8775S0ZXyo32dhldJib4KR30BStVvAeI96uhoA/0?wx_fmt=jpeg)

# 浅析\_IO\_FILE相关利用、FSOP与House\_of\_Orange技术

是气球呀

看雪学苑

为什么要学习\_IO\_FILE？

\_IO\_FILE的特性可以让我们在没有show的情况下完成信息泄露，也可以让我们在没有free()给出的情况下完成getshell。

\_IO\_FILE内部含有丰富的虚函数，对这些虚函数进行劫持，能够形成类似于修改got表的效果。

同时libc 2.34(2021年出现的)以后的libc版本都没有malloc\_hook之类的hook了，以后的版本都必须要运用\_IO\_FILE相关攻击来完成堆利用最后的步骤了。

一些高版本libc利用，也都需要IO\_FILE相关的基础知识，所以确实非常值得一学。本文主要目的在于梳理一下\_IO\_FILE相关的结构体，并尝试解释一些较低版本的利用手法，不涉及目前的高版本主流利用手法，仅作为下一阶段学习的预备。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xmZqtqSCpA0hqFnV6LGv52HFIxrf2VNiclMJSmo484U8yLUOGW9xFdg/640?wx_fmt=gif&from=appmsg)

**01**

**从I/O操作到\_IO\_FILE内部细节**

I/O流的操作，如stdin stdout stderr，是由FILE结构体所承载的。因为“一切皆文件”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4RuI5ak9DBIicfgsiaDm47iaEdN3B3tcNFuCeLZyzOZMNzBIqIb69qsPDQ/640?wx_fmt=jpeg&from=appmsg)

Linux 和 Unix 系统中，几乎所有的 I/O 操作都通过文件描述符来进行，这包括常规文件、设备、管道、网络套接字等。这种“一切皆文件”的思想提供了一种统一的抽象，使得程序可以使用相同的系统调用（如 read、write、open、close）来处理各种不同的 I/O 资源。

在这种背景下，C 标准库的 FILE 结构体也提供了一种统一的接口来处理各种 I/O 流，包括标准输入、标准输出、标准错误、文件等。FILE 结构体背后封装了底层的文件描述符和缓冲区管理，使得程序员能够用一致的方式来进行 I/O 操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4I0c7tYW854nia8lTk9412sg1ia1iaziayMffTdHMJwdM8iaGoXuIPibNeB1A/640?wx_fmt=jpeg&from=appmsg)

\_IO\_FILE是FILE实际的实现部分，对外不公开透明（opaque），这样易于用户进行使用而无需关注内部细节——如果需要修改 \_IO\_FILE 的内部实现，可以在不改变外部接口（即 FILE 和相关API）的情况下进行。

那么，\_IO\_FILE内部是如何实现的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xmZqtqSCpA0hqFnV6LGv52HFIxrf2VNiclMJSmo484U8yLUOGW9xFdg/640?wx_fmt=gif&from=appmsg)

**02**

**\_IO\_FILE结构体**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4jBsqJYv4WSZkdd6gtCriaHI3BVicPoH9xqBZA5CicK4vmYQwqOQQS0zmg/640?wx_fmt=jpeg&from=appmsg)

其实主要就是定义了文件的读写过程中需要用到的开始和结束的地址信息等，比如，write\_base,write\_end,这是控制写出内容的地址范围的。

如果攻击过程可以更改这两个值，那么，就可以在下次puts()、printf()等输出类函数执行的时候，造成被指定内存上的信息泄露。

其注释翻译如下，重点关注具有【标注】的部分：

```
struct _IO_FILE
{
  int _flags;/*【flag标志位】高两位字是 _IO_MAGIC，在这里是固定的"0xfbad"，低两位则决定了程序的执行状态。*/

  /* 以下指针对应于 C++ 的 streambuf 协议。*/
  char *_IO_read_ptr;    /*【读入】 当前读取指针 */
  char *_IO_read_end;    /*【读入】 读取区域的结束位置。*/
  char *_IO_read_base;    /*【读入】 回退区和读取区域的起始位置。*/

  char *_IO_write_base;    /*【写出】 写出区域的起始位置。*/
  char *_IO_write_ptr;    /*【写出】 当前写出指针。*/
  char *_IO_write_end;    /*【写出】 写出区域的结束位置。*/
  char *_IO_buf_base;    /* 保留区域的起始位置。*/
  char *_IO_buf_end;    /* 保留区域的结束位置。*/

  /* 以下字段用于支持回退和撤销操作。*/
  char *_IO_save_base; /* 非当前读取区域的起始位置指针。*/
  char *_IO_backup_base;  /* 回退区域的第一个有效字符指针 */
  char *_IO_save_end; /* 非当前读取区域的结束位置指针。*/
  struct _IO_marker *_markers;
  struct _IO_FILE *_chain;/*【链接】这里就是_IO_FILE之间的chain指针*/
  int _fileno;
  int _flags2;
  __off_t _old_offset; /* 以前是 _offset，但它太小了。(注：原话如此))*/

  /* pbase() 的列号加1；0 表示未知。*/
  unsigned short _cur_column;
  signed char _vtable_offset;
  char _shortbuf[1];

  _IO_lock_t *_lock;
#ifdef _IO_USE_OLD_IO_FILE
};
```

###

### flag

flag标志的作用是什么？事实上，能够在以下文件处找到\_flag字段的定义，以及低四位的值所对应的含义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO49pjuibaiam7YtsTqZGtIviarK9EicLWIRFV5omFcO8ef558Q5vC0D7iaFiaA/640?wx_fmt=png&from=appmsg)

一般在执行流程中会将\_flag和定义常量进行按位与运算，并根据与运算的结构进行判断如何执行。

### \_IO\_list\_all与chain指针

常见FILE结构体，比如stderr,stdout,stdin之间，有什么样的关联指针？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4RuI5ak9DBIicfgsiaDm47iaEdN3B3tcNFuCeLZyzOZMNzBIqIb69qsPDQ/640?wx_fmt=jpeg&from=appmsg)

通过chain指针，FILE(IO\_FILE)结构体互相之间形成了链接关系，
\_IO\_list\_all则是指向首个FILE结构体，一般就是stderr

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xTEcnDIwvib7fl07eic1SN12mq9BOd9yDR4TvK1ibtT6hnHnlwYWH6oJQ/640?wx_fmt=jpeg&from=appmsg)

\_IO\_list\_all同时是libc库文件里的一个指针，可以通过偏移获取其值

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4UpDvUzLr64rX52vuyib5R09AT9uIDLpgN3447j9oZLRicWsLc525ZyrQ/640?wx_fmt=jpeg&from=appmsg)

到这里就很好理解什么是FSOP文件流导向编程攻击了，从攻击者的角度出发，覆写\_IO\_list\_all指针，然后使用chain指针控制执行流。

其与ROP攻击同样是通过某种方式来改变了程序执行流程。

## \_IO\_FILE\_plus结构体

这是\_IO\_FILE的扩展结构，也是现在真正的主流结构，首先是引用了FILE结构，即\_IO\_FILE本身。

其变动在于，扩展了一个IO\_jump\_t类型的虚函数表(vtable,vitural table)指针。虚表，其中记录了本类中所有虚函数的函数指针，也就是说是个函数指针数组的起始位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4giaoEMMDyRtrs3pxHOPXMHEaYZ1NicBpfiahqeow3szvsaics2PM1LMbcA/640?wx_fmt=jpeg&from=appmsg)

为了方便之后的利用，在此贴出完整的\_IO\_FILE\_plus结构体内部的各字段偏移如下：

```
0x0   _flags
0x8   _IO_read_ptr
0x10  _IO_read_end
0x18  _IO_read_base
0x20  _IO_write_base
0x28  _IO_write_ptr
0x30  _IO_write_end
0x38  _IO_buf_base
0x40  _IO_buf_end
0x48  _IO_save_base
0x50  _IO_backup_base
0x58  _IO_save_end
0x60  _markers
0x68  _chain
0x70  _fileno
0x74  _flags2
0x78  _old_offset
0x80  _cur_column
0x82  _vtable_offset
0x83  _shortbuf
0x88  _lock
0x90  _offset
0x98  _codecvt
0xa0  _wide_data
0xa8  _freeres_list
0xb0  _freeres_buf
0xb8  __pad5
0xc0  _mode
0xc4  _unused2
0xd8  vtable
```

在以上的偏移之中，有一个显得比较特别，vtable，它是指向虚表的结构体指针。那么，vtable的内部构造又是怎么样的？

## \_IO\_jump\_t结构体

vtable虚表指针所属的IO\_jump\_t类型的结构如下，这个小小的表，承载了相当多的虚指针，修改这些指针可以实现类似于got表劫持的效果，也是高版本libc利用的常客了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4vY9icHPBX4zMJTgAbhLiaS15JnyMs8DXrZ7lF98fbqKiaZtETbo6XncTg/640?wx_fmt=png&from=appmsg)

这个函数表中一共有19个虚函数，分别完成IO相关的功能，由IO函数调用，

只要涉及到io操作，都会间接调用\_IO开头的虚函数，比如调用write就一定会间接调用\_\_write,调用puts就一定会间接调用\_\_xsputn等等。

显然，这就可能造成类似于got表劫持攻击的情况：控制了\_\_xsputn为onegadget，调用puts就会经过这一必然被执行的地方，从而getshell。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xmZqtqSCpA0hqFnV6LGv52HFIxrf2VNiclMJSmo484U8yLUOGW9xFdg/640?wx_fmt=gif&from=appmsg)

**03**

**信息泄露：无show条件下泄露libc基址**

针对没有show()的情况，可以对\_\_IO\_2\_1\_stdout(别看这一长串，其实就是stdout)这其中一个IO\_FILE结构体内部的write地址相关指针进行篡改，并在后面触发puts()，使得该结构体被使用，而且其实同时可以具备任意写能力。

## \_IO\_XSPUTN

主要参阅以下代码
https://github.com/bminor/glibc/blob/release/2.23/master/libio/fileops.c

为了方便看，再把\_flag字段的含义贴在这里一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4ZM5gJ4rUVq160a68D6261EFU3hfloRexunB78hMAcHDb0I4hGzVsOA/640?wx_fmt=png&from=appmsg)

\_IO\_XSPUTN，实际上的hidden ver是\_IO\_new\_file\_xsputn，其实hidden在这里又是类似于对用户透明的意思，\_IO\_new\_file\_xsputn才是。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4xchp6eyRk5DuvAJf0eSdbJdoa9YImwiaU0wlML4Cn6vvwzyO8vjPy5g/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4PoVvUSp5siczkY0haI8m6BKgv16gvFPED1NAvnI8EWI6BArOTpdNp1A/640?wx_fmt=jpeg&from=appmsg)

跟进去\_IO\_new\_file\_xsputn看，观察其伪造条件，不多说，上图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4bwR6dPf0r4SZb1GUfsW2t7KFhAArvbMNmgXAVpzic5Jicd6rp2EywBvQ/640?wx_fmt=jpeg&from=appmsg)

事实上，行缓冲那部分的逻辑不一定要到，而我们重点关注这几个部分：\_IO\_OVERFLOW、new\_do\_write。。

### 如何令\_IO\_OVERFLOW不返回EOF：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4O7PCUkVsuI0ricw4TYy9wbRvgMJsbn4ib0ehlGicb69QC5pSZTCmG9pJA/640?wx_fmt=png&from=appmsg)

###

### 如何使new\_do\_write函数不返回0，而是尽可能大的值

实际上这里，如果count<do\_write，就会提前return，那么就执行不到后面的逻辑了，显然这并不是我们希望看到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO43k4RYnK6Q3MNXstDQoM9l3OZRcB1f4udXA5FJuE1W1zVGTT0hicIYjQ/640?wx_fmt=jpeg&from=appmsg)

所以：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4vvvLUE2SYZjk8zwVu6HIv3VL4t1T0U5icErGj8luibysc0hQGksD2zmw/640?wx_fmt=jpeg&from=appmsg)

满足①即可绕过条件②
综上，可构造\_IO\_IS\_APPENDING、\_IO\_CURRENTLY\_PUTTING 为真，\_IO\_NO\_WRITES为假，write\_base和write\_ptr则指明write的地址范围。

### EXP

```
#include <stdio.h>

int main() {
    long long int *ptr = stdout;
    char str[0x10];

    puts("hahaha:");
    read(0, str, 0x10);

    // 设置flags
    *ptr = 0xfbad1800;  //0xfbad18XX

    // 设置_IO_read_ptr和_IO_read_end
    *(ptr + 1) = 0;  // _IO_read_ptr
    *(ptr + 2) = 0;  // _IO_read_end

    // 设置_IO_read_base
    *(ptr + 3) = 0;

    // 设置_IO_write_base和_IO_write_ptr
  ...