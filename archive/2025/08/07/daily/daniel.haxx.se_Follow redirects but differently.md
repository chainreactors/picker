---
title: Follow redirects but differently
url: https://daniel.haxx.se/blog/2025/08/06/follow-redirects-but-differently/
source: daniel.haxx.se
date: 2025-08-07
fetch_date: 2025-10-07T00:47:43.590521
---

# Follow redirects but differently

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2020/11/pointing-finger.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Follow redirects but differently

[August 6, 2025](https://daniel.haxx.se/blog/2025/08/06/follow-redirects-but-differently/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

In the early days of curl development we (I suppose it was me personally but let’s stick with *we* so that I can pretend the blame is not all on me) made the possibly slightly unwise decision to make the -X option change the HTTP method for all requests in a curl transfer, even when -L is used – and independently of what HTTP responses the server returns.

That decision made me write blog posts and inform people all over about how [using -X superfluously causes problems](https://daniel.haxx.se/blog/2015/09/11/unnecessary-use-of-curl-x/).

In curl 8.16.0, we introduce a different take on the problem, or better yet, a solution really: a new command line option that offers a modified behavior. Possibly the behavior people were thinking curl was having all along.

Just learn to use `--follow` going forward (in curl 8.16.0 and later).

This option works fine together with -X and will adjust the method in the possible subsequent requests according to the HTTP response code.

A long time ago I wrote separately about [the different HTTP response codes](https://daniel.haxx.se/blog/2016/02/18/http-redirects/) and what they mean in terms of changing (or not) the method.

## –location remains the same

Since we cannot break existing users and scripts, we had to leave the exiting `--location` option working exactly like it always has. This option is this mutually exclusive with `--follow`, so only pick one.

## QUERY friendly

Part of the reason for this new option is to make sure curl can follow redirects correctly for other HTTP methods than the good old fashioned GET, POST and PUT. We already see PATCH used to some extent but perhaps more important is the work on the spec for the new QUERY method. It is a flavor of POST, but with a few minor but important different properties. Possibly enough for me to write a separate blog post about, but right now we can stick to it being “like POST”, in particular from a HTTP client’s perspective.

We want curl to be able to do a “post” but with a QUERY method and still follow redirects correctly. *The -L and -X combination does not support this.*

curl can be made to issue a *proper* QUERY request and follow redirects correctly like this:

```
curl -X QUERY --follow -d sendthis https://example.com/
```

Thank you for flying curl!

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postc10kday](https://daniel.haxx.se/blog/2025/08/05/c10kday/)[Next Postcurl tells the %time](https://daniel.haxx.se/blog/2025/08/07/curl-tells-the-time/)

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