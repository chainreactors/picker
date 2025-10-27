---
title: HTTP Workshop 2022 – day 1
url: https://daniel.haxx.se/blog/2022/11/02/http-workshop-2022-day-1/
source: daniel.haxx.se
date: 2022-11-02
fetch_date: 2025-10-03T21:32:23.717438
---

# HTTP Workshop 2022 – day 1

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

# HTTP Workshop 2022 – day 1

[November 2, 2022](https://daniel.haxx.se/blog/2022/11/02/http-workshop-2022-day-1/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

> The HTTP Workshop is an occasional gathering of HTTP experts and other interested parties to discuss the Web’s foundational protocol.

The fifth [HTTP Workshop](https://httpwork.shop/) is a three day event that takes place in Oxford, UK. I’m happy to say that I am attending this one as well, as I have all the previous occasions. This is now more than seven years since [the first one](https://daniel.haxx.se/blog/2015/07/27/the-http-workshop-started/).

## Attendees

A lot of the people attending this year have attended previous workshops, but in a lot of cases we are now employed by other companies then when we attended our first workshops. Almost thirty HTTP stack implementers, experts and spec authors in a room.

There was a few newcomers and some regulars are absent (and missed). Unfortunately, we also maintain the lack of diversity from previous years. We are of course aware of this, but have still failed to improve things in this area very much.

## Setup

All the people gather in the same room. A person talks briefly on a specific topic and then we have a free-form discussion about it. When I write this, the slides from today’s presentations have not yet been made available so I cannot link them here. I will add those later.

## Discussions

Mark’s [introduction talk](https://github.com/HTTPWorkshop/workshop2022/blob/main/talks/intro.pdf).

Lucas Pardue started the morning with a presentation and discussion around logging, tooling and the difficulty of debugging modern HTTP setups. With binary protocols doing streams and QUIC, qlog and qvis are in many ways the only available options but they are not supported by everything and there are gaps in what they offer. Room for improvements.

Anne van Kesteren [showed a proposal](https://github.com/HTTPWorkshop/workshop2022/blob/main/talks/no-vary-search.pdf) from Domenic Denicola for a [No-Vary-Search](https://github.com/WICG/nav-speculation/blob/main/no-vary-search.md) response header. An attempt to specify a way for HTTP servers to tell clients (and proxies) that parts of the query string produces the same response/resource and should be cached and treated as the same.

An issue that is more complicated than what if first might seem. The proposal has some fans in the room but I think the general consensus was that it is a bad name for the header…

Martin Thomson talked about [new stuff in HTTP](https://github.com/HTTPWorkshop/workshop2022/blob/main/talks/new-stuff.pdf).

HTTP versions. HTTP/3 is used in over a third of the requests both as seen by Cloudflare server-side and measured in Firefox telemetry client-side. Extensible and functional protocols. Nobody is talking about or seeing a point in discussing about a HTTP/4.

WebSocket over h2/h3. There does not seem to be any particular usage and nobody mentioned any strong reason or desired to change the status. Web Transport is probably what instead is going to be the future.

Frames. Discussions around the use and non-use of the origin frame. Note widely used. Could help to avoid extra “SNI leakage” and extra connections.

Anne then took a second round in front of the room and questioned us on [the topic of cookies](https://github.com/HTTPWorkshop/workshop2022/blob/main/talks/cookies.pdf). Or perhaps more specifically about details in the spec and how to possible change the spec going forward. At least one person in the room insisted fairly strongly than any such restructures of said documents should be done *after* the ongoing 6265bis work is done.

## Dinner

A company very generously sponsored a group dinner for us in the evening and I had a great time. I was asked to not reveal the name of said company, but I can tell you that a lot of the conversations at the table, at least in the area where I was parked, kept up the theme from the day and were HTTP oriented. Including oblivious HTTP, IPv4 formatting allowed in URLs and why IP addresses should not be put in the SNI field. Like any good conversion among friends.

[HTTP](https://daniel.haxx.se/blog/tag/http/)[HTTP Workshop](https://daniel.haxx.se/blog/tag/http-workshop/)

# Post navigation

[Previous Postcurl 7.86.0 with WebSocket](https://daniel.haxx.se/blog/2022/10/26/7-86-0-with-websocket/)[Next PostWorkshop season 5 episode 2](https://daniel.haxx.se/blog/2022/11/03/workshop-season-5-episode-2/)

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
| 21 | 22 | 23 | 24 | [25](https://daniel.haxx.se/blog/2022/11/25/) | 26 | 27...