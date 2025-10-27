---
title: preparing for the worst
url: https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/
source: daniel.haxx.se
date: 2025-09-10
fetch_date: 2025-10-02T19:54:25.080078
---

# preparing for the worst

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/09/car-accident.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# preparing for the worst

[September 9, 2025](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/#comments)

One of these mantras I keep repeating is how we in the curl project keep improving, keep polishing and keep tightening every bolt there is. No one can do everything right from day one, but given time and will we can over time get a lot of things lined up in neat and tidy lines.

And yet new things creep up all the time that can be improved and taken yet a little further.

## An exercise

Back in the spring of 2025 we had an exercise at our curl up meeting in Prague. Jim Fuller played up an imaginary life-like scenario for a bunch of curl maintainers. In this role played *major incident* we got to consider how we would behave and what we would do in the curl project if something like Heartbleed or a serious breach occur.

It was a little of an eye opener for several of us. We realized we should probably get some more details written down and planned for.

## Plan ahead

We of course arrange for things and work on procedures and practices to the best of our abilities to make sure that there will never be any such *major incident* in the curl project. However, as we are all human and we all do mistakes, it would be foolish to think that we are somehow immune against incidents of the highest possible severity level. Rationally, we should just accept the fact that even though the risk is ideally really slim, it exists. It *could* happen.

## What if the big bad happens

We have now [documented some guidelines](https://curl.se/dev/vuln-disclosure.html#curl-major-incident-response) about what exactly constitutes a *major incident*, how it is declared, some roles we need to shoulder while it is ongoing, with a focus on both internal and external communication, and how we declare that the incident has ended. It’s straight forward and quite simple.

Feel free to criticize or improve those if you find omissions or mistakes. I imagine that if we ever get to actually use these documented steps because of such a project-shaking event, we will get reasons to improve it. Until then we just need to apply our imagination and make sure it seems reasonable.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Postgiants, standing on the shoulders of](https://daniel.haxx.se/blog/2025/09/08/giants-standing-on-the-shoulders-of/)[Next Postcurl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)

## One thought on “preparing for the worst”

1. ![](https://secure.gravatar.com/avatar/02aded8d36f62437a99c9b4737cc2af554c4ce4105099b429c05b65caeb70f76?s=34&d=monsterid&r=g) **[Fazal Majid](https://majid.info/)** says:

   [September 13, 2025 at 21:29](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/#comment-27321)

   The plan is sound, but the biggest optimization would be to have some real-time notification mechanism like Signal, SMS, or WhatsApp to warn the downstream distro package maintainers when a major incident is declared so it percolates quickly.

   I’m assuming you already have such a list, if not, it might be worth collecting the contact numbers.

   [Reply](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/?replytocom=27321#respond)

### Leave a Reply [Cancel reply](/blog/2025/09/09/preparing-for-the-worst/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
ninenineseven5one

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