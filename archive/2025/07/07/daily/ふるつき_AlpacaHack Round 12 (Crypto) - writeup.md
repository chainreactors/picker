---
title: AlpacaHack Round 12 (Crypto) - writeup
url: https://furutsuki.hatenablog.com/entry/2025/07/06/234110
source: ふるつき
date: 2025-07-07
fetch_date: 2025-10-06T23:24:53.978466
---

# AlpacaHack Round 12 (Crypto) - writeup

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_source=blogs_topright_button&utm_campaign=subscribe_blog)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2025-07-06](https://furutsuki.hatenablog.com/archive/2025/07/06)

# [AlpacaHack Round 12 (Crypto) - writeup](https://furutsuki.hatenablog.com/entry/2025/07/06/234110)

* [RSARSARSARSARSARSA](#RSARSARSARSARSARSA)
* [OTEC](#OTEC)
* [Flag Sharing](#Flag-Sharing)
* [Zero-sum game](#Zero-sum-game)
* [全体を通しての感想](#全体を通しての感想)

こんにちは。今日はAlpacaHack Round 12 (Crypto)でした。

AlpacaHackは6時間4問の[個人戦](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C4%BF%EF%BF%BD%EF%BF%BD%EF%BF%BD)CTFを[不定](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)期で開催しているCTFプラットフォームです。程よいボリュームであること、毎回良質な問題が提供されることから今一番贔屓にしています。

今回は[yu212](https://twitter.com/Yu_212_MC) さんによるCrypto回で、私はCTFではCryptoが特に好きなので参加して、4問中3問を解いて7位でした。目標は4時間[\*1](#f-7eabfdcb "競技自体は大体12:00 - 18:00JSTで6時間ありますが、寝坊したので4時間です")で4問のつもりだったのに実際は3問と及ばず残念ですが、せっかくなのでwriteupです。今回は個人的にははじめて問題に取り組む中でAIサービスをうまく使うことができたので、何をAIに助けてもらったのか、なども記録します。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20250706/20250706210929.png)

### RSARSARSARSARSARSA

問題は非常にシンプルです。

```
from math import gcd
import os
from Crypto.Util.number import getPrime, bytes_to_long

e = 19
while True:
    p = getPrime(2048)
    q = getPrime(2048)
    if gcd((p - 1) * (q - 1), e) == 1:
        break
n = p * q

flag = os.environ.get("FLAG", "Alpaca{**** REDACTED ****}")
assert len(flag) == 26 and flag.startswith("Alpaca{") and flag.endswith("}")

m = bytes_to_long((flag * 1337).encode())
c = pow(m, e, n)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
```

[RSA](https://d.hatena.ne.jp/keyword/RSA)の問題で、以下の要素があります。

* ![ e=19](https://chart.apis.google.com/chart?cht=tx&chl=%20e%3D19)
* フラグの長さが26文字であることが示されており、そのうち8文字は明らかになっている
* 暗号化されている平文はフラグ文字列を1337回繰り返したものであり、![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)より非常に大きい

![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)が小さいことで素朴に![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)乗根をとるアプローチや、![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)乗を含む[多項式](https://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)の根を求めるアプローチを想像します。今回は平文が大きいので前者のアプローチは棄却しました。

一方、後者のアプローチは平文の構造がわかっていることもあり有力と感じました。
[RSAで一部の値がわかっている時 - crypto-writeup-public](https://crypto-writeup-public.hatenablog.com/entry/RSA%E3%81%A7%E4%B8%80%E9%83%A8%E3%81%AE%E5%80%A4%E3%81%8C%E3%82%8F%E3%81%8B%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E6%99%82)の「eが小さく、mの大部分がわかっている時」のアプローチですね。

素朴に平文をエミュレートしてやればよく、flagは未知部分を![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)と置いて`prefix*256^19 + x*256 + suffix` と書けますから、あとはこれを1337回繰り返すようにして![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)乗すれば![ c](https://chart.apis.google.com/chart?cht=tx&chl=%20c)相当の式になります。結局![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)に関する19次の式に落ち着くので、Coppersmith法で解けます。

こういう感じですね

```
f = open("output.txt")

n = int(f.readline().strip().split(" = ")[1])
e = int(f.readline().strip().split(" = ")[1])
c = int(f.readline().strip().split(" = ")[1])

prefix = int(b"Alpaca{".hex(), 16)
suffix = int(b"}".hex(), 16)

PR.<x> = PolynomialRing(Zmod(n))
f = 0
for _ in range(1337):
    f = f*256**26 + (prefix*256**19 + x*256 + suffix)
f = (f**e - c).monic()

roots = f.small_roots(X=256**18, beta=0.5)
flag = b"Alpaca{" + int(roots[0]).to_bytes(18, "big") + b"}"
print(flag)
```

……というのはCTF終了後だからいえることで、なんか競技中はバグらせまくって大苦戦しました。素朴に筋肉が衰えていたのだと思いますが……。

↑の方針を立てたは良いのですが、なんか実装をミスって![ f](https://chart.apis.google.com/chart?cht=tx&chl=%20f)が ![ 19*1337](https://chart.apis.google.com/chart?cht=tx&chl=%2019%2A1337)次になって困り果て、AIに聞きまくったところ、3回目くらいで以下のようなコードを出してくれました。式をmonicにして、Coppersmith法のパラメータを調整するところだけ人間がやったら解けるところまでできていたので、本番はそれで解きました。

```
# bytes_to_long の結合ロジックを考慮
# b"Alpaca{" (7バイト) + x (18バイト) + b"}" (1バイト)
# x は下位19バイト目から下位2バイト目までを占める
# (R**len(suffix_bytes)) は x が左に suffix_bytes の長さ分シフトされる
# (R**(unknown_len + len(suffix_bytes))) は prefix が左に unknown_len + len(suffix_bytes) の長さ分シフトされる
long_flag_poly = prefix_val_part * (R**(unknown_len + len(suffix_bytes))) + \
                 x * (R**len(suffix_bytes)) + \
                 suffix_val_part

# 繰り返し部分の乗数 S を計算
# pow(R, flag_len * 1337) は非常に大きくなるので注意
S = (pow(R, flag_len * 1337) - 1) // (pow(R, flag_len) - 1)

# 平文 m の多項式
m_poly = long_flag_poly * S

# Coppersmith's Attack に渡す多項式
# f(x) = m_poly^e - c
f_poly = m_poly^e - c
```

まだ微妙にこの立式のことを理解してないのですが、やってることは同じなはず。なんか![ S](https://chart.apis.google.com/chart?cht=tx&chl=%20S)は[等比数列](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の和らしいです。私が`for`でやってることを数学的にまとめるとこうなるんでしょうね。

### OTEC

こちらもシンプルな問題です

```
import os
import signal
import secrets
from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes

signal.alarm(60)

flag = os.environ.get("FLAG", "Alpaca{**** REDACTED ****}").encode()

# Oblivious Transfer using Elliptic Curves
G = secp256k1.G
a = secrets.randbelow(secp256k1.q)
A = a * G

print(f"{A.x = }")
print(f"{A.y = }")

x, y = map(int, input("B> ").split(","))
B = Point(x, y, secp256k1)

k0 = long_to_bytes((a * B).x, 32)
k1 = long_to_bytes((a * (B - A)).x, 32)

def encrypt(message, key):
    return AES.new(key, AES.MODE_ECB).encrypt(pad(message, 16))

print(encrypt(flag[0::3], k0).hex())
print(encrypt(flag[1::3], k1).hex())
print(encrypt(flag[2::3], bytes(c0 ^ c1 for c0, c1 in zip(k0, k1))).hex())
```

[楕円曲線](https://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)を用いた紛失通信(Obilivious Transfer)が実装されています。紛失通信というのは送信者がn種類の値を暗号化して送り、受信者がそのうちのどれか1つのみを復号可能であって、送信者や他者からはどちらを復号できたかは不明、という性質をもつ[プロトコル](https://d.hatena.ne.jp/keyword/%EF%BF%BD%D7%A5%EF%BF%BD%EF%BF%BD%C8%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)です。そして、CTFでは大体受信者となって、なんとかしてすべての値を復号せよ、という問題が出題されます。

今回の問題では以下のような流れになっています。

1. 送信者が![ A = aG](https://chart.apis.google.com/chart?cht=tx&chl=%20A%20%3D%20aG)を計算して![ A](https://chart.apis.google.com/chart?cht=tx&chl=%20A)を渡してくれるので
2. 受信者は適当に![ b](https://chart.apis.google.com/chart?cht=tx&chl=%20b)を決めて![ B = bG](https://chart.apis.google.com/chart?cht=tx&chl=%20B%20%3D%20bG)を送ると
3. 送信者が![ aB](https://chart.apis.google.com/chart?cht=tx&chl=%20aB), ![ a(B - A)](https://chart.apis.google.com/chart?cht=tx&chl=%20a%28B%20-%20A%29)を計算し、それぞれのx座標を![ k_0, k_1](https://chart.apis.google.com/chart?cht=tx&chl=%20k_0%2C%20k_1)として
4. ![ k_0, k_1](https://chart.apis.google.com/chart?cht=tx&chl=%20k_0%2C%20k_1)および![ k_0 \oplus k_1](https://chart.apis.google.com/chart?cht=tx&chl=%20k_0%20%5Coplus%20k_1)を鍵として3種類の暗号文を送る

とりあえずこういう問題がでたら、とりあえず素朴にやって値1つを復号できることを確認します。

今回の場合は本当に適当な![ b](https://chart.apis.google.com/chart?cht=tx&chl=%20b)を選ぶと、![ k_0](https://chart.apis.google.com/chart?cht=tx&chl=%20k_0)の導出に使われる![ aB](https://chart.apis.google.com/chart?cht=tx&chl=%20aB)は![ aB = abG = baG = bA](https://chart.apis.google.com/chart?cht=tx&chl=%20aB%20%3D%20abG%20%3D%20baG%20%3D%20bA)と変形できるので受信者側で計算できて、![ k_0](https://chart.apis.google.com/chart?cht=tx&chl=%20k_0)で暗号化されている値が復号できます。一方このとき![ k_1](https://chart.apis.google.com/chart?cht=tx&chl=%20k_1)は![ a(B - A) = abG - aA = baG - aA = bA - aA](https://chart.apis.google.com/chart?cht=tx&chl=%20a%28B%20-%20A%29%20%3D%20abG%20-%20aA%20%3D%20baG%20-%20aA%20%3D%20bA%20-%20aA)から算出されますが、![ a](https://chart.apis.google.com/chart?cht=tx&chl=%20a)がわからないので![ aA](https://chart.apis.google.com/chart?cht=tx&chl=%20aA)は計算できず求められません。

![ k_1](https://chart.apis.google.com/chart?cht=tx&chl=%20k_1)を求めたい場...