---
title: vimのcolorschemeからはてなブログのシンタックスハイライトを作る
url: https://furutsuki.hatenablog.com/entry/2023/03/02/193042
source: ふるつき
date: 2023-03-03
fetch_date: 2025-10-04T08:31:34.178257
---

# vimのcolorschemeからはてなブログのシンタックスハイライトを作る

[![ふるつき](https://cdn.image.st-hatena.com/image/square/22d94d91fe8214e59637e6fa6173edbe2edc56c6/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F96439929%2F1745809789466802)](https://furutsuki.hatenablog.com/)

[ふるつき](https://furutsuki.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [ふるつき](https://furutsuki.hatenablog.com/)

## v(\*'='\*)v 記事がよかったらスターつけていってください

[2023-03-02](https://furutsuki.hatenablog.com/archive/2023/03/02)

# [vimのcolorschemeからはてなブログのシンタックスハイライトを作る](https://furutsuki.hatenablog.com/entry/2023/03/02/193042)

[vim](http://d.hatena.ne.jp/keyword/vim)のcolorschemeには theoremoon/cryptohack-color.[vim](http://d.hatena.ne.jp/keyword/vim) というやつを使っている。これは cryptohack/[sublime](http://d.hatena.ne.jp/keyword/sublime)-theme を変換したやつで、変換の感じがちょっと微妙で完全に同じハイライトにはならないものの、色の感じは気に入っている。

[github.com](https://github.com/theoremoon/cryptohack-color.vim)

[github.com](https://github.com/cryptohack/sublime-theme)

気に入っているので、[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上での[ソースコード](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の表示も、全く同じではないにせよ似たような感じになっていると嬉しい。

適当に動作を見ると、[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)での[シンタックス](http://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%F3%A5%BF%A5%C3%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)ハイライトは、なんか `.synIdentifier` みたいなクラスがつく感じで、これに[CSS](http://d.hatena.ne.jp/keyword/CSS)でスタイルが当てられている。この `Identifier` とかの部分は[vim](http://d.hatena.ne.jp/keyword/vim)のhighlight groupの名前と大体同じなので、[vim](http://d.hatena.ne.jp/keyword/vim)のcolorschemeから[CSS](http://d.hatena.ne.jp/keyword/CSS)を生成して、それを[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)のデザイン[CSS](http://d.hatena.ne.jp/keyword/CSS)に設定すればいい感じになるのではないか

というわけでやってみた。[CSS](http://d.hatena.ne.jp/keyword/CSS)生成くんはこんな感じ。適当なファイルに書き込んで開いて、`:source %` してから `:call GenerateColorschemeCSS()` をやってメッセージウィンドウに出てきたやつをコピーして貼り付ける

```
function! GenerateColorschemeCSS()
    let groups = ["Special", "Type", "Comment", "PreProc", "Identifier", "Constant", "Statement"]
    for g in groups
         let color = s:returnHighlightTerm(g, "guifg")
         echo ".syn" . g . " { color: " . color . " !important; }"
    endfor

    echo ".entry-content pre {"
    echo "background: " . s:returnHighlightTerm("Normal", "guibg") . " !important;"
    echo "color: " . s:returnHighlightTerm("Normal", "guifg") . " !important;"
    echo "}"
endfunction

" https://vi.stackexchange.com/questions/12293/read-values-from-a-highlight-group
function! s:returnHighlightTerm(group, term)
   " Store output of group to variable
   let output = execute('hi ' . a:group)

   if matchstr(output, "cleared") == "cleared"
       return s:returnHighlightTerm("Normal", a:term)
   endif

   let link = matchstr(output, "links to .*")
   if link != ""
       return s:returnHighlightTerm(link[9:], a:term)
   endif

   return matchstr(output, a:term.'=\zs\S*')
endfunction
```

[vim](http://d.hatena.ne.jp/keyword/vim)上での表示と比較するとまあまあ微妙だけど雰囲気はあるので良いか。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230302/20230302191540.png)![](https://cdn-ak.f.st-hatena.com/images/fotolife/F/Furutsuki/20230302/20230302192916.png)

[vim](http://d.hatena.ne.jp/keyword/vim) / [はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)

文字列とかがハイライトされてないのが結構悲しいけど、[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上ではそこには`.synConstant` クラスが当たっていて、 cryptohack-color.[vim](http://d.hatena.ne.jp/keyword/vim) では`Constant` highlight groupへのハイライトは定義されていないので`Normal`にフォールバックされているのでこうなる。

じゃあ[vim](http://d.hatena.ne.jp/keyword/vim)上だと文字列はどういうhighlight groupになっているかというと、`vimString` というやつだった。結局これは`String` というhighlight groupにリンクされている。

どうして[はてなブログ](http://d.hatena.ne.jp/keyword/%EF%BF%BD%CF%A4%C6%A4%CA%A5%D6%A5%EF%BF%BD%EF%BF%BD%EF%BF%BD)上では`synString` とかではなくて`synConstant` クラスが当たっているのか、あるいはどうして私の[vim](http://d.hatena.ne.jp/keyword/vim)では`Constant` highlight groupになっていないのか、というのは調べてない。

見返していると文字列が文字列っぽくハイライトされていないのは残念な感じがしてきたので今度気が向いたら調べて直そう。なんかミスってるんだろうな…

Furutsuki
[2023-03-02 19:30](https://furutsuki.hatenablog.com/entry/2023/03/02/193042)

[読者になる](https://blog.hatena.ne.jp/Furutsuki/furutsuki.hatenablog.com/subscribe?utm_source=blogs_entry_footer&utm_medium=button&utm_campaign=subscribe_blog)

[![この記事をはてなブックマークに追加](https://b.st-hatena.com/images/entry-button/button-only.gif)](https://b.hatena.ne.jp/entry/s/furutsuki.hatenablog.com/entry/2023/03/02/193042 "この記事をはてなブックマークに追加")

関連記事

* [![はてなブログの自作テーマのCSSをGitHub Pagesでホスティングして本番反映を楽にするテク](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "はてなブログの自作テーマのCSSをGitHub Pagesでホスティングして本番反映を楽にするテク")](https://furutsuki.hatenablog.com/entry/2023/11/26/155338)

  [2023-11-26](https://furutsuki.hatenablog.com/archive/2023/11/26)

  [はてなブログの自作テーマのCSSをGitHub Pagesでホスティングして本番反映を楽にするテク](https://furutsuki.hatenablog.com/entry/2023/11/26/155338)

  はてなブログにはテーマという概念があって、ブログのデザイン…
* [![InCTF Writeup](https://cdn.image.st-hatena.com/image/square/298058b2bffe422918ac5e915861b0c0839ae26b/backend=imagemagick;height=100;version=1;width=100/https%3A%2F%2Fcdn.blog.st-hatena.com%2Fimages%2Ftheme%2Fog-image-1500.png "InCTF Writeup")](https://furutsuki.hatenablog.com/entry/2019/09/23/225011)

  [2019-09-23](https://furutsuki.hatenablog.com/archive/2019/09/23)

  [InCTF Writeup](https://furutsuki.hatenablog.com/entry/2019/09/23/225011)

  I played InCTF as a member of zer0pts. We reached 22nd plac…

* もっと読む

コメントを書く

[«
RTACTF 2023 春 - 並走感想](https://furutsuki.hatenablog.com/entry/2023/03/21/222826)

[HackTM CTF Quals 2023 writeup - d-phi-e…
 »](https://furutsuki.hatenablog.com/entry/2023/02/20/141311)

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
  + [2023 / 10](https://furutsuki.hatenablog.com/archive/202...