---
title: curl 8.22.0
url: https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/
source: daniel.haxx.se
date: 2026-09-02
fetch_date: 2026-09-03T06:39:07.845153
---

# curl 8.22.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/08/curl-8-.22.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.22.0

[September 2, 2026](https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/#respond)

Welcome to this new release. Get it as always from <https://curl.se>.

If you rather want a security-patched older release branch, stay tuned for the follow-up [Rock-solid curl](https://rock-solid.curl.dev/) announcement within a few days.

## Release presentation

## Numbers

the 276th release
6 changes
70 days (total: 10,887)
302 bugfixes (total: 14,489)
525 commits (total: 39,608)
0 new public libcurl function (total: 100)
4 new curl\_easy\_setopt() option (total: 312)
4 new curl command line option (total: 278)
85 contributors, 55 new (total: 3,786)
43 authors, 29 new (total: 1,518)
9 security fixes (total: 215)

## Security

Associated with this release, we publish ten new CVEs. Nine of them are for curl and libcurl, and one is for wcurl.

* [CVE-2026-13608](https://curl.se/docs/CVE-2026-13608.html): OpenLDAP SASL authentication bypass
* [CVE-2026-18924](https://curl.se/docs/CVE-2026-18924.html): HTTP/2 server push UAF
* [CVE-2026-19931](https://curl.se/docs/CVE-2026-19931.html): Negotiate ambient user conn reuse
* [CVE-2026-80229](https://curl.se/docs/CVE-2026-80229.html): OpenSSL provider use-after-free
* [CVE-2026-80230](https://curl.se/docs/CVE-2026-80230.html): OpenSSL pinning bypass
* [CVE-2026-80231](https://curl.se/docs/CVE-2026-80231.html): native CA store conn reuse
* [CVE-2026-80255](https://curl.se/docs/CVE-2026-80255.html): secure cookie attribute bypass with tab
* [CVE-2026-82208](https://curl.se/docs/CVE-2026-82208.html): wolfSSL CA-cache hit overrides callback
* [CVE-2026-82209](https://curl.se/docs/CVE-2026-82209.html): domain-scoped PSL domain cookie

The wcurl one:

[CVE-2026-80256](https://curl.se/docs/CVE-2026-80256.html): wcurl backslash bypass

## Changes

* added support for Apple GSS Framework
* added API guards
* new RFC 9421 HTTP Message Signatures support (experimental)
* blocks NTLM fallback in SPNEGO negotiation
* dropped support for TLS-SRP
* added option to use Apple fast UDP

## Coming removals

* HTTP/2 Server Push
* local crypto implementations
* NTLM
* SMB

## Next

We plan the next curl release to happen at the end of October unless there are some bad regressions reported against 8.22.0.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostThere’s a libcurl.dll in my system32](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/)

### Leave a Reply [Cancel reply](/blog/2026/09/02/curl-8-22-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
17foursix5

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [curl 8.22.0](https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/)
  September 2, 2026
* [There’s a libcurl.dll in my system32](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/)
  August 17, 2026
* [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/)
  August 14, 2026
* [What the bliss taught us](https://daniel.haxx.se/blog/2026/08/03/what-the-bliss-taught-us/)
  August 3, 2026
* [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/)
  July 27, 2026
* [1,500 curl authors](https://daniel.haxx.se/blog/2026/07/25/1500-curl-authors/)
  July 25, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27551)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27550)
* Nick on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27549)
* [Moritz Buhl](https://moritzbuhl.de) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27547)
* [Daniel Stenberg](https://daniel.haxx.se/) on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27545)
* Nun Your Beeswax Inc. on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27544)
* Matthias Hörmann on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27539)
* entronid on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27538)
* Willy on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27537)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27536)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

September 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | [2](https://daniel.haxx.se/blog/2026/09/02/) | 3 | 4 | 5 | 6 |
| 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 |
| 28 | 29 | 30 |  | | | |

[« Aug](https://daniel.haxx.se/blog/2026/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)