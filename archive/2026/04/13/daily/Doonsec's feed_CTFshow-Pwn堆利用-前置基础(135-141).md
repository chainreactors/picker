---
title: CTFshow-Pwn堆利用-前置基础(135-141)
url: https://mp.weixin.qq.com/s/d7iPvd8jT16Fw0FEkbLynA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:45.593388
---

# CTFshow-Pwn堆利用-前置基础(135-141)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YdkQKXYKSBhE1f2ktI3PYPcau8NeW8dOcuz1SNAsApZaibZoMG0se1Y4ibE2HloQuGT23GYbFFJBN9rYWpR3CDu0JpP6DnVTgWBRVC6QK9JcM/0?wx_fmt=jpeg)

# CTFshow-Pwn堆利用-前置基础(135-141)

原创

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

纪念一下我做的第一个堆题

## pwn135

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBj6libpMxBib6UF9EjVTwRbX8slLzP6icaaKA6nbmmibGMuwiazOJXicKCwZy4om7ufa40icX0qcOV70ZRicHiaRXL7Rmh9op0qH4ZpiaBBw/640?wx_fmt=png&from=appmsg)

135-140是演示题目阶段，好好理解吧，我还是觉得栈到堆跨度有点大，比0基础到学会栈溢出的跨度还大

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia5v7jJSovm3bKltLdHVlm4mGnyPfn9TcHAdGI4LlICWvm7F6G6PHuVicd3hwibnSbrcWJMEdiaP5heN0BemokDSqaJgQvaZDIr7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhha7KYJGoeHJFFqYJu953kFos1psSdIu3rcELyz5wb9xEN0oyzETE7B7gldib4mn9WamE0ibXrbBGaF27nrpyic2RGu90cBwoeww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgQDg1HUArvncZM5ic4e9wIyOE1ibpRCEugF0LyibiaAVibOGEDD2IFZDuDUEr4JFWibKZM9YibnzV0o4gtkVbEkibLKFoT1ibcDN0lWA4E/640?wx_fmt=png&from=appmsg)

上来是做选择题，其实是为了给我们演示一下这几个函数的作用，让我们好好了解一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhmc72O1khq2fnNyAaO2kYwbcPz2S5ua999mjBON5Iia7c0Fq9ZFRjWfyLqiaMfibze4lrH12t7RlK2mF0uuDVfJxsWJ9g2ZakJEk/640?wx_fmt=png&from=appmsg)

靠输入v1在区分，我们就按照v1的大小来分析吧

首先是v1=1，malloc

```
printf("Enter the size to allocate using malloc: ");
__isoc99_scanf("%lu", &size);
ptr = malloc(size);
```

输入1之后会问我们需要多少size来用malloc，我们输入一个无符号长整形之后就开始ptr=malloc(size)了

这是一个内存分配函数，size就是要分配的字节数，ptr在这边是一个指针变量，主要是接受分配内存的起始地址

注意这个是动态分配的，程序运行的时候决定大小，内存不足的时候会返回NULL，最关键的是这边必须手动free(ptr)释放，否则会引发内存泄露

接下来是v1 = 2，也就是calloc

```
printf("Enter the size to allocate using calloc: ");
__isoc99_scanf("%lu", &size);
ptr = calloc(1uLL, size);
```

相对来说其实差不多，但是calloc接受的是两个参数

第一个参数表示要分配的元素数量，这里是一个元素

第二个参数表示每个元素的大小(字节数)，需要从用户输入获取

和malloc主要是区别在于一个是参数数量不一样，另一个是calloc的内存初始化是会自动清零的，而malloc是随机值，分配总量也不一样，calloc分配的是num\*size字节，而malloc是size字节

```
printf("Enter the size to allocate using realloc: ");
__isoc99_scanf("%lu", &size);
ptr = realloc(ptr, size);
```

最后是realloc，可以看到也是俩参数，这个函数明显比前边俩复杂不少

首先，这是一个用于重新分配内存的重要函数，第一个参数是指向之前分配的内存块的指针，而第二个参数是新的内存块的大小（字节数）

成功的返回值就是指向重新分配内存的指针，失败了就返回NULL，然后原来的内存块不变

主要有三种情况

起义是缩小内存

```
// 原始分配100字节
ptr = malloc(100);
// 缩小到50字节
ptr = realloc(ptr, 50);
```

一般是原地缩小，保留前边的内容

第二是扩大内存(原地)

```
ptr = malloc(100);
ptr = realloc(ptr, 150);
```

同样原地，指针不变

最后是扩大内存(迁移)

