---
title: yoshi-camp 2022 winter参加記【Day 2-3】
url: https://ptr-yudai.hatenablog.com/entry/2023/03/11/233340
source: CTFするぞ
date: 2023-03-12
fetch_date: 2025-10-04T09:19:41.737267
---

# yoshi-camp 2022 winter参加記【Day 2-3】

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2023-03-11](https://ptr-yudai.hatenablog.com/archive/2023/03/11)

# [yoshi-camp 2022 winter参加記【Day 2-3】](https://ptr-yudai.hatenablog.com/entry/2023/03/11/233340)

[勉強会](https://ptr-yudai.hatenablog.com/archive/category/%E5%8B%89%E5%BC%B7%E4%BC%9A)

# はじめに

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

# yoshi-camp

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
![ \psi_{1} = 1](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B1%7D%20%3D%201)
![ \psi_{2} = 2y](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B2%7D%20%3D%202y)
![ \psi_{3} = 3x^{4} + 6ax^{2} + 12bx - a^{2}](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B3%7D%20%3D%203x%5E%7B4%7D%20%2B%206ax%5E%7B2%7D%20%2B%2012bx%20-%20a%5E%7B2%7D)
![ \psi_{4} = 4y(x^{6} + 5ax^{4} + 20bx^{3} - 5a^{2}x^{2} - 4abx - 8b^{2} - a^{3})](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B4%7D%20%3D%204y%28x%5E%7B6%7D%20%2B%205ax%5E%7B4%7D%20%2B%2020bx%5E%7B3%7D%20-%205a%5E%7B2%7Dx%5E%7B2%7D%20-%204abx%20-%208b%5E%7B2%7D%20-%20a%5E%7B3%7D%29)
![ \psi_{2m+1} = \psi_{m+2}\psi_{m}^{3} - \psi_{m-1}\psi_{m+1}^{3} \ \ \ \ (m \geq 2)](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B2m%2B1%7D%20%3D%20%5Cpsi_%7Bm%2B2%7D%5Cpsi_%7Bm%7D%5E%7B3%7D%20-%20%5Cpsi_%7Bm-1%7D%5Cpsi_%7Bm%2B1%7D%5E%7B3%7D%20%5C%20%5C%20%5C%20%5C%20%28m%20%5Cgeq%202%29)
![ \psi_{2m} = \cfrac{\psi_{m}}{2y}(\psi_{m+2}\psi_{m-1}^{2} - \psi_{m-2}\psi_{m+1}^{2}) \ \ \ \ (m \geq 3)](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cpsi_%7B2m%7D%20%3D%20%5Ccfrac%7B%5Cpsi_%7Bm%7D%7D%7B2y%7D%28%5Cpsi_%7Bm%2B2%7D%5Cpsi_%7Bm-1%7D%5E%7B2%7D%20-%20%5Cpsi_%7Bm-2%7D%5Cpsi_%7Bm%2B1%7D%5E%7B2%7D%29%20%5C%20%5C%20%5C%20%5C%20%28m%20%5Cgeq%203%29)

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
    elif m == ...