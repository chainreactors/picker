---
title: 2026fic初赛计算机&amp;互联网取证部分
url: https://mp.weixin.qq.com/s/7YeaeZFm1jJ_3He4cpe-bw
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:26.568494
---

# 2026fic初赛计算机&amp;互联网取证部分

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnaYoTkOWOE1QGczljJQp41ibiccDdLUVSmYibQe33AaRzsuZs7bG6EWgwAuENVOuT0Eia4Nyqib14gvjhwuguOuOrNRfV0vrV6AuxI/0?wx_fmt=jpeg)

# 2026fic初赛计算机&互联网取证部分

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原本想着把二进制程序复现完再发的，结果盘古石杯耗尽了我们全部的精力，所以最后的二进制部分随缘更新~

说什么都多余了，来看题吧，感觉剧情不如平航杯

## 案情简介

某日，警方接到举报，举报人称近期互联网上出现了一涉黄网站极为活跃并大肆推广。警方跟进线索分析后，找到相应的网站进行了摸排调查，最终锁定网站的运营者李安弘，警方在对其实施抓捕的现场对电子数据进行了提取固定。

通过对李安弘的审讯，警方了解到，其雇佣了技术人员帮忙架设淫秽视频平台，并找到境外团队对网站进行推广，经过审讯和调查，该嫌疑人还有多种其他违法行为，用以牟利。

请各位参赛选手对检材进行分析，尝试还原整个案件和关键信息。

(本故事纯属虚构，仅为考试设计，可能会出现各检材间时间细节无法对齐现象，请忽略）

## 容器密码

`FIC-{e404d6e66586e9460c23755afab5a872bcf78ab4}`

## 计算机部分

从来没见过的Deepin操作系统，应该是基于linux内核的

好多记录了答案的应用不在桌面上，要在下方任务栏找

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmg1vS9LJ4KRGgicVHxLZxIOp9icFgBkXKvqia20dKPF82ibWgIZOXRMWNt9Fg8XCicnaQlzPnuSkzL750YXYWv3nBaIss4KxJjwZL4/640?wx_fmt=jpeg&from=appmsg)

有点恶心

### 1. 分析计算机检材，操作系统版本号为

23.1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rn6EDgsFvgNWCWn6HZAHsIHVcuQj86dCplQic7TlLZVsgJzBUGz0prpDz0fKdxNPibdvoh8urugMw6ibvMxspypXDybJXx4OzbB5I/640?wx_fmt=png&from=appmsg)

### 2. 分析计算机检材，李安弘曾收到一份免费领取token的邮件的疑似钓鱼邮件，其发送用户邮箱为

hf13338261292@outlook.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmBFAzIjRaDtUDLwDl501GuRckIEg0cPhWEy0YyIvU3HVnQe9ppffvbgdLlZc7MFW00Ja1icCxWdo9w6TxhtmmmSkETDMSQmxtw/640?wx_fmt=png&from=appmsg)

注意不要跟上面那个`回复：Token 限时免费领`的邮件搞混了

### 3. 分析计算机检材，李安弘电脑中记录的黄金换现金的商家联系方式为

136 1281 7854

这种一般都是记录在记事本、便签之类的应用里面，但是找了半天没找到

最后在下方的启动器中找到了语音记事本

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmLFsCLO9BvfEWVJHNqkhrgoC92y2S3IewQfLx02Gxyfz0Sq4UPhJDKtAS9Le0xZAHEiakYr8MGtjGV1ibJ1bXjic3E2lbWHCWvick/640?wx_fmt=png&from=appmsg)

### 4. 分析计算机检材，推广设计图中的apk下载链接为

https://drive.google.com/file/d/1z3aRS-lkaJYKm7Cp1XjtUmVPsOEVW2fV/view?usp=sharing

在邮件中发现与推广设计图相关的邮件

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmHbUjSMfp77vbUmnHtSzLicPaEibCpPYgsyeaR4hibScibJ7dlfqoLqernFopcPN8e4rV8GEUpjsesI7VxicwBxvibtdjuX11ia7sVa0/640?wx_fmt=png&from=appmsg)

在仿真中通过启动器找到邮箱，找到这封邮件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkQkheZYyxIG6yqbxGTxKOuEx7BMGiczcjM6AjtnwqmFeibLib7KJraRRicJEclgPm2cXE7WcbkvDSOfNcyQUNZ0JKZnAFUiaaJtHkA/640?wx_fmt=png&from=appmsg)

还有3个附件，统统下载下来

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmtTGNicuTSVHYxRgvmFcLaibMyAYY404YSxa6kNiaFZUDIgNyAxUnW8RZMicblRROt7ibqXLV6LQZzic9Z0ZglhDib2AlmanWEeqicYDg/640?wx_fmt=png&from=appmsg)

看起来推广设计图被加密了，先看一看加密图片查看.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkiauZPZ5Rv1BhFIFDcunbof8sDyZPYpR3gAaG5cA2S3l73MDDx1TaxIskJsWk5EiaGhoicLY1MiaJBoWv1cibiaPeI6GRJBm0kqQXLk/640?wx_fmt=png&from=appmsg)

图片应该是被rsa加密了，那么public.txt应该给出了rsa相关参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnuSzOBkmYBOrLZeYCb5qR7vnWUqB5nr3CcKQTmsz6wXKaYSEu0I3YvUsh9O8jPcQIJ4Oe6icULYnTSpEWbs0saxewgBtEXUuQA/640?wx_fmt=png&from=appmsg)

public.txt给出了rsa模数：

```
57751892008149574447756694613209346511056045951970458143905594411398554113111623746466692172544473909892773600617029641656248235151775166339061269972238018743173330948084699695182438765935110193323089354031112350869626121317836465551360104372140181097747761558797918522051881262043738603183528521379831286761
```

和公钥指数：

```
65537
```

根据html，我们需要根据和恢复出私钥指数

回顾一下rsa：

1. 随机选取两个不同的大质数和
2. 计算模数
3. 计算欧拉函数
4. 选取公钥指数，满足，且，即互质，一般取65537
5. 计算私钥指数即为在模的乘法逆元这里已知了和，就可以尝试分解出和，计算出，进而计算出

本题存在的漏洞是和比较接近，可以用Fermat法分解出来

上脚本

```
from math import isqrt, gcd

from random import randrange

import time

import sys

# =========================

# RSA 参数

# =========================

n = 57751892008149574447756694613209346511056045951970458143905594411398554113111623746466692172544473909892773600617029641656248235151775166339061269972238018743173330948084699695182438765935110193323089354031112350869626121317836465551360104372140181097747761558797918522051881262043738603183528521379831286761

e = 65537

# =========================================================

# 1. 小素数试除

# =========================================================

def trial_division(n, limit=100000):

    print("[*] Stage 1: small prime trial division")

    for i in range(2, limit):

        if n % i == 0:

            return i, n // i

    returnNone

# =========================================================

# 2. Fermat 分解（p≈q）

# =========================================================

def fermat_factor(n):

    print("[*] Stage 2: Fermat factorization")

    a = isqrt(n)

    if a * a < n:

        a += 1

    step = 0

    whileTrue:

        b2 = a * a - n

        b = isqrt(b2)

        if b * b == b2:

            p = a - b

            q = a + b

            if p * q == n:

                return p, q

        a += 1

        step += 1

        if step % 200000 == 0:

            print(f"    iter={step}")

# =========================================================

# 3. Pollard Rho（通用）

# =========================================================

def pollard_rho(n):

    print("[*] Stage 3: Pollard Rho")

    if n % 2 == 0:

        return2

    whileTrue:

        x = randrange(2, n - 1)

        y = x

        c = randrange(1, n - 1)

        d = 1

        while d == 1:

            x = (pow(x, 2, n) + c) % n

            y = (pow(y, 2, n) + c) % n

            y = (pow(y, 2, n) + c) % n

            d = gcd(abs(x - y), n)

        if d != n:

            return d

# =========================================================

# 主流程

# =========================================================

start = time.time()

p = q = None

# -------------------------

# Stage 1

# -------------------------

res = trial_division(n)

if res:

    p, q = res

    print("[+] Found by trial division")

# -------------------------

# Stage 2

# -------------------------

ifnot p:

    res = fermat_factor(n)

    if res:

        p, q = res

        print("[+] Found by Fermat")

# -------------------------

# Stage 3

# -------------------------

ifnot p:

    factor = pollard_rho(n)

    p = factor

    q = n // factor

    print("[+] Found by Pollard Rho")

# =========================================================

# 输出 RSA 私钥

# =========================================================

print("\n==============================")

print("[+] p =", p)

print("[+] q =", q)

phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

print("[+] d =", d)

print("==============================")

print(f"[*] time = {time.time() - start:.2f}s")

'''
输出结果：
[*] Stage 1: small prime trial division
[*] Stage 2: Fermat factorization
[+] Found by Fermat

==============================
[+] p = 7599466560762641743052493422970151283281211357103780410638724588686758080375558505939025432223250000657857469723929623791715127854747607854590078838861499
[+] q = 7599466560762641743052493422970151283281211357103780410638724588686758080375558505939025432223250000657857469723929623791715127854747607854590078838861739
[+] d = 35523357349779905170178187485659935251135867134837314931979222758324282670976025397371947065926313872401811028702468817834912779886756496413632572670718195811151125658055182908097177746721685442556966643339035563906268671458582959248629716030078694677882031903468615733997083390985840508421177858054952995297
==============================
[*] time = 0.02s
'''
```

用html解密一下

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmcZBvKibFeRsuvnGkV146cBewxCVeBicOiaTRPl06bCnT7riaNSvzakQsdhgnecObOZlS3yIU2I894tuO5es3fOI835UEehu7gC20/640?wx_fmt=png&from=appmsg)

还是张涩图，扫个码就能看到链接

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkCCQ6jK9lPiajlhich0eMH4h3OEsK4hZeNaOmM3ttSEd6vvqZwdayyibz6pxX7aXpxuASph9EVJKoOnH4vWxgovCgK6FwCPibo6v0/640?wx_fmt=png&from=appmsg)

### 5. 分析计算机检材，李安弘电脑vpn软件开放的代理端口为

9527

在启动器里面找到vpn软件Clash Verge，首页里面就有

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlN0hOTDiajCjxNMC27ySCLv4mBJrSPxNW0K9LvoYbEwUMnM7VBD9iaibic1A9fLAPBiabiacC0zV1Aa5VO7Uj4SFVUzFtqaarfibV3po/640?wx_fmt=png&from=appmsg)

设置里面也能看到

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rklkyk193juc1sV0hbzRic9MbIoYkymicSN3LagxcTdu2h9DRUW...