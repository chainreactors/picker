---
title: 7.88.1 the second final one
url: https://daniel.haxx.se/blog/2023/02/20/7-88-1-the-second-final-one/
source: daniel.haxx.se
date: 2023-02-21
fetch_date: 2025-10-04T07:37:36.482913
---

# 7.88.1 the second final one

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/curl-7.88.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# 7.88.1 the second final one

[February 20, 2023](https://daniel.haxx.se/blog/2023/02/20/7-88-1-the-second-final-one/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Things did not work out the way we had planned. The [7.88.0 release](https://daniel.haxx.se/blog/2023/02/15/curl-7-88-0-seven-stops-here/) that was supposed to be the last curl version 7 release contained a nasty bug that made us decide that we better ship an update once that is fixed. This is the update. *The second final version 7 release*.

## Release presentation

## Numbers

**the 214th release
0 changes
5 days (total: 9,103)**
2**5 bug-fixes (total: 8,690)**
**32 commits (total: 29,853)
0 new public libcurl function (total: 91)
0 new curl\_easy\_setopt() option (total: 302)**
**0 new curl command line option (total: 250)**
**19 contributors, 7 new (total: 2,819)**
**10 authors, 1 new (total: 1,120)**
**0 security fixes (total: 135)**

## Bugfixes

As this is a rushed patch-release, there is only a small set of bugfixes merged in this cycle. The following notable bugs were fixed.

### http2 multiplexed data corruption

The main bug that triggered the patch release. In some circumstances , when data was delivered as a HTTP/2 multiplexed stream, curl would get it wrong and cause the saved data to be corrupt. It would get the wrong data from the internal buffer.

This was not a new bug, but recent changes made it more likely to trigger.

### make connect timeouts use full duration

In some cases curl would only allow half the given timeout period when doing connects.

### runtests: fix “uninitialized value $port”

Running the test suite with verbose mode enabled, it would error out with this message. Since a short while back, we consider warnings in the test script fatal so this then aborts all the tests.

### tests: make sure gnuserv-tls has SRP support before using it

The test suite uses gnuserv-tls to verify SRP authentication. It will only use this tool if found at startup, but due to recent changes in the GnuTLS project that ships this tool, it now builds with SRP disabled by default and thus can’t be used for this test. Now, the test script also checks that it actually supports SRP before trying to use it.

### setopt: allow HTTP3 when HTTP2 is not defined

A regression made it impossible to ask for HTTP/3 if the build did not also support HTTP/2.

### socketpair: allow EWOULDBLOCK when reading the pair check bytes

The fix in 7.88.0 turned out to cause occasional hiccups (on Windows at least) and this is a follow-up improvement for the verification of the socketpair emulation. When we create the pair and verify that it works, we must make sure that the code handles EWOULDBLOCK correctly.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postcurl 7.88.0 seven stops here](https://daniel.haxx.se/blog/2023/02/15/curl-7-88-0-seven-stops-here/)[Next PostMy 2023 dev machine](https://daniel.haxx.se/blog/2023/02/20/my-2023-dev-machine/)

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

February 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | [1](https://daniel.haxx.se/blog/2023/02/01/) | 2 | 3 | 4 | 5 |
| [6](https://daniel.haxx.se/blog/2023/02/06/) | [7](https://daniel.haxx.se/blog/2023/02/07/) | 8 | 9 | 10 | 11 | 12 |
| 13 | 14 | [15](https://daniel.haxx.se/blog/2023/02/15/) | 16 | 17 | 18 | 19 |
| [20](https://daniel.haxx.se/blog/2023/02/20/) | 21 | 22 | [23](https://daniel.haxx.se/blog/2023/02/23/) | 24 | 25 | 26 |
| 27 | 28 |  | | | | |

[« Jan](https://daniel.haxx.se/blog/2023/01/)

[Mar »](https://daniel.haxx.se/blog/2023/03/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)