---
title: 通过ELF函数劫持，理解Linux系统的动态链接生命周期
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458583804&idx=2&sn=9d6fcf4f12a36e923959b3260a2bbe60&chksm=b18c327686fbbb608acc4091877081eeab84712b38ab710ec75ff6a222a05a878fd17e648ddf&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-26
fetch_date: 2025-10-06T19:20:07.922297
---

# 通过ELF函数劫持，理解Linux系统的动态链接生命周期

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8ibuxfGF1AObOb8hPheSuMku7LSIibDHyzFLZOzBEWGewicZDwIOGj1aEA/0?wx_fmt=jpeg)

# 通过ELF函数劫持，理解Linux系统的动态链接生命周期

magicsong

看雪学苑

**01**

**ELF 动态链接过程**

Linux 系统中的动态链接虽然是一个基础话题，近二十年来有许多书籍和文章讨论，但是很多内容较为繁杂。本次，我们以一个案例来说明动态链接和寻址过程，贯穿动态链接的主要生命周期，从一个不一样的视角，带你入门二进制 Patch、ELF 感染，深入体验 ELF 的动态链接过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ85iaRNqRkXcxfrBTdMjR4YeSMlyN4c3WvrjrhtwlooUXFnhTynYZGJzQ/640?wx_fmt=png&from=appmsg)

可执行文件`hello`调用动态库`myfun.so`函数。编译阶段，链接器将`myfun.so`写入到`hello`的 .`dynamic`节，运行阶段，链接器`ld.so`就会装载`myfun.so`，遍历`.rela.plt`节中的重定位符号，填充对应的`.got.plt`节的实际符号地址。这样`hello`在运行时，就能跳转到对应函数的真实地址。整个动态链接生命周期如下所示，结合后文内容，你就能明白动态链接的符号如何实现定位功能。

### 动态共享库

编写共享库函数`myfun.c`

```
#include <stdio.h>
#include "myfun.h"
void func1() {
    printf("Hello, this is func1.\n");
}
void func2() {
    printf("Hello, this is func2.\n");
}
```

相应的头文件`myfun.h`

```
void func1();
void func2();
```

编译为动态共享库

```
gcc myfun.c -shared -o myfun.so
```

### 主程序

主程序代码`hello.c`调用动态库的`func1`

```
#include <stdio.h>
#include "myfun.h"

void main() {
    func1();
    getchar();
}
```

编译可执行程序

```
gcc hello.c myfun.so -o hello
```

上面的程序很简单，我们从整个 ELF 文件动态链接生命周期的每个阶段尝试通过函数劫持的方式，使得原本调用`getchar()`改为调用`func1`或者`func2`。

> 将恶意代码插入到 ELF 二进制文件，通常被称为 “ELF 二进制文件感染”。高质量的 ELF 二进制文件感染通常涉及使用特定的感染算法，这些算法针对 ELF 文件的不同用例。

通过了解动态链接过程，有助于后续将函数流劫持到我们注入的恶意代码，更好的实现感染效果。本次主要跟大家分享一下，如何通过动态链接生命周期中的每个阶段，改变程序执行流。

**02**

**.text 代码跳转修补**

使用 IDA 反编译 hello

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8nH7vPVdGVzL3ozyvGYoKueoRc9ibpyiadiaHRslBRg6cqPdGRSCTPW4zA/640?wx_fmt=png&from=appmsg)

IDA 反汇编窗口识别到的汇编指令是已经优化过的，事实上操作系统并不直接感知函数跳转的符号，对于系统来说，只有地址才是真实的。这一点，可以从`call _getchar`原始指令看出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8wKibUxfdYic6NhnRY3qUysqh4Pk9lEfaDxlPP0moAx0MBbHsSaQ8qIUg/640?wx_fmt=png&from=appmsg)

call 操作数是一个偏移地址，**跳转地址 = 当前指令地址 + 偏移地址**。ReverseWidget 的反汇编引擎 Capstone 也进行了优化，当我们设置好当前指令的地址，就可以直接得出`call`指令的跳转地址。`0X1040`指向`.plt`节的代码。因此，如果要将`call _getchar`改为`call _func1`，需要将`call 0x1040`改为`0x1030`，也就是将`e4`改为`d4`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8ibL8fAE46Diax2mIibZHpibUVdyKU3BrQ89msMvP754iabSZxDWkpicUCH2g/640?wx_fmt=png&from=appmsg)

IDA Patch 以后，执行`hello`，发现原本不打印的`getchar`已被改为`func1`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8A5PPlYPkrfibXES1DR50Xpohevtib2b6LichEcrkI8YQHps3VW8EwR8Ew/640?wx_fmt=png&from=appmsg)

**03**

**.plt 代码跳转修补**

.plt 也是一段代码，但是使用的是`jump`而非`call`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8EO0awiarvzHbg86VxrS9FoyvpoviagJ9nZNiaywxbRNuWFSD9loiaGuHXw/640?wx_fmt=png&from=appmsg)

这时候，Capstone 似乎并不能直接算出跳转地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8TgOJZk7fObRGqfYkewn9iaPXMdukRoAz72wQWiciby9rR3exOeq2SXTOw/640?wx_fmt=png&from=appmsg)

**跳转地址 = 当前 DIP + 偏移地址**（当前指令的下一条指令地址）

```
hex(0x1046 + 0x2fc2) = 0x4008
```

