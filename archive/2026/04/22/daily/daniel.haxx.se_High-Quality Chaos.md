---
title: High-Quality Chaos
url: https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/
source: daniel.haxx.se
date: 2026-04-22
fetch_date: 2026-04-23T04:43:45.515766
---

# High-Quality Chaos

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Screenshot-2026-04-22-at-13-38-54-Open-Source-AI-reality-Foss-north-2026-Google-Slides.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# High-Quality Chaos

[April 22, 2026](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/#comments)

As I have been preparing slides for my coming talk at foss-north on April 28, 2026 I figured I could take the opportunity and share a glimpse of the current reality here on my blog. The *high quality chaos* era, as I call it.

## No more AI slop

I complained and I complained about the high frequency junk submissions to the curl bug-bounty that grew really intense during 2025 and early 2026. To the degree that we [shut it down completely](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) on February 1st this year. At the time we speculated if that would be sufficient or if the flood would go on.

Now we know.

## Higher volume, higher quality

In March 2026, the curl project went [back to Hackerone](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/) again once we had figured out that GitHub was not good enough.

From that day, the nature of the security report submissions have changed.

The slop situation is not a problem anymore.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Open-Source-AI-reality-Foss-north-20264.jpg)

**AI slop rate**

The report frequency is higher than ever. Recently it’s been about double the rate we had through 2025, which already was more than double from previous years.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Open-Source-AI-reality-Foss-north-20261.jpg)

**Number of hours between security reports**

The quality is higher. The rate of confirmed vulnerabilities is back to and even surpassing the 2024 pre-AI level, meaning somewhere in the 15-16% range.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Open-Source-AI-reality-Foss-north-20262.jpg)

**Confirmed vulnerability rate**

In addition to that, the share of reports that identify a bug, meaning that they aren’t vulnerabilities but still some kind of problem, is significantly higher than before.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Open-Source-AI-reality-Foss-north-20263.jpg)

**Share of reports that were bugs, not vulnerabilities**

## Everything is AI now

Almost every security report now uses AI to various degrees. You can tell by the way they are worded, how the report is phrased and also by the fact that they now easily get very detailed duplicates in ways that can’t be done had they been written by humans.

The difference now compared to before however, is that they are mostly very high quality.

The reporters rarely mention exactly which AI tool or model they used (and really, we don’t care), but the evidence is strong that they used such help.

## We are not unique

I did a quick unscientific poll on Mastodon to see if other Open Source projects see the same trends and man, do they! Friends from the following projects confirmed that they too see this trend. Of course the exact numbers and volumes vary, but it shows its not unique to any specific project.

Apache httpd, BIND, curl, Django, Elasticsearch Python client, Firefox, git, glibc, GnuTLS, GStreamer, Haproxy, Immich, libssh, libtiff, Linux kernel, OpenLDAP, PowerDNS, python, Prometheus, Ruby, Sequoia PGP, strongSwan, Temporal, Unbound, urllib3, Vikunja, Wireshark, wolfSSL, …

I bet this list of projects is just a random selection that just happened to see my question. You will find many more experiencing and confirming this reality view.

## An explosion

When we ship curl 8.20.0 in the middle of next week – end of April 2026, we expect to announce at least six new vulnerabilities. Assuming that the trend keeps up for at least the rest of the year, and I think that is a fair assumption, we are looking at an estimated explosion and a record amount of CVEs to be published by the curl project this year.

We might publish closer to 50 curl vulnerabilities in 2026.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Open-Source-AI-reality-Foss-north-20265.jpg)

**Number of published vulnerabilities**

Given this universal trend, I cannot see how this pattern can not also be spotted and expected to happen in many other projects as well.

## Where does it end?

The tools are still improving. We keep adding flaws when we do bugfixes and add new features.

Someone has suggested it might work as with fuzzing, that we will see a plateau within a few years. I suppose we just have to see how it goes.

This avalanche is going to make maintainer overload even worse. Some projects will have a hard time to handle this kind of backlog expansion without any added maintainers to help.

It is probably a good time for the bad guys who can easily find this many problems themselves by just using the same tools, before all the projects get time, manpower and energy to fix them.

Then everyone needs to update to the newly released *fixed* versions of all packages, which we know is likely to take an even longer time.

We are up for a bumpy ride.

[AI](https://daniel.haxx.se/blog/tag/ai/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[CVE](https://daniel.haxx.se/blog/tag/cve/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostDon’t trust, verify](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/)

## One thought on “High-Quality Chaos”

1. ![](https://secure.gravatar.com/avatar/f297613e7cf2b450b9deb2551964574d6598c73e8b0897f30001918adfc94ef1?s=34&d=monsterid&r=g) **Mats Lundgren** says:

   [April 22, 2026 at 18:36](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/#comment-27429)

   Well written Daniel.

   Mozilla recently published their findings after having access to Mythos and it shows a similar trend.

   They conclude with I believe a pretty positive note:
   ——-
   Encouragingly, we also haven’t seen any bugs that couldn’t have been found by an elite human researcher. Some commentators predict that future AI models will unearth entirely new forms of vulnerabilities that defy our current comprehension, but we don’t think so. Software like Firefox is designed in a modular way for humans to be able to reason about its correctness. It is complex, but not arbitrarily complex.

   The defects are finite, and we are entering a world where we can finally find them all.
   ——-
   Link:
   <https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/>

   [Reply](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/?replytocom=27429#respond)

### Leave a Reply [Cancel reply](/blog/2026/04/22/high-quality-chaos/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
5seven9sixeight

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/)
  April 22, 2026
* [Don’t trust, verify](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/)
  March 26, 2026
* [One hundred weirdo emails](https://daniel.haxx.se/blog/2026/03/25/one-hundred-weirdo-emails/)
  March 25, 2026
* [NTLM and SMB go opt-in](https://daniel.haxx.se/blog/20...