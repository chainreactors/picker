---
title: More HTTP/3 focus, one backend less
url: https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/
source: daniel.haxx.se
date: 2026-01-17
fetch_date: 2026-01-18T03:38:13.706316
---

# More HTTP/3 focus, one backend less

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/06/QUIC-672x372.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# More HTTP/3 focus, one backend less

[January 17, 2026](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/01/17/more-http-3-focus-one-backend-less/#respond)

In the curl project we have a long tradition of offering multiple optional backends for specific protocols. In this spirit we have added experimental support for a number of different HTTP/3 + QUIC backends over time. A while ago we dropped one of those experiments, the [msh3](https://daniel.haxx.se/blog/2025/07/29/carving-out-msh3/) backend.

[Today](https://github.com/curl/curl/pull/20226) we cleanup even more and **remove support for yet another backend: the OpenSSL-QUIC stack** and we are now down to only supporting two different HTTP/3 alternatives: the nghttp2 + nghttp3 combo or quiche. And out of those two, the quiche backend is still considered experimental.

The first release shipping with this change will be curl 8.19.0.

## OpenSSL-QUIC

This is the QUIC stack implemented and provided by OpenSSL. To make matters a little complicated, this is a separate thing from the *QUIC API* that OpenSSL also offers. The first one is a full QUIC implementation, the second one is an API that is powerful enough to allow a separate QUIC implementation use OpenSSL for its cryptographic and TLS needs.

## A quick recap how history unfolded

2019 – BoringSSL introduced an API for QUIC. QUIC implementations picked it up and it worked. A pull request was made for OpenSSL to allow them to provide the same API so that QUIC stacks all over could use OpenSSL.

2021 – OpenSSL eventually denied merging the pull-request and announced they would instead implement their own QUIC stack – that nobody had asked for.

2023 – OpenSSL 3.2 shipped with support for their own QUIC stack. It was broken in many ways.

2025: OpenSSL version 3.4.1 was released and now the QUIC stack worked *decently*. In OpenSSL 3.5.0 they announced a QUIC API that now finally allowed independent QUIC stacks to use OpenSSL.

## Experimental

Skilled contributors added support for OpenSSL-QUIC to curl primarily to allow people using OpenSSL to still be able to use HTTP/3.

OpenSSL’s own QUIC implementation only reached *experimental* state in curl meaning that we explicitly and strongly discourage users from using it in production and reserve ourselves the right to change functionality and more between versions.

There are three reasons why it did not graduate from experimental and they are also the reasons why we think we are better off without offering support for it:

1. The API is lacking. We have communicated with the OpenSSL-QUIC team since even before the API first shipped and it still does not offer the knobs and controls we would like to make it a competitive QUIC alternative. We don’t feel they care much.
2. The performance is bad. And by bad I mean really bad. The leading QUIC implementation alternative ngtcp2 transfers data *much* faster in all benchmarks and comparisons. Sometimes up to **a factor three** difference.
3. The memory use is abysmal. The amount of more memory required to do transfers with OpenSSL-QUIC compared to ngtcp2 can reach **a factor** **twenty.**

## A drawing

This makes the curl backend situation simpler in the HTTP/3 and QUIC department as the image below tries to show.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/01/curl-HTTP_3-backends9.jpg)

HTTP/3 backends in curl in January 2026

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP/3](https://daniel.haxx.se/blog/tag/http3/)[OpenSSL](https://daniel.haxx.se/blog/tag/openssl/)[QUIC](https://daniel.haxx.se/blog/tag/quic/)

# Post navigation

[Previous Postcurl 8.18.0](https://daniel.haxx.se/blog/2026/01/07/curl-8-18-0/)[Next PostMy first 20,000 curl commits](https://daniel.haxx.se/blog/2026/01/17/my-first-20000-curl-commits/)

### Leave a Reply [Cancel reply](/blog/2026/01/17/more-http-3-focus-one-backend-less/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
7threefoursixnine

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

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
* [A curl 2025 review](https://daniel.haxx.se/blog/2025/12/23/a-curl-2025-review/)
  December 23, 2025

# Recent Comments

* Ted Lyngmo on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27379)
* tetsuoii on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27378)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27377)
* spagoveanu on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27376)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27375)
* [Verisimilitude](http://verisimilitudes.net) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27374)
* Billy O'Neal on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27373)
* Billy O'Neal on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27372)
* [Daniel Stenberg](https://daniel.haxx.se/) on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27371)
* John Brown II on [no strcpy either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/comment-page-1/#comment-27370)

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
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Dec](https://daniel.haxx.se/blog/2025/12/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()