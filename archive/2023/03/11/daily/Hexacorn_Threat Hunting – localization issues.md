---
title: Threat Hunting – localization issues
url: https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/
source: Hexacorn
date: 2023-03-11
fetch_date: 2025-10-04T09:15:30.122404
---

# Threat Hunting – localization issues

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/)
[Next →](https://www.hexacorn.com/blog/2023/03/12/list-of-clean-mutexes-and-mutants/)

# Threat Hunting – localization issues

Posted on [2023-03-10](https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/ "11:47 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

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

This entry was posted in [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/ "Permalink to Threat Hunting – localization issues").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")