---
title: SECCON Beginners CTF 2025 writeup
url: https://furutsuki.hatenablog.com/entry/2025/07/27/223211
source: ふるつき
date: 2025-07-28
fetch_date: 2025-10-06T23:16:38.267869
---

# SECCON Beginners CTF 2025 writeup

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2025-07-27](https://furutsuki.hatenablog.com/archive/2025/07/27)

# [SECCON Beginners CTF 2025 writeup](https://furutsuki.hatenablog.com/entry/2025/07/27/223211)

SECCON Beginners CTF 2025のCrypto問題のwriteupです。

* [seesaw](#seesaw)
* [01-Translator](#01-Translator)
* [elliptic4b](#elliptic4b)
* [Golden Ticket](#Golden-Ticket)
* [mathmyth](#mathmyth)

## seesaw

```
import os
from Crypto.Util.number import getPrime

FLAG = os.getenv("FLAG", "ctf4b{dummy_flag}").encode()
m = int.from_bytes(FLAG, 'big')

p = getPrime(512)
q = getPrime(16)
n = p * q
e = 65537
c = pow(m, e, n)

print(f"{n = }")
print(f"{c = }")
```

qが16bit程度しかないので[素因数分解](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%B0%EF%BF%BD%EF%BF%BD%EF%BF%BD%CA%AC%EF%BF%BD%EF%BF%BD)できます。↓のscriptではlimit書いてるけどいらないと思う

```
f = open("output.txt")

n = int(f.readline().strip().split(" = ")[1])
c = int(f.readline().strip().split(" = ")[1])

((p, _), (q, _)) = factor(n, limit=2**17)
d = pow(65537, -1, (p-1)*(q-1))
m = pow(c, d, n)

print(bytes.fromhex(hex(m)[2:]))
```

## 01-Translator

```
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), 16))

flag = os.environ.get("FLAG", "CTF{dummy_flag}")
flag_bin = f"{bytes_to_long(flag.encode()):b}"
trans_0 = input("translations for 0> ")
trans_1 = input("translations for 1> ")
flag_translated = flag_bin.translate(str.maketrans({"0": trans_0, "1": trans_1}))
key = os.urandom(16)
print("ct:", encrypt(flag_translated, key).hex())
```

フラグがサーバ側でバイナリ文字列に変換されたあと、更にユーザの入力に応じて`0` `1` をそれぞれ好きな文字列に置換できます。その後置換後の文字列をAESのECBモードで暗号化されたものが渡されます。

ECBモードをみると、同じ平文ブロックを暗号化すると同じ暗号文になるという性質を思い出すので、これを利用したくなります。具体的には`0`, `1` をそれぞれ適当な1ブロックに置換すると、暗号文全体は`0` を暗号化したブロックと`1`を暗号化したブロックからなり、その2種類だけ[\*1](#f-c4c83c11 "厳密には末尾にパディングブロック")となるので平文を復元できます。

```
from ptrlib import Socket, chunks

# sock = Socket("nc localhost 9999")
sock = Socket("nc 01-translator.challenges.beginners.seccon.jp 9999")

sock.sendlineafter("0> ", "0" * 16)
sock.sendlineafter("1> ", "1" * 16)

ct = sock.recvlineafter("ct:").decode().strip()
cs = chunks(ct, 32)

flag = 0
for c in cs[:-1]:  # last block is padding
    if c == cs[0]:
        flag = flag*2 + 1
    else:
        flag = flag*2
print(bin(flag))
print(bytes.fromhex(hex(flag)[2:]))
```

## elliptic4b

```
import os
import secrets
from fastecdsa.curve import secp256k1
from fastecdsa.point import Point

flag = os.environ.get("FLAG", "CTF{dummy_flag}")
y = secrets.randbelow(secp256k1.p)
print(f"{y = }")
x = int(input("x = "))
if not secp256k1.is_point_on_curve((x, y)):
    print("// Not on curve!")
    exit(1)
a = int(input("a = "))
P = Point(x, y, secp256k1)
Q = a * P
if a < 0:
    print("// a must be non-negative!")
    exit(1)
if P.x != Q.x:
    print("// x-coordinates do not match!")
    exit(1)
if P.y == Q.y:
    print("// P and Q are the same point!")
    exit(1)
print("flag =", flag)
```

ランダムな![ y](https://chart.apis.google.com/chart?cht=tx&chl=%20y)が渡されて、![ P = (x, y)](https://chart.apis.google.com/chart?cht=tx&chl=%20P%20%3D%20%28x%2C%20y%29)がsecp256k1 上の点になるように![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)を渡した後、![ Q = aP](https://chart.apis.google.com/chart?cht=tx&chl=%20Q%20%3D%20aP)が![ P](https://chart.apis.google.com/chart?cht=tx&chl=%20P)と異なる![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)座標を持ち、![ P](https://chart.apis.google.com/chart?cht=tx&chl=%20P)と同じ![ y](https://chart.apis.google.com/chart?cht=tx&chl=%20y)座標をもつように![ a](https://chart.apis.google.com/chart?cht=tx&chl=%20a)をうまく選べれば勝ち、となります。

まず![ y](https://chart.apis.google.com/chart?cht=tx&chl=%20y)座標から![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)座標を求める必要がありますが、これは[楕円曲線](https://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の式![ y^2 \equiv x^3 + ax + b \mod p](https://chart.apis.google.com/chart?cht=tx&chl=%20y%5E2%20%5Cequiv%20x%5E3%20%2B%20ax%20%2B%20b%20%5Cmod%20p)を満たすように式に![ a, b, y](https://chart.apis.google.com/chart?cht=tx&chl=%20a%2C%20b%2C%20y)を代入して![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)を求めればよいです。

続いていい![ a](https://chart.apis.google.com/chart?cht=tx&chl=%20a)を求めます。まずそもそも同一の[楕円曲線](https://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)上にy座標が同じでx座標が異なる2つの点が存在するのか、という話ですが、存在します。平面座標上での[楕円曲線](https://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の形を思い出すと![ P](https://chart.apis.google.com/chart?cht=tx&chl=%20P)と![ -P](https://chart.apis.google.com/chart?cht=tx&chl=%20-P)がまさにそういう点ですね。もはや常識。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20250727/20250727210338.png)

ということは![ a = -1](https://chart.apis.google.com/chart?cht=tx&chl=%20a%20%3D%20-1)

```
from ptrlib import Socket

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
K = GF(p)
a = K(0x0000000000000000000000000000000000000000000000000000000000000000)
b = K(0x0000000000000000000000000000000000000000000000000000000000000007)
E = EllipticCurve(K, (a, b))
G = E(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
E.set_order(0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 * 0x1)

PR.<x> = PolynomialRing(K)

while True:
    # sock = Socket("nc localhost 9999")
    sock = Socket("nc elliptic4b.challenges.beginners.seccon.jp 9999")
    y = int(sock.recvlineafter("y = "))
    f = y**2 - (x**3 + a*x + b)
    roots = f.roots()
    if len(roots) != 0:
        break

x = roots[0][0]
G1 = E((x, y))

inv = Zmod(E.order())(-1)
G2 = inv *G1
assert G1[0] == G2[0]

sock.sendlineafter("x = ", str(x))
sock.sendlineafter("a = ", str(inv))
sock.interactive()
```

## Golden Ticket

問題の[スクリプト](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)はやや長いので省略。encryption ticketを利用すると`Enc(key, iv, input || pad)` がえられるオ[ラク](https://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルが利用でき、decryption ticketを利用すると`Dec(key, iv, input || pad)`が得られるオ[ラク](https://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルが利用できます。`Enc`, `Dec` AES-[CBC](https://d.hatena.ne.jp/keyword/CBC)による暗号化・復号で、どちらも`input` は16バイト（1ブロック）までで、それぞれ3回まで利用できます。

目的は 6ブロックのランダムな文字列 challenge に対して、`Dec(key, iv', payload) == challenge` となるような `iv'`, `payload` を求めることです。

まずは`iv`を求めます。ここで2回オ[ラク](https://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルを使う方法を考えていて時間を溶かしていたけど、`input == pad`となるようにinputを決めて（つまり `input = 0x10101010...10`）decryption ticketを利用すると、1ブロック目は `0x1010...10` をAESで復号したものに`IV`をXORした値、2ブロック目は `0x1010...10` をAESで復号したものに1ブロック目の平文、`0x1010...10` をXORした値、となります。

ここからは![ Enc, Dec](https://chart.apis.google.com/chart?cht=tx&chl=%20Enc%2C%20Dec)はAESによる1ブロックのみの暗号化を表すことにすると、1ブロック目は![ Dec(0x1010...10) \oplus IV](https://chart.apis.google.com/chart?cht=tx&chl=%20Dec%280x1010...10%29%20%5Coplus%20IV)、2ブロック目は![ Dec(0x1010...10) \oplus 0x1010...10](https://chart.apis.google.com/chart?cht=tx&chl=%20Dec%280x1010...10%29%20%5Coplus%200x1010...10) となります。2ブロック目の結果から![ Dec(0x1010...10)](https://chart.apis.google.com/chart?cht=tx&chl=%20Dec%280x1010...10%29)がわかるので、1ブロック目の結果にXORすると![ IV](https://chart.apis.google.com/chart?cht=tx&chl=%20IV)が手に入ります。

![ IV](https://chart.apis.google.com/chart?cht=tx&chl=%20IV)がわかったので、これを利用してencryption ticketやdecryption ticketを利用すると何ができるかを考えます。encryp...