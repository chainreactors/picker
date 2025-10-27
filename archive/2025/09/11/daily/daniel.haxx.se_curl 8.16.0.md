---
title: curl 8.16.0
url: https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/
source: daniel.haxx.se
date: 2025-09-11
fetch_date: 2025-10-02T19:58:16.743063
---

# curl 8.16.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/09/curl-8.16.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.16.0

[September 10, 2025](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/#respond)

Welcome to one of the more feature-packed curl releases we have had in a while. Exactly eight weeks since we shipped [8.15.0](https://daniel.haxx.se/blog/2025/07/16/curl-8-15-0/).

## Release presentation

## Numbers

the 270th release
17 changes
56 days (total: 10,036)
260 bugfixes (total: 12,538)
453 commits (total: 36,025)
2 new public libcurl function (total: 98)
0 new curl\_easy\_setopt() option (total: 308)
3 new curl command line option (total: 272)
76 contributors, 39 new (total: 3,499)
32 authors, 17 new (total: 1,410)
2 security fixes (total: 169)

## Security

We publish two severity-low vulnerabilities in sync with this release:

* [CVE-2025-9086](https://curl.se/docs/CVE-2025-9086.html) identifies a bug in the cookie path handler that can make curl get confused and override a secure cookie with a non-secure one using the same name. If the planets all happen to align correctly.
* [CVE-2025-10148](https://curl.se/docs/CVE-2025-10148.html) points out a mistake in the WebSocket implementation that makes curl *not* update the frame mask correctly for each new outgoing frame – as it is supposed to.

## Changes

We have a long range of changes this time:

* curl gets a [`--follow` option](https://daniel.haxx.se/blog/2025/08/06/follow-redirects-but-differently/)
* curl gets an [`--out-null` option](https://daniel.haxx.se/blog/2025/07/30/output-nothing-with-out-null/)
* curl gets a `--parallel-max-host` option to limit concurrent connections per host
* `--retry-delay` and `--retry-max-time` accept decimal seconds
* curl gets support for `[--longopt=value](https://daniel.haxx.se/blog/2025/07/31/option-parsing-in-curl/)`
* curl [-w now supports %time{}](https://daniel.haxx.se/blog/2025/08/07/curl-tells-the-time/)
* now libcurl caches *negative* name resolves
* ip happy eyeballing: [keep attempts running](https://daniel.haxx.se/blog/2025/08/04/even-happier-eyeballs/)
* bump minimum mbedtls version required to 3.2.0
* add [curl\_multi\_get\_offt](https://curl.se/libcurl/c/curl_multi_get_offt.html)() for getting multi related information
* add [CURLMOPT\_NETWORK\_CHANGED](https://curl.se/libcurl/c/CURLMOPT_NETWORK_CHANGED.html) to signal network changed to libcurl
* use the `NETRC` environment variable (first) if set
* bump minimum required mingw-w64 to v3.0 (from v1.0)
* smtp: allow suffix behind a mail address for RFC 3461
* make default TLS version be minimum 1.2
* [drop support for msh3](https://daniel.haxx.se/blog/2025/07/29/carving-out-msh3/)
* support CURLOPT\_READFUNCTION for WebSocket

## Bugfixes

The official bugfix count surpassed 250 this cycle and we have documented them all in [the changelog](https://curl.se/ch/), including links to most issues or pull-requests where they originated.

See the release presentation for a walk-through of some of the perhaps most interesting ones.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postpreparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/)[Next PostDeveloper of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)

### Leave a Reply [Cancel reply](/blog/2025/09/10/curl-8-16-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
4fiveninethree1

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

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

September 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| [8](https://daniel.haxx.se/blog/2025/09/08/) | [9](https://daniel.haxx.se/blog/2025/09/09/) | [10](https://daniel.haxx.se/blog/2025/09/10/) | 11 | 12 | [13](https://daniel.haxx.se/blog/2025/09/13/) | 14 |
| 15 | 16 | 17 | [18](https://daniel.haxx.se/blog/2025/09/18/) | [19](https://daniel.haxx.se/blog/2025/09/19/) | 20 | 21 |
| [22](https://daniel.haxx.se/blog/2025/09/22/) | 23 | 24 | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« Aug](https://daniel.haxx.se/blog/2025/08/)

[Oct »](https://daniel.haxx.se/blog/2025/10/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)