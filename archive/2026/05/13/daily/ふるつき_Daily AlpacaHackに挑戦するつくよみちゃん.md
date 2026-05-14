---
title: Daily AlpacaHackに挑戦するつくよみちゃん
url: https://furutsuki.hatenablog.com/entry/2026/05/14/002228
source: ふるつき
date: 2026-05-13
fetch_date: 2026-05-14T05:45:53.104442
---

# Daily AlpacaHackに挑戦するつくよみちゃん

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2026-05-14](https://furutsuki.hatenablog.com/archive/2026/05/14)

# [Daily AlpacaHackに挑戦するつくよみちゃん](https://furutsuki.hatenablog.com/entry/2026/05/14/002228)

という動画シリーズを最近投稿している。

[www.nicovideo.jp](https://www.nicovideo.jp/series/556457?ref=garage_share_other)

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20260514/20260514001938.png)

Daily AlpacaHackという、毎日初心者向けの問題を1問出題してくれる常設型のCTFイベントがあって、その問題を大体毎日解いて、動画にして投稿している。
解いている様子を画面録画して、画面右下にゆっくりつくよみちゃんが登場し、そのとき考えていたことや喋っていたことを喋ってくれて、字幕がついている。なんとなくBGMもついている、みたいな単純な動画をアップロードしてる。

初心者の人にとっては他人が解いている風景が動画という形式でもれなく示されて、考えていることが常に喋られているというのは嬉しいのではないかと思っていて、自分の取り組みがDaily AlpacaHackの盛り上がりに寄与できていたら嬉しい。

これをやってるのはなんとなくできそうだったからだけど、実際仕組みを組んでみたら結構簡単にできて感動したので、仕組みを紹介。

ざっくりこういう感じ。

```
graph TD
    A[OBS Studio: 録画データ] --> B[OpenAI Whisper: 文字起こし]
    B --> C[SRTファイル: 手動修正]
    C --> D[SHAREVOX: 音声生成]
    C --> E[SHAREVOX: 母音・発話時間取得]
    F[PSDファイル: イラスト素材] --> G[表情合成処理]
    E --> G
    D --> H[ffmpeg: 合成処理]
    A --> H
    C --> H
    G --> H
    H --> I[完成動画]

    style A fill:#f9f,stroke:#333
    style I fill:#bbf,stroke:#333
    style H fill:#ff9,stroke:#333
```

録画・文字起こし・音声合成……みたいな難しいところは全部既存のアプリケーションがなんとかしてくれて、自分はちょっと高級なffmpegのwrapperを書いたら完了。ffmpegの扱いもAIに聞いたらよく、良い時代。Whisperみたいな高級書き起こしツールが登場してくれたおかげで、自分は適当にマイクに向かって喋りながら問題を解いておいたらある程度意味の通る台本ができあがっているので、修正の手間はほとんどない。10年前にこれを作るのは簡単ではなかっただろうな。

ただ不満もあって、今改善したいのは文字起こしが画面というか実際の発話に比べてちょっと早すぎるのと文字起こしの精度がわるいこと。だけど、これは自分の努力では難しくて、Whisperの進歩に頼ることになりそう。

個人的にはSHAREVOX（VOICEVOXのフォーク？　つくよみちゃんの音声が入ってるのはこっちだった）のAPIで発話の長さや母音が取れたのが面白かった。これを元にゆっくりつくよみちゃん素材のPSDから口の形を合成する、みたいなこともできて楽しい。しかしこういうのはよくみる動画とかでもやられている気がするので、自分で作らなくてもなんかツールがあったんっだろうと思っている。

作ってて一番苦労したのは動画の合成部分で、最初はmoviepyを使ってこのフレームはこの表情で音声はこれ、みたいなのを指示していたんだけど、フレームごとにループしてffmpegに入力する、というのをpythonでやると遅すぎて、30分の動画の合成に10時間くらいかかっていた。これはpythonのソースコードをclaude codeに読ませて「Goにして。並列化できるところは並列化して」と言ったら改善した。Goで書かれたffmpegのwrapperができあがり、30分の動画も1時間ちょっとで出力されるくらいになった。

一応作ったコードも公開しておきます。アセットはリポジトリに含めてないのにソースコードにベタ書きしてるから、適宜フォントやBGM、ゆっくりつくよみちゃん素材をいい感じの場所に配置してもらう必要がある。

<https://github.com/theoremoon/yukkuri-tsukuyomi-chan-jikkyo>[github.com](https://github.com/theoremoon/yukkuri-tsukuyomi-chan-jikkyo)

[seiga.nicovideo.jp](https://seiga.nicovideo.jp/seiga/im11206659)

これでだれでもゆっくりつくよみちゃん実況がつくれます。でもそれよりDaily AlpacaHackを解いてほしい。解けなかったらつくよみちゃんが解いている動画をみてupsolveしてください。動画がわかりにくかったら教えてください。よろしくお願いします。

Furutsuki
[2026-05-14 00:22](https://furutsuki.hatenablog.com/entry/2026/05/14/002228)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_medium=button&utm_source=blogs_entry_footer&utm_campaign=subscribe_blog)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2026/05/14/002228 "この記事をはてなブックマークに追加")

関連記事

* [![AlpacaHack Round 3 (Crypto) writeup](https://cdn.image.st-hatena.com/image/square/6dd0742dd7e0e99b0ae271c9466436ab103498c0/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2FF%2FFurutsuki%2F20240915%2F20240915182654.png "AlpacaHack Round 3 (Crypto) writeup")](https://furutsuki.hatenablog.com/entry/2024/09/15/201136)

  [2024-09-15](https://furutsuki.hatenablog.com/archive/2024/09/15)

  [AlpacaHack Round 3 (Crypto) writeup](https://furutsuki.hatenablog.com/entry/2024/09/15/201136)

  最近登場した個人戦CTFプラットフォームであるAlpacaHackで、Cr…
* [![CakeCTF 2022 開催記](https://cdn.image.st-hatena.com/image/square/1b063ada8dfad725c31d5b8aedbf87d6072b4fd3/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2F2022.cakectf.com%2F_next%2Fstatic%2Fimage%2Fthemes%2Fcake2022%2Fneko.e0c2a45acc10cf9f42e3c3cb9f3e45fe.png "CakeCTF 2022 開催記")](https://furutsuki.hatenablog.com/entry/2022/09/05/000733)

  [2022-09-05](https://furutsuki.hatenablog.com/archive/2022/09/05)

  [CakeCTF 2022 開催記](https://furutsuki.hatenablog.com/entry/2022/09/05/000733)

  年に2度ある人生最大の娯楽ことCTF開催のうちの一回、CakeCTFの…
* [![CTF crypto 逆引き](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "CTF crypto 逆引き")](https://furutsuki.hatenablog.com/entry/2021/03/16/095021)

  [2021-03-16](https://furutsuki.hatenablog.com/archive/2021/03/16)

  [CTF crypto 逆引き](https://furutsuki.hatenablog.com/entry/2021/03/16/095021)

  theoremoon/ctf-crypto-dict へのコントリビュートお待ちしてお…

* もっと読む

コメントを書く

[Daily AlpacaHack B-SIDE 2/17-20 ECRSA w…
 »](https://furutsuki.hatenablog.com/entry/2026/02/21/155330)

プロフィール

[![id:Furutsuki](https://cdn.profile-image.st-hatena.com/users/Furutsuki/profile.png?1503402472)](https://furutsuki.hatenablog.com/about)

[id:Furutsuki](https://furutsuki.hatenablog.com/about)
[*はてなブログPro*](https://blog.hatena.ne.jp/-/pro?plus_via=blog_plus_badge&utm_source=pro_badge&utm_medium=referral&utm_campaign=register_pro "はてなブログPro")

最終更新:
2026-05-14 00:22

株式会社はてなで働いています

読者です
読者をやめる

読者になる
読者になる

[このブログについて](https://furutsuki.hatenablog.com/about)

おすすめCTF

* <https://alpacahack.com/>

検索

ランダムに記事を表示

🔄

[最新記事](https://furutsuki.hatenablog.com/archive)

* [Daily AlpacaHackに挑戦するつくよみちゃん](https://furutsuki.hatenablog.com/entry/2026/05/14/002228)
* [Daily AlpacaHack B-SIDE 2/17-20 ECRSA writeup](https://furutsuki.hatenablog.com/entry/2026/02/21/155330)
* [2025年に読み始めて面白かったWeb小説](https://furutsuki.hatenablog.com/entry/2025/12/30/155702)
* [SECCON Beginners CTF 2025 writeup](https://furutsuki.hatenablog.com/entry/2025/07/27/223211)
* [AlpacaHack Round 12 (Crypto) - writeup](https://furutsuki.hatenablog.com/entry/2025/07/06/234110)

注目記事

[月別アーカイブ](https://furutsuki.hatenablog.com/archive)

* ▼
  ▶

  [2026](https://furutsuki.hatenablog.com/archive/2026)
  + [2026 / 5](https://furutsuki.hatenablog.com/archive/2026/05)
  + [2026 / 2](https://furutsuki.hatenablog.com/archive/2026/02)
* ▼
  ▶

  [2025](https://furutsuki.hatenablog.com/archive/2025)
  + [2025 / 12](https://furutsuki.hatenablog.com/archive/2025/12)
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
  + [2022 / 7](https://furutsuki.hatenablog.com/archive/20...