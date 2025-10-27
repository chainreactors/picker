---
title: curl 8.12.1
url: https://daniel.haxx.se/blog/2025/02/13/curl-8-12-1/
source: daniel.haxx.se
date: 2025-02-14
fetch_date: 2025-10-06T20:35:56.188420
---

# curl 8.12.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/curl-8.12.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.12.1

[February 13, 2025](https://daniel.haxx.se/blog/2025/02/13/curl-8-12-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

This is a quick follow-up patch release due to the number of ugly regressions in the [8.12.0 release](https://daniel.haxx.se/blog/2025/02/05/curl-8-12-0/).

## Release presentation

## Numbers

**the 265th release
0 changes
8 days (total: 9,827)**
**65 bugfixes (total: 11,428)**
**67 commits (total: 34,180)
0 new public libcurl function (total: 96)
0 new curl\_easy\_setopt() option (total: 306)**
**0 new curl command line option (total: 267)**
**25 contributors, 14 new (total: 3,332)**
**34 authors, 18 new (total: 1,341)**
**0 security fixes (total: 164)**

## Bugfixes

### libcurl

* asyn-thread: fix build with `CURL_DISABLE_SOCKETPAIR`
* asyn-thread: fix the returned bitmask from Curl\_resolver\_getsock
* asyn-thread: survive a c-ares/HTTPSRR channel set to NULL
* content\_encoding: #error on too old zlib
* imap/pop3/smtp: TLS upgrade fixes
* include necessary headers for `inet_ntop`/`inet_pton`
* drop support for libssh older than 0.9.0
* netrc: return code cleanup, fix missing file error
* openssl-quic: ignore ciphers for h3
* openssl: fix out of scope variables in goto
* vtls: fix multissl-init
* vtsl: eliminate ‘data->state.ssl\_scache’
* wakeup\_write: make sure the eventfd write sends eight bytes

### tool

* tool\_ssls: switch to tool-specific get\_line function

### scripts

* build: add tool\_hugehelp.c into IBMi build
* configure/cmake: check for realpath
* configure/cmake: set asyn-rr a feature only if httpsrr is enabled
* runtests: fix the disabling of the memory tracking
* runtests: quote commands to support paths with spaces

### docs

* CURLOPT\_SSH\_KNOWNHOSTS.md: strongly recommend using this
* CURLSHOPT\_SHARE.md: adjust for the new SSL session cache
* SPONSORS.md: clarify that we don’t promise goods or services

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postdisabling cert checks: we have not learned much](https://daniel.haxx.se/blog/2025/02/11/disabling-cert-checks-we-have-not-learned-much/)[Next PostOpenSSL does a QUIC API](https://daniel.haxx.se/blog/2025/02/16/openssl-does-a-quic-api/)

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

February 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| [3](https://daniel.haxx.se/blog/2025/02/03/) | 4 | [5](https://daniel.haxx.se/blog/2025/02/05/) | 6 | 7 | 8 | 9 |
| 10 | [11](https://daniel.haxx.se/blog/2025/02/11/) | 12 | [13](https://daniel.haxx.se/blog/2025/02/13/) | 14 | 15 | [16](https://daniel.haxx.se/blog/2025/02/16/) |
| 17 | [18](https://daniel.haxx.se/blog/2025/02/18/) | 19 | 20 | 21 | [22](https://daniel.haxx.se/blog/2025/02/22/) | 23 |
| [24](https://daniel.haxx.se/blog/2025/02/24/) | [25](https://daniel.haxx.se/blog/2025/02/25/) | 26 | 27 | [28](https://daniel.haxx.se/blog/2025/02/28/) |  | |

[« Jan](https://daniel.haxx.se/blog/2025/01/)

[Mar »](https://daniel.haxx.se/blog/2025/03/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)