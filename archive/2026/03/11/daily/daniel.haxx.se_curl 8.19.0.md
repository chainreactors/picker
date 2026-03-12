---
title: curl 8.19.0
url: https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/
source: daniel.haxx.se
date: 2026-03-11
fetch_date: 2026-03-12T04:07:10.873158
---

# curl 8.19.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/03/curl-8-.19.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.19.0

[March 11, 2026](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/#respond)

## Release presentation

## Numbers

the 273rd release
8 changes
63 days (total: 10,712)
264 bugfixes (total: 13,640)
538 commits (total: 38,024)
0 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 308)
0 new curl command line option (total: 273)
77 contributors, 48 new (total: 3,619)
37 authors, 21 new (total: 1,451)
4 security fixes (total: 180)

## Security

We [stopped the bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) but it has not stopped people from finding vulnerabilities in curl.

* [CVE-2026-1965: bad reuse of HTTP Negotiate connection](https://curl.se/docs/CVE-2026-1965.html)
* [CVE-2026-3783: token leak with redirect and netrc](https://curl.se/docs/CVE-2026-3783.html)
* [CVE-2026-3784: wrong proxy connection reuse with credentials](https://curl.se/docs/CVE-2026-3784.html)
* [CVE-2026-3805: use after free in SMB connection reuse](https://curl.se/docs/CVE-2026-3805.html)

## Changes

* We stopped the bug-bounty. It’s worth repeating, even if it was no code change.
* The cmake build got a `CURL_BUILD_EVERYTHING` option
* Initial support for MQTTS was merged
* curl now supports fractions for –limit-rate and –max-filesize
* curl’s -J option now uses the redirect name as a backup
* we [no longer support OpenSSL-QUIC](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/)
* on Windows, curl can now get built to use the native CA store by default
* the minimum Windows version curl supports is now Vista (up from XP)

## Pending removals

The following upcoming changes might be worth noticing. See [the deprecate documentation](https://curl.se/dev/deprecate.html) for details.

* NTLM support becomes opt-in
* RTMP support is getting dropped
* SMB support becomes opt-in
* Support for c-ares versions before 1.16 goes away
* Support for CMake 3.17 and earlier gets dropped
* TLS-SRP support will be removed

## Next

We plan to ship the next curl release on April 29. See you then!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostDependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/)

### Leave a Reply [Cancel reply](/blog/2026/03/11/curl-8-19-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
eightseven83five

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [curl 8.19.0](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/)
  March 11, 2026
* [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/)
  March 10, 2026
* [10K curl downloads per year](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/)
  March 9, 2026
* [curl up 2026](https://daniel.haxx.se/blog/2026/02/26/curl-up-2026/)
  February 26, 2026
* [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/)
  February 25, 2026
* [decomplexification continued](https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/)
  February 24, 2026

# Recent Comments

* Dmitry on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27414)
* Oleg on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27413)
* Johannes Müller on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27412)
* Gürkan on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27411)
* No One Of Consequence on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27410)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27409)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27408)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27407)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27406)
* mw on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27405)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

March 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| [9](https://daniel.haxx.se/blog/2026/03/09/) | [10](https://daniel.haxx.se/blog/2026/03/10/) | [11](https://daniel.haxx.se/blog/2026/03/11/) | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 |  | | | | |

[« Feb](https://daniel.haxx.se/blog/2026/02/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)