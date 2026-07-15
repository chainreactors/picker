---
title: Workshop Basel day one
url: https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/
source: daniel.haxx.se
date: 2026-07-14
fetch_date: 2026-07-15T04:48:52.705540
---

# Workshop Basel day one

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/07/HTTP-ws.jpg)

[Network](https://daniel.haxx.se/blog/category/tech/net/), [Web](https://daniel.haxx.se/blog/category/web/)

# Workshop Basel day one

[July 14, 2026](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/#respond)

On this hot summer’s day in Basel, Switzerland, the seventh HTTP workshop started. These events tend to work roughly the same way and the people in the room are also to large extent familiar and known since previous editions. Forty people in a meeting room, where we take turns in doing short talks on HTTP and networking topics, with the following question and discussion session. The rules for the meetings are explicitly Chatham rules, which means that everything I write about the meeting will be sufficiently fuzzy and without many company or personal names. This is not the kind of meeting that can be easily summed up in a short blog post anyway. You really should be here.

Present in the room were representatives from all the world’s most prominent and used HTTP deployments: clients, browsers, CDNs, proxies and servers. I’m happy to say that there were also several first-timers. We like fresh blood.

(If you think I’m being overly brief or vague about specifics in this post; that is partially on purpose but primarily because I’m a lousy note-taker and mostly write this up after a busy day that also may have involved beer.)

After a round of introductions, we started.

## **Extending REST for State synchronization**

REST is a set of constraints, and in this presentation it was argued that it can or maybe even should be extended to do more. A number of recent applications like Mastodon/ActivityPub, Bluesky/AT, Matrix, Nostr, IndieWeb, all currently use HTTP to do state synchronization but they all do it differently in their own unique ways. Can REST and maybe HTTP be adjusted to help this for improved interoperability?

## **Last-Modified header use over time**

Looking at the Common Crawl data and comparing data over time, it was observed that responses use the Last-Modified header field more now than they did in the past, and there were great follow-up speculations on why this is so. Data also shows that a large share of these headers present dates that are almost identical to the time the requests were issued.

## **How is HTTP used in the world?**

With the [cc-lint tool](https://projects.mnot.net/cc-lint/), data was gathered on how HTTP is actually used today, proving that there is work to be done: deprecated headers are used, some headers are done wrong, and many are overly big. This indicates that there are well used both servers and clients out there that would benefit from cleanup. It probably also shows that doing HTTP correctly and all the correct headers is far from an easy task.

## **AI-bots’ use of HTTP**

Another presentation showed data, this time from a well-known CDN, on the impact the existing AI scraper bots have on the Internet from their point of view. It showed that roughly half of the requests and half of the bandwidth are spent by scraper bots. A long discussion followed where the numbers were questioned as maybe the numbers look like this because a sufficiently large number of the “bad AI scrapers” appear as regular users to the classifiers. Speculations of different kinds were made.

## **The Apple HTTP stack two years later**

As a follow-up from a presentation from a previous HTTP workshop we got to learn how the journey on developing their new HTTP stack has progressed and several fun adventures and lessons from that were shared with the audience.

## **Why new HTTP APIs?**

A look into new [HTTP API development at Apple](https://github.com/apple/swift-http-api-proposal). Some discussions and lessons learned from creating new APIs for both servers and clients.

## **Android Networking**

We got an excellent walk-through of some details and internals of the Android networking stack. Emphasis was perhaps especially put on ECH and QUIC connection migration, and the final “don’t tell us when your connection closed” led to a long new discussion on how we really should fix the problem: when connection has been left idle for a long time and it is closed by the server, the client (mobile phones) don’t want to be told. This, because getting that RST and more, just wakes up the radio and more on the phone only to tell it to go back to sleep. It was theorized that if we could get rid of this unnecessary battery waste, the accumulated gain across billions of devices would make a serious dent.

## **Day one world problem solving**

Several additional HTTP related problems were of course also subsequently solved as we then wandered into the city for dinner and maybe a beer. Of course yours truly returned back to his hotel room in good time to be able to write up this blog post.

The best part of these workshops might be the (no pun intended) networking and discussions had completely outside of the agenda.

End of day one. Two more to come,

[HTTP](https://daniel.haxx.se/blog/tag/http/)[HTTP Workshop](https://daniel.haxx.se/blog/tag/http-workshop/)[QUIC](https://daniel.haxx.se/blog/tag/quic/)

# Post navigation

[Previous PostDo excellent vulnerability reports](https://daniel.haxx.se/blog/2026/06/29/do-excellent-vulnerability-reports/)

### Leave a Reply [Cancel reply](/blog/2026/07/14/workshop-basel-day-one/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
sixfour42eight

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/)
  July 14, 2026
* [Do excellent vulnerability reports](https://daniel.haxx.se/blog/2026/06/29/do-excellent-vulnerability-reports/)
  June 29, 2026
* [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/)
  June 26, 2026
* [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/)
  June 25, 2026
* [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)
  June 24, 2026
* [curl 8.21.0](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/)
  June 24, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [Do excellent vulnerability reports](https://daniel.haxx.se/blog/2026/06/29/do-excellent-vulnerability-reports/comment-page-1/#comment-27531)
* entronid on [Do excellent vulnerability reports](https://daniel.haxx.se/blog/2026/06/29/do-excellent-vulnerability-reports/comment-page-1/#comment-27530)
* Nils on [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/comment-page-1/#comment-27528)
* entronid on [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/comment-page-1/#comment-27527)
* [Jan Tångring](https://etn.se/) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#comment-27525)
* [Daniel Stenberg](https://daniel.haxx.se/) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#comment-27524)
* [Jonathan Desrosiers](https://jonathandesrosiers.com) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#c...