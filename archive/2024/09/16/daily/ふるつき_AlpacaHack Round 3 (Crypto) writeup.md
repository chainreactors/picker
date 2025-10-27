---
title: AlpacaHack Round 3 (Crypto) writeup
url: https://furutsuki.hatenablog.com/entry/2024/09/15/201136
source: ふるつき
date: 2024-09-16
fetch_date: 2025-10-06T18:22:04.872343
---

# AlpacaHack Round 3 (Crypto) writeup

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_source=blogs_topright_button&utm_campaign=subscribe_blog)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2024-09-15](https://furutsuki.hatenablog.com/archive/2024/09/15)

# [AlpacaHack Round 3 (Crypto) writeup](https://furutsuki.hatenablog.com/entry/2024/09/15/201136)

最近登場した[個人戦](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C4%BF%EF%BF%BD%EF%BF%BD%EF%BF%BD)CTFプラットフォームであるAlpacaHackで、Crypto回があったので参加しました。一回6時間、4問だけの出題で気軽に挑戦できるので良いですね。adminやauthorは国内CTFプレイヤーで上から数えても五指か十指かそのくらいにはいる実力者で問題の質も保証されているので、入門者にも[\*1](#f-cdec9335 "やさしいチュートリアルとかはないのでそういう期待はできないけど、ここで出題される問題に取り組んで復習するという取り組みができれば、世の中のひどいCTFをから守られながら実力をつけることができます")経験者にも、私のような「昔やってました」という人にもおすすめです。

出るかどうか迷ってたけど寝坊しつつもいい感じの時間に起きられたので出て、2時間40分55秒で全完して10位でした。上振れも下振れもしない、実力程度の順位かな〜と思います。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20240915/20240915182654.png)

以下writeup。AlpacaHackにはCTF始めたての人もたくさん参加していると思うので（参加してくれていると嬉しいので）、どういうことを考えていた、とかも頑張って書きます。

* [qrime](#qrime)
* [Rainbow Sweet Alchemist](#Rainbow-Sweet-Alchemist)
* [A Dance of Add and Mul](#A-Dance-of-Add-and-Mul)
* [Hat Trick](#Hat-Trick)

## qrime

問題名みて「primeのpがqになってるやつ〜！ [RSA](https://d.hatena.ne.jp/keyword/RSA)で![ n=p^2](https://chart.apis.google.com/chart?cht=tx&chl=%20n%3Dp%5E2)

```
def gen():
    while True:
        q = getRandomNBitInteger(256)
        r = getRandomNBitInteger(256)
        p = q * nextPrime(r) + nextPrime(q) * r
        if isPrime(p) and isPrime(q):
            return p, q, r
```

雑に読むと、「![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)は適当な[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)で、![ r](https://chart.apis.google.com/chart?cht=tx&chl=%20r)はランダムな値。![ p = qr' + q'r](https://chart.apis.google.com/chart?cht=tx&chl=%20p%20%3D%20qr%27%20%2B%20q%27r)と書いて![ p](https://chart.apis.google.com/chart?cht=tx&chl=%20p)は[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)で、![ n=pq](https://chart.apis.google.com/chart?cht=tx&chl=%20n%3Dpq)」ということがわかる[\*2](#f-3c081f5f "n=pqはこの関数の外で計算されているから、当然この関数だけをみてわかるわけではない")。ここで![ q', r'](https://chart.apis.google.com/chart?cht=tx&chl=%20q%27%2C%20r%27)は適当な小さい整数![ \alpha, \beta](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Calpha%2C%20%5Cbeta)をつかって ![ q' = q + \alpha, r' = r + \beta](https://chart.apis.google.com/chart?cht=tx&chl=%20q%27%20%3D%20q%20%2B%20%5Calpha%2C%20r%27%20%3D%20r%20%2B%20%5Cbeta)と表せるような[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)で、記号は適当に導入した。

で、問題は![ n, r](https://chart.apis.google.com/chart?cht=tx&chl=%20n%2C%20r)と[RSA](https://d.hatena.ne.jp/keyword/RSA)で暗号化された![ c = m^e \mod n](https://chart.apis.google.com/chart?cht=tx&chl=%20c%20%3D%20m%5Ee%20%5Cmod%20n)が与えられているというやつ。明らかに![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)の作り方が変で、ヒントの![ r](https://chart.apis.google.com/chart?cht=tx&chl=%20r)ももらえているので、![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)をを[素因数分解](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%B0%EF%BF%BD%EF%BF%BD%EF%BF%BD%CA%AC%EF%BF%BD%EF%BF%BD)する系の問題でしょう、ということにはあたりがつく。

で、まずは適当に導入した記号を使いつつ![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)を開いていく。

![ n = pq = (qr' + q'r)q = (q(r + \beta) + (q + \alpha)r)q = 2q^2r + q^2\alpha + qr\beta](https://chart.apis.google.com/chart?cht=tx&chl=%20n%20%3D%20pq%20%3D%20%28qr%27%20%2B%20q%27r%29q%20%3D%20%28q%28r%20%2B%20%5Cbeta%29%20%2B%20%28q%20%2B%20%5Calpha%29r%29q%20%3D%202q%5E2r%20%2B%20q%5E2%5Calpha%20%2B%20qr%5Cbeta)

すると（![ \alpha, \beta](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Calpha%2C%20%5Cbeta)は小さいことがわかってて全探索すればよいので）![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)が![ q, r](https://chart.apis.google.com/chart?cht=tx&chl=%20q%2C%20r)の2変数で表されることがわかって、![ r](https://chart.apis.google.com/chart?cht=tx&chl=%20r)は既知だから![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)について解いたらよいね、ということがわかる。

わかるけど、競技中の私は「あ〜あきらかに![ q^2r > q^2, qr](https://chart.apis.google.com/chart?cht=tx&chl=%20q%5E2r%20%3E%20q%5E2%2C%20qr)だね〜、じゃあ![ n \simeq 2q^r](https://chart.apis.google.com/chart?cht=tx&chl=%20n%20%5Csimeq%202q%5Er)って近似できて![ \frac{n}{2r} \simeq q^2](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cfrac%7Bn%7D%7B2r%7D%20%5Csimeq%20q%5E2)って変形すれば![ q^2](https://chart.apis.google.com/chart?cht=tx&chl=%20q%5E2)の近似値が取れそう〜って言って解きました。

こう。近似した後ちゃんとした![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)の値になるかどうかは、近似値に適当な値を足したり引いたりして![ n](https://chart.apis.google.com/chart?cht=tx&chl=%20n)を割り切れるかで判定した。

```
from Crypto.Util.number import isPrime
from gmpy2 import iroot

n=2006...7779
e=65537
c=7716...708
r=307...5270

# n = 2*q**2*r + q**2*a + q*r*b
# -> n / (2*r) ~ q**2

qq, _ = iroot(n // (2*r), 2)
for diff in range(-200, 200):
    q = qq + diff
    if isPrime(q) and n % q == 0:
        p = n // q
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        m = pow(c, d, n)
        print(bytes.fromhex(hex(m)[2:]))
        quit()
```

## Rainbow Sweet Alchemist

何を言ってるかはわからないけど、Acronym的に[RSA](https://d.hatena.ne.jp/keyword/RSA)ということだけがわかる。

で、ちゃんと[スクリプト](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)を読みはじめるとまず `r = random.Random(0)` と書いてあって「あ〜これランダムと言いつつ値が固定されてるやつじゃん〜」になる。さらに真面目に読むと、[RSA](https://d.hatena.ne.jp/keyword/RSA)で、![ p, q](https://chart.apis.google.com/chart?cht=tx&chl=%20p%2C%20q)の作り方が次のように独特であることがわかる。

* `deterministicGetPrime` は呼び出すたびに異なる[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)を返す関数
* これで適当に[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)を集めて`factors`として、全部掛けて+1したあたいが[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)ならその[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)が![ p](https://chart.apis.google.com/chart?cht=tx&chl=%20p)あるいは![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)になる
* もし[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)じゃなかったら`factors` からランダムな値を抜いて、別にランダムな[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)を`factors`に１個追加してもう一回試す、というのをやる

先述の `r = random.Random(0)` によって、`determinisitcGetPrime`の![ k](https://chart.apis.google.com/chart?cht=tx&chl=%20k)回目の呼び出しの値はわかる。一方`factors`からどの値が抜かれるか、というのは固定されてない乱数生成器がつかわれていてわからない、という問題。

まず一瞬考えるのは「`determinisitcGetPrime`が返す[素数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)は全部わかるわけだから`factors`から何が抜かれたらどうなる、を全部シミュレーションしたら良いんじゃね」ということだが、面倒だからやらなかった。

かわりに考えたのは、「![ p](https://chart.apis.google.com/chart?cht=tx&chl=%20p)（![ q](https://chart.apis.google.com/chart?cht=tx&chl=%20q)）は![ p =  2p_1p_2\dots p_k + 1](https://chart.apis.google.com/chart?cht=tx&chl=%20p%20%3D%20%202p_1p_2%5Cdots%20p_k%20%2B%201)という形式で、どの![ p_i](https://chart.apis.google.com/chart?cht=tx&chl=%20p_i)も64bitだから、![ p, q](https://chart.apis.google.com/chart?cht=tx&chl=%20p%2C%20q)は[B-smooth](https://crypto-writeup-public.hatenablog.com/entry/B-smooth)な値なんだなぁ」ということ。要するに![ p-1](https://chart.apis.google.com/chart?cht=tx&chl=%20p-1)の素因数がある程度小さい値に限られるということで、こういうケースではpollard's p-1 methodという[素因数分解](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%B0%EF%BF%BD%EF%BF%BD%EF%BF%BD%CA%AC%EF%BF%BD%EF%BF%BD)方法が有効[\*3](#f-a56215ce "これは知識として覚えてる")。

が、実際には拾ってきたp-1法をやってみてもうまくいかなくて、もうちょい工夫する必要がある。

p-1法については[このエントリ](https://wacchoz.hatenablog.com/entry/2019/01/20/120000#p-1%E6%B3%95)とかにかいてあって、私は良く知らないが、読んでみると適当な![ a](https://chart.apis.google.com/chart?cht=tx&chl=%20a)にたいして![ p-1](https://chart.apis.google.com/chart?cht=tx&chl=%20p-1)のあらゆる素因数（の候補）の積![ M](https://chart.apis.google.com/chart?cht=tx&chl=%20M)があって![ gcd(a^M - 1, n)](https://chart.apis.google.com/chart?cht=tx&chl=%20gcd%28a%5EM%20-%...