---
title: 对称加密与非对称加密算法原理详解
url: https://mp.weixin.qq.com/s/eubdY7pqCe0_KysexvCRZA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:50:53.100257
---

# 对称加密与非对称加密算法原理详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaABk8n1Yb8NfCs4akOia4HFGwecH69pygvicmicRmmNC68wV1tACA0S4IXTkLemVnM49NM8RVGydiclmgDZia4lqYLaiaBKcMoviasmI8/0?wx_fmt=jpeg)

# 对称加密与非对称加密算法原理详解

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

众所周知数据对于一个公司来说，非常重要，一旦数据泄露，公司将面临非常大的威胁，数据加密非常重要。

对称加密是指加密和解密使用相同密钥的加密算法，常见的对称加密算法有DES,DES3,AES加密算法。对称加密由于其加解密速度快，常被用于大量的数据加密场景，还有对传输效率要求高的场景如VPN之间的传输，但是由于其密匙不方便保存，所以适合于内部系统。

**01**

**DES加密算法**

DES加密算法是一种分组加密算法，通过将输入的明文按64位一组，进行分组加，加密过程分为初始置换明文，分组明文，生成子密匙，密匙与明文加密，经过S盒替(如表1.14所示)，P盒替换(如图1.16所示)，置换后的密文与原32位明文加密。具体流程图如下图1.1 DES加密流程图

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawPwvibD0pfVpL3V6HwVJVqckqdLkuZcWicAbVSJaQ7YaR4rQpjaQj3ceQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

图1.1 DES流程图

初始置换：初始置换是只将输入的64位明文，按照一个置换表进行置换位置，具体置换规则：初始数据里面的64是1号位，置换表的1则到了第40这个位置，那么64置换之后就到了第40这个位置、63是原来的2号位，在置换表里面是第8号位，所以63经过置换表则到了第8位，其他的位置执行同样的操作，具体操作如表1.1，表1.2，表1.3：

表1.1 初始数据表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VaweH9TTKZK130WJIZ5jCIaITYCGrt6DIZUciaQ9Dcv8fOUgoxDgkwg2kg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

表1.2 置换表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawCuOOHw80ZVRIls7N92cTg86Xdm4kRufibHUl9uWoWicSnStJNR9eJtKA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

表1.3 置换后数据

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawtYCDwMgiapNFFMcM3GZqLDj1wrEElmysRq2afCQ8UD5dXRcHRO7XowQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

拿到置换后的数据后，将明文分组左右两组。将初始置换之后的数据按前32位为左边L0，后32位为右边R0。具体分组如表1.4,1.5.

表1.4 左边L0

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawwQrVTOZh98TGELWs5OKBYTN9pIgL2VeJnxibDVtrEJSEw8AiciaGibwuibA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

表1.5 右边R0

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawV0l6dibiaKRwicHmibxwGZervb1wwicJ1YTw1eEZoQR9PzrgGebxHq0fT4g/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

主密匙是用户定义的一个密匙，将一个主密匙生成16个子密匙，每一次操作用一个密匙。用户设置的一个64位key,我们将其忽略第8,16,24,32,40,48,56,64奇偶检验位。得到一个56位key,将其进行移位操作，再进行压缩置换就得到具体加密的KEY。具体操作如表1.6 所示

表1.6 移位操作是移位表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6Vaw024rtwbLCR1z5VzyEZBcsSicpLWb5xArMYzvYV06PQzxcBDQrywxMHw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

从表中我们可以知道，第一轮是左移一位，第三轮是左移两位,后面一堆位数安按照1.6所示即可。具体移位如表1.7，表1.8

表1.7 主密匙表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawOJ8a3JLnYa0YnVHq2HNaXOn7EmCicibpwNfgAMXGlmXRHeY6qLIlQIeg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

表1.8 左移一位后的密匙

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6Vawbkgwvq95pYmxWB3u0vakgEBsXNLp7W6QfKAXdCGzib3pvvhWjsS7GYA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

移位之后进行压缩置换，将56位的密匙进行48位的置换表置换，得到48位密匙舍去8位，如表1.9,1.10，表1.11所示

表1.9 密匙

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawIcT3UAqDibp4eR10VLg88lfeCAXdIngzzlPnWrod4HZFic4cRiaoMe5Yg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

表1.10 48位置换表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawHNnqdJ71TViacib3M1ic29ictodYXyPAnBqL95WkhYVv7E9VBM0eVrBtJQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

表1.11 置换之后得到的数据KEY1

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawGHn9luOdEF77UuVNaZIlyHlvgibQGaFTzWOjX1hEOoeKtiamunPRfhTA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

得到48位密匙后，因为明文分组是32位，所以对明文进行扩充置换成48位，以下操作是对明文进行扩充置换，对于扩充后的明文我们可以发现，他中间四列是原来的明文，并没有修改，增加的第一列是原明文的最后一列从倒数排列，新添加的第后一列，则是第一列的倒数。具体如表1.12，表1.13所示。

表1.12 左边明文L0

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawwErvKDUR0l1CibrNMicNI9zC2ksfIm171ZDfibVRn6ItGdlObDDfbKdNw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

表1.13 扩充之后的明文L0

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawfhOw2l9GibiadZMJY3vYRiaxkfs2EeYDt1ibRDib69RtdxJphHkeIeTjdwQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

现在得到48位密匙和48位数据，就可以进行异或加密操作了。异或操作后面拿到的数据是加密后的数据，我们对此数据进行S盒替换和P盒替换。

