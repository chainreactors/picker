---
title: Prefetch-Hash-Cracker - A Small Util To Brute-Force Prefetch Hashes
url: https://buaq.net/go-134332.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:24.323950
---

# Prefetch-Hash-Cracker - A Small Util To Brute-Force Prefetch Hashes

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

![](https://8aqnet.cdn.bcebos.com/e76d14ae357bcaa0ffe2b3a18cdb520b.jpg)

Prefetch-Hash-Cracker - A Small Util To Brute-Force Prefetch Hashes

Motivation During the forensic analysis of a Windows machine, you may find the name of a de
*2022-11-5 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-134332.htm)
阅读量:55
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj6Xnr8aatAl5k9_UR8HFYjRESqANs4TzMPAHZfgUY7sSWLnXHKGXMe3wkU62R00BdkYEvDd_kKkmYuRHNlDyOyxuHR2kwYUixsWMi55nSPsZj45ppxEbaq8XhDVK5brFCg7HwhtoLfc4iQIRB50HLQoR_xLHTm12JsHcLJZQD80n1GrJIkHYy8oGqiRA=w640-h242)](https://blogger.googleusercontent.com/img/a/AVvXsEj6Xnr8aatAl5k9_UR8HFYjRESqANs4TzMPAHZfgUY7sSWLnXHKGXMe3wkU62R00BdkYEvDd_kKkmYuRHNlDyOyxuHR2kwYUixsWMi55nSPsZj45ppxEbaq8XhDVK5brFCg7HwhtoLfc4iQIRB50HLQoR_xLHTm12JsHcLJZQD80n1GrJIkHYy8oGqiRA)

## Motivation

During the [forensic analysis](https://www.kitploit.com/search/label/Forensic%20Analysis "forensic analysis") of a Windows machine, you may find the name of a deleted prefetch file. While its content may not be recoverable, the filename itself is often enough to find the full path of the executable for which the prefetch file was created.

## Using the tool

The following fields must be provided:

* *Executable name*
* *Prefetch hash*
   8 [hexadecimal](https://www.kitploit.com/search/label/Hexadecimal "hexadecimal") digits at the end of the prefetch filename, right before the `.pf` extension.
* *Hash function*
* *Bodyfile*
* *Mount point*

### Hash function

There are 3 known prefetch hash functions:

* *SCCA XP*
   Used in Windows XP
* *SCCA Vista*
   Used in Windows Vista and Windows 10
* *SCCA 2008*
   Used in Windows 7, Windows 8 and Windows 8.1

### Bodyfile

A bodyfile of the volume the executable was executed from.

The bodyfile format is not very restrictive, so there are a lot of variations of it - some of which are not supported. Body files created with `fls` and `MFTECmd` should work fine.

### Mount point

The mount point of the bodyfile, as underlined below:

```
0|C:/Users/Peter/Desktop ($FILE_NAME)|62694-48-2|d/d-wx-wx-wx|...
```

## How does it work?

The provided bodyfile is used to get the path of every folder on the volume. The tool appends the provided executable name to each of those paths to create a list of possible full paths for the executable. Each possible full path is then hashed using the provided hash function. If there's a possible full path for which the result matches the provided hash, that path is outputted.

## Limitations

The following cases are not supported:

* Hosting applications, such as `svchost.exe` and `mmc.exe`
* Applications executed with the `/prefetch:#` flag
* Applications executed from a UNC (network) path

### The 29-character limit

If the executable name is longer than 29 characters (including the extension), it will be truncated in the prefetch filename. For example, executing this file:

```
This is a very long file nameSo this part will be truncated.exe
```

From the `C:\Temp` [directory](https://www.kitploit.com/search/label/Directory "directory") on a [Windows 10](https://www.kitploit.com/search/label/Windows%2010 "Windows 10") machine, will result in the creation of this prefetch file:

```
THIS IS A VERY LONG FILE NAME-D0B882CC.pf
```

In this case, the executable name cannot be derived from the prefetch filename, so you will not be able to provide it to the tool.

## License

[MIT](https://choosealicense.com/licenses/mit/ "MIT")

Prefetch-Hash-Cracker - A Small Util To Brute-Force Prefetch Hashes
![Prefetch-Hash-Cracker - A Small Util To Brute-Force Prefetch Hashes](https://blogger.googleusercontent.com/img/a/AVvXsEj6Xnr8aatAl5k9_UR8HFYjRESqANs4TzMPAHZfgUY7sSWLnXHKGXMe3wkU62R00BdkYEvDd_kKkmYuRHNlDyOyxuHR2kwYUixsWMi55nSPsZj45ppxEbaq8XhDVK5brFCg7HwhtoLfc4iQIRB50HLQoR_xLHTm12JsHcLJZQD80n1GrJIkHYy8oGqiRA=s72-w640-c-h242)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/prefetch-hash-cracker-small-util-to.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)