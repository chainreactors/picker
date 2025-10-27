---
title: 2024第四届“网鼎杯”朱雀组 writeup
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511399&idx=1&sn=273c780a71db7f58e52566ae018cf950&chksm=e89d85bfdfea0ca99659dfcd12362619e8e4249bda58a995e0895c879f5f099b3ecbd0851574&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-07
fetch_date: 2025-10-06T19:19:08.219314
---

# 2024第四届“网鼎杯”朱雀组 writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT9qDIaDfQvWPj6DQmg01BjVRDC6bJxmzo34THjPzePFabAiakeaiaI0PQ/0?wx_fmt=jpeg)

# 2024第四届“网鼎杯”朱雀组 writeup

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Reverse

### Re1

SMC

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT6l41ZrfCPUMlWcysOlhNV9HgE6WEvvmDHZ5Cuic8hFt1VEXeJesxbmA/640?wx_fmt=png&from=appmsg)

写个idapython patch一下

```
start = 0x140003000
for i in range(0x600):
    PatchByte(start+i, (Byte(start+i)+0x42)&0xff)
```

base24

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT0j9aQ4F8eKicNsINkr3A06JDZAAVJVySZyGurmLJmcZI8v3ke4xEezg/640?wx_fmt=png&from=appmsg)

叫gpt帮忙写一个解密就行

```
# -*- coding: utf-8 -*-
import libnum

def decode_base24(ciphertext, code_table):
    """
    Decodes a base24 encoded string using a custom code table.

    :param ciphertext: The base24 encoded string to decode.
    :param code_table: A string containing all the characters in the base24 code table.
    :return: The decoded string.
    """
    # 将密文字符串中的每个字符转换为其在码表中的索引
    temp = [code_table.index(char) for char in ciphertext if char in code_table]

    # 将索引转换为十进制数
    num = 0
    for i, value in enumerate(temp):
        num += value * (24 ** (len(temp) - i - 1))

    # 将十进制数转换为字符串
    decoded_bytes = libnum.n2s(num)

    # 解码为可读字符串
    decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

    return decoded_string

# 自定义码表
base24_code_table = "4836CR7F9TXGQVWYB2JPHKDM"

# 放入密文
ciphertext = "4FKMKYP497G87QXHBTRJKCGM63XXCC8CDQX39TQPYFY"

# 解码
decoded_string = decode_base24(ciphertext, base24_code_table)

print(decoded_string[::-1])
```

### Re2

Vmp的壳子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTEPo9wLibS31DKEYbRau8ial9OcWeees1jfgaOiaa9IwVx4n8rbwBF0Nug/640?wx_fmt=png&from=appmsg)

不好脱，直接字符串大法搜索关键函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTiabOX6siamcFcjU6GCGTvmUuNJ0NEtszCbRdPLtY9rO145TBeWX1zD5w/640?wx_fmt=png&from=appmsg)

发现有些关键信息，比如勒索病毒加密等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTIp27zCUibyEEXsI8g34mZSTCRVrgEnglciaD2rwcVr7cs2Kj2Ria0jLBg/640?wx_fmt=png&from=appmsg)

跟进svchost.exe字符串发现存在一个异或解密，配合字符串信息大致认为解密后释放了一个svchost.exe程序或者注入进了svchost进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT0ggYmxINL4XcmsCxmB5H9RuGhC16m7mtXPtpDCLgianu8Cqr5iaiaSWlA/640?wx_fmt=png&from=appmsg)

丢沙盒里检测可以看到确实如此。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTiaNSCvXBRLa7Y4qURbpr8oCvNTbOaGh4uM1AXorzhQkFS3JIP8hT2Ew/640?wx_fmt=png&from=appmsg)

因为存在断点check，所以先运行再瞬间断点，即可绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT0VYQ9p7pliavFSPqMnqIG51nYS8F5Bw37pONnIHtYJTicdgv1aiaaMO9Q/640?wx_fmt=png&from=appmsg)

把0x3650048的数据提取出来再异或。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTB85PrLJhBPkmemgmSSIufytoQOm5b7TibiciaGQIicLa1yJsJvGdPZjSnw/640?wx_fmt=png&from=appmsg)

可以看到elf文件中对文件进行了加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNT9NHpQvao2wcEcpu9lxFxR5GuhBkV2AX67WBHyjDX2W5w75ZNztqQuA/640?wx_fmt=png&from=appmsg)

典型的aes加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTYLmMRelu0vuQJDX1OZ6wcI5bm8bDGYicyibrYO4fCAgeVBAxm8AXAicVw/640?wx_fmt=png&from=appmsg)

Key导出来则是：3b7e151638aed2a6bbf7158819cf4f3c
赛博厨子加上xor爆破解密得到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSeWL4L1fV1zIFWflQJ0fNTBcoKVe0VYpvjGmGN82ia0QCpYcKia7ywQ9TIsm6cb6u2sfSB7Fzo0hGQ/640?wx_fmt=png&from=appmsg)

## crypto

### crypto002

这一题没啥好说的，1024的n，给了p的高256，就是一个已知p高位攻击，稍微爆破几个比特就行了。具体爆破多少位，取决于你设置的 epilon是多少，8比特差不多要0.01，12比特要0.02，我的电脑差不多一个小时。

### crypto003

第一问给的是

p1 = getPrime(1024)
q1 = nextprime(2024 \* p1)

直接对 n1/2024 开跟就能得到一个素数了

第二问是

n2 = p2 \* q2
n22 = p2 \* p2 + q2 \* q2

解方程，没啥说的。

第三问

```
r = random.getrandbits(1024)
p3 = r
while not is_prime(p3):
    p3 += random.getrandbits(400)
q3 = r
while q3 < p3:
    q3 += random.getrandbits(500)
while not is_prime(p3):
    q3 += random.getrandbits(500)
n3 = p3 * q3
f.write("n3 = {0}\n".format(n3))
```

这里题目有点问题，都是以 p3 是否为素数来结束循环，所以q3其实不是一个素数。。。

但比赛的是时候没想那么多。测试发现就是直接对 n3 开根就能得到 p3 的高位，然后就是一个p的已知高位攻击。

最后一问才是这一题最难的地方，

```
m1 = p1 * m * m + p2 * m + p3
m2 = q1 * m * m + q2 * m + q3
c1 = pow(m1, e, n)
c2 = pow(m2, e, n)
```

这里根据前面我们已经获得到 p1,p2,p3,q1,q2,q3，只有未知数m

并且m是两个方程，也就是 f(m) = p1 \* m \* m + p2 \* m + p3,g(m)=q1 \* m \* m + q2 \* m + q3的共根。这里引用明文相关攻击的思路，就是对两个多项式求一个 GCD，但是直接GCD可能会爆递归深度，这里用的是 fast\_polymonial\_gcd，当初做seectf遇到的 https://jayxv.github.io/2023/06/15/2023%20seectf/，罗密欧朱丽叶这一题。

结束

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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