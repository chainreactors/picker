---
title: curl 8.17.0
url: https://daniel.haxx.se/blog/2025/11/05/curl-8-17-0/
source: daniel.haxx.se
date: 2025-11-05
fetch_date: 2025-11-06T03:14:10.730315
---

# curl 8.17.0

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/11/curl-8.17.0.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.17.0

[November 5, 2025](https://daniel.haxx.se/blog/2025/11/05/curl-8-17-0/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2025/11/05/curl-8-17-0/#respond)

Download curl from [curl.se](https://curl.se/).

## Release presentation

## Numbers

the 271st release
11 changes
56 days (total: 10,092)
448 bugfixes (total: 12,537)
699 commits (total: 36,725)
2 new public libcurl function (total: 100)
0 new curl\_easy\_setopt() option (total: 308)
1 new curl command line option (total: 273)
69 contributors, 35 new (total: 3,534)
22 authors, 5 new (total: 1,415)
1 security fixes (total: 170)

## Security

[CVE-2025-10966](https://curl.se/docs/CVE-2025-10966.html): missing SFTP host verification with wolfSSH. curl’s code for managing SSH connections when SFTP was done using the wolfSSH powered backend was flawed and missed host verification mechanisms.

## Changes

We drop support for several things this time around:

* drop Heimdal support
* drop the winbuild build system
* drop support for Kerberos FTP
* drop support for wolfSSH

And then we did some other smaller changes:

* up the minimum libssh2 requirement to 1.9.0
* add a [notifications API](https://curl.se/libcurl/c/curl_multi_notify_enable.html) to the multi interface
* expand to use 6 characters per size in the progress meter
* support Apple SecTrust – use the native CA store
* add `[--knownhosts](https://curl.se/docs/manpage.html#--knownhosts)` to the command line tool
* [wcurl](https://curl.se/wcurl/): import v2025.11.04
* write-out: make `%header{}` able to output *all* occurrences of a header

## Bugfixes

We set a new project record this time with no less than [448 documented bugfixes](https://curl.se/ch/) since the previous release.

The release presentation mentioned above discusses some of the perhaps most significant ones.

## Coming next

There a small set of pull-requests waiting to get merged, but other than that our future is not set and we greatly appreciate your feedback, submitted issues and provided pull-requests to guide us.

If this release happens to include an annoying regression, there might be a patch release already next week. If we are lucky and it doesn’t, then we aim for a 8.18.0 release in the early January 2026.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous PostYes really, curl is still developed](https://daniel.haxx.se/blog/2025/11/04/yes-really-curl-is-still-developed/)

### Leave a Reply [Cancel reply](/blog/2025/11/05/curl-8-17-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
eight9fivefive7

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [curl 8.17.0](https://daniel.haxx.se/blog/2025/11/05/curl-8-17-0/)
  November 5, 2025
* [Yes really, curl is still developed](https://daniel.haxx.se/blog/2025/11/04/yes-really-curl-is-still-developed/)
  November 4, 2025
* [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/)
  October 25, 2025
* [On 110 operating systems](https://daniel.haxx.se/blog/2025/10/23/on-110-operating-systems/)
  October 23, 2025
* [AIxCC curl details](https://daniel.haxx.se/blog/2025/10/22/aixcc-curl-details/)
  October 22, 2025
* [A royal gold medal](https://daniel.haxx.se/blog/2025/10/21/a-royal-gold-medal/)
  October 21, 2025

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [AIxCC curl details](https://daniel.haxx.se/blog/2025/10/22/aixcc-curl-details/comment-page-1/#comment-27348)
* [Stephen Paulger](https://newspeak.org.uk) on [AIxCC curl details](https://daniel.haxx.se/blog/2025/10/22/aixcc-curl-details/comment-page-1/#comment-27347)
* Jesse on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27345)
* [Stefan Pejcic](https://pejcic.rs/) on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27344)
* Lorenz Klopfenstein on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27342)
* [Jonathan Hartley](https://tartley.com) on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27341)
* Pat on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27340)
* [Peter Krefting](http://www.softwolves.pp.se/cbm/) on [A gold ceremony to remember](https://daniel.haxx.se/blog/2025/10/25/a-gold-ceremony-to-remember/comment-page-1/#comment-27339)
* Fonzi on [A royal gold medal](https://daniel.haxx.se/blog/2025/10/21/a-royal-gold-medal/comment-page-1/#comment-27338)
* Roger on [A royal gold medal](https://daniel.haxx.se/blog/2025/10/21/a-royal-gold-medal/comment-page-1/#comment-27337)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

November 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | [4](https://daniel.haxx.se/blog/2025/11/04/) | [5](https://daniel.haxx.se/blog/2025/11/05/) | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 |

[« Oct](https://daniel.haxx.se/blog/2025/10/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)