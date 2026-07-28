---
title: 2026黄鹤杯网络安全人才创新大赛学生组（Misc部分）
url: https://mp.weixin.qq.com/s/HEDRih5xoCFJtxCi2AAK8g
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:55:07.912715
---

# 2026黄鹤杯网络安全人才创新大赛学生组（Misc部分）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBiabxMf0ll26rBB7RX7CRUicJ6GicTibyK2YicFWbB04soSia9SiaY5PwJnXTdBqfelUAC3a8aB9e4niciaTQTByK0ZiaBbmljra8gseq9eg/0?wx_fmt=jpeg)

# 2026黄鹤杯网络安全人才创新大赛学生组（Misc部分）

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于玫家大院
，作者玫幽倩

![](https://wx.qlogo.cn/mmhead/sc8lJYpicUaWe4sDb1V43WuBUWZ0qR9taqbprebuQQgm7KqcuLHn9KvCrh8JtkISVnFMib07gRibM4/0)

**玫家大院**
.

希望我们所有人都越来越好，博客更新更快https://mei-you-qian.github.io/，合作私聊s2764174229

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaynsGiaOJf6bf5CyBXyS0X4dR8HyQ0Pjr6Q3iaJxTI3EXfDUrM9IZN44000ibeYxk2OUz6sGX8jy0ichgdibDvhBOOictL61T0dDyZM/640?wx_fmt=png&from=appmsg "null")

刚刚比完不久，本来想着出个misc全，但是有最后有一道一解的misc还是做不太出，好久没发了先水一篇好了

所以本文只有潮痕留声和失序货栈，纯水（）

## Misc

### 潮痕留声-HHB2026

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjoUNibcDNmaTeCEoFjyFdveU9Ma4QmeJMVwVER8XEECYDib3YHzGNxss0uPwrYOhZnmce52IrYlb66u64VoGFJpbczPQ3GuvDiac/640?wx_fmt=png&from=appmsg "null")

首先是潮痕留声，好久没有手搓了，这一次手搓了一道还是蛮开心的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgY6SU1r3VX3MWfga8oheyOxVic0bRxObvBkcbByODjUrgIZyibiaQQgStNCI8Rov2oLTeHu3VZmibria1IkR40grFNWKWbhOpOklQM/640?wx_fmt=png&from=appmsg "null")

打开附件，发现只有一个data.png

拿到png先看看十六进制

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBj2fQgTicDrNJic60s76DbpS4fQmVBxAhMGc5eVGULsUx0vcFdb1t6QzU17Ac9vrHLTXvNlNushKXEpcrBAFttgDEuZ7QNj0Q4cs/640?wx_fmt=png&from=appmsg "null")

我们追踪png的文件尾AE 42 60 82，发现文件后冗余大量的信息

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgfrlgTYlVKoXjD6ia8L0rlrJX10efcURLQc2oOjCsYf6ST5gQhR4aKU56lXsQ2ylMpXS4RKHSUSXXExht9CBjVfyFtUKBl5ADc/640?wx_fmt=png&from=appmsg "null")

对冗余信息进行信息探查，发现了十六进制末尾写的是4030B405

倒转一下正好就是0x504B0304，即zip压缩包的开始标志

想到题目可能是将压缩包的十六进制倒转后拼接在了png文件之后，我们提取一下，再倒转回去即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh8EicoYdhxKjJibmOdbOwGYAN5YWbXMOYunonCBxOTUCC8uy7dYgPBaXw6slbvWjo76bWWAkVA5tBwA4PsiaXJG1XpAvrwAQI2n0/640?wx_fmt=png&from=appmsg "null")

利用cyberchef进行reverse即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiasQajgU3ibqibsckMvPZkXvm7eovlIC5uevOkhyGiciazS4odakicblBAaNNuYIvxSB88oIfuu5Q8GfwqTXhHMxdS43ZIhKpxdVFy8/640?wx_fmt=png&from=appmsg "null")

下载后发现是一个加密的压缩包

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgKBWF4BQecGhia8sRhANxkXCpn5XxiabyFZ7jrxmTPnE7ib2kruDKmvmib4twycHOMOI8ML5rh5WIXjzAFjg2Un29eNy4QSZ9VBeE/640?wx_fmt=png&from=appmsg "null")

这个加密方法可以排除是明文爆破的可能了，伪加密发现也不是

