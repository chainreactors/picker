---
title: 记一次挖矿木马样本分析
url: https://mp.weixin.qq.com/s/NtFXOYRJfOUjwrFctk1aHA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:02:58.245315
---

# 记一次挖矿木马样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lFfjZayicKlHcmtmOM4HpElEtW19mrOSrQNibUjGovD4DIZC9TnBE6827KwpRSLmicn6oL93d11trRQweVU1dK7pw1sDtonDY73zLtGGH8Mlib0/0?wx_fmt=jpeg)

# 记一次挖矿木马样本分析

原创

培根
培根

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 有一台vps被弱口令上马了
>
> 翻来翻去
>
> 找到个二进制文件如下

### 前言

![Untitled](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlEUR1JzJicjcRPlce11DqH1mzSfJn0F6FpCu9YqJcpiaak2LMj6RpfibcRFDZ1Zvbcoog0CwTkrLiaNK96k8zbFZk3Q5VwOqDu19YY/640?wx_fmt=png&from=appmsg "null")

搜main函数关键字可以判断是用shc加密shell脚本生成的二进制文件

![Untitled](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGylbYCfGxO0N6YDtuCjaOx3Ttvk9KHY6w8DBW6aa40cu4EVLBcT4MpJCa9AcySjyt4TK90wULQ7ibr8N1VlDEVKFBHsowdQticQ/640?wx_fmt=png&from=appmsg "null")![Untitled](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlFhCLCcm4KNCCibqvBdjBxFdYWBDoRrj0vibIsxkTkkDqNjZIsbvJR7Wb03Dzwib9UlwVjjpzMJ9yCdlYV5Eg83VcAIWpCK8x6H9I/640?wx_fmt=png&from=appmsg "null")

在0000000000400F7E位置函数，找到了加载shell命令的位置

![image-20240108211127374](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlEl0YA9cygWM2JwyYYSUI3Lbp6Y0p8a092dl9UJwLXqIH9G4nfcUu3cujA7tHcibokyP3Q2SQkvdsEqYFlx1yMwrJhM6tdAYxDc/640?wx_fmt=png&from=appmsg "null")

shc部分源码

```
/* shc.c */

/**
 * This software contains an ad hoc version of the 'Alleged RC4' algorithm,
 * which was anonymously posted on sci.crypt news by cypherpunks on Sep 1994.
 *
 * My implementation is a complete rewrite of the one found in
 * an unknown-copyright (283 characters) version picked up from:
 *    From: allen@gateway.grumman.com (John L. Allen)
 *    Newsgroups: comp.lang.c
 *    Subject: Shrink this C code for fame and fun
 *    Date: 21 May 1996 10:49:37 -0400
 * And it is licensed also under GPL.
 *
 *That's where I got it, now I am going to do some work on it
 *It will reside here: http://github.com/neurobin/shc
 */

staticconstchar my_name[] = "shc";
staticconstchar version[] = "Version 4.0.3";
staticconstchar subject[] = "Generic Shell Script Compiler";
staticconstchar cpright[] = "GNU GPL Version 3";
staticconststruct {constchar * f, * s, * e; }
    provider = { "Md Jahidul", "Hamid", "<jahidulhamid@yahoo.com>" };
```

尝试生成一个echo “helloworld”，看看shc生成的文件是什么构造

### shc

安装shc

```
sudo add-apt-repository ppa:neurobin/ppa
sudo apt-get update
sudo apt-get install shc
```

加密后会得到一份生成的c源码和可执行文件

```
[04:08:08] ctfshow@ubuntu /home/ctfshow/Desktop/test (0)
> shc -f ./test.sh
[04:08:11] ctfshow@ubuntu /home/ctfshow/Desktop/test (0)
> ls
test.sh  test.sh.x*  test.sh.x.c
[04:08:12] ctfshow@ubuntu /home/ctfshow/Desktop/test (0)
> ./test.sh.x
hello
```

会输出一个test.sh.c和编译好的test.sh.x

---

