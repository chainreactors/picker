---
title: curl 8.14.1
url: https://daniel.haxx.se/blog/2025/06/04/curl-8-14-1/
source: daniel.haxx.se
date: 2025-06-05
fetch_date: 2025-10-06T22:53:22.061407
---

# curl 8.14.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/06/curl-8.14.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.14.1

[June 4, 2025](https://daniel.haxx.se/blog/2025/06/04/curl-8-14-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

This is a patch-release done only a week since the previous version with no changes merged only bugfixes. Because some of the regressions in 8.14.0 were a little too annoying to leave unattended for a full cycle.

## Release presentation

## Numbers

the 268th release
0 changes
7 days (total: 9,938)
35 bugfixes (total: 12,049)
48 commits (total: 35,238)
0 new public libcurl function (total: 96)
0 new curl\_easy\_setopt() option (total: 308)
0 new curl command line option (total: 269)
20 contributors, 4 new (total: 3,431)
9 authors, 1 new (total: 1,376)
1 security fix (total: 167)

## Security

[CVE-2025-5399: WebSocket endless loop](https://curl.se/docs/CVE-2025-5399.html). A malicious WebSocket server can send a particularly crafted packet which makes libcurl get trapped in an endless busy-loop. Severity LOW.

## Bugfixes

We count about 31 bugfixes, view them all on [the 8.14.1 changelog page](https://curl.se/ch/8.14.1.html).

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostDecomplexification](https://daniel.haxx.se/blog/2025/05/29/decomplexification/)[Next PostWhat we can’t measure](https://daniel.haxx.se/blog/2025/06/05/what-we-cant-measure/)

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

June 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| 2 | 3 | [4](https://daniel.haxx.se/blog/2025/06/04/) | [5](https://daniel.haxx.se/blog/2025/06/05/) | 6 | 7 | 8 |
| 9 | 10 | [11](https://daniel.haxx.se/blog/2025/06/11/) | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| [23](https://daniel.haxx.se/blog/2025/06/23/) | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 |  | | | | | |

[« May](https://daniel.haxx.se/blog/2025/05/)

[Jul »](https://daniel.haxx.se/blog/2025/07/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)