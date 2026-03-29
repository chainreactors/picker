---
title: 2026春节题目
url: https://mp.weixin.qq.com/s/FR4AVaAoMxjHUWVtSGBAsw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:39:39.218430
---

# 2026春节题目

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aV8UF5rUbwdA9GH114PQO1gJ0Ag5LVYuUTACict7os13ho5HkF2GZRkPLvzCKngQjGHq3aFic5Yn6EOhCbia0evn22kuZCl9Tor38PPVduf3l0/0?wx_fmt=jpeg)

# 2026春节题目

原创

吾爱pojie
吾爱pojie

吾爱破解论坛

![]()

在小说阅读器中沉浸阅读

作者**论****坛账号：仿佛\_一念成佛**

又到了每年一度的解题环节了，我也是等了蛮久的，去年的这个时候都已经结束好久了，今年的春节太后面了，导致我以为都不会有了。

好吧，话不多说，我上一下自己的解题思路吧。纯小白

## Windows 初级题（二）

用 Ida 打开后，`shift + F12` 可以看到如下关键词

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwePaUSYdpmuicoFlO5lxcibvSQns5wYHtZ3pukq8jdYpFlaMslPa4l10PHYIwZ52iaQAYopUicjvC17Goea0G9V8sJf85S0Xu2wseU/640?wx_fmt=png&from=appmsg)

双击点进`[+] Correct flag:`，可以看到一个关键函数`sub_BCD130`，这个函数就是验证函数了。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwexVkJnPWibD0CGdkTx02sZRhovxKYBvqcHCOYQnGubpCibG3ls46t8GlWiaRD0NzIpLR28hOsoG5FJQfbdicZn1JrapjUJiaDPEK0k/640?wx_fmt=png&from=appmsg)

在左侧的窗口中找到`start`函数，按`F5`反编译，发现调用了验证函数。

```
 复制代码 隐藏代码
result = sub_BCD130(dword_BDF024);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwe6ATmzOproR3TicNLxP88VcI4IadicDSZqkaDYNJgxqKibNF18CCzsqE5q8LRk2SLTDfiaaKEsiaiaaicA1CKa2AFaHu7KHjfRDvvDVw/640?wx_fmt=png&from=appmsg)

双击点进，就看到了这个验证函数的反编译代码了，分析一下这个函数的流程：

1. 首先就打印了一个横幅，表示一些提示信息，告诉我们正确的 flag 长度是关键。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwc6guWeia3rXWa7KwQ760PozG4t234zpmmCso1srRgj9nROqVvZ22MdKoN04g2PvDExBuONApjxQtzbS8GKufpQwXkVibuNiaLyJE/640?wx_fmt=png&from=appmsg)

2. 接着就让用户输入密码了，然后读取用户输入的内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwea7ynr7F46XHmgOOPib3ohE7qlNohocN1iaEzgXkOhdSbr6kuticw1bfcIkF63jo32goExELVWql3OahmTaaUtNicbhMZ5eBiaKXg0/640?wx_fmt=png&from=appmsg)

3. 检查输入内容(sub\_B01740) （第一个陷阱）

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfW3ybD7HAHoWHcOVTl2dlfOBt412ia8GuLicyicqRvvf6j8u6sOVHSW64zYicoGdLRJYFQ5stbvEurkgs8OO2FX2OMQq5rbGTyXSQ/640?wx_fmt=png&from=appmsg)

这一步检查了输入的内容，其内容为

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfjibHkxWq9znBKlsbt67NkAeiaibibHO1ticOyxicdkvBDAnDQB7e0JvXa2ZO7rVNFy55nf48mLU2n8NDXsReib3ggxWR6zWkfYicJH7w/640?wx_fmt=png&from=appmsg)

中间有一个`v2 = byte_BD3019[v1++]`。这里是一个关键点，它是一个数组，保存着一个假 Flag，也就是`52pojie_2026_HappyNewYear`，这是一个诱饵。通过 Hex view 可以看到这个诱饵。

函数是从`53`（ASCII '5'）开始的，然后逐字符读取`byte_BD3019`里的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwdyvDEZsibM7NWDToEEiarJPzyP1cpMBhyb0vkicWllMaTJd2v6cIcUXczQbatLm2XwX0GSaqTvmlcuWswEFJq5R01lVib47ZkWaYQ/640?wx_fmt=png&from=appmsg)

4. 前 16 字符对比 （第二个陷阱）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwc2AfkcZq3Efkf07cn0erxichKYrxQhhcQTFTibGLXF6ReTRLJ3XdGuXdblee0USwXYpZWUZzKNXN0ePrrOBXG4IicMfTdftkhVm4/640?wx_fmt=png&from=appmsg)

这一步是对输入的前十六个字符进行对比，这里也有一个数组(byte\_BD3032), 其内容为`52pojie2026Happy`. 如果此刻输入的内容前 16 为刚好匹配，就会进入`You're getting closer` 的分支，提示我们输入的内容已经很接近了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfga7xabtF5JP6L7DibticJTtibJAA7pibzXWVgGcibEZiaO8ng65JanF9oLZBknGgfqQeaB8jbTrO6v04twaD951GjO3xR7fgcEqqKI/640?wx_fmt=png&from=appmsg)

