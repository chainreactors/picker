---
title: HackTM CTF Quals 2023 writeup - d-phi-enc
url: https://furutsuki.hatenablog.com/entry/2023/02/20/141311
source: ふるつき
date: 2023-02-21
fetch_date: 2025-10-04T07:36:51.451652
---

# HackTM CTF Quals 2023 writeup - d-phi-enc

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2023-02-20](https://furutsuki.hatenablog.com/archive/2023/02/20)

# [HackTM CTF Quals 2023 writeup - d-phi-enc](https://furutsuki.hatenablog.com/entry/2023/02/20/141311)

HackTM CTF Quals 2023 に参加していました。今年の運営はあの[y011d4](https://twitter.com/y011d4/)さんが所属するWreckTheLineということで期待していましたが、想像を超える質と難易度のCrypto問題セットでした。

私はぼこぼこにされて全然解けませんでした。得意技であるところのFranklin-Reiter's related message attackとか、[グレブナー基底](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D6%A5%CA%A1%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)やresultantを使って式を整理する技が活躍する問題でちゃんと技を発動できなかったのが悔やまれます。

唯一解けたd-phi-encも得意技が使えればもっとスマートに解けていそうでしたが、なんか力技で解いてしまったのでそのwriteupです。

* [問題概要](#問題概要)
* [近似パート](#近似パート)
* [立式パート](#立式パート)
* [solver](#solver)
* [感想](#感想)

## 問題概要

問題はすでに以下の[リポジトリ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%DD%A5%EF%BF%BD%EF%BF%BD%C8%A5%EF%BF%BD)で公開されていますが、改めて掲載するとこういう感じです。

[github.com](https://github.com/y011d4/my-ctf-challenges/tree/main/2023-HackTMCTF-2023/crypto/d-phi-enc)

```
from Crypto.Util.number import bytes_to_long, getStrongPrime

from secret import flag

assert len(flag) == 255
e = 3
p = getStrongPrime(1024, e=e)
q = getStrongPrime(1024, e=e)
n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
enc_d = pow(d, e, n)
enc_phi = pow(phi, e, n)
enc_flag = pow(bytes_to_long(flag), e, n)
print(f"{n = }")
print(f"{enc_d = }")
print(f"{enc_phi = }")
print(f"{enc_flag = }")
```

![ e=3](https://chart.apis.google.com/chart?cht=tx&chl=%20e%3D3)の[RSA](http://d.hatena.ne.jp/keyword/RSA)で、![ d, \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20d%2C%20%5Cphi)を暗号化したものが一緒に与えられている点がユニークです。初見の感想は「へーこれ解けるの」でした[\*1](#f-53363862 "だいたいこういうことを言っているときはこういう問題設定が解けることに感動しています")。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230220/20230220131440.png)

![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)

## 近似パート

とりあえず![ k=2](https://chart.apis.google.com/chart?cht=tx&chl=%20k%3D2)を決め打ってしまいます。![ ed = 1 + k\phi](https://chart.apis.google.com/chart?cht=tx&chl=%20ed%20%3D%201%20%2B%20k%5Cphi)にわかっている値を代入すると![ 3d = 1 + 2\phi](https://chart.apis.google.com/chart?cht=tx&chl=%203d%20%3D%201%20%2B%202%5Cphi)です。![ \phi = n - (p + q) + 1](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%20%3D%20n%20-%20%28p%20%2B%20q%29%20%2B%201)で、ごく大雑把に![ \phi \approx n](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%20%5Capprox%20n)と思うと![ d \approx \frac{2n}{3} + 1](https://chart.apis.google.com/chart?cht=tx&chl=%20d%20%5Capprox%20%5Cfrac%7B2n%7D%7B3%7D%20%2B%201)です。![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)の![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)との差は![ p + q](https://chart.apis.google.com/chart?cht=tx&chl=%20p%20%2B%20q)の約1024bitですから、![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)は上位1000bitくらいが一致し、下位![ 1024](https://chart.apis.google.com/chart?cht=tx&chl=%201024)bit程度が不明な近似になっています。もうちょっと頑張れば大体![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)の半分以下のサイズと言えるのでCoppersmithなどで![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)を求めることができそうです

もうちょっと頑張るパートは全探索ってやつをやります

## 立式パート

![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)の上位bitがわかっているといえば[pbctf2020 | Special Gift](https://scrapbox.io/crypto-writeup-public/pbctf2020_%7C_Special_Gift)ですが、今回は![ e](https://chart.apis.google.com/chart?cht=tx&chl=%20e)が小さいので![ \mod e](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cmod%20e)の式で解くことは難しそうです。![ s = p + q](https://chart.apis.google.com/chart?cht=tx&chl=%20s%20%3D%20p%20%2B%20q)とおいて![ e(d' + \alpha) \equiv 1 + 2*(-s + 1) \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20e%28d%27%20%2B%20%5Calpha%29%20%5Cequiv%201%20%2B%202%2A%28-s%20%2B%201%29%20%5Cmod%20n)のmultivariate coppersmithはできるか怪しいです。

そこで今回は与えられている![ E(d) = d^3 \pmod n, E(\phi) = \phi^3 \pmod n](https://chart.apis.google.com/chart?cht=tx&chl=%20E%28d%29%20%3D%20d%5E3%20%5Cpmod%20n%2C%20E%28%5Cphi%29%20%3D%20%5Cphi%5E3%20%5Cpmod%20n)を使います。

![ ed - 1 = 2\phi](https://chart.apis.google.com/chart?cht=tx&chl=%20ed%20-%201%20%3D%202%5Cphi)を全部![ e=3](https://chart.apis.google.com/chart?cht=tx&chl=%20e%3D3)の[RSA](http://d.hatena.ne.jp/keyword/RSA)で暗号化したと思うと![ 27E(d) - 27d^2 + 9d - 1 \equiv 8E(\phi) \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%2027E%28d%29%20-%2027d%5E2%20%2B%209d%20-%201%20%5Cequiv%208E%28%5Cphi%29%20%5Cmod%20n)です。この式では未知数は![ d](https://chart.apis.google.com/chart?cht=tx&chl=%20d)だけなので、先ほどの近似を使えば![ d = d' + \alpha](https://chart.apis.google.com/chart?cht=tx&chl=%20d%20%3D%20d%27%20%2B%20%5Calpha) とかいて1024bit未満の未知数![ \alpha](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Calpha)はCoppersmith's methodで求められそうです。

## solver

```
from Crypto.Util.number import bytes_to_long, getStrongPrime
from tqdm import tqdm

e = 3
n = ...
enc_d = ...
enc_phi = ...
enc_flag = ..

tt = n // 3
d_ = 2*tt + 1
unknown_bits = 1025
guess_size = 10
known_d = (d_ >> unknown_bits) << unknown_bits

PR.<lower_d> = PolynomialRing(Zmod(n))

for a in tqdm(range(2**guess_size)):
    d = known_d + (a << (unknown_bits - guess_size)) + lower_d
    f = (8*enc_phi - 27*enc_d) - (-27*d**2 + 9*d - 1)
    f = f.monic()

    roots = f.small_roots(X=2**(unknown_bits - guess_size), beta=1, epsilon=1/7)
    if len(roots):
        d = known_d + (a << (unknown_bits - guess_size)) + roots[0]
        m = pow(enc_flag, d, n)
        print(bytes.fromhex(hex(m)[2:]))
```

## 感想

なんでこんなゴリ押ししてしまったんや……。解けてよかったです

[\*1](#fn-53363862):だいたいこういうことを言っているときはこういう問題設定が解けることに感動しています

[\*2](#fn-b4df5fff):今思うとここまで考えて![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)に関するFranklin-Reiterに辿り着かないことあるんだ……という感じですね

Furutsuki
[2023-02-20 14:13](https://furutsuki.hatenablog.com/entry/2023/02/20/141311)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_medium=button&utm_source=blogs_entry_footer)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2023/02/20/141311 "この記事をはてなブックマークに追加")

関連記事

* [![CPCTF 2024 writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "CPCTF 2024 writeup")](https://furutsuki.hatenablog.com/entry/2024/04/21/180019)

  [2024-04-21](https://furutsuki.hatenablog.com/archive/2024/04/21)

  [CPCTF 2024 writeup](https://furutsuki.hatenablog.com/entry/2024/04/21/180019)

  久しぶりにCTFに参加しました。cryptoのある程度以上の難易度の…
* [![ACTF 2022 writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "ACTF 2022 writeup")](https://furutsuki.hatenablog.com/entry/2022/06/28/001931)

  [2022-06-28](https://furutsuki.hatenablog.com/archive/2022/06/28)

  [ACTF 2022 writeup](https://furutsuki.hatenablog.com/entry/2022/06/28/001931)

  zer0pts で ACTF に出たのでwriteupです。真面目に取り組んで8…
* [![TSG Live!8 CTF writeup - Two Keys](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "TSG Live!8 CTF writeup - Two Keys")](https://furutsuki.hatenablog.com/entry/2022/05/14/154346)

  [2022-05-14]...