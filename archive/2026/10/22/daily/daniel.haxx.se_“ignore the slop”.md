---
title: “ignore the slop”
url: https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/
source: daniel.haxx.se
date: 2026-10-22
fetch_date: 2026-10-23T06:45:06.286495
---

# “ignore the slop”

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/01/future-9045696-cropped.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# “ignore the slop”

[October 22, 2026](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/#comments)

Lots of people who are against the use of AI for all its ethical and inherent issues tell me this. *Just ignore it*. Don’t let *big AI* control us.

The “slop” they refer to is anything created that involved an AI, and in our case ([the curl project](https://curl.se/)) it is in particular vulnerability reports.

“Ignoring the slop” *cannot be done* and it doesn’t help. Vulnerability reports created with the help of AIs point out actual problems, and sometimes vulnerabilities. Ignoring real vulnerabilities because they were found by AI does not make users safe and secure. It makes them vulnerable. *We don’t want that*.

I personally don’t refer to this as *AI slop* because the reports are typically accurate and correct, even if much too wordy. I think “slop” implies that it is wrong, misleading or otherwise bad content.

One can certainly object to the use of AI, but when we get real vulnerabilities reported and proven, we cannot in good faith pretend they don’t exist just because we think the tech involved in digging them up is questionable. That would be a disservice to, or even betrayal of, our users.

We make curl secure for our users.

## Obligations

An Open Source project typically gives no guarantees at all, so there are no *legal* requirements that force us to fix flaws.

We are however a project with high goals of quality and stability and we would jeopardize our name and track record if we now would stop delivering on that. Also, a few of us involved in the project also sell curl related support and services, where at least part of that means providing *secure* curl releases, so we still have this *contractual obligation* to a set of customers. And they wouldn’t be customers in the fist place if the Open Source project didn’t already have the proven quality track record.

So no, we really cannot ignore vulnerability reports.

## The slop is gone

A sizeable portion of users seem to still believe we still suffer from a lot of made up and hallucinated reports by these AIs. We really don’t.

Almost all the stupidity and lies we saw in the vulnerability reports made by AIs in the past have ceased. Since spring 2026 the slop reports are practically gone. Our current challenge is much harder: [high volume, high quality](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/).

## AI talks too much

They always use too many words. Every report is now hundreds of lines and the explanations are convoluted and detailed (and often repeat themselves multiple times).

In a good report, the human writes a first paragraph explaining the problem *briefly* and then they submit the full report. It’s annoying when the reporter surrender everything to the AI, including the communication part.

The AIs are also still bad at figuring out exactly where the line is between a bug and a vulnerability, and if it is a vulnerability, what severity it is. This is not a surprise though, as this is also the case for human reporters.

A good trend is that they often produce good reproducers or proofs of concept helping to trigger and prove the problem/vulnerability. That was a really complicated part of the reporters’ work back in the day, now it’s just a prompt or two.

## Everything is with AI now

These days, like within the last few months, we have received hundreds of vulnerability reports submitted to curl and *every single one had AI involved to some extent*.

It is generally easy to tell on the language and the length and details of the report.

[AI](https://daniel.haxx.se/blog/tag/ai/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostDo minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/)

## One thought on ““ignore the slop””

1. ![](https://secure.gravatar.com/avatar/6d446c3138833e2143a1e5bf2f8ccdc7e13c82b4b71af2f8ad7b4e43ddc650af?s=34&d=monsterid&r=g) **Matthias Hörmann** says:

   [October 23, 2026 at 07:53](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/#comment-27566)

   To be fair to the AI the AI written stuff is not nearly as repetitive and full of inaccuracies as the posts by people who as anti AI and have based their entire opinion on its capabilities on the early models from a few years ago. I can’t help but think of it as Anti-AI slop sometimes.

   [Reply](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/?replytocom=27566#respond)

### Leave a Reply [Cancel reply](/blog/2026/10/22/ignore-the-slop/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
sixonetwoone4

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/)
  October 22, 2026
* [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/)
  October 20, 2026
* [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)
  October 15, 2026
* [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)
  October 14, 2026
* [A UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
  October 14, 2026
* [curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/)
  October 14, 2026

# Recent Comments

* Matthias Hörmann on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27566)
* Patrick T on [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/comment-page-1/#comment-27565)
* [Soufiane](https://www.easytutoriel.com) on [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/comment-page-1/#comment-27564)
* [Arthur Sathish](https://peeklaunch.com) on [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/comment-page-1/#comment-27563)
* [Daniel Stenberg](https://daniel.haxx.se/) on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27559)
* Jeremy Robst on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27558)
* [Daniel Stenberg](https://daniel.haxx.se/) on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27556)
* Andrei on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27555)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27551)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl performance](https://daniel.haxx.se/blog/2026/08/14/curl-performance-2/comment-page-1/#comment-27550)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp...