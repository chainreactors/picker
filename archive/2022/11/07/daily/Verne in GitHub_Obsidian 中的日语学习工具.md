---
title: Obsidian 中的日语学习工具
url: https://einverne.github.io/post/2022/11/japanese-learning-tools-in-obsidian.html
source: Verne in GitHub
date: 2022-11-07
fetch_date: 2025-10-03T21:51:20.753981
---

# Obsidian 中的日语学习工具

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# Obsidian 中的日语学习工具

Posted on 11/06/2022
, Last modified on 11/06/2022
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2022-11-06-japanese-learning-tools-in-obsidian.md)

介绍一下在 Obsidian 中学习，记录日语笔记相关的插件。

## Furigana

Furigana，注音假名，{振り仮名|ふりがな}，日语中为了表示汉字读音而在其上方或周围附注假名表音符号。印刷时内文以 7 号格大小的文字和五号格大小的振假名为标准。其别名为 ルビー，来自英语的 ruby，英国对 5.5 号字体的传统称呼，因此印刷物的振假名也被称为 ルビ。

## 网页 ruby 元素

W3C 为网页提供了 `<ruby>` 元素，虽然这个概念在 2001 年就被提出，但是一直没有被正式写入标准。

如果在网页中使用：

```
<ruby>漢字<rt>かんじ</rt></ruby>
```

那么浏览器在渲染的时候就会将日语假名显示在汉字上方。

## Markdown furigana

Markdown furigana 沿用了 markdown-it-ruby 的语法

* <https://github.com/steven-kraft/obsidian-markdown-furigana>

在 markdown 中使用如下的语法时

```
{漢字|かんじ}
```

就会渲染成：

```
<ruby>漢字<rt>かんじ</rt></ruby>
```

在显示的时候就会将假名显示在汉字上方。

![obsidian furigana](https://photo.einverne.info/images/2022/11/14/ZLfD.png)

同样这个插件不仅支持假名，注音，拼音都可以使用相同的语法进行标注。

## Word Splitting for Japanese in Edit mode

Word Splitting for Japanese in Edit mode 是一个在编辑模式下强化日语分词的 CodeMirror 编辑器的 Patch，就和之前用的中文分词插件一样，使得在 Obsidian 下选择单词更加智能，因为中文，日文都不是像英文那样使用空格来区分单词的，所以在选择的时候极有可能不是想选择的部分，这个插件可以让选择单词变得更加简单。

* <https://github.com/sonarAIT/cm-japanese-patch>

## Related Posts

* [Obsidian 中的日语学习工具](/post/2022/11/japanese-learning-tools-in-obsidian.html) - 11/06/2022
* [日语发音基础：五十音](/post/2022/10/japanese-hiragana-katakana.html) - 10/15/2022

---

* [← Previous（前一篇）](/post/2022/11/type-practice-website.html "打字输入练习网站推荐")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2022/11/pipedream-usage.html "在线工作流 Pipedream 使用记录")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2022/11/japanese-learning-tools-in-obsidian.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [学习笔记 496](/categories.html#学习笔记)

* [obsidian 21](/tags.html#obsidian)
* [japanese 12](/tags.html#japanese)
* [obsidian-plugins 1](/tags.html#obsidian-plugins)
* [hiragana 2](/tags.html#hiragana)
* [furigana 1](/tags.html#furigana)
* [html-ruby 1](/tags.html#html-ruby)
* [html 7](/tags.html#html)
* [w3c 1](/tags.html#w3c)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").