那么可以照着test.sh.c的源码来快速分析手上的二进制文件

调试发现ret会记录当前进程是否为父进程，

调试发现如果为父进程，则执行的命令是

```
exec bash ./<程序自己>
```

那么相当于把代码在子进程里面又跑了一遍

这个时候ret就是1了，加载的也会是text里面真正的代码段

![image-20240108211037704](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlHkXprqyhkO8E7ia3MDictcK3Ybf4DWEAa2F9rY2uu5J64wib6I1suyrrvFicCT0HnOeA41SibNmglX67fN65QBY8LDSgSD44NDQhgY/640?wx_fmt=png&from=appmsg "null")

### 思路

程序把shell命令用rc4加密在了硬编码里面，回到样本，只要更改ret的值然后调到execvp 然后print mem就能得到shell脚本了

### patch && dump mem

修改ret值

![Untitled](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGRTyHVQFVQpR4mKYicChiblZvrwASz6ouycCLmsFtPLMEfd9icEyR1YiaW4xkz4XD3RFJyzUicjxPE5a0J04oLGksuLtFEoxy8zuX0/640?wx_fmt=png&from=appmsg "null")

在memcpy下断

![image-20240108215950966](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGuoibyYFKJqHaMgZeUxAoRNVPyx7YbVj5uHujMpUXuVrGpQljMPV8eOLiabiczuUbf2wtvo7VhnqEXaFnukNHUgpJAViceUbiaXZIg/640?wx_fmt=png&from=appmsg "null")![Untitled](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlFfOr7tRTgtNuC8oP8oexlIR9uplTbjxLfa1TqK0btCAmrZI4DlS6JNZqmRFcia9uTo78U3GCxsHMfFfViaqP6xAt3eupTXEohms/640?wx_fmt=png&from=appmsg "null")

祖传字符串脚本

```
base  =0x000000000602B83
end = 0x00000000006074F0

ans=[]

for i in range(base,end):
    tmp = idc.get_wide_byte(i)
    ans.append(tmp)
    if(tmp == 0):
        print(bytes(ans))
        ans=[]
```

![Untitled](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlFBreicia9FrCHuOxoWA0x3J5miaChGZoGiaaboYH7ZGQxiadiacc3HFNTvFh6I3d1ck8eiaMYf6Wc4r3fmRiahfep6bqdj0qrZE1rXNds/640?wx_fmt=png&from=appmsg "null")

```
shlll = b''

with open("sh.tmp", "w") as f:
    print(shlll.decode(),file=f)
```

暂且写个脚本存一下

### shell分析

到这一步就比较明了了

shell脚本里面存的命令全是用明文显示的

![image-20240108220142481](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGNqFVJXSoeSHNpFa4AS8UT5xsNLGVYCRRcEoTcxoicZCElQxcjBjecfuKCUtRARo4Ic6wicHnmV3Xg8hTQo2ic0fjmulJVyLevKE/640?wx_fmt=png&from=appmsg "null")

首先是删除日志和竞品矿机，然后设置iptable

释放iptable\_reject

然后从远程服务器下载矿机

![image-20240108220528535](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlFfGt33HiclZU1Fgn7Rg9aSpz7DRnhTjondOctEF02hnibibKOFkUE4Gd22OUic8YvPshxarHeTLibib45gOOsZOian0KN4Mr9UibYs750/640?wx_fmt=png&from=appmsg "null")

其中一个ip是172.104.170.240

上网搜一下ip是一个矿池

![Untitled](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlFGCST2nEFchIbTvtN86fKntowRiconoeV5fOgh2QAeVJD2nWn88VLU0DNbicZRmNWf9nxUrIsKOrhwzabA9OGZ3ibb0SMLYRlx9Q/640?wx_fmt=png&from=appmsg "null")

搜索矿池ip发现样本行为和安天于今年5月发布的yayayaminer有一定相似之处，在初期的排查阶段借鉴了其思路

https://www.freebuf.com/articles/network/366444.html

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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