---
title: 一个简单的STM32固件分析
url: https://buaq.net/go-133327.html
source: unSafe.sh - 不安全
date: 2022-10-31
fetch_date: 2025-10-03T21:20:48.453891
---

# 一个简单的STM32固件分析

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

![](https://8aqnet.cdn.bcebos.com/131dd17910cf8cea11df6187d9c004dc.jpg)

一个简单的STM32固件分析

本文为看雪论坛精华文章看雪论坛作者ID：烧板侠看完论坛的 STM32固件逆向（https://bbs.pediy.com/thread-272811.htm）帖子后，又在评论区发现这个求助贴 stm3
*2022-10-30 18:5:4
Author: [mp.weixin.qq.com(查看原文)](/jump-133327.htm)
阅读量:42
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mEQ0MecmHK08NNlrjfAYUPQX1tKPCXkrQ7cdibWKPiakU6AkTlcJMxIlg/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：烧板侠

### 看完论坛的 STM32固件逆向（*https://bbs.pediy.com/thread-272811.htm*）帖子后，又在评论区发现这个求助贴 stm32芯片程序有xtea加密算法，但是数据排序的问题研究不明白（*https://bbs.pediy.com/thread-272872.htm*），于是想着分析分析练练手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m20bZXGCR5sa2WgqM3GBBh0ZzSWwQ7mD0zcuJqrRlALqLbe0qxU4cfA/640?wx_fmt=png)

根据求助贴内容，概括下有用的信息。

一个名为stm32f103RCT6.bin的固件，从固件名可以得知MCU型号为stm32f103RCT6。

MCU与设备A通信时用到了XTEA加密。

MCU注册时用到的密钥为 BA2F96A9。

MCU与设备A通信时的两个加密样例如下：

```
明文110 BE 62 F8 E8 DC 34 46密文18C 79 F5 D1 5E A9 46 2D 明文20E 77 50 C8 C6 27 E1 BF密文236 0A 1A 6E 6E FE F0 84
```

接下来目标就是根据上面信息，找到加密函数，还原加密过程。

**开始**

首先用IDA打开stm32f103RCT6.bin文件，选择ARM小端序，然OK进入即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mrTF6eVtruRLFnl7dGlVJ2Md5Ab1kvkSFtydDN46cMWribjHdjQcX3Ag/640?wx_fmt=png)

直接以Binary file打开，可以看到，IDA没有识别出任何函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mgiaBDqDEzTVJncUTBZ8krWJ5s3s9NzuopbFSicT4l91BrSd1k6bq1HsQ/640?wx_fmt=png)

习惯性的把前几个字节"D"三下，如下图，可以大胆的猜测加载基地址为0x8000000，事实上也确实如此，当然可以根据MCU型号stm32f103RCT6去查datasheet。不过更多确定基地址的方法请参考论坛的这个帖子 固件安全之加载地址分析（*https://bbs.pediy.com/thread-267719.htm*），里面详细介绍了多种方法来确定基地址，这里就不再赘述了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mlO9M4I9Lgf7Nk3ibT36DLC0m3lCthZZKmAGupqhNSZbB0NMtnGxcb1Q/640?wx_fmt=png)

Edit > Segments > Rebase program... 重设基地址为0x8000000，设置好基地址后，就已经往成功路上迈向一大步了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mZUL4FEr1ElCEKT13Y7TAuOjLn41diauVbYGzBmnLr98SlS1j9ia68Cwg/640?wx_fmt=png)

接下来，Alt + L从前面几个地址之后开始选择，一直到末尾，右键选择"Analyze selected area"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6msE4STtOUXnns753mSSqrKD6Qvia9aTq7wfwMHHBZShua5ptMqYSXpsg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m7CXXu5GOWib9qvEfED4joIKXyfFnRibDUmmAwaHaA8sS75vMNDicVwvug/640?wx_fmt=png)

出现下面提示框，选择Analyze，然后静待IDA分析过程结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mNUtYGqiaD8YlowicONzLyLDPmoEvfKibhoedcu6AgHh39n6m35mKmpwHg/640?wx_fmt=png)

