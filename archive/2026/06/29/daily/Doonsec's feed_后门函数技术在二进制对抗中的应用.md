---
title: 后门函数技术在二进制对抗中的应用
url: https://mp.weixin.qq.com/s/YVBUPZEQGB-_I4COIrWYxw
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:14.365295
---

# 后门函数技术在二进制对抗中的应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeCbSUJ3ekiaO49s5ap23tY3RtKT0Iafrztu4MvnYaw5OxKHb1ermENnw/0?wx_fmt=jpeg)

# 后门函数技术在二进制对抗中的应用

Ba0
Ba0

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/TL4Y9UAcgrv4ib11v7vDSBJYcwqpJYQAEhc55bHr0HwZTvddqsoibgBc0kanr5JGUpZ0KkxNp1z0XL1VFeFux9mQ/640?wx_fmt=gif&from=appmsg)

**二进制后门**可以理解为：我们只需要修改某个字节或某个函数，就可以将加密的过程变成解密的过程，大大节省逆向成本。

本题先对内置的dll进行解密，然后调用其加密函数对我们的txt进行加密，如果我们将加密的函数nop为解密函数，就可以直接解密，类比与RC4动态解密技术。

**1、初次分析**

**0地址异常反调试**

本题的一大亮点就是有 访问0地址的异常反调试，小伙伴们在做的时候有没有发现调试异常艰难呢

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeSGKUvib5cVHI0NL2k0toNgV1KJNNsjxE6euriaNymyITxs1ov2r1Qic6Q/640?wx_fmt=other&from=appmsg "null")

故意访问0地址

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe4C6XIu2JEuuH0p3C6eb1olPvZtpLnjtHKZmYwcgVCv7vsIGoMknnWA/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXepmk9VwTuS5IwDgMxdibybic21DIian6ibo1zDJI7yTHp0KwpGWdOj8ylzw/640?wx_fmt=other&from=appmsg "null")

然后走作者自定义的处理函数，如果我们在IDA动调的时候不经过处理函数，程序就会卡在哪里不能继续运行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeayzK8dwS9x1lY0okGJKb9m43zWFEb42ptkC6ga0n5LhjRwoavAsQpg/640?wx_fmt=other&from=appmsg "null")

做法很简单：将访问0地址的代码和异常处理函数完全给nop掉

（说白了：就是将所有跟异常有关的汇编都给nop掉就完事）

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeMqCWH1M7moLKKN7TcyeI7q1EvibIdkDXPfL2lXbRicLW4FcNCWmXHZ2Q/640?wx_fmt=other&from=appmsg "null")

处理函数也是完整nop

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeOibJ48icNZmAicb0ib8s1SibqJevDOmJm62dribFt7nzcic6jc9DZJibLumXtQ/640?wx_fmt=other&from=appmsg "null")

返回处也nop，跟开头相对应

**main函数**

分析main函数，发现反编译爆红

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeo3SoUAV7yz5WtSGetN4cRBbacasXOTvHmPsZopUmmRt9BRDk9oGyiaQ/640?wx_fmt=other&from=appmsg "null")

很正常，查看汇编代码，发现了异常反调试和异常花指令干扰分析

做法很简单：直接nop即可

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeUo4NXJZL8HHbiaRIzxMFtq2pey13q4jp4x3ziaofvckYd6470QvMKhWg/640?wx_fmt=other&from=appmsg "null")

具体做法参考：上面一小节，0地址异常反调试

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe2cBBRCpptuibdP9HibaEK6h9A547L7CrPiaibLkq1WPcBib3ZgFdiazQ0PYA/640?wx_fmt=other&from=appmsg "null")

nop

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXex4rxgb37iaMiaOAITrDf7sCewFslv1nHJIibAMevCjerHDvrVvOqh0ibBQ/640?wx_fmt=other&from=appmsg "null")

成功生成函数

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe11oIPc9eHsvWo9pdrNfJRHTia7nJedMicrGaBgbApBZVZH1ibOTicchnKA/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeibOK0DsPic9I7ll7ft7PTEWaJ2NTugSLk4THNIpeicpTIrTf4SIYpfmicQ/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeZzzyLt4ficDhguOppMDhSY5TXDL5tsVhrC2v6eM1iaJFqj57cv47ylpw/640?wx_fmt=other&from=appmsg "null")

**TLS回调函数**

尝试运行，发现直接退出，发现了TLS反调试函数

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeC3KU2JNI8Y15ibayDianx6PZQkkK05S9HH6fQPtsribjUVaia7Yn3yu5QA/640?wx_fmt=other&from=appmsg "null")

nop即可

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeBYVV14ibDu5unEY8ntapibkibkNKZolXibRH82BRH1m3KqE1WFa7rBPwicw/640?wx_fmt=other&from=appmsg "null")

生成函数

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeSoh7E1E8tjttqmBrttkeCZ5mh6sKV2UWcz5MuFw9k2icymfh1GmBnqQ/640?wx_fmt=other&from=appmsg "null")

