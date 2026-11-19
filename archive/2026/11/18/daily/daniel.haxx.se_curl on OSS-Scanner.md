---
title: curl on OSS-Scanner
url: https://daniel.haxx.se/blog/2026/11/18/curl-on-oss-scanner/
source: daniel.haxx.se
date: 2026-11-18
fetch_date: 2026-11-19T09:46:02.314211
---

# curl on OSS-Scanner

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/09/bug-insect-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl on OSS-Scanner

[November 18, 2026](https://daniel.haxx.se/blog/2026/11/18/curl-on-oss-scanner/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/11/18/curl-on-oss-scanner/#comments)

> [OSS Scanner](https://github.com/anthropics/oss-scanner/) is a service by Anthropic to scan critical open-source repositories for security vulnerabilities

## Enrollment

curl maintainer Max Dymond submitted [pull-request 1191](https://github.com/anthropics/oss-scanner/pull/1191) to OSS-Scanner in the end of October and we were swiftly enrolled into the program.

The idea for this service is inspired by [OSS-Fuzz](https://oss-fuzz.com/): Anthropic scans the participating open source projects for security problems on their machines at some interval with their magic applied and they let us know if they find anything. I don’t think they officially say exactly which model they use for this nor how often they rescan.

## First contact

Early in the morning of November 5 we received our first sign of life from them since they merged the PR. An automated mail:

```
Subject: [Anthropic OSS Scanner] Disclosing 45 security vulnerabilities in curl
```

Forty-five security vulnerabilities in a single shot is *a lot*. But sure, we did ask them to do this.

Of course, had we not asked them, chances are someone else would instead have figured these ones out and reported to us separately. There are many people with capable harnesses and AI models out there.

The Anthropic email with all the findings described that the analysis considers one of the flaws to be severity MEDIUM and the remaining 44 at severity LOW. In addition, they also found 23 *ordinary bugs* that are also included in the report.

The ordinary bugs they reported have not yet been analyzed. This blog post focuses on the 45 reported claimed *vulnerabilities.*

## The findings

In this large tarball we got individual markdown reports for each finding, together with their associated reproducers and in many cases also their suggested patches for mitigation.

With a little scripting and lots of manual fiddling, I submitted all these reports as individual issues on GitHub following [our new policy](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/). I paced myself and did this over a period of several days to soften the impact this had on the team.

Each report [starts in ASSESS](https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/) mode and once it has been given proper attention we move it to a suitable severity level or we set it to NONE if there is no vulnerability at all there.

You can [view all the issues yourself](https://github.com/curl/curl/issues?q=is%3Aissue+ANT-2026).

## Raising what a LOW is

In the curl project we have decided to gradually raise the requirements for severity LOW vulnerabilities. Issues that seem too ridiculous or unlikely we now set to NONE to a larger extent than we have in the past. As *just a bug* as we like to call them.

With this in mind, curl maintainers worked fiercely on the reports of the coming days until we had reached an initial verdict for all the 45 reports – and in the mean time we also received a few additional reports submitted by other reporters.

## Finding distribution

The severity MEDIUM finding we consider to be a LOW and we also agreed with an additional four findings, thus landing on five (11.1%) confirmed.

36 of the 45 findings we consider *just bug*s, three of them were not even bugs while one of the findings was *completely wrong*. The wrong one insisted the issue in the complete opposite way and claimed we should patch away our proper way to instead do it the AI’s suggested inferior way – which would introduce the vulnerability it warned for.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/11/chart6.png)

## Vulnerability rate

The 11% vulnerability confirm rate is lower than the average in vulnerability reports we have seen in 2026 but the 80% *just a bug* share is a *much higher* rate than ordinary reports. The average share of vulnerability reports that report “just a bug” has been at about 43% earlier during this year.

Combined, a conclusion must land on that these reports have high quality, but are way too eager to call them vulnerabilities. This should also be seen with the understanding that we as a project have shifted slightly and have higher requirements now.

## Language

One of the most annoying things with AI generated reports in general is the length of the reports and these ones are no exceptions.

It feels like an unwritten law that they *must* produce very long texts and it feels like the reports are always excessively long no matter the complexity of the issue it reports. In that regard, human reports still easily outperform the AIs’.

## Proposed patches

Several of these findings contain proposed patches for the identified issues. In some instances they have been almost exactly what were necessary, but more commonly the fixing took human effort to analyze the (too) long report and write up the fix for it.

Since 41 out of the 45 findings identified problems, we got our hands full. At the time of this writing, eleven of the reported bugs are still not addressed.

## Bugs never experienced

When an AI finds a bug, they tend to identify problems that no user ever ran into. Users typically report problems when they do something and curl then does something unexpected or it somehow doesn’t satisfy the user’s wishes. In these findings, the reported problems are more *theoretical*. In many cases this makes the reports less important, and sometimes unlikely to cause problems in real world use cases.

## Future

We willingly joined this effort as getting flaws and bugs reported helps us improve curl.

However, since the severity levels of the findings are of this, shall we say *trivial*, kind, it feels reasonable to reconsider our participation if this keeps up.

## You can help

Part of the idea of making more vulnerability reports public early is to make it possible for everyone to join in and help. Provide your comments and views on reports still in ASSESS. Submit your proposed changes as pull-requests, or help review changes proposed by others. Help review the advisories for confirmed vulnerabilities to make sure the descriptions make sense and are accurate and that we figure out exactly when they were introduced etc.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostThe curl 30 years gource](https://daniel.haxx.se/blog/2026/11/18/the-curl-30-years-gource/)

## One thought on “curl on OSS-Scanner”

1. ![](https://secure.gravatar.com/avatar/e3728bb535d8309361a2e541df14e3383d9e946cf97417a14e0ae3bbed09daf0?s=34&d=monsterid&r=g) **Willy** says:

   [November 18, 2026 at 12:00](https://daniel.haxx.se/blog/2026/11/18/curl-on-oss-scanner/#comment-27598)

   Hi Danel!

   That confirms to me what I expected from this service, i.e. nothing. I thought for a minute or two to register haproxy there until I read the CLA which looks like an abomination (i.e. you grant them perpetual rights to everything you have, that doesn’t even match licenses).

   [Reply](https://daniel.haxx.se/blog/2026/11/18/curl-on-oss-scanner/?replytocom=27598#respond)

### Leave a Reply [Cancel reply](/blog/2026/11/18/curl-on-oss...