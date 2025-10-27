---
title: secure Prime Generator writeup - Codegate CTF 2023 Preliminary
url: https://buaq.net/go-169886.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:24.624697
---

# secure Prime Generator writeup - Codegate CTF 2023 Preliminary

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

secure Prime Generator writeup - Codegate CTF 2023 Preliminary

サーバ側で何やら素数（？）を2つ生成
*2023-6-22 23:36:40
Author: [furutsuki.hatenablog.com(查看原文)](/jump-169886.htm)
阅读量:46
收藏*

---

サーバ側で何やら[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)（？）を2つ生成して、さらにそれを加工した値をあたかも[RSA](https://d.hatena.ne.jp/keyword/RSA)の![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)

validity checkに答えるのがなかなか難しくて、これを通過できないとだめなので、どうにかして![ p_1, q_1](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%2C%20q_1)の具体的な値を知る必要がありそうです。まず最初に考えたのは![ X_0](https://chart.apis.google.com/chart?cht=tx&chl=%20X_0)として![ p_1^{e_s}](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%5E%7Be_s%7D)を送り![ N = p_1 (q_1 + 1)](https://chart.apis.google.com/chart?cht=tx&chl=%20N%20%3D%20p_1%20%28q_1%20%2B%201%29)をもらって![ (q_1 + 1)^{e_s} \mod N_s](https://chart.apis.google.com/chart?cht=tx&chl=%20%28q_1%20%2B%201%29%5E%7Be_s%7D%20%5Cmod%20N_s)と![ q_1^{e_s} \mod N_s](https://chart.apis.google.com/chart?cht=tx&chl=%20q_1%5E%7Be_s%7D%20%5Cmod%20N_s)から![ q_1](https://chart.apis.google.com/chart?cht=tx&chl=%20q_1)を求める方法でしたが、これは[多項式](https://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)のGCDが[タイムアウト](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%E0%A5%A2%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)に微妙に届かなかったので不採用になりました。

次に考えたのは![ X_0](https://chart.apis.google.com/chart?cht=tx&chl=%20X_0)として![ p_1^{4e_s}](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%5E%7B4e_s%7D)を送り![ N = p_1^4 + p_1q_1 = p_1(p_1^3 + q_1)](https://chart.apis.google.com/chart?cht=tx&chl=%20N%20%3D%20p_1%5E4%20%2B%20p_1q_1%20%3D%20p_1%28p_1%5E3%20%2B%20q_1%29)とする方法で、これは![ p_1 \approx N^{1/4}](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%20%5Capprox%20N%5E%7B1%2F4%7D)とする近似がうまく行きました。当然![ q_1](https://chart.apis.google.com/chart?cht=tx&chl=%20q_1)も計算できるし、validity checkも通過できます。

あとはこのmodulus で![ flag ^ {65537} \mod N](https://chart.apis.google.com/chart?cht=tx&chl=%20flag%20%5E%20%7B65537%7D%20%5Cmod%20N)が復号できれば良いので、![ p_1^3 + q_1](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%5E3%20%2B%20q_1)が[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)になるまでガチャを回しました。

solution scriptはこちら

```
from ptrlib import Socket, Process
from random import randrange
from Crypto.Util.number import long_to_bytes, isPrime
from hashlib import sha256
from itertools import product as iterprod
from gmpy2 import iroot

def POW(sock):
    b_postfix = sock.recvlineafter("b = ").decode()[6:].strip()
    h = sock.recvlineafter(" = ").decode().strip()
    for brute in iterprod('0123456789abcdef', repeat=6):
        b_prefix = ''.join(brute)
        b_ = b_prefix + b_postfix
        if sha256(bytes.fromhex(b_)).hexdigest() == h:
            sock.sendlineafter(b' > ', b_prefix.encode())
            return True

    assert 0, "Something went wrong.."

while True:
    try:

        sock = Socket("nc 43.200.47.102 9001")
        POW(sock)
        SERVER_N = int(sock.recvlineafter("SERVER_N = "))
        SERVER_E = int(sock.recvlineafter("SERVER_E = "))

        for p in [2,3,5,7,11,13]:
            cands = [1] + [-1-x for x in range((p + 1) // 2 - 1)]
            sock.sendlineafter(" > ", " ".join([str(x) for x in cands]))

        for p in [2,3,5,7,11,13]:
            if p == 2:
                cands = [0] + [-1-x for x in range((p + 1) // 2 - 1)]
            else:
                cands = [1] + [-1-x for x in range((p + 1) // 2 - 1)]
            sock.sendlineafter(" > ", " ".join([str(x) for x in cands]))

        p1_enc = int(sock.recvlineafter("p1_enc = "))
        q1_enc = int(sock.recvlineafter("q1_enc = "))
        r = randrange(2**1536)

        X = [ pow(p1_enc, 4, SERVER_N) ]
        sock.sendlineafter("X > ", " ".join([str(x) for x in X + [0 for _ in range(12  - len(X))]]))

        N = int(sock.recvlineafter("N = "))
        p, _ = iroot(N, 4)
        q = (N - p**4) // p

        assert pow(p, SERVER_E, SERVER_N) == p1_enc, "p"
        assert pow(q, SERVER_E, SERVER_N) == q1_enc, "q"
        assert N == p*(p**3 + q), "N"

        for _ in range(20):
            b = int(sock.recvlineafter("b = "))
            digest = sha256(long_to_bytes(pow(b, N - (p+q) + 1, N))).hexdigest()
            sock.sendlineafter("digest > ", digest)
            line = sock.recvline()
            assert b"good" in line

        c = int(sock.recvlineafter("FLAG_ENC = "))
        if isPrime(p**3 + q) and (p**3 + q) > 2**(127 * 8):
            print(p)
            print(q)
            print(N)
            print(c)

            d = pow(65537, -1, p**3 + q - 1)
            m = pow(c, d, p**3 + q)
            print(long_to_bytes(m))

            quit()
    except AssertionError as e:
        print(e)
        continue
```

![ p_1, q_1](https://chart.apis.google.com/chart?cht=tx&chl=%20p_1%2C%20q_1)が![ \mod 2,3,5,7,11,13](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cmod%202%2C3%2C5%2C7%2C11%2C13)で満たすべき値を制御できたのはなんの意味があったんだろう…

文章来源: https://furutsuki.hatenablog.com/entry/2023/06/23/003640
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)