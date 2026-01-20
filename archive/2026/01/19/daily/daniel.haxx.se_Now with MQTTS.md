---
title: Now with MQTTS
url: https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/
source: daniel.haxx.se
date: 2026-01-19
fetch_date: 2026-01-20T03:33:46.552304
---

# Now with MQTTS

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Now with MQTTS

[January 19, 2026](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/#comments)

Back in 2020 we added [MQTT](https://daniel.haxx.se/blog/2020/04/14/curl-mqtt-true/) support to curl.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2016/04/good_curl_logo-1200x459.png)](https://curl.se/)

When curl 8.19.0 ships in the beginning of March 2026, we have also added MQTTS; meaning MQTT done securely over TLS.

This bumps the number of supported transfer protocols to 29 not too long after the project turned 29 years old.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/01/curl-coverage11.jpg)

The 29 transfer protocols (or schemes) that curl supports in January 2026

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/01/libcurl-backends7.jpg)

libcurl backends as of now

## What’s MQTT?

[Wikipedia describes it](https://en.wikipedia.org/wiki/MQTT) as *a lightweight, publish–subscribe, machine-to-machine network protocol for message queue/message queuing service. It is designed for connections with remote locations that have devices with resource constraints or limited network bandwidth, such as in the Internet of things (IoT). It must run over a transport protocol that provides ordered, lossless, bi-directional connections—typically, TCP/IP.*

## Coming protocol support *reduction*

If things go as planned, the number of supported protocols will decrease soon as we have RTMP scheduled for removal later in the spring of 2026.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[MQTT](https://daniel.haxx.se/blog/tag/mqtt/)[protocols](https://daniel.haxx.se/blog/tag/protocols/)[TLS](https://daniel.haxx.se/blog/tag/tls/)

# Post navigation

[Previous PostMy first 20,000 curl commits](https://daniel.haxx.se/blog/2026/01/17/my-first-20000-curl-commits/)

## 2 thoughts on “Now with MQTTS”

1. ![](https://secure.gravatar.com/avatar/75c5d927b0434111db9720dd78af8c83385cf28bb9aeafd031ba8cb0c4ffc558?s=34&d=monsterid&r=g) **Christophe Coevoet** says:

   [January 19, 2026 at 14:52](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/#comment-27383)

   Is the date of May 2026 actually correct ? This seems far away compared to the release schedule of curl, especially considering that the PR implementing it is already merged.

   [Reply](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/?replytocom=27383#respond)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 19, 2026 at 16:26](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/#comment-27384)

      @Christophe: oh right, thanks. It should be **beginning of March 2026**, no other month. Fixed now.

      [Reply](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/?replytocom=27384#respond)

### Leave a Reply [Cancel reply](/blog/2026/01/19/now-with-mqtts/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
threeoneeightnine9

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/)
  January 19, 2026
* [My first 20,000 curl commits](https://daniel.haxx.se/blog/2026/01/17/my-first-20000-curl-commits/)
  January 17, 2026
* [More HTTP/3 focus, one backend less](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/)
  January 17, 2026
* [curl 8.18.0](https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/)
  January 7, 2026
* [6,000 curl stickers](https://daniel.haxx.se/blog/2026/01/06/6000-curl-stickers/)
  January 6, 2026
* [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/)
  December 29, 2025

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/comment-page-1/#comment-27384)
* Christophe Coevoet on [Now with MQTTS](https://daniel.haxx.se/blog/2026/01/19/now-with-mqtts/comment-page-1/#comment-27383)
* [Daniel Stenberg](https://daniel.haxx.se/) on [More HTTP/3 focus, one backend less](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/comment-page-1/#comment-27381)
* Aaron Chen on [More HTTP/3 focus, one backend less](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/comment-page-1/#comment-27380)
* Ted Lyngmo on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27379)
* tetsuoii on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27378)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27377)
* spagoveanu on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27376)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27375)
* [Verisimilitude](http://verisimilitudes.net) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27374)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

January 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2026/01/06/) | [7](https://daniel.haxx.se/blog/2026/01/07/) | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | [17](https://daniel.haxx.se/blog/2026/01/17/) | 18 |
| [19](https://daniel.haxx.se/blog/2026/01/19/) | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Dec](https://daniel.haxx.se/blog/2025/12/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()