```
ptr = malloc(100);
ptr = realloc(ptr, 10000);
```

如果后续空间不够的话，会分配到新的大内存块，然后复制原数据到新数据，释放原内存块后返回新地址

注意如果一开始ptr就有内存块，然后在原地又去realloc还失败了的话，原来的指针会被覆盖为NULL，也就是说一开始的内存块在，但现在没有任何指针指向它，也无法访问，无法释放，这也叫内存泄露

大概就这样子了解了一下三个函数的概念，flag很好找的

```
if ( v1 == 4 )
      {
        printf("Here is you want: ");
        system("cat /ctfshow_flag");
      }
```

直接输入4就是了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaS2hvJTHyia9Jicueet5vVhPZwPv34yXd8JCysftHS8gYxK2WMHFC5OpQPO5F6gvibD1GSSK2TKGxaxfSIibkGnSAY6jGZAYQREmg/640?wx_fmt=png&from=appmsg)

## pwn136

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhPK5ahuHGklBXvQt2l5vYGxZicibaHLA9quZPqo2mUPCaEwicjLhz8iaeLSIfxpmf6K07pCfw8QXJb0O4R3W3xs3w8g1lug2q2Z6M/640?wx_fmt=png&from=appmsg)

上题讲了malloc,calloc和realloc三种不同的建堆手法，而这一题则变为了释放堆的题目

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg7IrUaAI97FJHgYibWBPGFcWicF4OVZSA2aZQKv94HuEicPQaENuAvDpjwPypOeq48QvB1MHfxibatf03eYgnfhN5n2hSXficgLLR0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBg44388SoUzW1LNYoceb3IDsO0TkGWDljyJuib4j6ibyyE0oC6QiaVMWFEZzIsRdyhHb1CvkcMVLpUpAZKTBRrQzl9sl2SO3ZlHIo/640?wx_fmt=png&from=appmsg)

发现还是三种，我们来看看具体代码

```
unsigned __int64 ctfshow()
{
  int v1; // [rsp+Ch] [rbp-24h] BYREF
  void *ptr; // [rsp+10h] [rbp-20h]
  void *v3; // [rsp+18h] [rbp-18h]
  void *v4; // [rsp+20h] [rbp-10h]
  unsigned __int64 v5; // [rsp+28h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  v3 = 0LL;
  v4 = 0LL;
  ptr = malloc(4uLL);
  if ( ptr )
  {
    v3 = calloc(1uLL, 4uLL);
    if ( v3 )
    {
      v4 = realloc(0LL, 4uLL);
      if ( v4 )
      {
        __isoc99_scanf("%d", &v1);
        if ( v1 == 2 )
        {
          free(v3);
          puts("ptr_calloc freed.");
          return __readfsqword(0x28u) ^ v5;
        }
        if ( v1 > 2 )
        {
          if ( v1 == 3 )
          {
            free(v4);
            puts("ptr_realloc freed.");
            return __readfsqword(0x28u) ^ v5;
          }
          if ( v1 == 4 )
          {
            printf("Here is you want: ");
            system("cat /ctfshow_flag");
          }
        }
        else if ( v1 == 1 )
        {
          free(ptr);
          puts("ptr_malloc freed.");
          return __readfsqword(0x28u) ^ v5;
        }
        puts("Invalid choice.");
        return __readfsqword(0x28u) ^ v5;
      }
      puts("Memory allocation failed for ptr_realloc.");
      free(ptr);
      free(v3);
    }
    else
    {
      puts("Memory allocation failed for ptr_calloc.");
      free(ptr);
    }
  }
  else
  {
    puts("Memory allocation failed for ptr_malloc.");
  }
  return __readfsqword(0x28u) ^ v5;
}
```

在一个个细看前不难发现，其实每一种释放的都是用的free这边

free的基本操作是先检查指针是不是NULL，是的话就直接返回，不是再继续

接着通过chunk头部的元数据来得到chunk大小和状态，最后根据chunk大小和状态将其放入适当的bin，或者和相邻的空闲chunk合并之后放入unsorted bin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiawF6GXuSLjO7LTA1V2p8yLcegIvgSIC1SlbZptDPUaWkD3CB0B1xXjqKAtCxOHVwib58D10S5ZgjoJIfeSDpiaB80fnCCwvAicUo/640?wx_fmt=png&from=appmsg)

free操作会通过PREV\_INUSE标志和size字段遍历来检查前一个和后一个chunk是否空闲，空闲的话就合并为更大的空闲chunk

一个个看吧，首先就是ptr\_malloc

