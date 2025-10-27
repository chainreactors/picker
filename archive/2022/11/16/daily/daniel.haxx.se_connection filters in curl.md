---
title: connection filters in curl
url: https://daniel.haxx.se/blog/2022/11/15/connection-filters-in-curl/
source: daniel.haxx.se
date: 2022-11-16
fetch_date: 2025-10-03T22:53:12.796304
---

# connection filters in curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/04/tools-1209764_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# connection filters in curl

[November 15, 2022](https://daniel.haxx.se/blog/2022/11/15/connection-filters-in-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

In the curl project, one of the holiest and most sacred rules is:

**we do not break the API or ABI**

Everything else is a matter of discussion.

## More features all the time

We keep adding features and we do improvements at a rather high pace. So much that we actually rarely do a release *without* introducing something new.

To be able to add features and to keep changing curl and making sure that it keeps up with the world around it and that it provides the features and the abilities that a world of Internet transfers needs, we need to make sure that the internals are written correctly. And by correctly, I mean in a way that allows us to extend and change curl when we want to – that doesn’t break the ABIs nor the tests.

## Refactors

curl is old and choices sometimes need to be reconsidered. Over the years we have refactored and changed the curl internals and design quite drastically several times. Thanks to an extensive test suite and a library API that was designed from the start to hide most internal choices, this has been possible to do without being visible to users. The upside has been that the internals have become easier to maintain and to extend with more features.

## Refactoring again

This time, we are again on a mission to [extend the curl feature set](https://daniel.haxx.se/blog/2022/10/19/funded-curl-improvements/) as I blogged about recently, and this time we have Stefan Eissing on board to do it.

So, without changing any API or breaking the ABI and having the large set of test cases remain working in the many CI jobs we have, Stefan introduced a new internal concept for curl: [connection filters](https://github.com/icing/blog/blob/main/curl-2022-10-30.md).

## Filters

We call them filters but they could also be seen as *layers* or maybe even *domino pieces*. Each filter is a piece of network logic and the idea is that we can chain them together at run-time to create *protocol cakes* (my word). curl can connect to a HTTP proxy, do TLS and speak HTTP/2 over that. That makes three separate filters put together.

Adding for example TLS to the proxy would just be inserting a filter in the right place in the chain, while using the filter-chain is done the same way no matter the filter chain length and independently of which exact filters it consists of.

The previous logic, before the filters, was a more like a vast number of conditional flag checks done in the right order. This new system reduces the amount of conditional checks and it also moves code for handling the different network filters into more localized and compartmentalized functions.

## More protocol combos

In addition to the more localized code for specifics features, this new concept more notably makes it easier to build new protocol layer combinations. Adding support for HTTP/2 to the proxy for example, should now ideally be a matter of adding a filter the right way and the transfer pipeline should otherwise “just work”.

Not everything internally is yet converted to filters even if [we have merged the first large pull request](https://github.com/curl/curl/pull/9855). Stefan now works on getting more curl code to use this concept before he can get into the actual protocol changes lined up for him.

## Performance

The filters do not impact transfer performance, I/O works the same as before.

## Details

If you long for more technical details and explanations about this, maybe to be able to dig into the curl source code yourself, then an excellent starting-point is the document in the curl source made for this purpose `[CONNECTION-FILTERS.md](https://github.com/curl/curl/blob/master/docs/CONNECTION-FILTERS.md)`.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[source code](https://daniel.haxx.se/blog/tag/source-code/)

# Post navigation

[Previous Postcurl’s new CA store cache](https://daniel.haxx.se/blog/2022/11/11/curls-new-ca-store-cache/)[Next PostConsidering C99 for curl](https://daniel.haxx.se/blog/2022/11/17/considering-c99-for-curl/)

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

November 2022

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | [2](https://daniel.haxx.se/blog/2022/11/02/) | [3](https://daniel.haxx.se/blog/2022/11/03/) | 4 | 5 | 6 |
| 7 | 8 | 9 | [10](https://daniel.haxx.se/blog/2022/11/10/) | [11](https://daniel.haxx.se/blog/2022/11/11/) | 12 | 13 |
| 14 | [15](https://daniel.haxx.se/blog/2022/11/15/) | 16 | [17](https://daniel.haxx.se/blog/2022/11/17/) | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | [25](https://daniel.haxx.se/blog/2022/11/25/) | 26 | 27 |
| 28 | 29 | 30 |  | | | |

[« Oct](https://daniel.haxx.se/blog/2022/10/)

[Dec »](https://daniel.haxx.se/blog/2022/12/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)