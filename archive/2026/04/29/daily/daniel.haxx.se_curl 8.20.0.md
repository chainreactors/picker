---
title: curl 8.20.0
url: https://daniel.haxx.se/blog/2026/04/29/curl-8-20-0/
source: daniel.haxx.se
date: 2026-04-29
fetch_date: 2026-04-30T05:29:01.014458
---

# curl 8.20.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/curl-8-.20.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.20.0

[April 29, 2026](https://daniel.haxx.se/blog/2026/04/29/curl-8-20-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/04/29/curl-8-20-0/#respond)

You always find the new curl releases [on the curl site](https://curl.se/)!

## Release presentation

## Numbers

the 274th release
8 changes
49 days (total: 10,761)
282 bugfixes (total: 13,922)
521 commits (total: 38,545)
0 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 308)
0 new curl command line option (total: 273)
73 contributors, 45 new (total: 3,664)
28 authors, 12 new (total: 1,463)
8 security fixes (total: 188)

## Security

As [mentioned elsewhere](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/), the security reporting volume has been intense lately. We publish *eight* new curl vulnerabilities this time.

* [CVE-2026-7168: cross-proxy Digest auth state leak](https://curl.se/docs/CVE-2026-7168.html)
* [CVE-2026-7009: OCSP stapling bypass with Apple SecTrust](https://curl.se/docs/CVE-2026-7009.html)
* [CVE-2026-6429: netrc credential leak with reused proxy connection](https://curl.se/docs/CVE-2026-6429.html)
* [CVE-2026-6276: stale custom cookie host causes cookie leak](https://curl.se/docs/CVE-2026-6276.html)
* [CVE-2026-6253: proxy credentials leak over redirect-to proxy](https://curl.se/docs/CVE-2026-6253.html)
* [CVE-2026-5773: wrong reuse of SMB connection](https://curl.se/docs/CVE-2026-5773.html)
* [CVE-2026-5545: wrong reuse of HTTP Negotiate connection](https://curl.se/docs/CVE-2026-5545.html)
* [CVE-2026-4873: connection reuse ignores TLS requirement](https://curl.se/docs/CVE-2026-4873.html)

## Changes

* now uses a thread pool and queue for resolving
* NTLM is disabled by default
* dropped support for CMake 3.17 and older
* dropped support for < c-ares 1.16.0
* SMB is disabled by default
* added CURLMNWC\_CLEAR\_ALL for all network changes
* [dropped RTMP support](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/)

## Bugfixes

The official count says over 260 bugfixes were merged in this 49 day cycle. See the [changelog](https://curl.se/ch/) for all the details.

## Pending Removals

Planned upcoming removals include:

* local crypto implementations
* NTLM
* SMB
* TLS-SRP support

If you are concerned about any of these, speak up on the curl-library ASAP.

## Next release

Unless we messed up this one and need to do a patch release, the pending next release is scheduled to happen on June 24.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostHigh-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/)

### Leave a Reply [Cancel reply](/blog/2026/04/29/curl-8-20-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
fourthree2four4

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [curl 8.20.0](https://daniel.haxx.se/blog/2026/04/29/curl-8-20-0/)
  April 29, 2026
* [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/)
  April 22, 2026
* [Don’t trust, verify](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/)
  March 26, 2026
* [One hundred weirdo emails](https://daniel.haxx.se/blog/2026/03/25/one-hundred-weirdo-emails/)
  March 25, 2026
* [NTLM and SMB go opt-in](https://daniel.haxx.se/blog/2026/03/22/ntlm-and-smb-go-opt-in/)
  March 22, 2026
* [bye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/)
  March 21, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27435)
* Name on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27434)
* Willy on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27433)
* [Daniel Stenberg](https://daniel.haxx.se/) on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27432)
* [Jan Tångring](https://etn.se/) on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27431)
* mw on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27430)
* Mats Lundgren on [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/comment-page-1/#comment-27429)
* [Fayner](https://fagnerbrack.com) on [One hundred weirdo emails](https://daniel.haxx.se/blog/2026/03/25/one-hundred-weirdo-emails/comment-page-1/#comment-27426)
* Mayank Sinha on [Don’t trust, verify](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/comment-page-1/#comment-27423)
* [Daniel Stenberg](https://daniel.haxx.se/) on [One hundred weirdo emails](https://daniel.haxx.se/blog/2026/03/25/one-hundred-weirdo-emails/comment-page-1/#comment-27421)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

April 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | 1 | 2 | 3 | 4 | 5 |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | [22](https://daniel.haxx.se/blog/2026/04/22/) | 23 | 24 | 25 | 26 |
| 27 | 28 | [29](https://daniel.haxx.se/blog/2026/04/29/) | 30 |  | | |

[« Mar](https://daniel.haxx.se/blog/2026/03/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)