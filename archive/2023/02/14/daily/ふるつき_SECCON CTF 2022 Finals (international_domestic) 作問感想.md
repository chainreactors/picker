---
title: SECCON CTF 2022 Finals (international/domestic) 作問感想
url: https://furutsuki.hatenablog.com/entry/2023/02/13/231456
source: ふるつき
date: 2023-02-14
fetch_date: 2025-10-04T06:30:39.040581
---

# SECCON CTF 2022 Finals (international/domestic) 作問感想

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2023-02-13](https://furutsuki.hatenablog.com/archive/2023/02/13)

# [SECCON CTF 2022 Finals (international/domestic) 作問感想](https://furutsuki.hatenablog.com/entry/2023/02/13/231456)

こんにちは。SECCON CTF 2019以来のオンサイトでありSECCON CTF 2019以来の決勝であるSECCON CTF 2022 Finals (international/domestic) が開催され、無事閉幕しました。私はSECCON CTF 2022 Quals から引き続きCTF WGとして作問に携わっていましたので、自分が出題した問題についていくらか感想や解説を書こうと思います。オンサイトCTF自体の感想や反省などについては別途どこかに書きます。

* [[Crypto 200] authenticator](#Crypto-200-authenticator)
  + [解説](#解説)
  + [感想](#感想)
* [[Crypto 300] hell](#Crypto-300-hell)
  + [解説](#解説-1)
  + [感想](#感想-1)
* [おわりに](#おわりに)

## [Crypto 200] authenticator

### 解説

次のような[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)が与えられる問題です。5秒単位で切り替わるタイムスタンプ`t`と秘密の値`key`、そして自由に指定できる入力`code`をもとに![ CRC(key \oplus t, code) ](https://chart.apis.google.com/chart?cht=tx&chl=%20CRC%28key%20%5Coplus%20t%2C%20code%29%20) が計算されるので、その値が`code` に帰ってくるような入力`code`を入力できればフラグがもらえる、という問題設定です。

ただし、ヒントとして![ CRC("hint", CRC(key \oplus t, code))](https://chart.apis.google.com/chart?cht=tx&chl=%20CRC%28%22hint%22%2C%20CRC%28key%20%5Coplus%20t%2C%20code%29%29)の値をもらうことができます。

[gist.github.com](https://gist.github.com/theoremoon/97a48061517a00d25b799a649d325550)

この問題では、まずヒントを利用して`key`の値を求め、その後制約を満たすようなcodeの値を計算することになります。[CRC](http://d.hatena.ne.jp/keyword/CRC)の計算が途中にあって難しそうに見えますが、単なる商環上の演算なので以下のように愚直にやると解けます。[CRC](http://d.hatena.ne.jp/keyword/CRC)の演算と[多項式環](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0%EF%BF%BD%EF%BF%BD)（商環）上の操作の対応については[CRC - crypto-writeup-public](https://scrapbox.io/crypto-writeup-public/CRC)などを参考にしてください。

[gist.github.com](https://gist.github.com/theoremoon/4aa1708f04bae203dad8934ff1d0a2c1)

### 感想

一見そこそこ複雑そうな問題設定ですが、[多項式環](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0%EF%BF%BD%EF%BF%BD)で考えると割と素直に解けるのでそこそこ気に入っています。

難易度でみれば簡単な部類だと思っていたのでCrypto warmup枠で出題しましたが、国内では4チームしか解けているチームがなかったのでもしかしたら少しむずかしかったのかもしれません。競技後に問いたプレイヤーに聞いてみるとCrypto jeopardyの中で一番苦戦したという声もありました。

一方、国際チームは順調に攻略して結局すべてのチームが正解したので、過去に[CRC](http://d.hatena.ne.jp/keyword/CRC)に関する問題や似たようなコンセプトの問題を解いたことがあるかどうかで感じる難易度が違ったかもしれません。[CRC](http://d.hatena.ne.jp/keyword/CRC)を[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)の理論からみるというのはなかなか便利で面白い技なので、もし知らなかった場合はこの機会に憶えてもらうと今後役に立つこともあるかもしれません。

## [Crypto 300] hell

### 解説

超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)（Hyperellipticcurve）に関する問題です。下記のSage[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)とその実行結果が与えられます。

[gist.github.com](https://gist.github.com/theoremoon/23e4335a43c59de1839bacdb83cd6826)

この[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)は有限体![ \mathbb{F_p}](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cmathbb%7BF_p%7D)上の超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ HC: y^2 + h(x)y = f(x)](https://chart.apis.google.com/chart?cht=tx&chl=%20HC%3A%20y%5E2%20%2B%20h%28x%29y%20%3D%20f%28x%29)（今回は![ h(x) = 0](https://chart.apis.google.com/chart?cht=tx&chl=%20h%28x%29%20%3D%200)）を、ある点![ (xv, yv)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28xv%2C%20yv%29)が![ C](https://chart.apis.google.com/chart?cht=tx&chl=%20C)上に含まれるように生成し、この点によって生成される[ヤコビアン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E4%A5%B3%EF%BF%BD%D3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上の（半）被約因子![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)に対して、![ 6D, 12D, 20D](https://chart.apis.google.com/chart?cht=tx&chl=%206D%2C%2012D%2C%2020D)（のMumford表現）を出力しています。この問題では![ yv](https://chart.apis.google.com/chart?cht=tx&chl=%20yv)がフラグになっているので、これを求めるのが目的です。

おそらく超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)について詳しくない皆様は何を言われているか全くわからないとは思いますが、そういう問題です。超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)についてざっくりと知りたい方は以下のエントリを参考にしてください。

[ptr-yudai.hatenablog.com](https://ptr-yudai.hatenablog.com/entry/2021/11/23/124118)

さて、この問題ではまず3つの被約因子のMumford表現から超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ HC](https://chart.apis.google.com/chart?cht=tx&chl=%20HC)を復元する必要があります。これについては超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)とその[ヤコビアン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E4%A5%B3%EF%BF%BD%D3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上の被約因子の間には、被約因子を![ (a, b)](https://chart.apis.google.com/chart?cht=tx&chl=%20%28a%2C%20b%29)と表現して![ a | b^2 + hb - f](https://chart.apis.google.com/chart?cht=tx&chl=%20a%20%7C%20b%5E2%20%2B%20hb%20-%20f)という関係があります。今回の問題では![ h = 0](https://chart.apis.google.com/chart?cht=tx&chl=%20h%20%3D%200)ですから![ a | b^2 - f](https://chart.apis.google.com/chart?cht=tx&chl=%20a%20%7C%20b%5E2%20-%20f)で、これを変形すると![ b^2 \equiv f \mod a](https://chart.apis.google.com/chart?cht=tx&chl=%20b%5E2%20%5Cequiv%20f%20%5Cmod%20a)となります。

今3つの被約因子![ 6D = (a_1, b_1), 12D = (a_2, b_2), 20D = (a_3, b_3)](https://chart.apis.google.com/chart?cht=tx&chl=%206D%20%3D%20%28a_1%2C%20b_1%29%2C%2012D%20%3D%20%28a_2%2C%20b_2%29%2C%2020D%20%3D%20%28a_3%2C%20b_3%29)を持っているのでそれぞれについて上記の式が成り立つので、中国剰余定理より![ f](https://chart.apis.google.com/chart?cht=tx&chl=%20f)が復元できます[\*1](#f-bfe1eef6 "3点で十分[tex: f]が求められるようなサイズになるように問題が作られています")。これで超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)のパラメータが求まりました

続いてはこの3点と超[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)のパラメータを利用して![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)を求めたいです。まずは![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)を計算し、その後![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)から![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)の座標を求めることになります。

与えられた3点から![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)を求めるには単に（[ヤコビアン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E4%A5%B3%EF%BF%BD%D3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上の）被約因子の演算をすればよく、![ 20D - (12D + 6D)](https://chart.apis.google.com/chart?cht=tx&chl=%2020D%20-%20%2812D%20%2B%206D%29)を計算すると![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)が求まります。

続いて![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)を求める方法ですが、[ヤコビアン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E4%A5%B3%EF%BF%BD%D3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)の位数を効率的に求める方法は今の所知られていないので![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)に対して![ 2](https://chart.apis.google.com/chart?cht=tx&chl=%202)の逆数をかけて![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)を求めることはできません。しかし、特定のケースにおける被約因子の2倍算ではx座標が単に2乗されるので[\*2](#f-dad6ea2b "https://github.com/sagemath/sage/blob/293dd7255b231ff9cd17407ee3c23841a06b5c5b/src/sage/schemes/hyperelliptic_curves/jacobian_morphism.py#L255 においてd=1の場合")、![ 2D](https://chart.apis.google.com/chart?cht=tx&chl=%202D)のx座標の![ \mathbb{F_p}](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cmathbb%7BF_p%7D)における[平方根](http://d.hatena.ne.jp/keyword/%CA%BF%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を求めれば![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)のx座標が計算できます。x座標が与えられたときに対応するy座標を計算することは簡単なので、これで![ D](https://chart.apis.google.com/chart?cht=tx&chl=%20D)が求まりました。

……以上の理屈をコードに落とし込むと以下のようになります。なんだか騙されたみたいに短くて簡単ですね。

[gist.github.com](https://gist.github.com/theoremoon/105614b6c689d604beb83957fa031f25)

### 感想

以前のyoshi-campでmitsuくんに超[楕円曲線](http://d.hatena.ne.jp/keyw...