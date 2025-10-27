---
title: curl for QNX
url: https://daniel.haxx.se/blog/2024/07/05/curl-for-qnx/
source: daniel.haxx.se
date: 2024-07-06
fetch_date: 2025-10-06T17:43:24.456722
---

# curl for QNX

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/07/world-map-curl-2000.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [wolfSSL](https://daniel.haxx.se/blog/category/work/wolfssl/)

# curl for QNX

[July 5, 2024](https://daniel.haxx.se/blog/2024/07/05/curl-for-qnx/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Starting *now*, there are official curl releases for [QNX](https://blackberry.qnx.com/) hosted on the curl.se website. See <https://curl.se/qnx>.

QNX is a commercial real-time operating system and these curl release packages are produced as a result of a business arrangement.

The plan is to from now on ship curl tarballs for three different QNX versions, and each archive contains curl and libcurl built for several different targets. The curl for QNX releases should be possible to release in sync with the regular releases, but they can also be updated out of sync if need be.

Every curl release from here on out will be packaged for QNX and made available.

curl and libcurl have been functional on QNX since decades – the first mention of curl and QNX together that I could find is from October 2000. curl releases for QNX were previously packaged and provided to end users by the QNX team themselves.

This move will allow QNX users to get the latest curl faster and make them able to keep up better with curl development. For features, bugfixes and perhaps most of all security.

We will also make sure that curl keeps building fine for QNX straight from the tarball.

The complete set of build and setup scripts for curl on QNX are maintained in the [curl-for-qnx git repository](https://github.com/curl/curl-for-qnx). Of course we will appreciate submitted issues and pull requests in that repository as well.

This commercial agreement is between Blackberry and wolfSSL. I am employed by wolfSSL. If you want *your* operating system to have equally fancy and always up-to-date releases, you know who to contact.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[WolfSSL](https://daniel.haxx.se/blog/tag/wolfssl/)

# Post navigation

[Previous Postwcurl is here](https://daniel.haxx.se/blog/2024/07/03/wcurl-is-here/)[Next Postcurl 8.9.0](https://daniel.haxx.se/blog/2024/07/24/curl-8-9-0/)

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

July 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | [3](https://daniel.haxx.se/blog/2024/07/03/) | 4 | [5](https://daniel.haxx.se/blog/2024/07/05/) | 6 | 7 |
| 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| 22 | 23 | [24](https://daniel.haxx.se/blog/2024/07/24/) | 25 | 26 | 27 | 28 |
| 29 | 30 | [31](https://daniel.haxx.se/blog/2024/07/31/) |  | | | |

[« Jun](https://daniel.haxx.se/blog/2024/06/)

[Aug »](https://daniel.haxx.se/blog/2024/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)