继续探查信息

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgiaJBib4WPgfb8YexiaC7DficIvTKOibraoyPAEXGpjhjsic1vVhJKdGkLO9KzAZwQyWXHKrQr3Aeic9Korr0zrFxNZy4bYu5ZOGOBAY/640?wx_fmt=png&from=appmsg "null")

查看属性发现明显提示2026\_????\_CHB，形似掩码

于是想到本题可能考察我们的是压缩包的掩码爆破

这边可以用工具，也可以用脚本，相对来说还是工具会快一些

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhXSicRSTq4gfiatiaNPZIlNyDe1km7tRKDvTuYZMp1WFibmNu82yEEmO1IsDZ23HddjaxKia6nL3ibNnCRrUGTLVOhGicWMmIoAzXEnM/640?wx_fmt=png&from=appmsg "null")

直接选择掩码爆破，写好掩码即可，除了ARCHPR，passware kit等工具，或是python脚本等等均可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhzuGSZbhKfCOBTbia89porFeozavcWTAu2viccibbCz2x7eaDq30GEiciaRmrNiba53sfZygibofWKddjdw8GdpDeEGEJlX7nTn6Xqgo/640?wx_fmt=png&from=appmsg "null")

进行爆破，很容易得到压缩包密码为2026\_D4fX\_CHB

得到新图片tide\_trace.png

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgcicZ4n9kj0RCEBb647kaAW3tmvkUQsic3TylT8KTWOEdsoe2ka352krXeG2gic8Vm31YyuVUgTqyb4WUSibCIbveElyAKLr8uhibI/640?wx_fmt=png&from=appmsg "null")

又是一张png文件，继续查看十六进制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhXceyRzp3SzogCZ3KI8UIsNcqp2ezAzvaDdibUf4icVHry8mNehFSGica30BEYia4F3icGc64GoFYM2vjeyWVHZgicCg7AU5ichhL7VM/640?wx_fmt=png&from=appmsg "null")

发现在文件尾后依旧藏有信息，且看文件头可以发现是一个多媒体文件

我们直接利用Foremost进行提取，得到了一个音频文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiacIicR87ceda5S0se8A0XbrEqECzw7NMNIRt1eETa2RaXTDibtwxGXyWPEBYBO5Vq6gkBPlHIfrssId0H3O4ZAvbSkVZlRuf7cg/640?wx_fmt=png&from=appmsg "null")

直接听没有什么信息，怀疑音频隐写，放入Audacity进行查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgGrbNLgQzCWCTF1VTfuKD7OAiaMNm444PnX50t6JPIm0ShPiajdftEwvNFVGHJQSAsUuuZLwQ9TWMtgaWQB5eZudOTCdQVtzibNU/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgq7ibNTYRftdJxdmR997b2zV33pYfD5HflCH3MMtLdOxKezYg1vLjT5wVM34bUH3DAvB6VH82qXH2CJLG5pibJMxOztodLY6icWY/640?wx_fmt=png&from=appmsg "null")

右键选择查看频谱图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhNOXVhAqnhSibXpohnX3h0C4dTtHwfEyNSBmhoKMmD4rratKeMCia0ib4gDVMCymSqficP0f180aSIRzt8pEampETy00Dna198Kl8/640?wx_fmt=png&from=appmsg "null")

明显藏有明文，进行处理

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgnr3xPHGGOeGf1dshvhDeNiaReGk68wb23oiaxQq1ZBzoicSRUMUTMMSuewenKsacAgJID6dvMokmMJxXsvr9V2c4uSNyIC9GsXw/640?wx_fmt=png&from=appmsg "null")

简单拉伸一下，发现是上下、左右都进行了翻转（看这个4最明显），我们手动反转回来

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YdkQKXYKSBgRP2NbMIemoy1Qq6CSgwP1KrWxvvib1M1EicOCCKBJuKsDA3alsltYicJDEQficfiaNVXIIVBfj3kgEaUVwPGpP6YU0BXjAq72kGsQ/640?wx_fmt=jpeg&from=appmsg "null")

现在我们得到了一个很类似flag的文件，但是不知道这个六乘六的矩阵如何处理，不知道flag是如何阅读的

回到原来解压出的tide\_trace.png，题目提示的潮痕还没用到，怀疑可能是宽高被修改过，我们可以利用CRC看看宽高有没有问题，有问题的话就CRC爆破出来正确的

```
import struct, zlib

d = open("tide_trace.png", "rb").read()
crc = struct.unpack(">I", d[29:33])[0]
rest = d[24:29]

for w in range(1, 2001):
    c = zlib.crc32(b"IHDR" + struct.pack(">I", w))
    for h in range(1, 2001):
        if zlib.crc32(struct.pack(">I", h) + rest, c) & 0xffffffff == crc:
            print("width =", w, "height =", h)
            quit()
```

