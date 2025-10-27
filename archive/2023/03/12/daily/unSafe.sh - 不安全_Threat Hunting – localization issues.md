---
title: Threat Hunting – localization issues
url: https://buaq.net/go-152971.html
source: unSafe.sh - 不安全
date: 2023-03-12
fetch_date: 2025-10-04T09:21:39.922938
---

# Threat Hunting – localization issues

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

Threat Hunting – localization issues

March 10, 2023 in threat hunting
*2023-3-11 07:47:21
Author: [www.hexacorn.com(查看原文)](/jump-152971.htm)
阅读量:34
收藏*

---

![](https://www.hexacorn.com/blog/wp-content/uploads/2011/10/Adam_Avatar_2_50x50.png)

March 10, 2023 *in [threat hunting](https://www.hexacorn.com/blog/category/threat-hunting/)*

So you finished writing your perfect threat hunting query.

Done and dusted, right?

Hmm, sorry… chances are, it is… broken.

How come?

One reason, but it has many acronyms: L10N, T9N, I18N or G11N.

If you are mostly dealing with English-centric versions of the operating systems you may now stop reading. But… You will be missing out.

Why?

THERE ARE OTHER LANGUAGES OUT THERE. And they come with a luggage…

The acronyms listed earlier expand into:

* Translation (T9N)
* Localization (L10N)
* Internationalization (I18N)
* Globalization (G11N)

They define a different world. The world that is quite esoteric to monoglots. The world that embraces the world of ‘other languages in use’. The whole lot of new devices ‘suddenly in scope’, too. The world of foreigners who do not use English as their MAIN language. Most of Europe really. Many places in the world, REALLY!

In this world, your c:\Program Files becomes… an item from this [table](https://en.wikipedia.org/wiki/Program_Files).

Pfff… and suddenly, all your queries relying on hard-coded ‘program files’ string need to be adjusted.

You are welcome! 🙂

And it’s not the only artifact that changes.

What about ‘New folder”? This [thread](https://www.devmedia.com.br/forum/traducao-dos-botoes/555742) shows some examples of “New Folder” string represented in various languages:

* Neuer Ordner
* New folder
* Nouveau dossier
* Nova Pasta
* Nowy folder
* Nuova Cartella

And again, this is just one of many ‘not so subtle’ localization changes to the OS that affects the way you should be writing your threat hunting queries or doing your DFIR engagement. And yes, it complicates things A LOT. And yes, Hebrew, Arabic, Chinese and Japanese versions of these do exist as well, and they complicate things even more.

Where does it leave us?

Simple answer: pay attention. More responsible answer: explore the environment & adjust queries as per need.

As long as your results generating framework/language supports Unicode you should be seeing these localized “things”, but only IF YOU EXPECT THEM. Once you see them, bundle them together and use them as a template, f.ex. use combos like this for a c:\program files folder name:

```
"\Program Files",
"\Programme",
"\Archivos de programa",
"\Programmes",
"\Programmi",
"\Arquivos de Programas",
"\Programmer",
"\Programfiler",
"\Fisiere Program"
```

These are not all the possibilities, of course, but they are good enough to make us all ‘aware’.

Going forward, we will all be localizing our queries. Oui?

文章来源: https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)