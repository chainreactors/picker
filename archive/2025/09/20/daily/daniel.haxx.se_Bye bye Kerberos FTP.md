---
title: Bye bye Kerberos FTP
url: https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/
source: daniel.haxx.se
date: 2025-09-20
fetch_date: 2025-10-02T20:26:01.526459
---

# Bye bye Kerberos FTP

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/09/Cerberus.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Bye bye Kerberos FTP

[September 19, 2025](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/#respond)

We are [dropping support](https://github.com/curl/curl/pull/18577) for this feature in curl 8.17.0. Kerberos5 FTP to be exact. The last Kerberos support we had for FTP.

## Badness

On September 16, 2025 we received [a security report](https://hackerone.com/reports/3341476) that accurately identified a possible stack based buffer overflow in the Kerberos FTP code that could allow a malicious FTP server cause havoc in curl.

Yikes. That is *bad*.

But wait, it also identified a second problem. In the exact same [commit](https://github.com/curl/curl/commit/0f4c439fc7347f499cf58299aae8ecb4f1bdf742) that introduced the potential security vulnerability (by me, no less) I also injected a second bug!

## A canary bug

This second bug effectively and completely broke the function and prevented Kerberos FTP from working. So no user would actually be vulnerable to the first problem because it simply never works anymore and no user would then use this against a malicious server!

At the time when I merged the commit this second bug was not detected because we obviously do not have tests and CI that test this piece of the code. It pains me to admit this, but we do have a few areas left in curl that aren’t covered by tests or enough tests.

I merged this bad code back in May 2024 and we have done over a year’s worth of releases since then and since not a single person has reported this breakage we can use this as a decent canary in the mine and safely conclude that not a single soul has used this feature in this time (with a recent curl install). If they did they didn’t tell us about it and I don’t count that.

## No users: no code

With this accidental/clever user check, we have then decided to instead of fixing the code we rip the entire thing out. Clearly we should not support this code since A) it isn’t used and B) it isn’t tested in the test suite. Perhaps also C) it is weird code.

Bye bye Kerberos5 FTP support. We introduced it back in [July 2007](https://github.com/curl/curl/commit/54967d2a3ab5559631407f7b7f67ef48c2dda6dd).

We had Kerberos4 support for FTP between September 2000 and August 2013.

As a follow-on effect, we also get rid of the last piece of code in the repository that were copyrighted “Kungliga Tekniska Högskolan” under a [BSD-3 license](https://opensource.org/license/bsd-3-clause). The only piece that was BSD-3 licensed. One less license to care about!

## Credits

The top image is a cropped version of [Cerberus and Heracles](https://en.wikipedia.org/wiki/Cerberus#/media/File:Hercules_and_Cerberus_LACMA_65.37.151.jpg). An etching by Antonio Tempesta (Florence, Italy, 1555–1630).

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[FTP](https://daniel.haxx.se/blog/tag/ftp/)

# Post navigation

[Previous PostFrom suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)[Next PostCRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)

### Leave a Reply [Cancel reply](/blog/2025/09/19/bye-bye-kerberos-ftp/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
15fourfive1

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

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

September 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| [8](https://daniel.haxx.se/blog/2025/09/08/) | [9](https://daniel.haxx.se/blog/2025/09/09/) | [10](https://daniel.haxx.se/blog/2025/09/10/) | 11 | 12 | [13](https://daniel.haxx.se/blog/2025/09/13/) | 14 |
| 15 | 16 | 17 | [18](https://daniel.haxx.se/blog/2025/09/18/) | [19](https://daniel.haxx.se/blog/2025/09/19/) | 20 | 21 |
| [22](https://daniel.haxx.se/blog/2025/09/22/) | 23 | 24 | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« Aug](https://daniel.haxx.se/blog/2025/08/)

[Oct »](https://daniel.haxx.se/blog/2025/10/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)