---
title: Weekly#4
url: https://buaq.net/go-256734.html
source: unSafe.sh - 不安全
date: 2024-08-18
fetch_date: 2025-10-06T18:02:25.795018
---

# Weekly#4

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

![]()

Weekly#4

Contents News | ArticleThe Book of Secret KnowledgeHow to
*2024-8-17 18:53:40
Author: [taxodium.ink(查看原文)](/jump-256734.htm)
阅读量:9
收藏*

---

## Contents

* [News | Article](#headline-1)
  + [The Book of Secret Knowledge](#headline-2)
  + [How to avoid losing items? Holding pens.](#headline-3)
  + [How I Created 175 Fonts Using Rust](#headline-4)
  + [Learn things that don't change](#headline-5)
  + [Obvious travel advice](#headline-6)
  + [ECMAScript Safe Assignment Operator Proposal](#headline-7)
* [Tutorial](#headline-8)
  + [Vue3 编译原理揭秘](#headline-9)
  + [PDF Explained （译作《PDF 解析》）](#headline-10)
  + [Learn Lit](#headline-11)
  + [Learn web components](#headline-12)
* [Code](#headline-13)
  + [One Thing Nobody Explained To You About TypeScript](#headline-14)
  + [Common Causes of Memory Leaks in JavaScript](#headline-15)
  + [Patterns for Memory Efficient DOM Manipulation with Modern Vanilla JavaScript](#headline-16)
  + [Transition to `height: auto` & `display: none` Using Pure CSS](#headline-17)
  + [CSS Grid Areas](#headline-18)
  + [Zoom, zoom, and zoom (The three types of browser (and CSS!) magnification)](#headline-19)
* [Cool Bit](#headline-20)
  + [3D Bookshelf](#headline-21)
* [Tool | Library](#headline-22)
  + [Icon Maker](#headline-23)
  + [Gradient Generator – CSS & SVG Export](#headline-24)
* [Music](#headline-25)

## News | Article

### [How to avoid losing items? Holding pens.](https://blog.alexwendland.com/2024-07-07-holding-pens/)

你会不会经常忘了东西放在哪？

可能是因为东西随手一放，没有放在特定的地方，再次找的时候就忘了之前放在哪了。

理想情况下就是总是把东西放回原来的地方，那么每次都去相同地方找就好了，但有时可能放的地方远，拿过去麻烦又放弃了。

作者建议在每个区域放一个专门用于放杂物的，提供一个集中的，轻松的放置点，定期清理，从而避免忘记东西在哪。

### [Obvious travel advice](https://dynomight.net/travel/)

作者的一些旅行建议和看法：

* 和谁一起去比去哪里更重要。
* 人在喝了液体后必须要小便。所以如果你即将去一个无法小便的地方，也许不要喝太多液体。
* 公交车上的风景比地铁有趣得多。
* 旅行揭示了稳定、根基、日常生活、社区、人际关系和家庭烹饪的价值。
* …

### [ECMAScript Safe Assignment Operator Proposal](https://github.com/arthurfiorette/proposal-safe-assignment-operator)

Safe Assignment Operator:

```
const [error, response] ?= await fetch("https://arthur.place")
```

有了 `?=` ，用 await 的时候就不用写很长的 try…catch… 处理了，也不用嵌套 try…catch… 处理一些错误，代码阅读下来整体会简洁清晰一些。

期待这个操作符正式加入规范。

## Tutorial

### [PDF Explained （译作《PDF 解析》）](https://zxyle.github.io/PDF-Explained/)

一本解释 PDF 格式的小册子。

之前做一个需求，需要将页面打印成 PDF。

页面转换的 PDF 打印后，和从设计稿导出的 PDF 打印比较，发现字体存在差异， 设计稿的字体比页面实现的看起来更大一些， 页面的一些高度也不对。

排除了不是页面样式实现问题后，猜测可能是设计稿导出的 PDF 有什么不一样。

比较了两份 PDF，页面实现的是 type0 字体，PDF 中内嵌了 font-family 指定的字体。

而设计稿导出的 PDF 是 type3 字体，相比 type0，可以实现更复杂的样式，但是实际打印可能不如 type0 兼容性好。

目前还不是很确定是不是字体原因，后续如果弄明白了再写篇博客整理一下。

## Code

### [One Thing Nobody Explained To You About TypeScript](https://kettanaito.com/blog/one-thing-nobody-explained-to-you-about-typescript)

作者指出了 `tsconfig.json` 中 `include` 字段理解上的一些误解。

> The include option controls what modules to apply this TypeScript configuration to.

`include` 字段指的是 tsconfig.json 对什么文件起作用，但是如果这里面包含的文件比较多，有时候可能会出现一些意外的类型。

例如开发时只希望提示 src 中文件的类型，但是如果 include 了 test 目录，可能在开发时会出现 test 目录的类型。

相当于将 test 目录中的类型，泄露到了 src 目录中。

当在 src 中编写了一个不存在于 src 的类型，但是存在 test 中，就不会报错，这可能并不是想要的表现。

解决办法就是针对不同目录，使用不同的 tsconfig.json ，然后通过 `reference` 字段链接不同目录的 tsconfig.json 。

## Music

本周推荐一个日本的爵士钢琴家: [福居良(Ryo Fukui)](https://music.163.com/#/artist?id=30107605)，他的爵士钢琴感觉比较容易欣赏。

类比的话，就像是听古典钢琴曲和久石让宫崎骏动画钢琴曲的差别，前者需要比较高的鉴赏能力，后者光是旋律就很抓耳，容易听下去。

福居良的爵士钢琴，就像是久石让那些动画钢琴曲一样，会让我很轻松地欣赏，反反复复地听。

他的所有专辑都推荐一听，其中我听的最多的是 《[My Back Pages(Live)](https://music.163.com/#/song?id=1313897920)》，整首曲子近 19 分钟，但是听起来一点不枯燥，当钢琴旋律流动时，果断点击红心收藏了。

Author
Spike Leung

LastMod

2024-08-18
[(b16a82c)](https://github.com/Spike-Leung/taxodium/commit/b16a82c7afce858b28987bacd92935b76d242b0c "refactor: :pencil2: typo fix")

License
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

文章来源: https://taxodium.ink/post/weekly/4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)