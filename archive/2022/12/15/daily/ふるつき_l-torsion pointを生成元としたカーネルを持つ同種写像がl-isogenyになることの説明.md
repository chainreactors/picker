---
title: l-torsion pointを生成元としたカーネルを持つ同種写像がl-isogenyになることの説明
url: https://furutsuki.hatenablog.com/entry/2022/12/14/142139
source: ふるつき
date: 2022-12-15
fetch_date: 2025-10-04T01:31:38.008163
---

# l-torsion pointを生成元としたカーネルを持つ同種写像がl-isogenyになることの説明

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2022-12-14](https://furutsuki.hatenablog.com/archive/2022/12/14)

# [l-torsion pointを生成元としたカーネルを持つ同種写像がl-isogenyになることの説明](https://furutsuki.hatenablog.com/entry/2022/12/14/142139)

伝わるようなタイトルを考えるのが難しすぎる！

同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)計算の基本命題[\*1](#f-1b15f733 "初めてこれを知った https://joint.imi.kyushu-u.ac.jp/wp-content/uploads/2022/08/220802_03aikawa.pdf での呼称を使ってますが、もうちょっと名前っぽい名前がありそうな気がする")というやつがあって、詳しくは説明しないんですが主張としては、

（有限体上の）[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ E](https://chart.apis.google.com/chart?cht=tx&chl=%20E)を定義域とする同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ \phi: E \to E'](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi%3A%20E%20%5Cto%20E%27)（とその終域![ E'](https://chart.apis.google.com/chart?cht=tx&chl=%20E%27)）は![ E](https://chart.apis.google.com/chart?cht=tx&chl=%20E)と代数閉包上の[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ E(\bar{\mathbb{F_p}})](https://chart.apis.google.com/chart?cht=tx&chl=%20E%28%5Cbar%7B%5Cmathbb%7BF_p%7D%7D%29)の有限部分群![ C](https://chart.apis.google.com/chart?cht=tx&chl=%20C)から同型を除いて一意に定まり、![ \ker \phi = C](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cker%20%5Cphi%20%3D%20C)である

というものです。

つまり、適当な[楕円曲線](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CA%B1%DF%B6%EF%BF%BD%EF%BF%BD%EF%BF%BD)と同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の核にしたい群があれば同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)が決まります。さらにここで核にしている![ C](https://chart.apis.google.com/chart?cht=tx&chl=%20C)が[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)位数なら、![ C](https://chart.apis.google.com/chart?cht=tx&chl=%20C)の代わりにその生成元![ H](https://chart.apis.google.com/chart?cht=tx&chl=%20H)だけあれば良いです（そしてVéluの公式などで![ E, H](https://chart.apis.google.com/chart?cht=tx&chl=%20E%2C%20H)から![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)を具体的に計算できます）。

この時![ H](https://chart.apis.google.com/chart?cht=tx&chl=%20H)が![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-torsion pointであれば、![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)は![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-isogenyとなるのですが、その理屈がわからなくて考えたので説明します。

---

というわけで[素数](http://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%BF%EF%BF%BD)![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)を位数とする適当な点![ H \in E(\bar{\mathbb{F_p}})](https://chart.apis.google.com/chart?cht=tx&chl=%20H%20%5Cin%20E%28%5Cbar%7B%5Cmathbb%7BF_p%7D%7D%29)をとってきて、![ H](https://chart.apis.google.com/chart?cht=tx&chl=%20H)が生成する[巡回群](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ \langle H \rangle](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Clangle%20H%20%5Crangle)を核とする同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)を求めたとします。

この時、![ \deg \phi = \#\langle H \rangle = l](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cdeg%20%5Cphi%20%3D%20%5C%23%5Clangle%20H%20%5Crangle%20%3D%20l)が成り立ちます[\*2](#f-44ce9a8f "書いてなかったけど[tex: \phi]は有理多項式なので次数が定まります")。なぜなら、![ \ker \phi = \lbrace H, 2H, \dots, (l-1)H ,lH \rbrace](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cker%20%5Cphi%20%3D%20%5Clbrace%0AH%2C%202H%2C%20%5Cdots%2C%20%28l-1%29H%20%2ClH%20%5Crbrace) より![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)は![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)個の根を持ち、![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)個の根を持つためには![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)は![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)次の[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)である必要があるからです。

従って、![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-torsion point ![ H](https://chart.apis.google.com/chart?cht=tx&chl=%20H)を生成元とした[カーネル](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%CD%A5%EF%BF%BD)を持つ同種[写像](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)は![ l](https://chart.apis.google.com/chart?cht=tx&chl=%20l)-isogenyです

……という理屈で私は納得したけど、皆さんはどうですか。ミスってるよとか行間がデカすぎるとか、ここに厳密な証明書いてありますよとかあれば教えてください。

[\*1](#fn-1b15f733):初めてこれを知った <https://joint.imi.kyushu-u.ac.jp/wp-content/uploads/2022/08/220802_03aikawa.pdf> での呼称を使ってますが、もうちょっと名前っぽい名前がありそうな気がする

[\*2](#fn-44ce9a8f):書いてなかったけど![ \phi](https://chart.apis.google.com/chart?cht=tx&chl=%20%5Cphi)は有理[多項式](http://d.hatena.ne.jp/keyword/%C2%BF%EF%BF%BD%E0%BC%B0)なので次数が定まります

Furutsuki
[2022-12-14 14:21](https://furutsuki.hatenablog.com/entry/2022/12/14/142139)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_medium=button&utm_source=blogs_entry_footer)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2022/12/14/142139 "この記事をはてなブックマークに追加")

関連記事

* [![TSGCTF 2023参加記](https://cdn.image.st-hatena.com/image/square/16c86559a3a78e67f44258cd91e37a824dd44616/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2FF%2FFurutsuki%2F20231112%2F20231112115543.png "TSGCTF 2023参加記")](https://furutsuki.hatenablog.com/entry/2023/11/12/121722)

  [2023-11-12](https://furutsuki.hatenablog.com/archive/2023/11/12)

  [TSGCTF 2023参加記](https://furutsuki.hatenablog.com/entry/2023/11/12/121722)

  TSGCTF 2023にzer0ptsとして参加していました。これという問題…
* [![secure Prime Generator writeup - Codegate CTF 2023 Preliminary](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "secure Prime Generator writeup - Codegate CTF 2023 Preliminary")](https://furutsuki.hatenablog.com/entry/2023/06/23/003640)

  [2023-06-23](https://furutsuki.hatenablog.com/archive/2023/06/23)

  [secure Prime Generator writeup - Codegate CTF 2023…](https://furutsuki.hatenablog.com/entry/2023/06/23/003640)

  サーバ側で何やら素数（？）を2つ生成して、さらにそれを加工し…
* [![Ricerca CTF 2023 writeup / upsolve](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "Ricerca CTF 2023 writeup / upsolve")](https://furutsuki.hatenablog.com/entry/2023/04/23/143704)

  [2023-04-23](https://furutsuki.hatenablog.com/archive/2023/04/23)

  [Ricerca CTF 2023 writeup / upsolve](https://furutsuki.hatenablog.com/entry/2023/04/23/143704)

  CTF日本最強企業であるところのリチェルカセキュリティが開催し…
* [![楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク")](https://furutsuki.hatenablog.com/entry/2023/01/18/144400)

  [2023-01-18](https://furutsuki.hatenablog.com/archive/2023/01/18)

  [楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク](https://furutsuki.hatenablog.com/entry/2023/01/18/144400)

  最近このテクを使う問題をいくつか解いたのでメモ。楕円曲線と…
* [![点の位数を整えるテク](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918a...