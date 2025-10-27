---
title: Combining zipdump, file-magic And myjson-filter
url: https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/
source: Didier Stevens
date: 2023-01-01
fetch_date: 2025-10-04T02:50:39.144262
---

# Combining zipdump, file-magic And myjson-filter

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 31 December 2022

### Combining zipdump, file-magic And myjson-filter

Filed under: [maldoc](https://blog.didierstevens.com/category/maldoc/),[Malware](https://blog.didierstevens.com/category/malware/) — Didier Stevens @ 9:38

In this blog post, I show how you can combine my tools [zipdump.py](https://blog.didierstevens.com/2022/12/29/update-zipdump-py-version-0-0-24/), [file-magic.py](https://blog.didierstevens.com/2022/12/23/update-file-magic-py-version-0-0-5/) and [myjson-filter.py](https://blog.didierstevens.com/2022/12/24/update-myjson-filter-py-version-0-0-3/) to select and analyze files of a particular type.

I start with a [daily batch of malware files published by Malware Bazaar](https://datalake.abuse.ch/malware-bazaar/daily/).

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-095447.png)

I let it produce [JSON output](https://blog.didierstevens.com/2018/07/09/jsonoutput/) using option –jsonoutput, that can be consumed by some of my tools, like [file-magic.py](https://blog.didierstevens.com/2022/12/23/update-file-magic-py-version-0-0-5/), my tool to identify files based on the content using the libmagic library.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-095633.png)

In the output above, we can see that most files are PE files (Windows executables).

For this example, I’m interested in Office files (ole files). I can filter the output of file-magic.py for that with option -r. Libmagic identifies this type of file as “Composite Document File …”, thus I filter for Composite:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-100133.png)

This gives me a list of malicious Office documents. I want to extract URLs from them, but I don’t want to extract all of these files from the ZIP container to disk, and do the URL extraction file per file.

I want to do this with a one-liner. 🙂

What I’m going to do, is use file-magic’s option –jsonoutput, so that it augments the json output of zipdump with the file type, and then I use my tool [myjson-filter.py](https://blog.didierstevens.com/2022/12/24/update-myjson-filter-py-version-0-0-3/) to filter that json output for files that are only of a type that contains the word Composite. With this command:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-100625.png)

This produces JSON output that contains the content of each file of type Composite, found inside the ZIP container.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-100803.png)

This output can be consumed by my tool [strings.py](https://blog.didierstevens.com/2022/09/19/update-strings-py-version-0-0-8/), to extract all the strings.

Side note: if you want to know first which files were selected for processing, use option -l:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-101232.png)

Let’s pipe the filtered JSON output into strings.py, with options to produce a list of unique strings (-u) that contain the word http (-s http), like this:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-101848.png)

I use my tool [re-search.py](https://blog.didierstevens.com/2022/07/24/update-re-search-py-version-0-0-21/) to extract a list of unique URLs:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-102624.png)

I filter out common URLs found in Office documents:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-102826.png)

And finally, I sort the URLs by domain name using my tool [sortcanon.py](https://blog.didierstevens.com/2022/07/20/update-sortcanon-version-0-0-2/):

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-103044.png)

The adobe URLs are not malicious, but the other ones could be.

This one-liner allows me to quickly process daily malware batches, looking for easy IOCs (cleartext URLs in Office documents) without writing any malicious file to disk.

```
zipdump.py --jsonoutput 2020-10-24.zip | file-magic.py --jsoninput --jsonoutput | myjson-filter.py -t Composite | strings.py --jsoninput -u -s http | re-search.py -u -n url -F officeurls | sortcanon.py -c domain
```

Remark that by using an option to search for strings with the word http (-s http), I reduce the output of strings to be processed by re-search.py, so that the search is faster. But that limits you (mostly) to URLs with protocol http or https.

Leave out this option if you want to search for all possible protocols, or try -s “://”.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221231-103700.png)

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/feed/) [TrackBack URI](https://blog.didierstevens.com/2022/12/31/combining-zipdump-file-magic-and-myjson-filter/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/pr...