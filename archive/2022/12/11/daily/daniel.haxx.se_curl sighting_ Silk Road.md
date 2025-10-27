---
title: curl sighting: Silk Road
url: https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/
source: daniel.haxx.se
date: 2022-12-11
fetch_date: 2025-10-04T01:12:27.901050
---

# curl sighting: Silk Road

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/silkroad-phpcode.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl sighting: Silk Road

[December 10, 2022](https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/#comments)

In the 2021 movie [Silk Road](https://www.imdb.com/title/tt7937254/?ref_=nv_sr_srsg_0), at around 19:23-19:26 into the film we can see Ross Ulbricht, the lead character, write a program on his laptop that uses curl. A few seconds we get a look at the screen as Ross types on the keyboard and explains to the female character who says *I didn’t know you know how to code* that he’s teaching himself to write code.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Silk-Road-2021.png)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Silk-Road-2021.png)

## The code

Let’s take a look at the code on the screen. This is PHP code using the well known [PHP/CURL binding](https://www.php.net/manual/en/book.curl.php). The URL on the screen on line two has really bad contrast, but I believe this is what it says:

```
<?php
  $ch = curl_init("http://silkroadvb5pzir.onion");
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_PROXY,
              "http://127.0.0.1:9050/");
  curl_setopt($ch, CURLOPT_PROXYTYPE, 7);
  $output = curl_exec($ch);
  $curl_error = curl_error($ch);
  curl_cl
```

`.onion` is a TLD for websites on [Tor](https://www.torproject.org/) so this seems legit as it a URL for this purpose could look like this. But then Ross confuses matters a little. He uses *two* `curl_init()` calls, one that sets a URL and then again a call *without* a URL. He could just have removed line three and four. This doesn’t prohibit the code from working, it just wouldn’t have passed a review.

The code then sets a proxy to use for the transfer, specified as an HTTP URL which is a little odd since the proxy type he then sets on the line below is 7, the number corresponding to `CURLPROXY_SOCKS5_HOSTNAME` – so not a HTTP proxy at all but a SOCKS5 proxy. The typical way you access Tor: as a SOCKS5 proxy to which you pass the host name, as opposed to resolving the host name locally.

The last line is incomplete but should ultimately be `curl_close($ch);` to close the handle after use.

All in all a seemingly credible piece of code, especially if we consider it as a work in progress code. The minor mistakes would be soon be fixed.

## Credits

Viktor Szakats spotted this and sent me the screenshot above. Thanks!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[movies](https://daniel.haxx.se/blog/tag/movies/)[PHP](https://daniel.haxx.se/blog/tag/php/)

# Post navigation

[Previous PostFaster base64 in curl](https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/)[Next PostIDN is crazy](https://daniel.haxx.se/blog/2022/12/14/idn-is-crazy/)

## 2 thoughts on “curl sighting: Silk Road”

1. ![](https://secure.gravatar.com/avatar/55c204e02883ba1f43870399c9ab4a96f8a7b702a33a3f1d9fde981b7293f11d?s=34&d=monsterid&r=g) **Peter** says:

   [December 11, 2022 at 21:53](https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/#comment-26513)

   The sad part about this is that one reason “frosty”, i.e. Ross Ulbricht, was caught was his post on stackoverflow:

   <https://stackoverflow.com/questions/15445285/how-can-i-connect-to-a-tor-hidden-service-using-curl-in-php>

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [December 11, 2022 at 23:00](https://daniel.haxx.se/blog/2022/12/10/curl-sighting-silk-road/#comment-26514)

      @Peter: Oh, I did not know about that. Thanks for this tidbit! Curious how similar that stackoverflow question’s code sample is to the code seen in the movie…

Comments are closed.

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

December 2022

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2022/12/06/) | 7 | 8 | 9 | [10](https://daniel.haxx.se/blog/2022/12/10/) | 11 |
| 12 | 13 | [14](https://daniel.haxx.se/blog/2022/12/14/) | 15 | 16 | 17 | 18 |
| [19](https://daniel.haxx.se/blog/2022/12/19/) | 20 | [21](https://daniel.haxx.se/blog/2022/12/21/) | 22 | [23](https://daniel.haxx.se/blog/2022/12/23/) | 24 | 25 |
| 26 | [27](https://daniel.haxx.se/blog/2022/12/27/) | [28](https://daniel.haxx.se/blog/2022/12/28/) | 29 | [30](https://daniel.haxx.se/blog/2022/12/30/) | 31 |  |

[« Nov](https://daniel.haxx.se/blog/2022/11/)

[Jan »](https://daniel.haxx.se/blog/2023/01/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)