---
title: skip a curl transfer
url: https://daniel.haxx.se/blog/2024/08/17/skip-a-curl-transfer/
source: daniel.haxx.se
date: 2024-08-18
fetch_date: 2025-10-06T18:03:21.251886
---

# skip a curl transfer

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/08/skip-a-bit-holy-grail.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# skip a curl transfer

[August 17, 2024](https://daniel.haxx.se/blog/2024/08/17/skip-a-curl-transfer/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

This is episode three in my mini-series of posts describing news in the coming [curl](https://curl.se/) 8.10.0 release. Part one was [more help](https://daniel.haxx.se/blog/2024/08/09/more-curl-help/), part two [verbose, verbose and verbosest](https://daniel.haxx.se/blog/2024/08/12/verbose-verboser-verbosest/).

This new command line option in curl 8.10.0 is a simple one that has been requested by users repeatedly over the years so I figure it was about time we actually provide it.

*If the target file already exists on disk, skip downloading it.*

It is exactly as simple as that. No date check, no size check, no checking if the file is even what you want it to be. If the target file is present and exists that is a signal enough that the file should not be downloaded; to skip the transfer.

A real-world command line using this feature could then look like this:

```
curl --skip-existing --output local/dir/file https://example.com
```

Or if instead -O is used, it still works the same:

```
curl --skip-existing -O https://example.com/me.jpg
```

Easy, right? See the [manpage](https://curl.se/docs/manpage.html#--skip-existing).

## Broken files can also be present

To avoid a previous broken download remainder to linger around and cause future transfers to get skipped, remember that curl also has a [–remove-on-errror](https://daniel.haxx.se/blog/2022/03/11/remove-leftovers-on-curl-error/) option.

## Ships

In curl 8.10.0, on September 11, 2024.

## Image

From a movie with a suitable if even perhaps subtle reference.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostSo the Department of Energy emailed me](https://daniel.haxx.se/blog/2024/08/14/so-the-department-of-energy-emailed-me/)[Next Posta filename when none exists](https://daniel.haxx.se/blog/2024/08/19/a-filename-when-none-exists/)

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

August 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2024/08/06/) | 7 | [8](https://daniel.haxx.se/blog/2024/08/08/) | [9](https://daniel.haxx.se/blog/2024/08/09/) | 10 | 11 |
| [12](https://daniel.haxx.se/blog/2024/08/12/) | 13 | [14](https://daniel.haxx.se/blog/2024/08/14/) | 15 | 16 | [17](https://daniel.haxx.se/blog/2024/08/17/) | 18 |
| [19](https://daniel.haxx.se/blog/2024/08/19/) | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Jul](https://daniel.haxx.se/blog/2024/07/)

[Sep »](https://daniel.haxx.se/blog/2024/09/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)