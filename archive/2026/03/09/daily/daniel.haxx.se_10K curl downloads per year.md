---
title: 10K curl downloads per year
url: https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/
source: daniel.haxx.se
date: 2026-03-09
fetch_date: 2026-03-10T04:02:34.338163
---

# 10K curl downloads per year

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/12/Paris_Tuileries_Garden_Facepalm_statue-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# 10K curl downloads per year

[March 9, 2026](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/#respond)

The Linux Foundation, the organization that we want to love but that so often makes that a hard bargain, has created something they call “Insights” where they gather lots of metrics on Open Source projects.

I held back so I never blogged and taunted OpenSSF for their [scorecard](https://scorecard.dev/) attempts that were always lame and misguided. This [Insights](https://insights.linuxfoundation.org/) thing looks like their next attempt to “grade” and “rate” Open Source. It is so flawed and full of questionable details that I decided there is no point in me listing them all in a blog post – it would just be too long and boring. Instead I will just focus on a single metric. The one that made me laugh out load when I saw it.

## Package downloads

They claim curl was downloaded 10,467 times the last year. ([source](https://insights.linuxfoundation.org/project/curl/repository/curl-curl/popularity?timeRange=past365days&start=2025-03-09&end=2026-03-09&widget=package-downloads))

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/03/Screenshot-2026-03-09-at-23-14-36-Curl-curl-curl-Repository-popularity-LFX-Insights.png)

Number of curl downloads the last 365 days according to Linux Foundation

What does “a download” mean? They refer to statistics from [ecosyste.ms](https://ecosyste.ms/), which is an awesome site and service, but it has absolutely no idea about curl downloads.

How often is curl “downloaded”?

curl release tarballs are downloaded from curl.se at a rate of roughly 250,000 / month.

curl images are currently pulled from docker at a rate of around 400,000 – 700,000 / day. curl is pulled from quay.io at roughly the same rate.

curl’s git repository is cloned roughly 32,000 times / day

curl is installed from Linux and BSD distributions at an unknown rate.

curl, in the form of libcurl, is bundled in countless applications, games, devices, cars, TVs, printers and services, and we cannot even guess how often it is downloaded as such an embedded component.

curl is installed by default on every Windows and macOS system since many years back.

But no, 10,467 they say.

# Post navigation

[Previous Postcurl up 2026](https://daniel.haxx.se/blog/2026/02/26/curl-up-2026/)

### Leave a Reply [Cancel reply](/blog/2026/03/09/10k-curl-downloads-per-year/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
five7four1eight

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [10K curl downloads per year](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/)
  March 9, 2026
* [curl up 2026](https://daniel.haxx.se/blog/2026/02/26/curl-up-2026/)
  February 26, 2026
* [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/)
  February 25, 2026
* [decomplexification continued](https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/)
  February 24, 2026
* [Open Source security in spite of AI](https://daniel.haxx.se/blog/2026/02/03/open-source-security-in-spite-of-ai/)
  February 3, 2026
* [A third medal](https://daniel.haxx.se/blog/2026/02/02/a-third-medal/)
  February 2, 2026

# Recent Comments

* No One Of Consequence on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27410)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27409)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27408)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27407)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27406)
* mw on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27405)
* Jesse on [A third medal](https://daniel.haxx.se/blog/2026/02/02/a-third-medal/comment-page-1/#comment-27403)
* [Lawrence Li](https://lawrenceli.me) on [GregKH awarded the Prize for Excellence in Open Source 2026](https://daniel.haxx.se/blog/2026/01/30/gregkh-awarded-the-prize-for-excellence-in-open-source-2026/comment-page-1/#comment-27401)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl distro meeting 2026](https://daniel.haxx.se/blog/2026/01/28/curl-distro-meeting-2026/comment-page-1/#comment-27398)
* [Anatolij Vasilev](https://r0.fyi/) on [curl distro meeting 2026](https://daniel.haxx.se/blog/2026/01/28/curl-distro-meeting-2026/comment-page-1/#comment-27397)

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
| [9](https://daniel.haxx.se/blog/2026/03/09/) | 10 | 11 | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 |  | | | | |

[« Feb](https://daniel.haxx.se/blog/2026/02/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()