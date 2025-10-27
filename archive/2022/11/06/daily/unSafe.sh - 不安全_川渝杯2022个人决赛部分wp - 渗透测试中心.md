---
title: 川渝杯2022个人决赛部分wp - 渗透测试中心
url: https://buaq.net/go-134331.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:23.528102
---

# 川渝杯2022个人决赛部分wp - 渗透测试中心

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/afe2a0713373f454eb8f613423b08e3e.jpg)

川渝杯2022个人决赛部分wp - 渗透测试中心

re-babyre1、下载得到chall.txt，使用file命令查看文件类型，该文件是python文件2.这里将chall.txt重命名为chall.pyc使用在线python反编译得到pytho
*2022-11-5 19:39:0
Author: [www.cnblogs.com(查看原文)](/jump-134331.htm)
阅读量:70
收藏*

---

## re-babyre

1、下载得到chall.txt，使用file命令查看文件类型，该文件是python文件

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193903741-1287479675.png)

2.这里将chall.txt重命名为chall.pyc

使用在线python反编译得到python(https://tool.lu/pyc)

```
from ctypes import c_uint32
```

3、分析步骤，flag分成了三段：

第一段可以用z3求解

第二段为魔改tea，key为第一段前16字节

第三段为换标base64

4、分段求解即可

```
from ctypes import c_uint32
import base64
'''

from z3 import *

v = [ Int(f'v[{i}]') for i in range(21)]
s = Solver()

s.add(((((((-v[0] + v[1] - v[2]) + v[3] + v[4] - v[5] - v[6]) + v[7] - v[8]) + v[9] - v[10] - v[11] - v[12]) + v[13] - v[14] - v[15] - v[16] - v[17]) + v[18] - v[19]) + v[20] == -321 )
s.add(((((((-v[0] + v[1] - v[2]) + v[3] - v[4] - v[5] - v[6] - v[7]) + v[8] + v[9] + v[10] - v[11]) + v[12] - v[13]) + v[14] - v[15] - v[16]) + v[17] - v[18] - v[19]) + v[20] == -265 )
s.add(((-2 * v[0] + v[1] + 2 * v[3] + 2 * v[4] - 2 * v[5]) + 2 * v[7] + 2 * v[9] - 2 * v[10] - 2 * v[11] - 2 * v[12] - 2 * v[14] - 2 * v[15] - 2 * v[16]) + 2 * v[18] == -144 )
s.add(((-3 * v[0] + 2 * v[1] - v[2]) + 2 * v[4] - 2 * v[5]) + 2 * v[9] - 2 * v[11] - 2 * v[14] - 2 * v[16] - 2 * v[17] - 2 * v[19] == -637 )
s.add(((((((-2 * v[0] + v[1] - v[2]) + v[3] + 2 * v[4] - 2 * v[6]) + 2 * v[7] - 2 * v[8]) + 2 * v[9] - 2 * v[11] - 2 * v[12]) + 2 * v[13] - 2 * v[14]) + 2 * v[18] - 2 * v[19]) + 2 * v[20] == -158 )
s.add((((-6 * v[0] + 3 * v[1] - v[2]) + 2 * v[4] - 2 * v[6] - 2 * v[12]) + 2 * v[13] - 2 * v[16] - 2 * v[17]) + 2 * v[18] == -449 )
s.add((((-6 * v[0] + 3 * v[1] + v[4] - v[5] - 2 * v[6]) + 2 * v[7] - 2 * v[8] - 2 * v[11]) + 2 * v[13] - 2 * v[14] - 2 * v[15] - 2 * v[17]) + 2 * v[20] == -778 )
s.add(((-6 * v[0] + 3 * v[1] + v[4] - v[5] - 2 * v[6]) + 2 * v[9] - 2 * v[12] - 2 * v[14] - 2 * v[17]) + 2 * v[18] - 2 * v[19] == -760 )
s.add((((-13 * v[0] + 5 * v[1] + 2 * v[2] - v[3]) + v[4] - v[5] - 3 * v[6]) + 2 * v[9] - 2 * v[11] - 2 * v[12]) + 2 * v[13] - 2 * v[14] - 2 * v[17] == -1270 )
s.add((((((-22 * v[0] + 8 * v[1] + 3 * v[2] - 4 * v[3]) + 2 * v[4] + v[5] - 2 * v[6] - v[7]) + v[8] - v[9] - v[10]) + v[11] + v[12] - v[13] - v[14] - v[15]) + v[16] + v[17] - v[18]) + v[19] - v[20] == -1494 )
s.add(((((-2 * v[0] + v[1] - v[2]) + v[3] + v[4] - v[5] - v[6]) + v[7] - v[8]) + v[9] - 2 * v[10] - 2 * v[11]) + 2 * v[13] - 2 * v[14] - 2 * v[15] == -528 )
s.add(((((-21 * v[0] + 8 * v[1] + 4 * v[2] - 2 * v[3]) + 2 * v[4] - v[5] - 4 * v[6] - v[7]) + v[9] - v[10] - 2 * v[11] - 2 * v[12] - 2 * v[14] - 2 * v[16]) + 2 * v[18] - 2 * v[19]) + 2 * v[20] == -1853 )
s.add(((((-14 * v[0] + 5 * v[1] - v[3]) + 3 * v[4] - 2 * v[6]) + v[7] - v[8]) + v[9] - 2 * v[10] - v[11] - 2 * v[12]) + 2 * v[20] == -913 )
s.add(((((-20 * v[0] + 7 * v[1] + 3 * v[2] - 2 * v[3]) + 2 * v[4] - 3 * v[6]) + v[9] - 2 * v[10] - v[11] - v[12]) + 2 * v[13] - 2 * v[19]) + 2 * v[20] == -1310 )
s.add((((-11 * v[0] + 4 * v[1] + v[2] - v[3]) + v[4] - v[5] - 2 * v[6] - v[8]) + v[9] - 2 * v[10] - v[11] - v[12]) + v[13] - 2 * v[14] - 2 * v[15] - 2 * v[16] - 2 * v[19] == -1576 )
s.add((((((-21 * v[0] + 8 * v[1] + 3 * v[2] - 3 * v[3]) + v[4] - v[5] - 4 * v[6]) + v[9] - v[10] - v[11] - v[12]) + v[13] - v[14] - 2 * v[17]) + 2 * v[18] - 2 * v[19]) + 2 * v[20] == -1830 )
s.add(((((-27 * v[0] + 9 * v[1] + 5 * v[2] - 4 * v[3]) + v[4] - v[5] - 4 * v[6] - v[7]) + v[9] - 3 * v[10] - v[11] - v[12]) + v[13] - 2 * v[14] - v[15] - 2 * v[17]) + 2 * v[18] - 2 * v[19] == -2692 )
s.add((((-17 * v[0] + 7 * v[1] - 2 * v[3]) + 3 * v[4] - 2 * v[6] - v[8]) + v[9] - 2 * v[10] - v[11] - v[12]) + v[13] - v[14] - v[15] - v[16] - 2 * v[19] == -1519 )
s.add(((((-25 * v[0] + 9 * v[1] + 3 * v[2] - 3 * v[3]) + 3 * v[4] - 4 * v[6] - v[7]) + v[9] - v[10] - v[11] - v[12]) + v[13] - v[14] - v[15] - v[16] - v[17]) + 2 * v[18] == -1937 )
s.add((((((-24 * v[0] + 9 * v[1] + 4 * v[2] - 3 * v[3]) + v[4] - v[5] - 4 * v[6]) + v[9] - 2 * v[10] - v[11] - v[12]) + v[13] - v[14] - v[15] - v[16] - v[17]) + v[18] - 2 * v[19]) + 2 * v[20] == -2078 )
s.add((((((-8 * v[0] + 3 * v[1] + v[2] + 2 * v[4] - v[5] - 2 * v[6]) + v[7] - v[8]) + v[9] - v[10] - v[11] - v[12]) + v[13] - v[14] - v[15] - v[16] - v[17]) + v[18] - v[19]) + 2 * v[20] == -654)

print(s.check())
m=s.model()
print(m)
'''
v=[0]*21
v[6] = 99
v[16] = 49
v[3] = 103
v[0] = 102
v[13] = 45
v[5] = 99
v[12] = 48
v[4] = 123
v[10] = 48
v[1] = 108
v[7] = 102
v[8] = 101
v[2] = 97
v[15] = 54
v[11] = 54
v[9] = 52
v[18] = 45
v[20] = 50
v[14] = 97
v[19] = 52
v[17] = 49

v=bytes(v)
print(v)
flag1=v
def ints2bytes(v = None):
    n = len(v)
    res = b''
    for i in range(n // 2):
        res += int.to_bytes(v[2 * i], 4, 'little')
        res += int.to_bytes(v[2 * i + 1], 4, 'little')
    return res

def bytes2ints(cs = None):
    new_length = len(cs) + (8 - len(cs) % 8) % 8
    barray = cs.ljust(new_length, b'\x00')
    i = 0
    v = []
    while  i  < new_length:
        v0 = int.from_bytes(barray[i:i + 4], 'little')
        v1 = int.from_bytes(barray[i + 4:i + 8], 'little')
        v.append(v0)
        v.append(v1)
        i += 8
        continue

   return v

keys = bytes2ints(v[:16])

c = [86,2,249,121,139,89,236,10,233,193,135,89,22,235,221,127,52,113,82,87,79,72,111,65,61]
flag3=bytes(c[-9:])
print(flag3)
c = c[:-9]

c = bytes2ints(bytes(c))

def enc(v = None, key = None):
    magic = 0xDEADBEEF
    l = c_uint32(v[0])
    r = c_uint32(v[1])
    total = c_uint32(0)
    for _ in range(42):
        l.value -= ((r.value << 4) - (r.value >> 6)) + (key[total.value & 3] << 2) ^ key[r.value << 3 & 3]
        total.value -= magic
        r.value += ((l.value << 5) + (l.value << 4) ^ key[total.value & 3] >> 2) + key[l.value & 3]
    return (l.value, r.value)

def dec(v = None, key = None):
    magic = 0xDEADBEEF
    l = c_uint32(v[0])
    r = c_uint32(v[1])
    total = c_uint32(0)
    for _ in range(42):
        total.value -= magic
    for _ in range(42):
        r.value -= ((l.value << 5) + (l.value << 4) ^ key[total.value & 3] >> 2) + key[l.value & 3]
        total.value += magic
        l.value += ((r.value << 4) - (r.value >> 6)) + (key[total.value & 3] << 2) ^ key[r.value << 3 & 3]

    return (l.value, r.value)

flag2=[]
for i in range(2):
    v0,v1 = dec(c[2 * i:2 * i + 2],keys)
    flag2.extend([v0, v1])
flag2=ints2bytes(flag2)
print(flag2)

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
b = 'ABCDEFGHIJKLMNOPQRST0123456789+/UVWXYZabcdefghijklmnopqrstuvwxyz'
flag3=flag3.decode()
trantab = flag3.maketrans(b, a)
flag3 = base64.b64decode(flag3.translate(trantab))
print(flag3)

flag=flag1 + flag2+ flag3
print(flag)
```

5、运行得到flag

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193905455-933857045.png)

flag{ccfe4060-a611-42d7-8265-32f75cb8cdb8}

## MISC-timu

观察一下发现是sql盲注流量，成功时长度为437,SQL注入流量分析

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193906301-235743518.png)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193907126-1838541285.png)

http.content\_length == 437筛选一下导出文本

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193907951-501544063.png)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221105193908828-806819100.png)

写个脚本提取一下flag

```
import re

number = []
with open("flag.txt","r",encoding="utf-8") as f:
    for i in f.readlines():
        flag_number = re.search('\)\)=(.+?)--',i)
        if flag_number:
            print(chr(int(flag_nu...