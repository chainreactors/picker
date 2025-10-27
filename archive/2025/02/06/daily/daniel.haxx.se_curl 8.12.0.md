---
title: curl 8.12.0
url: https://daniel.haxx.se/blog/2025/02/05/curl-8-12-0/
source: daniel.haxx.se
date: 2025-02-06
fetch_date: 2025-10-06T20:35:34.587153
---

# curl 8.12.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/curl-8.12.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.12.0

[February 5, 2025](https://daniel.haxx.se/blog/2025/02/05/curl-8-12-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

## Release presentation

## Numbers

**the 264th release
8 changes
56 days (total: 9,819)**
**244 bugfixes (total: 11,417)**
**367 commits (total: 34,180)
2 new public libcurl function (total: 96)
0 new curl\_easy\_setopt() option (total: 306)**
**1 new curl command line option (total: 267)**
**65 contributors, 34 new (total: 3,332)**
**34 authors, 18 new (total: 1,341)**
**3 security fixes (total: 164)**

## Security

[CVE-2025-0167: netrc and default credential leak](https://curl.se/docs/CVE-2025-0167.html). When asked to use a `.netrc` file for credentials **and** to follow HTTP redirects, curl could leak the password used for the first host to the followed-to host under certain circumstances. This flaw only manifests itself if the netrc file has a `default` entry that omits both login and password. A rare circumstance.

[CVE-2025-0665: eventfd double close](https://curl.se/docs/CVE-2025-0665.html). libcurl would wrongly close the same file descriptor twice when taking down a connection channel after having completed a threaded name resolve.

[CVE-2025-0725: gzip integer overflow](https://curl.se/docs/CVE-2025-0725.html). When libcurl is asked to perform automatic gzip decompression of content-encoded HTTP responses with the `CURLOPT_ACCEPT_ENCODING` option, **using zlib 1.2.0.3 or older**, an attacker-controlled integer overflow would make libcurl perform a buffer overflow. *There should be virtually no users left using such an old and vulnerable zlib version.*

## Changes

* curl: [add byte range support](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/) to –variable reading from file
* curl: make –etag-save acknowledge –create-dirs
* curl: add ‘time\_queue’ variable to -w
* getinfo: provide info which auth was used for HTTP and proxy:
* openssl: add support to use keys and certificates from PKCS#11 provider
* QUIC: 0RTT for gnutls via CURLSSLOPT\_EARLYDATA
* vtls: feature ssls-export for SSL session im-/export
* [hyper: dropped support](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/)

## Bugfixes

Some of the bugfixes to highlight.

### libcurl

* acknowledge CURLOPT\_DNS\_SERVERS set to NULL
* fix CURLOPT\_CURLU override logic
* initial HTTPS RR resolve support
* ban use of sscanf()
* conncache: count shutdowns against host and max limits
* support use of custom libzstd memory functions
* cap cookie expire times to 400 days
* parse only the exact cookie expire date
* include the shutdown connections in the set curl\_multi\_fdset returns
* easy\_lock: use Sleep(1) for thread yield on old Windows
* ECH: update APIs to those agreed with OpenSSL maintainers
* fix ‘time\_appconnect’ for early data with GnuTLS
* HTTP/2 and HTTP7/3: strip TE request header
* mbedtls: fix handling of blocked sends
* mime: explicitly rewind subparts at attachment time.
* fix mprintf integer handling in float precision
* terminate snprintf output on windows
* fix curl\_multi\_waitfds reporting of fd\_count
* fix return code for an already-removed easy handle from multi handle
* add an ssl\_scache to the multi handle
* auto-enable `OPENSSL_COEXIST` for wolfSSL + OpenSSL builds
* use SSL\_poll to determine writeability of OpenSSL QUIC streams
* free certificate on error with Secure Transport
* fix redirect handling to a new fragment or query (only)
* return “IDN” feature set for winidn and appleidn

### scripts

* numerous cmake improvements
* scripts/mdlinkcheck: markdown link checker

### curl tool

* return error if etag options are used with multiple URLs
* accept digits in –form type= strings
* make –etag-compare accept a non-existing file

### docs

* add INFRASTRUCTURE.md describing project infra

## Next

The next release is *probably* going to be curl 8.13.0 and if things go well, it ships on April 2, 2025.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostEuropean Open Source Achievement Award](https://daniel.haxx.se/blog/2025/02/03/european-open-source-achievement-award/)[Next Postdisabling cert checks: we have not learned much](https://daniel.haxx.se/blog/2025/02/11/disabling-cert-checks-we-have-not-learned-much/)

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

[« Jan](https://dan...