---
title: curl 8.18.0
url: https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/
source: daniel.haxx.se
date: 2026-01-07
fetch_date: 2026-01-08T03:29:13.185250
---

# curl 8.18.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/01/curl-8-.18.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.18.0

[January 7, 2026](https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/#respond)

Download curl from [curl.se](https://curl.se/)!

## Release presentation

## Numbers

the 272nd release
5 changes
63 days (total: 10,155)
391 bugfixes (total: 13,376)
758 commits (total: 37,486)
0 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 308)
0 new curl command line option (total: 273)
69 contributors, 36 new (total: 3,571)
37 authors, 14 new (total: 1,430)
6 security fixes (total: 176)

## Security

This time there is no less than *six* separate vulnerabilities announced.

* [CVE-2025-13034](https://curl.se/docs/CVE-2025-13034.html): skipping pinning check for HTTP/3 with GnuTLS
* [CVE-2025-14017](https://curl.se/docs/CVE-2025-14017.html): broken TLS options for threaded LDAPS
* [CVE-2025-14524](https://curl.se/docs/CVE-2025-14524.html): bearer token leak on cross-protocol redirect
* [CVE-2025-14819](https://curl.se/docs/CVE-2025-14819.html): OpenSSL partial chain store policy bypass
* [CVE-2025-15079](https://curl.se/docs/CVE-2025-15079.html): libssh global knownhost override
* [CVE-2025-15224](https://curl.se/docs/CVE-2025-15224.html): libssh key passphrase bypass without agent set

## Changes

There are a few this time, mostly around dropping support for various dependencies:

* drop support for VS2008 (Windows)
* drop Windows CE / CeGCC support
* drop support for GnuTLS < 3.6.5
* gnutls: implement CURLOPT\_CAINFO\_BLOB
* openssl: bump minimum OpenSSL version to 3.0.0

## Bugfixes

See the release presentation video for a walk-through of some of the most important/interesting fixes done for this release, or go check out the full list in [the changelog](https://curl.se/ch/).

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Post6,000 curl stickers](https://daniel.haxx.se/blog/2026/01/06/6000-curl-stickers/)

### Leave a Reply [Cancel reply](/blog/2026/01/07/curl-8-18-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
8three7seven7

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [curl 8.18.0](https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/)
  January 7, 2026
* [6,000 curl stickers](https://daniel.haxx.se/blog/2026/01/06/6000-curl-stickers/)
  January 6, 2026
* [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/)
  December 29, 2025
* [A curl 2025 review](https://daniel.haxx.se/blog/2025/12/23/a-curl-2025-review/)
  December 23, 2025
* [20,000 issues on GitHub](https://daniel.haxx.se/blog/2025/12/16/20000-issues-on-github/)
  December 16, 2025
* [Parsing integers in C](https://daniel.haxx.se/blog/2025/11/13/parsing-integers-in-c/)
  November 13, 2025

# Recent Comments

* Ted Lyngmo on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27379)
* tetsuoii on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27378)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27377)
* spagoveanu on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27376)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27375)
* [Verisimilitude](http://verisimilitudes.net) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27374)
* Billy O'Neal on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27373)
* Billy O'Neal on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27372)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27371)
* John Brown II on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27370)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

January 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2026/01/06/) | [7](https://daniel.haxx.se/blog/2026/01/07/) | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Dec](https://daniel.haxx.se/blog/2025/12/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)