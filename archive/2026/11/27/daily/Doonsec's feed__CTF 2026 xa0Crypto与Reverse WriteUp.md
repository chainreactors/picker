---
title: ?CTF 2026 xa0Crypto与Reverse WriteUp
url: https://mp.weixin.qq.com/s/kmXH1vVTdlgvP9EGuJr6vw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:47.405726
---

# ?CTF 2026 xa0Crypto与Reverse WriteUp

# ?CTF 2026  Crypto与Reverse WriteUp

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# QCTF 2026 Crypto 与 Reverse WriteUp

本篇汇总 Crypto 与 Reverse 两个方向的题目。Crypto 包含密码学实现、RSA、格攻击、矩阵与曲线相关题型；Reverse 包含汇编、安卓逆向、虚拟机、随机数、数独与字节码分析。

## 题目概览

### Crypto

* **W1**：Advanced Encryption tandard、手撕平方根-Easy、手撕平方根-Hard、签到、Decision、简单的RSA
* **W2**：Curve、leaked\_primes、FHE、certificate
* **W3**：ezDec、LinearRSA、LongTime、Matrix Shi(f)t
* **W4**：Double Bind、Bivariate copper

### Reverse

* **W1**：intro、Hello\_Assem1y、Pangbai 泰拉记二周目（1）、艾克赛尔
* **W2**：Pangbai 泰拉记二周目（2）、PangbaiOfficial、壳有壳味、这是一个二游五灵王的陷阱、Mathgame、何为百合啊？
* **W3**：宝石魔术 ·现代刻印、cpp 噩梦、Bytecode SMC、ezHook、signal
* **W4**：Pangbai 泰拉记二周目（3）

## Crypto

### W1

#### Advanced Encryption tandard

#1 分析

题目给出了16 个 0 字节和flag 被一个去掉 S 盒的“AES”加密后的结果（密钥未知），要求据此还原出flag。

#2 解题思路

可以发现，去掉 S 盒以后的 AES 加密过程实际上是私钥（题目中的secret\_key，视为 16 个 G=GF(2)[x]/(x8+x4+x3+x+1) 上的元素）和明文（视为另外 16 个 G 上的元素）在 G 上的线性运算。由于密文 enc 的前 16 字节所对应的明文已知（为 16 个0 字节），于是将私钥视为 16 个 G 上的变量，先按照加密流程进行符号计算，再对照enc 的前 16 字节列出 16 条一次方程，最后解列出的方程组即可得到私钥。由于题目使用的是 CTR（计数器）模式，因此得到私钥以后使用私钥再次加密密文即可得到 flag。

#3 exp

