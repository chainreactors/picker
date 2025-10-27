---
title: 【2025春节】解题领红包所有题writeup
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141764&idx=1&sn=8da89593f71aa14f99d387bcb7f2ac15&chksm=bd50a6d08a272fc63dce7e48511233eb23b0ac8713331a9c545f253b0e4c38dcf84174478e60&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2025-02-15
fetch_date: 2025-10-06T20:36:36.466483
---

# 【2025春节】解题领红包所有题writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZKZ5cdSZ2Fq37DR7DevRZAnrErFLuKNicLwfonxPic0zBvA3byDTxygdkmsGriaBNkgRqj2iclZ3ek67w/0?wx_fmt=jpeg)

# 【2025春节】解题领红包所有题writeup

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：BMK （通杀榜第一名）**

### 解题领红包之一 {送分题}

没什么好说的

### 解题领红包之二 {Windows 初级题}

运行动调直接拿flag

### 解题领红包之三 {Android 初级题}

base64+xxtea

```
 复制代码 隐藏代码
from struct import *
def shift(z, y, x, k, p, e):
    return ((((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4))) ^ ((x ^ y) + (k[(p & 3) ^ e] ^ z)))
def encrypt(v, k):
    delta = 0x9E3779B9
    n = len(v)
    rounds = 6 + 52 // n
    x = 0
    z = v[n - 1]
    for i in range(rounds):
        x = (x + delta) & 0xFFFFFFFF
        e = (x >> 2) & 3
        for p in range(n - 1):
            y = v[p + 1]
            v[p] = (v[p] + shift(z, y, x, k, p, e)) & 0xFFFFFFFF
            z = v[p]
        p += 1
        y = v[0]
        v[n - 1] = (v[n - 1] + shift(z, y, x, k, p, e)) & 0xFFFFFFFF
        z = v[n - 1]
    return v
def decrypt(v, k):
    delta = 0x9E3779B9
    n = len(v)
    rounds = 6 + 52 // n
    x = (rounds * delta) & 0xFFFFFFFF
    y = v[0]
    for i in range(rounds):
        e = (x >> 2) & 3
        for p in range(n - 1, 0, -1):
            z = v[p - 1]
            v[p] = (v[p] - shift(z, y, x, k, p, e)) & 0xFFFFFFFF
            y = v[p]
        p -= 1
        z = v[n - 1]
        v[0] = (v[0] - shift(z, y, x, k, p, e)) & 0xFFFFFFFF
        y = v[0]
        x = (x - delta) & 0xFFFFFFFF
    return v
from base64 import *

if __name__ == '__main__':
    key = list(unpack("<4I",b"my-xxtea-secret\x00"))
    enc = b64decode(b"hjyaQ8jNSdp+mZic7Kdtyw==")
    print(len(enc))
    enc = list(unpack(f"<{len(enc)//4}I",enc))
    print(enc)
    pt = decrypt(enc,key)
    s = b''
    for i in range(len(pt)):
        s+=pack("<I",pt[i])
    print(s.decode())
```

### 解题领红包之四 {Android 中级题}

白盒aes，但是是ofb模式。本来直接调试拿xor的值就完事了，但是懒得掏出来一年没用的测试机直接静态看恢复密钥了。

直接用的前年的强网杯的白盒aes模版跑的dfa，把so中的数据提取一下放到对应的变量中去就行

