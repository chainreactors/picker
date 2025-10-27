---
title: Copyright without years
url: https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/
source: daniel.haxx.se
date: 2023-01-09
fetch_date: 2025-10-04T03:21:37.290471
---

# Copyright without years

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/10/Screenshot-2018-2-16-BMW-i3-Open-Source-Licences-YouTube-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Copyright without years

[January 8, 2023](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [13 Comments](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comments)

Like so many other software projects the curl project has copyright mentions at the top of almost every file in the source code repository. Like

```
Copyright (C) 1998 - 2022, Daniel Stenberg ...
```

Over the years we have used a combination of scripts and manual edits to update the ending year in that copyright line to match the year of the latest update of that file.

As soon as we started a new year and someone updated a file, the copyright range needed update. Scripts and tools made it less uncomfortable, but it was always somewhat of a pain to remember and fix.

## In 2023 this changed

When the year was again bumped and the first changes of the year were done to curl, we should then consequentially start updating years again to make ranges end with 2023.

Only this time someone asked me *why?* and it made me decide that *what the heck, let’s completely rip them out instead!* Doing it at the beginning of the year is also a very good moment.

## Do we need the years?

The [Berne Convention](https://en.wikipedia.org/wiki/Berne_Convention) states that copyright “must be automatic; it is prohibited to require formal registration”.

The often-used copyright lines are not necessary to protect our rights. According to the Wikipedia page mentioned above, the Berne Convention has been ratified by 181 states out of 195 countries in the world.

They can still serve a purpose as they are informational and make the ownership question quite clear. The year ranges add questionable value though.

I have tried to find resources that argue **for** the importance of the copyright years to be stated and present, but I have not found any credible sources. Possibly because I haven’t figured out where to look.

## Not alone

It turns out quite a few projects run by many different organizations or even huge companies have already dropped the years from their source code header copyright statements. Presumably at least some of those giant corporations have had their legal departments give a green light to the idea before they went ahead and published source code that way to the world.

## Low risk

We own the copyrights no matter if the years are stated or not. The exact years the files were created or edited can still easily be figured out since we use version control, should anyone ever actually care about it. And we give away curl for free, under an extremely liberal license.

I don’t think we risk much by doing this move.

## January 3, 2023

On this day I merged commit [2bc1d775f510](https://github.com/curl/curl/commit/2bc1d775f510196154283374284f98d3eae03544), which updated 1856 files and removed copyright years from almost everywhere in the source code repository.

I decided to leave them in the [main license file](https://github.com/curl/curl/blob/master/COPYING). Partly because this is a file that lots of companies include in their products and I have had some use of seeing the year ranges in there in the past!

## Bliss

Now we can forget about copyright years in the project. It’s a relief!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[source code](https://daniel.haxx.se/blog/tag/source-code/)

# Post navigation

[Previous PostAn m1 for curl](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/)[Next PostMy weekly report on email](https://daniel.haxx.se/blog/2023/01/10/my-weekly-report-on-email/)

## 13 thoughts on “Copyright without years”

1. ![](https://secure.gravatar.com/avatar/e8ba51324d89c6b187da36a19917b5feab8a6ed0f7cdafa5f3f754a179490b61?s=34&d=monsterid&r=g) **[Roy Fielding](https://roy.gbiv.com/)** says:

   [January 10, 2023 at 00:43](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comment-26544)

   Yes, and no, and but …

   Yes, it is low risk to remove the years because you don’t intend to enforce the copyright.

   And, no, those files should not have had a range of years in the first place (that’s an ambiguous notice, which would be interpreted as the first year anyway). It’s a cargo cult thing.

   But the committed version isn’t a valid notice at all, since the year of first publication is required to make it so (at least in the US). The US code is described at <https://www.copyright.gov/title17/92chap4.html>

   Note that a valid copyright notice also has value as a deterrent and as sticky documentation. The law (and some OSS licenses) require that such notices be retained unaltered.

   OTOH, removing all of the notices is fine, if that is what you want to do. My preference is to have one, overall, valid copyright notice in README or NOTICE files. That one should have a date of first publication, which usually refers to the date that this overall collected/joint work is published (i.e., this year). But you can also choose to just make it the year that the file was created and never have to update it again.

   1. ![](https://secure.gravatar.com/avatar/910bbb3911a4a39325f4922fb42222666ea2329e562e368af78615ee1136b8ce?s=34&d=monsterid&r=g) **Cody Schafer** says:

      [January 10, 2023 at 01:59](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comment-26545)

      Note the “a notice of copyright as provided by this section may be placed on” within the linked page ( <https://www.copyright.gov/title17/92chap4.html> ). I.E.: note the “\_may\_”.

      This was changed by H.R.4262 – Berne Convention Implementation Act of 1988, (<https://www.congress.gov/bill/100th-congress/house-bill/4262/text>), from “shall be placed on all” making the Notice of Copyright optional.

      So it’s correct that in the context of the 401 that “Copyright ” is not a “Notice of Copyright”, but it’s also not required for copyright to be established (since 1988).
   2. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 10, 2023 at 09:11](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comment-26546)

      I keep the copyright mentions (without years) for informational purposes for those who find the files and read them. They then tell the reader who owns the copyright and explain the license.

      This happens to also match how the REUSE check/project wants them.
2. ![](https://secure.gravatar.com/avatar/8e908b28dd21db7518d2b85480a95b6235b0eff69f31b4d903d6bfd0895aaa08?s=34&d=monsterid&r=g) **[Jeffrey Paul](https://jeffpaul.com)** says:

   [January 10, 2023 at 21:27](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comment-26547)

   Is there any rationale perhaps to include the original year when the file was created as a sort of “copyrighted from this year onward”? So perhaps a copyright line like “Copyright (C) 1998+, Daniel Stenberg, , et al.”?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 10, 2023 at 23:40](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/#comment-26548)

      @Jeffrey: sure, that would still solve the update-pro...