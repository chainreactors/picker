---
title: yoshi-camp 2022 winter参加記【Day 2-3】
url: https://buaq.net/go-153022.html
source: unSafe.sh - 不安全
date: 2023-03-12
fetch_date: 2025-10-04T09:21:31.635096
---

# yoshi-camp 2022 winter参加記【Day 2-3】

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

![](https://8aqnet.cdn.bcebos.com/7aac10a034ed4c3804fe0b463540b47d.jpg)

yoshi-camp 2022 winter参加記【Day 2-3】

はてなブログ謎オラクルによるブロ
*2023-3-11 22:33:40
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-153022.htm)
阅读量:18
收藏*

---

[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)謎オ[ラク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルによるブログのスパム認定が解除されたので、yoshi-campの参加記続きを書いていきまーす。

Day 0とDay 1はこっち：

[ptr-yudai.hatenablog.com](https://ptr-yudai.hatenablog.com/entry/2022/12/13/235034)

* [はじめに](#はじめに)
* [yoshi-camp](#yoshi-camp)
  + [Day 2](#Day-2)
    - [[mitsu] ネコちゃん式　～安全な曲線の生成～](#mitsu-ネコちゃん式安全な曲線の生成)
      * [Frobenius写像とHasseの定理](#Frobenius写像とHasseの定理)
      * [等分多項式](#等分多項式)
      * [Schoofのアルゴリズム](#Schoofのアルゴリズム)
      * [実装の上での問題](#実装の上での問題)
      * [Schoofのアルゴリズムの実装](#Schoofのアルゴリズムの実装)
    - [[Xornet] Bilinyar Map in CTF](#Xornet-Bilinyar-Map-in-CTF)
      * [Weil Pairing](#Weil-Pairing)
      * [Tate Pairing](#Tate-Pairing)
      * [DDH問題](#DDH問題)
      * [MOV Attack](#MOV-Attack)
      * [BLS](#BLS)
      * [BLS12-381](#BLS12-381)
      * [実装パート](#実装パート)
    - [[ﾈｺﾁｬﾝ] Tornado Cats](#ﾈｺﾁｬﾝ-Tornado-Cats)
  + [Day 3](#Day-3)
    - [写真集](#写真集)
  + [おわりに](#おわりに)

## Day 2

### [mitsu] ネコちゃん式　～安全な曲線の生成～

yoshi-camp一番の鬼講師ことmitsu先生が今回も[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)についてお話してくれました。

タイトル通り安全な[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)を作る方法を考えるのですが、これは[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数を計算すると確認できます。
つまり、この講義では[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数を計算するためのSchoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)の原理と高速化についてお勉強しました。

#### Frobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)とHasseの定理

Hasseの定理は[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の本には必ずといっていいほど書いてある定理です。

![ |\# E(\mathbb{F}_p) - (p+1)| \leq 2\sqrt{p}](https://chart.apis.google.com/chart?cht=tx&chl=%20%7C%5C%23%20E%28%5Cmathbb%7BF%7D_p%29%20-%20%28p%2B1%29%7C%20%5Cleq%202%5Csqrt%7Bp%7D)

ここで、左辺の絶対値の中身はFrobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)という[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のトレースになっています。
Frobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)も有名ですが、次のように定義される[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のことです。

![ \phi: E(\mathbb{\bar{F}}_p) \ni (x, y) \mapsto (x^{p}, y^{p}) \in E(\mathbb{\bar{F}}_p)](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%3A%20E%28%5Cmathbb%7B%5Cbar%7BF%7D%7D_p%29%20%5Cni%20%28x%2C%20y%29%20%5Cmapsto%20%28x%5E%7Bp%7D%2C%20y%5E%7Bp%7D%29%20%5Cin%20E%28%5Cmathbb%7B%5Cbar%7BF%7D%7D_p%29)

[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数がFrobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のトレースから計算できるというのは、pwnerの私でも知っている話でした。
しかし、具体的にトレースをどう計算するかは一切知らなかったので、ここから新しい内容に入ります。

#### 等分[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)

Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)本体に入る前に、[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)で必要となる[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の等分[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)を計算します。
つまり、n-ねじれ点のx座標を根に持つ[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)を求めます。

[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)自体は簡単に求められます。
単純に[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の加算公式を使い、![ (m-1)P = P](https://chart.apis.google.com/chart?cht=tx&chl=%20%28m-1%29P%20%3D%20P) を計算して方程式が得られるからです。

簡単でも面倒なので、mitsuくんからの天啓を使ってみましょう。
[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ E/\mathbb{F}_{p}](https://chart.apis.google.com/chart?cht=tx&chl=%20E%2F%5Cmathbb%7BF%7D_%7Bp%7D)に付随する[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)![ \psi_{m}](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7Bm%7D)を計算して出来上がったものがこちらになります。

![ \psi_{0} = 0](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B0%7D%20%3D%200)

これ自体は等分[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)ではなく、等分[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)は、次のように![y](https://chart.apis.google.com/chart?cht=tx&chl=y)を消去した関数として定義されています。

![ f_{m} = 1 \ \ \ \ (m = 1)](https://chart.apis.google.com/chart?cht=tx&chl=%20f_%7Bm%7D%20%3D%201%20%5C%20%5C%20%5C%20%5C%20%28m%20%3D%201%29)
![ f_{m} = \psi_{m} \ \ \ \ (m \ \ \mathrm{is} \ \ \mathrm{odd})](https://chart.apis.google.com/chart?cht=tx&chl=%20f_%7Bm%7D%20%3D%20%5Cpsi_%7Bm%7D%20%5C%20%5C%20%5C%20%5C%20%28m%20%5C%20%5C%20%5Cmathrm%7Bis%7D%20%5C%20%5C%20%5Cmathrm%7Bodd%7D%29)
![ f_{m} = \cfrac{\psi_{m}}{\psi_{2}} \ \ \ \ (m \ \ \mathrm{is} \ \ \mathrm{even})](https://chart.apis.google.com/chart?cht=tx&chl=%20f_%7Bm%7D%20%3D%20%5Ccfrac%7B%5Cpsi_%7Bm%7D%7D%7B%5Cpsi_%7B2%7D%7D%20%5C%20%5C%20%5C%20%5C%20%28m%20%5C%20%5C%20%5Cmathrm%7Bis%7D%20%5C%20%5C%20%5Cmathrm%7Beven%7D%29)

![\psi, f_{m}](https://chart.apis.google.com/chart?cht=tx&chl=%5Cpsi%2C%20f_%7Bm%7D)の定義に照らしあわせると、![ f_{m}](https://chart.apis.google.com/chart?cht=tx&chl=%20f_%7Bm%7D)は[帰納](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%C7%BC)的に計算できます。実装してみましょう。

```
from functools import cache

@cache
def division_polynomial(E, m):
    f = lambda m: division_polynomial(E, m)
    a, b = E.a4(), E.a6()
    PR = PolynomialRing(E.base(), 'x')
    x = PR.gen()
    if m == 0:
        return PR(0)
    elif m == 1 or m == 2:
        return PR(1)
    elif m == 3:
        return 3*x^4 + 6*a*x^2 + 12*b*x - a^2
    elif m == 4:
        return 2*(x^6 + 5*a*x^4 + 20*b*x^3 - 5*a^2*x^2 - 4*a*b*x - 8*b^2 - a^3)
    elif m % 2 == 0:
        n = m // 2
        return (f(n+2)*f(n-1)^2 - f(n-2)*f(n+1)^2) * f(n)
    else:
        n = (m-1) // 2
        F = 4*(x^3 + a*x + b)
        if n % 2 == 1:
            return f(n+2)*f(n)^3 - F^2*f(n-1)*f(n+1)^3
        else:
            return F^2*f(n+2)*f(n)^3 - f(n-1)*f(n+1)^3
```

この関数で求めた方程式の根が、ねじれ点のx座標になっていることを確認します。

```
E = EllipticCurve(GF(13), [2, 3])
m = 9
f = division_polynomial(E, m)
print(f)

for x, _ in f.roots():
    try:
        P = E.lift_x(x)
        print(P, m*P)
    except ValueError:
        pass
```

結果：

```
9*x^40 + 8*x^38 + x^37 + 3*x^36 + 10*x^35 + 12*x^33 + 10*x^32 + 11*x^31 + 3*x^30 + 5*x^29 + 9*x^28 + 2*x^27 + x^26 + x^23 + 4*x^21 + 9*x^20 + 6*x^19 + 6*x^18 + 2*x^17 + 12*x^16 + 2*x^15 + 6*x^14 + 5*x^13 + 3*x^12 + 9*x^11 + 7*x^10 + 9*x^9 + 2*x^8 + 10*x^7 + 3*x^6 + 3*x^5 + x^4 + 4*x^3 + 11*x^2 + 6*x
(0 : 9 : 1) (0 : 1 : 0)
(11 : 2 : 1) (0 : 1 : 0)
(9 : 3 : 1) (0 : 1 : 0)
(3 : 7 : 1) (0 : 1 : 0)
```

できました！

#### Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)

Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)の本質は中国人剰余定理です。
Frobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のトレース![t](https://chart.apis.google.com/chart?cht=tx&chl=t)は、![p](https://chart.apis.google.com/chart?cht=tx&chl=p)未満の小さな[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)![l_{1}, l_{2}, \...