5. 长度验证

通过前面两个陷阱，我们知道了两个线索，现在让我们继续分析下一部分的代码

此处代码提示我们密码必须要求为 31 个字符。也就是说，正确的 flag 长度必须为 31 个字符。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbweiashKaoOUKFk8hrjD5FqicDg3mftqmYMmdpy6gPhDFo6X4AGiaEA34nbkbPgyfSrpRaBa76KpAQhyz3ravhXibQgKdegfQIDI3Zw/640?wx_fmt=png&from=appmsg)

6. XOR 缓冲区比对

这是核心的验证部分了。程序调用了一个函数`sub_B016D0`来判断是否是正确的 flag

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwcMMqHoYibmYtsZ31kFu9W7a3qr6icsbrd2eFKiceYIUJrWPjyGg0guvFQO7hBGzibld9ibmDlNmhYVeevNoBkuFFdqgNibszOVKTlLY/640?wx_fmt=png&from=appmsg)

双击进入这个函数，查看具体的实现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwcgDWDhOCeJGy02VmbSg08DNibHtBQyKZHV8DILgueyicpvWGrEqeCp7ibRSANEibEZ7A0M4bUdBic5R8Ca9iaCDJ947X15pahoOH68U/640?wx_fmt=png&from=appmsg)

在这里有一个非常关键的函数，也就是`sub_B01620`。这一步直接就告诉了我们正确的答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwcnYC8Fn2D02MKGM3rn4BuO2bOFXUxMO1T9QYrzFLZkcOiauF7xjTibG8tdKCAYPurUHiavSaKpwNEK555VMMRJPhVyVu87YV7OLk/640?wx_fmt=png&from=appmsg)

通过这里的分析，可以知道每个字节进行了 XOR 0x42 的操作。交给 AI 来帮我们写一个简单的脚本来解密这个 XOR 缓冲区，得到正确的 flag。

```
 复制代码 隐藏代码
import struct

buf = bytearray(32)
struct.pack_into('<I', buf,  0, 758280311)
struct.pack_into('<I', buf,  4, 1663511336)
struct.pack_into('<I', buf,  8, 1880974179)
struct.pack_into('<I', buf, 12, 494170226)
struct.pack_into('<I', buf, 16, 842146570)
struct.pack_into('<I', buf, 20, 657202491)
struct.pack_into('<I', buf, 24, 658185525)
struct.pack_into('<H', buf, 28, 12323)
buf[30] = 99

for i inrange(31):
    buf[i] ^= 0x42

password = buf[:31].decode('ascii')
print(f"Password: {password}")
print(f"Length:   {len(password)}")

checksum = sum((i + 1) * c for i, c inenumerate(password.encode()))
print(f"Checksum: {checksum} (expected: 44709)")
```

输出：

```
 复制代码 隐藏代码
Password: 52pojie!!!_2026_Happy_new_year!
Length:   31
Checksum: 44709 (expected: 44709)
```

输出的结果和我们前面知道的线索完全匹配，长度为 31，前 16 字符也不完全匹配，校验和也正确。

哦对了，忘记说怎么知道这个 checksum 了。

7. Checksum 验证

很简单，它直接写死了哈哈

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbweEusTNuLsbLZt2iatAvBpV88FVLULV67HjOQunE7ArAczrvq2Q0MaFUqvU5ybzE3Gx3GqFLeMoyLMclqY5tGJUFcEv58OY9CBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfstJRV2Psrg3LYlFlicSV6ll7iade8FvWxvPtu8jicrOt1c0G9eNznFGIjSTpDSXicAuYUjOCKeVdpJBiap3yWBCb903IOVX6IMRDw/640?wx_fmt=png&from=appmsg)

至于计算方法也很简单

```
 复制代码 隐藏代码
checksum = Σ (i × password[i-1])   for i = 1, 2, ..., len
         = 1×p[0] + 2×p[1] + 3×p[2] + ... + 31×p[30]
```

8. 最终验证