```
#include <iostream>
#include <cstring>
#include <utility>
usingnamespacestd;
constexprconstunsignedchar rcon[] = {0x00, 0x01, 0x02, 0x04, 0x08,
0x10, 0x20, 0x40, 0x80, 0x1b, 0x36};
constexpr unsigned char HexToDec(const char c)
{
return c - (c >= 'a' ? 'a' - 10 : '0');
}
constexpr unsigned char XTimes(const unsigned char val)
{
return (val << 1) ^ ((static_cast<signedchar>(val) >> 7) &
0x1b);
}
constexpr unsigned char Mul(unsigned char a, unsigned char b)
{
unsignedchar ans = 0;
while (b)
{
if (b % 2)
ans ^= a;
a = XTimes(a);
b /= 2;
}
return ans;
}
constexpr unsigned char Inv(unsigned char a)
{
unsignedchar ans = 1;
for (unsigned i = 254; i; i /= 2)
{
if (i % 2)
ans = Mul(ans, a);
a = Mul(a, a);
}
return ans;
}
char hex_enc[2048];
unsignedchar secret_key[16], round_keys[44][4], enc[1024],
counter[16], result[16];
struct Variable
{
unsignedchar coef[17];
constexpr Variable() : coef{} {}
constexpr Variable(const unsigned char val) : coef{}
{
coef[16] = val;
}
friendconstexpr Variable operator^(const Variable &a, const
Variable &b)
{
Variable ans;
for (unsigned i = 0; i < 17; ++i)
ans.coef[i] = a.coef[i] ^ b.coef[i];
return ans;
}
constexpr Variable &operator^=(const Variable &other)
{
for (unsigned i = 0; i < 17; ++i)
coef[i] ^= other.coef[i];
return *this;
}
friend constexpr Variable XTimes(const Variable &a)
{
Variable ans;
for (unsigned i = 0; i < 17; ++i)
ans.coef[i] = XTimes(a.coef[i]);
return ans;
}
} var_sk[16], var_rks[44][4], equ[16];
constexprconst Variable var_zeros[16]{};
template <typename T>
void KeyExpansion(const T (&secret_key)[16], T (&round_keys)[44][4])
{
memcpy(round_keys, secret_key, sizeof(secret_key));
for (unsigned i = 4; i < 44; ++i)
if (i % 4)
for (unsigned j = 0; j < 4; ++j)
round_keys[i][j] = round_keys[i - 4][j] ^ round_keys[i
- 1][j];
else
{
for (unsigned j = 0; j < 4; ++j)
round_keys[i][j] = round_keys[i - 4][j] ^ round_keys[i
- 1][(j + 1) % 4];
round_keys[i][0] ^= rcon[i / 4];
}
return;
}
template <typename T>
void AddRoundKey(T (&state)[4][4], const T (&round_key)[4][4])
{
for (unsigned i = 0; i < 4; ++i)
for (unsigned j = 0; j < 4; ++j)
state[i][j] ^= round_key[i][j];
return;
}
template <typename T>
void ShiftRows(T (&state)[4][4])
{
T temp[4];
for (unsigned i = 0; i < 4; ++i)
{
for (unsigned j = 0; j < 4; ++j)
temp[j] = state[j][i];
for (unsigned j = 0; j < 4; ++j)
state[j][i] = temp[(i + j) % 4];
}
return;
}
template <typename T>
void MixColumns(T (&state)[4][4])
{
for (unsigned i = 0; i < 4; ++i)
{
T temp1[4], temp2[4];
for (unsigned j = 0; j < 4; ++j)
temp1[j] = state[i][j] ^ state[i][(j + 1) % 4];
for (unsigned j = 0; j < 4; ++j)
temp2[j] = XTimes(temp1[j]) ^ state[i][(j + 1) % 4] ^
temp1[(j + 2) % 4];
for (unsigned j = 0; j < 4; ++j)
state[i][j] = temp2[j];
}
return;
}
template <typename T>
void AESEncrypt(const T (&block)[16], const T (&round_keys)[44][4], T
(&result)[16])
{
T state[4][4];
for (unsigned i = 0; i < 16; ++i)
state[i / 4][i % 4] = block[i];
AddRoundKey(state, *reinterpret_cast<const
T(*)[4][4]>(round_keys));
for (unsigned round = 1; round <= 9; ++round)
{
ShiftRows(state);
MixColumns(state);
AddRoundKey(state, *reinterpret_cast<const
T(*)[4][4]>(round_keys + round * 4));
}
ShiftRows(state);
AddRoundKey(state, *reinterpret_cast<const T(*)[4][4]>(round_keys
+ 40));
for (unsigned i = 0; i < 16; ++i)
result[i] = state[i / 4][i % 4];
return;
}
int main()
{
ios::sync_with_stdio(false);
cin.tie(nullptr);
cin >> hex_enc;
size_t len_enc = 0;
while (hex_enc[2 * len_enc])
{
enc[len_enc] = (HexToDec(hex_enc[2 * len_enc]) << 4) |
HexToDec(hex_enc[2 * len_enc | 1]);
++len_enc;
}
for (unsigned i = 0; i < 16; ++i)
var_sk[i].coef[i] = 1;
KeyExpansion(var_sk, var_rks);
AESEncrypt(var_zeros, var_rks, equ);
for (unsigned i = 0; i < 16; ++i)
equ[i] ^= enc[i];
unsigned rank = 0;
for (unsigned i = 0; i < 16; ++i)
{
unsigned p = rank;
while (p < 16 && equ[p].coef[i] == 0)
++p;
if (p < 16)
{
swap(equ[p], equ[rank]);
constunsignedchar c = Inv(equ[rank].coef[i]);
equ[rank].coef[i] = 1;
for (unsigned j = i + 1; j < 17; ++j)
equ[rank].coef[j] = Mul(equ[rank].coef[j], c);
while ((++p) < 16)
if (equ[p].coef[i])
{
for (unsigned j = i + 1; j < 17; ++j)
equ[p].coef[j] ^= Mul(equ[p].coef[i],
equ[rank].coef[j]);
equ[p].coef[i] = 0;
}
++rank;
}
}
for (unsigned i = 16; i--;)
{
secret_key[i] = equ[i].coef[16];
for (unsigned j = i + 1; j < 16; ++j)
secret_key[i] ^= Mul(secret_key[j], equ[i].coef[j]);
}
KeyExpansion(secret_key, round_keys);
for (size_t i = 16; i < len_enc;)
{
++*reinterpret_cast<__uint128_t *>(counter);
AESEncrypt(counter, round_keys, result);
for (unsigned j = 0; j < 16 && i < len_enc; ++i, ++j)
cout.put(enc[i] ^ result[j]);
}
cout.put('\n');
return0;
}
```

