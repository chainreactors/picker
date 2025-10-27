---
title: The 2024 Workshop, day two
url: https://daniel.haxx.se/blog/2024/11/13/the-2024-workshop-day-two/
source: daniel.haxx.se
date: 2024-11-14
fetch_date: 2025-10-06T19:18:42.218881
---

# The 2024 Workshop, day two

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/better-internet.jpg)

[Network](https://daniel.haxx.se/blog/category/tech/net/), [Web](https://daniel.haxx.se/blog/category/web/)

# The 2024 Workshop, day two

[November 13, 2024](https://daniel.haxx.se/blog/2024/11/13/the-2024-workshop-day-two/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

The fun continues. See [day one](https://daniel.haxx.se/blog/2024/11/13/the-2024-http-workshop/).

In an office building close to the Waterloo station in London, around 40 persons again sat down at this giant table forming a big square that made it possible for us all to see each other. One by one there were brief presentations done with follow-up discussions. The discussions often reiterated old truths, brought up related topics and sometimes went deep down into the weeds about teeny weeny details of the involved protocol specs. The way we love it.

The people around the table represent Ericsson, Google, Microsoft, Apple, Meta, Akamai, Cloudflare, Fastly, Mozilla, Varnish. Caddy, Nginx, Haproxy, Tomcat, Adobe and curl and probably a few more I forget now. One could say with some level of certainty that a large portion of every day HTTP traffic in the world is managed by things managed by people present here.

This morning we all actually understood that the south entrance is actually the east one (yeah, that’s a so called *internal joke*) and most of us were sitting down, eager and prepared when the day started at 9:30 am.

**Capsule**. The capsule protocol ([RFC 9297](https://datatracker.ietf.org/doc/rfc9297/)) is a way to, put simply, send UDP packets/datagrams over old style HTTP/1 or HTTP/2 proxies.

**[Cookies](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/3.%20Semantics/cookies.pdf)**. With the 6265bis effort well on its way to ship as an updated RFC, there is an effort and intent to take yet another stab at improving and refreshing the cookie spec situation. In particular to better split off browser management and API related stuff from the more network-oriented over-the-wire details. You know yours truly never ceases an opportunity to voice his opinion on cookies… I approve of this attempt as well, as I think increasing clarity and improving the specification situation can’t but to help improve things.

**[Declarative web push](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/3.%20Semantics/declarative%20web%20push.pdf)**. There’s an ongoing effort to improve web push – not to be confused with server push, so that it can be done easier and without needing JavaScript to manage it in the client side.

**[Reverse HTTP](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/3.%20Semantics/reverse%20HTTP.pdf)**. There are origins who want to contact their CDNs without having to listening on any ports/sockets and still be able to provide content. That’s one of the use cases for Reverse HTTP and we got to learn details from internet drafts done on the topics for the last fifteen years and why it might still be a worthwhile effort and why the use cases still exist. But is there an enough demand to put it into HTTP?

**Server Stack Detection**. A discussion around how someone can detect the origin of the server stack of any given HTTP server implementation. Should there be a better way? What is the downside of introducing what would basically be the server version of the user-agent header field? Lots of productive discussions on how to avoid recreating problems of the past but in a reversed way.

**[MoQ: What is it and why is it not just HTTP/3?](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/4.%20Evolution/MoQ.pdf)** Was an educational session about the ongoing work done in this working group that is wrongly named and would appreciate more input from the general protocol community.

**[New HTTP stack](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/new%20stack.pdf)**. A description of the journey of a full HTTP stack rewrite: how components can be chained together and in which order and a follow-up discussion about if this should be included in documentation and if so in which way etc. Lessons included that the spec is one thing, the Internet is another. Maybe not an entirely new revelation.

**[Multiplexing in the year 2024](https://github.com/HTTPWorkshop/workshop2024/blob/main/talks/4.%20Evolution/multiplexing.pdf)**. There are details in HTTP/2 multiplexing that does not really work, there are assumptions that are now hard to change. To introduce new protocols and features in the modern HTTP stack, things need to be done for both HTTP/2 and HTTP/3 that are similar but still different and it forces additional work and pain.

What if we create a way to do multiplexing over TCP, so called “over streams”, so that the HTTP/3 fallback over TCP could still be done using HTTP/3 framing. This would allow future new protocols to remain HTTP/3-only and just make the transport be either QUIC+UDP or Streams-over TCP+TLS. This triggered a lot of discussions, mostly positive and forward-looking but also a lot of concerns raised about additional work and yet another protocols component to write and implement that then needs to be supported until the end of times because things never truly go away completely.

I think this sounds like a fun challenge! Count me in.

End of day two. I need a beer or two to digest this.

[HTTP](https://daniel.haxx.se/blog/tag/http/)[HTTP Workshop](https://daniel.haxx.se/blog/tag/http-workshop/)

# Post navigation

[Previous PostThe 2024 HTTP Workshop](https://daniel.haxx.se/blog/2024/11/13/the-2024-http-workshop/)[Next PostWorkshop season six, episode three](https://daniel.haxx.se/blog/2024/11/14/workshop-season-six-episode-three/)

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
* H. Stefan on [car brands running curl](https://daniel.hax...