---
title: QUERY with curl
url: https://daniel.haxx.se/blog/2026/06/21/query-with-curl/
source: daniel.haxx.se
date: 2026-06-20
fetch_date: 2026-06-21T06:49:46.880652
---

# QUERY with curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/06/IETF-Badge-HTTP.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Web](https://daniel.haxx.se/blog/category/web/)

# QUERY with curl

[June 21, 2026](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/#respond)

[RFC 10008](https://www.rfc-editor.org/info/rfc10008/) is brand new a specification detailing the new HTTP method called QUERY:

*This specification defines the QUERY method for HTTP. A QUERY requests that the request target process the enclosed content in a safe and idempotent manner and then respond with the result of that processing. This is similar to POST requests but can be automatically repeated or restarted without concern for partial state changes*

## A GET with body

For all practical purposes you can think of QUERY as a way to send a GET with a body. It looks exactly like POST, but done with another verb.

Contrary to POST, QUERY requests are *idempotent* – they can be retried or repeated when needed, for instance after a connection failure.

## curl it

You can use curl to do HTTP requests with QUERY just fine. curl offers the `--request` option (also known as -X in the short form) that you can use like this:

```
curl -d "data to send" -X QUERY https://example.com/
```

## But redirects!

There is one little caveat to remember with this curl option that changes the method. When *also* asking curl to follow any possible redirects, it is important that you use a new enough curl version because you want the [`--follow`](https://daniel.haxx.se/blog/2025/08/06/follow-redirects-but-differently/) option. **Not** the old `--location/-L` one.

Why? Because the old option changes the HTTP method on all subsequent requests independently of what the server responds, which in many cases is not what you want.

The newer `--follow` option instead acts according to what the HTTP response code suggests in should do. Stick to the same method again, or maybe switch to GET in the following request.

## Why?

Why or when would you use this? First of course you only want to use this if the server supports it, but the spec offers some reasons why this might be a good choice:

* avoid or circumvent URL size limits. Somewhere around 8000 bytes they start to no longer work reliably because servers and intermediaries set limits.
* expressing certain kinds of data in the URL is inefficient because encoding overhead
* URLs are more likely to be logged than request content

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP](https://daniel.haxx.se/blog/tag/http/)

# Post navigation

[Previous Postcurl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)

### Leave a Reply [Cancel reply](/blog/2026/06/21/query-with-curl/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
4nineone4four

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/)
  June 21, 2026
* [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)
  June 15, 2026
* [A human in control](https://daniel.haxx.se/blog/2026/06/10/a-human-in-control/)
  June 10, 2026
* [curl up 2026 summary](https://daniel.haxx.se/blog/2026/05/28/curl-up-2026-summary/)
  May 28, 2026
* [The pressure](https://daniel.haxx.se/blog/2026/05/26/the-pressure/)
  May 26, 2026
* [named globs with curl](https://daniel.haxx.se/blog/2026/05/16/named-globs-with-curl/)
  May 16, 2026

# Recent Comments

* [XQ539](https://wayne-intressierts.de) on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27514)
* fridayafternoon on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27513)
* ThankFull on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27512)
* fm on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27509)
* H. Stefan on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27508)
* bengan on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27507)
* Sam on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27506)
* [webknjaz (Sviatoslav Sydorenko)](https://webknjaz.me) on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27505)
* Sam on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27503)
* [Max Danielsson](https://www.autious.net) on [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/comment-page-1/#comment-27502)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

June 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 8 | 9 | [10](https://daniel.haxx.se/blog/2026/06/10/) | 11 | 12 | 13 | 14 |
| [15](https://daniel.haxx.se/blog/2026/06/15/) | 16 | 17 | 18 | 19 | 20 | [21](https://daniel.haxx.se/blog/2026/06/21/) |
| 22 | 23 | 24 | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« May](https://daniel.haxx.se/blog/2026/05/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)