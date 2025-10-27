---
title: yoshi-camp 2022 winter参加記【Day 0-1】
url: https://buaq.net/go-139874.html
source: unSafe.sh - 不安全
date: 2022-12-14
fetch_date: 2025-10-04T01:23:03.991025
---

# yoshi-camp 2022 winter参加記【Day 0-1】

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

![](https://8aqnet.cdn.bcebos.com/b1ec39104ac96c4991bb81046c1af147.jpg)

yoshi-camp 2022 winter参加記【Day 0-1】

今年もyoshi-campを開催
*2022-12-13 22:50:34
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-139874.htm)
阅读量:24
收藏*

---

今年もyoshi-campを開催しました。

今回は久しぶりのオンサイト開催で、zer0pts外部からの参加者も募集しました。
結果として、連絡してくれた./VespiaryのXornetさんとﾈさんを招待しました。

* [はじめに](#はじめに)
* [yoshi-campって何？](#yoshi-campって何)
* [yoshi-camp](#yoshi-camp)
  + [開催地決定](#開催地決定)
  + [Day 0](#Day-0)
    - [会場まで](#会場まで)
    - [会場着](#会場着)
  + [Day 1](#Day-1)
    - [朝](#朝)
    - [[theoremoon] 猫と学ぶ同種写像暗号](#theoremoon-猫と学ぶ同種写像暗号)
    - [[ptr-yudai] 猫たちと学ぶ量子コンピュータ](#ptr-yudai-猫たちと学ぶ量子コンピュータ)
    - [夜](#夜)
* [次回予告](#次回予告)

もともとはyoshikingが[セキュリティキャンプ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%C6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)に落ちたことを受け、[セキュリティキャンプ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%C6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)よりも高度な講義をyoshikingに受けさせる目的で開催されました。
ちなみに今年は私が[GCC](http://d.hatena.ne.jp/keyword/GCC)のチューターに落ちました。さようなら[GCC](http://d.hatena.ne.jp/keyword/GCC)。

yoshi-campの講義はMooreの法則で年々難易度がインフレしています。
インフレしすぎて今年は全然実装が追いつかなかったので、とりあえず今回は初日終了までの内容を出して、後から2日目以降を公開したいと思います。

## 開催地決定

今までは大学関連施設を借りて開催していましたが、宿泊場所から会場までの移動時間が無駄という理由で、今回はでかい家を借りました。
場所は最大10人程度が泊まれる箱根の別荘にしました。
候補はいろいろありましたが、富士山が見える部屋や全面ガラス張りの石風呂など施設が充実していたため全力でこの別荘を取りました。

当日までに持ち運びできるホワイトボードなどを購入しました。買っててよかったです。

## Day 0

### 会場まで

Day 1にみんなが早くチェックインできるよう、私は前日に家を開けました。
[秋葉原](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%D5%B8%EF%BF%BD)で5m [HDMI](http://d.hatena.ne.jp/keyword/HDMI)ケーブルを買うついでに将棋盤を買い、将棋盤を買ったついでにハゲタカというカードゲームを買いました。

新宿から箱根湯本まで行き、会場に行く前に温泉に入りました。
会場までは山を登り左右に揺れまくる激酔いバスで一本です。

### 会場着

今回借りた家は基本的にすべてが良かったのですが、周辺の店から家までの坂が大変でした。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221212/20221212115844.png)

第一犠牲者

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221212/20221212115912.png)

第二犠牲者

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221212/20221212115957.png)

第三〜第五犠牲者

事前にホストから、[HDMI](http://d.hatena.ne.jp/keyword/HDMI)が使えるでかいテレビがある情報を得ていたので、ディスプレイのセットアップやホワイトボードの配置を考えた後、講義資料の修正をしていました。
家が広すぎて寂しかったです。

## Day 1

### 朝

まず朝にyoshikingが到着しました。
卓球台があったので卓球を極めて、あとは[ジェンガ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)とかしてました。[\*1](#f-bb9f710e "演習予定のDraperの量子回路がバグり散らかして修正していたが、諦めて遊び始めた。")

その後theoremoon、Xornet、ﾈさんの順番に到着したと思います。
mitsu大教授はDay 2から来ました。

### [theoremoon] 猫と学ぶ同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)暗号

今流行りの激アツ（炎上）[プロトコル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D7%A5%EF%BF%BD%EF%BF%BD%C8%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)ことSIDH(Supersingular Isogeny [Diffie-Hellman](http://d.hatena.ne.jp/keyword/Diffie-Hellman))のお勉強です。

今回扱う同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)は[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)から別の[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)への[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)![\phi: E\rightarrow E'](https://chart.apis.google.com/chart?cht=tx&chl=%5Cphi%3A%20E%5Crightarrow%20E%27)で、次の性質を満たすらしいです。

* 有利[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)で表せる
* [全射](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)
* ![\phi(\mathcal{O}_E) = \mathcal{O}_{E'}](https://chart.apis.google.com/chart?cht=tx&chl=%5Cphi%28%5Cmathcal%7BO%7D_E%29%20%3D%20%5Cmathcal%7BO%7D_%7BE%27%7D)

有利[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)なので次数が定義でき、次数lの変換をl-isogenyと呼ぶそうです。

![E(\mathbb{F}_p)](https://chart.apis.google.com/chart?cht=tx&chl=E%28%5Cmathbb%7BF%7D_p%29)と![H\in E(\bar{\mathbb{F}}_p)](https://chart.apis.google.com/chart?cht=tx&chl=H%5Cin%20E%28%5Cbar%7B%5Cmathbb%7BF%7D%7D_p%29)が与えられたとき、![\ker{\phi}=\langle H \rangle](https://chart.apis.google.com/chart?cht=tx&chl=%5Cker%7B%5Cphi%7D%3D%5Clangle%20H%20%5Crangle)となる同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)は同型を除き一意に定まるという基本命題があると説明されていました。
そしてこの[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の計算はVéluの公式/Kohelの公式というので計算できるらしいですが、今回は本質でないのでsageの実装をお借りしています。

最初の演習ではn-isogenyをすべて求める関数を実装しました。当日の私の成果はこれだけです。
n-torsion pointを生成元として同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を求めれば良いとひよこ先生が言っていたので、それを実装しています。

```
def l_isogeny(E, l):
    for root in E.division_polynomial(l).roots():
        H = E.lift_x(root[0])
        phi = EllipticCurveIsogeny(E, H)
        E2 = phi.codomain()
        yield phi, E2
```

sageには`isogeny`というメソッドがEllipticCurveに生えていますが、上記実装の`l_isogeny`はすべてのl-isogenyを求めてくれます。

このあと高次数の同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を求める実装がありましたが、現地ではやり方が分からず死亡しました。
復習ということで演習の続きをやります。[\*2](#f-b3eb70a1 "参加記を書きつつsage 9.8を速い速いマシンでビルドすると、なんと15分弱でビルドが終わりました。")

SIDHするにはle-isogenyが欲しいのですが、そんなでかい値の`division_polynomial`を求めようとすると計算が終わりません。
そこで、生成元と曲線を移しながら、l-isogenyをe回計算するとle-isogenyになるようです。原理は理解できませんでした。

```
def l_isogeny(K):
    phi = EllipticCurveIsogeny(K.curve(), K)
    return phi

def prime_power_isogeny(K, l, e):
    E = K.curve()
    assert K.order() == l^e
    for i in range(e):
        phi = l_isogeny(l^(e-i-1) * K)
        E = phi.codomain()
        K = phi(K)
    return E
```

これでle-isogenyが計算できます。
まず、`prime_power_isogeny`にはle-ねじれ点を渡します。
これはよく分からなかったのですが、見かねた講師が1記事書いてくれています。

[furutsuki.hatenablog.com](https://furutsuki.hatenablog.com/entry/2022/12/13/131802)

それはそう。

```
G = E.gen(0)
K = int(G.order() / l^e) * G
```

とかで適当に作っておきましょう。

次にfor文の中ですが、

```
phi = l_isogeny(l^(e-i-1) * K)
```

でl-isogenyを計算しています。
さっきの`l_isogeny`はyieldですべての同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を求めていましたが、今回はl-ねじれ点を1つ渡してl-isogenyを求める実装に変わっている点は注意です。
Kはもともとle-ねじれ点だったため、le-i-1倍するとl-ねじれ点になります。
これをfor文でe回繰り返せば、le-isogenyが求まるという算段です。

さて、曲線を別の曲線に移せる同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を一意に計算できることが分かりました。
同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)で移る同型な[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)同士をまとめると、[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を辺としたグラフになり、これを同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)グラフと呼ぶそうです。
l-同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)はl+1個存在するので、各頂点はl+1個の辺を持ちます。
別の曲線から同じ曲線に移ることもあるため、[木構造](http://d.hatena.ne.jp/keyword/%EF%BF%BD%DA%B9%EF%BF%BD%C2%A4)ではなく一般的なグラフ構造です。

この性質を利用すれば、[ハッシュ関数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A5%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%D8%BF%EF%BF%BD)が作れることが分かります。
例えば適当な点を始点とし、2-isogenyを考えます。
入力の0ビット目が0ならx座標の小さい方に移す、といったルールを設ければ[ハッシュ関数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A5%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%D8%BF%EF%BF%BD)になります。

演習では始点について定義されていましたが、よく分からんかったので適当に一意に定まるように選びました。

```
def l_isogeny(E, l):
    for root in E.division_polynomial(l).roots():
        H = E.lift_x(root[0])
        yield EllipticCurveIsogeny(E, H)

def CGL_hash(message):
    p = 2^143 * 3 - 1
    E = EllipticCurve(GF(p^2), [1, 0])
    K = E.gen(0)

    prev_K = None
    for c in message:
        for i in range(8):
            bit = (c >> i) & 1

            next_point = []
            for phi in l_isogeny(E, 2):
                next_K = phi(K)
                if next_K != prev_K:
                    next_point.append((next_K, phi))
            next_point.sort(key=lam...