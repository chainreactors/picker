---
title: Rewriting curl in three days
url: https://daniel.haxx.se/blog/2022/10/14/rewriting-curl-in-three-days/
source: daniel.haxx.se
date: 2022-10-15
fetch_date: 2025-10-03T19:56:53.674712
---

# Rewriting curl in three days

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Rewriting curl in three days

[October 14, 2022](https://daniel.haxx.se/blog/2022/10/14/rewriting-curl-in-three-days/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

To celebrate the [hubris-infested comment](https://daniel.haxx.se/blog/2021/05/20/i-could-rewrite-curl/) from a few years ago, I created this book cover mock up.

Turned out very [popular on Twitter](https://twitter.com/bagder/status/1580488641096261632).

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/orly-rewriting-curl.png)](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/orly-rewriting-curl.png)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostThere is a tab in my cookie](https://daniel.haxx.se/blog/2022/10/14/there-is-a-tab-in-my-cookie/)[Next PostDeviating from specs](https://daniel.haxx.se/blog/2022/10/18/deviating-from-specs/)

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

October 2022

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | [14](https://daniel.haxx.se/blog/2022/10/14/) | 15 | 16 |
| 17 | [18](https://daniel.haxx.se/blog/2022/10/18/) | [19](https://daniel.haxx.se/blog/2022/10/19/) | 20 | 21 | 22 | 23 |
| 24 | 25 | [26](https://daniel.haxx.se/blog/2022/10/26/) | 27 | 28 | 29 | 30 |
| 31 |  | | | | | |

[« Sep](https://daniel.haxx.se/blog/2022/09/)

[Nov »](https://daniel.haxx.se/blog/2022/11/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)