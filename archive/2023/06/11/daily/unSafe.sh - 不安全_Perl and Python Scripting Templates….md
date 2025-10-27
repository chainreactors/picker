---
title: Perl and Python Scripting Templates…
url: https://buaq.net/go-168101.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:52.752346
---

# Perl and Python Scripting Templates…

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

Perl and Python Scripting Templates…

One of the most important (basic) technical skills in cybersecurity are:Knowing Exce
*2023-6-10 07:33:10
Author: [www.hexacorn.com(查看原文)](/jump-168101.htm)
阅读量:29
收藏*

---

One of the most important (basic) technical skills in cybersecurity are:

* Knowing [Excel](https://www.hexacorn.com/blog/category/excel/) (or Google sheets)
* Knowing basic programming/scripting (bash, cmd, powershell, vbs, vba, autoit, python, perl, etc.)
* Knowing and staying up to date with tools

I covered item #1 [a few times](https://www.hexacorn.com/blog/category/excel/).

I did cover #2 [to some extent](https://www.hexacorn.com/blog/2019/09/06/state-machine-vs-regex/) as well, but I’d like to expand on it today.

And #3 is your kinda FOMO at work – there are way too many projects/tools available today to know-them-all, but the more you know of more of them, the easier your job will become. As in, for almost every single cyber/hacking/reversing idea you can think of, there is someone, somewhere who has not only already thought of it before, but also implemented some cool tool, PoC, etc. I will go as far as to saying… tool and ideas foraging is one of the most important cyber skills today. Taking shortcuts, effectively using what is already out there is the ‘street-savvy’ cyber skill equivalent A.D. 2023.

Now, using tools is cool, but sometimes, and often really… we still need to do some work ourselves. This is why today I will focus on the #2… Just… a bit more optimized.

I can’t count how many times over last 2 decades I was in a need to write a simple script that would take a directory or a filename as an input, and then would do some quick processing of the files found inside that given directory (recursively), or on that specific given file, and then would spit out the results.

After doing the same repetitive work of coding the same routines over and over again I finally decided that I need some sort of a template. And I have developed one that I now use for quick&dirty processing of ‘many files of some kind’ on regular basis, and where the basic logic of enumerating the directory, checking the file extensions, their size, etc is already built-in. And anytime I re-use it, I simply mod the logic of that template to my needs, f.ex. use the right file-reading routine (f.ex. read as a single binary blob, or line-by-line), use appropriate character-encoding (ANSI, UTF-8, UTF-16, etc.), and then do some data processing (extract lines of interest, decrypt some data, etc.), and finally – spit out the results to the console.

I must admit that I used perl template for this sort of quick&dirty, case-by-case bulk file parsing solutions for many years. It actually worked like a charm, and I have used improved variants of the main template on web logs, executables, quarantine files, clusters of unknown files that needed classifying , etc. but eventually, with the whole world turning into Python over last decade, I developed a template for it as well.

Here they are:

* [Perl](http://hexacorn.com/examples/template_scan.pl.txt)
* [Python](http://hexacorn.com/examples/template_scan.py.txt)

I must admit it: compared to Perl, Python is definitely the language of the future, so my Python template is far richer…

If you find it useful, if you think I should add more code to any of these, please let me know. Thanks!

文章来源: https://www.hexacorn.com/blog/2023/06/09/perl-and-python-scripting-templates/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)