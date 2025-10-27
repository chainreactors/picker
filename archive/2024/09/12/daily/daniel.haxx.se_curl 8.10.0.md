---
title: curl 8.10.0
url: https://daniel.haxx.se/blog/2024/09/11/curl-8-10-0/
source: daniel.haxx.se
date: 2024-09-12
fetch_date: 2025-10-06T18:28:22.859967
---

# curl 8.10.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/curl-8.10.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.10.0

[September 11, 2024](https://daniel.haxx.se/blog/2024/09/11/curl-8-10-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

## Numbers

**the 260th release
18 changes
42 days (total: 9,672)**
**245 bugfixes (total: 10,804)**
**461 commits (total: 33,209)
0 new public libcurl function (total: 94)
0 new curl\_easy\_setopt() option (total: 306)**
**2 new curl command line option (total: 265)**
**57 contributors, 28 new (total: 3,239)**
**27 authors, 14 new (total: 1,302)**
**1 security fixes (total: 158)**

Download the new curl release from [curl.se](https://curl.se/) as always.

## Release presentation

## Security

[CVE-2024-8096: OCSP stapling bypass with GnuTLS](https://curl.se/docs/CVE-2024-8096.html) When curl is told to use the Certificate Status Request TLS extension, often referred to as OCSP stapling, to verify that the server certificate is valid, it might fail to detect some OCSP problems and instead wrongly consider the response as fine.

## Changes

* [–help [option]](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/)
* [–skip-existing](https://daniel.haxx.se/blog/2024/08/17/skip-a-curl-transfer/)
* with -O, [try harder to get a filename](https://daniel.haxx.se/blog/2024/08/19/a-filename-when-none-exists/)
* make –rate accept number of units. Previously it accepted N requests per single time unit, now it supports N requests per Z time units.
* make –show-headers the same as –include. To make the option name better spell out what it is for.
* –dump-header supports % to direct to stderr. To match a few of the other options that already support this.
* supports embedding a CA bundle and –dump-ca-embed. As this allows the curl tool to get built stand-alone without relying on an external CA store.
* [supports repeated use of the verbose option; -vv etc](https://daniel.haxx.se/blog/2024/08/12/verbose-verboser-verbosest/).
* libuv for parallel transfers with –test-event. To allow better and easier testing of curl’s event-based API. Available in debug-builds only.
* add [CURLINFO\_POSTTRANSFER\_TIME\_T](https://curl.se/libcurl/c/CURLINFO_POSTTRANSFER_TIME_T.html)
* add –enable-windows-unicode configure option
* [CURLOPT\_TLS13\_CIPHERS](https://curl.se/libcurl/c/CURLOPT_TLS13_CIPHERS.html) for mbedTLS and wolfSSL
* support for setting TLS version and ciphers for Rustls
* stop offering ALPN http/1.1 for http2-prior-knowledge
* support for sslcert/sslkey blob options for wolfSSL
* release tarball 100% reproducible. We also provide *verify-release* a convenient shell script allowing anyone and everyone to easily verify curl release tarballs.

## Bugfixes

See the [full changelog](https://curl.se/changes.html) for the complete list. Here follows my favorite subset:

* build: add `poll()` detection for cross-builds
* cmake: 40+ bugfixes
* configure: fail if PSL is not disabled but not found
* runtests: remove “has\_textaware”
* curl: find curlrc in XDG\_CONFIG\_HOME without leading dot
* curl: make the progress bar detect terminal width changes
* curl: bump maximum post data size in memory to 16GB
* bearssl/mbedtls/rustls/wolfssl: fix setting tls version
* gnutls/wolfssl: improve error message when certificate fails
* gnutls: send all data
* openssl: certinfo errors now fail correctly
* sectransp: fix setting tls version
* x509asn1: raise size limit for x509 certification information
* ftp: always offer line end conversions
* ftp: fix pollset for listening
* http2: improved upload eos handling
* idn: support non-UTF-8 input under AppleIDN
* ngtcp2: use NGHTTP3 prefix instead of NGTCP2 for errors in h3 callbacks
* pop3: fix multi-line responses
* managen: fix superfluous leading blank line in quoted sections. Nicer HTML version of the manpages.
* managen: in man output, remove the leading space from examples
* managen: wordwrap long example lines in ASCII output. Nicer curl `--manual` and `-h` output.
* manpage: ensure a maximum width for the text version.
* connect: always prefer ipv6 in IP eyeballing
* aws\_sigv4: fix canon order for headers with same prefix
* cf-socket: prevent KEEPALIVE\_FACTOR being set to 1000 for Windows
* rand: only provide weak random when needed
* sigpipe: init the struct so that first apply ignores
* url: fix connection reuse for HTTP/2 upgrades
* urlapi: verify URL *decoded* hostname when set
* asyn-thread: stop using GetAddrInfoExW on Windows

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postwebinar: mastering the curl command line](https://daniel.haxx.se/blog/2024/09/02/webinar-mastering-the-curl-command-line/)[Next Posttrurl 0.15.1](https://daniel.haxx.se/blog/2024/09/12/trurl-0-15-1/)

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
| 16 | 17 |...