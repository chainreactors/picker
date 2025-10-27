---
title: trurl 0.15.1
url: https://daniel.haxx.se/blog/2024/09/12/trurl-0-15-1/
source: daniel.haxx.se
date: 2024-09-13
fetch_date: 2025-10-06T18:27:28.087551
---

# trurl 0.15.1

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/trurl-0.15.1.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# trurl 0.15.1

[September 12, 2024](https://daniel.haxx.se/blog/2024/09/12/trurl-0-15-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

[trurl](https://curl.se/trurl/) is slowing growing up and maturing. This is a minor patch release following up the previous one done just a few weeks ago, fixing a few annoying bugs only.

Download it from [curl.se/trurl](https://curl.se/trurl)

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/trurl-logo-transparent.png)

## Fixes in 0.15.1

* The query parameter *normalization* introduced in 0.15 did not properly handle query pairs when one of the sides of the ‘=’ was blank.
* Make the generated manpage “source” to use the version number, not the title – which should be plain *trurl*.
* A minuscule escaping mistake in the manual markdown made the output render wrongly.
* Only install the manpage for ‘make install’ if there really is a manpage present – since it is generated and bundled in the release tarball it is not necessary present when users build their own

## Future

I have this feeling that we still have use cases and combinations that we don’t have tested in the test suite so we probably need to do a few more minor or patch releases until we are ready to bump this baby to 1.0.

[release](https://daniel.haxx.se/blog/tag/release/)[trurl](https://daniel.haxx.se/blog/tag/trurl/)

# Post navigation

[Previous Postcurl 8.10.0](https://daniel.haxx.se/blog/2024/09/11/curl-8-10-0/)[Next Postcurl 8.10.1](https://daniel.haxx.se/blog/2024/09/18/curl-8-10-1/)

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

September 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| [2](https://daniel.haxx.se/blog/2024/09/02/) | 3 | 4 | 5 | 6 | 7 | 8 |
| 9 | 10 | [11](https://daniel.haxx.se/blog/2024/09/11/) | [12](https://daniel.haxx.se/blog/2024/09/12/) | 13 | 14 | 15 |
| 16 | 17 | [18](https://daniel.haxx.se/blog/2024/09/18/) | [19](https://daniel.haxx.se/blog/2024/09/19/) | 20 | 21 | 22 |
| 23 | 24 | [25](https://daniel.haxx.se/blog/2024/09/25/) | 26 | 27 | 28 | 29 |
| 30 |  | | | | | |

[« Aug](https://daniel.haxx.se/blog/2024/08/)

[Oct »](https://daniel.haxx.se/blog/2024/10/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()