---
title: curl 8.11.0
url: https://daniel.haxx.se/blog/2024/11/06/curl-8-11-0/
source: daniel.haxx.se
date: 2024-11-07
fetch_date: 2025-10-06T19:18:22.663182
---

# curl 8.11.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/10/curl-8.11.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.11.0

[November 6, 2024](https://daniel.haxx.se/blog/2024/11/06/curl-8-11-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

## Numbers

**the 262nd release
5 changes
49 days (total: 9,728)**
**266 bugfixes (total: 11,094)**
**435 commits (total: 33,694)
0 new public libcurl function (total: 94)
0 new curl\_easy\_setopt() option (total: 306)**
**1 new curl command line option (total: 266)**
**55 contributors, 22 new (total: 3,268)**
**25 authors, 10 new (total: 1,312)**
**1 security fixes (total: 160)**

## Release presentation

## Security

[CVE-2024-9681: HSTS subdomain overwrites parent cache entry](https://curl.se/docs/CVE-2024-9681.html). When curl is asked to use HSTS, the expiry time for a subdomain might overwrite a parent domain’s cache entry, making it end sooner or later than otherwise intended.

## Changes

* –create-dirs works for –dump-header as well
* P12 format support added to GnuTLS backend
* Added options to disable IPFS
* TLSv1.3 earlydata support (with GnuTLS)
* Official WebSocket support

## Bugfixes

These are some of my favorite bugfixes in this release.

### Build

* cmake: document -D and env build options
* configure: add support for ‘unity’ builds
* configure: set linker flags to allow rustls build on macos

### curl

* detect ECH support dynamically, not at build time
* support –show-headers AND –remote-header-name
* make –skip-existing work for –parallel

### libcurl

* conncache: find bundle again in case it is removed
* curl.h: remove the struct pointer for CURL/CURLSH/CURLM typedefs
* ftp: fix 0-length last write on upload from stdin
* hsts: support “implied LWS” properly around max-age
* lib: remove function pointer typecasts for hmac/sha256/md5
* mprintf: do not ignore length modifiers of %o, %x, %X
* mprintf: treat %o as unsigned
* multi: make curl\_multi\_cleanup invalidate magic latter
* multi: make multi\_handle\_timeout use the connect timeout
* netrc: cache the netrc file in memory
* select: use poll() if existing, avoid poll() with no sockets
* url: use same credentials on redirect
* urlapi: normalize the IPv6 address

### protocols

* ngtcp2: set max window size to 10x of initial (128KB)
* url: connection reuse on h3 connections
* gnutls: use session cache for QUIC
* mbedTLS: fix handling of TLSv1.3 sessions
* schannel: ignore error on recv beyond close notify
* schannel: reclassify extra-verbose schannel\_recv messages
* quic: use send/recvmmsg when available
* quic: use the session cache with wolfSSL as well

### tests

* generate lib1521.c atomically
* remove all valgrind disable instructions
* remove debug requirement on 38 tests
* use ‘-4’ where needed

## Next

Unless we find a terrible regression, the next curl release is scheduled to ship on January 8, 2025.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postcurl -v google.com](https://daniel.haxx.se/blog/2024/11/05/curl-v-google-com/)[Next PostRock-solid curl](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/)

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

November 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | 1 | 2 | 3 |
| 4 | [5](https://daniel.haxx.se/blog/2024/11/05/) | [6](https://daniel.haxx.se/blog/2024/11/06/) | [7](https://daniel.haxx.se/blog/2024/11/07/) | 8 | 9 | 10 |
| 11 | 12 | [13](https://daniel.haxx.se/blog/2024/11/13/) | [14](https://daniel.haxx.se/blog/2024/11/14/) | 15 | 16 | 17 |
| 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| 25 | 26 | 27 | 28 | 29 | 30 |  |

[« Oct](https://daniel.haxx.se/blog/2024/10/)

[Dec »](https://daniel.haxx.se/blog/2024/12/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)