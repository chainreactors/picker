---
title: Best Pwnable Challenges 2022
url: https://ptr-yudai.hatenablog.com/entry/2022/12/06/123436
source: CTFするぞ
date: 2022-12-07
fetch_date: 2025-10-04T00:39:23.918178
---

# Best Pwnable Challenges 2022

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2022-12-06](https://ptr-yudai.hatenablog.com/archive/2022/12/06)

# [Best Pwnable Challenges 2022](https://ptr-yudai.hatenablog.com/entry/2022/12/06/123436)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)

# はじめに

この記事は[CTF Advent Calendar 2022](https://adventar.org/calendars/7550)の6日目の記事です。
昨日はEdwow Mathさんの「[Cryptoプレーヤーを始めてから今までで躓いたポイントとその解消法](https://m5453.hatenablog.com/entry/2022/12/05/011648)」でした。
前後をcrypto記事で挟まれてオセロなら負けてた。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221206/20221206123901.png)
[\*1](#f-f2a056d0 "深淵")

さて、去年の[Best Pwnable Challenges 2021](https://ptr-yudai.hatenablog.com/entry/2021/12/06/001931)に引き続き、主観で面白かったpwn問を選んでみます。
私が今年参加したCTFかつ解いた問題から選んでいるので、ご了承ください。[\*2](#f-9dffa718 "今年ほとんどCTF参加してないけど。")
参加CTF数が少ないのかpwnに飽きたのか、「これは誰が見ても面白い」みたいな問題があまり見つからなかったので、賛否両論だと思います。

* [はじめに](#はじめに)
* [受賞作品一覧](#受賞作品一覧)
  + [corchat - 創造力賞](#corchat---創造力賞)
    - [概要と解説](#概要と解説)
    - [コメント](#コメント)
  + [shamav - 脆弱性賞](#shamav---脆弱性賞)
    - [概要と解説](#概要と解説-1)
    - [コメント](#コメント-1)
  + [mykvm - 教育賞](#mykvm---教育賞)
    - [概要と解説](#概要と解説-2)
    - [コメント](#コメント-2)
  + [その他の良問](#その他の良問)

# 受賞作品一覧

## corchat - 創造力賞

創造力賞（Creativity Award）：解法がもっとも独創的だった問題に与えられる賞

[github.com](https://github.com/Crusaders-of-Rust/corCTF-2022-public-challenge-archive/tree/master/pwn/corchat)

### 概要と解説

最初に紹介するのがcorCTF 2022で出題されたcorchatという問題です。[Crusaders of Rust](https://cor.team/)のjazzpizazzさんとryaagardさんが作ったそうです。
問題内容は以下のwriteupをご覧ください。

[ptr-yudai.hatenablog.com](https://ptr-yudai.hatenablog.com/entry/2022/08/08/144339#pwn-corchat)

### コメント

スレッドのスタックからmaster canaryを書き換えるという問題はたまに見ますが、NULLバイト書き込みで1バイトずつcanaryを消していくという発想が面白かったです。
corCTFはあまり参加していませんが、他にも面白い問題があったそうなので要チェックですね。

## shamav - [脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)賞

[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)賞（[Vulnerability](http://d.hatena.ne.jp/keyword/Vulnerability) Award）：[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)がもっとも巧妙かつ自然に隠されていた問題に与えられる賞

### 概要と解説

次に紹介するのがSan Diego CTF 2022のshamavです。この問題は一般的なpwnと違い、[ファイルシステム](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B7%EF%BF%BD%EF%BF%BD%EF%BF%BD%C6%A5%EF%BF%BD)に関する知識が問われるmisc寄りの問題です。k3v1nさんが作問しています。

内容ですが、[Python](http://d.hatena.ne.jp/keyword/Python)製のしょぼい[アンチウイルス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B9)を実装したサービスになっています。
検査したいファイルパスはソケット経由で送信します。

```
def scan(path: str):
    res = _scan(path)
    log(f'[I] Scan complete: {path}')
    return res
...
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            try:
                os.unlink(SOCKET_FILE)
            except FileNotFoundError:
                pass
            s.bind(SOCKET_FILE)
            os.chmod(SOCKET_FILE, 0o777)
            s.listen()
            while True:
                log(f'[I] Ready for the next client')
                conn, _ = s.accept()
                res = scan(recvall(conn).decode(errors='surrogateescape'))
                log(f'[I] Scan result: {res}')
                try:
                    conn.sendall(res.encode())
                except OSError as e:
                    log(f'[E] OS error on sendall: {e}')
```

スキャンは単純に[ハッシュ値](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A5%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を比較する実装になっています。
[ハッシュ値](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A5%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)が一致すれば、該当ファイルを別[ディレクト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%A5%EF%BF%BD%EF%BF%BD%EC%A5%AF%EF%BF%BD%EF%BF%BD)リに隔離するような実装になっています。

```
def is_malware(file: str):
    with open(file, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest() in malware_hashes

def _scan(path: str):
    log(f'[I] Scanning file {path}')
    try:
        if os.lstat(path).st_uid != USER_UID:
            return "You do not have permission to scan this item"
    except OSError as e:
        return f'Error from OS: {e}'
    target_path = f'/home/antivirus/quarantine/sham-av-{genrandom()}'
    log(f'[D] Copying file from {path} to {target_path}')
    try:
        shutil.copyfile(path, target_path)
        if is_malware(target_path):
            log(f'[I] Found malware at {path}')
            return f'***** Malware detected! File quarantined at {target_path} *****'
    except IsADirectoryError as e:
        return f'An error occurred: {e}'
    return "File scan completed. No malware detected."
```

[アンチウイルス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B9)はantivirusユーザーで実行されており、我々はctfユーザーにいます。
Dockerfileは配布されていませんでしたが、リモートの様子を再現すると次のような権限になっています。

```
RUN chown antivirus:antivirus *
RUN chmod 755 launcher.sh
RUN chmod 755 server.py
RUN chmod 644 malware-hashes.txt
```

あとあんまり覚えてないですが、`quarantine`[ディレクト](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%A5%EF%BF%BD%EF%BF%BD%EC%A5%AF%EF%BF%BD%EF%BF%BD)リは実行権限はないですが、他ユーザーにも読み書きの権限はあったと思います。

[Python](http://d.hatena.ne.jp/keyword/Python)製ということもありTOCTOUが[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)なのは明らかですが、何をどう競合させるかで結構悩んだ記憶があります。
[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)が明らかなのに[脆弱性](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)賞なのかという感じですが、コードが小さい割にどう利用するかで結構悩んだので......

目標としては、以下のコードを悪用します。

```
shutil.copyfile(path, target_path)
```

`copyfile`はdstが[シンボリックリンク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%DC%A5%EF%BF%BD%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)のとき、リンク先にsrcの内容を上書きします。
もしdstに任意の[シンボリックリンク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%DC%A5%EF%BF%BD%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)が置ければ、[アンチウイルス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B9)のコードそのものを上書きできます。
`server.py`は何らかの原因でクラッシュすると自動的に再起動するようになっているため、もし`server.py`を書き換えられればantivirus権限が得られます。
実際、[FIFO](http://d.hatena.ne.jp/keyword/FIFO)をスキャンさせると落ちるため、antivirus権限でのコード実行は実現可能です。

さて、問題はdstに[シンボリックリンク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%DC%A5%EF%BF%BD%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を置けるかですが、宛先ファイル名は次のように生成されています。

```
with open('seed') as f:
    seed = base64.b64decode(f.read())

def genrandom():
    global ctr
    result = hashlib.sha256(ctr.to_bytes(CTR_LENGTH, byteorder='little') + seed).hexdigest()
    ctr += 1
    return result
...
target_path = f'/home/antivirus/quarantine/sham-av-{genrandom()}'
```

当然seedは読めませんし、[アンチウイルス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B9)が再起動するとseedは新しい乱数列で置き換わります。
想定解はこのseedをTOCTOUで置き換えるらしいのですが、今回は非想定解を使いました。

今回のプログラムは、`av.log`にログを吐きまくります。

```
    target_path = f'/home/antivirus/quarantine/sham-av-{genrandom()}'
    log(f'[D] Copying file from {path} to {target_path}')
```

このコードから分かるように、実は`shutil.copy`の直前でログに`target_path`が書き込まれています。

したがって、ログにファイル名が書き込まれてからコピーが走るまでの間に、ログからファイル名を取り出して[シンボリックリンク](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%DC%A5%EF%BF%BD%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)で置き換えることができれば優勝です。
サーバー[インスタンス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%F3%A5%B9%A5%EF%BF%BD%EF%BF%BD%...