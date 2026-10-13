---
title: The 2026 curl team
url: https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/
source: daniel.haxx.se
date: 2026-10-12
fetch_date: 2026-10-13T08:37:26.398299
---

# The 2026 curl team

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/01/kids-team-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# The 2026 curl team

[October 12, 2026](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/#comments)

The curl security team happens to also double as the curl core team. The small group of people who assess security reports and take project decisions.

The exact set of participants in this team of course vary over time, as this is a volunteer membership role without monetary compensation.

I decided to write this blog post to help show the light on some of my fellow curl maintainers. I think I often get too much credit and that curl is frequently called a one man show. It really is not and it has not been exclusively *my project* for many years. We are a team behind this.

As of October 2026 we are six humans in this team. Me and five fellow maintainers. curl would not have been close to what it is today without this team. These are the peeps I turn to first for everything hard, complicated or tough in the curl project when they need to be done in private first. In all other cases, public communication is preferred.

## The team

(alphabetical order, excluding myself)

**Max Dymond**. Max made his first commit in the source repository over nine years ago. He has otherwise made perhaps the biggest impact with his fierce work on the [curl fuzzers](https://github.com/curl/curl-fuzzer) and dealing with fall-outs from [OSS-Fuzz](https://google.github.io/oss-fuzz/). Having excellent fuzzing significantly contributes to us writing better code.

**Stefan Eissing**. Having authored his first curl commit just five years ago, Stefan currently has his name on more lines of code when doing git blame on production code than any other individual, including myself. Introduced the pytest test suite in curl. Master of all things HTTP. Productive like few.

**Dan Fandrich**. Made his first recorded curl commit *twenty-two* years ago. He has been involved with everything and everywhere in curl. In recent years perhaps most emphasized in test infrastructure as he made the test suite run parallelized a few years ago. He also wrote and admins [Test Clutch](https://testclutch.curl.se/), which helps us monitor CI test results.

**James Fuller**. Has been involved with curl for more than eight years. James focuses on security and is our own master of CVE reservations. Primary maintainer of [curl-container](https://github.com/curl/curl-container) – images for Docker and others.

**Viktor Szakats**. Having authored his first curl commit twelve years ago he is now the second most commit author in the project. Lead maintainer of [curl-for-win](https://github.com/curl/curl-for-win) which creates reproducible, static, curl binaries for Linux, macOS and Windows. Viktor is the unparalleled champion of our build and CI systems but shows up everywhere. Apparently he never sleeps.

## Invite-only

This group is invite-only and there is no documented set of requirements. You need a proven and established presence in the project, combined with a excellent knowledge of Open Source, protocols, networking and the curl project itself. Once you do, you might get invited to join. Not everyone accepts the invite when extended, and that is perfectly fine. It’s a lot of mostly thankless work without a paycheck.

## The rest

1,545 people have authored at least one commit in curl. A typical year, more than 150 individuals author commits and at least ten people author more than 10 commits each. People come and go over time. Here’s a list of [the top-100 authors](https://curl.se/gitstats/authors.html).

Everything that improves curl is welcome and takes us forward. Even bug reports and mere suggestions on the mailing list can help us figure out things or improve features in ways previously not considered.

More than 3,800 people are named in the [THANKS](https://curl.se/docs/thanks.html) file because they helped us out, one way or another.

curl is a team effort. A giant team.

## Steering the herd

Our job in the core team remains to steer the direction, to enforce boundaries, to lead by example (in addition to wade through an avalanche of vulnerability reports). To guide contributors, to review changes and try to make it even easier for more people to contribute.

Keeping top-notch quality while allowing and introducing newcomers.

Welcome!

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Open Source](https://daniel.haxx.se/blog/tag/open-source/)

# Post navigation

[Previous PostTwenty-two pending curl vulnerabilities](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/)[Next PostA slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)

## 2 thoughts on “The 2026 curl team”

1. ![](https://secure.gravatar.com/avatar/2febfa66539965bfc1ed9e5285062e85b2e2246ad3d375f074459f77ea06b6a6?s=34&d=monsterid&r=g) **Andrei** says:

   [October 12, 2026 at 19:05](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/#comment-27555)

   Is the announcement of Daniel Gustafsson’s stepping down from the security team so close to this post being published a coincidence?

   How many people are former members of the curl core team?

   [Reply](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/?replytocom=27555#respond)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [October 12, 2026 at 22:29](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/#comment-27556)

      No, Daniel stepping down served as a reminder for me that I really should highlight and celebrate my fellow team members better. It triggered me to write this blog post.

      The team has had two other members in the past, no longer part of it: Daniel Gustafsson and Kamil Dudka.

      [Reply](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/?replytocom=27556#respond)

### Leave a Reply [Cancel reply](/blog/2026/10/12/the-2026-curl-team/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
1nine2two5

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/)
  October 13, 2026
* [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/)
  October 12, 2026
* [Twenty-two pending curl vulnerabilities](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/)
  October 7, 2026
* [25 years on Apple computers](https://daniel.haxx.se/blog/2026/09/25/25-years-on-apple-computers/)
  September 25, 2026
* [curl 8.22.0](https://daniel.haxx.se/blog/2026/09/02/curl-8-22-0/)
  September 2, 2026
* [There’s a libcurl.dll in my system32](https://daniel.haxx.se/blog/2026/08/17/theres-a-libcurl-dll-in-my-system32/)
  August 17, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/comment-page-1/#comment-27556)
* Andrei on [The 2026 curl team](https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/...