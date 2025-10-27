---
title: wcurl is here
url: https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/
source: daniel.haxx.se
date: 2024-07-04
fetch_date: 2025-10-06T17:43:41.881208
---

# wcurl is here

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/04/tools-1209764_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# wcurl is here

[July 3, 2024](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/#comments)

Users tell us that remembering what curl options to use when they just want to download the contents of a URL is hard. This is one often repeated reason why some users reach for wget instead of curl on the command line. It downloads the data from the URL without you needing to provide any extra arguments. Without you *needing to remember* which option(s) to use.

In [the curl user survey of 2024](https://daniel.haxx.se/blog/2024/06/17/curl-user-survey-2024-analysis/), it was again mentioned several times.

## Enter wcurl

Samuel Henrique decided to do something about it. [Today he announced](https://samueloph.dev/blog/announcing-wcurl-a-curl-wrapper-to-download-files/) that he not only created [wcurl](https://github.com/Debian/wcurl) as a curl wrapper aimed at meeting this exact need, he also created a Debian package out of it and made sure wcurl now ships as part of the curl package. Starting in **8.8.0-2**. I already have it on my Debian unstable installations.

wcurl is implemented a shell script that uses curl. It also ships with its own [manpage](https://manpages.debian.org/unstable/curl/wcurl.1.en.html).

Take it for a spin. Tell the team what you think!

## Discussion

[Hacker news](https://news.ycombinator.com/item?id=40869458)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[wcurl](https://daniel.haxx.se/blog/tag/wcurl/)

# Post navigation

[Previous Postlong term curl versions](https://daniel.haxx.se/blog/2024/06/27/long-term-curl-versions/)[Next Postcurl for QNX](https://daniel.haxx.se/blog/2024/07/05/curl-for-qnx/)

## 4 thoughts on “wcurl is here”

1. ![](https://secure.gravatar.com/avatar/a26f17278f27410c7c0bbf20ff44b9f2880f3937d182066088611df5c83e23e2?s=34&d=monsterid&r=g) **Steffen** says:

   [July 4, 2024 at 10:40](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/#comment-27047)

   This is great. Humble opinion: wcurl should be shipped with curl.

   PS: Thank you for your work on curl!
2. ![](https://secure.gravatar.com/avatar/b34e5bb72bf3f7009295c23443e30a9f7653d75312df5dd67607d7b8fe64d2fe?s=34&d=monsterid&r=g) **Max** says:

   [July 4, 2024 at 12:57](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/#comment-27048)

   Why not just continue to use wget?

   1. ![](https://secure.gravatar.com/avatar/08381cb2010994103eb0db94ec378666f47f0d8963083e6db88a045c2d287d3d?s=34&d=monsterid&r=g) **Bennet Eapen** says:

      [July 4, 2024 at 14:41](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/#comment-27049)

      Exactly what I was thinking…
3. ![](https://secure.gravatar.com/avatar/44e91e4201bafe5e48ab8ee56bb4277a68154b8deacc45816ef6347a80ebf9bf?s=34&d=monsterid&r=g) **Paul Hoffman** says:

   [July 4, 2024 at 18:36](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/#comment-27050)

   +1 to making this part of the curl distribution, and +1 to the repeated thanks for the curl distribution.

   As for “why not use wget”: it has different options and assumptions that curl. They are fine, but remembering which one I’m about to get when I pick between curl and wget is error-prone.

Comments are closed.

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27317)
* Yoann Ricordel on [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/comment-page-1/#comment-27316)
* Ond?ej Surý on [Hello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/comment-page-1/#comment-27315)
* H. Stefan on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27314)
* Tjark on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27313)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

July 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | [3](https://daniel.haxx.se/blog/2024/07/03/) | 4 | [5](https://daniel.haxx.se/blog/2024/07/05/) | 6 | 7 |
| 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| 22 | 23 | [24](https://daniel.haxx.se/blog/2024/07/24/) | 25 | 26 | 27 | 28 |
| 29 | 30 | [31](https://daniel.haxx.se/blog/2024/07/31/) |  | | | |

[« Jun](https://daniel.haxx.se/blog/2024/06/)

[Aug »](https://daniel.haxx.se/blog/2024/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)