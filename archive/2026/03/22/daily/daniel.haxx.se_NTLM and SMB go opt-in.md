---
title: NTLM and SMB go opt-in
url: https://daniel.haxx.se/blog/2026/03/22/ntlm-and-smb-go-opt-in/
source: daniel.haxx.se
date: 2026-03-22
fetch_date: 2026-03-23T04:23:22.476607
---

# NTLM and SMB go opt-in

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/09/old-machine.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# NTLM and SMB go opt-in

[March 22, 2026](https://daniel.haxx.se/blog/2026/03/22/ntlm-and-smb-go-opt-in/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/03/22/ntlm-and-smb-go-opt-in/#respond)

The NTLM authentication method was always a beast.

It is a proprietary protocol designed by Microsoft which was reverse engineered a long time ago. That effort resulted in the online documentation that I based the curl implementation on back in 2003. I then also wrote the NTLM code for wget while at it.

NTLM broke with the HTTP paradigm: it is made to authenticate *the connection* instead of *the request*, which is what HTTP authentication is supposed to do and what all the other methods do. This might sound like a tiny and insignificant detail, but it has a major impact in all HTTP implementations everywhere. Indirectly it is also the cause for quite a few security related issues in HTTP code, because NTLM needs many special exceptions and extra unique treatments.

curl has recorded no less than *seven* past [security vulnerabilities](https://curl.se/docs/security.html) in NTLM related code! While that may not be only NTLM’s fault, it certainly does not help.

The connection-based concept also makes the method *incompatible* with HTTP/2 and HTTP/3. NTLM requires services to stick to HTTP/1.

NTLM (v1) uses super weak cryptographic algorithms (DES and MD5), which makes it a bad choice even when disregarding the other reasons.

We are slowly deprecating NTLM in curl, but we are starting out by making it opt-in. Starting in curl 8.20.0, NTLM is disabled by default in the build unless specifically enabled.

Microsoft themselves have deprecated NTLM already. The wget project looks like it is about to make their NTLM support opt-in.

## SMB

curl only supports SMB version 1. This protocol uses NTLM for the authentication and it is equally bad in this protocol. Without NTLM enabled in the build, SMB support will also get disabled.

But also: SMBv1 is in itself a weak protocol that is barely used by curl users, so this protocol is also opt-in starting in curl 8.20.0. You need to explicitly enable it in the build to get it added.

## Not removed yet

I want to emphasize that we have not removed support for these ancient protocols, we just strongly discourage using them and I believe this is a first step down the ladder that in a future will make them get removed completely.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postbye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/)

### Leave a Reply [Cancel reply](/blog/2026/03/22/ntlm-and-smb-go-opt-in/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
sixfourone6eight

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [NTLM and SMB go opt-in](https://daniel.haxx.se/blog/2026/03/22/ntlm-and-smb-go-opt-in/)
  March 22, 2026
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

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [bye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/comment-page-1/#comment-27418)
* Peter Krefting on [bye bye RTMP](https://daniel.haxx.se/blog/2026/03/21/bye-bye-rtmp/comment-page-1/#comment-27417)
* Matthias Hörmann on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27416)
* Matt on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27415)
* Dmitry on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27414)
* Oleg on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27413)
* Johannes Müller on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27412)
* Gürkan on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27411)
* No One Of Consequence on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27410)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27409)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

March 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| [9](https://daniel.haxx.se/blog/2026/03/09/) | [10](https://daniel.haxx.se/blog/2026/03/10/) | [11](https://daniel.haxx.se/blog/2026/03/11/) | [12](https://daniel.haxx.se/blog/2026/03/12/) | 13 | 14 | [15](https://daniel.haxx.se/blog/2026/03/15/) |
| 16 | 17 | 18 | 19 | 20 | [21](https://daniel.haxx.se/blog/2026/03/21/) | [22](https://daniel.haxx.se/blog/2026/03/22/) |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 |  | | | | |

[« Feb](https://daniel.haxx.se/blog/2026/02/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)