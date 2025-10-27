---
title: Probable_Subdomains - Subdomains Analysis And Generation Tool. Reveal The Hidden!
url: https://buaq.net/go-150559.html
source: unSafe.sh - 不安全
date: 2023-02-23
fetch_date: 2025-10-04T07:49:17.926173
---

# Probable_Subdomains - Subdomains Analysis And Generation Tool. Reveal The Hidden!

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

![](https://8aqnet.cdn.bcebos.com/84aef30fc1d50974fa77df4077fffc87.jpg)

Probable\_Subdomains - Subdomains Analysis And Generation Tool. Reveal The Hidden!

Online tool: https://weakpass.com/generate/domains TL;DR During bug bounties, penetrations
*2023-2-22 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-150559.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO8jlAQxr0iTi2JGDUI_-WqGscs1Z_pHs9aa42LZlvSo5h0EHjgR8wQMGcGvHOoepytEeAan2xuULA4l0lf46D7EYNXOX7_OZSLp52FkyfLXyANB-LSf-T5v4z-oje6A5MjZ7nPOrvmbAZy9PXNQDPfyqvQSLA8Iu77ZVuCQSnynYFovscTxQJVbhRHg/w640-h294/probable_subdomains_1_generate.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO8jlAQxr0iTi2JGDUI_-WqGscs1Z_pHs9aa42LZlvSo5h0EHjgR8wQMGcGvHOoepytEeAan2xuULA4l0lf46D7EYNXOX7_OZSLp52FkyfLXyANB-LSf-T5v4z-oje6A5MjZ7nPOrvmbAZy9PXNQDPfyqvQSLA8Iu77ZVuCQSnynYFovscTxQJVbhRHg/s544/probable_subdomains_1_generate.gif)