从上面的分析结果，我们知道了正确的 flag 是`52pojie!!!_2026_Happy_new_year!`，我们可以直接输入这个 flag 来验证一下。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfxhfadxKIOg8LGAfERl34EsdibQApCbeVEsz2o6aAczQ3Cg1AD3DmUankmwX4GeIMPkND2mianIqDia0ubRmFY9M2v5pDOa596ng/640?wx_fmt=png&from=appmsg)

至此，Windows 初级（二）就算是完全的解出来了。

## Android 初级题（一）

简单的 Android 初级题，对于这个，咱有两个解法，一是好好的完成游戏然后 flag 就会跳出来了。二是直接反编译这个 APK，找到关键函数，分析一下就知道了。

咱们这里的选择是第二种，反编译分析。

先用`jadx`打开这个 APK，搜索 int[][], 找到一个关键数组。这个数据很有可能就是加密后的数据，后面的解密也证实了确实是加密后的重要 flag 数据。另外按照经验，通常会用 XOR 来加密，所以咱们现在来找一下是谁调用了这个关键的数组

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfwU94O1moEvEFPzTjEVFzd4ecUfJVWKFCqlg0gqEB3NDTFLceGWgNrrgTdLngtMZW4yQp26kYVlORt05PqqBO3qBRjjPasckA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwddCFUpVgGZumxZticibteT0vnib8njN6tUSJ3ruR4jErnhsZr2nAynGa1PAXHOf0Dv9nHWdwCFBZg1h5t89H8VNf5rt3wkZBqa7Q/640?wx_fmt=png&from=appmsg)

既然找到了这个关键数组，根据经验，52 的春节题目一般的都是 XOR 加密的，所以现在来找一下密钥在哪里。

定位到 F.C.q0 方法，并且在下方看到了一个可疑的数据，假设这个 bytes 数据就是密钥，接下来找一下解密方法在哪里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aV8UF5rUbwfWgfxXH2hc2CoWUwr7cl2PBq4GuMjUMtNZR2vxsIsEwnlxhmdVAcRHp0QRmib8Gj0hSpr4XUsrtViaQ1pBrRgicUuRgpMzfk77dU/640?wx_fmt=png&from=appmsg)

已知在传入的时候定义了 25，在代码中往上面翻一番，找到 case25 的分支，发现了这个解密

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfaYpf1JTNrDNDu6Uk7vkDCZsztFiamFMX23s8HfpgUfZlbBVqmLl4jLUxDricYJEamS3fibr4KWhBrqic4qeQACleBhC3q8XIjgH0/640?wx_fmt=png&from=appmsg)

好了，现在知道了加密数据和密钥了，接下来就可以写一个简单的脚本来解密了。

```
 复制代码 隐藏代码
key = [0x36, 0x01, 0x16, 0x1C]
data = [
    [80, 109, 119, 123, 77],
    [97, 116, 34, 45, 105],
    [102, 49, 124, 45, 5, 94],
    [4, 49, 36, 42, 105],
    [101, 113, 100, 45, 88, 102, 73],
    [112, 50, 101, 104, 7, 119, 34, 112, 75]
]

flag = ''
for part in data:
    for i, val inenumerate(part):
        flag += chr(val ^ key[i % len(key)])

print(flag)  # flag{Wu41_P0j13_2026_Spr1ng_F3st1v4l}
```

输出：

```
 复制代码 隐藏代码
flag{Wu41_P0j13_2026_Spr1ng_F3st1v4l}
```

或者咱们静态分析，直接用 Frida 来 hook 这个解密函数，直接把解密后的结果打印出来也是可以的。这里就不赘述了。

## Windows 初级题（一）

先用Ida打开随便看一看，发现有PyInstaller特征，故此说明这是一个python程序被打包成了exe，知道这个就好办了。

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwdl0vjC6zuaiafkiaPnD7oibHviatjXKibQPYx1Yjz0MzSrjN3YamicLOhibC8GzG1TWHp9MsyxxRb9bm46ia8yj1ADRliccqD1x3a5SN3k/640?wx_fmt=png&from=appmsg)

用`pyinstxtractor` 来解压这个exe，得到一个crakeme\_easy.pyc的文件

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwe1UH0S1cuzBQia3o9Zv139ekThEN13GU2PhSu814fR71lg6GUhXu06PpmoMWtj8QibjeblQrx35gNh7Z9Ub7cnx7viazMbRCav7E/640?wx_fmt=png&from=appmsg)

再用一个工具来反编译这个pyc文件，得到汇编代码

```
 复制代码 隐藏代码
import dis, marshal

withopen('crackme_easy.pyc', 'rb') as f:
    f.read(16)  # 跳过 pyc 头
    code = marshal.load(f)

dis.dis(code)
```

![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfyunfPApGJYRJpJ5Gicl...