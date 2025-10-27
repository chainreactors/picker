---
title: VMProtect3.5模拟x86分支指令je、jne、jge和jl的分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458475529&idx=2&sn=d59d371c83e45fa4787d5e2baea980cb&chksm=b18e6c8386f9e59573e5b57d8ea75388f4f71f22b21f469781a8c56aca5f694199a6a1b32d27&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-10-13
fetch_date: 2025-10-03T19:47:16.536442
---

# VMProtect3.5模拟x86分支指令je、jne、jge和jl的分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GoKmKic7yAZ3C2nbNqh7WhmZfSGUNb9PdrbRWcqEAaFG0tGEzzYxILiaQOgM1YgmG4GFDhfplSWsnQ/0?wx_fmt=jpeg)

# VMProtect3.5模拟x86分支指令je、jne、jge和jl的分析

会飞的鱼油

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FHSwvGegS93da30f9s0tcGUA4dvQu2ZPDor1exrKlhr8K9DVCRdT4cLXxMEFgBcEMxN5DPTgbx5w/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：会飞的鱼油

#

#

```
一

前言
```

这篇文章主要是分析vmp3.5对je、jne、jge和jl分支指令的模拟。因为识别出vmp的分支指令后，可以利用符号执行或者其它的trace工具得到程序的全部路径的执行trace，然后合并这些路径重建程序混淆前的控制流图CFG，最后对控制流图进行优化应该是可以还原出与原程序语义上等价的代码。

#

#

```
二

分支指令模拟分析
```

x86指令的cmp实际是执行的减法操作，只是不改变操作数的值，而是程序状态寄存器eflags的值。vmp模拟的减法指令如下：

```
x-y = ~(~x+y)
```

标志位还原如下：

```
eflags1 : (~x+y)elfags2 : ~(~x+y)eflags = (eflags1 & 0x815) + (elfags2 & ~0x815)
```

为什么vmp使用0x815可以参考《VMP学习笔记之万用门（七）》这篇文章。

##

## **Jge和Jl指令分析**

这里先给出根据trace构建的eflags还原的DAG表示和jge指令模拟执行的DAG表示。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJiaPk17ibibq1wXJHvdREvMjK9BtdzRHLtx81MXXRXSDWej4icz0RhrRlibw/640?wx_fmt=png)

```
a&a = aa|a = aa|b = ~(~a & ~b)a&b = ~(~a | ~b)b = ~a, c=~b  -->  c=aa-b = ~(~a+b)a^b = (a|b) & (~a | ~b)~(a^b) = (a & b) | (~a & ~b)
```

在eflags还原的DAG中，0xfffff7ea = ~0x815，还原后的eflags值分别与0x80和0x800进行and运算，0x80和0x800对应的是sf和of标志位。分别and运算后也会产生两个eflags值，对应的是第二个DAG图里的eflags10\_0和eflags12\_68。

```
令 y = (~(eflags10_0 ^ eflags12_68)  &  (~0xffffffbf))  >>  6
```

上面这个运算就是为了判断SF标志位是否等于OF标志位，如果等于则输出为1，否则为0。SF==OF刚好是jge指令的跳转条件，这里~0xffffffbf = 0x40是取zf标志位的值。

```
令 dword_ss[0xffffcf14] = 0xffffffff + y，y等于0或1则vmbytecode读取指针vm_ip = (dword_ss[0xffffcf14] & 0x43db9e) + (~dword_ss[0xffffcf14]  & 0x43dc22) + dword_ss[0xffffcfcc]
```

0x43dc22为满足跳转条件时的读取地址，否则为0x43db9e。这里加一个dword\_ss[0xffffcfcc]是为了重定位，如果程序加载的是默认基址的话dword\_ss[0xffffcfcc]为0。同理，vmp访问全局变量前也是要重定位处理。需要注意的是模拟执行的过程中出现的一些常量并不是固定的。比如0xffffffbf、0x815、0x80、0x800等，有时候会对这些常量取反。

接下来给出jl指令的DAG表示。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJ6QrFmQKo2icl3DrQoiaiawmoD41fX6wW0kgnCsosrxdeibrOia6A2vRkKyw/640?wx_fmt=png)
从上图可以看出jl指令和jge指令的区别在于下面的异或运算结果有没有取反，其它都差不多。

##

## **Jne和Je指令分析**

