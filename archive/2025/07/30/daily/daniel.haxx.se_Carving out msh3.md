---
title: Carving out msh3
url: https://daniel.haxx.se/blog/2025/07/29/carving-out-msh3/
source: daniel.haxx.se
date: 2025-07-30
fetch_date: 2025-10-06T23:39:51.043715
---

# Carving out msh3

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/http3-sticker.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Carving out msh3

[July 29, 2025](https://daniel.haxx.se/blog/2025/07/29/carving-out-msh3/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

I hope that by now most readers of my blog have understood that curl, and libcurl specifically, is an architecture with a transfer core with a set of different *backends* plugged in. Backends powered by different third party libraries.

The exact set of backends used in a particular build is decided by the person that builds curl.

What backends that curl supports varies over time (and platform). We appreciate adding support for more backends and to let users decide which ones to use, as this allows us to approach it with a *survival of the fittest* attitude. What does not work in the long run or what isn’t actually used, we can deprecate and remove again. Ideally this helps us select the better ones for the future.

## HTTP/3

For the last few years curl has supported the HTTP/3 protocol powered by one out of **four** different backends:

1. nghttp3 + ngtcp2
2. quiche
3. nghttp3 + OpenSSL-QUIC
4. **msh3 + msquic**

(All except the first listed combination, we still label *experimental*.)

## Dropping msh3

In this quartet, there is one option that stands out a little: the last one. The msh3 powered backend was brought in and merged into the curl source tree a few years ago with the hope that this solution would end up a good choice for people on Windows since it is the only choice in the list that can get built to use the native Windows TLS solution *SChannel*.

Unfortunately, this work was never finalized. It never worked correctly in curl and the API and architecture of msh3 makes it quirky and cumbersome to integrate – and quite frankly we can’t seem to drum up any interest for people to test nor work on improving this backend.

As we have three other working backends, all of which also can build and run on Windows, we see no benefit in dragging msh3 along. In fact, there is a cost in maintenance and keeping the build working and the tests running etc that we rather avoid. In particular as we seem to be doing that for virtually no gain.

I want to stress that I don’t think there is anything wrong with msh3 nor its underlying msquic library. They simply have not been made to work properly in curl.

## Updated backend map

The msh3 backend has now been removed from git in the current master branch and this is how the HTTP/3 offer will look like in the coming curl 8.16.0 release.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/06/curl-HTTP_3-backends8.jpg)

HTTP/3 backends in the pending curl 8.16.0

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP/3](https://daniel.haxx.se/blog/tag/http3/)[QUIC](https://daniel.haxx.se/blog/tag/quic/)[windows](https://daniel.haxx.se/blog/tag/windows/)

# Post navigation

[Previous PostHello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/)[Next PostOutput nothing with –out-null](https://daniel.haxx.se/blog/2025/07/30/output-nothing-with-out-null/)

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

July 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | [3](https://daniel.haxx.se/blog/2025/07/03/) | 4 | 5 | 6 |
| 7 | [8](https://daniel.haxx.se/blog/2025/07/08/) | 9 | [10](https://daniel.haxx.se/blog/2025/07/10/) | [11](https://daniel.haxx.se/blog/2025/07/11/) | [12](https://daniel.haxx.se/blog/2025/07/12/) | [13](https://daniel.haxx.se/blog/2025/07/13/) |
| [14](https://daniel.haxx.se/blog/2025/07/14/) | 15 | [16](https://daniel.haxx.se/blog/2025/07/16/) | 17 | 18 | 19 | 20 |
| 21 | 22 | [23](https://daniel.haxx.se/blog/2025/07/23/) | 24 | 25 | 26 | 27 |
| [28](https://daniel.haxx.se/blog/2025/07/28/) | [29](https://daniel.haxx.se/blog/2025/07/29/) | [30](https://daniel.haxx.se/blog/2025/07/30/) | [31](https://daniel.haxx.se/blog/2025/07/31/) |  | | |

[« Jun](https://daniel.haxx.se/blog/2025/06/)

[Aug »](https://daniel.haxx.se/blog/2025/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()