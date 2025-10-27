---
title: SECCON CTF 2022作問感想：janken vs kurenaif
url: https://buaq.net/go-135418.html
source: unSafe.sh - 不安全
date: 2022-11-14
fetch_date: 2025-10-03T22:39:42.070362
---

# SECCON CTF 2022作問感想：janken vs kurenaif

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

![]()

SECCON CTF 2022作問感想：janken vs kurenaif

こんにちは。今年もSECCON CT
*2022-11-13 19:26:46
Author: [furutsuki.hatenablog.com(查看原文)](/jump-135418.htm)
阅读量:60
收藏*

---

こんにちは。今年もSECCON CTF 2022 (Qualification)が無事終了しました。私はCTF WGの一員として運営に参加していて、今回はCryptoの問題を一問提供しているのでその感想です。

提供した問題はjanken vs kureanifというやつで、これのauthorがtheoremoonでいいのかって感じの名前のやつです。zer0pts CTF 2021で出題した[janken vs yoshiking](https://github.com/zer0pts/zer0pts-CTF-2021/tree/master/crypto/janken_vs_yoshiking)の流れを汲む正統派（？）jankenシリーズですが、問題としては全く異なるので当然以前の問題について知らなくても解けます。この問題をみてjanken vs yoshikingのことを思い出した人はいないと思う。このカシオミニを賭けても良いです

問題としてはかなりシンプルで、名前の通りあのcrypto witch, kurenaifとじゃんけん勝負をすることになりますが、互いの手は乱数によって決まります。kurenaifの手を決める乱数のシードは事前に教えてもらえているので、kurenaifにじゃんけんで666連勝できるようなシードを入力できれば良いです。

```
import os
import signal
import random
import secrets

FLAG = os.getenv("FLAG", "fake{cast a special spell}")

def janken(a, b):
    return (a - b + 3) % 3

signal.alarm(1000)
print("kurenaif: Hi, I'm a crypto witch. Let's a spell battle with me.")

witch_spell = secrets.token_hex(16)
witch_rand = random.Random()
witch_rand.seed(int(witch_spell, 16))
print(f"kurenaif: My spell is {witch_spell}. What about your spell?")

your_spell = input("your spell: ")
your_random = random.Random()
your_random.seed(int(your_spell, 16))

for _ in range(666):
    witch_hand = witch_rand.randint(0, 2)
    your_hand = your_random.randint(0, 2)

    if janken(your_hand, witch_hand) != 1:
        print("kurenaif: Could you come here the day before yesterday?")
        quit()

print("kurenaif: Amazing! Your spell is very powerful!!")
print(f"kurenaif: OK. The flag is here. {FLAG}")
```

この問題では次のような知識を要求しています。

* [python](http://d.hatena.ne.jp/keyword/python)のrandomモジュールで使われている乱数生成[アルゴリズム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)について（[メルセンヌ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EB%A5%BB%EF%BF%BD%EF%BF%BD%EF%BF%BD)ツイスタ法）
* [メルセンヌ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EB%A5%BB%EF%BF%BD%EF%BF%BD%EF%BF%BD)ツイスタ法自体について（32bit × 624個の内部状態からなることなど）
* [python](http://d.hatena.ne.jp/keyword/python)のrandomモジュールのrandintの実装（32bit未満の乱数を生成するときは32bit未満の乱数を一個生成して、その値を切り詰めている）
* [python](http://d.hatena.ne.jp/keyword/python)のrandomモジュールのseedの実装（整数を渡したときにどのようにそれが内部状態に影響するか）

前半の3つは暗号問題を解く上では頻出の知識なので、この問題に取り組む上では知っておいてほしいと思っていたことで、今回は[seedの実装](https://github.com/python/cpython/blob/9588f880a286a8cc5597188f6ab44108c8f18761/Modules/_randommodule.c#L275)を読んでそれを逆算するような計算を組めますかというところを問う問題になりました。想定解法としてはz3のようなSMTソルバを用いて、[メルセンヌ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EB%A5%BB%EF%BF%BD%EF%BF%BD%EF%BF%BD)ツイスタの内部状態とその内部状態を生成するような乱数のseedを求めることになります。私の解法では内部状態を求めるパートとseedを求めるパートは別に分けましたが、多分[一気通貫](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%B5%A4%EF%BF%BD%CC%B4%EF%BF%BD)にも計算できると思います。

この問題はもともと以前開催したCakeCTF 2022に出題するつもりで作ったのですが、問題を一見したときに「これができるのか」という驚きがありそうなのと実装がそれなりに大変そうということで、もしかしたらSECCON CTFにも出せるかもと思ってptr-yudaiに相談して、こちらに回すことにしました。そういう経緯があって以前はjanken vs yoshiking2という名前でyoshikingとじゃんけんしていたのですが、SECCON CTFに出すということでじゃんけんのプレイヤーをkurenaifさんに交代してもらいました。以前は挑戦者の名前を入力してもらってそれを数値にして[\*1](#f-c6353ef4 "pythonのrandom.seedは文字列も受け付けますが、その場合途中で入力値をハッシュ関数にかける処理があるので望んだ乱数を生成するようなシードを生成するのは不可能そうでした")シードにするという不自然さの残る問題設定だったところが、kurenaifさんは魔女ということで、魔女と呪文で勝負！　という感じの問題設定にしてそこそこ自然にできて問題としても良くなりました。

さらにkurenaifさんに無茶を言ってこの問題のために動画を一本とってもらって、その動画の限定公開のURLをこの問題のフラグとしています。kurenaifさんは国内外のCTFプレイヤーによく知られている人気タレントなので、この仕組みも好評でした。思いの外solve数が伸びなかったこともあり、特に競技期間中に解けたチームはなかなか特別感が得られたのではないかと思います。まだその動画を見れていないという人は、ぜひ誰かのwriteupを読んだりして問題が稼働しているうちにupsolveしてURLを発見してください[\*2](#f-16d02a77 "まあ出題した問題や解法などのファイルは今後GitHubで公開するでしょうからそのタイミングをまてば問題を解かずに動画にアクセスすることはできるでしょうが、それはかなり味気ないと思います")。そしてぜひコメントなどを残していってください。

それにしても、思ったよりこの問題が解かれなかったので驚いています。個人的には同じSECCON CTFに出ていたCrypto問題ではinsufficientと同じかもうちょっと解かれるかなと思っていましたが、結果としては一番solve数の少ない問題になりましたし、解いたチームから推測すると日本のプレイヤーでこの問題を解いたのは2人しかいなさそうです。この問題を解いたり、取り組んだけど解けなかった人はどのあたりが大変だったり難しかったのか今度教えてください。

それでは、次はSECCON CTF 2022 (Final)でお会いしましょう

文章来源: https://furutsuki.hatenablog.com/entry/2022/11/13/202646
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)