分析得出，`.plt`跳转到`.got.plt`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8j3ctBCpZyG5HUXklBK82JgBd1WRKLo9awKL3VRzb0x1qn5AtKBEibag/640?wx_fmt=png&from=appmsg)

因此，如果要将`call _getchar`改为`call _func1`，需要将`.plt`跳转到`got`表中的`func1`。仍然使用 IDA Patch

```
hex(0x4000 - 0x1046) = 0x2fba
```

也就是将`c2`改为`ba`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8s29AFXLJibJbWac9HQc6X3Dw5atNYCOzDKqSiaaCVxkCPZVAmpysjsaA/640?wx_fmt=png&from=appmsg)

执行`hello`，`getchar`已被修改为`func1`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8A5PPlYPkrfibXES1DR50Xpohevtib2b6LichEcrkI8YQHps3VW8EwR8Ew/640?wx_fmt=png&from=appmsg)

**03**

**.pot.glt 劫持**

CTF 比赛中描述的`got`表劫持，通常指的就是`.got.plt`节中的函数指针，是缓冲区溢出常见的漏洞利用方式，也被称为`ret2got`。这是一种动态行为，动态链接器会在每次加载 so 时，将`.got.plt`地址修改为真实的外部函数地址，这就是所谓的**重定位**（延迟绑定）。ELF Patch 或者说感染，是在程序运行前，是一种静态行为，这不同于漏洞利用中的动态行为。因此，如果只是静态修改地址，是无法实现函数劫持的。

**04**

**.rela.plt 感染**

那么 .got.plt 存放的地址指针如何重定位？这是由 GNU libc 动态链接器/加载器`ld.so`在 ELF 文件加载到进程空间以后，程序运行之前完成的。动态链接器遍历`.rela.plt`节，完成函数地址的重定位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8f8BrHMSTJj9y2pOfibswvnW3Htic6Cx54Sa8MK5D6jIXpHU5ETlGkN9w/640?wx_fmt=png&from=appmsg)

在此节中，可以直接修改符号下标，实现函数替换。

```
┌──(kali㉿kali)-[~/elf]
└─$ elfspirit edit -R -n .rela.plt -i1 -j3 -m1 hello
0x4->0x1
```

此时我们发现重定位节的符号下标已被成功修改

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8p0BXerCHrdhribGTJ9YUlMApcJMicia755sURJk5LMnMtHy1RnPdHhWBQ/640?wx_fmt=png&from=appmsg)

**05**

**.dynsym 感染**

`.rela.plt`节表示了需要重定位的符号，该节中的`Info`成员高 8 位，表示在`.dynsym`动态符号表的下标，从而定位到我们在 IDA  看到的符号`getchar`，这就是一个完整的重定位符号流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8ia8RuYc3UrxWNQu2ZjxLWHyOibhZg0YaS30eIYc9exrUvvMTT02ypAiaQ/640?wx_fmt=png&from=appmsg)

因此，如果要将`call _getchar`改为`call _func2`，需要将动态符号表`getchar`改为`func2`

```
┌──(kali㉿kali)-[~/elf]
└─$ elfspirit edit -D -i4 -j6 -f func2 hello
getchar->func2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8c7lKZfomEgPr0oyMqibicovTQp4xV6TkicTcDgBoayPtmSqhRGLVibP8ibw/640?wx_fmt=png&from=appmsg)

结果显示，函数`getchar`已被劫持为`func2`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8Ge1tqExS0jibs35tk7doaDsAKeQfdOIjn8WW51gLn5ibllshaGczqP8A/640?wx_fmt=png&from=appmsg)

除上述方法以外，还可以修改`myfun.so`的动态符号表，达到相同的函数劫持效果。

◆在`hello`二进制中，引用的外部函数，统称为导入函数。

◆相应的，在`myfun.so`中，提供给外部调用方的函数，统称为导出函数。

**06**

**总结**

如今的 Linux 二进制世界，动态链接随处可见，理解了动态链接的过程，也就理解了函数的执行流，控制执行流是漏洞利用必不可少的一环。通过上述实际案例有助于我们更好的理解一个二进制如何找到外部符号的地址，也能告诉我们，可以在动态链接生命周期的任何一环实现函数劫持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8cjqagvia1QEiaK1arwX0233qZ6A5FYkV4dh5qbZ5aKKGAFNAgA5JPz4A/640?wx_fmt=png&from=appmsg)

看雪ID：magicsong

*https://bbs.kanxue.com/user-home-834205.htm*

\*本文为看雪论坛优秀文章，由 magicsong 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=21#wechat_redirect)

4、[关于安卓注入几种方式的讨论，开源注入模块实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579138&idx=1&sn=fef09513ae9f594e68a503f69a312f4f&chksm=b18dc04886fa495e440990cd2dbddb24693452562e53bd8cb565063ddee921b7e288477f4eea&scene=21#wechat_redirect)

5、[2024年KCTF水泊梁山-反混淆](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579017&idx=2&sn=a97dacde8a6c913108999da8a96a667f&chksm=b18dc0c386fa49d57ce9f0ce6923690d6eb8efb3ccb8032e8c6b923184af3dd29b1b4471f9a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8XyHmwsvpaVnOstLdm642KFGaDMT1ct5EYlrj1DRiaWd6XvibLZysaJ0Q/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG...