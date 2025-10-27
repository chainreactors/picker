---
title: zer0pts秘伝のcrypto-writeupを公開します
url: https://furutsuki.hatenablog.com/entry/2022/12/04/105458
source: ふるつき
date: 2022-12-05
fetch_date: 2025-10-04T00:30:45.203594
---

# zer0pts秘伝のcrypto-writeupを公開します

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2022-12-04](https://furutsuki.hatenablog.com/archive/2022/12/04)

xml version="1.0" encoding="UTF-8"?最終更新日

2023-12-18

# [zer0pts秘伝のcrypto-writeupを公開します](https://furutsuki.hatenablog.com/entry/2022/12/04/105458)

タイトルは盛りました。zer0ptsのFurutsukiです。

2019年ごろから個人的なwriteupあるいはupsolveのためにcrypto-writeupという名前で[scrapbox](https://d.hatena.ne.jp/keyword/scrapbox)を作って、知見をためて[チートシート](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%C8%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)的に使ったりしていました。あんまりちゃんとやっていたわけではないんですが、いまではだいたい800ページくらいに成長していて、問題を考えるときや解くときに重宝することもあります。

ある程度記事が溜まったあとはチームメイトにも公開して、zer0ptsの幾人かにもいくつかテクや知見を寄せてもらっていてなかなか価値のあるものに仕上がってきているのではないかと思います。

しかし昨年末くらいからはあまり時間が取れず、内容としては古くなってきてしまい価値が失われているなどの問題があり、秘匿することによってチームが得られるメリットも少なくなってしまいました。これ以上秘匿していてもだんだん滅びて価値を失うだけと考えて、この機会にcrypto-writeupを公開することにしました。もはやあんまり大した内容はないですが、cryptoを始めたばかりの人などに役立ててもらえればと思っています

以下免責事項です

* 半分くらいのページは書きかけまたはタイトルだけのような状況です
* 個人的に書いていたものなので間違いや不正確な理解があるかもしれません
* 特定の問題をけなすような表現があることがあります

それでもよければこちらからどうぞ（もとの[Scrapbox](https://d.hatena.ne.jp/keyword/Scrapbox)から[はてなブログ](https://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)に作り直しました）

[crypto-writeup-public.hatenablog.com](https://crypto-writeup-public.hatenablog.com/)

crypto-writeup自体は今後もチームで記事を細々とかいて行こうと思います、内容は適宜publicにも反映します

この記事は[CTF Advent Calendar](https://adventar.org/calendars/7550)の4日目の記事です。まだうまってないのでみんな書いてくれ！

Furutsuki
[2022-12-04 10:54](https://furutsuki.hatenablog.com/entry/2022/12/04/105458)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_medium=button&utm_source=blogs_entry_footer)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2022/12/04/105458 "この記事をはてなブックマークに追加")

関連記事

* [![CakeCTF 2023 作問感想](https://cdn.image.st-hatena.com/image/square/57b921967799a0175cea068c449b1d1e0dd09b71/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2FF%2FFurutsuki%2F20231116%2F20231116015150.png "CakeCTF 2023 作問感想")](https://furutsuki.hatenablog.com/entry/2023/11/16/015259)

  [2023-11-16](https://furutsuki.hatenablog.com/archive/2023/11/16)

  [CakeCTF 2023 作問感想](https://furutsuki.hatenablog.com/entry/2023/11/16/015259)

  この記事はCTF AdventCalendarの-15日目の記事です こんにちは…
* [![TSGCTF 2023参加記](https://cdn.image.st-hatena.com/image/square/16c86559a3a78e67f44258cd91e37a824dd44616/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2FF%2FFurutsuki%2F20231112%2F20231112115543.png "TSGCTF 2023参加記")](https://furutsuki.hatenablog.com/entry/2023/11/12/121722)

  [2023-11-12](https://furutsuki.hatenablog.com/archive/2023/11/12)

  [TSGCTF 2023参加記](https://furutsuki.hatenablog.com/entry/2023/11/12/121722)

  TSGCTF 2023にzer0ptsとして参加していました。これという問題…
* [![zer0pts CTF 2023](https://cdn.image.st-hatena.com/image/square/5825958ee43f2b3f8f0ee96f782ff75e53ab4fca/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2FF%2FFurutsuki%2F20230719%2F20230719012214.png "zer0pts CTF 2023")](https://furutsuki.hatenablog.com/entry/2023/07/19/023705)

  [2023-07-19](https://furutsuki.hatenablog.com/archive/2023/07/19)

  [zer0pts CTF 2023](https://furutsuki.hatenablog.com/entry/2023/07/19/023705)

  私の所属するzer0ptsというチームで、zer0pts CTF 2023というCT…
* [![楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク")](https://furutsuki.hatenablog.com/entry/2023/01/18/144400)

  [2023-01-18](https://furutsuki.hatenablog.com/archive/2023/01/18)

  [楕円曲線上の複数の点からその曲線のパラメータを思考停止で求めるテク](https://furutsuki.hatenablog.com/entry/2023/01/18/144400)

  最近このテクを使う問題をいくつか解いたのでメモ。楕円曲線と…
* [![TsukuCTF 2022 writeup ](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "TsukuCTF 2022 writeup ")](https://furutsuki.hatenablog.com/entry/2022/10/23/183520)

  [2022-10-23](https://furutsuki.hatenablog.com/archive/2022/10/23)

  [TsukuCTF 2022 writeup](https://furutsuki.hatenablog.com/entry/2022/10/23/183520)

  "This is a CTF with Japanese OSINT as the main genre." とい…

* もっと読む

コメントを書く

[«
点の位数を整えるテク](https://furutsuki.hatenablog.com/entry/2022/12/13/131802)

[HITCON CTF 2022 writeup
 »](https://furutsuki.hatenablog.com/entry/2022/12/03/172249)

プロフィール

[![id:Furutsuki](https://cdn.profile-image.st-hatena.com/users/Furutsuki/profile.png?1503402472)](https://furutsuki.hatenablog.com/about)

[id:Furutsuki](https://furutsuki.hatenablog.com/about)
[*はてなブログPro*](https://blog.hatena.ne.jp/-/pro?plus_via=blog_plus_badge&utm_source=pro_badge&utm_medium=referral&utm_campaign=register_pro "はてなブログPro")

最終更新:
2025-07-27 22:32

株式会社はてなで働いています

読者です
読者をやめる

読者になる
読者になる

[このブログについて](https://furutsuki.hatenablog.com/about)

検索

ランダムに記事を表示

🔄

[最新記事](https://furutsuki.hatenablog.com/archive)

* [SECCON Beginners CTF 2025 writeup](https://furutsuki.hatenablog.com/entry/2025/07/27/223211)
* [AlpacaHack Round 12 (Crypto) - writeup](https://furutsuki.hatenablog.com/entry/2025/07/06/234110)
* [2024年に読み始めて面白かったWeb小説](https://furutsuki.hatenablog.com/entry/2024/12/28/190330)
* [AlpacaHack Round 3 (Crypto) writeup](https://furutsuki.hatenablog.com/entry/2024/09/15/201136)
* [Google Capture The Flag 2024 IDEA writeup](https://furutsuki.hatenablog.com/entry/2024/06/28/092214)

[月別アーカイブ](https://furutsuki.hatenablog.com/archive)

* ▼
  ▶

  [2025](https://furutsuki.hatenablog.com/archive/2025)
  + [2025 / 7](https://furutsuki.hatenablog.com/archive/2025/07)
* ▼
  ▶

  [2024](https://furutsuki.hatenablog.com/archive/2024)
  + [2024 / 12](https://furutsuki.hatenablog.com/archive/2024/12)
  + [2024 / 9](https://furutsuki.hatenablog.com/archive/2024/09)
  + [2024 / 6](https://furutsuki.hatenablog.com/archive/2024/06)
  + [2024 / 4](https://furutsuki.hatenablog.com/archive/2024/04)
* ▼
  ▶

  [2023](https://furutsuki.hatenablog.com/archive/2023)
  + [2023 / 12](https://furutsuki.hatenablog.com/archive/2023/12)
  + [2023 / 11](https://furutsuki.hatenablog.com/archive/2023/11)
  + [2023 / 10](https://furutsuki.hatenablog.com/archive/2023/10)
  + [2023 / 7](https://furutsuki.hatenablog.com/archive/2023/07)
  + [2023 / 6](https://furutsuki.hatenablog.com/archive/2023/06)
  + [2023 / 4](https://furutsuki.hatenablog.com/archive/2023/04)
  + [2023 / 3](https://furutsuki.hatenablog.com/archive/2023/03)
  + [2023 / 2](https://furutsuki.hatenablog.com/archive/2023/02)
  + [2023 / 1](https://furutsuki.hatenablog.com/archive/2023/01)
* ▼
  ▶

  [2022](https://furutsuki.hatenablog.com/archive/2022)
  + [2022 / 12](https://furutsuki.hatenablog.com/archive/2022/12)
  + [2022 / 11](https://furutsuki.hatenablog.com/archive/2022/11)
  + [2022 / 10](https://furutsuki.hatenablog.com/archive/2022/10)
  + [2022 / 9](https://furutsuki.hatenablog.com/archive/2022/09)
  + [2022 / 7](https://furutsuki.hatenablog.com/archive/2022/07)
  + [2022 / 6](https://furutsuki.hatenablog.com/archive/2022/06)
  + [2022 / 5](https://furutsuki.hatenablog....