将exit函数nop掉即可，不用管反调试的事情了

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeoJFu7YZdib1bEfxoNpy9r2KEfouxgibZJRHJr43vibGicLkMh5wG89cia7g/640?wx_fmt=other&from=appmsg "null")

**2、内置DLL资源解密**

使用工具打开file\_encrypt

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeLcn8TBkboicQsnqricqYEEdcVpIEdcWHywMiaLEfKHFnNsGzaPlKMnKWg/640?wx_fmt=other&from=appmsg "null")

发现内置 pe程序，猜测key为0x33，解密

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeABAga9SbacCsATMIq76e2ZcIKTy4kViajjgr5Tm3P9xeGDjPfPT1Ipw/640?wx_fmt=other&from=appmsg "null")

这是程序使用0x33解密

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeFwmFfiae1172V9CdsicAlO5IDKKvnUiaLlPzpb2vDBeLN9prDylalZMHw/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeUutICysAumo21sCk9lIdQf5S3rUEhNlgNhxOBAudvfmibA5uI7ugYmA/640?wx_fmt=other&from=appmsg "null")

发现了很多加密函数和解密函数（Crypt开头），因此本题程序使用本dll进行加密和解密操作

在后面的分析中，也发现了函数加载了我们的dll

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeTfR23KXOGoxxicdh9dmKjgyVtStSl1V4abv9zN9a4AiaWhib7s82hlWxg/640?wx_fmt=other&from=appmsg "null")

**3、关键函数分析**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeZzzyLt4ficDhguOppMDhSY5TXDL5tsVhrC2v6eM1iaJFqj57cv47ylpw/640?wx_fmt=other&from=appmsg "null")

**sub\_401320**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe6xHMiaWgRUYNv2sEf5JsTgrIc0icvUmmlYjkaJibUBEvHfgbbpKMXRCLA/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXev2YpBRaVPVSJD1nSALTcBMEoDpF55fRic1d6OjfuW41LeVeCKqkyKvg/640?wx_fmt=other&from=appmsg "null")

使用IDA动调发现了很多bug，莫名其妙断下，改用x64dbg

**sub\_402000**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXejdAdNL4HmzsIAec5dm5I1S2l3uY2RKl7ARxvUyicVG3Hd4CknGGM3jQ/640?wx_fmt=other&from=appmsg "null")

路径和盘符有关，比如我在C盘

C:......\document\1.txt

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe9qOicoOjcDUfSo1rn1uAhL2q6pY5CmSHRgEhC6nsOiaCjne504XgvMTg/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe38aCoEuty6oU6pqpLon3pH8eribgJuVsib7tyLro0EQVs57gRiazvOWOw/640?wx_fmt=other&from=appmsg "null")

找到1.txt

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeQBUChCiawS9zPQibWGrb7Lu0Ew4h7WayGUUUn0OOHIPqRObfTw5kvaDQ/640?wx_fmt=other&from=appmsg "null")

**sub\_4017E0**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeNKBQC6qNkibBIET2icvsEEz0Zh1DOSolVSrCRBKm7Xva4Kviar7YervSw/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeFJ1tCC4q1gGSBbovdab2d719SsT2Qib7UxZn2PEcMJqZRI69rCWXlpw/640?wx_fmt=other&from=appmsg "null")

加载dll

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeVVOjWV9Hkv66U61uCc82hbPD5WibMHmibMicMOibMVewre2pK5P5pQpM0A/640?wx_fmt=other&from=appmsg "null")

**sub\_4013E0**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeiaPqNSkib0m6toTPXmQ7hF0R53JIbFcXBg5sG5HGylHlPKxjuITNVtKA/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeqxTf2DQ5lRebLhueXBofWFXeVZiaVj74pBC0TE7wSSaLqWp0pe6aBLw/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXe9ShPX4S5xz7aYmYJGxHjupYX7Uias5rvuibgL1u7aSy6sRc4dacWXuBw/640?wx_fmt=other&from=appmsg "null")

**4、解密**

既然使用了encrypto，那么我们改为decrypto就可以啦

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeXVWytiaCdp3MmJnsYOu8SlEz7J059SB87svt2C9kTICwOiaQRlEPwePA/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeNSUffnSZqnZGR1pHHRlZXxweX3IFsVxy51nhFxRamMZwPT0xcVxIkw/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeFxqcwHGASbGZGNbg2aicm6ez1eJ0HOfRbkiaC3wKxw1ia6WgGPzCNeClQ/640?wx_fmt=other&from=appmsg "null")

---

I added the missing CryptDecrypt call to the binary's import table and patched the executable to decrypt the files. The decryption call takes one parameter less than the encryption one, so I NOP'ed one push to the stack as well:

---

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fddLBN7dXC7XXeCWXt36zicuYia4KCZLCwdprkFR4CPTK8pxlDYSkwa8E7wajc77iaxMibBQ/640?wx_fmt=other&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgru97GQxia2fdd...