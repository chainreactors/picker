---
title: TsukuCTF 2022のWriteup
url: https://ptr-yudai.hatenablog.com/entry/2022/10/24/195448
source: CTFするぞ
date: 2022-10-25
fetch_date: 2025-10-03T20:46:14.150032
---

# TsukuCTF 2022のWriteup

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2022-10-24](https://ptr-yudai.hatenablog.com/archive/2022/10/24)

# [TsukuCTF 2022のWriteup](https://ptr-yudai.hatenablog.com/entry/2022/10/24/195448)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

SecHack部隊が旅費を稼ぐためのCTFことTsukuCTFに、チーム98ptsで[フェネック](http://d.hatena.ne.jp/keyword/%EF%BF%BD%D5%A5%EF%BF%BD%EF%BF%BD%CD%A5%C3%A5%EF%BF%BD)（ハイエナ）として参加し、チームとしては1位でした。
OSINT中心のCTFで真面目にOSINTに取り組んだのは人生初だと思います。[\*1](#f-15300a25 "AVTokyoのOSINT CTFみたいなのを1問を手伝ったことはあったけど、結局st98さんが解いてくれた。")

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221024/20221024194315.png)

チーム転職族

他のもふもふたちのwriteup

[nanimokangaeteinai.hateblo.jp](https://nanimokangaeteinai.hateblo.jp/entry/2022/10/23/180703)

[furutsuki.hatenablog.com](https://furutsuki.hatenablog.com/entry/2022/10/23/183520)

* [開催前](#開催前)
* [[Reversing] GradpaMemory](#Reversing-GradpaMemory)
* [[Hardware] DefuseBomb](#Hardware-DefuseBomb)
* [[OSINT] Attack of Tsukushi](#OSINT-Attack-of-Tsukushi)
* [[OSINT] Money](#OSINT-Money)
* [[OSINT] FlyMeToTheTsukushi](#OSINT-FlyMeToTheTsukushi)
* [[OSINT] inuyama082](#OSINT-inuyama082)
* [[OSINT] douro](#OSINT-douro)
* [[OSINT] PaperJack](#OSINT-PaperJack)
* [[OSINT] Robot](#OSINT-Robot)
* [[OSINT] Flash](#OSINT-Flash)
* [[OSINT] TakaiTakai](#OSINT-TakaiTakai)
* [[OSINT] uTSUKUSHIi](#OSINT-uTSUKUSHIi)
* [[OSINT] moon](#OSINT-moon)
* [[OSINT] what\_time\_is\_it](#OSINT-what_time_is_it)
* [[OSINT] station](#OSINT-station)
* [[OSINT] hub\_been\_stolen](#OSINT-hub_been_stolen)
* [[OSINT] FlagDM](#OSINT-FlagDM)
* [おわりに](#おわりに)

# 開催前

去年の問題を見てHardwareやReversingで何が出ているかを確認して予習しました。
それから、運営の人（おもにs氏）が報告しているCVE、触れている技術スタックなども調べました。

あとは運営の人間がここ1年以内くらいで行っている場所・住んでいる場所などをチェックしました：

* 北海道
* 福岡
* 京都
* 東京
* 名古屋

# [Reversing] GradpaMemory

```
問題文：
祖父からお誕生プレゼントが入った鍵付きの箱とa.outという名前のファイルをもらった。これを開けるには数字を入力すれば良いらしい。ヒントはこのファイルの計算結果が鍵であること、このファイルは1971年に冷蔵庫ほどもあるミニコンピューターで作成された実行ファイルであると言われた。
フラグ形式：Nは数値である。 TsukuCTF22{N}
```

謎のファイルが渡されます。

```
$ file a.out
a.out: PDP-11 old overlay
$ hexdump -C a.out
00000000  05 01 34 00 00 00 00 00  00 00 00 00 01 0a 02 0a  |..4.............|
00000010  81 0a 82 0a c1 0c c1 0c  c1 0c c1 0c c2 0c 42 60  |..............B`|
00000020  ff 01 70 61 73 73 77 64  20 69 73 20 69 6e 20 52  |..passwd is in R|
00000030  32 20 00 0a                                       |2 ..|
00000034
```

[PDP](http://d.hatena.ne.jp/keyword/PDP)-11というのは昔のミニ(大嘘)コンピュータだそうです。

`passwd is in R2` という文字列があるので、プログラム実行後のR2[レジスタ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EC%A5%B8%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の中身がフラグになりそうです。

調べると[pdp11dasm](https://github.com/caldwell/pdp11dasm/)という逆[アセンブラ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D6%A5%EF%BF%BD)があります。
この手のREADMEがただのテキストファイルのツールは動かないがちですが、今回は動いてくれました。

```
;
; pdp11dasm version 0.0.3
; disassembly of ../a.out
;
000000: 000405                  br      14                      ; ..
;
000002: 000064                  invalid opcode                  ; 4.
000004: 000000                  halt                            ; ..
000006: 000000                  halt                            ; ..
000010: 000000                  halt                            ; ..
000012: 000000                  halt                            ; ..
;
000014: 005001                  clr     r1                      ; ..
000016: 005002                  clr     r2                      ; ..
000020: 005201                  inc     r1                      ; ..
000022: 005202                  inc     r2                      ; ..
000024: 006301                  asl     r1                      ; A.
000026: 006301                  asl     r1                      ; A.
000030: 006301                  asl     r1                      ; A.
000032: 006301                  asl     r1                      ; A.
000034: 006302                  asl     r2                      ; B.
000036: 060102                  add     r1,r2                   ; B`
000040: 000777                  br      40                      ; ..
;
000042: 060560 071563           add     r5,71563(r0)            ; pass
000046: 062167 064440           add     (r1)+,64512             ; wd i
000052: 020163 067151           cmp     r1,67151(r3)            ; s in
000056: 051040                  bis     (r0),-(r0)              ;  R
000060: 020062 005000           cmp     r0,5000(r2)             ; 2 ..
```

`clr`はゼロクリア、`inc`はインクリメント、`asl`は左1ビットシフト、`add`は加算だそうです。
これを実行するとR2には18が入るはずです。

最初`TsukuCTF{22}`が一生受理されずに悩んでいましたが、あとでフォーマットが`TsukuCTF22`でした連絡が来て解決しました。
シフト演算ができなくなったかと思って、あやうく義務教育をやり直すべく幼稚園に入園届を出すところでした。

# [Hardware] DefuseBomb

```
問題文：
つくしくんは疑似時限爆弾解除競技の訓練として、３つの時限爆弾に関するそれぞれのデータ(DefBom1,DefBom2は回路図、DefBom3は基板製造データ)をもとに、３つそれぞれの爆弾解除を行う。各時限爆弾はタイマー(limit_timer)がON状態になったとき、爆弾(bomb)に電流が流れて爆発する。
切断可能な線はデータ内で示されており、DefBom1では１から６の番号が振られたハサミ、DefBom2 では１から５の番号が振られたハサミ, DefBom3 では１から５の番号が振られた矢印である。示された切断可能な線のうち、１つの線を切れば limit_timer が ON 状態になっても爆発せず解除に成功する。しかし、残りの線は切っても limit_timer が ON 状態になる、もしくは切断した瞬間に爆発する。

フラグ形式はTsukuCTF22{ここにDefbom1からDefbom3において切断した番号を順に書く}といった形です。例として、切断した線の番号が DefBom1 では"3"、DefBom2"では"1"、DefBom3 では"5"であった場合フラグ形式はTsukuCTF22{315}となります。

この問題は3回までフラグを提出できます。タイプミス等が無いように注意してフラグを提出して下さい！！
```

信号雷管（に電流を流すまでの嫌がらせ用の）の回路が、最初の2つは回路図の画像で、3つ目は基盤のガーバーデータで渡されます。
各回路のうちいくつかの配線には番号があり、そのどれかを切断すればスイッチがONになっても起爆しないらしいです。

1つ目：

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221023/20221023131413.jpg)

bombと書いてある赤い部分が接地されていると仮定し、スイッチがONになった際にbombに電流が流れないようにします。
それならbombの手前の線を切れよとずっと思っていましたが、そこは巧妙に隠されているのでしょう。

[TC74HC08AP](https://akizukidenshi.com/download/ds/Toshiba/TC74HC08AP.pdf)はANDゲートで、[TC74HC02AP](https://akizukidenshi.com/download/ds/Toshiba/TC74HC02AP.pdf)はNORゲートです。
発火部分から逆算するとわかりやすいです。

```
U3_pin1
= not (U3_pin2 or U3_pin3)
= not [(U1_pin12 and U1_pin13) or (U1_pin1 and U1_pin2)]
= not [U1_pin12 or (L and U1_pin2)]
= not U1_pin12
= not not (U3_pin8 or U3_pin9)
= SW1
```

したがって、U3の9ピンとスイッチをつなぐ4番の配線を切れば解除できます。

2つ目：

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221023/20221023132723.jpg)

[IRF3205](https://www.alldatasheet.jp/datasheet-pdf/pdf/68131/IRF/IRF3205.html)はN型の[MOSFET](http://d.hatena.ne.jp/keyword/MOSFET)です。

bombの抵抗がIRF3205のR\_DSよりも十分に大きいと仮定する[\*2](#f-fdb61a59 "bomb側に抵抗を挟むと場合によっては発火しないと思うので、bomb側にもトランジスタをかますなど工夫が要りそう")と、[トランジスタ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%A5%EF%BF%BD%F3%A5%B8%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)Q7,Q8のD-Sに電流を流すためにQ7,Q8両方のG-S間に電圧をかければ良いことが分かります。

まずQ7ですが、3番配線がつながっている限り、つねにG-S間に電圧がかかるので問題ないように見えます。
3番に電流を流すにはQ5,Q6のD-Sに電流が流れない必要があります。
よく見るとQ6は常にG-S間の電位差が0なので、1番と2番の配線は切っても切らなくても変わりません。[\*3](#f-66067ff8 "これが原因で上側の回路が虚無になっており、あまりに不安だったのでこの回路は念の為シミュレータで動作確認しました。命大切に。")

次にQ8ですが、こちらも5番配線がつながっている限り、つねにG-S間に電圧がかかります。
5番に電流を流すにはQ3,Q4のD-Sに電流が流れない必要があります。
4番を切るとQ3,Q4ともにG-S間の電位差がなくなるので、5番に電流が流れてくれます。

したがって、4番の配線を切ればbomb側に電流は流れません。

3つ目：

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221023/20221023134222.png)

上の図はガーバーデータをKiCadで開いて見やすくしたものです。

[TC74HC00AP](https://akizukidenshi.com/download/ds/toshiba/TC74HC00A.pdf)はNANDゲートです。
これも1つ目の回路と同様にbomb側から逆算します。

```
pin6
= not (pin5 and pin4)
= not [(not (L and pin6)) and (not (pin2 and pin1))]
= not [H and not pin1]
= pin1
= SW
```

つまり、1ピンとスイッチをつなぐ2番の配線を切れば解除できます。

```
TsukuCTF22{442}
```

# [OSINT] Attack of Tsukushi

```
問題文：
つくしくんはある観光地を調査した際に訪れた駅で写真を撮影した。果たしてこの写真が撮られた駅はどこだろうか？ フラグは駅の郵便番号（ハイフンなし）を入力して下さい
e.g. 東京駅の場合は郵便番号が100-...