S盒替换是将48位的数，分组8组，一组6位，进入S盒,一个S盒6位输入4位输出，及48位出入，进入8个S盒输出只有32位。具体替换如表1.14。

表1.14 S0盒

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawKhjbhQsvicibIKYPoFf7JTxc4b41LtzZyqdclofemM2bu7M2nVpVXgJg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

例如：输入为101110 那么他的第一位和最后一位组合10转换位10进制则为2及第2行，中间四为0111转为10进制及为7及第7列，所以第2行，第7列及为2转为2进制及为0010，所以输入101110，输出0010，S盒替换完成。经过S盒换以后就要经过P盒替换了，具体替换过程如下表1.15,1.16,1.17所示

表1.15 S盒替换后的数据

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawaXXvpibiaQnicfJRNib606ZPicg3gXgUseU7HHgnVUwOOl6ynLJcvAlAaeg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

表1.16 P盒

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawRYzF1rbrA2Aky0ruMr2ibYvT0zgMrbbSbJJFDADseS8R3NXY97ZdjCQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

表1.17 P盒置换后的数据

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6Vaw6iaOH3pg5krkzh4Le3PFMO38bqWgliaKZBh1yuAlZ3GdGz5lsdJkb1VA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

现在我们已经拿到P盒置换后的数据了，再跟我们第一次分组生成的32位左边的数据进行异或操作，这次拿到的数据就是我们第一轮加密后的数据，再进行左右互换，进行同样的加密操作，连续操作16次，加密就算完成了。

加密完成了，接下来就是解密了，解密和加密是同样的操作，输入64位明文，进行初始置换，将KEY倒着进行加密，密匙移位，加密是向左移，那么解密就是向右移，执行同样的操作就可以解密进行解密操作。

**02**

**AES加密算法**

AES加密算法是分组加密，每一组是16字节，是目前主流的高级加密算法。他的加密过程主要分为密匙轮询，字节替代，行移动，列混合，密匙加轮…….以上操作重复10次，输出的即是加密的数据，具体流程图如1.2所示

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawfI9GhoPq96ypTCtkx6wLJRHQZCfjUhC8M6PyHdc4ia2cdVpDsK1sFiaA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

图2.1 AES加密流程图

密匙加轮：用密匙与原文进行异或操作，原文是128位，密文也是128位，首先将主密匙与原文进行异或操作，后面再用主密匙生成40位子密匙。密匙生成过程如下所示：

KEY = 3C A1 0B 21 57 F0 19 16 90 2E 13 80 AC C1 07 BD

初始密匙：

W[0]=3C A1 0B 21
W[1]=57 F0 19 16
W[2]=90 2E 13 80
W[3]=AC C1 07 BD

生成密匙算法：

1.如果i不是4的倍数，那么第i列用如下公式：

W[i]=W[i-4] XOR W[i-1] (XOR表示异或的意思，下同)

2.如果i是4的倍数，那么第i列用如下公式：

W[i]=W[i-4] XOR T(W[i-1])

解释一下T（）函数：由三部分组成，字循环，字节替代，轮常量代替异或。

a.字循环：将1个字中的4个字节循环左移1个字节。即将输入字[a0, a1, a2, a3]变换成 [a1,a2,a3,a0]。

b.字节代换：对字循环的结果使用S盒进行字节代换(具体S盒如图2.2所示)。

c.轮常量异或：将前两步的结果同轮常量进行异或。具体如表2.1所示

表2.1 轮询常量表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawbFtkkqFDRbfEnEDaeormTTCjZkYF8JBAxWUyMibVbsx0ZB7lt6PQbgQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

例如：

初始密匙

W[0]=3C A1 0B 21
W[1]=57 F0 19 16
W[2]=90 2E 13 80
W[3]=AC C1 07 BD

计算W[4],W[5],W[6],W[7]

求W[4]的时候，因为4是4的倍数，所以，我们先要求T(W[3])

W[3]= AC C1 07 BD

左移一位 得到 C1 07 BD AC

进入S和字节替换

进S盒替换时，例如替换C1，C则是行，1则是列，找到第C行第1列即可以找到替换的数字(16进制的数)，S盒具体如图1.3所示

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawZzazoADqaF5kzYswPQaLc4bryia8Q47ibia1iaE2EmxgRh8icficDNOD7poQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)

图2.2 S盒

C1在S盒中对应78,

07在S盒中对应C5

BD在S盒中对应7A

AC在S盒中对应 91

所以经过第二步S盒替换变成了78,C5,7A,91

(3).将78 C5 7A 91 XOR 01 00 00 00 = 79 C5 7A 91

所以计算密匙如下：

W[4]= W[0] XOR T(W[3] ) = 3C A1 0B 21 XOR 79 C5 7A 91 = 45 64 71 B0
W[5]= W[1] XOR W[4] = 57 F0 19 16 XOR 45 64 71 B0 = 12 94 68 A6
W[6]= W[2] XOR W[5] = 90 2E 13 80 XOR 12 94 68 A6 = 82 BA 7B 26
W[7]= W[3] XOR W[6] = AC C1 07 BD XOR 82 BA 7B 26 = 2E 7B 7C 9B

同样的方法计算其他密匙。

有了密匙，将明文与密匙异或运算，接下来进行字节替代。例如，假设我们明文与密匙加轮得到的数据是abcdefghijklmnop具体如表2.2,2.3,2.4所示

表2.2 轮询后的数据

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicd0LlSRshb6rPdugAR6VawpzaJxdK62gShrReSP1exY4IiatI8AHYTyKqEhJojoaoI816dXt...