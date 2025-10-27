---
title: Combining zipdump, file-magic And myjson-filter
url: https://buaq.net/go-143561.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:16.007473
---

# Combining zipdump, file-magic And myjson-filter

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

![](https://8aqnet.cdn.bcebos.com/600a0a298feb52cf81e432a1353a548c.jpg)

Combining zipdump, file-magic And myjson-filter

In this blog post, I show how you can combine my tool zipdump.py, file-magic.py and myjson-filte
*2022-12-31 17:38:23
Author: [blog.didierstevens.com(查看原文)](/jump-143561.htm)
阅读量:28
收藏*

---

In this blog post, I show how you can combine my tool [zipdump.py](https://blog.didierstevens.com/2022/12/29/update-zipdump-py-version-0-0-24/), [file-magic.py](https://blog.didierstevens.com/2022/12/23/update-file-magic-py-version-0-0-5/) and [myjson-filter.py](https://blog.didierstevens.com/2022/12/24/update-myjson-filter-py-version-0-0-3/) to select and analyze files of a particular type.

I start with a [daily batch of malware files published by Malware Bazaar](https://datalake.abuse.ch/malware-bazaar/daily/).

![](https://didierstevens.files.wordpress.com/2022/12/20221231-095447.png)

I let it produce [JSON output](https://blog.didierstevens.com/2018/07/09/jsonoutput/) using option –jsonoutput, that can be consumed by some of my tools, like [file-magic.py](https://blog.didierstevens.com/2022/12/23/update-file-magic-py-version-0-0-5/), my tool to identify files based on the content using the libmagic library.

![](https://didierstevens.files.wordpress.com/2022/12/20221231-095633.png)

In the output above, we can see that most files are PE files (Windows executables).

For this example, I’m interested in Office files (ole files). I can filter the output of file-magic.py for that with option -r. Libmagic identifies this type of file as “Composite Document File …”, thus I filter for Composite:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-100133.png)

This gives me a list of malicious Office documents. I want to extract URLs from them, but I don’t want to extract all of these files from the ZIP container to disk, and do the URL extraction file per file.

I want to do this with a one-liner. 🙂

What I’m going to do, is use file-magic’s option –jsonoutput, so that it augments the json output of zipdump with the file type, and then I use my tool [myjson-filter.py](https://blog.didierstevens.com/2022/12/24/update-myjson-filter-py-version-0-0-3/) to filter that json output for files that are only of a type that contains the word Composite. With this command:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-100625.png)

This produces JSON output that contains the content of each file of type Composite, found inside the ZIP container.

![](https://didierstevens.files.wordpress.com/2022/12/20221231-100803.png)

This output can be consumed by my tool [strings.py](https://blog.didierstevens.com/2022/09/19/update-strings-py-version-0-0-8/), to extract all the strings.

Side note: if you want to know first which files were selected for processing, use option -l:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-101232.png)

Let’s pipe the filtered JSON output into strings.py, with options to produce a list of unique strings (-u) that contain the word http (-s http), like this:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-101848.png)

I use my tool [re-search.py](https://blog.didierstevens.com/2022/07/24/update-re-search-py-version-0-0-21/) to extract a list of unique URLs:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-102624.png)

I filter out common URLs found in Office documents:

![](https://didierstevens.files.wordpress.com/2022/12/20221231-102826.png)

And finally, I sort the URLs by domain name using my tool [sortcanon.py](https://blog.didierstevens.com/2022/07/20/update-sortcanon-version-0-0-2/):

![](https://didierstevens.files.wordpress.com/2022/12/20221231-103044.png)

The adobe URLs are not malicious, but the other ones could be.

This one-liner allows me to quickly process daily malware batches, looking for easy IOCs (cleartext URLs in Office documents) without writing any malicious file to disk.

```
zipdump.py --jsonoutput 2020-10-24.zip | file-magic.py --jsoninput --jsonoutput | myjson-filter.py -t Composite | strings.py --jsoninput -u -s http | re-search.py -u -n url -F officeurls | sortcanon.py -c domain
```

Remark that by using an option to search for strings with the word http (-s http), I reduce the output of strings to be processed by re-search.py, so that the search is faster. But that limits you (mostly) to URLs with protocol http or https.

Leave out this option if you want to search for all possible protocols, or try -s “://”.

![](https://didierstevens.files.wordpress.com/2022/12/20221231-103700.png)

文章来源: https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)