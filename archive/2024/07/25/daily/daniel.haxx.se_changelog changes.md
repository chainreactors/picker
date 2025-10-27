---
title: changelog changes
url: https://daniel.haxx.se/blog/2024/07/24/changelog-changes/
source: daniel.haxx.se
date: 2024-07-25
fetch_date: 2025-10-06T17:43:22.204165
---

# changelog changes

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/04/good_curl_logo-672x372.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# changelog changes

[July 24, 2024](https://daniel.haxx.se/blog/2024/07/24/changelog-changes/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

On the curl website we of course list exactly what changes that go into each and every single release we do. In recent years I have even gone back and made sure we provide this information for every single release ever done. At the moment that means 258 releases, listing over 10,000 bugfixes and almost 1,000 changes. From 1996 until today.

This is literally a wall of changes.

Since we keep doing somewhere between 150 and 250 bugfixes per release and we do a new release very eight weeks, the page with all changes these keeps growing quite fast.

Right now, the HTML of this page is at 1.1 megabytes.

## Use case

Most typically I think the use case for users visiting the changelog is to view what changes that were done in one specific curl release. Possibly checking out a few different ones. Very few users actually want tens of thousands of lines of text to scroll through. I believe.

## Enter single release changelogs

To make sure that people can read the changes for a single release only, and to reduce the amount of data a user needs to download in order to view those single release changes, I worked on a setup that generates separate individual changelog pages for every release. Easy to bookmark, load fast, contain only information about the specific releases and they make it easy to skip back and forth between past and future releases.

I deployed these changes today and if you go to <https://curl.se/ch/> now, you will see the changelog for the most recent release only.

## The all changes changelog remains

The [changelog showing everything](https://curl.se/changes.html) will remain and is still an option to browse. I personally use it at times when I want to control-f and look for a change done in a previous curl version that I cannot remember exactly which. This all-changes page remains only a click away if you rather view that one instead of the single-version thing.

## Design

I am not a web developer and I am not web designer. I know just enough HTML and CSS to be able to publish these things, but I do not do fancy and I am fully aware that I am not good at making “nice” or “attractive” designs. I focus on *usable* and *practical*.

As per curl website standards these pages are all static content using no JavaScript and only a few small images. Excellent for rendering fast and for caching well in the CDN.

## Known vulnerabilities

I did not especially mention this before, but only a few days ago I added direct links from each version header to the page for *known vulnerabilities* for that specific version and that link of course is now also present in the single version changelog page. Next to the link that goes directly to the release presentation video.

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/07/Screenshot-2024-07-24-at-14-09-16-curl-Changes-in-8.8.0.png)

Screenshot of the changelog page for curl 8.8.0

## Feedback?

If you find problems or have ideas on how to further improve the curl website, [let us know](https://github.com/curl/curl-www/issues)!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Web](https://daniel.haxx.se/blog/tag/web/)

# Post navigation

[Previous Postcurl 8.9.0](https://daniel.haxx.se/blog/2024/07/24/curl-8-9-0/)[Next Postcurl 8.9.1](https://daniel.haxx.se/blog/2024/07/31/curl-8-9-1/)

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

July 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | [3](https://daniel.haxx.se/blog/2024/07/03/) | 4 | [5](https://daniel.haxx.se/blog/2024/07/05/) | 6 | 7 |
| 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| 22 | 23 | [24](https://daniel.haxx.se/blog/2024/07/24/) | 25 | 26 | 27 | 28 |
| 29 | 30 | [31](https://daniel.haxx.se/blog/2024/07/31/) |  | | | |

[« Jun](https://daniel.haxx.se/blog/2024/06/)

[Aug »](https://daniel.haxx.se/blog/2024/08/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)

![]()

![]()