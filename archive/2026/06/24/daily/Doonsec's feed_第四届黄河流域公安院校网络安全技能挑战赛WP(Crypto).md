---
title: 第四届黄河流域公安院校网络安全技能挑战赛WP(Crypto)
url: https://mp.weixin.qq.com/s/o9ZaE1DtmQeQYVHxfOBljQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:04:21.977916
---

# 第四届黄河流域公安院校网络安全技能挑战赛WP(Crypto)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNS6iaKdc2uvZiazSfA8LBnMiaqPTR3bibvvapHI04teibocBykqC8jobCNH9nUB77tEkjrypickiaxM4r8buicxW3HlB1xibUuT5FCAO6IudGZ4pkBk/0?wx_fmt=jpeg)

# 第四届黄河流域公安院校网络安全技能挑战赛WP(Crypto)

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于沉思安全
，作者x3x\_bot

![](http://wx.qlogo.cn/mmhead/LTpwfH82ricmd0KHzGqehNEEwzZt6BXzI73pSJOp00riaWMEU7odeicdaJ5KDBltzq2VkUPbibZyxCw/0)

**沉思安全**

## 目录

* Crypto

+ Annihilati0n
+ Double²
+ Ledger Fog
+ Split Personality: Gauge
+ λd

## Crypto

### Annihilati0n

#### 题目概述

附件中有一个 Python 截断多重递归生成器。64 字节 flag 被分成 16 个 4 字节大端整数并用作递归系数：

```
n = 16
beta = 16
c = [int.from_bytes(flag[i:i+4], "big") for i in range(0, 64, 4)]
v = sum(i * j for i, j in zip(c, s)) % m
out.append(v >> beta)
```

设`B = 2^16`、`x[t] = B*out[t] + r[t]`、`0 <= r[t] < B`。那么隐藏序列满足

```
x[t+16] = c[0]*x[t] + ... + c[15]*x[t+15] (mod m)
```

对于 200 个泄漏的高位输出。

#### 关键思路

直接低 16 位路线不可行，因为每个低部分都会反馈到下一个状态。有用的对象是消灭关系：一个短多项式，其与隐藏的`x`序列的卷积为零模`m`。

重要的实现细节是对商格进行加权。对于`h = floor(m / 2^16)`，关系向量应该使`sum eta[i] * out[t+i]`以`h`为模变小，同时保持`eta`变小。成功使用的格子：

```
h = 65535
r = 70
t = 131
BKZ block = 20
eta_weight = 4
```

The lattice basis is:

```
[ out[i+j] for j in 0..t-1 | eta_weight * e_i ]   for i in 0..r-1
[ h * e_j                 | 0                    ]   for j in 0..t-1
```

在 BKZ 之后，eta 部分可被 `eta_weight` 整除的行给出了歼灭子式多项式。

#### 解题过程

使用上述参数后会产生许多短关系多项式。成对结果共享一个 512 位公因子：

```
factor ... 4294934537^16
modulus candidates = [4294934537]
```

So the modulus is:

```
m = 4294934537
```

然后超过`Z/mZ`的多项式gcd恢复了16次特征多项式。对 `m` 取模的较低系数取反，得到 16 个递归系数：

```
[1718378855, 2069195630, 813133407, 1295017077,
 1819620703, 1279677266, 1597010484, 1668035423,
 829644621, 1986226271, 1211396708, 863133518,
 813129543, 811553584, 1819685727, 829694333]
```

用`to_bytes(4, "big")`转换每个系数即可重建flag。

#### 关键求解代码

完整的实现在 `solve.sage` 中。生成 flag 的入口点是 `modrelw`，由下面的加权商格支持：

```
def search_quotient_relations_weighted(y, h, r, t, block_size=20, keep=8, scale=1, eta_weight=4):
    dim = r + t
    W = ZZ(eta_weight)
    L = Matrix(ZZ, dim, dim)
    for i in range(r):
        for j in range(t):
            L[i, j] = ZZ(scale) * ZZ(y[i + j])
        L[i, t + i] = W
    for j in range(t):
        L[r + j, j] = ZZ(scale) * ZZ(h)
    reduced = L.BKZ(block_size=block_size)
    etas = []
    for row in range(reduced.nrows()):
        raw_eta = [ZZ(reduced[row, t + j]) for j in range(r)]
        if any(raw_eta) and all(v % W == 0for v in raw_eta):
            etas.append([v // W for v in raw_eta])
            if len(etas) >= keep:
                break
    return etas
```

将恢复的eta行转换为多项式；结果恢复`m`，并且在`Z/mZ`上的gcd恢复特征多项式和系数。

#### 最终结果

```
flag{Ukn0wn_M0dulu5_LFSR_0r4cl3_1s_Mvch_H4rd3r_N0w_G0_S0lv3_1t!}
```

#### 完整求解脚本

```
import itertools
import json
import sys
import time

out = [23477, 44296, 2808, 15971, 4739, 10831, 25610, 26802, 24417, 46263, 31967, 20330, 59314, 58755, 33543, 38822, 32363, 11498, 14479, 60748, 1746, 48846, 45035, 63495, 7628, 58041, 15563, 65410, 62416, 52326, 32017, 15255, 31785, 5160, 46406, 5732, 30541, 16100, 9840, 46005, 43501, 41048, 37590, 5974, 52499, 59758, 60026, 5182, 19985, 1934, 30534, 27346, 52656, 46020, 40599, 58230, 8925, 21738, 41502, 18493, 24598, 38607, 3215, 49559, 49674, 36653, 43172, 1783, 60772, 13306, 21654, 27674, 30374, 9566, 18109, 27483, 12006, 52613, 63762, 5012, 12570, 245, 16694, 63041, 183, 17411, 6569, 20803, 23005, 52128, 60223, 327, 33374, 50304, 27073, 41285, 17999, 49599, 23059, 61257, 23351, 39086, 30097, 36894, 46601, 43953, 4648, 22314, 53552, 9781, 51567, 24307, 8385, 599, 53439, 20274, 38123, 6599, 23364, 43068, 39517, 60742, 53986, 60364, 24538, 13279, 39886, 32989, 62938, 61555, 48542, 44678, 17331, 55620, 24270, 2597, 34598, 967, 51873, 28770, 4222, 42457, 26642, 23959, 49336, 58807, 48295, 5885, 26201, 10594, 17870, 43952, 21827, 34083, 39870, 9444, 46963, 13061, 41528, 55419, 4183, 611, 39106, 3550, 10548, 32750, 30663, 41910, 65390, 45490, 22809, 15712, 31322, 61817, 45474, 28303, 32148, 25048, 34352, 36290, 37912, 63419, 26238, 12639, 53536, 7646, 54498, 8801, 26172, 55915, 56082, 33610, 48430, 35391, 4174, 31996, 51918, 33990, 33249, 53328]

n = 16

def search_linear_relations(y, r, t, block_size=20, keep=8, scale=1):
    print("search_linear_relations r=%d t=%d block=%d scale=%d" % (r, t, block_size, scale), flush=True)
    start = time.time()
    L = Matrix(ZZ, r, r + t)
    for i in range(r):
        for j in range(t):
            L[i, j] = ZZ(scale) * ZZ(y[i + j])
        L[i, t + i] = 1
    reduced = L.BKZ(block_size=block_size)
    print("BKZ done in %.2fs" % (time.time() - start), flush=True)
    etas = []
    for row in range(min(keep, reduced.nrows())):
        first = [ZZ(reduced[row, j]) for j in range(t)]
        eta = [ZZ(reduced[row, t + j]) for j in range(r)]
        if any(eta):
            print("row", row, "first_inf", max(abs(v) for v in first), "eta_inf", max(abs(v) for v in eta), flush=True)
            etas.append(eta)
    return etas

def search_linear_relations_fpylll(y, r, t, block_size=20, keep=8, scale=1):
    from fpylll import IntegerMatrix, LLL, BKZ

    print("search_linear_relations_fpylll r=%d t=%d block=%d scale=%d" % (r, t, block_size, scale), flush=True)
    rows = []
    for i in range(r):
        row = [0] * (r + t)
        for j in range(t):
            row[j] = int(ZZ(scale) * ZZ(y[i + j]))
        row[t + i] = 1
        rows.append(row)
    A = IntegerMatrix.from_matrix(rows)
    start = time.time()
    LLL.reduction(A)
    if block_size > 2:
        BKZ.reduction(A, BKZ.Param(block_size=int(block_size)))
    print("fpy linear reduction done in %.2fs" % (time.time() - start), flush=True)
    etas = []
    for row_idx in range(min(keep, A.nrows)):
        first = [ZZ(A[row_idx, j]) for j in range(t)]
        eta = [ZZ(A[row_idx, t + j]) for j in range(r)]
        if any(eta):
            print("fpy row", row_idx, "first_inf", max(abs(v) for v in first), "eta_inf", max(abs(v) for v in eta), flush=True)
            etas.append(eta)
    return etas

def search_quotient_relations(y, h, r, t, block_size=20, keep=8, scale=1):
    print("search_quotient_relations h=%d r=%d t=%d block=%d scale=%d" % (h, r, t, block_size, scale), flush=True)
    start = time.time()
    dim = r + t
    L = Matrix(ZZ, dim, dim)
    for i in range(r):
        for j in range(t):
            L[i, j] = ZZ(scale) * ZZ(y[i + j])
        L[i, t + i] = 1
    for j in range(t):
        L[r + j, j] = ZZ(scale) * ZZ(h)
    if block_size <= 2:
        reduced = L.LLL()
    else:
        reduced = L.BKZ(block_size=block_size)
    print("quotient reduction done in %.2fs" % (time.time() - start), flush=True)
    etas = []
    seen = set()
    for row in range(reduced.nrows()):
        first = [ZZ(reduced[row, j]) for j in range(t)]
        eta = [ZZ(reduced[row, t + j]) for j in range(r)]
        ifnot any(eta):
            continue
        key = tuple(eta)
        if key in seen:
            continue
        seen.add(key)
        first_inf = max(abs(v) for v in first)
        eta_inf = max(abs(v) for v in eta)
        eta_l1 = sum(abs(v) for v in eta)
        print("row", row, "first_inf", first_inf, "eta_inf", eta_inf, "eta_l1", eta_l1, flush=True)
        etas.append(eta)
        if len(etas) >= keep:
            break
    return etas

def search_quotient_relations_fpylll(y, h, r, t, block_size=20, keep=8, scale=1):
    from fpylll import IntegerMatrix, LLL, BKZ

    print("search_quotient_relations_fpylll h=%d r=%d t=%d block=%d scale=%d" % (h, r, t, block_size, scale), flush=True)
    dim = r + t
    rows = []
    for i in range(r):
        row = [0] * dim
        for j in range(t):
            row[j] = int(ZZ(scale) * ZZ(y[i + j]))
        row[t + i] = 1
        rows.append(row)
    for j in range(t):
        row = [0] * dim
        row[j] = int(ZZ(scale) * ZZ(h))
        rows.append(row)
    A = IntegerMatrix.from_matrix(rows)
    start = time.time()
    LLL.reduction(A)
    if block_size > 2:
    ...