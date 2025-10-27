---
title: SECCON CTF 2022 Finals運営記
url: https://ptr-yudai.hatenablog.com/entry/2023/02/17/014808
source: CTFするぞ
date: 2023-02-17
fetch_date: 2025-10-04T06:51:47.864356
---

# SECCON CTF 2022 Finals運営記

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_campaign=subscribe_blog&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2023-02-17](https://ptr-yudai.hatenablog.com/archive/2023/02/17)

# [SECCON CTF 2022 Finals運営記](https://ptr-yudai.hatenablog.com/entry/2023/02/17/014808)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[SECCON](https://ptr-yudai.hatenablog.com/archive/category/SECCON)

こんにちは、KoHの弟です。
SECCON CTFのすべてを、お話します。

* [Jeopardyに関して](#Jeopardyに関して)
  + [難易度調整](#難易度調整)
  + [rev](#rev)
  + [pwn](#pwn)
  + [ブース問](#ブース問)
* [King of the Hillに関して](#King-of-the-Hillに関して)
  + [SecLang](#SecLang)
    - [発案から実装まで](#発案から実装まで)
    - [非想定解を潰す](#非想定解を潰す)
    - [サーバーを書く](#サーバーを書く)
    - [ベンチマークする](#ベンチマークする)
    - [想定バグ一覧](#想定バグ一覧)
      * [配列の範囲外参照](#配列の範囲外参照)
      * [異なる型どうしの演算](#異なる型どうしの演算)
      * [任意の型の関数としての利用](#任意の型の関数としての利用)
      * [任意の型の配列としての利用](#任意の型の配列としての利用)
      * [配列のUse-after-Free](#配列のUse-after-Free)
      * [if/whileスコープ中での配列の確保](#ifwhileスコープ中での配列の確保)
      * [関数引数での配列の確保](#関数引数での配列の確保)
    - [反省点](#反省点)
  + [Heptarchy](#Heptarchy)
    - [アルゴリズム](#アルゴリズム)
    - [C](#C)
    - [C++](#C-1)
    - [Rust](#Rust)
    - [Go](#Go)
    - [Python](#Python)
    - [D](#D)
    - [WebAssembly](#WebAssembly)
  + [反省点](#反省点-1)
* [インフラとの戦い](#インフラとの戦い)
* [運営中](#運営中)
* [配布物に関して](#配布物に関して)
  + [優勝盾とメダル](#優勝盾とメダル)
  + [ステッカー](#ステッカー)
  + [チーム旗やプレートなど](#チーム旗やプレートなど)
  + [クリアファイル](#クリアファイル)
  + [お弁当の配布](#お弁当の配布)
  + [お菓子の配布](#お菓子の配布)
  + [作れなかったもの](#作れなかったもの)
* [アフターパーティ](#アフターパーティ)
* [おわりに](#おわりに)

# Jeopardyに関して

revとpwnをすべて作りました。つらい。
writeupはこっち

[ptr-yudai.hatenablog.com](https://ptr-yudai.hatenablog.com/entry/2023/02/14/033354)

## 難易度調整

KoHとの点数バランスを保ち、Jeopardyの問題が支配的になりすぎないように、静的配点を採用しました。
国内・国際の参加チームを確認し、どのチームが解けそうかを作問者に真剣に考えてもらい、次のようにsolve数を予測して点数をつけました。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230217/20230217002755.png)

結果として結構予想は外れてしまい、国内にとっては難しすぎて、国際にとっては簡単すぎる[\*1](#f-9939f00e "webを除く")ような結果となってしまいました。特にcryptoは国際に解かれすぎていて可哀想でした。

## rev

whiskyはもともとeasy pwnくらいで作る予定でしたが、uwsgiのドキュメントがカスすぎて何もできなかったので雑魚revに落ちました。
uwsgi iniを書けば[プラグイン](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D7%A5%E9%A5%B0%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を動かせることに気づけば、動的解析ですぐ解けると思います。

Paper Houseはハードウェアの問題です。
本当はハードウェアを設計して実機を配布したかったのですが、パーツが届きませんでした。
[Amazon.co.jp](http://d.hatena.ne.jp/keyword/Amazon.co.jp)の表示より大幅に遅れて昨日届きました。いらん。

Check in Abyssは予選に出題する予定でしたが、レビューで難しすぎるのではという声があり本戦に流しました。
ネタとなったSMMは会社のLT会で知ったもので、LT会の直後から問題を設計し始めていました。
事前知識があればそこまで難しくないかと思います。
ユーザー空間にナナチがいるのはすぐ分かりますが、SMMで動かしている暗号処理にも隠れナナチがいるので探してみてください。

## pwn

とりあえずwarmupに[Unicorn](http://d.hatena.ne.jp/keyword/Unicorn)のpwnでも置くかぁという適当な気持ちでdiagemuを作りました。
xbegin/xendを使う問題を考えていたところ、xendが[Unicorn](http://d.hatena.ne.jp/keyword/Unicorn)に認識されず、かつ命令サイズが意味不明になったことに気づいて問題にしました。
適当に[アセンブリ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D6%A5%EF%BF%BD)を入れて未定義命令のサイズが異常なことに気づけばすぐ解けるかと思います。

babyescapeはもともと`open_by_handle_at`でescapeする問題でしたが、調べたらShockerという古いdockerの有名なexploitがあり、簡単すぎると判断して`kexec_load`を代わりに許可しました。
[カーネル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%CD%A5%EF%BF%BD)ドライバをビルドするのが一番面倒で、あとは作業ゲーだからあまり出したくないと思っていましたが、ふるつきに「出しちゃえ」と言われたので出題しました。
結果、多くのチームを「解けそうだけど解けない」状態に陥れて時間を吸収するお邪魔問題になっていたようです。

Dusty Storageはもともとtcacheの`mp_.tcache_bin`に関する問題を作りたくて1年くらい経ってしまったので、そろそろ既出になる前に出そう、という焦りで問題化しました。
割と自然で綺麗な問題設計になったと思います。

Conversation Starterは予選に出す予定でしたが、十分な量の問題がすでにあったため本戦に回しました。
しふくろ先生に作問チェックしてもらい、無事非想定解が出たので修正しましたが、それでも非想定解が出ました。
libcのpartial overwriteは出してはいけない。

## ブース問

いつか出すかもしれないのでネタは言えませんが、他にもたくさん実機問のア[イデア](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%C7%A5%EF%BF%BD)がありました。
その中で一番実装と準備が簡単そうなLAN盗聴問題を出しました。

問題案自体はかなり前から必要な機材とともに提示していましたが、インフラチームとの兼ね合いでLANケーブルが微妙に足りませんでした。
初日必要分だけ前日に作り、１日目にインフラチームの方に買い出しに行っていただきました。

また、CTF for Beginnersのメンバー各位（[@hi120ki](https://twitter.com/hi120ki), [@n01e0](https://twitter.com/n01e0), [@satoki00](https://twitter.com/satoki00), [@Sz4rny](https://twitter.com/Sz4rny), [@task4233](https://twitter.com/task4233/), [@ushigai\_sub](https://twitter.com/ushigai_sub)）には特にお世話になりました。
両日ともにLANケーブルの作成を手伝ったもらい、無事必要なだけのLANケーブルを完成させられました。
また、当日はブースに拘束される監督役をお願いしました。

本当にありがとうございました。

# King of the Hillに関して

SECCONは例年King of the HillかAttack & Defense形式でした。
今年はKing of the Hillにすると決まっていたので、pwnのSecLangにあたる問題ア[イデア](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%C7%A5%EF%BF%BD)だけを思いついていました。
しかし、cryptoやwebのKing of the Hillがいつまで経っても提案されないので、このままではKoHが1問になってしまうという危惧からrevのHeptarchyも作りました。

## SecLang

このKoHでは、未知の[プログラミング言語](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D7%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%DF%A5%F3%A5%B0%B8%EF%BF%BD%EF%BF%BD%EF%BF%BD)仕様と、その[インタプリタ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%F3%A5%BF%A5%D7%A5%EA%A5%BF)（リモートで試せる）、[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)が渡されます。
[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)は[C言語](http://d.hatena.ne.jp/keyword/C%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のように、配列の範囲外参照や型の取り違えなど健全でないコードを許してしまうため、Rustのように健全な[機械語](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を生成できるように直しましょう、という問題です。

この問題は5分ごとに動く5つのランダムなテストケースの合格率と、他のチームの[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)を使って任意コード実行できるかかの２点で点数が付きます。
自分の[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)が攻撃を受けると、そのラウンドのテストケース結果はすべて無効になります。
したがって、他人のチームを攻撃しつつ、攻撃を防ぐために自分のチームの[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)を修正し、アップロードしなくてはなりません。
もはやA&Dですね。

### 発案から実装まで

実装が死ぬほど大変でした。体感3ヶ月以上使ったと思います。
と思ってログを見たら最初にア[イデア](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%C7%A5%EF%BF%BD)を出していたのは8ヶ月前の6月でした。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230214/20230214194443.png)

ここから数ヶ月かけで地道に言語仕様の制定と[インタプリタ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%F3%A5%BF%A5%D7%A5%EA%A5%BF)作成を進めていきます。
途中でつらくなってやめた時期もあったと思います。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230214/20230214195450.png)

つらそうなメッセージを投げるとふるつきが手伝ってくれます[\*2](#f-ac09ccfe "実際、最終的な文法やほとんどのテストケースはふるつき産です。")。神。

当初は下の図のような感じで、SecLangよりも高級な文法が提供されていました。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230214/20230214194644.png)

が、コーナーケースでいろいろバグったり、[コンパイル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)を作る段階になって死にそうになったりで、文法に制約をかけまくりました。

この問題はとにかくゲームバランスの設計が難しかったです。
7時間で攻撃と防御を両立できるよう、適度な量の[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)を埋め込んだり、攻撃を易しくするためNXを無効にして[機械語](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)をrwxにしたり、難易度を調整しました。
また、防御が難しくなりすぎないように、変数の型情報や配列のサイズ情報は残しつつ、それらを使ってないような[コンパイラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)を作りました。

さらに、他人がどういう修正を入れたかわからないと攻撃できない一方、パッチを公開すると他人の解法をコピーできてしまいます。
そこで、[コンパイル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D1%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)時に生成されるプログラムの[アセンブリ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D6%A5%EF%BF%BD)のみを開示することで、[脳死](http://d.hatena.ne.jp/keyword/%C7%BE%EF%BF%BD%EF%BF%BD)解法コピー解法を潰しました。

### 非想定解を潰す

参加者視点で考えると、テストケースは通しつつ攻撃は通さないようなハックを思いつこうとします。
次のような問題点を事前に潰しました。

* ...