```
ptr = malloc(4uLL);
free(ptr);
```

看上去很简单，从底层来看，假设ptr指向了一个4字节用户内存的chunk，大小为32字节。由于32字节是属于fast bin小内存的，所以释放之后该chunk会被插入fast bin对应索引的链表头部，其fd指针被设置为原链表头，链表头指向该chunk

堆的状态变化是fast bin里又多了一个空闲chunk，程序其他部分仍持有v3和v4的指针，它们指向的chunk仍处于已分配的状态

后边是ptr\_calloc

```
v3 = calloc(1uLL, 4uLL);
free(v3);
```

分配一个4字节的元素，后边free

这边和之前的malloc完全一样，因为calloc本身就和malloc产生的chunk结果无差异

最后是realloc

```
v4 = realloc(0LL, 4uLL);
free(v4);
```

之前分配块内存的指针在0，在这边又分配了一个新的4字节chunk

其实这边是realloc(NULL,4)，本质上就和malloc(4)无区别了，所以一样的，都是插入fast bin链表而已

如果这三个chunk大小都一样，会在同一个fast bin的，按释放顺序从头部一个个插入

若三个分配连续且无间隙，堆内存可能布局如下（从低地址到高地址）：

```
chunk_ptr (malloc) -> chunk_v3 (calloc) -> chunk_v4 (realloc) -> top chunk
```

释放了一个chunk之后，假设先释放了ptr，那么其chunk被标记为空闲，fd指向了fast bin链表，但是v3和v4还是PREV\_INUSE=1，即不会合并

释放了两个相邻chunk之后，由于fast bin不合并，所以其保持独立，这可能导致碎片化但速度更快

所以其实这一题三个free没啥区别啊

最后还是跟上一题一样直接按4出flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjVXrmuEKJOIQibGb2ofjctgRmML7ztwM18oh9m8ZbxLxVItibKic9IXbiaiaVibIOf6M2Y3iacYxpOxehhx3RdbGC1xrf66icMt1dqXp4/640?wx_fmt=png&from=appmsg)

## pwn137

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaYd1ibpb4zryu2CQl2SPqYHa9wmKCGSssiagicAVP30WyVWBegIICyUX5ibLXmCNwH9BeUOKoSFcXKwlBA7NzsFqrIlpHtw8HDlls/640?wx_fmt=png&from=appmsg)

怎么全是外文

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjvrvcTxE8MmW0ialDxiaY3es2D3Jkz4OOzDBibXk3plIWz9YC12Y0JbZ8CfPYf9EKZEvWdjrDIUFYu9D6QuzDzceBXfvEuiaiba0t0/640?wx_fmt=png&from=appmsg)

介绍sbrk()和brk()两个函数的题目

```
void *sbrk(intptr_t increment);
```

sbrk接受一个参数，increment>0就增加堆大小，<0就减少堆大小，=0就返回当前break位置，错误的时候返回(void \*)-1

本质来说，就是通过相对偏移量在调正堆顶指针，然后返回调整之前的堆顶地址

而brk

```
int brk(void *addr);
```

参数是要设置的新的break地址，也就是结束地址，成功就返回0，失败返回1

简而言之，brk设置堆顶指针，sbrk调整堆顶指针

```
void *sbrk(intptr_t increment);
int brk(void *addr);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhnIflFHrF2FeLibv8ldZicsDEC4Mfja6LUxE4JFPYZkS9yFz5RDmGIHxKv5AE4lhibfLCw1ERgGR4btEAxuicdTiaFD9BrOTTDnwfU/640?wx_fmt=png&from=appmsg)

这边可以看到试完就出flag了，所以flag不是重点，我们主要是尝试两个函数的调用反应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhzn2ZnQBu7QLT3mVe3Xz1O96D9VYQeiaq59PyUouPgjGo9JWzwgzzW6rtxbaU3wov782ByXibvEicZZ1OZCXTUCFJRUx79WvOTBs/640?wx_fmt=png&from=appmsg)

其实跟我们输入的没关系，就是给我们看了看，一开始获取当前程序的中断点位置，之后加了4096，也就是一页，最后又恢复了原始值，所以可以看到地址又回来了

## pwn138

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia1YzD2d8KNDmTxA3szNAwgW7jqABwlMElTvt0gGFAGclSLyeZgJ9XZy0Akz8xl3rqUlmfDYk9WsbmgaLFSnibECjp0N0ewwXzw/640?wx_fmt=png&from=appmsg)

私有匿名映射示例（机翻的

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhJFosNoXbs...