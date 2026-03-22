---
title: bye bye RTMP
url: https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/
source: daniel.haxx.se
date: 2026-03-21
fetch_date: 2026-03-22T04:18:45.359361
---

# bye bye RTMP

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/06/trimming-hedge.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# bye bye RTMP

[March 21, 2026](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/#comments)

In May 2010 we merged support for [the RTMP protocol](https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol) suite into curl, in our desire to support the world’s internet transfer protocols.

## RTMP

The protocol is an example of the spirit of an earlier web: back when we still thought we would have different transfer protocols for different purposes. Before HTTP(S) truly became the one protocol that rules them all.

RTMP was done by Adobe, used by Flash applications etc. Remember those? RTMP is an ugly proprietary protocol that simply was never used much in Open Source.

The common Open Source implementation of this protocol is done in the [rtmpdump project](https://rtmpdump.mplayerhq.hu/). In that project they produce a library, *librtmp*, which curl has been using all these years to handle the actual binary bits over the wire. Build curl to use librtmp and it can transfer RTMP:// URLs for you.

## librtmp

In our constant pursuit to improve curl, to find spots that are badly tested and to identify areas that *could* be weak from a security and functionality stand-point, our support of RTMP was singled out.

Here I would like to stress that I’m not suggesting that this is the only area in need of attention or improvement, but this was one of them.

As I looked into the RTMP situation I realized that we had *no* (zero!) tests of our own that actually verify RTMP with curl. It could thus easily break when we refactor things. Something we do quite regularly. I mean refactor (but also breaking things). I then took a look upstream into the librtmp code and associated project to investigate what exactly we are leaning on here. What we implicitly tell our users they can use.

I quickly discovered that the librtmp project does not have a single test either. They don’t even do releases since many years back, which means that most Linux distros have packaged up their code straight from their repositories. (The project insists that there is nothing to release, which seems contradictory.)

Is there perhaps any librtmp tests perhaps in the pipe? There had not been a single commit done in the project within the last twelve months and when I asked one of their leading team members about the situation, I was made clear to me that there is no tests in the pipe for the foreseeable future either.

## How about users?

In November 2025 I explicitly asked for RTMP users on the curl-library mailing list, and *one* person spoke up who uses it for testing.

In the 2025 user survey, 2.2% of the respondents said they had used RTMP within the last year.

The combination of *few users* and *untested code* is a recipe for pending removal from curl unless someone steps up and improves the situation. We therefor announced that we would remove RTMP support six months into the future unless someone cried out and stepped up to improve the RTMP situation.

We repeated this *we-are-doing-to-drop-RTMP* message in every release note and release video done since then, to make sure we do our best to reach out to anyone actually still using RTMP and caring about it.

If anyone would come out of the shadows *now* and beg for its return, we can always discuss it – but that will of course require work and adding test cases before it would be considered.

## Compatibility

Can we remove support for a protocol and still claim API and ABI backwards compatibility with a clean conscience?

This is the first time in modern days we remove support for a URL scheme and we do this without bumping the SONAME. We do not consider this an incompatibility primarily because *no one will notice*. It is only a break if it actually breaks something.

(RTMP in curl actually could be done using six separate URL schemes, all of which are no longer supported: rtmp`,`rtmpe`,`rtmps, rtmpt`,`rtmpte`,`rtmpts.)

The offical *number of URL schemes supported by curl* is now down to 27: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, MQTTS, POP3, POP3S, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

## When

[The commit](https://github.com/curl/curl/commit/ceae02db040de3cf7ae4c3f8ec99e8286b568c2e) that actually removed RTMP support has been merged. We had the protocol supported for almost sixteen years. The first curl release without RTMP support will be 8.20.0 planned to ship on April 29, 2026

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[URL](https://daniel.haxx.se/blog/tag/url/)

# Post navigation

[Previous PostOne hundred curl graphs](https://daniel.haxx.se/blog/2026/03/15/one-hundred-curl-graphs/)

## One thought on “bye bye RTMP”

1. ![](https://secure.gravatar.com/avatar/182c39d1abb76546e2f07cd21d3ffe3b4dab792f9e72b454f70a71b376b98a29?s=34&d=monsterid&r=g) **Peter Krefting** says:

   [March 22, 2026 at 00:53](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/#comment-27417)

   Surprisingly, RTMP is still alive and well. Or at least alive. Just not very much on the public internet. It is still being used as a way to deliver video streams from various sources on an intranet to a packager that then will create the DASH or HLS seen on the internet.

   Not being on the internet makes it hard to test, so I totally see why curl wants to drop it. Using librtmp directly instead of wrapping it inside libcurl is probably fine. Might even be easier…

   [Reply](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/?replytocom=27417#respond)

### Leave a Reply [Cancel reply](/blog/2026/03/21/bye-bye-rtmp/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
67seven6six

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [bye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/)
  March 21, 2026
* [One hundred curl graphs](https://daniel.haxx.se/blog/2026/03/15/one-hundred-curl-graphs/)
  March 15, 2026
* [chicken nuget](https://daniel.haxx.se/blog/2026/03/12/chicken-nuget/)
  March 12, 2026
* [curl 8.19.0](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/)
  March 11, 2026
* [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/)
  March 10, 2026
* [10K curl downloads per year](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/)
  March 9, 2026

# Recent Comments

* Peter Krefting on [bye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/comment-page-1/#comment-27417)
* Matthias Hörmann on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27416)
* Matt on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27415)
* Dmitry on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27414)
* Oleg on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27413)
* Johannes Müller on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03...