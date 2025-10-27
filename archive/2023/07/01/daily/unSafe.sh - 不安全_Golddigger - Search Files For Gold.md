---
title: Golddigger - Search Files For Gold
url: https://buaq.net/go-170919.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:03.512693
---

# Golddigger - Search Files For Gold

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

![](https://8aqnet.cdn.bcebos.com/66c1edde5f02ebeeaf5c307358bb4cc4.jpg)

Golddigger - Search Files For Gold

Gold Digger is a simple tool used to help quickly discover sensitive information in files re
*2023-6-30 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-170919.htm)
阅读量:29
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTFzmiwHyRNY6V5EfevMMMYX6QsBJzSUdFlYnTvNmTDpeCx7GFBvtdl8hZoA9VCK_KutKxsNxAVTQ6McHFhuY3HbBz9SmqJiTIGCpyokGDsKtzZ6BjZaLVUcQAF6_xuT64tKkUvPfjvUkFc8Qf8YTE9BpfcdpZFr3bbZSxym92TIW1tQLtmDt2J_whRO3J/w640-h286/dig.py.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTFzmiwHyRNY6V5EfevMMMYX6QsBJzSUdFlYnTvNmTDpeCx7GFBvtdl8hZoA9VCK_KutKxsNxAVTQ6McHFhuY3HbBz9SmqJiTIGCpyokGDsKtzZ6BjZaLVUcQAF6_xuT64tKkUvPfjvUkFc8Qf8YTE9BpfcdpZFr3bbZSxym92TIW1tQLtmDt2J_whRO3J/s886/dig.py.png)

Gold Digger is a simple tool used to help quickly [discover](https://www.kitploit.com/search/label/Discover "discover") [sensitive information](https://www.kitploit.com/search/label/Sensitive%20Information "sensitive information") in files recursively. Originally written to assist in rapidly searching files obtained during a penetration test.

## Installation

Gold Digger requires Python3.

```
virtualenv -p python3 .
```

## Usage

Directory to search for gold -r RECURSIVE, --recursive RECURSIVE Search directory recursively? -l LOG, --log LOG Log file to save output" dir="auto">

```
usage: dig.py [-h] [-e EXCLUDE] [-g GOLD] -d DIRECTORY [-r RECURSIVE] [-l LOG]

optional arguments:
  -h, --help            show this help message and exit
  -e EXCLUDE, --exclude EXCLUDE
                        JSON file containing extension exclusions
  -g GOLD, --gold GOLD  JSON file containing the gold to search for
  -d DIRECTORY, --directory DIRECTORY
                        Directory to search for gold
  -r RECURSIVE, --recursive RECURSIVE
                        Search directory recursively?
  -l LOG, --log LOG     Log file to save output
```

## Example Usage

Gold Digger will recursively go through all folders and files in search of content matching items listed in the `gold.json` file. Additionally, you can leverage an exclusion file called `exclusions.json` for skipping files matching specific extensions. Provide the root folder as the `--directory` flag.

An example structure could be:

```
~/Engagements/CustomerName/data/randomfiles/
~/Engagements/CustomerName/data/randomfiles2/
~/Engagements/CustomerName/data/code/
```

You would provide the following command to parse all 3 account reports:

```
python dig.py --gold gold.json --exclude exclusions.json --directory ~/Engagements/CustomerName/data/ --log Customer_2022-123_gold.log
```

## Results

The tool will create a log file containg the scanning results. Due to the nature of using regular expressions, there may be numerous false positives. Despite this, the tool has been proven to increase [productivity](https://www.kitploit.com/search/label/Productivity "productivity") when processing thousands of files.

## Shout-outs

Shout out to @d1vious for releasing [git-wild-hunt](https://www.kitploit.com/search/label/Git-Wild-Hunt "git-wild-hunt") [https://github.com/d1vious/git-wild-hunt](https://github.com/d1vious/git-wild-hunt "https://github.com/d1vious/git-wild-hunt")! Most of the regex in GoldDigger was used from this amazing project.

文章来源: http://www.kitploit.com/2023/06/golddigger-search-files-for-gold.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)