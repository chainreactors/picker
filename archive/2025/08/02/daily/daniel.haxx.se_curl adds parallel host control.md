---
title: curl adds parallel host control
url: https://daniel.haxx.se/blog/2025/08/01/curl-adds-parallel-host-control/
source: daniel.haxx.se
date: 2025-08-02
fetch_date: 2025-10-07T00:50:19.515447
---

# curl adds parallel host control

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/12/command-line-option-of-the-week.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl adds parallel host control

[August 1, 2025](https://daniel.haxx.se/blog/2025/08/01/curl-adds-parallel-host-control/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

I’m convinced a lot of people have not yet figured out that curl has supported parallel downloads for six years already by now.

Provided a practically unlimited number of URLs, curl can be asked to get them in a parallel fashion. It then makes sure to keep N transfers alive for as long as there is N or more transfers left to complete, where X is a custom number but 50 by default.

Concurrently transferring data from potentially a large number of different hosts can drastically shorten transfer times and who doesn’t prefer to complete their download job sooner rather than later?

## Limit connections per host

At times however, you may want to do a lot of transfers, and you want to do them in parallel for speed, but maybe you prefer to limit how many connections curl should use per each hostname among all the URLs?

This per-host limit is a feature libcurl has offered applications for a long time and now the time has come for curl tool users to also enjoy its powers.

Per host should perhaps be called *per origin* if we spoke web lingo, because it rather limits the number of connections to the same protocol + hostname + port number. We call that *host* here for simplicity.

To set a cap on how many connections curl is allowed to use for each specific server use `--parallel-max-host [number]`.

For example, if you want to download ten million images from this site, but never use more than six connections:

```
curl --parallel --parallel-max-host 6 https://example.com/[1-10000000].jpg --remote-name
```

## Connections

Pay special attention to the exact term: this limits the number of *connections* used to each host. If the transfers are done using HTTP/2 or HTTP/3, they can be done using many streams over just one or a few connections so doing 50 or 200 transfers in parallel should still be perfectly doable even with a limited number of connections. Not so much with HTTP/1.

## Ships in 8.16.0

This command line option will become available in the pending curl version 8.16.0 release.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postoption parsing in curl](https://daniel.haxx.se/blog/2025/07/31/option-parsing-in-curl/)[Next PostEven happier eyeballs](https://daniel.haxx.se/blog/2025/08/04/even-happier-eyeballs/)

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