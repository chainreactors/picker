---
title: curl 8.14.0
url: https://daniel.haxx.se/blog/2025/05/28/curl-8-14-0/
source: daniel.haxx.se
date: 2025-05-29
fetch_date: 2025-10-06T22:29:00.328548
---

# curl 8.14.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/curl-8.14.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.14.0

[May 28, 2025](https://daniel.haxx.se/blog/2025/05/28/curl-8-14-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2025/05/28/curl-8-14-0/#comments)

Welcome to another curl release.

## Release presentation

## Numbers

the 267th release
6 changes
56 days (total: 9,931)
229 bugfixes (total: 12,015)
406 commits (total: 35,190)
0 new public libcurl function (total: 96)
1 new curl\_easy\_setopt() option (total: 308)
1 new curl command line option (total: 269)
91 contributors, 47 new (total: 3,426)
36 authors, 17 new (total: 1,375)
2 security fixes (total: 166)

## Security

* [CVE-2025-4947: QUIC certificate check skip with wolfSSL](https://curl.se/docs/CVE-2025-4947.html)
* [CVE-2025-5025: No QUIC certificate pinning with wolfSSL](https://curl.se/docs/CVE-2025-5025.html)

## Changes

* When doing MQTT, curl now sends pings
* The Schannel backend now supports pkcs12 client certificates containing CA certificates
* Added `CURLOPT_SSL_SIGNATURE_ALGORITHMS` and `--sigalgs` for the OpenSSL backend
* ngtcp2 + OpenSSL’s new QUIC API is now supported. Requires OpenSSL 3.5 or later.
* wcurl comes bundled in the curl tarball
* websocket can now disable auto-pong

## Bugfixes

See the changelog on the curl site for the full set, or watch the release presentation for a “best of” collection.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostThe curl user survey 2025 is up](https://daniel.haxx.se/blog/2025/05/19/the-curl-user-survey-2025-is-up/)[Next PostDecomplexification](https://daniel.haxx.se/blog/2025/05/29/decomplexification/)

## One thought on “curl 8.14.0”

1. ![](https://secure.gravatar.com/avatar/fd34001f44983edfeb0e400944f5b8db1c292171915754ae8b46b2ebc3a298ea?s=34&d=monsterid&r=g) **Luna Jernberg** says:

   [May 28, 2025 at 14:42](https://daniel.haxx.se/blog/2025/05/28/curl-8-14-0/#comment-27184)

   a regression has been found so coming a 8.14.1 i think:

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

May 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2025/05/06/) | 7 | 8 | 9 | 10 | 11 |
| 12 | [13](https://daniel.haxx.se/blog/2025/05/13/) | [14](https://daniel.haxx.se/blog/2025/05/14/) | 15 | [16](https://daniel.haxx.se/blog/2025/05/16/) | 17 | 18 |
| [19](https://daniel.haxx.se/blog/2025/05/19/) | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | [28](https://daniel.haxx.se/blog/2025/05/28/) | [29](https://daniel.haxx.se/blog/2025/05/29/) | 30 | 31 |  |

[« Apr](https://daniel.haxx.se/blog/2025/04/)

[Jun »](https://daniel.haxx.se/blog/2025/06/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)