Online tool: [https://weakpass.com/generate/domains](https://weakpass.com/generate/domains "https://weakpass.com/generate/domains")

## TL;DR

During bug bounties, penetrations tests, [red teams](https://www.kitploit.com/search/label/Red%20Teams "red teams") exercises, and other great activities, there is always a room when you need to launch amass, subfinder, sublister, or any other tool to find [subdomains](https://www.kitploit.com/search/label/Subdomains "subdomains") you can use to break through - like **test.google.com**, **dev.admin.paypal.com** or **staging.ceo.twitter.com**. Within this repository, you will be able to find out the answers to the following questions:

1. What are the most [popular subdomains](https://github.com/zzzteph/probable_subdomains/tree/main/wordlists/subdomains "popular subdomains")?
2. What are the most [common words](https://github.com/zzzteph/probable_subdomains/tree/main/wordlists/levels "common words") in multilevel subdomains on different levels?
3. What are the most [used words](https://github.com/zzzteph/probable_subdomains/tree/main/wordlists/words "used words") in subdomains?

And, of course, [wordlists](https://github.com/zzzteph/probable_subdomains/tree/main/wordlists "wordlists") for all of the questions above!

## Methodology

As sources, I used lists of subdomains from public [bugbounty](https://www.kitploit.com/search/label/Bugbounty "bugbounty") programs, that were collected by [chaos.projectdiscovery.io](https://chaos.projectdiscovery.io/ "chaos.projectdiscovery.io"), [bounty-targets-data](https://github.com/arkadiyt/bounty-targets-data/ "bounty-targets-data") or that just had responsible disclosure programs with a total number of **4095** domains! If subdomains appear more than in 5-10 **different** scopes, they will be put in a certain list. For example, if **dev.stg** appears both in **\*.google.com** and **\*.twitter.com**, it will have a frequency of 2. It does not matter how often **dev.stg** appears in **\*.google.com**. That's all - **nothing more, nothing less< /strong>.**

You can find complete list of sources [here](https://github.com/zzzteph/probable_subdomains/blob/main/statistics.md "here")

### Lists

#### Subdomains

In these lists you will find most popular subdomains **as is**.

| Name | Words count | Size |
| --- | --- | --- |
| [subdomains.txt.gz](https://download.weakpass.com/subdomains.txt.gz "subdomains.txt.gz") | 21901389 | 501MB |
| [subdomains\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/subdomains/subdomains_top100.txt "subdomains_top100.txt") | 100 | 706B |
| [subdomains\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/subdomains/subdomains_top100.txt "subdomains_top1000.txt") | 1000 | 7.2KB |
| [subdomains\_top10000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/subdomains/subdomains_top100.txt "subdomains_top10000.txt") | 10000 | 70KB |

#### Subdomain levels

In these lists, you will find the most popular words from subdomains split by levels. F.E - **dev.stg** [subdomain](https://www.kitploit.com/search/label/Subdomain "subdomain") will be split into two words **dev** and **stg**. **dev** will have level = 2, **stg** - level = 1. You can use these [wordlists](https://www.kitploit.com/search/label/Wordlists "wordlists") for combinatory attacks for subdomain searches. There are several types of level.txt wordlists that follow the idea of subdomains.

| Name | Words count | Size |
| --- | --- | --- |
| [level\_1.txt.gz](https://download.weakpass.com/level_1.txt.gz "level_1.txt.gz") | 8096054 | 153MB |
| [level\_2.txt.gz](https://download.weakpass.com/level_2.txt.gz "level_2.txt.gz") | 7556074 | 106MB |
| [level\_3.txt.gz](https://download.weakpass.com/level_3.txt.gz "level_3.txt.gz") | 1490999 | 18MB |
| [level\_4.txt.gz](https://download.weakpass.com/level_4.txt.gz "level_4.txt.gz") | 205969 | 3.2MB |
| [level\_5.txt.gz](https://download.weakpass.com/level_5.txt.gz "level_5.txt.gz") | 71716 | 849KB |
| [level\_1\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_1_top100.txt "level_1_top100.txt") | 100 | 633B |
| [level\_1\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_1_top1000.txt "level_1_top1000.txt") | 1000 | 6.6K |
| [level\_2\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_2_top100.txt "level_2_top100.txt") | 100 | 550B |
| [level\_2\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_2_top1000.txt "level_2_top1000.txt") | 1000 | 5.6KB |
| [level\_3\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_3_top100.txt "level_3_top100.txt") | 100 | 531B |
| [level\_3\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_3_top1000.txt "level_3_top1000.txt") | 1000 | 5.1KB |
| [level\_4\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_4_top100.txt "level_4_top100.txt") | 100 | 525B |
| [level\_4\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_4_top1000.txt "level_4_top1000.txt") | 1000 | 5.0KB |
| [level\_5\_top100.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_5_top100.txt "level_5_top100.txt") | 100 | 449B |
| [level\_5\_top1000.txt](https://raw.githubusercontent.com/zzzteph/probable_subdomains/main/wordlists/levels/level_5_top1000.txt "level_5_top1000.txt") | 1000 | 5.0KB |

#### Popular splitted subdomains

In these lists, you will find the most popular splitted words from subdomains on all levels. For example - **dev.stg** subdomain will be splitted in two words **dev** and **stg**.

| Name | Words count | Size |
| --- | --- | --- |
| [words.txt.gz](https://download.weakpass.com/words.txt.gz "words.txt.gz") | 17229401 | 278MB |
| [words\_top100.txt](https://github.com/zzzteph/probable_subdomains/blob/main/wordlists/words/words_top100.txt "words_top100.txt") | 100 | 597B |
| [words\_top1000.txt](https://github.com/zzzteph/probable_subdomains/blob/main/wordlists/words/words_top1000.txt "words_top1000.txt") | 1000 | 5.5KB |
| [words\_top10000.txt](https://github.com/zzzteph/probable_subdomains/blob/main/wordlists/words/words_top10000.txt "words_top10000.txt") | 10000 | 62KB |

#### Google Drive

You can download all the files from [Google Drive](https://drive.google.com/drive/folders/1LI--YcCoKAY6ysCds5IaT00q_i15jkkB?usp=sharing "G...