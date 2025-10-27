---
title: Dropping old OpenSSL
url: https://daniel.haxx.se/blog/2025/08/28/dropping-old-openssl/
source: daniel.haxx.se
date: 2025-08-29
fetch_date: 2025-10-07T00:48:03.977187
---

# Dropping old OpenSSL

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/06/trimming-hedge.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Dropping old OpenSSL

[August 28, 2025](https://daniel.haxx.se/blog/2025/08/28/dropping-old-openssl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

curl added support for OpenSSL immediately when it was first released, as they switched away from SSLeay, in the late 1990s.

We have since supported it over the decades as both OpenSSL and curl have developed.

A while back the OpenSSL project stopped updating their 1.0.x and 1.1.x public branches. This means that unless you are paying for support from someone, and only relies on the public open versions these OpenSSL releases are going to decay and soon be insecure choices. Nothing to rely on.

As a direct result of this, the curl project has decided to drop support for OpenSSL 1.0.2 and 1.1.1 soon.

We stop supporting OpenSSL 1.0.2 in **December 2025**.

We stop supporting OpenSSL 1.1.1 in **June 2026**.

Starting in June 2026, we plan to only support OpenSSL 3 and later. Of course with the caveat that we might change our minds or schedule as we go along and things happen.

All pending removals from curl are [listed here](https://curl.se/dev/deprecate.html).

## Contract support remains

Part of the reason for us dropping this support is the fact that basically only users who are already paying for OpenSSL support are the ones who are going to be using these versions.

We will offer [commercial support](https://curl.se/support.html) for curl with OpenSSL 1.1.1 for as long as customers want it, even when support gets removed from the public curl version.

## The forks remain

This news is for OpenSSL support only and does not affect the forks. We intend to keep supporting the whole fork family AmiSSL, AWS-LC, BoringSSL, LibreSSL and QuicTLS going forward as well.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[OpenSSL](https://daniel.haxx.se/blog/tag/openssl/)

# Post navigation

[Previous PostAI slop attacks on the curl project](https://daniel.haxx.se/blog/2025/08/18/ai-slop-attacks-on-the-curl-project/)[Next Postgiants, standing on the shoulders of](https://daniel.haxx.se/blog/2025/09/08/giants-standing-on-the-shoulders-of/)

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

August 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | [1](https://daniel.haxx.se/blog/2025/08/01/) | 2 | 3 |
| [4](https://daniel.haxx.se/blog/2025/08/04/) | [5](https://daniel.haxx.se/blog/2025/08/05/) | [6](https://daniel.haxx.se/blog/2025/08/06/) | [7](https://daniel.haxx.se/blog/2025/08/07/) | [8](https://daniel.haxx.se/blog/2025/08/08/) | 9 | 10 |
| 11 | 12 | 13 | 14 | [15](https://daniel.haxx.se/blog/2025/08/15/) | 16 | 17 |
| [18](https://daniel.haxx.se/blog/2025/08/18/) | 19 | 20 | 21 | 22 | 23 | 24 |
| 25 | 26 | 27 | [28](https://daniel.haxx.se/blog/2025/08/28/) | 29 | 30 | 31 |

[« Jul](https://daniel.haxx.se/blog/2025/07/)

[Sep »](https://daniel.haxx.se/blog/2025/09/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)