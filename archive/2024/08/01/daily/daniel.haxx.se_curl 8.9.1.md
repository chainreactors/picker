---
title: curl 8.9.1
url: https://daniel.haxx.se/blog/2024/07/31/curl-8-9-1/
source: daniel.haxx.se
date: 2024-08-01
fetch_date: 2025-10-06T18:04:26.887184
---

# curl 8.9.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/07/curl-8.9.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.9.1

[July 31, 2024](https://daniel.haxx.se/blog/2024/07/31/curl-8-9-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Some annoying regressions triggered this.

## Numbers

**the 259th release
0 changes
7 days (total: 9,630)**
**28 bugfixes (total: 10,559)**
**43 commits (total: 32,748)
0 new public libcurl function (total: 94)
0 new curl\_easy\_setopt() option (total: 306)**
**0 new curl command line option (total: 263)**
**19 contributors, 5 new (total: 3,211)**
**10 authors, 1 new (total: 1,288)**
**1 security fixes (total: 158)**

Download the new curl release from [curl.se](https://curl.se/) as always.

## Release presentation

## Security

We decided to do a patch release. Then yesterday we got a security vulnerability reported and so now we have that fixed in here as well.

[CVE-2024-7264: ASN.1 date parser overread](https://curl.se/docs/CVE-2024-7264.html) (*severity low*) libcurl’s ASN1 parser code has the `GTime2str()` function, used for parsing an ASN.1 Generalized Time field. If given an syntactically incorrect field, the parser might end up using -1 for the length of the *time fraction*, leading to a `strlen()` getting performed on a pointer to a heap buffer area that is not (purposely) null terminated.

## Bugfixes

This release is done only because we shipped a few regressions in 8.9.0 we rather let users avoid. Here are some noteworthy fixes from the past week:

* connection shutdown fix for event based processing – this would cause applications to keep monitoring sockets “too much”, easily leading to busy-loops or worse
* cmake builds detect libssh and nettle better
* several libcurl functions now survive NULL pointer inputs better
* fixed an Apple SDK bug workaround for non-macOS targets
* the curl tool builds with the manual enabled on OS400
* works around an IBM (OS400) ASCII run-time library bug
* speed limiting for 32bit systems had the wrong math
* allow wolfSSL’s implementation of kyber to be used
* wolfssl CA store caching fix
* more defensive and portable socket code for the curl tool’s `--ip-tos` logic

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postchangelog changes](https://daniel.haxx.se/blog/2024/07/24/changelog-changes/)[Next Postlibcurl is 24 years old](https://daniel.haxx.se/blog/2024/08/06/libcurl-is-24-years-old/)

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