#### 手撕平方根-Easy

#1 分析

题目首先给出满足存在大质数p、q 使得n=pq 的正整数n，让用户输入一个 [0,n) 中的整数x，并尝试寻找并返回一个满足的 [0,n) 中的正整数y（或报告其不存在），最后将 flag 编码为整数 m 后计算并返回。题目要求据此还原 flag。

#2 解题思路

考虑到如果存在整数 、 使得 、 且 ，则由

可知  与  中必有一个给出  的非平凡因子。因此只需求出满足上面条件的 ，再将题目的平方根输出用作候选值。

题目中的 `Sqrt(x, p)` 会等概率返回一个满足 $0\le a<p$ 且="" $a^2\equiv="" x\pmod="" p$="" 的整数="" $a$；对奇质数="" $p$，若这样的="" $a$="" 存在，则另一个解是="" $p-a$。由于分别对="" $p,q$="" 开方，题目的输出会从最多四个模="" $n$="" 的平方根中随机选取一个。<="" p="">

因此可以在  中任取 （例如取 ），令 。返回的  有约  的概率与  模  既不相同也不互为相反数，此时取 ，计算两个最大公因数即可分解 。

对于随机生成的整数 ，四个模  平方根都不同的概率为

因此上一段的方法以接近  的概率成功，重复几次即可。得到  后，按与题目相同的 CRT 组合方式从  恢复 ，并筛选  的候选，再按题目相反顺序还原 flag。

#3 exp

```
from pwn import process, remote
from random import randint
from Crypto.Util.strxor import strxor
from Crypto.Util.number import GCD, inverse
from hashlib import sha3_512
def Sqrt(x: int, p: int):
    x %= p
    if x == 0:
        return x
    pM1D2 = (p - 1) // 2
    whileTrue:
        r = randint(0, p - 1)
        if pow(r * r - x, pM1D2, p) != 1:
            if r * r % p == x:
                return r
            break
    a, b, c, d = 1, 0, (-2 * r) % p, x
    for i in bin(pM1D2 + 1)[:1:-1]:
        if i == "1":
            a, b = (b - a * c) % p, b * d % p
        else:
            b = (a * d - b * c) % p
        c, d = (2 * d - c * c) % p, d * d % p
    return a
whileTrue:
    # target = process(["python3", "chall.py"])
    target = remote("127.0.0.1", 12345)
    target.recvuntil(b"n = ")
    n = int(target.recvline(drop=True))
    y1 = randint(1, n - 1)
    target.sendlineafter(b"x = ", str(y1 * y1 % n).encode())
    target.recvuntil(b"y = ")
    y2 = int(target.recvline(drop=True))
    g = GCD(n, y1 + y2)
    if g != 1and g != n:
        p, q = g, n // g
        break
    g = GCD(n, y1 - y2)
    if g != 1and g != n:
        p, q = g, n // g
        break
    target.close()
target.recvuntil(b"c = ")
c = int(target.recvline(drop=True))
mp, mq = Sqrt(c, p), Sqrt(c, q)
cp, cq = q * inverse(q, p), p * inverse(p, q)
candidate_m = [(i * cp + j * cq) % n for i in (mp, p - mp) for j in
(mq, q - mq)]
for m in candidate_m:
    if m < 2**1024:
        bytes_m = m.to_bytes(length=128, byteorder="little")
        r, l = bytes_m[:64], bytes_m[64:...