---
title: curl 8.2.1
url: https://daniel.haxx.se/blog/2023/07/26/curl-8-2-1/
source: daniel.haxx.se
date: 2023-07-27
fetch_date: 2025-10-04T11:54:51.179833
---

# curl 8.2.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/07/curl-8.2.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.2.1

[July 26, 2023](https://daniel.haxx.se/blog/2023/07/26/curl-8-2-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Welcome. Due to some annoying regressions in the previous release we think we owned it to everyone to do a quick patch follow-up.

Download curl 8.2.1 from <https://curl.se>.

## Release presentation

## Numbers

**the 221st release
0 changes
7 days (total: 9,259)**
**27 bug-fixes (total: 9,194)**
**37 commits (total: 30,646)
0 new public libcurl function (total: 91)
0 new curl\_easy\_setopt() option (total: 303)**
**0 new curl command line option (total: 255)**
**20 contributors, 7 new (total: 2,927)**
**13 authors, 3 new (total: 1,173)**
**0 security fixes (total: 146)**

## Bugfixes

Here are some the most important fixes in this release

### configure: check for nghttp2\_session\_get\_stream\_local\_window\_size

We use this function now, introduced in nghttp2 1.15.0, released in September 2016.

### return IPv6 first for localhost resolves

Resolving “localhost” did not return the (fixed) addresses in the correct order. It now returns IPv6 as the first.

### http2 regression on upload EOF handling

When we added an optimization in the previous release we missed a code path that sometimes lead to “hanging” uploads over HTTP/2.

### os400: correct EXPECTED\_STRING\_LASTZEROTERMINATED

curl builds fine for “IBM i” again.

### quiche: fix lookup of transfer at multi

Doing multiplexed HTTP/3 over multiple connections with quiche works much better.

### mkhelp: strip off escape sequences

The command sequence that generates the man page display code for the `--manual` option did at some point regress to include escape sequences. Now those sequences are properly filtered out.

### fix build when SIZEOF\_CURL\_OFF\_T > SIZEOF\_OFF\_T

A build problem was fixed for these rare platforms.

### do not clear the credentials on redirect to absolute URL

Yet another regression that we allowed because we apparently did not have a test for this! Now we have a test and redirects to the same origin when using -u for credentials now send the credentials even in the redirected request.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postcurl 8.2.0](https://daniel.haxx.se/blog/2023/07/19/curl-8-2-0/)[Next Postintroducing curl command line variables](https://daniel.haxx.se/blog/2023/07/31/introducing-curl-command-line-variables/)

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

July 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 17 | 18 | [19](https://daniel.haxx.se/blog/2023/07/19/) | 20 | 21 | 22 | 23 |
| 24 | 25 | [26](https://daniel.haxx.se/blog/2023/07/26/) | 27 | 28 | 29 | 30 |
| [31](https://daniel.haxx.se/blog/2023/07/31/) |  | | | | | |

[« Jun](https://daniel.haxx.se/blog/2023/06/)

[Aug »](https://daniel.haxx.se/blog/2023/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)