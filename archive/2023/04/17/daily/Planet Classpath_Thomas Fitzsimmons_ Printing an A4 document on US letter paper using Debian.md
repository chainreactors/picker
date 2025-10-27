---
title: Thomas Fitzsimmons: Printing an A4 document on US letter paper using Debian
url: https://www.fitzsim.org/blog/?p=518
source: Planet Classpath
date: 2023-04-17
fetch_date: 2025-10-04T11:31:27.402093
---

# Thomas Fitzsimmons: Printing an A4 document on US letter paper using Debian

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Printing an A4 document on US letter paper using Debian

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [April 15, 2023April 15, 2023](https://www.fitzsim.org/blog/?p=518)
[Leave a comment on Printing an A4 document on US letter paper using Debian](https://www.fitzsim.org/blog/?p=518#respond)

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

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[April 15, 2023April 15, 2023](https://www.fitzsim.org/blog/?p=518)Posted in[Uncategorized](https://www.fitzsim.org/blog/?cat=1)

## Post navigation

[Previous Post Previous post:
llama.cpp and POWER9](https://www.fitzsim.org/blog/?p=511)

[Next Post Next post:
Pixel phones are sold with bootloader unlocking disabled](https://www.fitzsim.org/blog/?p=545)

## Leave a comment

### [Cancel reply](/blog/?p=518#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)