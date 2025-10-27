---
title: Thomas Fitzsimmons: Printing an A4 document on US letter paper using Debian
url: https://buaq.net/go-158867.html
source: unSafe.sh - 不安全
date: 2023-04-17
fetch_date: 2025-10-04T11:31:43.368071
---

# Thomas Fitzsimmons: Printing an A4 document on US letter paper using Debian

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

Thomas Fitzsimmons: Printing an A4 document on US letter paper using Debian

My wife bought a dress pattern on Etsy that she received as a PDF. It was a lar
*2023-4-16 11:41:21
Author: [www.fitzsim.org(查看原文)](/jump-158867.htm)
阅读量:16
收藏*

---

My wife bought a dress pattern on Etsy that she received as a PDF. It was a large pattern that spanned many pages, meant to be trimmed and taped together into a large continuous sheet. The pattern was labelled “**A4-letter**“, meaning that it should be printable on A4 or letter paper. For accuracy, the pattern had to be printed at its native scale without cropping. The document contained a calibration box that was intended by the designer to be **5cm x 5cm** exactly; I measured it with a ruler after each test print. The pattern’s internal tiles had four alignment chevrons, one on each side, which I could measure to ensure they had not been cropped. Getting the document printed perfectly turned out to be a puzzle, so I thought I’d publish what worked for me.

*evince*‘s “**Properties**” dialog showed the document’s native dimensions as “**Paper Size:”, “A4, Portrait (8.27 × 11.69 inch)**“, but on hand, I only had **US letter 8.5 x 11 inch** printer paper. I tried printing from several PDF viewers: *xpdf 3.04*, *evince 3.38.2*, and *Firefox 111.0.1*. I did test prints with many settings combinations in the different viewers. All my naive attempts failed in various ways, either scaling the document or cropping the margins. I won’t document all the specific failure modes, I’ll just skip to the method that worked, which combined an external tool and *evince*.

To change the document’s built-in margins, I used *pdfcrop 2020/06/06 v1.40*, part of Debian’s *texlive-extra-utils 2020.20210202-3* package. First, I removed the document’s built-in margins:

```
$ pdfcrop pattern_A4-letter.pdf
PDFCROP 1.40, 2020/06/06 - Copyright (c) 2002-2020 by Heiko Oberdiek, Oberdiek Package Support Group.
==> 23 pages written on `pattern_A4-letter-crop.pdf'.
```

The cropped document’s right and bottom edges fit on the page, but now the left and top edges spilled off. The final step was to extend the left and top margins of the cropped document by some number of units (arrived at through test-page experimentation), such that no spillover occurred on any side:

```
$ pdfcrop pattern_A4-letter-crop.pdf --margins "50 20 0 0"
PDFCROP 1.40, 2020/06/06 - Copyright (c) 2002-2020 by Heiko Oberdiek, Oberdiek Package Support Group.
==> 23 pages written on `pattern_A4-letter-crop-crop.pdf'.
```

In evince, in the “**Print**” dialog, on the “**Page Setup**” tab, I set “**Scale:**” to “**100.0**” and “**Paper size:**” to “**A4**“. On the “**Page Handling**” tab, I set “**Page Scaling:**” to “**None**” and left “**Select page size using document page size**” unchecked. All of the above steps proved necessary and sufficient to print the pattern at the document-native scale with each tile’s extents fully on the page.

文章来源: https://www.fitzsim.org/blog/?p=518
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)