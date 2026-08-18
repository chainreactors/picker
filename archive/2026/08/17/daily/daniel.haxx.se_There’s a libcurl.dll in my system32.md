---
title: There’s a libcurl.dll in my system32
url: https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/
source: daniel.haxx.se
date: 2026-08-17
fetch_date: 2026-08-18T02:52:12.249170
---

# There’s a libcurl.dll in my system32

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/08/window-919333_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Windows](https://daniel.haxx.se/blog/category/tech/win/)

# There’s a libcurl.dll in my system32

[August 17, 2026](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/#respond)

This afternoon I had a meeting with IT people at a huge US power infrastructure company. They had found a `libcurl.dll` file in their `C:\Windows\System32` directory and asked us for help to upgrade it. Their vulnerability scanner identified it as vulnerable to several [publicly known vulnerabilities](https://curl.se/docs/security.html). *Can we bump it to the latest version please?*

No. We really cannot.

There are literally *thousands* of Windows applications that use libcurl. Many of them install a libcurl.dll file in your file system as part of their installation process and yes, some of them even put it in the system32 directory. They *can* optionally link with libcurl statically, which allows them to use the library and its API without using an external file. There are pros and cons with either method.

When libcurl is shipped as a separate DLL file, it is easily checked by for example vulnerability scanners and they may find that your Windows installation contains a libcurl version that contains known vulnerabilities. The system may even contain *many* separate libcurl installations, each potentially at different versions and containing a different set of vulnerabilities.

## Not part of Windows

[Microsoft ships curl as a bundled part of Windows](https://daniel.haxx.se/blog/2018/01/13/microsoft-curls-too/) since many years back, but they build with a *static* libcurl so they never ship any libcurl.dll file and therefore we know that the file does not originate from there. It is not part of the Windows installation. Something else installs it.

## We can’t fix those

Whoever built that exact libcurl.dll file needs to be the one who updates it. It is next to impossible for anyone else to know or figure out exactly how that file was built – and getting it wrong will most certainly crash the application or cause other odd and unpredictable behavior.

## Figure out who uses it

My advice: figure out which application that uses this DLL. With *tasklist* you can check which currently running application that uses a specific DLL, and I have been told there are tools that can scan executable files to find out which ones that use a specific DLL.

This is not something we can do.

## We can still help

We can help application makers with advice, education and tricks on how to build curl the best and most effective way. We can even build or ship curl for them. We are leading experts on curl, networks and transfers.

We also offer [long-term stable curl releases](https://rock-solid.curl.dev/) and we can do [backports of security fixes](https://curl.se/support.html) for any curl version of your choice.

*But we can’t runtime patch your Windows installation for you.*

(Yes, this problem is similar to the [deleting curl problem](https://daniel.haxx.se/blog/2023/04/24/deleting-system32curl-exe/).)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[windows](https://daniel.haxx.se/blog/tag/windows/)

# Post navigation

[Previous Postcurl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/)

### Leave a Reply [Cancel reply](/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
eighttwo31four

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [There’s a libcurl.dll in my system32](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/)
  August 17, 2026
* [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/)
  August 14, 2026
* [What the bliss taught us](https://daniel.haxx.se/blog/2026/08/03/what-the-bliss-taught-us/)
  August 3, 2026
* [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/)
  July 27, 2026
* [1,500 curl authors](https://daniel.haxx.se/blog/2026/07/25/1500-curl-authors/)
  July 25, 2026
* [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/)
  July 16, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27551)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27550)
* Nick on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27549)
* [Moritz Buhl](https://moritzbuhl.de) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27547)
* [Daniel Stenberg](https://daniel.haxx.se/) on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27545)
* Nun Your Beeswax Inc. on [HTTP Message Signatures with curl](https://daniel.haxx.se/blog/2026/07/27/http-message-signatures-with-curl/comment-page-1/#comment-27544)
* Matthias Hörmann on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27539)
* entronid on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27538)
* Willy on [Workshop Basel day three](https://daniel.haxx.se/blog/2026/07/16/workshop-basel-day-three/comment-page-1/#comment-27537)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Workshop Basel day one](https://daniel.haxx.se/blog/2026/07/14/workshop-basel-day-one/comment-page-1/#comment-27536)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

August 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| [3](https://daniel.haxx.se/blog/2026/08/03/) | 4 | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | [14](https://daniel.haxx.se/blog/2026/08/14/) | 15 | 16 |
| [17](https://daniel.haxx.se/blog/2026/08/17/) | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 31 |  | | | | | |

[« Jul](https://daniel.haxx.se/blog/2026/07/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)