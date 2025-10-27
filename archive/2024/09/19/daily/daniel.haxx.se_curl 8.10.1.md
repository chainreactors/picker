---
title: curl 8.10.1
url: https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/
source: daniel.haxx.se
date: 2024-09-19
fetch_date: 2025-10-06T18:25:30.585704
---

# curl 8.10.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/curl-8.10.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.10.1

[September 18, 2024](https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/#comments)

Welcome to this follow-up patch release, just a week after we shipped [8.10.0](https://daniel.haxx.se/blog/2024/09/11/curl-8-10-0/). *A bunch of bugfixes*.

## Numbers

**the 261th release
0 changes
7 days (total: 9,679)**
**24 bugfixes (total: 10,828)**
**50 commits (total: 33,259)
0 new public libcurl function (total: 94)
0 new curl\_easy\_setopt() option (total: 306)**
**0 new curl command line option (total: 265)**
**19 contributors, 7 new (total: 3,246)**
9 **authors, 1 new (total: 1,303)**
**0 security fixes (total: 158)**

Download the new curl release from [curl.se](https://curl.se/) as always.

## Release presentation

## Bugfixes

These are the perhaps most important ones fixed this time:

* fix configure –with-ca-embed. It could otherwise sometimes lead to an empty bundled CA store.
* cmake: ensure `CURL_USE_OPENSSL`/`USE_OPENSSL_QUIC` are set in sync
* cmake: fix MSH3 to appear on the feature list
* runtests: accecpt ‘quictls’ as OpenSSL compatible. It would previously skip a few tests that are marked OpenSSL specific.
* connect: store connection info when really done
* fix FTP CRLF line endings for ASCII transfer regression. Perhaps most notably this problem was seen on directory listings, which are done using ASCII mode.
* fix HTTP/2 end-of-stream handling when uploading data from stdin
* http: make max-filesize check not count ignored bodies. Like in the case where a URL is redirected to a second place, the first URL might still provide a body that curl ignores.
* fix AF\_INET6 use outside of USE\_IPV6. Made the build fail on systems without IPv6 support.
* check that the multi handle is valid in curl\_multi\_assign. Perhaps not exactly libcurl’s responsibility, but we found at least one application that did this after the 8.10.0 upgrade.
* on QUIC connects, keep on trying on draining server
* request: correctly reset the eos\_sent flag. When doing multiple HTTP/2 uploads using the same handle – this caused problems for git.
* transfer: fix sendrecv() without interim poll. An optimization that optimized a little too much… Most commonly this problem was seen with PHP programs that often (but unwisely) skip the polling.
* rustls: fixed minor logic bug in default cipher selection
* rustls: support strong CSRNG data. Now every curl build using TLS ensures use of strong random numbers.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Posttrurl 0.15.1](https://daniel.haxx.se/blog/2024/09/12/trurl-0-15-1/)[Next Posttrurl 0.16](https://daniel.haxx.se/blog/2024/09/19/trurl-0-16/)

## One thought on “curl 8.10.1”

1. ![](https://secure.gravatar.com/avatar/d5e4491f5d1df0cf18b245274b5fa8ecc27f6cca744d18a2283e21066371992e?s=34&d=monsterid&r=g) **[Carlos Saltos](http://csaltos.com)** says:

   [September 18, 2024 at 08:15](https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/#comment-27067)

   Gracias !!

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