这时候，可以看到，IDA已经识别出许多函数了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6miap1LUfWhGgf8YYyATLTicEnHgtCFCiaiaYUGbbzltrHxVoRqnmQicAvSAQ/640?wx_fmt=png)

接下来使用Findcrypt插件搜索加密常量，看看有没有什么发现，Search > Find crypto constants，如下图，可以看到，有个TEA的delta加密常量，这正好对应前面提到的MCU通信时使用了XTEA加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mUAjHiblxhpKdhbHVAsw0hzLr11ibNiatXWxDAKR1E6CUh5ZO1MU0ibqicqQ/640?wx_fmt=png)

跟踪查看引用该常量的sub\_800E288函数，F5结果如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mBp2n5hS2via8QraqaoiaztZkne8nTgwFFfPznYL6EJzNdlPrRgIRENIg/640?wx_fmt=png)

对比网上的XTEA加密C代码，可以知道，sub\_800E288函数的参数从左到右为，加密密钥、加密输入、加密输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m8oCGlUicFHELjueK3qibbppH3aIzEzNhYAX249K4RSGfjszI8tSFsXuQ/640?wx_fmt=png)

对照上面XTEA加密C代码，就可以对一些变量重命名了，如下图所示，可以看到，加密时的密钥输入并不直接作为XTEA加密的密钥，而是经过了一些运算进行了变换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mcP4fpiczouFG20LY0nyEPUlO1jGmXPEndicRSibhcySETibqkBwMXWjZ9w/640?wx_fmt=png)

接下来详细分析加密过程，首先时最前面的这部分，存在大量的 左移24、左移16和左移8，熟悉的朋友可能很快就反应过来，这个是大小端转换。所谓大小端指的是"大端序"（BigEndian）和"小端序"（LittleEndian）。用一句话来说"大端序"就是高位在前，低位在后，"小端序"就是低位在前，高位在后。举个简单例子对于同一个4字节的byte数组"12 34 56 78"，在大端序里面把它当成4字节的int的话它就是0x12345678，而在小端序里面把它当成4字节的int的话它就是0x78563412了。下面的"<<24 <<16 <<8"作用就是用来将4个byte的数组转为大端序的整数（MCU是小端序的，直接用\*(int \*)类型强转的话得到的结果就是一个小端序的int）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6micjWwicmqyHNEegzQBqUZugrE49VSksPnpYwt6Pg7ibAQkJ4KQHyTFdfw/640?wx_fmt=png)

忽略左移24、左移16和左移8这些端序转换的部分，我们能发现，其实对于输入in在正式XTEA加密前没有做任何特殊处理，而对于密钥的每一个字节则与一些常量进行了异或处理。同样地，看到"0x66、0x6F ..."，这些值，熟悉的情况下，很容易反应过来，这些可能是ASCII码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6micjWwicmqyHNEegzQBqUZugrE49VSksPnpYwt6Pg7ibAQkJ4KQHyTFdfw/640?wx_fmt=png)

TAB键切换查看反汇编代码，如下图，可以看到这些常量都是基于地址0x8030A30开始的偏移量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6miaWFyGHUv33Wjun7ckhqiamonV0UdmzH5Ixw4St5DDmvicturuLlwtmhg/640?wx_fmt=png)

查看0x8030A30地址，"A"一下，可以得到一个字符串，如下图所示，看得出来这是个有故事的字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6m6F0h2HphSUAdWmaIfZONvQYbJsp7LSrAmvxA8DOaMwGQyJ7S6c2Zjw/640?wx_fmt=png)

回到反编译代码窗口，重新F5一下，可以看到，反编译代码更清晰明了了，密钥在用于XTEA加密之前，每个字节会与上面的字符串相对应的字节进行异或处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mZlVJuTwIw00yR9OFHnyMR8vrjk6uukXBSlrFLECSkjSsyszIEYWnzA/640?wx_fmt=png)

