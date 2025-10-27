---
title: RTACTF 2023 春 - 並走感想
url: https://furutsuki.hatenablog.com/entry/2023/03/21/222826
source: ふるつき
date: 2023-03-22
fetch_date: 2025-10-04T10:14:36.986046
---

# RTACTF 2023 春 - 並走感想

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2023-03-21](https://furutsuki.hatenablog.com/archive/2023/03/21)

# [RTACTF 2023 春 - 並走感想](https://furutsuki.hatenablog.com/entry/2023/03/21/222826)

長時間CTFに飽いた強者たちの遊びことRTACTFの第２回が開催されました。前回は走者として参加しましたが、今回は私は走者を退いて一参加者として参戦しました。だこつさんの画面が見たかったので……

というわけで並走writeupです。当日の[アーカイブ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)はこちら

* [XOR-CBC](#XOR-CBC)
* [Collision-DES](#Collision-DES)
* [Reused AES](#Reused-AES)
* [1R-AES](#1R-AES)
* [感想](#感想)

## XOR-[CBC](http://d.hatena.ne.jp/keyword/CBC)

目標タイム： 480秒
記録： 560.06秒（4位）

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230321/20230321212931.png)

与えられている暗号化[スクリプト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)は長いので省略しますが、次の図のような暗号化が行われていて、平文の先頭は `RTACTF{` であることが保証されているので既知です。

```
XOR-CBC Explained:

     plain 0       plain 1       plain 2
        |             |             |
        v             v             v
IV --> XOR  +------> XOR  +------> XOR
        |   |         |   |         |
        v   |         v   |         v
key -> XOR  | key -> XOR  | key -> XOR
        |   |         |   |         |
        +---+         +---+         |
        |             |             |
        v             v             v
[IV] [cipher 0]    [cipher 1]    [cipher 2]
```

`cipher 0` は ![ cipher_0 = IV \oplus key \oplus plain_0](https://chart.apis.google.com/chart?cht=tx&chl=%20cipher_0%20%3D%20IV%20%5Coplus%20key%20%5Coplus%20plain_0)

読めるフラグを256通りの中から探すのに失敗して、パディングが正常かどうかを見ればよいのに気がつくのに時間をかけてしまって目標タイムに届かなかったのが無念でした。

```
from ptrlib import chunks, xor
cipher = chunks(bytes.fromhex("6528337d61658047295cef0310f933eb681e424b524bcc294261bd471ca25bcd6f3217494b1ca7290c158d7369c168b3"), 8)

iv, cipher = cipher[0], cipher[1:]

for x in range(256):
    plain = b"RTACTF{" + bytes([x])
    k = xor(iv, xor(cipher[0], plain))

    last_c = cipher[0]

    m = plain
    for c in cipher[1:]:
        m += xor(c, xor(last_c, k))
        last_c = c

    if m[-1] == 7:
        print(m)
```

## Collision-DES

目標タイム： 720秒
記録： 529.61 秒（3位）

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230321/20230321220106.png)

```
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

FLAG = os.getenv("FLAG", "RTACTF{**** REDACTED ****}")

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 8))

if __name__ == '__main__':
    key1 = os.urandom(8)
    print(f"Key 1: {key1.hex()}")
    key2 = bytes.fromhex(input("Key 2: "))

    assert len(key1) == len(key2) == 8, "Invalid key size :("
    assert len(set(key1).intersection(set(key2))) == 0, "Keys look similar :("

    plaintext = b"The quick brown fox jumps over the lazy dog."
    if encrypt(key1, plaintext) == encrypt(key2, plaintext):
        print("[+] You found a collision!")
        print(FLAG)
    else:
        print("[-] Nope.")
```

DESで、相異なる2つの鍵で1つの平文を暗号化して同一の平文になることがありますか？　という問題です。まあそういうことがあることもあると思うけど、平文が固定されているので流石にそんなペアを見つけることはできないでしょう。となると、違う鍵に見えて実は同じ挙動をする鍵になっている必要があって、こういうときにDESでは鍵は64bit中の56bitしか使われないという話を思い出します。

[Wikipedia](http://d.hatena.ne.jp/keyword/Wikipedia)でそのエピソードを調べて、「じゃあどのbitが使われないのか調べにDESの実装見に行くか」をしかけたところで「RTACTFでそんなことしてる暇ないだろ」と思い直して、鍵を1バイトずつ変化させて同じになるペアを探す、という方針に切り替えました。これがうまくハマったのは良かった。各バイトのLSBがそうというのは全然気がついていませんでした。

```
from ptrlib import Socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

sock = Socket("nc 35.194.118.87 7002")
key1 = bytes.fromhex(sock.recvlineafter("1: ").decode())

plaintext = b"The quick brown fox jumps over the lazy dog."
key2 = list(key1)

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 8))

for i in range(8):
    for c in range(256):
        if c == key1[i]:
            continue

        key2[i] = c
        if encrypt(key1, plaintext) == encrypt(bytes(key2), plaintext):
            print("found")
            break
    else:
        print("not found")
        quit()

print(key1.hex())
print(bytes(key2).hex())
sock.sendlineafter("2: ", bytes(key2).hex())
sock.interactive()
```

ところでこの問題の `len(set(key1).intersection(set(key2))) == 0` という制約だと`key1` に最下位bitのみがことなる2バイトがあるときに問題が解けなくなってしまうので、普通に1バイトずつ比較して同じのがあったらだめ、ということにしたら良かったと思います

## Reused AES

目標タイム： 1080秒
記録： 1966.67秒（4位）

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230321/20230321220033.png)

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

iv = os.urandom(16)
key = os.urandom(16)
FLAG = os.getenv("FLAG", "RTACTF{**** REDACTED ****}").encode()

def encrypt(data):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(pad(data, 16))

if __name__ == '__main__':
    print(encrypt(FLAG).hex())
    print(encrypt(input("> ").encode()).hex())
```

シンプルな問題で良いですね。CFBという文字を見た瞬間に「暗号利用モード」で検索しました。

なんか[Wikipedia](http://d.hatena.ne.jp/keyword/Wikipedia)に書いてある挙動と違ってデータが1バイトずつ処理されていそうであるだとか、サーバが入力を受け付けるときはhex encodingされていない想定であるだとかにひっかかって無限に時間を浪費していましたが、とりあえず `\0` を暗号化すれば1バイト目のストリームキーが手に入るので、あとは既知の平文と`\0` を組み合わせて1バイトずつ特定しました。

```
from ptrlib import Socket, xor

l = 1
known = b""

while len(known) < l:

    sock = Socket("nc 35.194.118.87 7001")
    # sock = Socket("nc localhost 9999")
    a = bytes.fromhex(sock.recvline().decode())
    if l == 1:
        l = len(a)

    sock.sendlineafter("> ", (known + b"\0" * (len(a) - len(known))))
    y = bytes.fromhex(sock.recvline().decode())
    m = xor(a, y)[len(known)]
    print(bytes([m]))
    sock.close()
    known = known + bytes([m])
    print(known)
```

## 1R-AES

目標：1320秒
記録：3030.96秒（7位）

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230321/20230321221025.png)

```
import aes
import os

key = os.getenv("KEY", "*** REDACTED ***").encode()
assert len(key) == 16

flag = os.getenv("FLAG", "RTACTF{*** REDACTED ***}")
assert flag.startswith("RTACTF{") and flag.endswith("}")
la = flag[len("RTACTF{"):-len("}")]
assert len(la) == 16

cipher = aes.AES(key)
print("enc(la):", cipher.encrypt_block(la.encode()).hex())

while True:
    cipher = aes.AES(key)
    plaintext = bytes.fromhex(input("msg > "))
    assert len(plaintext) == 16
    print("enc(msg):", cipher.encrypt_block(plaintext).hex())
```

AESの実装は [aes/aes.py at d6857518fa95f08352a250242b0cf21d2544e470 · boppreh/aes · GitHub](https://github.com/boppreh/aes/blob/d6857518fa95f08352a250242b0cf21d2544e470/aes.py)ですが、ラウンド数が1になるように改造されています。

1ラウンドだと以下の処理のループの部分が一回も回らないので、処理は `add_round_key` `sub_bytes` `shift_rows` `add_round_key` のみ、未知の値は16バイト x 2個のラウンド鍵のみになります。

```
    def encrypt_block(self, plaintext):
        """
        Encrypts a single block of 16 byte long plaintext.
        """
        assert len(plaintext) == 16

        plain_state = bytes2matrix(plaintext)

        add_round_key(plain_state, self._key_matrices[0])

        for i in range(1, self.n_rounds):
            sub_bytes(plain_state)
            shift_rows(plain_state)
            mix_columns(plain_state)
            add_round_key(plain_state, self._key_matrices[i])

        sub_bytes(plain_state)
        shift_rows(plain_state)
        add_round_key(plain_state, self._key_matrices[-1])

        return matrix2bytes(plain_state)
```

解いてるときはAES, 少ラウンド数, Chosen-Plaintext Attack可能 → はい内部状態を求めるんですね、になりましたが意外と想定は平文があっているかを前から見ればよかったらしいです。ブロック単位で処理してるからだめだろうな〜と思ってその選択肢は捨ててました……。

とりあえずラウンド数の少な...