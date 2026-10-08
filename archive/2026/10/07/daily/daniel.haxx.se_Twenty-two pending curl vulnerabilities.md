---
title: Twenty-two pending curl vulnerabilities
url: https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/
source: daniel.haxx.se
date: 2026-10-07
fetch_date: 2026-10-08T08:07:52.829807
---

# Twenty-two pending curl vulnerabilities

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/06/oops-sign-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Twenty-two pending curl vulnerabilities

[October 7, 2026](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/#respond)

On October 14 2026 we will ship curl 8.23.0. The next iteration in the never-ending series of version bumps from the [curl project](https://curl.se/).

We always think of the next release as the best version we ever did – and this time is no exception. Decades of collected experiences and meticulous polishing has lead us to this.

## Earlier than planned

We decided to shorten the release cycle this time, so that we can release 8.23.0 a few weeks earlier than what we originally planned. We took this decision after we received one particular vulnerability report that highlighted a rather significant flaw.

We will ship a new version with this problem removed, together with twenty-one other albeit less serious security vulnerabilities addressed.

## Severity HIGH

In the curl project we only assign one of the four different severity levels on all CVEs we report (LOW, MEDIUM, HIGH or CRITICAL), as we basically [don’t believe in CVSS scoring](https://daniel.haxx.se/blog/2025/01/23/cvss-is-dead-to-us/). We have only published two CVEs with severity HIGH since 2021, the most recent one being [CVE-2023-38545](https://curl.se/docs/CVE-2023-38545.html); that could lead to a heap buffer overflow.

Now we are about to release another one: CVE-2026-92392.

## All info will be revealed next week

All details about CVE-2026-92392 will become public in the European morning of October 14, 2026 in synchronization of the release of curl 8.23.0 which of course will have this problem fixed.

We will ship updated [Rock-solid curl](https://rock-solid.curl.dev/) versions in sync with this.

For the safety and security of curl users everywhere (and frankly, all the infrastructure that uses curl), no details of this flaw will be made public before this date.

We will alert the distros@openwall mailing list and paying curl support customers about this problem (and the associated fix) ahead of time.

I will follow-up with a separate blog post after October 14 to describe this flaw in detail. How it can be triggered, why it isn’t quite the end of the world and what we do in curl to fix this and similar classes of problems.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Post25 years on Apple computers](https://daniel.haxx.se/blog/2026/09/25/25-years-on-apple-computers/)

### Leave a Reply [Cancel reply](/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
oneonethree49

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Twenty-two pending curl vulnerabilities](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/)
  October 7, 2026
* [25 years on Apple computers](https://daniel.haxx.se/blog/2026/09/25/25-years-on-apple-computers/)
  September 25, 2026
* [curl 8.22.0](https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/)
  September 2, 2026
* [There’s a libcurl.dll in my system32](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/)
  August 17, 2026
* [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/)
  August 14, 2026
* [What the bliss taught us](https://daniel.haxx.se/blog/2026/08/03/what-the-bliss-taught-us/)
  August 3, 2026

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

October 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| 5 | 6 | [7](https://daniel.haxx.se/blog/2026/10/07/) | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

[« Sep](https://daniel.haxx.se/blog/2026/09/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)