首先给出Jne指令的模拟执行的DAG表示。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJ53Au7QibPGqHYWJP9HicOecviakq7q8kEKYRGAEb3c7HUeUmoPnSoaulQ/640?wx_fmt=png)
jne指令和jge指令模拟执行的区别在于上图下面的异或运算被替换成了eflags的还原运算，直接获取ZF标志位进行判断，其它都差不多。而jne指令与je指令的区别在于eflags的还原运算后有没有取反。je指令模拟执行的DAG表示如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJC1jOTGVE6Nibhx5A5cbiaG6tZ28vZsS8P9Gibm117aFibe1GHOvUm7XLtA/640?wx_fmt=png)
从以上几个分支指令的DAG图可以看出vmp模拟执行分支指令的一些特征如下：
1、eflags寄存器的值参与了运算，正常编写程序几乎不会用到eflags寄存器。
2、模拟分支指令的过程中会用到一些常量，比如0xffffffbf、0x815、0x80、0x800等。
3、vm\_ip的两个跳转地址也参与了运算。

根据以上几个特征以及一些模拟运算的特征，可以判断vmp是否在模拟分支指令的执行。模拟过程中的常量比如0x40、0x800等可以确定可能使用了哪些分支指令，一般是两个相反跳转条件的分支指令。再根据eflags还原后的结果或者异或运算后的结果有没有取反来确定是哪一个分支指令。最后根据用于修改vm\_ip的两个目的地址中，有兄弟节点是取反运算的则为满足跳转条件的地址，比如je指令的DAG图里的0x40add8就是满足跳转条件的目的地址。

#

#

```
三

总结
```

根据分支指令确定各个执行路径，再利用这些路径的trace还原程序混淆前的CFG图，最后对CFG图进行全局优化达到虚拟化还原的目的是可行的。但是，这种方法会有一个路径爆炸问题。这里附上用于测试jge指令代码虚拟化混淆后还原的CFG图，由于没有做全局的赋值传播和公共子表达式删除，所以还原的代码还有些瑕疵。这次就不分享代码了，感兴趣的可以在之前分享的代码自行修改。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJQgehS4RQPYTNuegtib5DY7zSkvXzV5q8gTluu2jQOnevWlSeibOFtwWg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJa8rYPKEZ9N1u27QNk8E9PBfibBnZLdlpfYKyWkLIgIEWzossTeXXPnA/640?wx_fmt=png)

**看雪ID：会飞的鱼油**

https://bbs.pediy.com/user-home-742617.htm

\*本文由看雪论坛 会飞的鱼油 原创，转载请注明来自看雪社区

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FhH4xRicNVuXw6qEJQa2LD1GZazVvVXibY7PzVe7jGARu465cp2Ortb2QP77TzKHIhaq57ZmKKVREg/640?wx_fmt=png)

2.5折门票限时抢购![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UQQ68afWhJytuHspOcDRtNqnosZfRiaqD9E6ZQs5jaeMyw9vTrDd3DTA/640?wx_fmt=png)

峰会官网：https://meet.kanxue.com/kxmeet-6.htm

**#****往期推荐**

1.[进程 Dump & PE unpacking & IAT 修复 - Windows 篇](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473853&idx=2&sn=8fd4d2448cc087a58348422ec5c8e04b&chksm=b18e65f786f9ece1d9240bff1ebf9bc5bb25edabf0237ccfabe07642e94ea288b10c5f73b10d&scene=21#wechat_redirect)

2.[NtSocket的稳定实现，Client与Server的简单封装，以及SocketAsyncSelect的一种APC实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473852&idx=1&sn=7cc6b9eb080137f59729bfef67edfde0&chksm=b18e65f686f9ece0031c2554e0fc82a1714041c00c599e3f11975c7d6a6327117c16f454b5a9&scene=21#wechat_redirect)

3.[如何保护自己的代码？给自己的代码添加NoChange属性](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473851&idx=2&sn=c1abdc853c9f7cd53aa9e0f55809c0c6&chksm=b18e65f186f9ece7f00e8a39f9c371f457fd514ab11e468a9e53b01f29ee6a29448921a52739&scene=21#wechat_redirect)

4.[针对某会议软件，简单研究其CEF框架](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473847&idx=1&sn=ad73bc3a39d01fbdc0ef69f51e1f7606&chksm=b18e65fd86f9ecebedc7b8244af1252aebc923f97c01338211dc7a9ae52c5f212cab4ab1f467&scene=21#wechat_redirect)

5.[PE加载过程 FileBuffer-ImageBuffer](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473846&idx=2&sn=0258ae8d48a044dda44652e214c6c2b7&chksm=b18e65fc86f9ecea2bf2e6afa9ab5e0199da90be9f63e4c645ae8bd3628506b20907ec8fcaf7&scene=21#wechat_redirect)

6.[APT 双尾蝎样本分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458473839&idx=2&sn=650e486a3df2a44513f657c1c7779128&chksm=b18e65e586f9ecf3120b7cf8aa5125f68c10c15e6bbfd33b064622d1bcc41b91da0f881de828&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicd7icG69uHMQX9DaOnSPpTgamYf9cLw1XbJLEGr5Eic62BdV6TRKCjWVSQ/640?wx_fmt=gif)

点击“阅读原文”，了解更多！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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