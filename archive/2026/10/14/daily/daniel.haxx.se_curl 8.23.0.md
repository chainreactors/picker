---
title: curl 8.23.0
url: https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/
source: daniel.haxx.se
date: 2026-10-14
fetch_date: 2026-10-15T06:44:02.704654
---

# curl 8.23.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/10/curl-8-.23.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.23.0

[October 14, 2026](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/#respond)

## Release presentation

## Numbers

the 277th release
4 changes
42 days (total: 10,929)
281 bugfixes (total: 14,770)
476 commits (total: 40,084)
0 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 312)
0 new curl command line option (total: 278)
84 contributors, 58 new (total: 3,844)
45 authors, 28 new (total: 1,546)
24 security fixes (total: 239)

## Security

This time we announce no less than *twenty-four* fixed vulnerabilities. So many that I decided to not list them individually here. Go check them on [the curl security page](https://curl.se/docs/security.html).

## Changes

* The symbol formerly known as `CURL_GLOBAL_WIN32` is now deprecated in favor of the more accurately named `CURL_GLOBAL_WINSOCK`. Used with the [curl\_global\_init](https://curl.se/libcurl/c/curl_global_init.html) function.
* SMB(S) support is gone. Neither curl nor libcurl support these protocols anymore.
* The tool’s [–no-clobber](https://curl.se/docs/manpage.html#--no-clobber) option got two improvements: 1) it now inserts the number into the file name as “-[number]” *before* the file extension if there is an extension. 2) It now tries many more numbers before giving up. Up to 9999.

## Bugfixes

Over two hundred and sixty bugfixes landed in this release. Check them out in the [8.23.0 changelog](https://curl.se/changes.html).

# Post navigation

[Previous PostA slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)[Next PostA UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)

### Leave a Reply [Cancel reply](/blog/2026/10/14/curl-8-23-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
25onefiveeight

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)
  October 14, 2026
* [A UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
  October 14, 2026
* [curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/)
  October 14, 2026
* [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)
  October 13, 2026
* [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/)
  October 12, 2026
* [Twenty-two pending curl vulnerabilities](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/)
  October 7, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27559)
* Jeremy Robst on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27558)
* [Daniel Stenberg](https://daniel.haxx.se/) on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27556)
* Andrei on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27555)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27551)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27550)
* Nick on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27549)
* [Moritz Buhl](https://moritzbuhl.de) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27547)
* [Daniel Stenberg](https://daniel.haxx.se/) on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27545)
* Nun Your Beeswax Inc. on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27544)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

October 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | 6 | [7](https://daniel.haxx.se/blog/2026/10/07/) | 8 | 9 | 10 | 11 |
| [12](https://daniel.haxx.se/blog/2026/10/12/) | [13](https://daniel.haxx.se/blog/2026/10/13/) | [14](https://daniel.haxx.se/blog/2026/10/14/) | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Sep](https://daniel.haxx.se/blog/2026/09/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)