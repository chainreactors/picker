---
title: 1k-0036 means sad eyeballs on my LG
url: https://daniel.haxx.se/blog/2025/05/13/1k-0036-means-sad-eyeballs-on-my-lg/
source: daniel.haxx.se
date: 2025-05-14
fetch_date: 2025-10-06T22:29:16.329666
---

# 1k-0036 means sad eyeballs on my LG

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

[Network](https://daniel.haxx.se/blog/category/tech/net/), [Technology](https://daniel.haxx.se/blog/category/tech/)

# 1k-0036 means sad eyeballs on my LG

[May 13, 2025](https://daniel.haxx.se/blog/2025/05/13/1k-0036-means-sad-eyeballs-on-my-lg/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

For a to me unknown reason IPv6 connectivity has been failing to my home the last few days. When I try to curl curl.se I get to see a lot of IPv6 related failures and instead it connects to and uses one of the IPv4 addresses.

IPv6 has been working fine for me non-stop for the last few years before this. I suspect there is something on the ISP side and they are doing some planned maintenance in a few days that might change things. It’s not a big deal, everything I do on my machine just magically and transparently adapts.

## Enter the TV

In my living room my family has an LG TV from a few years back. I find it pretty neat. It runs WebOS and has a bunch of streaming apps installed. Our household currently streams shows from Netflix, Disney, Max and SVT Play (The Swedish national broadcasting) on it.

What do you think happens to the TV and its apps when IPv6 does not work although hosts still resolve to a bunch of IPv6 + IPv4 addresses?

The TV OS itself, installing apps and everything works exactly as always.

Netflix: no difference. Streams as nicely and cleanly as always. SVT Play: runs perfectly.

Disney’s app gets stuck showing a rotating progress bar that never ends. Horribly user hostile.

The Max app fires up and allows me to select a media to watch, and then after I press play it sits showing the progress bar for a while until it fails with this `1k-0036` error.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/LGTV-problem-ipv6.jpg)

The original Swedish error. My TV is set to Swedish.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/LGTV-problem-ipv6-en.jpg)

The translated to English version just to keep everyone in the loop.

## On a computer

Trying their services using the same account on the same network but from a computer in a browser showed no problems at all.

## Tracking down the problem

The Max customer service advice on how to fix this of course started out with the standard most predictable actions:

1. Unplug your device, keep it off for ten seconds and then start it again.
2. The exact same procedure with your router.

Not a word or attempt to explain what the error code actually means. But then when I told the support person that these tricks did not help, they instead asked me to **disable IPv6** in the TV’s network settings.

Even though I already knew I had this glitch for the moment with IPv6, it was first when I read his advise that I actually connected the two issues. To me, the problems were so unlikely to be related that I had not even considered it!

So now we know what 1k-0036 means.

## Bye bye IPv6 TV

And yeps it was quickly confirmed: disabling IPv6 in the network settings for the TV now made streaming with the Max app work again. And yes, with the Disney app as well.

I was mildly negatively surprised that these two highly popular streaming apps actually do not handle happy eyeballs and selecting between IP address families better. Rather lame.

While we know curl is part of WebOS this clearly hints that it is not used for streaming using these services at least. (Because curl has supported happy eyeballs for decades already and clearly has no problem to connect to a host just because IPv6 glitches.) Not that surprising really. We already know that Netflix for example also use curl in their app but only for most things around and not the actual media stream.

Disabling IPv6 on the TV config comes with basically no downside so I will probably just leave it off now.

[Network](https://daniel.haxx.se/blog/tag/network/)[Technology](https://daniel.haxx.se/blog/tag/technology/)[TV](https://daniel.haxx.se/blog/tag/tv/)

# Post navigation

[Previous Postcurl up 2025 is over](https://daniel.haxx.se/blog/2025/05/06/curl-up-2025-is-over/)[Next PostSupported curl versions and end of life](https://daniel.haxx.se/blog/2025/05/14/supported-curl-versions-and-end-of-life/)

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

May 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | [6](https://daniel.haxx.se/blog/2025/05/06/) | 7 | 8 | 9 | 10 | 11 |
| 12 | [13](https://daniel.haxx.se/blog/2025/05/13/) | [14](https://daniel.haxx.se/blog/2025/05/14/) | 15 | [16](https://daniel.haxx.se/blog/2025/05/16/) | 17 | 18 |
| [19](https://daniel.haxx.se/blog/2025/05/19/) | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | [28](https://daniel.haxx.se/blog/2025/05/28/) | [29](https://daniel.haxx.se/blog/2025/05/29/) | 30 | 31 |  |

[« Apr](https://daniel.haxx.se/blog/2025/04/)

[Jun »](https://daniel.haxx.se/blog/2025/06/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()