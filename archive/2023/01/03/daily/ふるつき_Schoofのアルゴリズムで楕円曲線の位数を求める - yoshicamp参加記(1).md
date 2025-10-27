---
title: Schoofのアルゴリズムで楕円曲線の位数を求める - yoshicamp参加記(1)
url: https://furutsuki.hatenablog.com/entry/2023/01/02/233804
source: ふるつき
date: 2023-01-03
fetch_date: 2025-10-04T02:54:38.632666
---

# Schoofのアルゴリズムで楕円曲線の位数を求める - yoshicamp参加記(1)

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_medium=button&utm_source=blogs_topright_button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2023-01-02](https://furutsuki.hatenablog.com/archive/2023/01/02)

# [Schoofのアルゴリズムで楕円曲線の位数を求める - yoshicamp参加記(1)](https://furutsuki.hatenablog.com/entry/2023/01/02/233804)

* [前回のyoshicamp!](#前回のyoshicamp)
* [2日目朝](#2日目朝)
* [Schoofのアルゴリズムを用いた楕円曲線の位数計算](#Schoofのアルゴリズムを用いた楕円曲線の位数計算)
  + [overview](#overview)
  + [tを求めるための立式](#tを求めるための立式)
  + [Schoofのアルゴリズム(l-torsion pointについて考えることで次数と探索範囲を減らしてあとでCRTする）](#Schoofのアルゴリズムl-torsion-pointについて考えることで次数と探索範囲を減らしてあとでCRTする)
  + [実装](#実装)
* [昼](#昼)
* [次回予告](#次回予告)

## 前回のyoshicamp!

./VespiaryからXornetさんとﾈｺﾁｬﾝを招き、例年以上の盛り上がりを見せるyoshicamp。[芦ノ湖](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%CE%B8%EF%BF%BD)を見下ろしながら始まったキャンプだったが、久々ということで気合が入っていたのか、私の同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)暗号の講義もptr-yudaiの量子の講義も時間内には終わらなかった！　コンビニのおかずと冷凍餃子を食べて[ボードゲーム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%DC%A1%EF%BF%BD%EF%BF%BD%C9%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を遊び1日目を終えて、2日目朝〜の講義はmitsuくんによる「ネコちゃん式-～安全な[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の生成～」です。

他の人のyoshicampレポートは <https://yoshicamp.zer0pts.com/> をご覧ください

## 2日目朝

前日結構ハードに体力を使った割にはそこそこ早起きできた。ptr-yudaiは先に起きていたっぽい。朝[ゴハン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%CF%A5%EF%BF%BD)のパンをかじりながら外を眺めていたら、[芦ノ湖](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%CE%B8%EF%BF%BD)の向こう側に富士山が見えることに気がついた。雲のない開放的な空に堂々とそびえていてかっこよかった。白状するとこのタイミングまで富士山があることに気がついてなかったです。

それはそれとして8:30 頃にはmitsuくんがやってきて、9時か9時半ごろには講義がぬるりと始まった。

## Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)を用いた[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数計算

### overview

暗号で[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)を用いるにあたって[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数というのは重要な指標で、適当に[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)を生成してしまうと性質の悪い（例えばECDLPが簡単に解ける）位数を持ってしまうことがある。そうならないように、暗号[プロトコル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D7%A5%EF%BF%BD%EF%BF%BD%C8%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)で[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)を利用するときはその曲線の位数を確かめておこう。ところで[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数をどうやって求めるかというと……というのが前説。

まずはSchoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)を用いて位数を計算する方法が紹介された。Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)自体は位数ではなくFrobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のトレース![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)を計算する[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)だが、[標数](http://d.hatena.ne.jp/keyword/%C9%B8%EF%BF%BD%EF%BF%BD)![ p](https://chart.apis.google.com/chart?cht=tx&chl=%20p)の[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ E(\mathbb{F_p})](https://chart.apis.google.com/chart?cht=tx&chl=%20E%28%5Cmathbb%7BF_p%7D%29)の位数とFrobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のトレース![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)の間には次のような関係が成り立つことが知られている。

![ p + 1 - \#E(\mathbb{F_p}) = t](https://chart.apis.google.com/chart?cht=tx&chl=%20p%20%2B%201%20-%20%5C%23E%28%5Cmathbb%7BF_p%7D%29%20%3D%20t)

すなわち、![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)がわかれば![ t, p](https://chart.apis.google.com/chart?cht=tx&chl=%20t%2C%20p)から[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数が計算可能である。

### tを求めるための立式

Frobenius[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ \phi: E \to E](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%3A%20E%20%5Cto%20E)は![ \phi( (x, y) ) = (x^p, y^p)](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%28%20%28x%2C%20y%29%20%29%20%3D%20%28x%5Ep%2C%20y%5Ep%29)と定義される自己[準同型写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%C6%B1%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)で、なんか口頭で補足されていた感じだと行列表示みたいなのと対応付けられるらしく、特性[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)やトレースが定義できるということだった。その特性[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)とは ![ \lambda(X) = X^2 - tX + p](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Clambda%28X%29%20%3D%20X%5E2%20-%20tX%20%2B%20p) であり、ここにトレース![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)が登場する。ケイリー・ハミルトンの定理より![ \lambda(\phi) = \phi^2 - t\phi + p = 0](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Clambda%28%5Cphi%29%20%3D%20%5Cphi%5E2%20-%20t%5Cphi%20%2B%20p%20%3D%200)なので、具体的な点![ P = (x, y) \in E](https://chart.apis.google.com/chart?cht=tx&chl=%20P%20%3D%20%28x%2C%20y%29%20%5Cin%20E)を代入して移項して![ (x^{p^2}, y^{p^2})+ p(x, y)  = t(x^p, y^p)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28x%5E%7Bp%5E2%7D%2C%20y%5E%7Bp%5E2%7D%29%2B%20p%28x%2C%20y%29%20%20%3D%20t%28x%5Ep%2C%20y%5Ep%29)を解けば良いということだったが、ここでケイリー・ハミルトンの定理が出てきた理由はちゃんとはわかっていない。

とにかく、

![ (x^{p^2}, y^{p^2})+ p(x, y)  = t(x^p, y^p) \cdots ( \triangle )](https://chart.apis.google.com/chart?cht=tx&chl=%20%28x%5E%7Bp%5E2%7D%2C%20y%5E%7Bp%5E2%7D%29%2B%20p%28x%2C%20y%29%20%20%3D%20t%28x%5Ep%2C%20y%5Ep%29%20%5Ccdots%20%28%20%5Ctriangle%20%29)

を満たすような![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)こそが今求めたい![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)である。そしてこれを効率的に求める方法の一つがSchoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)である。

### Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)(l-torsion pointについて考えることで次数と探索範囲を減らしてあとでCRTする）

Schoofの[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)では小さい[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)![ l_i](https://chart.apis.google.com/chart?cht=tx&chl=%20l_i)を用いて![ l_i](https://chart.apis.google.com/chart?cht=tx&chl=%20l_i)-torsion pointを考えるということにして、![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)の代わりに![ (x^{p^2}, y^{p^2})+ p(x, y)  = t_i(x^p, y^p)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28x%5E%7Bp%5E2%7D%2C%20y%5E%7Bp%5E2%7D%29%2B%20p%28x%2C%20y%29%20%20%3D%20t_i%28x%5Ep%2C%20y%5Ep%29)を満たす![ t_i \equiv t \mod l_i](https://chart.apis.google.com/chart?cht=tx&chl=%20t_i%20%5Cequiv%20t%20%5Cmod%20l_i)を全探索したあとで中国剰余定理を用いて![ t](https://chart.apis.google.com/chart?cht=tx&chl=%20t)を復元するという方法を取る[\*1](#f-c7bdb3a1 "なんで特定のねじれ群についてだけ考えるでよいのかは理解できてない")。

![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-torsion point [\*2](#f-37374033 "面倒なので添字のiを外しているけど、それぞれのiについて考えています")を考えているということは![ x](https://chart.apis.google.com/chart?cht=tx&chl=%20x)は必ず![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-division polynomial ![ f_l](https://chart.apis.google.com/chart?cht=tx&chl=%20f_l)について![ f_l(x) = 0](https://chart.apis.google.com/chart?cht=tx&chl=%20f_l%28x%29%20%3D%200)を満たすから、![ (\triangle )](https://chart.apis.google.com/chart?cht=tx&chl=%20%28%5Ctriangle%20%29)は![ f_l](https://chart.apis.google.com/chart?cht=tx&chl=%20f_l)が生成する[イデアル](http:...