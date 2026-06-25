---
title: curl 8.21.0
url: https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/
source: daniel.haxx.se
date: 2026-06-24
fetch_date: 2026-06-25T06:08:44.598784
---

# curl 8.21.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/06/curl-8-.21.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.21.0

[June 24, 2026](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/#respond)

## Release presentation

## Numbers

the 275th release
6 changes
56 days (total: 10,817)
276 bugfixes (total: 14,187)
531 commits (total: 39,077)
0 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 308)
1 new curl command line option (total: 274)
102 contributors, 69 new (total: 3,731)
45 authors, 26 new (total: 1,489)
18 security fixes (total: 206)

## Security

As [mentioned before](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/), the security report volume has been intense lately. We publish *eighteen* new curl vulnerabilities this time. A new project record for a single release and for the total number of vulnerabilities published within the same calendar year.

As always, we have document each vulnerability in detail and I encourage you to read up on the details.

### Severity Medium

* [CVE-2026-8925](https://curl.se/docs/CVE-2026-8925.html): SASL double-free
* [CVE-2026-8927](https://curl.se/docs/CVE-2026-8927.html): env-set cross-proxy Digest auth state leak
* [CVE-2026-9079](https://curl.se/docs/CVE-2026-9079.html): stale proxy password leak
* [CVE-2026-11856](https://curl.se/docs/CVE-2026-11856.html): cross-origin Digest auth state leak

### Severity Low

* [CVE-2026-8286](https://curl.se/docs/CVE-2026-8286.html): wrong STARTTLS connection reuse
* [CVE-2026-8458](https://curl.se/docs/CVE-2026-8458.html): wrong reuse for different services
* [CVE-2026-8924](https://curl.se/docs/CVE-2026-8924.html): trailing dot domain super cookie
* [CVE-2026-8926](https://curl.se/docs/CVE-2026-8926.html): password leak with netrc and user in URL
* [CVE-2026-8932](https://curl.se/docs/CVE-2026-8932.html): incomplete mTLS config matching in conn reuse
* [CVE-2026-9080](https://curl.se/docs/CVE-2026-9080.html): UAF after pause in socket callback
* [CVE-2026-9545](https://curl.se/docs/CVE-2026-9545.html): exposing HTTP/3 early data
* [CVE-2026-9546](https://curl.se/docs/CVE-2026-9546.html): sending old referer
* [CVE-2026-9547](https://curl.se/docs/CVE-2026-9547.html): SSH improper host validation
* [CVE-2026-10536](https://curl.se/docs/CVE-2026-10536.html): HTTP/2 stream-dependency tree UAF
* [CVE-2026-11352](https://curl.se/docs/CVE-2026-11352.html): QUIC zero-length UDP datagrams busy-loop
* [CVE-2026-11564](https://curl.se/docs/CVE-2026-11564.html): Native CA trust persist
* [CVE-2026-11586](https://curl.se/docs/CVE-2026-11586.html): WS Auto-PONG memory exhaustion
* [CVE-2026-12064](https://curl.se/docs/CVE-2026-12064.html): proto-default skips SSH verification

## Changes

The huge focus on vulnerability reports during this release cycle made us merge fewer new features than we wanted, but here are the ones we still managed to get to:

* curl: [named globs](https://daniel.haxx.se/blog/2026/05/16/named-globs-with-curl/)
* curl: named globs in output file name for uploads
* HTTP/3 proxy CONNECT and MASQUE CONNECT-UDP support
* removed HTTP/2 stream dependency tracking
* removed support for CURLAUTH\_DIGEST\_IE
* added support for SHA256 host public keys with libssh

## Bugfixes

We again manage to land more than 250 separate bugfixes, and they are all detailed in [the changelog](https://curl.se/ch/).

## Pending removals

Planned upcoming removals include:

* local crypto implementations
* NTLM
* SMB
* TLS-SRP support

If you are concerned about any of these, speak up on the [curl-library list](https://curl.se/mail/list.cgi?list=curl-library) ASAP.

## Next release

Unless we messed up this one and need to do a patch release, the pending next release is scheduled to happen on September 2. This release cycle is extended by two weeks due to [the summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/).

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostQUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/)[Next Posta CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)

### Leave a Reply [Cancel reply](/blog/2026/06/24/curl-8-21-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
9nineeighteightone

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)
  June 24, 2026
* [curl 8.21.0](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/)
  June 24, 2026
* [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/)
  June 21, 2026
* [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)
  June 15, 2026
* [A human in control](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/)
  June 10, 2026
* [curl up 2026 summary](https://daniel.haxx.se/blog/2026/05/28/curl-up-2026-summary/)
  May 28, 2026

# Recent Comments

* MORIWAKE Shigeru on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27516)
* [Kavyansh Garg](https://kavyansh.me) on [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/comment-page-1/#comment-27515)
* [XQ539](https://wayne-intressierts.de) on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27514)
* fridayafternoon on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27513)
* ThankFull on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27512)
* fm on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27509)
* H. Stefan on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27508)
* bengan on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27507)
* Sam on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27506)
* [webknjaz (Sviatoslav Sydorenko)](https://webknjaz.me) on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27505)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

June 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 8 | 9 | [10](https://daniel.haxx.se/blog/2026/06/10/) | 11 | 12 | 13 | 14 |
| [15](https://daniel.haxx.se/blog/2026/06/15/) | 16 | 17 | 18 | 19 | 20 | [21](https://daniel.haxx.se/blog/2026/06/21/) |
| 22 | 23 | [24](https://daniel.haxx.se/blog/2026/06/24/) | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« May](https://daniel.haxx.se/blog/2026/05/)

[Privacy]...