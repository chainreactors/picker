---
title: trurl 0.16
url: https://daniel.haxx.se/blog/2024/09/19/trurl-0-16/
source: daniel.haxx.se
date: 2024-09-20
fetch_date: 2025-10-06T18:27:07.487646
---

# trurl 0.16

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/trurl-0.16.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# trurl 0.16

[September 19, 2024](https://daniel.haxx.se/blog/2024/09/19/trurl-0-16/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

([Download trurl here](https://curl.se/trurl/))

## Release presentation

At 08:00 UTC I will do a [live-streamed release presentation of trurl 0.16 on Twitch](https://www.twitch.tv/curlhacker).

## Bump

I decided to bump the minor version number again because there is a new option: `--qtrim`.

This is the old `--trim` option made simpler and specialized for query components only. When we added originally `--trim`, the idea was that it would be similar to `--set` and `--get` and be able to trim different components – but over time we have realized that the only component the trimming operation really makes sense for is query.

Hence, now we have the query trim option and the old trim option is deprecated. The old option still works but is not advertised in the `--help` output.

## Manpage

[The trurl manpage](https://curl.se/trurl/manual.html) now features a section describing the different URL components, how they work and some specific options that affect them. With examples.

The manpage has almost doubled in size compared to [0.15.1](https://daniel.haxx.se/blog/2024/09/12/trurl-0-15-1/) and the nroff version is now over 800 lines long. All in the name of making sure every option and feature is understood properly.

## Bugfixes

* query normalization. When a name/value pair had a blank string on either side of the equals character, trurl messed it up.
* user/password/options/fragment normalization. trurl now normalizes all these fields if provided.
* lowercase %-encoding. In some instances trurl was not consistently using lowercase hexadecimal in its output.

## Tests

I looked for white spots in the test suite: untested options and option combinations, and have worked to fill those voids. This release has around thirty new test cases and trurl is now verified using more than two hundred tests.

[trurl](https://daniel.haxx.se/blog/tag/trurl/)

# Post navigation

[Previous Postcurl 8.10.1](https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/)[Next PostTalk: Keeping the world from Burning](https://daniel.haxx.se/blog/2024/09/25/talk-keeping-the-world-from-burning/)

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

September 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| [2](https://daniel.haxx.se/blog/2024/09/02/) | 3 | 4 | 5 | 6 | 7 | 8 |
| 9 | 10 | [11](https://daniel.haxx.se/blog/2024/09/11/) | [12](https://daniel.haxx.se/blog/2024/09/12/) | 13 | 14 | 15 |
| 16 | 17 | [18](https://daniel.haxx.se/blog/2024/09/18/) | [19](https://daniel.haxx.se/blog/2024/09/19/) | 20 | 21 | 22 |
| 23 | 24 | [25](https://daniel.haxx.se/blog/2024/09/25/) | 26 | 27 | 28 | 29 |
| 30 |  | | | | | |

[« Aug](https://daniel.haxx.se/blog/2024/08/)

[Oct »](https://daniel.haxx.se/blog/2024/10/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)