发现图片高度有问题，应该是 960 × 960才对

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBh6bzAmHbUuGwpW9kB9uTLOrcmTFk4LwW8yyE6FJ2N68rRX2dXSfXc5r5Xia5rDDXEAEkBbTwXzzdJCueQhN1qQTmjHbUzOJY18/640?wx_fmt=png&from=appmsg "null")

我们知道，在PNG文件签名之后就是IHDR，内容固定13字节

```
4 字节：宽度
4 字节：高度
1 字节：位深
1 字节：颜色类型
1 字节：压缩方式
1 字节：过滤方式
1 字节：隔行方式
```

所以我们宽度确实是0x3C0，即960，但是高度不是，改成0x3C0即可

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhGdll87hxd4rvgk1w8kHicKuFicVyjg09FocoDKT4CYJjKQksxlZgyUW0ricoNl6ibMbh8vwVvCpxT7zOZWJD70NI6julwMRLI7lA/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBia3GHz3KPR0q5cUqJtTicpQVWTZ0lPFiccthohffbYHiaflWzMaLtQciaU8aoiaFoXxaOH6U2GToo5VXvAnCxRkDfYDWr8Aib1F4pQBg/640?wx_fmt=png&from=appmsg "null")

即可得到上图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhZuuRwXcBbkWxZZm6seBm0qnWowFv3ctxMQsfP3aCVAHZU7GAIbMNBrnEznsriafq47xWGHvvGUglibrL3vGh5VPULsh2rWibGpo/640?wx_fmt=png&from=appmsg "null")

接着又发现这图的颜色类型为6

```
0：灰度
2：RGB 真彩色
3：索引颜色
4：灰度 + Alpha
6：RGB + Alpha
```

所以本题是RGBA图片，出题人多放个Alpha肯定不会瞎放，我们查一下

```
from PIL import Image
import numpy as np

a = np.array(Image.open("tide_trace.png").convert("RGBA"))[:, :, 3]
v, n = np.unique(a, return_counts=True)

for x, y in zip(v, n):
    print(x, y)
```

发现确实不干净，alpha通道有255和254两种，只有最低像素位不一样，一个是1一个是0，明显存在LSB隐写

但是是对半分的，检查一下RGB的最低位好像都是差不多对半分的

说明不是直接存的，是某种关系，最常见的就是异或了，我们可以试一下，一共也没几种

```
channels = {
    "R": rgba[:, :, 0] & 1,
    "G": rgba[:, :, 1] & 1,
    "B": rgba[:, :, 2] & 1,
    "A": rgba[:, :, 3] & 1,
}
names = list(channels)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        name1 = names[i]
        name2 = names[j]

        result = channels[name1] ^ channels[name2]
        print(
            name1,
            name2,
            result.mean()
        )
```

发现只有green通道和alpha通道异或存在明显的异常值，只有7.11%的位置不同，很不自然

想到直接异或生图看看

```
from PIL import Image
import numpy as np

p = np.array(Image.open("tide_trace.png").convert("RGBA"))
x = ((p[:, :, 3] & 1) ^ (p[:, :, 1] & 1)) * 255
Image.fromarray(x.astype("uint8")).save("xor.png")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhAZoOM5Yn9TJYznvbkfWibQtZaBD7aB7PatMas6u3L9vhB8wjcZIqOVIJwGL62tSUEibSgC7wY9MRCUawVnKM4YgOlUtRcfFBxY/640?wx_fmt=png&from=appmsg "null")

明显是一张路线图，还有起点终点

我们按这个路线，走一遍刚刚拿到的6乘6字符表即可得到flag

flag{60a8d749-3760-4560-8bc7-86f2faa7754d}

### 失序货栈-HHB2026

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgiaKbfqLOg9P2FoVaXDRibmdCsqPa6Ddb8saLU6RMs60w1Iua2H5koKtk1GSgGQuzkfle8j9CRdicicWfd22u2KLwL07J2vbThfv0/640?wx_fmt=png&from=appmsg "null")

题目说是序号乱的一塌糊涂，但是说有局部重叠，还有校验码，猜测确实是提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjuibZkUGO1BLDflEiaTn3g2MpicnQeB8LQ173gv5kb6QDibRuHXgc49tibicY3nXja39BqQfKIXd32IJzuWsB1RB...