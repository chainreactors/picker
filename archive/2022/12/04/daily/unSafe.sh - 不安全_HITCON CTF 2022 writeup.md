---
title: HITCON CTF 2022 writeup
url: https://buaq.net/go-138390.html
source: unSafe.sh - 不安全
date: 2022-12-04
fetch_date: 2025-10-04T00:28:25.133257
---

# HITCON CTF 2022 writeup

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

![]()

HITCON CTF 2022 writeup

もう日が経ってしまったけど、HITC
*2022-12-3 16:22:49
Author: [furutsuki.hatenablog.com(查看原文)](/jump-138390.htm)
阅读量:48
收藏*

---

もう日が経ってしまったけど、HITCON CTF 2022のcrypto問題のwriteupです。難しい問題は解けなかったけど簡単な問題も楽しかったです。あらゆるところで言ってるけど、[maple](http://d.hatena.ne.jp/keyword/maple)とlyxがめちゃめちゃ信用できる。

* [Baby SSS](#Baby-SSS)
* [Secret](#Secret)
* [Superprime](#Superprime)

## Baby SSS

```
from random import SystemRandom
from Crypto.Cipher import AES
from hashlib import sha256
from secret import flag

rand = SystemRandom()

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

DEGREE = 128
SHARES_FOR_YOU = 8

poly = [rand.getrandbits(64) for _ in range(DEGREE + 1)]
shares = []
for _ in range(SHARES_FOR_YOU):
    x = rand.getrandbits(16)
    y = polyeval(poly, x)
    shares.append((x, y))
print(shares)

secret = polyeval(poly, 0x48763)
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR)
print(cipher.encrypt(flag))
print(cipher.nonce)
```

とりあえずひと目見てわかることを整理します。

とりあえず一式から[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)全部を復元できないかを考えますが、[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)の係数は64bitであるのに対して、各シェアの![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)

しかし今回は8個のシェアが与えられているので、それぞれのシェアで![ y_i \mod x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20y_i%20%5Cmod%20x_i) を取ると、係数の定数項を中国剰余で復元できそうです。定数項（仮に![ k_{i, 0}](https://chart.apis.google.com/chart?cht=tx&chl=%20k_%7Bi%2C%200%7D)とします）がわかれば、![ y_i = k_0 + \sum_{j=1}^{N} k_0x_i^j](https://chart.apis.google.com/chart?cht=tx&chl=%20y_i%20%3D%20k_0%20%2B%20%5Csum_%7Bj%3D1%7D%5E%7BN%7D%20k_0x_i%5Ej)なので ![ (y_i - k_0) / x_i \equiv k_1 \mod x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20%28y_i%20-%20k_0%29%20%2F%20x_i%20%5Cequiv%20k_1%20%5Cmod%20x_i)となり、次々に係数が求まります。

実装するとこう

```
import ast
from hashlib import sha256
from Crypto.Cipher import AES

with open("output.txt") as f:
    shares = ast.literal_eval(f.readline())
    ciphertext = ast.literal_eval(f.readline())
    nonce = ast.literal_eval(f.readline())

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

DEGREE = 128
SHARES_FOR_YOU = 8

coeffs = []
for d in range(DEGREE + 1):
    pairs = []
    values = []
    mods = []
    for i in range(len(shares)):
        x, y = shares[i]
        s = y - polyeval(coeffs, x)
        values.append(s // x**d)
        mods.append(x)

    c = CRT(values, mods)
    coeffs.append(c)

secret = polyeval(coeffs, int(0x48763))
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(cipher.decrypt(ciphertext))
```

ptrlibのCRTメソッドは各![ x_i](https://chart.apis.google.com/chart?cht=tx&chl=%20x_i)が厳密に互いに素であることを要求してきたので今回はSagemathを使いました。そのうち治したい。

## Secret

問題はこう

```
import random, os
from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(1024)
q = getPrime(1024)
n = p * q

flag = open('flag','rb').read()
pad_length = 256 - len(flag)
m = bytes_to_long(os.urandom(pad_length) + flag)
assert(m < n)
es = [random.randint(1, 2**512) for _ in range(64)]
cs = [pow(m, p + e, n) for e in es]
print(es)
print(cs)
```

唯一の![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)のもとで、64個の![ { e_i }](https://chart.apis.google.com/chart?cht=tx&chl=%20%7B%20e_i%20%7D)を用いて![ c_i = m^{e_i + p} \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20c_i%20%3D%20m%5E%7Be_i%20%2B%20p%7D%20%5Cmod%20n)という暗号化をしている[RSA](http://d.hatena.ne.jp/keyword/RSA)です。一見Common Moudulus Attack典型のような形をしていますが、![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)が不明なので、まず![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)を求める必要がありそうです。

これについては最近N1CTF 2022で出題されたBrand new checkinという問題で似たような要求があったことを思い出し、出題者である[maple](http://d.hatena.ne.jp/keyword/maple)さんのwriteupを見に行ったところ、さらに過去に[maple](http://d.hatena.ne.jp/keyword/maple)さんが出題した問題の解説がありました。

[github.com](https://github.com/maple3142/My-CTF-Challenges/tree/master/ImaginaryCTF/Round%2026/no_modulus)

これによれば、以下のような理屈で![ c](https://chart.apis.google.com/chart?cht=tx&chl=%20c)と![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)の複数の組から![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)が求まります。

複数の数の組![ {a_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Ba_i%7D)を仮定して、![ a_0e_0 + a_1e_1 + \dots = 0 \mod \phi(n)](https://chart.apis.google.com/chart?cht=tx&chl=%20a_0e_0%20%2B%20a_1e_1%20%2B%20%5Cdots%20%3D%200%20%5Cmod%20%5Cphi%28n%29)となるとき、![ \prod m^{a_ie_i} \equiv m^{1} \equiv 1 \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cprod%20m%5E%7Ba_ie_i%7D%20%5Cequiv%20m%5E%7B1%7D%20%5Cequiv%201%20%5Cmod%20n)なので、![ \prod c_i^{a_i} -1 = kn](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cprod%20c_i%5E%7Ba_i%7D%20-1%20%3D%20kn)となり、このような![ {a_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Ba_i%7D)と同様の![ {b_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Bb_i%7D)を用意して、![ \gcd(\prod c_i^{a_i} - 1, \prod c_i^{b_i} - 1) = n](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cgcd%28%5Cprod%20c_i%5E%7Ba_i%7D%20-%201%2C%20%5Cprod%20c_i%5E%7Bb_i%7D%20-%201%29%20%3D%20n)となることが期待できます[\*1](#f-1fd3529c "実際にはLLLで整数解ではなく有理数解が得られるので分母を払った形のgcdをとることになるとおもいます。詳しくはmapleさんの解説にあります")。

さて、![ {e_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Be_i%7D)からそのような![ {a_i}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7Ba_i%7D)を求めるのはLLLの得意とするところで、

![\begin{pmatrix} e_0 & 1 \\ e_1 & & 1 \\ \vdots & & & \ddots \end{pmatrix}](https://chart.apis.google.com/chart?cht=tx&chl=%5Cbegin%7Bpmatrix%7D%20e_0%20%26%201%20%5C%5C%20e_1%20%26%20%26%201%20%5C%5C%20%5Cvdots%20%26%20%26%20%26%20%5Cddots%20%5Cend%7Bpmatrix%7D)

という行列のLLLでそのような係数が複数求まります[\*2](#f-e795f109 "実践的にはスケーリングをすることになります")。

今回は少し発展して![ \sum a_i (p + e_i) \equiv 1 \mod \phi(n)](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Csum%20a_i%20%28p%20%2B%20e_i%29%20%5Cequiv%201%20%5Cmod%20%5Cphi%28n%29) の場合について考える必要があるので一筋縄ではいかない、というかこれをLLLで解くのは無理じゃないか……？　と思っていましたが、なんか実験していたら適当なスケーリングでなんとかなりました……。なんで……？ LLLのこと何もわかりません[\*3](#f-590caef4 "まあなんか[tex: a_ip + a_jp = 0]となるようにうまく選んで打ち消してるんだと思う")。

下のプログラムで![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)が求まります。あとはCommon Modulus Attackをやるだけなので省略。ptrlibでできます。

```
import ast

f = open("output.txt")
es = ast.literal_eval(f.readline())
cs = ast.literal_eval(f.readline())

K = 2**1024
M = matrix(QQ, len(es), len(es)+1)
M.set_block(0, 0, matrix(QQ, len(es), 1, [e + K for e in es]) * K)
M.set_block(0, 1, matrix.identity(len(es)))

L = M.LLL()
S = product(int(c)**r for c, r in zip(cs, L[0][1:]))
T = product(int(c)**r for c, r in zip(cs, L[1][1:]))
t2 = cputime()

r = gcd(S.numerator() - S.denominator(), T.numerator() - T.denominator())
print(r)
```

## Superprime

```
from Crypto.Util.number import getPrime, isPrime, bytes_to_long

def getSuperPrime(nbits):
    while True:
        p = getPrime(nbits)
        pp = bytes_to_long(str(p).encode())
        if isPrime(pp):
            return p, pp

p1, q1 = getSuperPrime(512)
p2, q2 = getSuperPrime(512)
p3, q3 = getSuperPrime(512)
p4, q4 = getSuperPrime(512)
p5, q5 = getSuperPrime(512)

n1 = p1 * q1
n2 = p2 * p3
n3 = q2 * q3
n4 = p4 * q5
n5 = p5 * q4

e = 65537
c = bytes_to_long(open("flag.txt", "rb").read().strip())
for n in sorted([n1, n2, n3, n4, n5]):
    c = pow(c, e, n)

print(f"{n1 = }")
print(f"{n2 = }")
print(f"{n3 = }")
print(f"{n4 = }")
print(f"{n5 = }")
print(f"{e = }")
print(f"{c = }")
```

5重の[RSA](http://d.hatena.ne.jp/keyword/RSA)ですが[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)の生成が特殊で、[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)![ p_i](https://chart.apis.google...