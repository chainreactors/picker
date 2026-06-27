---
title: A curl mountain movie
url: https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/
source: daniel.haxx.se
date: 2026-06-26
fetch_date: 2026-06-27T05:50:41.319436
---

# A curl mountain movie

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/10/daniel-mountain.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# A curl mountain movie

[June 26, 2026](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [3 Comments](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/#comments)

One of my favorite visuals for known vulnerabilities in curl is *the mountain*. It shows how many currently known vulnerabilities were present in the code through-out curl’s history.

In the end of June 2026 it looks like this:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/06/Screenshot-2026-06-26-at-11-48-10-curl-Project-status-dashboard.png)

Over time we get more vulnerabilities reported. Since every flaw has a version range during which the problem existed and with more issues that have overlapping version ranges, the mountain grows. It changes shape every time we do a release or we publish a new vulnerability.

At this moment in time, [curl version 7.34.0](https://curl.se/ch/7.34.0.html) is the release that contains the most number of known vulnerabilities: [101](https://curl.se/docs/vuln-7.34.0.html). The worst one ever if you will. Out of a total of 206.

The mountain uses different colors for different severity levels of the published vulnerabilities, as the legend in the top-left of the image explains.

To illustrate the ever-changing nature of the shape and size, I wrote a script that renders *the mountain* the way it looked at specific dates in the past up until today. More specifically, the script renders one image for every month since curl started (March 1998). I then turned these 340 individual images into a little movie that shows how it grew into today’s shape. At four months/second.

The data for this come from [vuln.pm](https://github.com/curl/curl-www/blob/master/docs/vuln.pm) and the [curl git repository](https://github.com/curl/curl). The graph rendering is based on the [dashboard scripts](https://github.com/curl/stats/). All images put into a movie with ffmpeg of course.

## The 2016 drop

Several people have asked what happened in 2016 that caused the notable drop. A slope if you will.

If we zoom in on that, we can spot that [curl 7.51.0](https://curl.se/ch/7.51.0.html) has eleven fewer vulnerabilities than the version before that. This release was the first one after the 2016 [Cure53 code audit](https://daniel.haxx.se/blog/2016/11/23/curl-security-audit/), but other than that there is no clear distinct process or obvious code changes that explain this trend shift.

Lots of other graphs show just the ordinary pace and growth in various project areas. It was still fairly early days CI-wise but had been running at least a few CI jobs per commit for a few years already by then.

curl was adopted into the OSS-Fuzz project in July 2017, which since then makes us find some issues better, but the drop looks like it happened before then.

We had already been analyzing the code regularly on Coverity since a few years.

Better tooling? New compiler options? We simply don’t know.

## Future

As we keep announcing more vulnerabilities going forward, things will continue to change. Maybe I will come back and make another movie in five years?

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[movies](https://daniel.haxx.se/blog/tag/movies/)

# Post navigation

[Previous PostTrailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/)

## 3 thoughts on “A curl mountain movie”

1. ![](https://secure.gravatar.com/avatar/18f4f7ebdcd48383951a52a88f401bd6460ae74b626016010b1f0604cac90826?s=34&d=monsterid&r=g) **[Jonathan Desrosiers](https://jonathandesrosiers.com)** says:

   [June 26, 2026 at 13:52](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/#comment-27523)

   Very interesting way to chart the data!

   With so many past versions of curl, I’m curious how you go about determining which versions contain a specific vulnerability. Especially when the affected code in newer versions diverges from previous ones.

   [Reply](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/?replytocom=27523#respond)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [June 26, 2026 at 13:57](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/#comment-27524)

      We spend a significant effort researching every specific vulnerability which includes going back in history to find the exact commit that introduced the flaw. So we know exactly in which versions and over which time periods every single problem were shipped in releases.

      [Reply](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/?replytocom=27524#respond)
2. ![](https://secure.gravatar.com/avatar/67581f121f68072418299f07ebc200e3e7e16144be43dff14503338a9e301faa?s=34&d=monsterid&r=g) **[Jan Tångring](https://etn.se/)** says:

   [June 26, 2026 at 14:47](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/#comment-27525)

   That picture is [xkcd.com/2347](https://xkcd.com/2347/)

   That’s Daniel supporting the all modern digital infrastructure mountain

   [Reply](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/?replytocom=27525#respond)

### Leave a Reply [Cancel reply](/blog/2026/06/26/a-curl-mountain-movie/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
nine1four45

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/)
  June 26, 2026
* [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/)
  June 25, 2026
* [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)
  June 24, 2026
* [curl 8.21.0](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/)
  June 24, 2026
* [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/)
  June 21, 2026
* [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)
  June 15, 2026

# Recent Comments

* [Jan Tångring](https://etn.se/) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#comment-27525)
* [Daniel Stenberg](https://daniel.haxx.se/) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#comment-27524)
* [Jonathan Desrosiers](https://jonathandesrosiers.com) on [A curl mountain movie](https://daniel.haxx.se/blog/2026/06/26/a-curl-mountain-movie/comment-page-1/#comment-27523)
* Matthias Hörmann on [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/comment-page-1/#comment-27522)
* Paul Ducklin on [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/comment-page-1/#comment-27521)
* WC on [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/comment-page-1/#comment-27520)
* [Daniel Stenberg](https://daniel.haxx.se/) on [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/comment-page-1/#comment-27519)
* [Martijn](https://martijnv.com/) on [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/tra...