```
 复制代码 隐藏代码
from test2 import *

#abcdefghijklmnop

def change_index():
    global v16
    array2 = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
    arr = [0] * 16

    for i in range(16):
        arr[i] = v16[array2[i]]

    v16 = arr

import numpy

v11 = numpy.array(v11).reshape((9,16,256)).tolist()
v12 = numpy.array(v12).reshape((9,96,16,16)).tolist()
print(len(v13))
v13 = numpy.array(v13).reshape((9,16,256)).tolist()
table4 = numpy.array(table4).reshape((16,256)).tolist()
def AAA():
    global v16
    global  ss
    global flag
    for i in range(9):
        change_index()
        if i==8 and flag: #最后一轮修改得到dump
            v16[ss] = 0
        for j in range(4):
            num = v11[i][4 * j][v16[4 * j]]
            num2 = v11[i][4 * j + 1][v16[4 * j + 1]]
            num3 = v11[i][4 * j + 2][v16[4 * j + 2]]
            num4 = v11[i][4 * j + 3][v16[4 * j + 3]]
            num5 = v12[i][24 * j][(num >> 28 & 15)][(num2 >> 28 & 15)]
            num6 = v12[i][24 * j + 1][(num3 >> 28 & 15)][(num4 >> 28 & 15)]
            num7 = v12[i][24 * j + 2][(num >> 24 & 15)][(num2 >> 24 & 15)]
            num8 = v12[i][24 * j + 3][(num3 >> 24 & 15)][(num4 >> 24 & 15)]
            v16[4 * j] = (v12[i][24 * j + 4][num5][num6] << 4 | v12[i][24 * j + 5][num7][num8])
            num5 = v12[i][24 * j + 6][(num >> 20 & 15)][(num2 >> 20 & 15)]
            num6 = v12[i][24 * j + 7][(num3 >> 20 & 15)][(num4 >> 20 & 15)]
            num7 = v12[i][24 * j + 8][(num >> 16 & 15)][(num2 >> 16 & 15)]
            num8 = v12[i][24 * j + 9][(num3 >> 16 & 15)][(num4 >> 16 & 15)]
            v16[4 * j + 1] = (v12[i][24 * j + 10][num5][num6] << 4 | v12[i][24 * j + 11][num7][num8])
            num5 = v12[i][24 * j + 12][(num >> 12 & 15)][(num2 >> 12 & 15)]
            num6 = v12[i][24 * j + 13][(num3 >> 12 & 15)][(num4 >> 12 & 15)]
            num7 = v12[i][24 * j + 14][(num >> 8 & 15)][(num2 >> 8 & 15)]
            num8 = v12[i][24 * j + 15][(num3 >> 8 & 15)][(num4 >> 8 & 15)]
            v16[4 * j + 2] = (v12[i][24 * j + 16][num5][num6] << 4 | v12[i][24 * j + 17][num7][num8])
            num5 = v12[i][24 * j + 18][(num >> 4 & 15)][(num2 >> 4 & 15)]
            num6 = v12[i][24 * j + 19][(num3 >> 4 & 15)][(num4 >> 4 & 15)]
            num7 = v12[i][24 * j + 20][(num & 15)][(num2 & 15)]
            num8 = v12[i][24 * j + 21][(num3 & 15)][(num4 & 15)]
            v16[4 * j + 3] = (v12[i][24 * j + 22][num5][num6] << 4 | v12[i][24 * j + 23][num7][num8])
            num = v13[i][4 * j][v16[4 * j]]
            num2 = v13[i][4 * j + 1][v16[4 * j + 1]]
            num3 = v13[i][4 * j + 2][v16[4 * j + 2]]
            num4 = v13[i][4 * j + 3][v16[4 * j + 3]]
            num5 = v12[i][24 * j][(num >> 28 & 15)][(num2 >> 28 & 15)]
            num6 = v12[i][24 * j + 1][(num3 >> 28 & 15)][(num4 >> 28 & 15)]
            num7 = v12[i][24 * j + 2][(num >> 24 & 15)][(num2 >> 24 & 15)]
            num8 = v12[i][24 * j + 3][(num3 >> 24 & 15)][(num4 >> 24 & 15)]
            v16[4 * j] = (v12[i][24 * j + 4][num5][num6] << 4 | v12[i][24 * j + 5][num7][num8])
            num5 = v12[i][24 * j + 6][(num >> 20 & 15)][(num2 >> 20 & 15)]
            num6 = v12[i][24 * j + 7][(num3 >> 20 & 15)][(num4 >> 20 & 15)]
            num7 = v12[i][24 * j + 8][(num >> 16 & 15)][(num2 >> 16 & 15)]
            num8 = v12[i][24 * j + 9][(num3 >> 16 & 15)][(num4 >> 16 & 15)]
            v16[4 * j + 1] = (v12[i][24 * j + 10][num5][num6] << 4 | v12[i][24 * j + 11][num7][num8])
            num5 = v12[i][24 * j + 12][(num >> 12 & 15)][(num2 >> 12 & 15)]
            num6 = v12[i][24 * j + 13][(num3 >> 12 & 15)][(num4 >> 12 & 15)]
            num7 = v12[i][24 * j + 14][(num >> 8 & 15)][(num2 >> 8 & 15)]
            num8 = v12[i][24 * j + 15][(num3 >> 8 & 15)][(num4 >> 8 & 15)]
            v16[4 * j + 2] = (v12[i][24 * j + 16][num5][num6] << 4 | v12[i][24 * j + 17][num7][num8])
            num5 = v12[i][24 * j + 18][(num >> 4 & 15)][(num2 >> 4 & 15)]
            num6 = v12[i][24 * j + 19][(num3 >> 4 & 15)][(num4 >> 4 & 15)]
            num7 = v12[i][24 * j + 20][(num & 15)][(num2 & 15)]
            num8 = v12[i][24 * j + 21][(num3 & 15)][(num4 & 15)]
            v16[4 * j + 3] = (v12[i][24 * j + 22][num5][num6] << 4 | v12[i][24 * j + 23][num7][num8])
    change_index()
    for k in range(16):
        v16[k] = table4[k][v16[k]]

    for l in range(16):
        v16[l] = v16[l]

flag = 1

for ss in range(16):
    v16 = [i for i in range(97, 97 + 16)]
    AAA()
    for i in v16:
        print(hex(i)[2:].zfill(2), end='')
    print()

# 3694bf644864b8474a4576bb89c69f14
# 1094bf644864b85e4a4554bb89ac9f14
# 9d94bf644864b8514a45d7bb89299f14
# 0ff94bf644864b8f74a45a7bb8939f14
# 1894bf644864b8eb4a4567bb896a9f14
# 0360bf642c64b8474a4576cb89c62f14
# 3660bf646764b8474a45768e89c6af14
# 3697bf646764b8474a45764289c61b14
# 36d5bf647f64b8474a45763589c64214
# 3694e96448afb847834576bb89c69f54
# 3694fd64486db847814576bb89c69f8d
# 3694ae6448d9b847744576bb89c69fbb
# 3694c1644893b847214576bb89c69f97
# 3694bfc84864ef474ab176bbcac69f14
# 03694bf3f48647474ab576bb23c69f14
# 03694bf84864ef474ad176bb11c69f14
# 3694bf3f4864c2474ad476bbcac69f14
data = b"""
43941d39cd79f798851e0f2928123ad2
24941d39cd79f76a851ebb2928103ad2
84941d39cd79f726851ec42928373ad2
83941d39cd79f7bf851ed12928633ad2
c4941d39cd79f78b851e822928373ad2
43e81d398b79f798851e0f06281246d2
43d01d39c479f798851e0f72281238d2
43d61d39ee79f798851e0fab28128ed2
432f1d399a79f798851e0faa281269d2
43947d39cdcaf798511e0f2928123ae0
43942339cd18f798bd1e0f2928123a27
4394ce39cd26f798bd1e0f2928123ab4
43949f39cd2af7983b1e0f2928123a1c
43941d9ccd79c69885d20f2931123ad2
43941d9bcd794c9885eb0f2930123ad2
43941d2ccd79099885010f2929123ad2
43941d47cd79879885230f2942123ad2"""
with open("E://trace",'wb') as f:
    f.write(data)
import phoenixAES
phoenixAES.crack_file('E://trace',[],True,False,3)
```

```
 复制代码 隐藏代码
Last round key #N found:
931C3A97F6D1C217E58CF94FC843B226931C3A97F6D1C217E58CF94FC843B226
```

用stark解出原密钥为7E13141528AED2A6ABF7158809CF4F3C

```
 复制代码 隐藏代码
from Crypto.Ciph...