再来看后面这部分，如下图，后面的其实就是标准XTEA加密，只不过对于加密结果的输出，同样有大小端的转换，"HIBYTE(x) BYTE2(x) BYTE1(x)"与上面的"<<24 <<16 <<8"一样，常见于数据大小端转换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mX3nDxcQ2cGPNriczicMjic8CXictvXXXeJw2jqUKFZaeZGSl8q0CibFu4ww/640?wx_fmt=png)

到这里就结束了吗？- 答案是还没有，求助贴里面提到的MCU注册密钥是"BA2F96A9"，只有4个字节大小的密钥，但是这个加密函数的密钥输入却有16个字节，所以从MCU注册密钥"BA2F96A9"到加密密钥userKey中间还有一些过程需要去分析。

对 sub\_800E288 "X"一下，查看sub\_800E288函数的交叉引用，如下图，可以看到只有一处调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mUZG2xK5O2tfBcFJlRQLxQAzKxSWqT2SIH70o95Bn4kyBsLib8vq9BrA/640?wx_fmt=png)

查看该调用，如下图，可以看到第一个参数加密密钥是以地址0x20000104传入的，所以加密密钥就储存在0x20000104地址处，接下来只要查看哪些函数有往0x20000104地址写数据，即可找到密钥变换的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mRFib6RiaIKCCoiaQGeMu2EPicRlz8ib4G4f9TkdJCK9X1zs4XrYEJ65cgibw/640?wx_fmt=png)

接下来Text Serach搜索0x20000104，看哪些函数使用了0x20000104地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mP11IjicdG7m0ulTugTbogAmKse3G9PIc4yPMBATY8bnVPhg0KyQLl1w/640?wx_fmt=png)

如下图，搜索的结果并不多，挨个查看后，可以看到只有sub\_800F3C8函数中有往0x20000104地址写数据的代码，而且sub\_800F3C8函数参数为unsigned int类型（刚好是4个字节大小），所以基本上可以确定这个函数就是MCU注册时的密钥变换为加密密钥的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mia7vnY1fTkpYaVxKOp4tS364v4xaiahAiaEpVZT0Q5pSeCBSAlyrMicQfA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EIYibYYZeLWTNdZPWX6Ot6mmokhPGSFvRWun1laP8ESvFiaVSFZYT9NCO0CjnNCtF8oSXW8r2yicTWw/640?wx_fmt=png)

接下来将sub\_800F3C8和sub\_800E288这两个函数反编译伪代码提取出来，用VS Code简单写个程序验证下，代码如下：

```
#include <stdio.h>#include "defs.h"void keyExpand(unsigned int key, _BYTE *outKey);void XTEA(_BYTE *userkey, _BYTE *in, _BYTE *out); void keyExpand(unsigned int key, _BYTE *outKey){  int i; // r0   for ( i = 0; i < 16; i = (i + 1) )    *(i + outKey) = key >> (8 * (3 - i % 4));} void XTEA(_BYTE *userkey, _BYTE *in, _BYTE *out){  unsigned int v3; // r3  unsigned int v4; // r4  unsigned int v5; // r5  unsigned int i; // r6  int v7[4]; // [sp+0h] [bp-34h]  unsigned int v8; // [sp+10h] [bp-24h]  unsigned int v9; // [sp+14h] [bp-20h]   char aStefanlovesmay[] = "StefanLovesMaya!";   if ( userkey !=0  && in!=0 && out!=0 )  {    v8 = (*in << 24) + (in[1] << 16) + (in[2] << 8) + in[3];    v9 = (in[4] << 24) + (in[5] << 16) + (in[6] << 8) + in[7];    v7[0] = (userkey[3] ^ aStefanlovesmay[3])          + ((*userkey ^ aStefanlovesmay[0]) << 24)          + ((userkey[1] ^ aStefanlovesmay[1]) << 16)          + ((userkey[2] ^ aStefanlovesmay[2]) << 8);    v7[1] = (userkey[7] ^ aStefanlovesmay[7])          + ((userkey[4] ^ aStefanlovesmay[4]) << 24)          + ((userkey[5] ^ aStefanlovesmay[5]) << 16)         ...