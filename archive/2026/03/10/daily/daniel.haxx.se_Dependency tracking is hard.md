---
title: Dependency tracking is hard
url: https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/
source: daniel.haxx.se
date: 2026-03-10
fetch_date: 2026-03-11T04:03:43.442546
---

# Dependency tracking is hard

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/07/sardines-on-shelves-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Dependency tracking is hard

[March 10, 2026](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/#comments)

curl and libcurl are written in C. Rather low level components present in many software systems.

They are typically not part of any *ecosystem* at all. They’re just a tool and a library.

In lots of places on the web when you mention an Open Source project, you will also get the option to mention in which ecosystem it belongs. npm, go, rust, python etc. There are easily at least a dozen well-known and large ecosystems. curl is not part of any of those.

Recently there’s been a push for PURLs ([Package URLs](https://github.com/package-url/purl-spec)), for example when describing your specific package in a CVE. A package URL only works when the component is part of an ecosystem. curl is not. We can’t specify curl or libcurl using a PURL.

SBOM generators and related scanners use package managers to generate lists of used components *and their dependencies*. This makes these tools quite frequently just miss and ignore libcurl. It’s not listed by the package managers. It’s just in there, ready to be used. Like magic.

It is similarly hard for these tools to figure out that curl in turn also depends and uses other libraries. At build-time you select which – but as we in the curl project primarily just ships tarballs with source code we cannot tell anyone what dependencies their builds have. The additional libraries libcurl itself uses are all similarly outside of the standard ecosystems.

Part of the explanation for this is also that libcurl and curl are often shipped bundled with the operating system many times, or sometimes *perceived* to be part of the OS.

Most graphs, SBOM tools and dependency trackers therefore stop at the binding or system that uses curl or libcurl, but without including curl or libcurl. The layer above so to speak. This makes it hard to figure out exactly how many components and how much software is depending on libcurl.

A perfect way to illustrate the problem is to check GitHub and see how many among its vast collection of many millions of repositories that depend on curl. After all, curl is installed in some thirty billion installations, so clearly it used *a lot*. (Most of them being libcurl of course.)

It lists *one* dependency for curl.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/03/github-depdencies.png)

Repositories that depend on curl/curl: one. Screenshot taken on March 9, 2026

What makes this even more amusing is that it looks like this single dependent repository ([Pupibent/spire](https://github.com/Pupibent/spire)) lists curl as a dependency by mistake.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[github](https://daniel.haxx.se/blog/tag/github/)

# Post navigation

[Previous Post10K curl downloads per year](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/)

## 2 thoughts on “Dependency tracking is hard”

1. ![](https://secure.gravatar.com/avatar/5c15d18f75daf96c7ecbe67c820ada35d7dcbbb504e7d1555419f759902972f7?s=34&d=monsterid&r=g) **Gürkan** says:

   [March 10, 2026 at 11:54](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/#comment-27411)

   <https://github.com/Pupibent/spire/blob/0a6bfb1b569e308234428a76f95e3c912ca537db/go.mod#L8>

   🙂

   [Reply](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/?replytocom=27411#respond)
2. ![](https://secure.gravatar.com/avatar/a924d4816fad3f42570d58df48870205b263393ce1c97507dfe95fcae0faae6c?s=34&d=monsterid&r=g) **Johannes Müller** says:

   [March 10, 2026 at 14:33](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/#comment-27412)

   `go.mod` files with random inaccurate dependencies in random repositories seems to be a thing.
   This monstrosity is the only file in this repo, for example: <https://github.com/flushedface/look-at-my-profile/blob/master/go.mod>

   [Reply](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/?replytocom=27412#respond)

### Leave a Reply [Cancel reply](/blog/2026/03/10/dependency-tracking-is-hard/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
3three8five9

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/)
  March 10, 2026
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

# Recent Comments

* Johannes Müller on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27412)
* Gürkan on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27411)
* No One Of Consequence on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27410)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27409)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27408)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27407)
* Aaron Dewes on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27406)
* mw on [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/comment-page-1/#comment-27405)
* Jesse on [A third medal](https://daniel.haxx.se/blog/2026/02/02/a-third-medal/comment-page-1/#comment-27403)
* [Lawrence Li](https://lawrenceli.me) on [GregKH awarded the Prize for Excellence in Open Source 2026](https://daniel.haxx.se/blog/2026/01/30/gregkh-awarded-the-prize-for-excellence-in-open-source-2026/comment-page-1/#comment-27401)

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
| [9](https://daniel.haxx.se/blog/2026/03/09/) | [10](https://daniel.haxx.se/blog/2026/...